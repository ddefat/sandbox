from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

from caesar.models.product import Product
from caesar.forms.product import ProductForm, SearchForm

from django.shortcuts import render, redirect
from django import forms


@login_required()
#@permission_required('polls.can_vote', raise_exception=True)
def products_page(request):

    form = SearchForm(request.GET or None)
    #queryset = Product.objects.all()  16 REQUEST TO THE DB
    queryset = Product.objects.all().select_related('borrower').prefetch_related('category') # 6 REQUEST INSTEAD OF 16!!

    if form.is_valid():
        if form.cleaned_data['name']:
            queryset = queryset.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data['category']:
            queryset = queryset.filter(category__name__icontains=form.cleaned_data['category'])
        if form.cleaned_data['borrowed']:
            queryset = queryset.exclude(borrower=None)

    products = queryset

    context = {
        'form' : form,
        'products': products
    }

    # Import render here because of mock_patch render
    # need to be done here; if not, products_page will not render mock_render
    # but the inital render and the test mock will fail (def test_product_page_list(self, mock_render):)
    #from django.shortcuts import render
    # Return the template
    return render(request, 'products.html', context)


@login_required()
def product_detail(request, pk):
    if pk:
        product = Product.objects.get(pk=pk)

    context = {
        'product': product
    }
    # Return the template
    #from django.shortcuts import render
    return render(request, 'product.html', context)


@login_required()
def product_add(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products/list')
    #from django.shortcuts import render
    return render(request, 'add_product.html', {'form': form})


@login_required()
def product_update(request, pk):
    form = ProductForm(request.POST or None, instance=Product.objects.get(pk=pk) or None)
    if form.is_valid():
        form.save()
        return redirect('products:product_detail', pk)
    return render(request, 'add_product.html', {'form': form})


@login_required()
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    form = forms.Form(request.POST or None)
    if form.is_valid():
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect('products:products_list')
    return render(request, 'delete_confirm.html', {'form': form})