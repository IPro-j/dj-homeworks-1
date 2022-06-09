import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from students.models import Student, Course
from model_bakery import baker


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_course_create(api_client, student_factory, course_factory):
    # Arrange
    url = reverse("courses-list")
    courses = course_factory(_quantity=1)

    # Act
    respond = api_client.get('/api/v1/courses/', {'name': courses[0].name})
    data = respond.json()

    # Assert
    assert respond.status_code == 200
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_course_list_create(api_client, student_factory, course_factory):
    # Arrange
    url = reverse("courses-list")
    courses = course_factory(_quantity=10)

    #Act
    respond = api_client.get('/api/v1/courses/')
    data = respond.json()
    print(data[0]['name'])

    # Assert
    assert respond.status_code == 200
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_course_id_filter(api_client, student_factory, course_factory):
    # Arrange
    url = reverse("courses-list")
    courses = course_factory(_quantity=10)

    # Act
    id_filter = 1
    respond = api_client.get('/api/v1/courses/', {'id': id_filter})
    data = respond.json()

    # Assert
    assert respond.status_code == 200
    assert data[0]['id'] == id_filter


@pytest.mark.django_db
def test_course_name_filter(api_client, student_factory, course_factory):
    # Arrange
    url = reverse("courses-list")
    courses = course_factory(_quantity=10)

    # Act
    name_filter = courses[7].name
    respond = api_client.get('/api/v1/courses/', {'name': name_filter})
    data = respond.json()

    # Assert
    assert respond.status_code == 200
    assert data[0]['name'] == name_filter


@pytest.mark.django_db
def test_course_post(api_client, student_factory, course_factory):
    # Arrange

    # Act
    respond = api_client.post('/api/v1/courses/', {"name": "Физика"})

    # Assert
    assert respond.status_code == 201


@pytest.mark.django_db
def test_course_patch(api_client, student_factory, course_factory):
    # Arrange
    courses = course_factory(_quantity=1)

    # Act
    respond = api_client.patch('/api/v1/courses/', {"id": courses[0].id, "name": "Физика"})

    # Assert
    assert respond.status_code == 200


@pytest.mark.django_db
def test_course_delete(api_client, student_factory, course_factory):
    # Arrange
    courses = course_factory(_quantity=1)

    # Act
    respond = api_client.delete('/api/v1/courses/', {'id': courses[0].id})

    # Assert
    assert respond.status_code == 200 or respond.status_code == 204
