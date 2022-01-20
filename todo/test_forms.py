from django.test import TestCase
from .forms import ItemForm

"""
 we're now testing that the form is not valid. The error occurred on the name
field and the specific error message is what we expect
"""
class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        form = ItemForm({'name':''})
        # When the form is invalid it should also send back a dictionary of fields on which
        # there were errors and the Associated error messages
        self.assertIn('name', form.errors.keys())
        self.assertFalse(form.is_valid())
        """
        we're using the zero index here because the form will return a list of errors on each field.
        And this verifies that the first item in that list is our string telling us the field is required.
        """
        self.assertEqual(form.errors['name'][0], 'This field is required.')
    

    def test_done_field_is_not_required(self):
        """
        create the form sending only a name.
        And then just test that the form is valid 
        as it should be even without selecting a done status.
        """
        form = ItemForm({'name':'Test Todo Item'})
        self.assertTrue(form.is_valid())


    """
    a test to ensure that the only fields that are displayed in
    the form are the name and done fields.
    This will ensure that the fields are defined explicitly.
    
    """
    def test_fields_are_explicit_in_form_metaclass(self):
        # initiate an empty form
        form = ItemForm()
        """
        to check whether the form.meta.fields attribute
        is equal to a list with name and done in it.
        And if someone changes the item model down the road our form won't
        accidentally display information we don't want it to.
        This will also protect against the fields being reordered.
        Since the list must match exactly.
        """
        self.assertEqual(form.Meta.fields, ['name', 'done'] )
