from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class IndexView(ListView):
    template_name = 'index.html'
    model = Category
    queryset = Category.objects.all()
    context_object_name = "categories"


class CategoryListView(ListView):
    template_name = 'category_list.html'
    model = Category
    queryset = Category.objects.all()
    context_object_name = "categories"



#
# def get_categories(request):
#     categories = Category.objects.all()
#     context = {
#         'categories':categories
#     }
#     return render(request,'category_list.html', context)
# #


class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    queryset = Post.objects.filter(is_draft=False)
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) < 4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()

        return context

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            qs = Post.objects.filter(is_draft=False, category__slug=category_slug)
            return qs
        return Post.objects.filter(is_draft=False)


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_post = Post.objects.filter(is_draft=False)
        if len(latest_post) < 5:
            context['latest_post'] = latest_post
        else:
            context['latest_post'] = latest_post[:5]

        context['categories'] = Category.objects.all()

        return context


class ProfileView(DetailView):
    template_name = 'profile.html'
    model = Post
    queryset = Post.objects.all()













