from django.contrib import admin
from DjangoEcommerceApp.models import Categories, SubCategories, Products, ProductMedia, ProductTransaction, ProductDetails, ProductAbout, ProductTags, ProductQuestions, ProductReviews, ProductReviewVoting, ProductVarient, ProductVarientItems, CustomerOrders, OrderDeliveryStatus, MerchantUser
# Register your models here.

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(ProductMedia)
admin.site.register(ProductTransaction)
admin.site.register(ProductDetails)
admin.site.register(ProductAbout)
admin.site.register(ProductTags)
admin.site.register(ProductQuestions)
admin.site.register(ProductReviews)
admin.site.register(ProductReviewVoting)
admin.site.register(ProductVarient)
admin.site.register(ProductVarientItems)
admin.site.register(CustomerOrders)
admin.site.register(OrderDeliveryStatus)
admin.site.register(MerchantUser)