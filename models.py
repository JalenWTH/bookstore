from django.db import models

class signup_model(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phone=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    street_address=models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=30,null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    zip_code=models.IntegerField(null=True,blank=True)
    def __self__():
        return f'{self.fname} {self.lname} {self.phone} {self.email} {self.street_address} {self.city} {self.state} {self.zip_code}'
        
class book_model(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50, null=True)
    author_fname=models.CharField(max_length=30)
    author_lname=models.CharField(max_length=30)
    copyright_year=models.CharField(max_length=4)
    image_url=models.CharField(max_length=100)
    def __self__():
        return f'{self.book_id} {self.title} {self.author_fname} {self.author_lname} {self.copyright_year}'
    
        
class order_model(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phone=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=100)
    street_address=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    zip_code=models.IntegerField()
    book=models.ForeignKey(book_model, on_delete=models.CASCADE)
    order_id=models.IntegerField(primary_key=True)
    def __self__():
        return f'{self.fname} {self.lname} {self.phone} {self.email} {self.street_address} {self.city} {self.state} {self.zip_code} {self.book} {self.order_id}'

models_list = (signup_model, book_model, order_model)