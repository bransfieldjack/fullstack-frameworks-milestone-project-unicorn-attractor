from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from tickets.models import Bugs, Features, Comments
from rest_framework.views import APIView
from rest_framework.response import Response


Users = get_user_model()


def stats(request):
    
    return render(request, 'stats.html')


def get_data(request, *args, **kwargs):
    
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response
    
    
class ChartData(APIView):
    
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