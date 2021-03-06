from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required
from .forms import InvoiceForm,SearchByDateForm
from .models import Invoice,Room,Count
from .utilities import gen_duesbill,gen_moneyreciept,gen_inv
from datetime import datetime


@login_required
def profile_menu(request):
    return render(request, 'profile_menu.html')
@login_required
def make_duesbill(request):
    if request.method=='POST':
        print(request.POST)
        gen_duesbill(request)
        return HttpResponseRedirect(reverse('imageview')+"?i=duebill.jpeg")
    return render(request,'make_duesbill.html')

@login_required
def make_moneyreciept(request):
    if request.method=='POST':
        gen_moneyreciept(request)
        return HttpResponseRedirect(reverse('imageview')+"?i=moneyreciept.jpeg")
    return render(request,'make_moneyreciept.html')

@login_required
def image_view(request):
    return render(request,'imageview.html',{'img':request.GET.get('i',""),'time':datetime.now()})


@login_required
def add_invoice(request):
    rooms = Room.objects.all()
    if request.method=="POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            print(reverse('invoicedetail',args=[form.cleaned_data['invoice_no']]))
            return HttpResponseRedirect(reverse('invoicedetail',args=[form.cleaned_data['invoice_no']]))
        return render(request,'invoiceform.html',{'tag':"Add Invoice",'form':form,'rooms':rooms})
    return render(request,'invoiceform.html',{'tag':"Add Invoice",'form':InvoiceForm(),'rooms':rooms})

@login_required
def invoice_detail(request,no):
    obj = Invoice.objects.get(invoice_no=no)
    return render(request,'invoicedetail.html',{'obj':obj})

@login_required
def edit_invoice(request,pk):
    invoice = Invoice.objects.get(pk=pk)
    form = InvoiceForm(instance=invoice)
    if request.method=="POST":
        form = InvoiceForm(request.POST,instance=invoice)
        if form.is_valid():
            form.save()
            return render(request,'invoiceform.html',{'edit':True,'tag':"Edit Invoice",'msg':"Invoice Updated in Database",'form':form,'invoice_no':invoice.invoice_no,'rooms':Room.objects.all()})

    return render(request,'invoiceform.html',{'edit':True,'tag':"Edit Invoice",'form':form,'invoice_no':invoice.invoice_no,'rooms':Room.objects.all()})


@login_required
def view_invoice(request):
    objects = Invoice.objects.all()
    return render(request,'viewinvoice.html',{'objects':objects})


@login_required
def print_inv_cc(request,invoice_no):
    invoice = Invoice.objects.get(invoice_no=invoice_no)
    gen_inv(invoice)
    return HttpResponseRedirect(reverse('imageview')+"?i=invcc.jpeg")

@login_required
def print_inv_hc(request,invoice_no):
    invoice = Invoice.objects.get(invoice_no=invoice_no)
    gen_inv(invoice,copy='hc')
    return HttpResponseRedirect(reverse('imageview')+"?i=invhc.jpeg")

@login_required
def search_invoice(request):
    if request.method=="POST":
        if request.POST['filter']=='name':
            objects = Invoice.objects.filter(name__contains=request.POST['q'])
        elif request.POST['filter']=='invoice': objects = Invoice.objects.filter(invoice_no=request.POST['q'])
        form = SearchByDateForm(request.POST)
        if form.is_valid(): objects = Invoice.objects.filter(date__range=(form.cleaned_data['fdate'],form.cleaned_data['tdate']))
        wgst = 0
        wogst = 0
        tgst = 0
        wgstwogst = 0
        for o in objects:
            wgst = wgst + o.gstable() + o.gst()*2
            wogst = wogst + o.nongstable()
            tgst = tgst + o.gst()*2
            wgstwogst = o.gstable()
        return render(request,'searchinvoice.html',{'objects':objects,'total':wgst+wogst,'wgst':wgst,'wogst':wogst,'tgst':tgst,'wgstwogst':wgstwogst})
    return render(request,'searchinvoice.html')


@login_required
def searchbyno(request):
    if request.method=="POST":
        obj = Invoice.objects.get(invoice_no=request.POST['invoice_no'])
        return render(request,'searchbyno.html',{'obj':obj})
    return render(request,'searchbyno.html')