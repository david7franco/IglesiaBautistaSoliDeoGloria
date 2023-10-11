from django import forms


class ContactForm(forms.Form):
    Nombre = forms.CharField(max_length=100, label="Nombre")
    Email = forms.EmailField(label="Correo Electrónico")
    Mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)
