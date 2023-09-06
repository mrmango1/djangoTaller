from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    contactForm = ContactForm()
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get("name")
            from_email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            email = EmailMessage(
                subject,
                f"De: {name} <{from_email}> \n\n{message}",
                from_email,
                ("andersongrefa@gmail.com",)
            )
            try:
                email.send()
                return redirect(reverse("contact") + "?ok")
            except Exception as e: 
                print(e)
                return redirect(reverse("contact") + "?fail")

    return render(request, "contact.html", {'contactForm': contactForm})