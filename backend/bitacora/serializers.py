from django.contrib.auth.models import User
from rest_framework import serializers
from .models import AuthorizedTravel, EmployeeProfile, TravelExpense


class AuthorizedTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedTravel
        fields = '__all__'


class EmployeeProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = EmployeeProfile
        fields = '__all__'


class TravelExpenseSerializer(serializers.ModelSerializer):
    total_amount = serializers.ReadOnlyField()

    class Meta:
        model = TravelExpense
        fields = '__all__'
