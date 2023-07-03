import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import CreateUserForm, ShoesForm


def index(request):
    return render(request, "index.html")


def shoes(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']

    # Filtering shoes by type and brand
    types = [shoe_type[1] for shoe_type in Shoes.TYPE]
    brands = [shoe_brand[1] for shoe_brand in Shoes.BRAND]

    selected_type = request.GET.get('type')
    selected_brand = request.GET.get('brand')
    if selected_type:
        all_shoes = Shoes.objects.filter(type=selected_type).order_by('name')
    elif selected_brand:
        all_shoes = Shoes.objects.filter(brand=selected_brand).order_by('name')
    else:
        all_shoes = Shoes.objects.all().order_by('name')

    # Pagination
    p = Paginator(all_shoes, 6)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    # Counting the types of shoes for each type
    shoe_type_counts = []
    for shoe_type in Shoes.TYPE:
        count = Shoes.objects.filter(type=shoe_type[0]).count()
        shoe_type_counts.append((shoe_type[1], count))

    # Counting the types of shoes for each type
    shoe_brand_counts = []
    for shoe_brand in Shoes.BRAND:
        count = Shoes.objects.filter(brand=shoe_brand[0]).count()
        shoe_brand_counts.append((shoe_brand[1], count))

    context = {"shoes": page, "cart_items": cart_items, "shoe_types": types,
               "shoe_brands": brands, "shoe_type_counts": shoe_type_counts, "shoe_brand_counts": shoe_brand_counts}
    return render(request, "shoes.html", context=context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def add_shoes(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = ShoesForm(request.POST, request.FILES)
        else:
            pair_of_shoes = Shoes.objects.get(pk=id)
            form = ShoesForm(request.POST, request.FILES, instance=pair_of_shoes)
        if form.is_valid():
            form.save()
        return redirect("shoes")
    else:
        if id == 0:
            form = ShoesForm()
        else:
            pair_of_shoes = Shoes.objects.get(pk=id)
            form = ShoesForm(instance=pair_of_shoes)

    context = {"form": form}
    return render(request, "addShoes.html", context=context)


def shoes_details(request, id=0):
    pair_of_shoes = Shoes.objects.get(pk=id)
    context = {"pair_of_shoes": pair_of_shoes}
    return render(request, "shoes_details.html", context=context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def delete_shoes(request, id=0):
    pair_of_shoes = Shoes.objects.get(pk=id)
    pair_of_shoes.delete()
    return redirect('shoes')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customer'])
def delete_item(request, id=0):
    order_item = OrderItem.objects.get(pk=id)
    order_item.delete()
    return redirect('cart')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customer'])
def delete_order(request, id=0):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('cart')


# @csrf_exempt
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Bad credentials')

    context = {}
    return render(request, "registration/login.html", context=context)


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    customer = Customer()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            customer.user = user
            customer.first_name = user.username
            customer.email = user.email
            customer.save()

            messages.add_message(request, messages.SUCCESS, 'Account was created for ' + user.username)
            return redirect('loginPage')

    context = {"form": form}
    return render(request, "registration/register.html", context=context)


@login_required(login_url='loginPage')
def logoutUser(request):
    logout(request)
    return redirect('loginPage')


def not_allowed(request):
    return render(request, 'not_allowed.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customer'])
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {"items": items, "order": order}
    return render(request, "cart.html", context=context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customer'])
def add_to_cart(request, id=0):
    if request.method == 'POST':
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            shoes_id = request.POST.get('shoes_id')
            selected_size = request.POST.get('selected_size')
            print(selected_size)
            pair_of_shoes = get_object_or_404(Shoes, pk=shoes_id)

            order_item_exists = order.orderitem_set.filter(shoes=pair_of_shoes, selected_size=selected_size).first()

            if order_item_exists:
                order_item = order_item_exists
                order_item.quantity += 1
                order_item.save()
            else:
                order_item = OrderItem.objects.create(shoes=pair_of_shoes, order=order, quantity=1)
                order_item.selected_size = selected_size
                order_item.save()

        return redirect('cart')
    else:
        return redirect('shoes')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customer'])
def increase_quantity(request, id):
    order_item = OrderItem.objects.get(pk=id)
    order_item.quantity += 1
    order_item.save()
    return redirect('cart')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customer'])
def decrease_quantity(request, id):
    order_item = OrderItem.objects.get(pk=id)
    if order_item.quantity > 0:
        order_item.quantity -= 1
    if order_item.quantity == 0:
        order_item.quantity = 0;
    order_item.save()
    return redirect('cart')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customer'])
def checkout(request, id):
    if request.method == "POST":
        order = Order(pk=id)
        order.delete()
        return redirect('order_confirmed')
    else:
        order = Order(pk=id)
    context = {"order": order}
    return render(request, "checkout.html", context=context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'customer'])
def order_confirmed(request):
    return render(request, "order_confirmed.html")
