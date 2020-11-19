from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductsViewSet, basename='products')
router.register(r'categories', views.CategoriesViewSet)
router.register(r'customers', views.CustomersViewSet)
router.register(r'orders', views.OrdersViewSet)
router.register(r'details', views.OrdersDetailsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]