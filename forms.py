from django import forms

class user_data_form(forms.Form):
    fname=forms.CharField(label='First Name:',max_length=30)
    lname=forms.CharField(label='Last Name:', max_length=30)
    phone=forms.CharField(label='Phone Number:', max_length=10)
    email=forms.CharField(label='Email:',max_length=100)
    password=forms.CharField(label='Password', max_length=100)
    street_address=forms.CharField(label='Street Address:',max_length=50)
    city=forms.CharField(label='City:',max_length=30)
    state=forms.CharField(label='State:',max_length=20)
    zip_code=forms.IntegerField(label='Zip Code:')
    
  