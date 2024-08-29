from django.shortcuts import render

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
        return render(request,'index.html')


