from django import forms
from django.forms import TextInput

class CrearPostFormulario(forms.Form):

    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 700px;', 'class': 'form-control'}))
    # date = forms.DateField()
    body = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 700px; height: 300px', 'class': 'form-control'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 700px;', 'class': 'form-control'}))
    #posiblemente estos tendrían que cargarse solos como date
    author = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 700px;', 'class': 'form-control'}))
    image = forms.ImageField(required=None)

class ComentarPosts(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 300px; ', 'class': 'form-control'}))
    body_comment = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 300px; height: 100px', 'class': 'form-control'}))