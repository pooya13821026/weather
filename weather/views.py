from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import xmltodict
import json

from .requestapi import get_weather
from .serializers import WeatherSerializer


class WeatherDetail(APIView):
    def get(self, request):
        serializer = WeatherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.validated_data['city']
        weather_data = get_weather(city)
        return Response(weather_data)

    def post(self, request):
        serializer = WeatherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = serializer.validated_data['city']
        weather_data = get_weather(city)
        return Response(weather_data)
