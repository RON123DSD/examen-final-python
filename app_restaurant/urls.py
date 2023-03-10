from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('apps.clientes.urls')),
    path('meseros/', include('apps.meseros.urls')),
    path('platos/', include('apps.platos.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('apps.meseros.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

