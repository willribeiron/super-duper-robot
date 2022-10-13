from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from appbanco.views import DepositViewset, TransactionViewset

router = DefaultRouter()
router.register("deposit", DepositViewset, basename="deposit")
router.register("transaction", TransactionViewset, basename="transaction")
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
