from django.test import TestCase
from .models import Item

# Create your tests here.
# To test the HTTP responses of the views.
# We can use a built-in HTTP client that comes with the Django testing framework.

class TestViews(TestCase):
    """
    Every test will be defined as a method that begins with the word test.
    Self here refers to our test Django class because it inherits the testcase class
    which has a bunch of pre-built methods and functionality that we can use.
    """
    def test_get_todo_list(self):
        # retrieve URL of homepage
        response = self.client.get('/')
        # confirm a successful HTTP response
        self.assertEqual(response.status_code, 200)
        # confirm the view uses the correct template
        self.assertTemplateUsed(response, 'todo/todo_list.html')
    
    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')
    

    def test_get_edit_item_pagt(self):
        # create an item for the test
        item = Item.objects.create(name='Test Todo Item')
        # add an f before the opening quotation mark.
        # And then anything we put in curly brackets
        # will be interpreted and turned into part of the string
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        response = self.client.post('/add', {'name':'Test Added Item'})
        self.assertRedirects(response, '/')


    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # prove that the item is in fact deleted
        existing_items = Item.objects.filter(id=item.id)
        # We can be certain the view works by asserting 
        # whether the length of existing items is zero.
        self.assertEqual(len(existing_items), 0)


    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        # use assert false to check it's done status
        self.assertFalse(updated_item.done)

    
    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        # the updated items name is equal to updated name using assertEqual
        self.assertEqual(updated_item.name, 'Updated Name')

