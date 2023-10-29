from unittest.mock import AsyncMock, Mock

import pytest
from pydantic import BaseModel

from brasilapi.http import AsyncHttpClient
from brasilapi.services.base import GetOne, GetList
from brasilapi.exception.validation_exception import ValidationException


class ResponseModel(BaseModel):
    value: str


class NewResponseModel(BaseModel):
    text: str


async def test__get_one_await_should_succeed():
    http_client_mock = Mock(spec=AsyncHttpClient, get=AsyncMock(return_value={"value": "test"}))
    assert await GetOne(path="/path", deserializer_class=ResponseModel, http_client=http_client_mock) == ResponseModel(
        value="test"
    )
    assert http_client_mock.get.call_args[0][0] == "/path"


async def test__get_one_should_await_should_raise_validation_error():
    http_client_mock = Mock(spec=AsyncHttpClient, get=AsyncMock(return_value={}))
    with pytest.raises(ValidationException):
        await GetOne(path="/path", deserializer_class=ResponseModel, http_client=http_client_mock)


async def test__get_one_with_deserializer_class_should_succeed():
    http_client_mock = Mock(spec=AsyncHttpClient, get=AsyncMock(return_value={"text": "test"}))
    get_one = GetOne(path="/path", deserializer_class=ResponseModel, http_client=http_client_mock)
    assert await get_one.with_deserializer_class(NewResponseModel) == NewResponseModel(text="test")


async def test__get_list_await_should_succeed():
    http_client_mock = Mock(spec=AsyncHttpClient, get=AsyncMock(return_value=[{"value": "test"}]))
    assert await GetList(path="/path", deserializer_class=ResponseModel, http_client=http_client_mock) == [
        ResponseModel(value="test")
    ]
    assert http_client_mock.get.call_args[0][0] == "/path"


async def test__get_list_with_deserializer_class_should_succeed():
    http_client_mock = Mock(spec=AsyncHttpClient, get=AsyncMock(return_value=[{"text": "test"}]))
    get_list = GetList(path="/path", deserializer_class=ResponseModel, http_client=http_client_mock)
    assert await get_list.with_deserializer_class(NewResponseModel) == [NewResponseModel(text="test")]


async def test__get_list_await_should_raise_validation_error():
    http_client_mock = Mock(spec=AsyncHttpClient, get=AsyncMock(return_value=[{"invalid": "response"}]))
    with pytest.raises(ValidationException):
        await GetList(path="/path", deserializer_class=ResponseModel, http_client=http_client_mock)
