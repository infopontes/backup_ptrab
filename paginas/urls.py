from django.urls import URLPattern, path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
]