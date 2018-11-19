from rest_framework.serializers import ModelSerializer
from survey.models import Category, SurveyQuestion, SurveyCategories


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('category_id',  'title', 'description', 'created_date')


class SurveyQuestionSerializer(ModelSerializer):

    class Meta:
        model = SurveyQuestion
        fields = ('survey_question_id', 'question', 'opening_time', 'closing_time', 'created_by', 'created_date')


class SurveyCategoriesSerializer(ModelSerializer):

    class Meta:
        model = SurveyCategories
        fields = ('survey_categories_id', 'survey_id', 'category_id')
