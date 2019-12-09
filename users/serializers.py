from rest_framework import serializers
from users.models import CustomUser
from users.utils import generate_activation_code


class RegisterSerializer(serializers.ModelSerializer):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    # password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
            'password2'
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data["email"], validated_data["password"])
        user.is_active = False
        user.activation_code = generate_activation_code()
        # send_code.delay()
        return user


class ActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'activation_code',
        )

    def update(self, instance, validated_data):
        instance.is_active = True
        return instance


#
# class PaymentCallbackSerializer(serializers.ModelSerializer):
#     """
#     "id": 145,
#     "hash": "8d00fa317124196405bf72d6f6a61636b76f8ecf0cf72f171afe68edcebd2fb4",
#     "to": "1HqfAERDGvv2Mwuc2UPB5dXC4RHFNdG9QQ",
#     "_from": "1XXXAERDGvv2Mwuc2UPB5dXC4RHFNdG9QQ",
#     "amount": 0.01,
#     "currency": "ETH",
#     "confirmations": 10,
#     "confirmed": True
#     """
#     id = serializers.IntegerField()
#
#     class Meta:
#         fields = (
#             "id",
#             "hash",
#             "_from",
#             "_to",
#             "currency",
#             "amount",
#             "confirmations",
#             "confirmed",
#         )
#         model = Invoice
#
#     def update(self, instance, validated_data):
#         if not instance.transaction_id:
#             instance.transaction_id = validated_data["id"]
#             instance.hash = validated_data["hash"]
#             instance._from = validated_data["_from"]
#
#         if validated_data["confirmations"] > instance.confirmations:
#             instance.confirmations = validated_data["confirmations"]
#
#         if validated_data["confirmed"]:
#             instance.confirmed = validated_data["confirmed"]
#
#         # deal with status
#         if instance.status == 'new':
#             if validated_data["amount"] < instance.amount:
#                 instance.status = "invalid"
#             else:
#                 if instance.confirmed:
#                     instance.status = "complete"
#                 else:
#                     instance.status = "paid"
#
#         instance.save()
#         return instance
#



