from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    To tell the form which model it's going to be associated with.
    We need to provide an inner class called meta.
    This inner class just gives our form some information about itself
    such as how it should display errors.
    """
    class Meta:
        model = Item
        fields = ['name', 'done']
