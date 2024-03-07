
from . import views
from django.urls import path
app_name='myapp'



urlpatterns = [

    # path('', views.home,name='home'),
    path('', views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat,name='products-by-category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetails,name='prodetails'),
]