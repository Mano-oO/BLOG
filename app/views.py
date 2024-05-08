from django.shortcuts import render
from .models import *
from .forms import *

from django.http import HttpResponse, JsonResponse

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            contents = form.contents(request.POST, instance=blog_post)
            if contents.is_valid():
                contents.save()

            
            blog_post_data = {
                'id': blog_post.id,
                'title': blog_post.title,
                'content': blog_post.content,
                'image_url': blog_post.image.url,
                'category': blog_post.category,
                'author': blog_post.author,
                'blog_contents': [],
            }

            for content_instance in blog_post.blogcontent_set.all():
                content_data = {
                    'subtitle': content_instance.subtitle,
                    'paragraph': content_instance.paragraph,
                    
                }
                blog_post_data['blog_contents'].append(content_data)

            return JsonResponse({'success': True, 'blog_post': blog_post_data})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = BlogPostForm()

    return render(request, 'blog_post.html', {'form': form})


def n1(request):
    posts = BlogPost.objects.all()

    context = {
        'section_title': "THE BLOGS YOU HAVE POSTED ",
        'section_description': "SCROLLDOWN",
        'posts': posts,
    }

    
    return render(request, "index.html",context)

def n2(request):
    
    return render(request, "photography.html")


def n4(request):
    if request.method == 'POST':
        form = ContactDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data added successfully')
        else:
            return HttpResponse(form.errors)
    else:
        form = ContactDetailForm()
    return render(request, 'contact.html' ,{'form': form})
    

def n5(request):
    
    return render(request, "about.html")

def n6(request):
    
    return render(request, "single.html")

    
def n7(request):
    posts = BlogPost.objects.all()

    context = {
        'section_title': "THE BLOGS YOU HAVE POSTED ",
        'section_description': "SCROLLDOWN",
        'posts': posts,
    }
    return render(request, "travel.html",context)