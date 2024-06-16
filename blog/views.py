from django.shortcuts import render

from blog.data import posts


def blog(request):
    print('blog')
    
    context = {
        'posts': posts,
    }
    
    return render(request, 'blog/index.html', context)

def exemplo(request):
    print('exemplo')
    
    context = {
        'text': 'Olá blog',
        'title': 'Essa é uma página de exemplo - ',
    }
    
    return render(request, 'blog/exemplo.html', context)

