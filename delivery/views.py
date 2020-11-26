from django.shortcuts import render, HttpResponse, redirect
from shop.models import Order_place
from django.contrib import messages
# Create your views here.

def delivery(request):
    if request.user.has_perm(Order_place.delivery_user) == True:
        try:
            order_list = []
            order = Order_place.objects.all()
            print(order[0].name)
            category = Order_place.objects.values('state', 'order_id')
            print(category)
            cats = {item['state'] for item in category}
            for cat in cats:
                ord1 = Order_place.objects.filter(state=cat)
                print(ord1)
                order_list.append(ord1)
            params = {'order_list':order_list, 'category':cats}
            print(params)
        except Exception:
            params = {'nthing':'Nothing To Deliver'}
            pass
        return render(request, 'delivery/delivery.html', params)
    
    else:
        messages.warning(request, "You Dont Have Access To View That Page")
        return redirect('/shop')

def delivery_details(request, id):
    if request.user.has_perm(Order_place.delivery_user) == True:
        order = Order_place.objects.filter(order_id=id)
        params = {'order':order[0]}
        if request.method == 'POST':
            order = Order_place.objects.get(order_id=id) 
            status = request.POST["status"]
            order.status = status   
            order.save()
            print(status)
            if order.status == "Order Completed":
                order.delete()
                print(order.status)   
                print(Order_place.objects.all())
                return redirect('/delivery')
            return redirect('/delivery')
        return render(request, 'delivery/delivery_details.html', params)
    else:
        messages.warning(request, "You Dont Have Access To View That Page")
        return redirect('/shop')