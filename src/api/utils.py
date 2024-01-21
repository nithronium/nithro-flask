def check_fields(required_fields, request):
    for field in required_fields:
        if field not in request.json:
            return False
    return True
