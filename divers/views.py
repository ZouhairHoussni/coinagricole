from django.shortcuts import render
from .functions import multiplicable_by_5

weekdays = ['lundi','mardi','mercredi','jeudi','vendredi']
text = "Mia San Mia !! "
def home_view(request):
    
    context = {'test' : "This is a test",
    'multi8':multiplicable_by_5(8),
    'weekdays': weekdays}
    return render(request, 'divers/home_page.html',context=context)

def about_view(request):

    context = {
        'text': text
    }


    return render(request,'divers/about_page.html',context=context)