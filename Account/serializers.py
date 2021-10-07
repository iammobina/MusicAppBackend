from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'email2', 'password', 'name', 'username', 'lastname', 'phonenumber', 'agreetoterms')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def validate(self, attrs):
        email = attrs.get('email')
        email2 = attrs.get('email2')

        user = self.context.get('request')

        if email == email2:
            return attrs
        else:
            raise serializers.ValidationError('Emails Must match')

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class ArtistSerializer(serializers.ModelSerializer):
    singerfacebooklinks = serializers.CharField()
    singerinstalink = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ('email', 'email2', 'password', 'name', 'username', 'lastname', 'phonenumber', 'singerfacebooklinks',
                  'singerinstalink')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def validate(self, attrs):
        email = attrs.get('email')
        email2 = attrs.get('email2')

        user = self.context.get('request')

        if email == email2:
            return attrs
        else:
            raise serializers.ValidationError('Emails Must match')

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'email2', 'password', 'name', 'username', 'lastname', 'phonenumber', 'artworks')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def validate(self, attrs):
        email = attrs.get('email')
        email2 = attrs.get('email2')

        user = self.context.get('request')

        if email == email2:
            return attrs
        else:
            raise serializers.ValidationError('Emails Must match')

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
