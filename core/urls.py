from django.urls import path, include
from . import views

Category_Item_id = views.CategoryItemIdViewset.as_view({
    'get': 'retrieve',
})

Table_Order_id = views.TableOrderIdViewset.as_view({
    'get': 'retrieve',
})

app_name = 'core'
urlpatterns = [
    path('api/List_All_Tables/', views.TableAllViewset.as_view()),  # http://127.0.0.1:8000/api/List_All_Tables/
    path('api/List_All_Category/', views.CategoryAllViewset.as_view()),  # http://127.0.0.1:8000/api/List_All_Category/
    path('api/List_All_Item/', views.ItemAllViewset.as_view()),  # http://127.0.0.1:8000/api/List_All_Item/
    path('api/Category_Item_All/', views.CategoryItemAllViewset.as_view()),# http://127.0.0.1:8000/api/Category_Item_All/
    path('api/Category_Item_id/<int:pk>', Category_Item_id),  # http://127.0.0.1:8000/api/Category_Item_id/2
    path('api/Table_Order_All/', views.TableOrderAllViewset.as_view()),  # http://127.0.0.1:8000/api/Table_Order_All
    path('api/Table_Order_id/<int:pk>', Table_Order_id),#http://127.0.0.1:8000/api/Table_Order_id/3

]
