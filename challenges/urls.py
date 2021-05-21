from django.urls.conf import path
from .views import *


urlpatterns = [
    path("image-data", GetChallengeImage.as_view(), name="image_data")
]
