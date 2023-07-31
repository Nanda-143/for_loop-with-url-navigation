from django.shortcuts import render

d={10:20,'habbits':['cricket','carroms','vollyball']}
def forloop(request):
    return render(request,'forloop.html',context=d)

def conditions(request):
    return render(request,'conditions.html')