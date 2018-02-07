# blog/views.py
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.all()  # 이 시점에는 DB 액세스가 이루어 지지 않음 

    q = request.GET.get('q', '')  # q가 있는경우 가져오고, 없는 경우  ''(빈 문자열) 반환
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q': q,
    })  # appname/html 이름


def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)  # post.get_absolute_url() => post_detail
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)  # post.get_absolute_url() => post_detail
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })