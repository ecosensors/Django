from django.shortcuts import render

# Create your views here.
def blog_index(request):
    return render(request,'blog/index.html',context={'toto':'toto'})


def article(request, no_article):
    print(no_article)
    if no_article in ["01","02","03"]:
        return render(request, f"blog/article_{no_article}.html", context={'a':'d'})
    return render(request, "blog/article_not_found.html")