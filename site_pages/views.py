from site_pages.models import AddPage
from site_pages.serializers import PageSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


class AddPageView(CreateAPIView):
    queryset = AddPage.objects.all()
    serializer_class = PageSerializer


class ListPageView(ListAPIView):
    queryset = AddPage.objects.all()
    serializer_class = PageSerializer 


class UpdatePageView(RetrieveUpdateAPIView):
    queryset = AddPage.objects.all()
    serializer_class = PageSerializer 
    fields = ['content']


class PageContentView(APIView):
    renderer_classes = [StaticHTMLRenderer]

    def get(self, request, pk):
        obj = get_object_or_404(AddPage, pk=pk)
        data = PageSerializer(obj)["content"]
        return Response(data)


# Create your views here.
