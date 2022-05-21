from django.shortcuts import render, redirect
from .models import signup_model, book_model, order_model
from .forms import user_data_form
import random

# Create your views here.

'''
Make it so that when a book is ordered, an instance of the order model is 
created with a randomly generated order id. 

Make sure the styling of the checkout.html template is correct.
'''

def Home(request):
    all_books=[]
    for x in book_model.objects.values():
        all_books.append(x)
    display_books=[]
    for i in range(0,3):
        chosen_book=random.choice(all_books)
        display_books.append(chosen_book)
        all_books.remove(chosen_book)
        
    return render(request, 'bookstore/home.html', {'display_books':display_books})
    

    try:
        if request.session['signed_in'] == True:
            all_books=book_model.objects.values()
            display_books=[]
            for i in range(2):
                display_books.append(random.choice(all_books))
                all_books.delete(display_books[i])
                    
            return render(request, 'bookstore/home.html', {'display_books':display_books})
            
    except KeyError:
        return redirect('Login')
         
def Login(request):
    if request.method == 'POST':
        form=user_data_form(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            x=signup_model.objects.filter(iexact__email=email).values()
            if len(x) == 0:
                signed_up=False
                form=user_data_form(requst.POST)
                return render(request,'bookstore/login.html',{'form':form,'signed_up':signed_up, })
            
            elif x['password'] != password:
                signed_up=False
                form=user_data_form(request.POST)
                return render(request,'bookstore/login.html',{'form':form,'signed_up':signed_up})
           
            request.session['logged_in'] = True
            request.session['fname']=fname
            request.session['lname']=lname
            request.session['email']=email
            request.session.set_expiry(3600)
            return redirect('Home')
            
            
        else:
            valid=False
            form=user_data_form(request.POST)
            return render(request,'bookstore/login.html',{'form':form,'valid':valid})
   
    form=user_data_form()
    return render(request, 'bookstore/login.html', {'form':form})
    
def Signup(request):
    print(request.method)
    if request.method == 'POST':
        form=user_data_form(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['fname']
            lname=form.cleaned_data['lname']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            for queryset in signup_model.objects.values():
                if queryset['email'] == email:
                    signed_up=True
                    form=user_data_form(request.POST)
                    return render(request,'bookstore/signup.html', {'form':form,'signed_up':signed_up})
                
                instance=signup_form(fname=fname, lname=lname, phone=phone, email=email, password=password)
                instance.save()
                return redirect('Login')
        
        else:
            valid=False
            form=user_data_form(request.POST)
            return render(request, 'signup.html', {'form':form,'valid':valid})

    else:
        form=user_data_form()
        return render(request, 'bookstore/signup.html', {'form':form})
    
def Order(request, book_id):
    if request.method=='POST':
        return render(request, 'bookstore/checkout.html', {'book_id':book_id})

    selected_book=book_model.objects.filter(book_id=book_id).values()
    return render(request, 'bookstore/order.html',{'book':selected_book})
    
def Checkout(request, book_id):
    if request.method=='POST':
        form=user_data_form(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['fname']
            lname=form.cleaned_data['lname']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            street_address=form.cleaned_data['street_address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zip_code=form.cleaned_data['zip_code']
            instance=order_model(fname=fname,lname=lname,phone=phone,email=email,street_address=street_address,state=state,city=city,zip_code=zip_code,)
                     

        
        else:
            print('Invalid Form')

    try:
        if request.session['logged_in']==True:
            request.session['fname']=fname
            request.session['lname']=lname
            request.session['phone']=phone
            request.session['email']=email
            form=user_data_form({'fname':fname,'lname':lname,'phone':phone,'email':email})
            selected_book=book_model.objects.filter(book_id=book_id).values()
            return render(request, 'bookstore/checkout.html', {'form':form,'book':selected_book})
            
    except KeyError:
        form=user_data_form()
        return render(request, 'bookstore/checkout.html', {'book_id':book_id})
        
        