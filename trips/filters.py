from django_filters import rest_framework


class TripFilter(rest_framework.FilterSet):
    user_id = rest_framework.CharFilter(
        field_name='user_profile__user__id', lookup_expr='iexact')
    started_at = rest_framework.DateFilter(
        field_name='started_at', lookup_expr='gte')
    ended_at = rest_framework.DateFilter(
        field_name='ended_at', lookup_expr='lte')
