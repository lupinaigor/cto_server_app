from django.http import JsonResponse

def success_response(data, message="Success"):
    return JsonResponse({
        "success": True,
        "message": message,
        "data": data
    })

def error_response(message="Error", data=None, status_code=400):
    return JsonResponse({
        "success": False,
        "message": message,
        "data": data
    }, status=status_code)
