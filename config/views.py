from django.http import HttpResponse
def xss(request):
    return render(request, 'xss.html')