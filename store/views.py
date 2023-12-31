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
    return render(request,'cart.html')