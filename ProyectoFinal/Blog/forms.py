from django import forms

class CrearPostFormulario(forms.Form):

    title = forms.CharField()
    # date = forms.DateField()
    body = forms.CharField()
    tags = forms.CharField()
    #posiblemente estos tendrían que cargarse solos como date
    author = forms.CharField()
    #comments = forms.CharField()

class ComentarPosts(forms.Form):
    user = forms.CharField()
    body_comment = forms.CharField()