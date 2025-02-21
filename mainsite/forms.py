from django import forms
from django.utils.translation import gettext_lazy as _

class DoacaoAlimentoForm(forms.Form):
    
    class Meta:
        fields = '__all__'

    name = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "dummy",
                "aria-describedby": "instituicao",
            }
        ), label=_('Insira seu nome:')
    )
    email = forms.EmailField(
        required=True,
        max_length=80,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "dummy",
                "aria-describedby": "email",
            }
        ), label=_('Insira seu e-mail:')
    )
    phone = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "dummy",
                "aria-describedby": "telefone",
            }
        ), label=_('Insira seu telefone:')
    )

class IntercambioForm(forms.Form):
    
    class Meta:
        fields = '__all__'

    name = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "dummy",
                "aria-describedby": "nome",
            }
        ), label=_('Insira seu nome:')
    )
    email = forms.EmailField(
        required=True,
        max_length=80,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "dummy",
                "aria-describedby": "email",
            }
        ), label=_('Insira seu e-mail:')
    )
    phone = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "dummy",
                "aria-describedby": "telefone",
            }
        ), label=_('Insira seu telefone:')
    )