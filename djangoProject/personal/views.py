from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def personal(request):
#     return HttpResponse('details with the id number ')
    return render(request, 'personal/index.html')

def contact(request):
    return render(request, 'personal/contact.html')
