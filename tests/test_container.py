

class TestMovie:
    def test_not_find_movie(self,client):
        response = client.get('/api/movie/1')
        print(response.json)
        assert response.status_code == 404
        assert response.json == dict({"error":"Movie {movie_id} not found"})
