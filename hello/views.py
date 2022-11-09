from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, BSIT 4C!")

def test(request):
    return HttpResponse("<a href='#'>link</a>")
