from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "titulo_post", "autor", "cuerpo")

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Este sera el titulo de tu post",
                }
            ),
            "titulo_post": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Este sera el titulo de la pestaña",
                }
            ),
            "autor": forms.Select(
                attrs={"class": "form-control", "placeholder": "Tu nombre"}
            ),
            "cuerpo": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Comparte tus ideas!!!"}
            ),
        }
