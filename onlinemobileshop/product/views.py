from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.forms import Form
from product.forms import BrandForm, MobileForm, OrderForm, OrderUpdateForm, TrackForm, SearchForm, RegistrationForm
from product.models import Brand, Order
from product.models import Mobile
from django.contrib.auth.decorators import login_required


# Create your views here.
def createBrand(request):
    form = BrandForm
    context = {}
    context['form'] = form
    obj = Brand.objects.all()
    context['brands'] = obj
    if request.method == "POST":
        form = BrandForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return render(request, 'product/create_brand.html', context)
        else:
            return render(request, 'product/create_brand.html', context)

    return render(request, 'product/create_brand.html', context)


def editBrand(request, pk):
    obj = Brand.objects.get(id=pk)
    form = BrandForm(instance=obj)
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = BrandForm(instance=obj, data=request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('createbrand')
        else:
            return render(request, 'product/edit_brand.html', context)
    return render(request, 'product/edit_brand.html', context)


def deleteBrand(request, pk):
    Brand.objects.get(id=pk).delete()
    return redirect('createbrand')


def createMobile(request):
    form = MobileForm
    context = {}
    context["form"] = form
    products = Mobile.objects.all()
    context['mobiles'] = products
    if request.method == "POST":
        form = MobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    return render(request, 'product/create_product.html', context)

@login_required(login_url='login')
def homePage(request):
    context = {}
    obj = Mobile.objects.all()
    context['products'] = obj
    form = SearchForm
    context['search'] = form
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            brand = request.POST.get("brand_name")
            products = Mobile.objects.filter(brand__brand_name=brand)
            print(products)
            context['products'] = products
            return render(request, 'product/homepage.html', context)
        else:
            msg = "No Result found!"
            context['msg'] = msg
            return render(request, 'product/homepage.html', context)

    return render(request, 'product/homepage.html', context)


def mobileView(request, pk):
    obj = Mobile.objects.get(id=pk)
    context = {}
    context['form'] = obj
    return render(request, 'product/view_mobile.html', context)


def orders(request, pk):
    context = {}
    form = OrderForm(initial={'productid': pk, "user": request.user})
    context['form'] = form
    obj = Mobile.objects.get(id=pk)
    context['status'] = obj

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'product/success.html', context)
    return render(request, 'product/order.html', context)


def viewOrder(request):
    obj = Order.objects.all()
    context = {}
    context['orders'] = obj
    return render(request, 'product/vieworders.html', context)


def orderUpdate(request, pk):
    print(type(pk))
    obj = Order.objects.get(id=pk)
    pid = obj.productid
    obj2 = Mobile.objects.get(id=pid)
    form = OrderUpdateForm(instance=obj)
    context = {}
    context['mobile'] = obj2
    context['form'] = form
    if request.method == "POST":
        obj = Order.objects.get(id=pk)
        form = OrderUpdateForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('vieworder')

    return render(request, 'product/order_update.html', context)


def trackOrders(request):
    form = TrackForm
    context = {}
    obj = Order.objects.all()
    context['form'] = form
    if request.method == "POST":
        form = TrackForm(request.POST)
        if form.is_valid():
            names = request.POST.get("personname")
            print("formname", names)

            for i in obj:

                print("objname", i.personname)
                if names == i.personname:
                    context['i'] = i

                    return render(request, 'product/status.html', context)
        else:
            form = TrackForm(request.POST)
            context['form'] = form
            return render(request, 'product/track.html', context)

    return render(request, 'product/track.html', context)


def searchBrand(request):
    form = SearchForm
    context = {}
    context['form'] = form
    if request.method == "POST":
        print("hi")
        form = SearchForm(request.POST)
        brand = request.POST.get('brand_name')
        if form.is_valid():

            obj = Brand.objects.all()
            print(obj)
            for i in obj:
                print(brand, "--", i.brand_name)
                if brand == i.brand_name:
                    print(brand, "matched", i.brand_name)
                    context['form'] = i
                    return render(request, 'product/search.html', context)
                # else:
                #     context['form']="not found"
                #     return render(request, 'product/search.html', context)

    return render(request, 'product/home.html', context)


def register(request):
    form = RegistrationForm
    context = {}
    context['form'] = form
    if request.method == "POST":
        print("inside click")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("inside valid")
            form.save()
            print("saved")
            return redirect('login')
        else:
            context['form'] = form
            return render(request, 'product/registraion.html', context)

    return render(request, 'product/registraion.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        if(username=="admin")&(password=="admin"):
            return render(request,'product/adminhome.html')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                context = {}
                context['form'] = "IN VALID USER NAME OR PASSWORD!"
                return render(request, 'product/login.html', context)

    return render(request, 'product/login.html')


def test(request):
    return render(request, 'product/base.html')


def logOut(request):
    logout(request)

    return redirect("homepage")


def viewUserOrder(request):
    obj = Order.objects.filter(user=request.user,active_status=1)
    context = {}
    context['orders'] = obj

    print(len(obj))
    if(len(obj)==0):
        context={}
        context['msg']="No Orders"
        return render(request, 'product/viewuserorder.html', context)
    else:
        context = {}
        context['orders'] = obj

        return render(request, 'product/viewuserorder.html', context)


def cancelOrder(request, pk):
    print("workde")
    obj = Order.objects.get(id=pk)
    obj.active_status=0
    obj.save()
    print(obj.active_status)

    return redirect('viewuserorder')
def adminPage(request):
    return render(request, "product/adminhome.html")