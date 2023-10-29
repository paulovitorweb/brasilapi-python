from brasilapi.exception.request_exception import RequestException


def test__request_exception():
    exc = RequestException(status=500, resource="/path")
    assert str(exc) == "Error in request to BrasilAPI, resource=/path, status=500"
