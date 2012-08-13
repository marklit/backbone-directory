import datetime
from haystack import indexes
from .models import Person


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    
    def get_model(self):
        return Person
    
    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(hide_person=False,
            created_time__lte=datetime.datetime.now())
