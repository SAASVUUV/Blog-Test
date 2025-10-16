from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


def get_date(post):
    return post.get('date')


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blogs/index.html",{
#         "posts": latest_posts
#     })

class StartinPageView(ListView):
    template_name = "blogs/index.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("-date")[:3]
        return data



class AllPostsView(ListView):
    template_name = "blogs/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"



# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blogs/all-posts.html", {
#         "all_posts": all_posts
#     })




class SinglePostView(View):
    template_name = "blogs/post-detail.html"
    model = Post

    def get(self, request, slug):
        post= Post.objects.get(slug=slug)
        context = {
            "post":post,
            "pos_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blogs/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post= Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post":post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all()
        }
        return render(request, "blogs/post-detail.html", context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
    




# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, "blogs/post-detail.html", {
#         "post": post,
#         "post_tags":post.tags.all()
#     })