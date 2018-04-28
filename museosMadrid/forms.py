from django import forms
form .models import Comentario

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('autor', 'texto')
