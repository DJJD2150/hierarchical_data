from django.shortcuts import render
from hierarchical_data_app.models import Data

# Create your views here.
def show_data(request):
    return render(request, "data.html", {'data': Data.objects.all()})