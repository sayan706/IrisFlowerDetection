from django.shortcuts import render
from requests import post
import joblib
# Create your views here.
def index(request):
    return render(request,'index.html')

def preprocessdata(slen,swid,plen,pwid):
    test_data=[[slen,swid,plen,pwid]]
    trained_model=joblib.load("model.pkl")
    prediction=trained_model.predict(test_data)
    return prediction

def predict(request):
    if request.method=='POST':
        slen = float(request.POST.get('slen'))
        swid = float(request.POST.get('swid'))
        plen = float(request.POST.get('plen'))
        pwid = float(request.POST.get('pwid'))
        
        prediction=str(preprocessdata(slen,swid,plen,pwid))
        data = {'SAYAN':prediction}

        return render(request,'prediction.html',context=data)
    return render(request,'prediction.html')
