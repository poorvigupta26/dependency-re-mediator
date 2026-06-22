from network import fetch_url


def test_fetch_url():
    assert isinstance(
        fetch_url("https://example.com"),
        int
    )