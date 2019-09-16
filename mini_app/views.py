from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.http.response import JsonResponse
from django.http import HttpResponse
from . import models
from .forms import PostCreateForm, PostCreateFormSet, TagInlineFormSet
from .models import Article

# Create your views here.
def index(request):
  template_name = "mini_app/index.html"
  return render(request, template_name)

def new(request):
  template_name = "mini_app/new.html"
  form = PostCreateForm(request.POST or None)
  context = {'form': form}
  if request.method == 'POST' and form.is_valid():
    post = form.save(commit=False)
    formset = TagInlineFormSet(request.POST, instance=post)
    if formset.is_valid():
      post.author_id = request.user.id
      post.save()
      formset.save()
      return redirect(article_all)
    else:
      context['formset'] = formset
  else:
    context['formset'] = TagInlineFormSet()
  return render(request, template_name,context)

def article_all(request):
  template_name = "mini_app/article_all.html"
  context = {"articles":models.Article.objects.order_by('posted_at')}
  return render(request,template_name,context)

def view_article(request,pk):
  template_name = "mini_app/view_article.html"
  try:
    article = models.Article.objects.get(pk=pk)
  except models.Article.DoesNotExist:
    raise Http404
  if request.method == "POST":
    models.Comment.objects.create(text=request.POST["text"],article=article)
  context = {"article":article}
  return render(request,template_name,context)

def edit(request,pk):
  template_name = "mini_app/edit.html"
  try:
    article = models.Article.objects.get(pk=pk)
  except models.Article.DoesNotExist:
    raise Http404
  form = PostCreateForm(request.POST or None, instance=article)
  formset = TagInlineFormSet(request.POST or None, instance=article)
  if request.method == 'POST' and form.is_valid() and formset.is_valid():
    form.save()
    formset.save()
    return redirect(view_article, pk=pk)
  context = {
    'form': form,
    'formset': formset
  }
  return render(request,template_name,context)

def delete(request,pk):
  try:
    article = models.Article.objects.get(pk=pk)
  except models.Article.DoesNotExist:
    raise Http404
  article.delete()
  return redirect(article_all)

def like(request,pk):
  try:
    article = models.Article.objects.get(pk=pk)
  except models.Article.DoesNotExist:
    raise Http404
  article.like += 1
  article.save()
  return redirect(view_article,pk)

def api_like(request, pk):
  try:
    article = models.Article.objects.get(pk=pk)
  except models.Article.DoesNotExist:
    raise Http404
  article.like += 1
  article.save()
  return JsonResponse({"like":article.like})

def add(request):
  form = PostCreateForm(request.POST or None)
  context = {'form': form}
  if request.method == 'POST' and form.is_valid():
    post = form.save(commit=False)
    formset = TagInlineFormSet(request.POST, instance=post)
    if formset.is_valid():
      post.save()
      formset.save()
      return redirect(index)
    else:
      context['formset'] = formset
  else:
    context['formset'] = TagInlineFormSet()

  return render(request, 'mini_app/add.html', context)

def update_post(request, pk):
  template_name = "mini_app/update_post.html"
  post = get_object_or_404(Article, pk=pk)
  form = PostCreateForm(request.POST or None, instance=post)
  formset = TagInlineFormSet(request.POST or None, instance=post)
  if request.method == 'POST' and form.is_valid() and formset.is_valid():
    form.save()
    formset.save()
    return redirect(update_post, pk=pk)
  context = {
    'form': form,
    'formset': formset
  }
  return render(request,template_name,context)

def view_tag(request,pk):
  template_name = "mini_app/view_tag.html"
  try:
    tag = models.Tag.objects.get(pk=pk)
    articles = tag.article_set.all()
  except models.Tag.DoesNotExist:
    raise Http404
  context = {"tag": tag, "articles": articles.order_by('posted_at')}
  return render(request,template_name,context)