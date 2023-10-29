from unittest.mock import AsyncMock, Mock

from pytest_mock import MockerFixture

from brasilapi.services.bank import BankService
from brasilapi.dto.bank import Bank
from brasilapi.services.base import GetOne, GetList

_module_path = BankService.__module__


def test__bank_service_should_return_get_one_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_one_instance_mock = Mock(spec=GetOne)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetOne", return_value=get_one_instance_mock)
    assert BankService(http_client_mock).get(1) is get_one_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/banks/v1/1",
        "deserializer_class": Bank,
        "http_client": http_client_mock,
    }


def test__bank_service_should_return_get_list_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_list_instance_mock = Mock(spec=GetList)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetList", return_value=get_list_instance_mock)
    assert BankService(http_client_mock).get_all() is get_list_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/banks/v1",
        "deserializer_class": Bank,
        "http_client": http_client_mock,
    }
