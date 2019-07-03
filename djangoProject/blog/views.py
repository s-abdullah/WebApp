from django.shortcuts import render
# Create your views here.

posts = [
	{
		'author': 'Abdullah Siddique',
		'title': 'My Blog Website',
		'content': 'First Psot content',
		'data_posted': 'July 4th 2019'
	},

	{
		'author': 'Sid Buoy',
		'title': 'Le Post',
		'content': 'First Psot content',
		'data_posted': 'August 14 2019'
	}
]


def home(request):
	context = {
		'posts': posts
	}


	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')
