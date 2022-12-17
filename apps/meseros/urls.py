from django.urls import path
from . import views
urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_list_vc/', views.MeserosList.as_view(), name='meseros_list_vc'),
    path('meseros_delete_vc/<int:pk>/', views.MeserosDelete.as_view(), name='meseros_delete_vc'),
    path('meseros_create_vc/', views.MeserosCreate.as_view(), name='meseros_create_vc'),
    path('meseros_edit_vc/<int:pk>/', views.MeserosUpdate.as_view(), name='meseros_edit_vc'),
    path('meseros_list_drf_def/', views.meseros_api_view, name='owner_list_rf_def'),
    # URLs Django RESTFRAMEWORK
    path('meseros_list_drf_def/', views.meseros_api_view, name='meseros_list_rf_def'),
    path('meseros_detail_drf_def/<int:pk>', views.meseros_detail_view, name='meseros_detail_rf_def')


# URLs serializers
    # path('meseros_list_serializer/', views.ListMeserosSerializer(), name='meseros_list_srr')
]