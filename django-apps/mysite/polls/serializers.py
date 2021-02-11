from rest_framework  import serializers
#this framework allows me  the developer to use a single classs for related views
from polls.models import Question 

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        fields =(
            'id',
            'question_text',
            'pub_date',
        )
        model =Question
