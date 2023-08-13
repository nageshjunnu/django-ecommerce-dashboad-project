from django.contrib import admin
from django.urls import path
from DjangoEcommerceApp import views,AdminViews
from django.conf.urls.static import static
from DjangoEcommerce import settings
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("admin/", views.adminLogin, name="admin_login"),
    path('demo', views.demoPage),
    path('demoPage', views.demoPageTemplate,name="demoPage"),
    path('admin_login_process', views.adminLoginProcess, name="admin_login_process"),
    path('admin_logout_process', views.adminLogoutProcess, name="admin_logout_process"),
    

    #Page For Admin
    path('admin_home', AdminViews.admin_home, name="admin_home"),
   
    #Catgory     
    path("category_list", AdminViews.CategoriesListView.as_view(), name="category_list"),
    path("category_create", AdminViews.CategoriesCreate.as_view(), name="category_create"),
    path("category_update/<slug:pk>", AdminViews.CategoriesUpdate.as_view(), name="category_update"),
    
    # Sub Category
    path("sub_category_list", AdminViews.SubCategoriesListView.as_view(), name="sub_category_list"),
    path("sub_category_create", AdminViews.SubCategoriesCreate.as_view(), name="sub_category_create"),
    path("sub_category_update/<slug:pk>", AdminViews.SubCategoriesUpdate.as_view(), name="sub_category_update"),
    
    #Merchant User
    path("merchant_create", AdminViews.MerchantUserCreate.as_view(), name="merchant_create"),
    path("merchant_list", AdminViews.MerchantUserListView.as_view(), name="merchant_list"),
    path("merchant_update/<slug:pk>", AdminViews.MerchantUserUpdateView.as_view(), name="merchant_update"),
    
    # Products
    path("product_create", AdminViews.ProductView.as_view(), name="product_create"),
    path("file_upload", AdminViews.file_upload, name="file_upload"),
    path('product_list',AdminViews.ProductListView.as_view(),name="product_list"),
    
]