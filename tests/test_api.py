def test_full_flow(client):
    # 1. Register
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

    # 2. Login
    response = client.post(
        "/auth/token",
        data={"username": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    token = token_data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Create Post
    response = client.post(
        "/blog/",
        json={"title": "My Post", "content": "Hello"},
        headers=headers,
    )
    assert response.status_code == 200
    post_data = response.json()
    assert post_data["title"] == "My Post"
    post_id = post_data["id"]

    # 4. Create Comment
    response = client.post(
        f"/blog/{post_id}/comments",
        json={"content": "Nice post"},
        headers=headers,
    )
    assert response.status_code == 200
    comment_data = response.json()
    assert comment_data["content"] == "Nice post"
    assert comment_data["post_id"] == post_id

    # 5. List Posts
    response = client.get("/blog/")
    assert response.status_code == 200
    assert len(response.json()) > 0
