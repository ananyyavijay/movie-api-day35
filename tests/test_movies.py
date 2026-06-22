from tests.conftest import client


# def test_health():
#     response = client.get("/health")

#     assert response.status_code == 200


def test_create_movie():
    payload = {
        "title": "Inception",
        "year": 2010,
        "genre": ["Action", "Sci-Fi"],
        "rating": 4.8
    }

    response = client.post("/movies", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Inception"
    assert data["year"] == 2010


def test_get_movies():
    response = client.get("/movies")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_movie_by_id():
    payload = {
        "title": "Interstellar",
        "year": 2014,
        "genre": ["Sci-Fi"],
        "rating": 4.9
    }

    created = client.post("/movies", json=payload)

    movie_id = created.json()["id"]

    response = client.get(f"/movies/{movie_id}")

    assert response.status_code == 200
    assert response.json()["id"] == movie_id
    assert response.json()["title"] == "Interstellar"


def test_get_movie_not_found():
    response = client.get("/movies/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Movie not found"