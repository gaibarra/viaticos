from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AuthorizedTravel, EmployeeProfile, TravelExpense
from .serializers import AuthorizedTravelSerializer, EmployeeProfileSerializer, TravelExpenseSerializer

class AuthorizedTravelViewSet(viewsets.ModelViewSet):
    queryset = AuthorizedTravel.objects.all()
    serializer_class = AuthorizedTravelSerializer

class EmployeeProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer

class TravelExpenseViewSet(viewsets.ModelViewSet):
    queryset = TravelExpense.objects.all()
    serializer_class = TravelExpenseSerializer

    @action(detail=True, methods=['get'])
    def expenses_by_type(self, request, pk=None):
        travel_expense = self.get_object()
        expense_type_count = {
            'Hospedaje': 0,
            'Alimentación': 0,
            'Transporte': 0,
        }

        for expense in travel_expense:
            if expense.expense_type == 'Hospedaje':
                expense_type_count['Hospedaje'] += 1
            elif expense.expense_type == 'Alimentación':
                expense_type_count['Alimentación'] += 1
            elif expense.expense_type == 'Transporte':
                expense_type_count['Transporte'] += 1

        return Response(expense_type_count)
    
    
    
    
    
    
