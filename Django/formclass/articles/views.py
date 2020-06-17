from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):

    if request.method == 'POST':
        # 요청이 post면 Database에 저장
        # 1. 요청에 실려온 Data 꺼내오기
        form = ArticleForm(request.POST)
        # 2_1. 유효성 검사
        if form.is_valid():
            # 2-2. 검정된 Data 꺼내오기
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # 2-3. Database에 저장
            article = Article(title=title, content=content)
            article.save()
        # 3. 저장된 Data를 확인할 수 있는 곳으로 안내
            return redirect('articles:detail', article.pk)


    else: # GET 에 해당됨
        # 작성 양식 보여주기
        form = ArticleForm(
                        max_length=10,
                        label='제목',
                        widget={
                            
                        }
        )
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)


def detail(request, pk):
    # Database에서 data가져오기
    article = Article.objects.get(pk=pk) #db pk = 입력pk
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)