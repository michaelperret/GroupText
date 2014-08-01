from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django_twilio.client import twilio_client
from letsparty.forms import NamedUserCreationForm, EventCreationForm, AddressCreationForm
from letsparty.models import Event, Address
from party import settings
from party import urls
from django.http import HttpResponse
from django_twilio.decorators import twilio_view
from twilio.twiml import Response

# Need to clean up the format of the file a bit, a lot of extra blank lines



def register(request):
    if request.method == 'POST':
        form = NamedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you for signing up for our website, {}. I hope you enjoy using my app! NOW LETS FUCKING PARTY!!'.format(user.first_name,user.date_joined)
            html_content = '<h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using my app!</div><br><em>NOW LETS FUCKING PARTY!!</em>'.format(user.first_name)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            twilio_client.sms.messages.create(to="+1" + user.phone, from_=settings.TWILIO_NUMBER, body='Thanks for signing up! Time to partayyyy!')
            return redirect("home.html")
    else:
        form = NamedUserCreationForm()



    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def home(request):
    data = {
        'parties': Event.objects.all()
    }
    return render(request, 'home.html', data)
# Create your views here.

@login_required
def create(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():

            # Would be better to make a save function on your custom form that does the following code
            # Then you can just call form.save() here like a ModelForm
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            location = form.cleaned_data['location']
            guests = form.cleaned_data['guests'].split(', ')
            creator = request.user
            if len(guests)> 0:
                for guest in guests:
                    twilio_client.sms.messages.create(to="+1"+guest, from_=settings.TWILIO_NUMBER, body="{} just invited you to his {} party at {} on {}".format(creator,title,location,date))

            Event.objects.create(title=title, date=date, location=location, creator=creator)
            twilio_client.sms.messages.create(to="+1" + creator.phone, from_=settings.TWILIO_NUMBER, body='You just created a {} party on {} at {}'.format(title,date,location))

            return redirect("/")
    else:
        form = EventCreationForm()
        return render(request, 'create.html', {'form': form})


@twilio_view
def sms(request):
    name = request.POST.get('Body', '')
    msg = 'Hey %s'

    r = Response()
    r.message(msg)
    return r


@login_required
def address(request):
    if request.method == 'POST':
        form2 = AddressCreationForm(request.POST)
        if form2.is_valid():
            title = form2.cleaned_data['title']
            street = form2.cleaned_data['street']
            city = form2.cleaned_data['city']
            state = form2.cleaned_data['state']
            zipcode = form2.cleaned_data['zip']
            Address.objects.get_or_create(title=title, street=street, city=city, state=state, zipcode=zipcode)

        return redirect("/")
    else:
        form2 = AddressCreationForm()
        return render(request, 'address.html', {'form': form2})

# message = twilio_client.sms.messages.create(to="+1" + phone, from_="+YOUR_TWILIO_NUMBER", body=bodytext)
