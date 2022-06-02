from ctypes.wintypes import MSG
from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

# views here.
def login(request):
    return render(request,'app1/login.html')

def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        a = str("cst")#to approve account admin need to overwrite status value with this key string to approve 
        # Checking the emailid with database
        user = LeafUser.objects.get(Email=email)

        if user:
            if user.Password == password:
                if user.Status == a:#if admin approves then the key string is updated and this loop will be true
                # We are getting user data in session
                    request.session['Username'] = user.Username
                    request.session['Email'] = user.Email
                    return redirect('showfromitemtabletohomepage')
                else:
                    message = " Account Not approved"
                    return render(request,"app1/login.html",{'msg':message})
            else:
                message = "Password does not match"
                return render(request,"app1/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app1/signup.html",{'msg':message})

def signup(request):
    return render(request,'app1/signup.html')
    #input from signup to create a user in db

def inputfromsignup(request):#input from signup page 
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        status = request.POST['status']
        service = request.POST['service']
        phno = request.POST['phno']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']

    # First we will validate that user already exist
    user = LeafUser.objects.filter(Email=email)

    if user:
        message = "User already exist"
        return render(request,'app1/signup.html',{'msg':message})
    else:
        if password == confirmpassword:
            newuser = LeafUser.objects.create(Username=username,Email=email,Status=status,Service=service,Phonenumber=phno,Password=password,Confirmpassword=confirmpassword)
            message = "User registered Successfully,Approval Pending "
            return render(request,'app1/login.html',{'msg':message})
        else:
            message = "Password and Confirm Password Does not Match"
            return render(request,"app1/signup.html",{'msg':message})

def contact(request):
    return render(request,'app1/contact_us.html')
def index(request):
    return render(request,'app1/index.html')
def homepage(request):
    return render(request,'app1/homepage.html')
def about(request):
    return render(request,'app1/about.html')


def buy(request):
    return redirect('showfromitemtable')#redirected to showfromitemtable function


def sell(request):
    return render(request,'app1/sell.html')
def donate(request):
    return render(request,'app1/donate.html')
def successuser(request):
    return render(request,'app1/successuser.html')
def buydemo(request):
    return render(request,'app1/buydemo.html')
def sold(request):
    return render(request,'app1/sold.html')

def donated(request):
    return render(request,'app1/donated.html')

def addingitem(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        itemname = request.POST['itemname']
        price = request.POST['price']   
        image= request.FILES['image']

        newitem = Item.objects.create(Username=username,Email=email,Itemname=itemname,Price=price,Image=image)
        return render(request,'app1/sold.html')

#imagefetch
def showfromitemtable(request):
    all_item = Item.objects.all()
    return render(request,"app1/buy.html",{'key1':all_item})

def showfromitemtabletohomepage(request):
    all_itemhome = Item.objects.all()
    return render(request,"app1/homepage.html",{'key1':all_itemhome})

def myorders(request):
    return render(request,'app1/mo.html')

def posts(request):
    return redirect('showfromposttable')

def addingpost(request):#adding post function
    if request.method == 'POST':
        postno = request.POST['postno']
        postdetails = request.POST['postdetails']   
        image= request.FILES['image']

        newpost = Posts.objects.create(Postno=postno,Postdetails=postdetails,Image=image)
        return render(request,'app1/posted.html')

def posted(request):
    return render(request,'app1/posted.html')
def addpost(request):
    return render(request,'app1/addpost.html')

def showfromposttable(request):
    all_posts = Posts.objects.all()
    return render(request,"app1/posts.html",{'key1':all_posts})

def donate(request):
    return render(request,'app1/donate.html')

def addingitemfromdonatepage(request):# function to add item from donate page
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        itemname = request.POST['itemname']
        price = request.POST['price']   
        image= request.FILES['image']
        x = str("free")

        newdonation = Item.objects.create(Username=username,Email=email,Itemname=itemname,Price=x,Image=image)
        return render(request,'app1/donated.html')