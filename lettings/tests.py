import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_status_code_200(client):
    path = reverse('lettings:index')
    res = client.get(path)
    assert res.status_code == 200


@pytest.mark.django_db
def test_title_is_displayed_in_index(client):
    path = reverse('lettings:index')
    res = client.get(path)
    res_content = res.content
    assert str(res_content).find('<title>Lettings</title>') > 0


@pytest.mark.django_db
def test_title_is_displayed_for_lettings_letting_view(client):
    test_address = Address.objects.create(number=7217, street="Bedford Street",
                                           city="Brunswick", state='GA', zip_code=31525,
                                           country_iso_code='USA')
    test_letting = Letting.objects.create(title='Joshua Tree Green Haus /w Hot Tub',
                                       address=test_address)
    path = reverse('lettings:letting', kwargs={'letting_id': test_letting.id})
    res = client.get(path)
    res_content = res.content
    assert str(res_content).find(test_letting.title) > 0
