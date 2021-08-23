from django.shortcuts import render

# Create your views here.
def content_html(request):
    return render(request,'content.html')