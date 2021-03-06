from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.
def index(request):
    #return HttpResponse ('Hello from Post')

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, 'post/index.html', context)

def details(request, id):
#      return HttpResponse(f'details with the id number {id}')
    post = Posts.objects.get(id=id)

    context = {
    'post': post
    }

    return render(request, 'post/details.html', context)
