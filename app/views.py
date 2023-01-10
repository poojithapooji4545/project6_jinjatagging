from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'pooji','age':23}
    return render(request,'jinja.html',d)