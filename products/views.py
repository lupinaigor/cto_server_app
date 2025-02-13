from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
from .models import Product
from decimal import Decimal
from .utils.main import parse_request_data
from .utils.validators import validate_product_data
from .utils.response_helpers import success_response, error_response
from .utils.filters import custom_filter

@require_http_methods(["GET", "POST"])
def all_products(request):
    try:
        if request.method == "GET":
            products = Product.objects.all().values()
            filters = custom_filter(request)
            products = products.filter(filters)
            return success_response(list(products.values())) if products.exists() else error_response("No products found")

        elif request.method == "POST":
            data = parse_request_data(request)
            validate_product_data(data)
            product = Product.objects.create(
                name=data['name'],
                description=data['description'],
                price=Decimal(data['price']),
                category=data['category']
            )
            return success_response(product.__str__())
    except (ValidationError, ValueError) as e:
        return error_response(data=str(e), status_code=400)
    except Exception as e:
        return error_response(data=str(e))

@require_http_methods(["GET", "DELETE", "PUT"])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        if request.method == "GET":
            return success_response(product.__str__())
        elif request.method == "DELETE":
            product.delete()
            return success_response("Product deleted")
        elif request.method == "PUT":
            data = parse_request_data(request)
            validate_product_data(data)
            product.name = data['name']
            product.description = data['description']
            product.price = Decimal(data.get('price', '0.00'))
            product.category = data['category']
            product.save()
            return success_response(message="Product updated", data=product.__str__())
    except Product.DoesNotExist:
        return error_response(f"Product with id-{pk} not found", status_code=404)
    except (ValidationError, ValueError, KeyError) as e:
        return error_response(data=str(e))
    except Exception as e:
        return error_response(data=str(e))

