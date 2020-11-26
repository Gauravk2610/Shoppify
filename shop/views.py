from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Product, Contact, Order_place, Subscriber
import json

# Create your views here.
def index(request):
    if request.user.is_authenticated is True:
        if request.user.has_perm(Order_place.delivery_user) == True:
            print(request.user.has_perm)
        print(bool(request.user.has_perm)) 
        product = Product.objects.all()
        category = Product.objects.values('category')
        cats = {item['category'] for item in category}
        params = {'product':product, 'category':cats}
        return render(request, 'shop/index.html', params)
    
    else:
        return redirect('/')

def product(request, id):
    if request.user.is_authenticated is True:
        product = Product.objects.filter(product_id=id)
        params = {'product_id':product[0]}
        return render(request, 'shop/product_details.html', params)
    
    else:
        return redirect('/')

def contact(request):
    if request.user.is_authenticated is True:
        params = None
        if request.method == 'POST':
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            desc = request.POST.get('message', '')
            if name and email and subject and desc != None:
                print(name, email, subject, desc)
                contact = Contact(name=name, email=email, subject=subject, desc=desc)
                contact.save()
            else:
                params = {'info':'Please Input Valid Credentials'}

        return render(request, 'shop/contact.html', params)
    
    else:
        return redirect('/')

def checkout(request):
    if request.user.is_authenticated is True:
        if request.method == "POST":
            user = request.user
            items_json = request.POST.get('itemsJson', '')
            name = request.POST.get('firstName', '') + " " + request.POST.get('lastName', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
            country = request.POST.get('country', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip', '')
            phone = request.POST.get('phone', '')
            print(name, email)
            order = Order_place(user = user, items_json=items_json, name=name, email=email, address=address, country=country, state=state, zip_code=zip_code, phone=phone)
            order.save()
            thank = True
            return render(request, 'shop/checkout1.html', {'thank':thank})
        return render(request, 'shop/checkout1.html')

    else:
        return redirect("/")

def tracker(request):
    if request.user.is_authenticated is True:
        total = 0
        order_llist = []
        order_list = Order_place.objects.filter(user=request.user)
        print(bool(order_list))
        if bool(order_list) != False:
            order_id = order_list[0].order_id
            print(order_list)
            for item in order_list:

                status = item.status
                item = (item.items_json)
                res = json.loads(item)
                for item in res:
                    print(item)
                    print(res)
                    print(item)
                    prod_item_id = item.split(":")[0].split("pr")[-1].strip('"')
                    prod_id = "pr" + prod_item_id
                    print(prod_item_id)
                    qty = res["pr{}".format(prod_item_id)][0]
                    prod_name = res["pr{}".format(prod_item_id)][1]
                    prod_price = res["pr{}".format(prod_item_id)][2]
                    print(prod_name)
                    total = total + qty
                    order_llist.append({
                        'qty':qty,
                        'prod_name':prod_name,
                        'prod_price':prod_price,
                        'status':status

                    })
            print(order_id)

            return render(request, 'shop/tracker.html', {'order_llist':order_llist, 'total':total, 'order_id':order_id})

        else:
            messages.warning(request, "Please Do Shop Something Before You Track Your Orders ")
            return redirect('/shop')
        
    else:
        return redirect('/')

def about(request):
    if request.user.is_authenticated is True:

        return render(request, "about/aboutus.html")

    else:
        return redirect('/')

def team(request):
    if request.user.is_authenticated is True:
    
        return render(request, "about/team.html")
    
    else:
        return redirect('/')


def subscriber(request):
    if request.user.is_authenticated is True:
        if request.method == "POST":
            user = request.user
            email = request.POST["email"]
            print(user, email)
            subscriber = Subscriber(user=user, email=email)
            subscriber.save()
            return redirect("/shop/thanks")
    
    else:
        return redirect('/')

def thanks(request):
    if request.user.is_authenticated is True:

        return render(request, "shop/thanks.html")
    
    else:
        return redirect('/')