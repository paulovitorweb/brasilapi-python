from unittest.mock import AsyncMock, Mock

import pytest
from pytest_mock import MockerFixture

from brasilapi.services.cep import CEPService
from brasilapi.dto.cep import CEP, CEPv1
from brasilapi.services.base import GetOne

_module_path = CEPService.__module__


def test__cep_service_v1_should_return_get_one_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_one_instance_mock = Mock(spec=GetOne)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetOne", return_value=get_one_instance_mock)
    assert CEPService(http_client_mock).get("89010025", api_version="v1") is get_one_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/cep/v1/89010025",
        "deserializer_class": CEPv1,
        "http_client": http_client_mock,
    }


def test__cep_service_v2_should_return_get_one_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_one_instance_mock = Mock(spec=GetOne)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetOne", return_value=get_one_instance_mock)
    assert CEPService(http_client_mock).get("89010025", api_version="v2") is get_one_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/cep/v2/89010025",
        "deserializer_class": CEP,
        "http_client": http_client_mock,
    }


def test__cep_service_default_should_return_get_one_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_one_instance_mock = Mock(spec=GetOne)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetOne", return_value=get_one_instance_mock)
    assert CEPService(http_client_mock).get("89010025") is get_one_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/cep/v2/89010025",
        "deserializer_class": CEP,
        "http_client": http_client_mock,
    }


def test__cep_service_should_raise_error_when_an_invalid_api_version_is_provided(mocker: MockerFixture):
    mocker.patch(f"{_module_path}.GetOne")
    with pytest.raises(ValueError, match="api_version must be v1 or v2"):
        CEPService(AsyncMock()).get("89010025", api_version="v3")
