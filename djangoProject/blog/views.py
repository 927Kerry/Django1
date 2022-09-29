from django.shortcuts import render
from django.http import HttpResponse
from .models import Post #. means from models file in same folder


# posts = [
#     {
#         'author': 'Stanlinic',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': '27th July, 2022'
#     },
#     {
#         'author': 'Stanlinic2',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': '23th July, 2022'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




# Create your views here.
