from miniflask.app.services.example_service import add_two_numbers

def sum_api(a, b):
    return {"result": add_two_numbers(a, b)}