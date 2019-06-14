from elasticsearch_dsl import analyzer


from django_elasticsearch_dsl import DocType, Index, fields

from  .models import Poll



# Name of the Elasticsearch index
POLL_INDEX = Index('poll')

# See Elasticsearch Indices API reference for available settings
POLL_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@POLL_INDEX.doc_type
class PollDocument(DocType):
    """Poll Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    question = fields.StringField(
        fields={
            'raw': fields.StringField(
                analyzer='keyword'
            )
        }
    )
    created_by= fields.StringField(
        fields={
            'raw': fields.StringField(
                analyzer='keyword'
            )
        }
    )
    pub_date = fields.DateField()
    
    

    class Meta(object):
        """Meta options."""

        model = Poll  