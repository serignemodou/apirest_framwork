from rest_framework import serializers
from postings.models import BlogUser

class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = [
            'pk',
            'userid',
            'usernames',
            'password',
            'title',
            'content',
            'timestamp',
        ]

        read_only_fields=['userid']
# ce fichier nous permet de convertir en json et de mettre des conditions de validations        
#convertir en JSON
# Validation des données
    
    def validate_title(self, value):
        qs = BlogUser.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("title already exist please choice another one")
        return value  
     