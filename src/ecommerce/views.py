from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	context = {
	"title":"Hello World!",
	"content":"Welcome to the homepage.",
	}
	return render(request,"home_page.html", context)


def about_page(request):
	context = {
		"title":"about page",
		"content":" Welcome to the about page.",
	}
	return render(request,"home_page.html", context)

def contact_page(request):
	context = {
		"title":"contact",
		"content":" Welcome to the contact page.",
	}
	if request.method == "POST":
		#print(request.POST)
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('content'))
	return render(request,"contact/view.html", context)