from django.shortcuts import render, redirect
from .forms import Contactform
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = Contactform()

    if request.method == "POST":
        contact_form = Contactform(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get("your_name")
            email = request.POST.get("your_email")
            comentary = request.POST.get("comentary")

            mail = EmailMessage("Message from DjangoApp", "{} has sent you a message from {}\n\nThe message:\n\n{}".format(name, email, comentary),"", ["martinsanchezdavid27@gmail.com"], reply_to=[email])

            try:
                email.send()
                
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?novalid")


    return render(request, "contact/contact.html", {'myform': contact_form})