from payment.models import CreditCard
from rest_framework import serializers

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('id', 'owner', 'credit_no', 'ccv', 'expire_date')
