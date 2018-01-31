from rest_framework import serializers
from django.contrib.auth.models import User
from dynatag.models import Configuration, Application

    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')

'''
class UserappSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Userapp
        fields = ('source', 'Authcontent', 'user', 'create_date')
'''
        
class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Application
        fields = ('appname', 'description', 'apptoken', 'tokenrefresh_time', 'appuri', 'user', 'create_date')
           
class ConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Configuration
        fields = ('type', 'initalnum', 'actualnum', 'prefix', 'suffix', 'pstartdate', 'penddate', 'targetdate', 'application', 'create_date')

     
    
    
    