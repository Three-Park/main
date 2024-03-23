"""
URL configuration for fairy_tairy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from books.views import BookViewSet
from diaries.views import DiaryViewSet, DiaryBookViewSet, DiaryAdminViewSet
from emotion_chat.views import EmotionViewSet
from images.views import ImageAdminViewSet, ImageViewSet
from recommend_music.views import MusicAdminViewSet, MusicViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'diary', DiaryViewSet, basename='diary')
router.register(r'diary_book', DiaryBookViewSet, basename='diary_book')
router.register(r'diary_admin', DiaryAdminViewSet, basename='diary_admin')
router.register(r'emotion', EmotionViewSet, basename='emotion')
router.register(r'image', ImageViewSet, basename='image')
router.register(r'image_admin', ImageAdminViewSet, basename='image_admin')
router.register(r'music',MusicViewSet,basename='music')
router.register(r'music_admin', MusicAdminViewSet, basename='music_admin')


urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 