from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    print("=== Httprequest Information ===")
    print(f"method: {request.method}")
    print(f"Path: {request.path}")
    print(f"Full Path: {request.get_full_path()}")
    print(f"Scheme: (request.scheme)")
    print(f"Host: {request.get_host()}")
    print(f"User Agent: {request.META.get ('HTTP_USER_AGENT','')}")
    print(f"Remote Address: {request.META.get('REMOTE_ADDR')}")
    print(f"GET Parameters: (request.GET)")
    print(f"POST Data: (request. POST)")
    print(f"Cookies: (request.COOKIES)")
    print(f"Headers:")
    for header, value in request.headers.items():
        print(f"{header}: {value}")
    response = HttpResponse('Blog Home')
    if request.method == 'POST':
        print('name: ', request.POST.get('name'))
        print('password: ', request.POST.get('password'))
        name = request.POST.get('name')
        return HttpResponse(f'Hello, {name}')
return render(request, '/Users/sunflower/Desktop/wa/webdev/myysite/blog/templates/blog/home.html')