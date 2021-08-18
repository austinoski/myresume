from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import ContactResponse


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contact_response = ContactResponse.objects.create(**form.cleaned_data)
        contact_response.save()
        messages.add_message(
            request, messages.SUCCESS, 'Your response has been saved successfully. Thank you!'
        )
        return redirect(reverse_lazy('home'))
    else:
        messages.add_message(
            request, messages.INFO, 'Something went wrong, please retry.'
        )
        return redirect(reverse_lazy('home'))