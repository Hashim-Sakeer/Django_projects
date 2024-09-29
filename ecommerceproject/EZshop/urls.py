from django.urls import path
from . import views

app_name='EZshop'

urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:cslug>/',views.allprodcat,name='products_by_category'),
    path('<slug:cslug>/<slug:pslug>/',views.proDetail,name='procatdetail'),
]
