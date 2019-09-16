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


# class PostForm(forms.Form):
#   title = forms.CharField()
#   text = forms.CharField()
#   FORMA_INGRESSO_CHOICES = (
# ('AG','Agendado'),
# ('EN','Enem'),
# ('PR','Prova'),
# ('AC','Análise de Currículo'),
# ('RD','Redação'),
# ('VG','Vagas'),
# )
#   tags = forms.MultipleChoiceField(choices=FORMA_INGRESSO_CHOICES,)

# class ChkForm(forms.Form):
#     labels = ['チェック','複数チェック','ラジオボタン','動的選択肢１','動的選択肢２']
#     CHOICE = [
#           ('1','選択肢＜１＞'),
#           ('2','選択肢＜２＞'),
#           ('3','選択肢＜３＞')]
#     two = forms.MultipleChoiceField(
#           label=labels[1],
#           required=False,
#           disabled=False,
#           initial=[],
#           choices=CHOICE,
#           widget=forms.CheckboxSelectMultiple(attrs={
#               'id': 'two','class': 'form-check-input'}))
    #  labels = ['チェック','複数チェック','ラジオボタン','動的選択肢１','動的選択肢２']

    #  four = forms.MultipleChoiceField(
    #       label=labels[3],
    #       required=False,
    #       disabled=False,
    #       widget=forms.CheckboxSelectMultiple(attrs={
    #            'id': 'four','class': 'form-check-input'}))