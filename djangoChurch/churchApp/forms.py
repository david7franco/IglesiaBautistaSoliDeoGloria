from django import forms


class ContactForm(forms.Form):
    Nombre = forms.CharField(max_length=100, label="Nombre")

    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))    
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    Mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)
