from django import forms
from home.models import Messagess
from product.models import Order


class ContactForm(forms.ModelForm):
    class Meta:
        model = Messagess
        fields = ( 'name', 'surname', 'email', 'phone',  'message',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ( 'name','surname','phone','amount','category', 'food', 'address',)