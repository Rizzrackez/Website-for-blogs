from home.models import Post, Tag
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import TagForm, CommentForm
from django.db.models import Q
from django.views.generic import View


# get all POST object


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
    context = {'form': form}
    return render(request, 'home/add_comment.html', context)


def page_home(request):
    return render(request, 'home/page_home.html')


def view_home(request):
    query = request.GET.get('search', '')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(post__icontains=query))
    else:
        posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'home/view_home.html', context)


# class CommentListView(ListView):
#     model = Comment
#     template_name = 'home/comment.html'
#     context_object_name = 'comments '
#
#
# class CommentDetailView(DetailView):
#     model = Comment
#
#
# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     fields = ['content']
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#
# def comments_list(request):
#     args = {'comments': Comment.objects.all()}
#     return render(request, 'home/comment.html', args)


class PostListView(ListView):

    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'home/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-created')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'post', 'tags']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'post', 'tags']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


def tags_list(request):
    args = {'tags': Tag.objects.all()}
    return render(request, 'home/tags_list.html', args)


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'home/tag_detail.html', context={'tag': tag})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'home/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'home/tag_create.html', context={'form': bound_form})



