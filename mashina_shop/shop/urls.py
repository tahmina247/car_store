from django.urls import path
from .views import *

urlpatterns = [
    path('', CarViewSet.as_view({'get':'list',
                                 'post':'create'}), name='car_list'),
    path('<int:pk>/', CarViewSet.as_view({'get':'retrieve',
                                          'put':'update',
                                          'delete':'destroy'}), name='car_detail'),
    path('', CarMarkaViewSet.as_view({'get':'list',
                                      'post':'create'}), name='carmarka_list'),
    path('<int:pk>/', CarMarkaViewSet.as_view({'get':'retrieve',
                                               'put':'update',
                                               'delete':'destroy'}), name='carmarka_detail'),
    path('', CarModelViewSet.as_view({'get':'list',
                                      'post':'create'}), name='carmodel_list'),
    path('<int:pk>/', CarModelViewSet.as_view({'get':'retrieve',
                                               'put':'update',
                                               'delete':'destroy'}), name='carmodel_detail')
]
