
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('detail/<int:estate_id>', views.estate_detail_view, name='estate_detail'),
    path('price/<int:estate_id>', views.price_detail_view, name='price_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
