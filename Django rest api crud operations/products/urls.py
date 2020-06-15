from django.urls import path
from.import views

urlpatterns = [
    path("product/",views.home,name='home'),
    path("product/<int:pk>",views.product_detail),
    path("export",views.export,name='example'),
    path("url_api",views.url_api,name='url_api')


]