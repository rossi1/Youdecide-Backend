from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from survey.models import Category, SurveyQuestion, SurveyCategories
from survey.serializers import CategorySerializer, SurveyCategoriesSerializer, SurveyQuestionSerializer


class CategoryAPIListView(APIView):
    """
    List all the  Category instances, or create a new Appointment instance.
    """
    #queryset =

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryAPIDetailView(RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a given Category instance.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SurveyQuestionAPIListView(APIView):
    """
    List all the  SurveyQuestion instances, or create a new SurveyQuestion instance.
    """
    #queryset =

    def get(self, request, format=None):
        survey_question = SurveyQuestion.objects.all()
        serializer = SurveyCategoriesSerializer(survey_question, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SurveyCategoriesSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyQuestionAPIDetailView(RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a given SurveyQuestion instance.
    """
    serializer_class = SurveyCategoriesSerializer
    queryset = SurveyQuestion.objects.all()

    def get_object(self, pk):
        try:
            return SurveyQuestion.objects.get(pk=pk)
        except SurveyQuestion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey_question = self.get_object(pk)
        serializer = SurveyCategoriesSerializer(survey_question)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        survey_question = self.get_object(pk)
        serializer = SurveyCategoriesSerializer(survey_question, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        survey_question = self.get_object(pk)
        survey_question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)