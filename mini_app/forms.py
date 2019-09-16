from django import forms
from .models import Article, Tag

class PostCreateForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'

  class Meta:
    model = Article
    fields = ['title','text']
    exclude = ('tags',)

PostCreateFormSet = forms.modelformset_factory(
  Article, form=PostCreateForm, extra=1
)

TagInlineFormSet = forms.inlineformset_factory(
  Article, Article.tags.through, fields='__all__', can_delete=False
)
