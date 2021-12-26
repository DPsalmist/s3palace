from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from django.urls import reverse
from cart.cart import Cart
from .tasks import order_created

# Paypal payment gateway 
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],
										quantity=item['quantity'])
            cart.clear()
            order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/create.html',{'cart': cart, 'form': form})

# Braintress payment gateway   
def braintree_order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order,product=item['product'],price=item['price'],
										quantity=item['quantity'])
			# clear the cart
			cart.clear()
			# launch asynchronous task
			order_created.delay(order.id)
			# set the order in the session
			request.session['order_id'] = order.id
			# redirect for payment
			return redirect(reverse('payment:process'))
			#return render(request,'orders/order/created.html',{'order': order})
	else:
		form = OrderCreateForm()
	return render(request,'orders/order/create.html',{'cart': cart, 'form': form})