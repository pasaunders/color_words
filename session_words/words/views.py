from django.shortcuts import render, redirect


def rendering(request):
    return render(request, 'words/index.html',context=None)


def add(request):
    return redirect('/')


def clear(request):
    return redirect('/')