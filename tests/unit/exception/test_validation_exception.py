from pydantic import BaseModel

from brasilapi.exception.validation_exception import ValidationException


class TextModel(BaseModel):
    value: str


def test__validation_exception():
    try:
        TextModel.model_validate({})
    except Exception as err:
        exc = ValidationException(raw_response={"foo": "bar"}, resource="/path", errors=[err])
    assert "Error when deserializing response from BrasilAPI" in str(exc)
