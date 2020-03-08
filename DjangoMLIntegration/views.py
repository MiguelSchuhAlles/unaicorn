from django.shortcuts import render
from . import fake_model
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    age = int(request.GET["age"])
    #prediction = ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    prediction = ml_predict.prediction_model(1, 1, age, 1, 1, 11, 1, 1)
    return render(request, 'result.html', {'age': prediction})