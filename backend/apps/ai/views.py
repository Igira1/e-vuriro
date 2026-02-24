from django.http import JsonResponse

def predict_view(request):
    return JsonResponse({"message": "AI endpoint works!"})