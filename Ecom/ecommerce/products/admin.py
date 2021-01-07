from django.contrib import admin

from .models import Product, ProductImage

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	#to display the column for admin
	list_display=['title','price','active','updated']
	#to allow admin to edit
	list_editable=['price', 'active']
	#for readonly fields for admin
	readonly_fields=['timestamp','updated']
	#to use the same name as that of title
	prepopulated_fields = {"slug":("title",)}
	class meta:
		model = Product


admin.site.register(Product,ProductAdmin)

admin.site.register(ProductImage)

# admin.site.register(UserRegistration)
#
# admin.site.register(OrderProduct,Order)
