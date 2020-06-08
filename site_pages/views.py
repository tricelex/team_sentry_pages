from site_pages.models import AddPage
from site_pages.serializers import PageSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView


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

class PageContentView(RetrieveAPIView):
    pass # TODO
# Create your views here.
