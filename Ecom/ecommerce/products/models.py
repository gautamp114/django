from django.db import models
# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank= True)
	price = models.DecimalField(decimal_places=2,max_digits=20,default=30.00)
	sales_price = models.DecimalField(decimal_places=2,max_digits=20,null=True, blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add= True, auto_now=False)
	updated = models.DateTimeField(auto_now_add= False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	class Meta:
		#to make title and slug unique together
		unique_together = ('title', 'slug')

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add= False, auto_now=True)


	def __str__(self):
		return self.product.title

# class OrderProduct(models.Model):
# 	product = models.ForeignKey(Product, on_delete= models.CASCADE)
#
# 	def __str__(self):
# 		return self.product.title
#
# class Order(models.Model):
# 	items = models.ManyToManyField(OrderProduct)
# 	ordered_date = models.DateTimeField(auto_now_add=True)
# 	ordered = models.BooleanField(default=False)
#
# 	def __str__(self):
# 		return self.order.items
