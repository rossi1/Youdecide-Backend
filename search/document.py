
from django.conf import settings
from django_elasticsearch_dsl import  DocType, Index, fields

from polls.models import Poll




# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


INDEX.doc_type
class PollDocument(DocType):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    question = fields.StringField(
        fields={
            'raw': fields.StringField(analyzer='keyword'),
            'suggest': fields.CompletionField(multi=True)
        }
    )
    
    pub_date = fields.DateField()

   

    class Meta(object):
        """Meta options."""

        model = Poll  # The model associate with this Document