from django.shortcuts import render,redirect
from .models import*
#     return render(request,"index.html")
# def about(request):
#     return render(request,"about.html")
# def demo(request):
#     return render(request,"demo.html")
# def hello(request):
#     return render(request,"hello.html")

def index (request):
    if request.method =='POST':
        name=request.POST['name']
        age=request.POST['age']
        mark=request.POST['mark']
        obj=details(name=name,age=age,mark=mark)
        obj.save()
        return redirect(index)
    obj=details.objects.all()
    return render(request,'index.html',{'obj':obj})
def delete_g (request,pk):
    prodobj=details.objects.get(pk=pk)
    prodobj.delete()
    return redirect("index")

def edit_g(request,pk):
    prodobj=details.objects.get(pk=pk)
    prodobj.edit()
    return render(request,"hello.html")




