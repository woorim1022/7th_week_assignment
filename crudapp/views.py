from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
# Create your views here.
def home(request):
    blogs = Blog.objects     #쿼리셋
    return render(request, 'crudapp/home.html', {'blogs': blogs})
    #사전형 자료형
                                    #가져올 이름 #template에서 쓰는 변수

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'crudapp/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'crudapp/new.html')

def postcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
        else:
            return redirect('postcreate')
    else: 
        form = BlogForm()
        return render(request, 'crudapp/new.html', {'form': form})

def edit(request):
    return render(request, 'crudapp/edit.html')

def postupdate(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', blog_id=post.pk) # 수정한 글의 상세 페이지로 돌아간다
        else:
            return redirect('postupdate', blog_id=post.pk)
 

    else:
        form = BlogForm(instance=post) # post 객체에 이미 저장돼있는 것들을 form에 띄워둠
        return render(request, 'crudapp/edit.html', {'form': form})


def postdelete(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    post.delete() # Post DB에서 post 객체 삭제
    return redirect('home')