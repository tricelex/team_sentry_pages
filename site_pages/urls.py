from django.urls import path
from site_pages.views import AddPageView, ListAPIView

urlpatterns = [
    path('add-page/',AddPageView.as_view() ),
    # path('list-pages/',ListPageView.as_view() ),
    # path('set-page-markdown/',PageView.as_view() ),
]