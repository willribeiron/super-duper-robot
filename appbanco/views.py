from rest_framework import mixins, viewsets
from appbanco.serializers import DepositSerializer, TransactionSerializer
from appbanco.models import Deposit, Transaction


class TransactionViewset(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class DepositViewset(viewsets.ModelViewSet):
    serializer_class = DepositSerializer
    queryset = Deposit.objects.all()
