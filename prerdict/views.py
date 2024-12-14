from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .mdel import PostQualityPredictor

def predict_price(request):
    prediction = None
    if request.method == 'POST':
        try:
            reputation = float(request.POST.get('reputation'))
            mpxr = float(request.POST.get('mpxr'))
            print(reputation)
            print(mpxr)
            # age = float(request.POST.get('mpxr'))
            
            predictor = PostQualityPredictor()
            prediction = predictor.predict(reputation, mpxr)
        except (ValueError, TypeError):
            prediction = "Invalid input"
    
    return render(request, 'predict.html', {'prediction': prediction})