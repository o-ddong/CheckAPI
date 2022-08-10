
import json

from django.core import serializers
from django.db.models import (Sum, Count, Case, When, Avg,
                              IntegerField, Value, F)
from django.http import HttpResponse

from django.shortcuts import render

from .models import Whitelist, Blacklist

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WhitelistSerializer, BlacklistSerializer, BlacklistPackageCntSerializer, \
    WhitelistPackageCntSerializer

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'select/index.html')

class CheckAPI:
    def __init__(self):
        self.whitelist_cert_sha1_table = 0
        self.blacklist_cert_sha1_table = 0

    def certCount(self, hash_value):
        self.whitelist_cert_sha1_table = Whitelist.objects.filter(cert_sha1=hash_value)
        self.blacklist_cert_sha1_table = Blacklist.objects.filter(cert_sha1=hash_value)

    def getResult(self):
        if self.whitelist_cert_sha1_table or self.blacklist_cert_sha1_table:
            result = {'flag': 1, 'whiteCnt': len(self.whitelist_cert_sha1_table), \
                      'blackCnt': len(self.blacklist_cert_sha1_table)}
        else:
            result = {'flag': 0, 'whiteCnt': len(self.whitelist_cert_sha1_table), \
                      'blackCnt': len(self.blacklist_cert_sha1_table)}
        return result

def query(hash_value, selectlist, num):
    return selectlist.objects \
                        .filter(cert_sha1=hash_value) \
                        .values('cert_sha1', 'packagename') \
                        .annotate(cnt = Count('packagename')) \
                        .order_by('-cnt')[:num]

class certSelect(APIView):
    @csrf_exempt
    def get(self, request):
        hash_value = request.data['cert_sha1_hash']
        checkApi = CheckAPI()
        checkApi.certCount(hash_value)
        return Response(checkApi.getResult())

class certPackage(APIView):
    def get(self, request):
        hash_value = request.data['cert_sha1_hash']
        num = int(request.data['num1'])

        blackResult = query(hash_value, Blacklist, num)
        whiteResult = query(hash_value, Whitelist, num)

        try:
            blackSerializer = BlacklistPackageCntSerializer(blackResult, many=True)
            whiteSerializer = WhitelistPackageCntSerializer(whiteResult, many=True)
            jsonData = {
                'Whitelist' : whiteSerializer.data,
                'Blacklist' : blackSerializer.data
            }
            return HttpResponse(json.dumps(jsonData))

        except Exception as e:
            print(e)