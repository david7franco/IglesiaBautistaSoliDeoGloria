from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.conf import settings
# Create your views here.
def main_page(request):
    return render(request, "churchApp/main_page.html", {})

def success(request):
    return render(request, "churchApp/success.html")

def sermons(request):
    return render(request, "churchApp/sermons.html")

#contact page

def contact(request):
    thank_you_message=None
    if request.method == 'POST':
        # Handle form submission
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            name = form.cleaned_data['Nombre']
            email = form.cleaned_data['Email']
            contact_block = form.cleaned_data['Mensaje']
            thank_you_message = "Thank you for your submission!"
    else:
        # Display the form for initial page load
        form = ContactForm()

    return render(request, "churchApp/contact.html", {'form': form, 'thank_you_message': thank_you_message})

#donation page
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

#functions for about us and showing the letter 
def about_us(request):
    show_letter = request.GET.get('show_letter', False)
    return render(request, 'churchApp/about_us.html', {'show_letter': show_letter})

def toggle_letter(request):
    show_letter = not request.GET.get('show_letter', False)
    if show_letter:
        return render(request, 'churchApp/letter.html')  # Render the 'letter.html' template
    else:
        return redirect('about_us')
    