from rest_framework import serializers
from stores.models import Pizzeria, Image
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class PizzeriaListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    def get_absolute_url(self, obj):
         return reverse('pizzeria_detail', args=(obj.pk,))

    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'logo_image',
            'pizzeria_name',
            'city',
            'zip_code',
            'absolute_url'
        ]

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['id', 'image', 'image_title', 'uploded_at']
        model = Image

class PizzeriaDetailSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()
    pizzeria_images = ImageSerializer(many=True, required=False)

    def get_update(self, obj):
        return reverse('pizzeria_update', args=(obj.pk,))

    def get_delete(self, obj):
            return reverse('pizzeria_delete', args=(obj.pk,))

    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'street',
            'city',
            'state',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active',
            'update',
            'delete',
            'pizzeria_images'
       ]

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        UserModel = get_user_model()
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        new_token = Token.objects.create(user=user)
        return user

    class Meta:
        model = get_user_model()
        fields = [ "username", "password"]