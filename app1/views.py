from django.shortcuts import render
def wish(request):
    d={'name':'DINESH','age':20}
    return render(request,'wish.html',contex=d)
# Create your views here.
