from unittest.mock import AsyncMock, Mock

from pytest_mock import MockerFixture

from brasilapi.services.feriado import FeriadoNacionalService
from brasilapi.dto.feriado import FeriadoNacional
from brasilapi.services.base import GetList

_module_path = FeriadoNacionalService.__module__


def test__feriado_service_should_return_get_list_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_list_instance_mock = Mock(spec=GetList)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetList", return_value=get_list_instance_mock)
    assert FeriadoNacionalService(http_client_mock).get_all(2023) is get_list_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/feriados/v1/2023",
        "deserializer_class": FeriadoNacional,
        "http_client": http_client_mock,
    }
