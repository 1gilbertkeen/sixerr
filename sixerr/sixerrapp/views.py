from django.shortcuts import render

# Create your views here.
def home(request):
    return render( request,  'home.html', {})

def project_detail(request, id):
    return render( request, 'project_detail.html', {})