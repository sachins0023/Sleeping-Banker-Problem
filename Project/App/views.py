from django.shortcuts import render
from .models import User, Session
from .serializers import UserSerializer, SessionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import copy
# Create your views here.

@api_view(['GET',])
def api_user_list(request):
    user = User.objects.all()
    if request.method == "GET":
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
@api_view(['POST',])
def api_user_create(request):
    if request.method == "POST":
        # print(type(headers))
        # print(type(request.data))
        headers = dict((header, value) for (header, value) in request.META.items() if (header.startswith('HTTP_') or header.startswith('REMOTE_')))
        # print(dict(request.data))\
        req_query = dict(request.data)
        print("".join(req_query["mobile_number"]))
        if User.objects.filter(mobile_number=("".join(req_query["mobile_number"])), user_name=("".join(req_query["user_name"]))):
            user = User.objects.get(mobile_number=("".join(req_query["mobile_number"])), user_name=("".join(req_query["user_name"])))
            serializer = UserSerializer(user)
            serializer_data = copy.copy(serializer.data)
            serializer_data["headers"] = json.dumps(headers)
            return Response(serializer_data)
        request_data = copy.copy(request.data)
        request_data["headers"] = json.dumps(headers)
        # request_data = json.dumps(request_data)
        serializer = UserSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data["success"] = "Created Successfully"
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET',])
def api_session_list(request):
    session = Session.objects.all()
    if request.method == "GET":
        serializer = SessionSerializer(session, many=True)
        return Response(serializer.data)