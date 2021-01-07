from django.shortcuts import render, Http404, redirect
from products.models import Product, ProductImage

# Create your views here.
def home(request):
		all_products = Product.objects.all()
		context = {'products':all_products}
		template = 'home.html'
		return render(request,template,context)

def search(request):
	# print ('hello')
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query': q, 'products': products}
		template = 'results.html'
	else:
		template = 'home.html'
		context = {}
	return render(request,template,context)


def single(request, slug):
		product = Product.objects.get(slug=slug)
		images = product.productimage_set.all()
		context = {'product':product, 'images':images}
		template = 'single_product.html'
		return render(request,template,context)
