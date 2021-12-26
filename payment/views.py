import braintree
from django.shortcuts import render
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order

# Create your views here.

# Paypal 
def paypalpayment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/paypalprocess.html', {'order': order,
                                                    'form':form})


# instantiate Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def payment_process(request):
    """The view that processes the payment using dropin ui"""
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        # retrieve nonce 
        # retrieve nonce
        nonce = request.POST.get('paymentMethodNonce', None)

        # # create User 
        customer_kwargs = {
            "first_name": order.first_name,
            "last_name": order.last_name,
            "email": order.email
        }
        customer_create = gateway.customer.create(customer_kwargs)
        customer_id = customer_create.customer.id

        #create and submit transaction
        
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })

        print(result)
        print('Payment was successful!')
        if result.is_success:
            #mark the order as paid 
            order.paid = True   
            # store the unique transaction id 
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = gateway.client_token.generate()

        return render(
            request,
            'payment/rayment.html',
            {
                'order':order,
                'client_token': client_token
            }
        )


def newpayment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    
    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale({ 
                                           'amount': f'{total_cost:.2f}', 
                                           'payment_method_nonce': nonce,
                                           'options': {'submit_for_settlement': True 
                                                    }
                                           })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = gateway.client_token.generate()
        return render(request, 'payment/newprocess.html', {'order': order,'client_token': client_token})


def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')