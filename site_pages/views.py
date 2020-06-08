from site_pages.models import AddPage
from site_pages.serializers import PageSerializer
from rest_framework.generics import CreateAPIView, ListAPIView


class AddPageView(CreateAPIView):
    queryset = AddPage.objects.all()
    serializer_class = PageSerializer

class ListPageView(ListAPIView):
    pass
    


# Create your views here.
