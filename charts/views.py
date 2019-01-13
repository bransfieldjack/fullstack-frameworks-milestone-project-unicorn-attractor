from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from tickets.models import Bugs, Features, Comments
from rest_framework.views import APIView
from rest_framework.response import Response


Users = get_user_model() # Retrieves the users form the Users model, to be used in the graph. 


def stats(request):
    
    """
    Renders the stats page. The data will be retrieved from the page using AJAX, no python logic required in this function.
    """
    
    return render(request, 'stats.html')


def get_data(request, *args, **kwargs):
    
    """
    A test function to research returning API data from REST using python logic instead of AJAX. 
    """
    
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response
    
    
class ChartData(APIView):
    
    """
    Returns data from the API endpoint. Passes values into variables to be used in template via AJAX. 
    """
    
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        
        users = Users.objects.all().count()
        comments = Comments.objects.all().count()
        features = Features.objects.all().count()
        bugs = Bugs.objects.all().count()
        
        labels = ["Users", "Comments", "Features", "Bugs"]
        default_items = [users, comments, features, bugs]
        
        data = {
                "labels": labels,
                "default_items": default_items,
            }
        return Response(data)