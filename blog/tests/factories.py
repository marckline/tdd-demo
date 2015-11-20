import factory

from ..models import Post, Author

class AuthorFactory(factory.DjangoModelFactory):
    name = "Some Guy"
    position = "Head Honcho"

    class Meta:
        model = Author


class PostFactory(factory.DjangoModelFactory):
    title = "Marketers won't believe these lead generation techniques for marketing marketing to marketers"
    author = factory.SubFactory(AuthorFactory)

    class Meta:
        model = Post


