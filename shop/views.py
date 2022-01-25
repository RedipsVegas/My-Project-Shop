from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.views.generic.base import View
from .forms import UserCreateForm
from django.http import HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'shop/login.html'
    success_url = '/shop/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/shop/")


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/shop/login/"
    template_name = "shop/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


def homepage(request):
    return render(request, 'homepage.html')


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {'products': products,
                                                      'categories': categories,
                                                      'category': category,
                                                      })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        })
