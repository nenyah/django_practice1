# Create your views here.
# 引入序列化类
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# 引入rest_framework相关模块
from rest_framework.views import APIView

# 引入数据表
from .models import Type1, Type2, Type3, Type4
from .serializers import Type1ModelSerializer, Type2ModelSerializer
from .serializers import Type3ModelSerializer, Type4ModelSerializer


# Create your views here.
class Type1View(APIView):
    """
    all Type1
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type1.objects.all()
        Types_serializer = Type1ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)


class Type2View(APIView):
    """
    all Type2
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type2.objects.all()
        Types_serializer = Type2ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)


class Type3View(APIView):
    """
    all Type3
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type3.objects.all()
        Types_serializer = Type3ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)


class Type4View(APIView):
    """
    all Type4
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type4.objects.all()
        Types_serializer = Type4ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)
