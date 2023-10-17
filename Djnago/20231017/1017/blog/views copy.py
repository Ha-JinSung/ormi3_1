from django.shortcuts import render
from .models import Post

def postlist(request):
    posts = Post.objects.all()
    # http://127.0.0.1:8000/blog/?q=hello
    # 공식문서 : https://docs.djangoproject.com/en/4.2/ref/request-response/
    print(request)
    print(dir(request))
    print(type(request))
    # 여기에서 출력되는것들은 templates에서도 출력 가능
    # {{request.user}}
    print(request.user)
    print(dir(request.user))
    print(type(request.user))
    print(request.user.is_authenticated)
    print(request.user.id) # user id는 1번
    print(request.user.username)
    print(request.user.is_superuser)
    print(request.user.password)
    print(request.GET)
    print(request.GET.get('q'))
    print(request.GET.get('hello', 'world')) # hello라는 쿼리가 없으면 world를 출력
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES) # 어플리케이션 > 쿠키에 저장되어있는 정보
    print(request.path)
    print(request.method)
    print(request.get_full_path_info())
    print(request.get_host()) # 정보보안 확인차 접속자가 어떻게 오는지 알수 있다.
    return render(request, 'blog/postlist.html', {'posts':posts})