import json
from django.core.exceptions import ValidationError

def parse_request_data(request):
    if not request.body:
        raise ValidationError("Request body is empty")

    try:
        return json.loads(request.body).get("data")
    except json.JSONDecodeError as e:
        raise ValidationError(f"Invalid JSON data: {str(e)}")
