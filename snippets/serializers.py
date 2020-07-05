from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


# class SnippetSerializer(serializers.Serializer)
    # id = serializers.IntegerField(read_only = True)
    # title = serializers.CharField(required = True, allow_blank = True, max_length = 100)
    # code = serializers.CharField(style = {'base_template':'textarea.html'})
    # lineno = serializers.BooleanField(required  = False)
    # language = serializers.ChoiceField(choices = LANGUAGE_CHOICES, default = 'python')
    # style = serializers.ChoiceField(choices = STYLE_CHOICES, default = 'fiendly' )


    # def create(self, validate_data):
    #     #Create and return a new `Snippet` instance, given the validated data
    #     return Snippet.objects.create(**validate_data)

    # def update(self, instance, validate_data):
    #     #Update and return an existing `Snippet` instance, given the validated data.

    #     instance.title = validate_data.get('title', instance.title)
    #     instance.code = validate_data.get('code', instance.code)
    #     instance.lineno = validate_data.get('lineno', instance.lineno)
    #     instance.languages = validate_data.get('language', instance.language)
    #     instance.style = validate_data.get('style', instance.style)
    #     instance.save()

    #     return instance

class SnippetSerializer(serializers.ModelSerializer):
    # the above code can be replaced with the following
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

