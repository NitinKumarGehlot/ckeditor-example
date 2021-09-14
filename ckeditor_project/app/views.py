from django.shortcuts import render
from .forms import CommentForm
from django.contrib import messages
from .models import Comment
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            messages.success(request,'Saved Successfully')
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=CommentForm()
    return render(request, 'app/index.html', {'form':form})

def show(request):
    data=Comment.objects.all()
    return render(request,'app/show.html',{'data':data})