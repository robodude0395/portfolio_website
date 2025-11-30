import pytest
from unittest.mock import patch
from app import app   # import your Flask app object


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_visit_page_returns_index_html(client):
    # Patch render_template inside your app module
    with patch("app.render_template") as mock_render:
        mock_render.return_value = "<html>fake index</html>"

        response = client.get("/")

        # Assertions
        mock_render.assert_called_once_with("index.html")
        assert response.status_code == 200
        assert b"fake index" in response.data
