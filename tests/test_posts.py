import requests
import pytest
from api.api_client import APIClient
from test_data.posts import POST_IDS
from config import BASE_URL


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)

def test_get_posts(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200

    posts = response.json()
    assert len(posts) > 0

@pytest.mark.parametrize("post_id", POST_IDS)
def test_get_post_by_id(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 200

    post = response.json()
    assert post["id"] == post_id
    assert "title" in post
    assert "body" in post
    assert "userId" in post

def test_get_post_not_found(api_client):
    response = api_client.get("/posts/9999")
    assert response.status_code == 404

def test_create_post(api_client):
    payload = {
        "title": "API Test",
        "body": "Created using pytest",
        "userId": 1
    }

    response = api_client.post("/posts", payload)
    assert response.status_code == 201

    post = response.json()

    assert post["title"] == payload["title"]
    assert post["body"] == payload["body"]
    assert post["userId"] == payload["userId"]
    assert "id" in post

def test_update_post(api_client):
    payload = {
        "title": "Updated API Test",
        "body": "Updated using pytest",
        "userId": 1
    }

    response = api_client.put("/posts/1", payload)
    assert response.status_code == 200

    post = response.json()

    assert post["id"] == 1
    assert post["title"] == payload["title"]
    assert post["body"] == payload["body"]
    assert post["userId"] == payload["userId"]

def test_delete_post(api_client):
    response = api_client.delete("/posts/1")
    assert response.status_code == 200
