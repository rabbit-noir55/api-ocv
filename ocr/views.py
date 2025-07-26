from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utilits import *
# Create your views here.
class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        image = request.FILES.get('image')
        if image:
            # Rasmni o'qish va raqamlarni olish
            numbers = captcha_text(image)
            return Response({"message": numbers}, status=status.HTTP_200_OK)
        return Response({"error": "Rasm topilmadi"}, status=status.HTTP_400_BAD_REQUEST)