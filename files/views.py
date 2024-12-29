from django.http import HttpResponse

def destinations(request):
    print("My request: ", request)
    return HttpResponse("My Destinations")
