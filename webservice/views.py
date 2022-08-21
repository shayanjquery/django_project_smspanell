from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import MessageSerializer
from django.http import HttpResponse
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from kavenegar import *
# import requests
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import time
import webbrowser as web
import pyautogui as pg


# Create your views here.

@swagger_auto_schema(methods=['post',],request_body=MessageSerializer )
@api_view(['POST'])
def send_message(request):
    serializers = MessageSerializer(data=request.data)
    if serializers.is_valid():

        if serializers.data['Service'] == 'telegram':
            proxiess = {
                'https': '198.59.191.234:8080',
            }
            bot_token = '5517900793:AAF8yg0Ns5Apkl2y3ZvAmRyK0J4jZlFt3Y4'
            bot_chatID = '-710909527'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + serializers.data['Context']
            requests.get(send_text, proxies=proxiess)
        elif serializers.data['Service'] == 'whatsapp':
            ph = serializers.data['Phone']
            Phone = "+98" + ph
            web.open('https://web.whatsapp.com/send?phone=' + Phone + '&text=' + serializers.data['Context'])
            time.sleep(10)
            pg.press('enter')

        elif serializers.data['Service'] == 'sms':

            try:
                api = KavenegarAPI(
                    '79663078784A3566367245647066555746303363624B744A727A6364703749414174374977424D6D706E453D')
                params = {
                    'sender': '10008663',
                    'receptor': serializers.data['Phone'],
                    'message': serializers.data['Context'],
                }
                response = api.sms_send(params)
                print(response)
            except APIException as e:
                print(e)
            except HTTPException as e:
                print(e)
            return Response({"Status": "Success"}, status=status.HTTP_200_OK)
        return Response({"Status": "Success"}, status=status.HTTP_200_OK)

