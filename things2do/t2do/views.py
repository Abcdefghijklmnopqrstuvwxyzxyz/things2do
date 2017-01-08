from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import auth
from datetime import datetime
from t2do.models import Plan, ContactItem

# Create your views here.
def index(request):
	if request.user.is_authenticated:return HttpResponseRedirect("/account/");
	return render(request, "t2do/index.html");

def about(request):
	return HttpResponse("<h1> About Things2Do</h1>")
	#return render(request, "t2do/about.html");

def reg(request):
	return render(request, "t2do/new.html")
	#return render(request, "t2do/reg.html");

def login(request):
	if request.method == 'GET':
		return HttpResponseRedirect("/");
	try:
		next = request.POST['next'];
	except KeyError:
		next = '/account/'
	try:
		password = request.POST['pass']
		username = request.POST['user']
	except KeyError:
		return HttpResponseRedirect('/');
	user = authenticate(username=username, password=password);
	if user is None:
		return HttpResponse("<h1> Bad Username</h1>");
	else:
		auth.login(request, user);
		return HttpResponseRedirect("/account/?page=1");

	#Fallback
	return HttpResponseRedirect("/");

def logout(request):
	auth.logout(request);
	return HttpResponseRedirect("/");

@login_required(login_url="/")
def user_index(request):
	try:
		page = int(request.GET['page'])
	except KeyError:
		page = 1
	finally:
		page=page-1
		quan = 25;
		first = page * quan;
		last = page * quan + quan;
		planList = Plan.objects.filter(user__exact=request.user).order_by('-importance', '-end_time')[first: last];
		return render(request, "t2do/dashboard.html", {'title': "My Plans", 'plans': planList, 'page': page, 'next': page+2});

@login_required(login_url="/")
def edit_plan(request):
	try:
		id = request.GET['id']
	except KeyError:
		return render(request, 't2do/base.html', {'error': 'Please check your url "%s" is correct.' % request.path})
	current = get_object_or_404(Plan, pk=id)
	start_time = current.start_time.isoformat()[:19]
	deadline = current.end_time.isoformat()[:19]
	return render(request, "t2do/edit.html", {'current': current, 'startTime': start_time, 'deadline': deadline, 'title': 'Edit Plan'})

@login_required(login_url="/")
def add_plan(request):
	return HttpResponse("<h1>Add new ")

@login_required(login_url="/")
def user_setting(request):
	return render(request, "t2do/base.html", {'error': 'Coming Soon...'}, status=404)

@login_required(login_url="/")
def submit_plan(request):
	try:
		id = request.POST['id'];
	except KeyError:
		return HttpResponseRedirect("/account/");
	current = get_object_or_404(Plan, pk=id);
	if current.user != request.user:
		return render(request, 't2do/base.html', {'error': '403 Forbidden'}, status=403);
	else:
		#As the browser will send us time in ISO format, we have to proccess them.
		#The ISO time format here is: YYYY-MM-HHTHH:MM
		start_iso = request.POST['start'];
		end_iso = request.POST['end'];
		#I am not sure about it so let's print them out
		print(start_iso, end_iso);
		if start_iso is not '':
			start_time = datetime(int(start_iso[0:4]), int(start_iso[5:7]), int(start_iso[8:10]), int(start_iso[11:13]), int(start_iso[14:16]));
			current.start_time = start_time;
		if end_iso is not '':
			end_time = datetime(int(end_iso[0:4]), int(end_iso[5:7]), int(end_iso[8:10]), int(end_iso[11:13]), int(end_iso[14:16]));
			current.end_time = end_time;
	#finally:
		importance = request.POST['importance'];
		description = request.POST['description'];
		name = request.POST['name'];
		current.importance = importance
		current.description = description
		current.name = name
		current.save();
		return HttpResponseRedirect('/account/');

