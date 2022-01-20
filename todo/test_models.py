"""
test that our todo items will be created
by default with the done status of false.
"""
from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        # To confirm that it's done status is in fact, false by default
        self.assertFalse(item.done)
    

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        #confirm that this name is returned when we render this item as a string
        self.assertEqual(str(item), 'Test Todo Item' )
        
