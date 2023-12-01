from django import forms
from .models import Product, Comment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'description', 'price']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class DeleteCommentForm(forms.Form):
    confirm_deletion = forms.BooleanField(
        required=True,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )