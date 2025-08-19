from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, "blog/all-post.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html", {"slug": slug})