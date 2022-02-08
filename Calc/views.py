from django.shortcuts import redirect, render
import numpy as np
import numpy_financial as npf

def home(request):
    return render(request, 'Calc/home.html')

def calculate(request):
    
    if request.GET.get('rate') and request.GET.get('per') and request.GET.get('pmt') and request.GET.get('pv'):
        rate = float(request.GET.get('rate'))
        per = int(request.GET.get('per'))
        pmt = int(request.GET.get('pmt'))
        pv = int(request.GET.get('pv'))
        x = round(npf.fv(rate/100/12, per, -pmt, -pv), 2)
        return render(request, 'Calc/calculate.html', {'x':x, 'rate':rate, 'per':per, 'pmt':pmt, 'pv':pv})
    else:
        return redirect(home)