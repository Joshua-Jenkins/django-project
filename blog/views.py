from django.shortcuts import render
# FAKE DATA
posts = [
    {
        'author': 'Joshua Jenkins',
        'title': 'blog post one',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Fred Doe',
        'title': 'blog post two',
        'content': 'First post content',
        'date_posted': 'August 28, 2018'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
