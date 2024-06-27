from blog.utils import CreateListRetrieveViewSet
from blog.models import Post
from blog.serializers import PostSerializer

class PostViewSet(CreateListRetrieveViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
