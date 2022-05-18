from unittest.mock import Mock
import tmdb_client

movie_id = 583

def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("tests.test_tmdb_client.some_function_to_mock", my_mock)
   assert some_function_to_mock() == 2

def test_get_poster_url_uses_default_size():
   _path = "some-poster-path"
   expected_default_size = 'w342'
   poster_url = tmdb_client.get_poster_url(_path=_path)
   assert expected_default_size in poster_url

def test_get_single_movie():
   movie= tmdb_client.get_single_movie(movie_id=movie_id)
   assert movie

def test_get_single_movie_cast():
    cast=tmdb_client.get_single_movie_cast(movie_id)
    assert len(cast)>1

def test_random_get_backdrop(monkeypatch):
   back_mock=Mock()
   back_mock.return_value= {'aspect_ratio': 1.778, 'height': 1040, 'iso_639_1': None, 'file_path': '/rL3VEvszvN2hVUjNU2bxa49rbQ4.jpg', 'vote_average': 5.312, 'vote_count': 1, 'width': 1849}
   monkeypatch.setattr("tmdb_client.random_get_backdrop", back_mock)
   assert "file_path" in tmdb_client.random_get_backdrop(movie_id)