from django.conf import settings

from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from polls.models import Poll

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


from django_elasticsearch_dsl.registries import registry


@INDEX.doc_type
class PollDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    question = fields.StringField(
        
        fields={
            'raw': fields.StringField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )

    slug = fields.StringField(
        
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

   
    """
    created_by = fields.StringField(
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )
    """

    pub_date = fields.DateField()

    expire_date = fields.DateField()



    class Django(object):
        """Meta options."""

        model = Poll # The model associate with this Document