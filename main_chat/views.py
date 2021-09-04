from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User_message
from .forms import UsersForm
# Create your views here.


def main(request):
    message = User_message.objects.order_by('-id')
    return render(request, 'main_chat/main.html', {'message':message})


def chat(request):
    error = ''
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = UsersForm()
    data={
        'form':form,
        'error': error
    }
    return render(request, 'main_chat/chat.html',data)


def music(request):
    message = User_message.objects.order_by('-id')
    return render(request, 'main_chat/music.html', {'message':message})


def cinema(request):
    message = User_message.objects.order_by('-id')
    return render(request, 'main_chat/cinema.html', {'message':message})
