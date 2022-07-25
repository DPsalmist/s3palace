from django.shortcuts import render, get_object_or_404
from .models import Suits, Category, Sub_Category
from cart.forms import CartAddProductForm
from django.db.models import Q 

# Create your views here.

def about(request, category_slug=None):
    category = None
    subcategories = Sub_Category.objects.all()
    suits = Suits.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Sub_Category, slug=category_slug)
        suits = suits.filter(category=category)
    
    context = {
		'category': category,
        'suits':suits,
        'subcategories': subcategories
     }
    return render(request, 'shop/product/about.html', context)

def contact(request, category_slug=None):
     category = None
     subcategories = Sub_Category.objects.all()
     suits = Suits.objects.filter(available=True)
     
     if category_slug:
         category = get_object_or_404(Sub_Category, slug=category_slug)
         suits = suits.filter(category=category)
     context = {
         'category': category,
        'suits':suits,
        'subcategories': subcategories
     }
     return render(request, 'shop/product/contact.html', context)

def home_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    subcategories = Sub_Category.objects.all()
    #products = Product.objects.filter(available=True)
    all_suits = Suits.objects.filter(available=True)
    #shoes = Shoes.objects.filter(available=True)

    # Filters
    suits = Suits.objects.filter(available=True).order_by('created')[:12]
    cheap_suits = 40000
    last_suit = Suits.objects.filter(available=True).last()
    #cheap_suits = Suits.objects.filter(available=True).filter(price__range())
    penultimate_suit = Suits.objects.filter(available=True).order_by('-created')[0:1]
    pen_suit = penultimate_suit[0]
    
    # Category Filters 
    chinese_suits = all_suits.filter(category__id__exact=2).order_by('-created')[0:3]
    italian_suits = all_suits.filter(category__id__exact=1).order_by('-created')[0:3]
    turkey_suits = all_suits.filter(category__id__exact=3).order_by('-created')[0:3]

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        subcategory = get_object_or_404(Sub_Category, slug=category_slug)
       # products = products.filter(category=category)
        suits = suits.filter(category=subcategory)
        
    context = {
		'category': category,
        'last_suit':last_suit,
        'pen_suit':pen_suit,
        'suits':suits,
        'categories': categories,
        #'products': products,
        'subcategories': subcategories,
        'italian_suits':italian_suits,
        'chinese_suits':chinese_suits,
        'turkey_suits':turkey_suits
        }
    return render(request,'shop/product/index.html', context)

def suit_detail(request, id, slug):
    suit = get_object_or_404(Suits, id=id, slug=slug, available=True)
    subcategories = Sub_Category.objects.all()
    cart_product_form = CartAddProductForm()
    print('This is suit detail=', suit)
    context = {
		'suit': suit,
        'subcategories':subcategories,
		'cart_product_form': cart_product_form,
	}
    return render(request,'shop/product/suit_detail.html',context)

def category_list(request, category_slug=None):
    category = None
    subcategories = Sub_Category.objects.all()
    suits = Suits.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Sub_Category, slug=category_slug)
        suits = suits.filter(category=category)
    
    for a in suits:
        print('This is suit:',a, a.get_absolute_url)
        
    context = {
		'category': category,
        'suits':suits,
        'subcategories': subcategories
        }
    return render(request,'shop/product/suit_category_list.html', context)

def search(request):
    # get search query
    search_query = request.GET.get('q')
    subcategories = Sub_Category.objects.all()
    
    print('search object: ', search_query)
    suits = Suits.objects.filter(Q(name__icontains=search_query) | Q(category__name__icontains=search_query)).filter(available=True).order_by('created')
    print('returned search results = ', suits)
    context = {'suits':suits, 'search_query':search_query, 'subcategories':subcategories}

    return render(request, 'shop/product/search_results.html', context)
    

