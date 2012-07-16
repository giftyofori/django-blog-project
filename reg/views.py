
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
       name=request.POST['username']
       pasword=request.POST['password']
       user=authenticate(username=name, password=pasword)
       if user is not None:
    	    if user.is_active:
    	       login(request,user)
    	       return render_to_response('blog/posts')
   
            else:
	        print 'Your account has been disabled'
    else:
	print 'Invalid login'
    
    form = LoginForm()
    return render_to_response('reg/do_login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated()
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('reg/logout.html')# Create your views here.
