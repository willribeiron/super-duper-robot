from rest_framework import serializers
from appbanco.models import Client, Transaction, Deposit


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        sender = validated_data["sender"]
        receiver = validated_data["receiver"]
        sender.balance -= validated_data["value"]
        receiver.balance += validated_data["value"]
        sender.save()
        receiver.save()
        return Transaction.objects.create(sender=validated_data["sender"], receiver=validated_data["receiver"],
                                          value=validated_data["value"])


class DepositSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        client = validated_data["receiver"]
        client.balance += validated_data["value"]
        client.save()
        return Deposit.objects.create(receiver=validated_data["receiver"], value=validated_data["value"])

