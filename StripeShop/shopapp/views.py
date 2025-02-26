from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Item
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def index_view(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def item_detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item.html', {'item': item, 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})

def buy_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    session = stripe.checkout.Session.create(
    line_items= [{
      'price_data': {
        'currency': 'rub',
        'product_data': {
          'name' : item.name,
        },
        'unit_amount': int(item.price * 100)
      },
      'quantity': 1,
    }],
    mode= 'payment',
    success_url="http://127.0.0.1:8000/shopapp/success",
    cancel_url="http://127.0.0.1:8000/shopapp/cancel",
    )
    return JsonResponse({
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLIC_KEY
    })

def success_view(request):
    return render(request, 'success.html')

def cancel_view(request):
    return render(request, 'cancel.html')