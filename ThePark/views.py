from django.http import HttpResponse

def account_information(request):
    pass;

def search_preferences(request):
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
