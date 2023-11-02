from django.contrib import admin
from django.urls import path
from.import views

app_name='ewebapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail,name='prodCatdetail')
]
