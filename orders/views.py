from rest_framework.response import Response
from orders.serializers import Item_Serializer
from rest_framework.request import Request
from rest_framework.response import Response
from orders.serializers import Item_Serializer
from orders.models import Electronic_Item
from django.contrib.auth import get_user_model

User=get_user_model()

from rest_framework import status, generics, mixins
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema

from rest_framework.filters import SearchFilter,OrderingFilter



class CustomPaginator(PageNumberPagination):
    page_size=2
    page_query_param='page'
    page_size_query_param='page_size'


class Orders_Listing_CreateViewMixins(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
    ):
    """ a simple way for listing and creating an order view"""
    serializer_class=Item_Serializer
    queryset=Electronic_Item.objects.all()
    pagination_class=CustomPaginator
    """
    you can do more with filtering and searching.
    say: http://127.0.0.1:8000/orders/all_orders/?ordering=-price

    http://127.0.0.1:8000/orders/all_orders/?search=Gikondo
    """
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['electronic','district_name','^sector_name','price','weight','description','customer__username']

    

    @swagger_auto_schema(operation_description="listing all orders",
                         operation_summary="listing all orders")
    def get(self,request:Request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    @swagger_auto_schema(operation_description="send us an order",
                         operation_summary="send us an order")
    def post(self,request:Request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    
class View_an_Order(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class=Item_Serializer
    queryset=Electronic_Item.objects.all()
    pagination_class=CustomPaginator
    
    @swagger_auto_schema(operation_description="view single order",
                         operation_summary="view single order")
    def get(self, request:Request, *args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    

    
class Update_Your_Order(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class=Item_Serializer
    queryset=Electronic_Item.objects.all()

    @swagger_auto_schema(operation_description="update your order",
                         operation_summary="change your order")
    def put(self, request:Request, *args,**kwargs):
        return self.update(request,*args,**kwargs)
    


    
class Remove_Your_Order(generics.GenericAPIView, mixins.DestroyModelMixin):
    serializer_class=Item_Serializer
    queryset=Electronic_Item.objects.all()

    @swagger_auto_schema(operation_description="remove an order",
                         operation_summary="delete an order")
    def delete(self, request:Request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
# let's have orders depending on type of Electronic bought

class Orders_per_type_of_item(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class=Item_Serializer
    queryset=Electronic_Item.objects.all()
    
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['electronic','district_name','^sector_name','price','weight','description','customer__username']

    pagination_class=CustomPaginator

    """ 
    To use this end point you must provide which item type, 
    choose among {phones,laptops,dektops,appliances}
     just like: 
    http://127.0.0.1:8000/orders/item_name/?electronic=phones
    """
    @swagger_auto_schema(operation_summary="orders for specific electronic item",
                         operation_description="You will need to pass" 
                         " an electronic item from choose among {phones,laptops,dektops,appliances}"
                         " to use this end point you must add query ?electronic="
                         "  say for instance:    http://127.0.0.1:8000/orders/item_name/?electronic=phones "
                         
                         )
    def get(self, request:Request):
        kind_of_item=self.request.query_params.get('electronic')
        filtered_kinds=Electronic_Item.objects.all().filter(electronic=kind_of_item)

        serializer=self.serializer_class(instance=filtered_kinds, many=True)

        if kind_of_item is not None:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(data={"Query Not found"})
        


# orders requested per single district

class Orders_per_District(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=Item_Serializer
    pagination_class=CustomPaginator
    
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['electronic','district_name','^sector_name','price','weight','description','customer__username']

    queryset=Electronic_Item.objects.all()

    """
    To check orders per district you will need to choose among:
    {kicukiro,Gasabo,Nyarugenge}
    say for instance: 

    http://127.0.0.1:8000/orders/single_district/?district_name=Gasabo
    """
    @swagger_auto_schema(operation_summary="orders for specific district name",
                         operation_description="You will need to pass" 
                         " district name ,choose among {kicukiro,Nyarugenge ,Gasabo}"
                         " to use this end point you must add query ?district_name="
                         "  say for instance: "   
    "  http://127.0.0.1:8000/orders/single_district/?district_name=Gasabo"
                         
                         )
    def get(self, request:Request):
        district=self.request.query_params.get('district_name')
        per_district=Electronic_Item.objects.all().filter(district_name=district)

        serializer=self.serializer_class(instance=per_district, many=True)

        if district is not None:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(data={"Check if district is in Kigali, please"}, status=status.HTTP_400_BAD_REQUEST)

# suppose we want to know how many computers sold in Kicukiro?

class Single_Item_per_District(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=Item_Serializer
    pagination_class=CustomPaginator
    
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['electronic','district_name','^sector_name','price','weight','description','customer__username']

    queryset=Electronic_Item.objects.all()

    def get(self, request:Request):
        kind_of_item=self.request.query_params.get('electronic')
        district=self.request.query_params.get('district_name')

        filtered=Electronic_Item.objects.all().filter(electronic=kind_of_item).filter(district_name=district)
        serializer=self.serializer_class(instance=filtered, many=True)

        if kind_of_item is not None:
            if district is not None:
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        

        else:
            return Response(data={"check district name and our products carefully"})


    
# get an Order(s) for specific Customer

class Orders_for_Client(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class=Item_Serializer
    pagination_class=CustomPaginator
    
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['electronic','district_name','^sector_name','price','weight','description','customer__username']
    queryset=Electronic_Item.objects.all()

    @swagger_auto_schema(operation_summary="orders per single client",operation_description="Pass client id to get his requested orders")
    def get(self, request:Request, client_id):
        client=User.objects.get(pk=client_id)
        client_orders=Electronic_Item.objects.all().filter(customer=client)

        serializer=self.serializer_class(instance=client_orders, many=True)

        if client is not None:
            return Response(data=serializer.data, status=status.HTTP_302_FOUND)
        
        else:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
    



