from rest_framework import serializers
from todos import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields= (
            "id",
            "title",
            "description",
            "created_at"
        )
        read_only_fields =("created_at", )
        model = models.Todo
