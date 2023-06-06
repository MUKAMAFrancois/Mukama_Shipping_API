from rest_framework import serializers
from rest_framework.validators import ValidationError

from rest_framework.authtoken.models import Token
from accounts.models import User

class SignUP_Serializer(serializers.ModelSerializer):
    # validation
    email=serializers.EmailField()
    username=serializers.CharField(max_length=80)
    password=serializers.CharField(min_length=8,write_only=True)
    class Meta:
        model=User
        fields=['username','email','password'] 

    # let's create validation to check if the user exists in database

    def validate(self, attrs):
        # check if email exists from attributes / dictionary of emails
        email_exists=User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("Email Already Exists")
        return super().validate(attrs)
    
    
    # we need to make password to be unseen  in databse
    # override
    def create(self, validated_data):
        password=validated_data.pop("password")
        user=super().create(validated_data)
        user.set_password(password)
        #token creation for each user
          
        user.save()
        return user




