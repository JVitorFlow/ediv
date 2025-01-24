from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import Users

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Users
        fields = ('id', 'email', 'name', 'password')

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = Users
        fields = ('id', 'email', 'name', 'password')