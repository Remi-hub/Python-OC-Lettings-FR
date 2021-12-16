import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_status_code_200(client):
    path = reverse('lettings:index')
    res = client.get(path)
    assert res.status_code == 200

@pytest.mark.django_db
def test_title_is_displayed(client):
    path = reverse('lettings:index')
    res = client.get(path)
    res_content = res.content
    assert str(res_content).find('<title>Lettings</title>') > 0
