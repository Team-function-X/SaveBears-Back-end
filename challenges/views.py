from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views, status
import requests
import time


def get_random_challenge():
    return 1


class GetChallengeImage(views.APIView):
    """
    AWS Lamda 서버로부터 사진분석 결과를 가져옴
    Plastic,
    """

    def get(self, request):
        image = request.GET['image']
        point = 0
        req = 0
        while req != 10:
            result = requests.get(
                f"https://th5a2rg7k4.execute-api.ap-northeast-2.amazonaws.com/api/{image}")
            if result.status_code == status.HTTP_200_OK:
                break
            req += 1
            print(req)
            if req == 9:
                return JsonResponse({"err_message": "Error Occurred When parsing image"}, status=status.HTTP_400_BAD_REQUEST)
        result_json = result.json()
        labels = result_json['labels']
        print(labels)
        if "Plastic" in labels:
            point += 1
        if "Aluminium" in labels:
            point += 1

        return JsonResponse({"point": point}, status=status.HTTP_200_OK)
