from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views, status
import requests
import json


class GetChallengeImage(views.APIView):
    """
    AWS Lamda 서버로부터 사진분석 결과를 가져옴
    Plastic, 
    """

    def get(self, request):
        image = request.GET['image']
        point = 0
        result = requests.get(
            f"https://th5a2rg7k4.execute-api.ap-northeast-2.amazonaws.com/api/{image}")
        result_json = result.json()
        labels = result_json['labels']
        for i in labels:
            if not i.find('Aluminium'):
                point += 1
            if not i.find('Plastic'):
                point += 1
        print(point)
        return JsonResponse(result_json)
