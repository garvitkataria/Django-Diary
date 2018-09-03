
from django.shortcuts import render
from django.contrib.auth.models import User
from .form import RegisterForm, LoginForm
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login

def regester(request):

	# user = User.objects.create_user('john2', 'lennon2@thebeatles.com', 'johnpassword')
	# user.last_name = 'Lennon2'
	# user.save()
	print(request.method)
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			# n=User()
			# n.last_name=()
			# n.first_name=form.cleaned_data['title']
			# n.email=form.cleaned_data['body']
			# n.save()
			#n = User.objects.create_user(**form.cleaned_data)
			n = User()
			n.last_name=form.cleaned_data['last_name']
			n.first_name=form.cleaned_data['last_name']
			n.email=form.cleaned_data['username']
			n.username=form.cleaned_data['email']
			n.password=form.cleaned_data['password']
			n.save()
			return HttpResponseRedirect('/blog')
	else:
		form = RegisterForm()
	return render(request, 'UserRegister1/auth.html', {'form': form})

def login(request):
	print(request.method)
	if request.method == 'POST':
	 	form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/blog')
		else:
			form = LoginForm()
		# return render(request, 'UserRegister1/auth.html', {'form': form})
