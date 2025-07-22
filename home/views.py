from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ContactMessage
from django.conf import settings
# Create your views here.

def homepage(request):
    return render(request, 'home/index.html')

def services_delivery(request):
    return render(request, 'services/delivery.html')

def storage_service(request):
    return render(request, 'services/storage.html')

def business_support(request):
    return render(request, 'services/business_support.html')

def contact_view(request):
    return render(request, 'contact.html')

def track_request(request):
    return render(request, 'track_request.html')


def about_values(request):
    return render(request, 'about/values.html')

def about_technology(request):
    return render(request, 'about/technology.html')

def about_academy(request):
    return render(request, 'about/academy.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the message in the database
        contact_msg = ContactMessage.objects.create(name=name, email=email, message=message)

        # Send an email notification
        subject = f"New Contact Message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # send to your own email
                fail_silently=False,
            )
            messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
        except Exception as e:
            messages.error(request, 'Error sending email. Please try again later.')

        return redirect('contact')
    else:
        return redirect('contact')