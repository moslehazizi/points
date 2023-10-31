from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # django-admin
    path('admin/', admin.site.urls),

    #user-management
    path('accounts/', include('allauth.urls')),

    #local-app
    path('', include('pages.urls')),
    path('student/', include('students.urls')),
    path('messenger/', include('messenger.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
