from django.contrib.auth.forms import UserCreationForm
from django import forms
from letsparty.models import Partier, Event, Address

__author__ = 'Michael'

class EmailUserCreationForm(UserCreationForm):
    username = forms.RegexField(label="Username", max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only.",
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")}, widget=forms.TextInput(attrs={'placeholder': 'michaelp'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'example@example.com'}))

    class Meta:
        model = Partier
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                Partier.objects.get(username=username)
            except Partier.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )

class NamedUserCreationForm(EmailUserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Michael'}))
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder': 'Perret'}))
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': '2345678989'}))
    class Meta:
        model = Partier
        fields = ("username", "email", "first_name", "last_name", "password1", "password2", "phone")


# Why aren't you using model forms below for these? This will clean up your views that save these forms.
class EventCreationForm(forms.Form):
    title = forms.CharField(max_length=40)
    date = forms.CharField(max_length=30)
    location = forms.ModelChoiceField(queryset=Address.objects.all())
    guests = forms.CharField(max_length=1000,help_text='Phone numbers only please. Separated by a comma and a space.')
    # creator = forms.ChoiceField(Partier.objects.all())

class AddressCreationForm(forms.Form):
    title = forms.CharField(max_length=100, help_text="We save all your addresses so you don't have to type them again!")
    street = forms.CharField(max_length=160, help_text="ex: 225 Maiden Ln")
    city = forms.CharField(max_length=160, help_text="ex: San Francisco")
    state = forms.CharField(max_length=2,help_text="ex: CA")
    zipcode = forms.CharField(max_length=5,help_text="ex: 94019")
