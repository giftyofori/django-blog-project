
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    posts = Post.objects.all()
    t=loader.get_template('blog/post_list.html')
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))

def post_detail(request, id, showComments=True):
    post = Post.objects.get(id = id)
    comments = post.comment_set.all()
    return render_to_response('blog/post_detail.html',{'post':post,'comments':comments})
   
'''
    tk='<h1 style="color:pink">' +thing.title +'</h1>' +     '<br>'+thing.body +'<br>'+'<h4 style="color:green">'+'comment:'+'</ h4>'+something.body
    return HttpResponse(tk)
'''
   

   
   
    
def post_search(request, term):
    posts= Post.objects.filter(body__icontains =term)
    return render_to_response('blog/post_search.html',{'posts':posts,'term':term})
   

def home(request):
    print 'it works'
    return render_to_response('blog/base.html',{})
 





















# Create your views here.
