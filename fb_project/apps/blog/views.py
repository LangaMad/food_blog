from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoryListView(ListView):
    template_name = 'category_list'
    model = Category
    queryset = Category.objects.all()


# def get_categories(request):
#     categories = Category.objects.all()
#     context = {
#         'catigories':categories
#     }
#     return render(request,'category_list.html', context)



class PostListView(ListView):
    template_name = 'post_list'
    model = Post
    queryset = Post.objects.filter(is_draft=False)


