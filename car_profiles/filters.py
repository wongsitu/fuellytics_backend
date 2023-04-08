from django_filters import rest_framework


class CarProfileFilter(rest_framework.FilterSet):
    user_id = rest_framework.CharFilter(
        field_name='user__id', lookup_expr='iexact')
