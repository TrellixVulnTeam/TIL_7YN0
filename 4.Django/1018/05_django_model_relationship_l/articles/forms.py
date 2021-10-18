from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('title', 'content',)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = 
        exclude = ('article','user',)  # 없앴다고 해결된건 아님. 다른 방법으로 참조할 pk 가져와야 한다.
        