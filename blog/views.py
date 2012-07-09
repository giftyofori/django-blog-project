
from django.template import Context, loader

from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)

def post_detail(request, id, showComments=True):
    thing = Post.objects.get(id = id)
    something= Comment.objects.get(id=id)
    
    return HttpResponse('<h1 style="color:pink">' +thing.title +'</h1>' + '<br>'+thing.body +'<br>'+'<h4 style="color:green">'+'comment:'+'</h4>'+something.body)
   

   
    
def post_search(request, term):
    search= Post.objects.filter(title__icontains =term)
    return HttpResponse ( search.body)
   

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete sene?')
 





















# Create your views here.
