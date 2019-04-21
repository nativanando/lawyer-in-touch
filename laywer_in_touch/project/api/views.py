from django.contrib.auth.models import User, Group
from .models import Customer, Lawyer, Contract
from rest_framework import viewsets
from rest_framework.decorators import action
from project.api.serializers import UserSerializer, GroupSerializer, CustomerSerializer, LawyerSerializer, ContractSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    """
    This is a new endpoint example
    """
    @action(detail=False, methods=['get'])
    def recent_users(self, request):
        """
        example of raw query called from serializer
        """
        return UserSerializer.recent_users(self)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class LawyerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
