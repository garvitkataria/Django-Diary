from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import NameForm
from .models import Post

from django.contrib.auth.decorators import login_required

def index(request):
	return render(request,'post/form.html')

@login_required(login_url='/accounts/login/')
def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			n=Post()
			n.title=form.cleaned_data['title']
			n.body=form.cleaned_data['body']
			n.save()
			return HttpResponseRedirect('blog/')
	else:
		form = NameForm()
	return render(request, 'post/form.html', {'form': form})