from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Cart, Order, OrderItem


def home(request):

    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(
        request,
        'home.html',
        {'products': products}
    )


def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        id=pk
    )

    return render(
        request,
        'product_detail.html',
        {'product': product}
    )


@login_required
def add_to_cart(request, pk):

    product = get_object_or_404(
        Product,
        id=pk
    )

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart(request):

    items = Cart.objects.filter(
        user=request.user
    )

    total = sum(
        item.product.price * item.quantity
        for item in items
    )

    return render(
        request,
        'cart.html',
        {
            'items': items,
            'total': total
        }
    )


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


@login_required
def checkout(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    cart_items.delete()

    return render(
        request,
        'success.html'
    )


@login_required
def increase_quantity(request, pk):

    item = get_object_or_404(
        Cart,
        id=pk,
        user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect('cart')


@login_required
def decrease_quantity(request, pk):

    item = get_object_or_404(
        Cart,
        id=pk,
        user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


@login_required
def remove_cart(request, pk):

    item = get_object_or_404(
        Cart,
        id=pk,
        user=request.user
    )

    item.delete()

    return redirect('cart')