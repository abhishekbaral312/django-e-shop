from django.shortcuts import redirect,render
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import ListView
from django.db.models import Count


class Store(View):
    def get(self, request):
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None;
        categories = Category.get_all_categories();
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_categoryid(categoryId)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['page_obj'] = page_obj


        return render(request, 'store.html', data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        data2 ={}
        data2['page_obj']=page_obj

        return render(request,'store.html',data2)


