from django.shortcuts import render,HttpResponse,redirect
from .models import Item,Imagedetail
from django.views.generic import ListView,DetailView

# Create your views here.



#home
# def home(request):
#     items=Item.objects.all()
#     context={"items":items}
#     return render(request,'core/home.html',context)
class Home(ListView):
    model=Item
    template_name="core/home.html"
    context_object_name="items"
    paginate_by=2

def DetailItem(request,pk):
    item=Item.objects.get(pk=pk)

    if request.method =="GET":
        context={'item':item}
        return render(request,'core/detail_item.html',context)

    if request.method=='POST':
        data=request.POST.copy()
        print(data)
        return redirect('core:detail_item' ,pk)