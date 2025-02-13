from decimal import Decimal, InvalidOperation
from django.db.models import Q

def custom_filter(request):
    filters = Q()
    price_min = request.GET.get("price_min")
    price_max = request.GET.get("price_max")
    category = request.GET.get("category")
    search = request.GET.get("search")

    if search:
        filters &= Q(name__icontains=search)
    if price_min:
        try:
            price_min = Decimal(price_min)
            filters &= Q(price__gte=price_min)
        except (ValueError, InvalidOperation):
            raise ValueError("Invalid price_min value")
    if price_max:
        try:
            price_max = Decimal(price_max)
            filters &= Q(price__lte=price_max)
        except (ValueError, InvalidOperation):
            raise ValueError("Invalid price_max value")
    if category:
        filters &= Q(category__icontains=category)

    return filters
