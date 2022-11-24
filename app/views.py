from django.shortcuts import render

def app_view(request):
    return render(request,'app/app_page.html')