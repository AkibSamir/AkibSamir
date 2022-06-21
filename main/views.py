from django.http import request
from django.core.paginator import Paginator
from django.db.models import Q 
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib import messages
from main.forms import ContactModelForm
from .models import About, BlogPost, Certification, Contact, Education, Portfolio, Skills, Tag, Category

# Create your views here.
def index(request):
    skills = Skills.objects.all()
    context = {
        'skills':skills,
    }
    return render(request, 'index.html', context=context)


def resume(request):
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    context = {
        'educations':educations,
        'certifications':certifications,
        
    }
    return render(request, 'resume.html', context=context)

def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios':portfolios,
       
    }
    return render(request, 'portfolio.html', context=context)

def portfolio_single(self, pk):
    portfolios = Portfolio.objects.get(id=pk)
    context = {
        'portfolios':portfolios,
    }
    return render(request, 'portfolio-details.html', context=context)


def about(request):
    abouts = About.objects.all()
   
    context = {
        'abouts':abouts,
        
    }
    return render(request, 'about.html', context=context)

def contact(request):
    contacts = Contact.objects.all()
    forms = ContactModelForm()
    if request.method == "POST":
        forms = ContactModelForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')
        
    context = {
        'contacts':contacts,
        'forms':forms,
        
    }
    return render(request, 'contact.html', context=context)


def blog(request):
    categoryId = request.GET.get('category')
    tagId = request.GET.get('tag')     
    if 'search' in request.GET:
        search = request.GET['search'] 
        posts = BlogPost.objects.filter(
            Q(title__icontains=search)|
            Q(category__name__icontains=search)|
            Q(tags__name__icontains=search)
            ).distinct()
    elif categoryId:
        posts = BlogPost.objects.filter(category = categoryId)
    elif tagId:
        posts = BlogPost.objects.filter(tags = tagId)
    else: 
        # If not searched, return default posts
        posts = BlogPost.objects.all().order_by("-created_on")

    categories = Category.objects.all().annotate(posts_count=Count('blogpost'))
    tags = Tag.objects.all()       
    post_list = BlogPost.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    totalpage = posts.paginator.num_pages

    context = {
            'posts': posts,
            'categories': categories,
            'tags': tags,
            'post_list':post_list,
            'total_page': [n+1 for n in range(totalpage)],
            'page_number': int(page_number),
       
        
        }
    return render(request, 'blog.html', context=context)


# def search_post(request):
#     search = request.GET.get('search') 
#     if search in request.GET:
#         posts = BlogPost.objects.filter(
#             Q(title__icontains=search) | 
#             Q(category__icontains=search)|
#             Q(tags__icontains=search)
#             )
#         context = {
#         'posts':posts,  
#         }
        
#         return render(request, 'blog.html', context=context)
#     else:
#        posts = BlogPost.objects.all().order_by("-created_on")

#        context={
#         'posts':posts,
#        }

#        return render(request, 'search.html', context=context)
    

def blog_single(request, pk):
    posts = BlogPost.objects.get(id=pk)
    categories = Category.objects.all().annotate(posts_count=Count('blogpost'))
    post_list = BlogPost.objects.all().order_by('-created_on')
    tags = Tag.objects.all()
    context = {
        'posts':posts,
        'categories': categories,
        'post_list':post_list,
        'tags': tags,
    }
    return render(request, 'blog-single.html', context=context)