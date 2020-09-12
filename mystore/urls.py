from django.contrib import admin
from django.urls import path
from mystore import views
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = "mystore"

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^product_detail/(\d+)/$', views.product_detail, name='product_detail'),
    url(r'^tao_cookie/(\d+)/$', views.tao_cookie, name='tao_cookie'),
    url(r'^doc_cookie/(\d+)/$', views.doc_cookie, name='doc_cookie'),
    url(r'^xoa_cookie/(\d+)/$', views.xoa_cookie, name='xoa_cookie'),
]