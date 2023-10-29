from unittest.mock import AsyncMock, Mock

from pytest_mock import MockerFixture

from brasilapi.services.ddd import DDDService
from brasilapi.dto.ddd import DDD
from brasilapi.services.base import GetOne

_module_path = DDDService.__module__


def test__bank_service_should_return_get_one_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_one_instance_mock = Mock(spec=GetOne)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetOne", return_value=get_one_instance_mock)
    assert DDDService(http_client_mock).get("83") is get_one_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/ddd/v1/83",
        "deserializer_class": DDD,
        "http_client": http_client_mock,
    }
