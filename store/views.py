from django.shortcuts import render,redirect
from django .http import HttpResponse
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def index (request):
    popular_details = {
        'popular_details': Popular.objects.all()
    }
    return render(request,'index.html',popular_details)
def about (request):
    return render(request,'about.html')
def product (request):
    product_details = {
        'details' :Product.objects.all(),
    }

    return render(request,'product.html',product_details)
def why (request):
    return render(request,'why.html')
def testimonial (request):
    return render(request,'testimonial.html')

def signup(request):
    if request.method=="POST":      # method post aanenkil
        username=request.POST['username'] # username enna variable lekk post lulla username ne store aakunnu
        email=request.POST['email']              # ,,,,,
        password=request.POST['password']           # ,,,,,
        cnfpassword=request.POST['cnfmpassword']   # ,,,,,
        if User.objects.filter(username=username).exists(): # filter cheyth username same aayittullava undo enn check cheyynnnu
            messages.info(request,"username already exists")  # undenkil ee msg pas cheyyunnu
            return redirect('signup')                         # ennitt aa signup pagel thanne redirect cheyyunnu
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return redirect('signup')
        elif password != cnfpassword :                      # password not equal cnfpassword aanenkil 
            messages.info(request,"password mismatch")      # equal alla enkil ee msg pas cheyyunnu
            return redirect('signup')                         # ennitt aa signup pagel thanne redirect cheyyunnu
        else:
            user=User.objects.create_user(username=username,email=email,password=password) # ithokke tharanam cheytha shesham user create cheyyunnu athinayi mukalil user ennath import cheyynm
                                                                                         # crete_user enna function upayokich nerthe vecha variablekk assign cheyyunnu
            user.save();                          # athine save cheyyunnu
            return redirect('index')              # sett aanenkil index pagelekk redirect cheyyunnu
    else:
        return render(request,'signup.html')     # alla enkil signup l thanne redirect cheyyunnu


def Loginn(request):
    if request.method == "POST":          #method post aanenkil
        username = request.POST['username'] #variablil store cheyyka
        password = request.POST['password']
        user = authenticate(username=username,password=password) # 
        if user is not None :    # none ella ennundenkil
            auth.login(request,user) #default aayituula function an login athineyan call cheydhadh
            return redirect('index')
        else:
            messages.info(request,"invalid login")
    return render(request,'login.html')



def Logoutt(request):
    auth.logout(request)   #default aayituula function an logout athineyan call cheydhadh
    return redirect ('index')


def conditions(request):
    return render(request,'terms.html')

@login_required(login_url='login')
def cart(request):
    current_user=request.user
    crt=cart_Model.objects.get(user=current_user)
    cart_items=crt.items.all()
    sub_total=0
    for s in cart_items:
        sub_total=(s.quantity)*(s.item.product_rate)
    total=0
    for c in cart_items:
        total=total+((c.quantity)*(c.item.product_rate))
    items_count = cart_items.count()
    return render(request,'cart.html',{'cart_items':cart_items,'sub_total':sub_total,'total':total,'items_count':items_count})

def add_to_cart (request,i):
    current_user = request.user
    item = Product.objects.get(id=i)
    qty = 1
    price = item.product_rate
    
    try:
        user_cart=cart_Model.objects.get(user=current_user)
        new_cart_item=cart_item(item=item,quantity=qty,price=price)
        new_cart_item.save()
        user_cart.items.add(new_cart_item)
        user_cart.save()
    except:
        return redirect('login')
    
    return redirect('cart')

def remove_cart_item(request,item_id):
    current_user = request.user
    user_cart = cart_Model.objects.get(user=current_user)
    item = cart_item.objects.get(id=item_id)
    user_cart.items.remove(item)
    user_cart.save()
    return redirect('cart')

def increase_item(request, item_id):
    item = cart_item.objects.get(id=item_id)
    item.quantity+=1
    item.price = item.quantity*item.item.product_rate
    item.save()
    return redirect('cart')

def decrease_item(request, item_id):
    item = cart_item.objects.get(id=item_id)
    if item.quantity > 1 :
        item.quantity-=1
        item.price = item.quantity*item.item.product_rate
        item.save()
    return redirect('cart')

def Check_out(request):
    current_user = request.user
    try:
        cart_instance = cart_Model.objects.get(user=current_user)
        cart_items=cart_instance.items.all()
        orderd_cart_items = cart_items.delete()
        return render(request,'check_out.html')
    except:
        return render(request, 'cart.html', {'error_message': 'Cart not found for the current user.'})