import re
import smtplib

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages

from django.core.mail import send_mail
from email.mime.text import MIMEText

# Create your views here.
def index(request):
    return render(request, "boat_app/index.html")

def contact(request):
    if 'form' not in request.session:
        request.session['form'] = {}

    context = {
        'form' : request.session['form']
    }
    return render(request, "boat_app/contact.html", context)

def submit_contact_form(request):
    form = {
        'f_name': request.POST['f_name'],
        'l_name': request.POST['l_name'],
        'email': request.POST['email'],
        'phone': request.POST['phone'],
        'message': request.POST['message']
    }
    request.session['form'] = form
    email_match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', form['email'])

    phone_match = re.match('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', form['phone'])

    if len(form['f_name']) < 2 or len(form['l_name']) < 2:
        messages.add_message(request, messages.INFO, 'First and Last Name must be at least 2 characters')

    if not email_match:
        messages.add_message(request, messages.INFO, 'Not a valid email address')

    print "****** {} *******".format(form)
    if form['phone'] and not phone_match:
        messages.add_message(request, messages.INFO, 'Not a valid phone number - (e.g. XXX-XXX-XXXX)')

    if not form['message']:
        messages.add_message(request, messages.INFO, 'Please enter a message to be sent')

    if get_messages(request):
        return redirect('/contact')

    # # Create a text/plain message
    # msg = MIMEText(form['message'])
    #
    # # me == the sender's email address
    # # you == the recipient's email address
    # msg['Subject'] = 'The contents of %s' % msg
    # msg['From'] = form['email']
    # msg['To'] = 'ambrosecoc@gamil.com'
    #
    # # Send the message via our own SMTP server, but don't include the
    # # envelope header.
    # s = smtplib.SMTP('localhost:8000')
    # s.sendmail(form['email'], ['ambrosecoc@gamil.com'], msg.as_string())
    # s.quit()
    # send_mail(
    #     'Subject here',
    #     form['message'],
    #     'ambrosecoc@gmailcom',
    #     ['ambrosecoc@gmail.com'],
    #     fail_silently=False,
    # )

    return redirect('/contact')

def test(request):
    return render(request, "boat_app/test.html")
