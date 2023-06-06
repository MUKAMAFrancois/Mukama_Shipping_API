from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()



sectors=[('kimisagara','Kimisagara'),('Nyamirambo','Nyamirambo'),('Gitega','Gitega'),
             ('Kacyiru','Kacyiru'),('Kanombe','Kanombe'),
             ('Masaka','Masaka'),('Gikondo','Gikondo'),
             ('Muhima','Muhima'),('Rwezamenyo','Rwezamenyo'),('Niboye','Niboye'),
             ('Gatsata','Gatsata'),('Jali','Jali'),
             ('Gisozi','Gisozi'),('Kimihurura','Kimihurura'),
             ('Jabana','Jabana'),('Remera','Remera')]




    
districts=[('Kicukiro','Kicukiro'),('Gasabo','Gasabo'),('Nyarugenge','Nyarugenge')]


class Electronic_Item(models.Model):

    electronics=[('phones','SmartPhones'),('laptops','Laptops'),('desktops','Desktops'),('appliances','Home appliances')]

    
    customer=models.ForeignKey(User,on_delete=models.CASCADE, related_name='ship_to')
    created_at=models.DateTimeField(auto_now=True)
    electronic=models.CharField(max_length=40, choices=electronics)
    description=models.CharField(max_length=500, default='')
    price=models.FloatField()
    weight=models.FloatField()
    warranty=models.FloatField()
    electronic_picture=models.ImageField(upload_to='electronics/')
    
    district_name=models.CharField(max_length=20, choices=districts)
    sector_name=models.CharField(max_length=30, choices=sectors)
    be_shipped=models.BooleanField(default=False, help_text='can we deliver it?, free service')
    #phone_number=PhoneNumberField(unique=True, null=False)
    phone_number=models.PositiveBigIntegerField(unique=True,null=True)

    def __str__(self):
        return f"Order for:{self.customer.username}"
    

