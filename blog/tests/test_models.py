import pytest

from .factories import PostFactory, AuthorFactory

@pytest.mark.django_db
def test_post_must_have_author():
    with pytest.raises(ValueError):
        post = PostFactory()
        post.author = None
