from rest_framework.serializers import ModelSerializer, SerializerMethodField

from blog.models import Post


class PostSerializer(ModelSerializer):
    created_at = SerializerMethodField()
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_created_at(self, obj):
        return obj.created_at.strftime('%B %d, %Y')