from django.http import HttpResponse

def first_view(request):
    return HttpResponse("Hello! Start of Django!")

def xss(request):
    return render(request, 'xss.html')