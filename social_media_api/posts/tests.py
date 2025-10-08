from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment
from rest_framework.authtoken.models import Token

User = get_user_model()

class PostCommentAPITests(APITestCase):
    def setUp(self):
        # users
        self.user1 = User.objects.create_user(username='u1', password='pass')
        self.user2 = User.objects.create_user(username='u2', password='pass')
        # tokens
        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)

        # a post by user1
        self.post = Post.objects.create(author=self.user1, title='Hello', content='World')

    def test_create_post_requires_auth(self):
        url = reverse('post-list')  # router name: post-list
        data = {'title': 'New', 'content': 'Body'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_authenticated(self):
        url = reverse('post-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        data = {'title': 'New', 'content': 'Body'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.filter(author=self.user1).count(), 2)

    def test_comment_lifecycle(self):
        # create comment as user2
        url = reverse('comment-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token2.key)
        data = {'post': self.post.pk, 'content': 'Nice post'}
        r = self.client.post(url, data)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        comment_id = r.data['id']

        # user1 cannot edit user2's comment
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        edit_url = reverse('comment-detail', args=[comment_id])
        r2 = self.client.put(edit_url, {'post': self.post.pk, 'content': 'Hacked'})
        self.assertIn(r2.status_code, (status.HTTP_403_FORBIDDEN, status.HTTP_405_METHOD_NOT_ALLOWED))

        # user2 can delete
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token2.key)
        r3 = self.client.delete(edit_url)
        self.assertEqual(r3.status_code, status.HTTP_204_NO_CONTENT)
