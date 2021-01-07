from django.shortcuts import render, HttpResponseRedirect
from .models import Cart,CartItem
from django.urls import reverse
from products.models import Product
from django.contrib.auth.decorators import login_required

# from user.models import CustomerLogin
# Create your views here.
@login_required(login_url='login_page')
def cartview(request):
    request.session['username'] = request.user.username
    username = request.session['username']
    context = {'username':username}
    try:
        the_id = request.session['cart_id']
    except:
        the_id= None
    if the_id:
        welcome_message = "Welcome to your cart"
        cart = Cart.objects.get(id=the_id)
        context = {'cart':cart,'welcome_message':welcome_message,'username':username}
    else:
        message = "Your cart is empty keep shopping!!"
        context = {"empty": True, 'message': message,'username':username}


    template = 'cart.html'
    return render(request, template, context)

@login_required(login_url='login_page')
def update_cart(request, slug):
    request.session.set_expiry(300)
    # to check whether the cart id exist
    try:
        the_id = request.session['cart_id']
    except:
    # if cart id DoesNotExist create an instance of it and save
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
        #creating an instance of CartItem
    cart_item, created = CartItem.objects.get_or_create(product = product) #

    if not cart_item in cart.items.all():
        cart.items.add(cart_item)
    else:
        # cart.items.remove(cart_item)
        return HttpResponseRedirect(reverse('cart'))

    qty = request.POST.get('quantity')
    print(qty)

    new_total = 0.00
    for items in cart.items.all():
        line_total = float(items.product.price)*items.quantity
        new_total += line_total

    request.session['items_total'] = cart.items.count()
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse('home'))
