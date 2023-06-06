from django.urls import path
from . import views

urlpatterns=[
    # CRUD for making an order
    path('all_orders/', views.Orders_Listing_CreateViewMixins.as_view(), name='all_orders'),
    path('view_your_order/<int:pk>/',views.View_an_Order.as_view(),name='single_order'),
    path('update_your_order/<int:pk>/',views.Update_Your_Order.as_view(),name='update_order'),
    path('remove_your_order/<int:pk>/',views.Remove_Your_Order.as_view(),name='delete_order'),

    # orders filtered by electronic item
    path('item_name/?electronic=',views.Orders_per_type_of_item.as_view(),name='per_item_name'),
    path('single_district/?district_name=',views.Orders_per_District.as_view(),name='per_district_name'),

    #
   # path('',views.Single_Item_per_District.as_view(),name='single_item_per_district'),

   #orders for certain client
   path('customer/<int:client_id>/', views.Orders_for_Client.as_view(),name='certain_customer'),
   






]