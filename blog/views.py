from django.shortcuts import render

posts = [
    {
        'author': 'FrancoFT',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'FrancoFT',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)
