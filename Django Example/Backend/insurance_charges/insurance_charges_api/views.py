from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import pickle

# Create your views here.


@api_view(['POST'])
def InsuranceChargesList(request):
    if request.method == 'POST':
        data = request.data
        age = int(data['age'])
        number_of_children = int(data['children'])
        bmi = float(data['bmi'])
        
        with open('/Users/tategillespie/Desktop/455 TA/Flask Example/Django Example/Backend/insurance_charges/insurance_charges_api/sample_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        prediction = model.predict([[age, bmi, number_of_children]])

        return JsonResponse({'prediction': prediction[0]})
