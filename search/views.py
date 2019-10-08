from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
    SUGGESTER_COMPLETION
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    CompoundSearchFilterBackend,
    SuggesterFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .document import PollDocument
from .serializers import PollBookSerializer



class PollDocumentView(BaseDocumentViewSet):
    """The BookDocument view."""

    document = PollDocument
    serializer_class = PollBookSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
        SuggesterFilterBackend
    ]
    # Suggester fields
    suggester_fields = {
        'question_suggest': {
            'field': 'question.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
            'options': {
                'size': 20,  # Override default number of suggestions
            },
        },
    }
    # Define search fields
    search_fields = (
        'question',
        'slug',
        'pub_date',
    )
    # Define filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            # Note, that we limit the lookups of id field in this example,
            # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ]},
        'question': 'question.raw',
        #'created_by': 'created_by.raw',
        'pub_date': 'pub_date',
        'expire_date': 'expire_date',
        'slug': 'slug.raw',
        
    }
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'question': 'question.raw',
        #'created_by': 'created_by.raw',
        'pub_date': 'pub_date',
    }
    # Specify default ordering
    ordering = ('id', 'pub_date', )