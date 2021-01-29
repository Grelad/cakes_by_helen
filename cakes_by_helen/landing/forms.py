from django.forms import ModelForm
from landing.models import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'phone', 'comment', 'type']

        error_messages = {
            'name': {
                'max_length': "Name is too long.",
            },
            'phone': {
                'max_length': "Phone number couldn't be more than 17 characters long.",
            },
            'comment': {
                'max_length': "Comment is too long.",
            },
        }
