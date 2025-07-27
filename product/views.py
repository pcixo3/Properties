from django.shortcuts import render, get_object_or_404
from .models import Estate, Category


def index_view(request):
    parent_categories = Category.objects.filter(parent_category__isnull=True)
    estates = Estate.objects.filter(is_active=True)

    return render(request,
                  'main/index.html',
                  {'estates': estates,
                   'parent_categories': parent_categories})


def estate_detail_view(request, estate_id):
    estate = get_object_or_404(Estate, id=estate_id)
    category = estate.category

    return render(
        request=request,
        template_name='main/estate_detail.html',
        context={'estate': estate,
                 'category': category}
    )


def price_detail_view(request, estate_id):
    estate = get_object_or_404(Estate, id=estate_id)

    return render(
        request=request,
        template_name='main/price_detail.html',
        context={'estate': estate}
    )