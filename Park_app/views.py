from django.shortcuts import render
from django.http import HttpResponse
from ThePark.models import Account, Animal

def account_information(request, this_animal):
    if (request.method == "POST"):
        my_account = Account.objects.create(
            my_pet = this_animal;
            matches = []
        )
    return render(request, 'account_information.html', {'my_account':my_account})

def search_preferences(request):
    # Returns another account in the database that matches preferences of my_account
    pass;

def manage_matches(request):
    pass;

def new_offers(request):
    if (request.method == "GET"):
        pass
    elif (request.method == "POST"):

        # send GET request to self
        pass
    else:
        return HttpResponse("This ain't it, Chief.")
