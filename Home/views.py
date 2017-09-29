from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')


def new_post(request):
    return render(request, '_newPostForm.html')