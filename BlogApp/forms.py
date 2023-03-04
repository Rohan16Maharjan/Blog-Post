from django.forms import ModelForm
from .models import Contact

# Create the form class.
class ContactForm(ModelForm):
  class Meta:
        model = Contact
        fields = '__all__'


