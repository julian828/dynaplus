from rest_framework import serializers
from django.contrib.auth.models import User
from dynatag.models import Configuration, Application


    
class UserSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")  #HyperlinkedModelSerializer
        
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')

'''
class UserappSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Userapp
        fields = ('source', 'Authcontent', 'user', 'create_date')
'''
        
class ApplicationSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    #user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Application
        fields = ('id', 'appname', 'description', 'apptoken', 'tokenrefresh_time', 'appuri', 'user', 'create_date')
           
class ConfigurationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Configuration
        fields = ('id', 'confname','type', 'initalnum', 'actualnum', 'prefix', 'suffix', 'pstartdate', 'penddate', 'targetdate', 'application', 'create_date')

     
    
    
    