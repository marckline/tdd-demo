import pytest

from .factories import PostFactory, AuthorFactory


def test_post_must_have_author():
    post = PostFactory()
    post.author = None
    post.save()

    assert 0

