from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from blogs.models import Blog, Comments

# Create your views here.


class IndexView(View):
    def get(self, request):
        all_blogs = Blog.objects.all()
        return render(request, 'index.html', {
            "all_blogs": all_blogs,
        })


class BlogsView(View):
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        all_comments = Comments.objects.filter(blog=blog)
        return render(request, 'blog-detail.html', {
            "blog": blog,
            "all_comments": all_comments,
        })


class AddCommentsView(View):
    def post(self, request):
        blog_id = request.POST.get("blog_id", 0)
        comments = request.POST.get("comments", 0)
        if int(blog_id) > 0 and comments:
            blog_comments = Comments()
            blog = Blog.objects.get(id=blog_id)
            blog_comments.blog = blog
            blog_comments.comments = comments
            blog_comments.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "添加失败"}', content_type='application/json')


