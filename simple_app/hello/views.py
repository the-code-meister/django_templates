from django.http import HttpResponse

def hello_view(request):
    html = "<html><body>Hello World</body></html>"
    return HttpResponse(html)
