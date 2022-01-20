from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
#  take an http request from the user and
# return an http response to the user that says hello.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        """
        Django will automatically compare the data submitted
        in the post request to the data required on the model.
        And make sure everything matches up.
        """
        if form.is_valid():
            # save our item
            form.save()
        return redirect('get_todo_list')
    # Create a context which contains the empty form.
    # And then return the context to the template.
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    # get instance of the item model
    """
    With an ID equal to the item ID that was passed into
    the view via the URL.This method will either return
    the item if it exists.Or a 404 page not found if not.
    we'll create an instance of our item form and
    return it to the template in the context.
    """
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # Telling it that it should be prefilled with the information
    # for the item we just got from the database
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


"""
toggle the item status and
redirect back to the to do list.
"""


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # flip to the opposite of what of whatever it is
    # if done status is true it will flip to false and vice versa
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
