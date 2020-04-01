from home.models import Post, Tag
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from home.forms import *
from django.db.models import Q
from django.views.generic import View
from django.core.paginator import Paginator


def page_home(request):
    return render(request, 'home_page.html')


# def view_home(request):
#     query = request.GET.get('search', '')
#     if query:
#         posts = Post.objects.filter(Q(title__icontains=query) | Q(post__icontains=query))
#     else:
#         posts = Post.objects.all()
#
#     context = {
#         'posts': posts
#     }
#     return render(request, 'home/view_home.html', context)
#

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            form.instance.user = request.user
            comment.save()
            return redirect('home:post-detail', pk=post.id)
    else:
        form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'home/add_comment.html', context)


def posts_view(request):
    posts = Post.objects.all().order_by('-created')
    tags = Tag.objects.all()
    paginator = Paginator(posts, 4)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'tags': tags
    }
    return render(request, 'home/posts.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            context = {
                'post': post,
                'form': form
            }

            return render(request, 'home/post_detail.html', context)

    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'home/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('home:blog-home')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'home/post_create.html', context)


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':

        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():

            post.title = form['title'].value()
            post.post = form['post'].value()
            post.save()

            return redirect('home:blog-home')
    else:
        form = PostUpdateForm(instance=post)

    context = {
        'form': form,
    }

    return render(request, 'home/post_update.html', context)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect('home:blog-home')


def user_posts(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(user=user).order_by('-created')
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'home/user_posts.html', context)


def tags_list(request):
    context = {
        'tags': Tag.objects.all()
    }
    return render(request, 'home/tags_list.html', context)


def tag_detail(request, slug):
    tag = Tag.objects.get(slug=slug)
    context = {
        'tag': tag
    }
    return render(request, 'home/tag_detail.html', context)

