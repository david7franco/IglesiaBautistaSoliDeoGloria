from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
# Create your views here.
def main_page(request):
    return render(request, "churchApp/main_page.html", {})

def success(request):
    return render(request, "churchApp/success.html")

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            name = form.cleaned_data['Nombre']
            email = form.cleaned_data['Correo Electrónico']
            contact_block = form.cleaned_data['Mensaje']
            #needs to still implement insert data to db
    else:
        # Display the form for initial page load
        form = ContactForm()

    return render(request, "churchApp/contact.html", {'form': form})

def donation(request):
    return render(request, 'churchApp/donate.html')

def process_donation(request):
    if request.method == 'POST':
        # Process the donation here (e.g., save to the database, integrate with a payment gateway, etc.)

        return HttpResponse('Method not allowed', status=405) # database not setup yet, redirecting to a HttpResponse
        #return redirect('thank_you')
    else:
        # Handle GET requests (direct access to the URL)
        return HttpResponse('Method not allowed', status=405)

def thank_you(request):
    return HttpResponse('Thank you for your donation!')

def about_us(request):
    return render(request, 'churchApp/about_us.html')