from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView

# Create your views here.
def main_page(request):
    return render(request, "churchApp/main_page.html", {})

def success(request):
    return render(request, "churchApp/success.html")

def sermons(request):
    return render(request, "churchApp/sermons.html")



#contact page
class ContactView(FormView):
    thank_you_message=None
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact")
    
    def form_valid(self, form):
        name = form.cleaned_data['Nombre']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        contact_block = form.cleaned_data['Mensaje']
        thank_you_message = "Thank you for your submission!"

        full_message = f""" 
        Recieved message below from 
        {name}, {email}, {subject},

        --------------------------------------

        {contact_block} 
        """

        send_mail(
        subject="Received contact form submission",
        message=full_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.NOTIFY_EMAIL],
    )
        return super(ContactView, self).form_valid(form)

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
    