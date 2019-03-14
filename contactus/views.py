from django.shortcuts import render, redirect
from .forms import MessageForm
from django.contrib import  messages
from . models import Branch


# Create your views here.


def home(request):
    all_branches = Branch.objects.all()
    context = {
        'all_branches': all_branches,
    }
    return render(request, 'contactus/home.html', context)


def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We have received your message!')
            return redirect('message')

    else:
        form = MessageForm()

    return render(request, 'contactus/message.html', {'form':form})


