from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views, status
import requests


class GetChallengeImage(views.APIView):
    """
    AWS Lamda 서버로부터 사진분석 결과를 가져옴
    """

    def get(self, request, a):
        print(a)
        print("1")
        result = requests.get(
            f"https://th5a2rg7k4.execute-api.ap-northeast-2.amazonaws.com/api/test.jpeg")
        result_json = result.json()
        return JsonResponse(result_json, safe=False)
