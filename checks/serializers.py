from rest_framework import serializers
from .models import Whitelist, Blacklist

class WhitelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whitelist
        # fields = '__all__'
        # fields = ['md5', 'sha256', 'cert_sha1']
        fields = ['cert_sha1', 'packagename']



class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        # fields = '__all__'
        fields = ['cert_sha1', 'packagename']



class WhitelistPackageCntSerializer(serializers.ModelSerializer):
    cnt = serializers.IntegerField()
    class Meta:
        model = Whitelist
        fields = ['cert_sha1', 'packagename', 'cnt']
        depth = 1

class BlacklistPackageCntSerializer(serializers.ModelSerializer):
    cnt = serializers.IntegerField()
    class Meta:
        model = Blacklist
        fields = ['cert_sha1', 'packagename', 'cnt']
        depth = 1