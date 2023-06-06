from rest_framework import serializers
from orders.models import Electronic_Item


class Item_Serializer(serializers.ModelSerializer):

    class Meta:
        model=Electronic_Item
        fields=('customer','phone_number','district_name',
                'sector_name','electronic_picture','electronic',
                'description','price','warranty','weight','id',
                'created_at','be_shipped')

        



