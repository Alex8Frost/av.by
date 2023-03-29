import django_filters
import back.models as models


class TransportAdFilter(django_filters.FilterSet):
    # mark__iexact = django_filters.NumberFilter(field_name='mark', lookup_expr='iexact')
    model__iexact = django_filters.NumberFilter(field_name='model', lookup_expr='iexact')

    mark = django_filters.CharFilter(field_name='mark__name', lookup_expr='iexact')

    year_lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte')
    year_gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte')

    price_lte = django_filters.NumberFilter(field_name='price_in_dollar', lookup_expr='lte')
    price_gte = django_filters.NumberFilter(field_name='price_in_dollar', lookup_expr='gte')

    engine = django_filters.CharFilter(field_name='engine', lookup_expr='iexact')
    engine_cap_lte = django_filters.NumberFilter(field_name='engine_capacity', lookup_expr='lte')
    engine_cap_gte = django_filters.NumberFilter(field_name='engine_capacity', lookup_expr='gte')

    drive_unit = django_filters.CharFilter(field_name='drive_unit', lookup_expr='iexact')

    body = django_filters.CharFilter(field_name='body', lookup_expr='iexact')
    transmission = django_filters.CharFilter(field_name='transmission', lookup_expr='iexact')

    class Meta:
        model = models.TransportAd
        fields = ['mark',
                  'model',
                  'year_lte', 'year_gte',
                  'price_lte', 'price_gte',
                  'engine',
                  'engine_cap_lte', 'engine_cap_gte',
                  'body',
                  'transmission'
                  ]
