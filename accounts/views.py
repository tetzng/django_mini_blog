from django.shortcuts import render, redirect
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# @login_required
# def index(request):
#   return render(request, 'accounts/top.html')

# def signup(request):
#   template_name = 'accounts/signup.html'
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('index')
#   else:
#     form = UserCreationForm()
#   context = {'form': form}
#   return render(request, template_name, context)

def signup(request):
  template_name = 'accounts/signup.html'
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
  else:
    form = SignUpForm()
  context = {'form': form}
  return render(request, template_name, context)