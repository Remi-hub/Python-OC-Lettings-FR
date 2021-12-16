from django.test import TestCase
from django.urls import reverse, resolve
import pytest
# import views


# # Create your tests here.
# class TestUrls:
#
#     def test_detail_url(self):
#         path = reverse('profile', kwargs={'username': '4meRomance'})
#         assert resolve(path).view_name == 'profile'



# class TestClient:
#     @pytest.fixture()
#     def test_client(self):
#         views.testing = True
#         with views as client:
#             return client
#
#
# class TestIndex(TestClient):
#
#     def test_status_code_200(self, test_client):
#         res = test_client.get()
