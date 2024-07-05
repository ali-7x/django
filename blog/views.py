from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404
# Create your views here.
def inh(request):
    return render(request, 'inh.html')
def bas(request):
    return render(request, 'bas.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request,id):
    # method 1
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("haaaah404")
    # return render(request, 'blog/post/detail.html',{'post':post})
    # method 2
    post = get_object_or_404(Post,id=id,status=Post.Status.Published)
    return render(request,'blog/post/detail.html' , {'post':post})