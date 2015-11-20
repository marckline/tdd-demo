import pytest

from .factories import PostFactory, AuthorFactory

@pytest.mark.django_db
def test_post_must_have_author():
    post = PostFactory()
    post.author = None
    post.save()

    assert 0

