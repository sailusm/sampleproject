from django.forms import ModelForm
from django import forms
from product.models import Mobile,Brand,Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class BrandForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            'brand_name':forms.TextInput(attrs={'class':'form-control'})
        }
    def clean(self):
        print("inside clean")
        cleaned_data = super().clean()
        brand_name = cleaned_data.get('brand_name')
        obj = Brand.objects.all()
        for i in obj:
            if (brand_name == i.brand_name):
                messege = "brand name already exists"
                self.add_error('brand_name', messege)
                print("condiftion")

                # name = models.CharField(max_length=130, unique=True)
                # brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
                # ram = models.CharField(max_length=120)
                # price = models.IntegerField()
                # camera = models.CharField(max_length=120)
                # os = models.CharField(max_length=120)
                # image = models.ImageField(upload_to='images')
                #


class MobileForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'os': forms.TextInput(attrs={'class': 'form-control'}),
            'camera': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        widgets = {
            'personname': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'productid': forms.HiddenInput,
            'status':forms.HiddenInput(),
            'user':forms.HiddenInput(),
            'active_status':forms.HiddenInput(),
        }

class OrderUpdateForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        widgets = {
            'personname': forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}),
            'address': forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}),
            'pin': forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}),
            'email': forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}),
            'productid':forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # 'status': forms.ChoiceField(attrs={'class': 'form-control'}),
        }

class TrackForm(ModelForm):
    class Meta:
        model=Order
        fields=['personname']

    def clean(self):
        print("inside clean")
        cleaned_data = super().clean()
        name = cleaned_data.get('personname')
        obj=Order.objects.all()
        flag = 0
        for i in obj:

            if name == i.personname:

               flag=0
               break

            else:
                flag=1


        if(flag==1):
            messege = "enter valid name"
            self.add_error('personname', messege)
            print(messege)

class SearchForm(forms.Form):
    brand_name=forms.CharField(max_length=120)

    def clean(self):
        print("hi")
        cleaned_data=super().clean()
        brand=cleaned_data.get('brand_name')
        products = Mobile.objects.filter(brand__brand_name=brand)
        if len(products)==0:
            messege="no result found"
            self.add_error('brand_name',messege)


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
