from django import forms

def formClass(placeHolder):
    return {'class': 'form-control mt-1', 'placeholder': placeHolder }

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs=formClass('Nombre')), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs=formClass('Email')), min_length=3, max_length=100)
    subject = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(attrs=formClass('Asunto')), min_length=3, max_length=100)
    message = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs=formClass('Mensaje')), min_length=15, max_length=1000)