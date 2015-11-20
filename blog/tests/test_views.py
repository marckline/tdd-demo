import pytest, factory

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase

from .factories import PostFactory

class PostViewTests(APITestCase):

    def test_post_list(self):
        for i in range(0,1):
            post = PostFactory()
            post.save()

        url = reverse('post-list')
        response = self.client.get(url)

        assert len(response.data) == 2




