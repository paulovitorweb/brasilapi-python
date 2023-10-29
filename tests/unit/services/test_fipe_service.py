from unittest.mock import AsyncMock, Mock

from pytest_mock import MockerFixture

from brasilapi.services.fipe import FipeWrapper, FipeMarcaService, FipePrecoService, FipeTabelaService
from brasilapi.dto.fipe import FipeMarca, FipePreco, FipeTabela
from brasilapi.services.base import GetList

_module_path = FipeWrapper.__module__


def test__fipe_wrapper_service_should_return_services():
    wrapper = FipeWrapper(AsyncMock())
    assert (type(wrapper.marcas), type(wrapper.preco), type(wrapper.tabelas)) == (
        FipeMarcaService,
        FipePrecoService,
        FipeTabelaService,
    )


def test__fipe_marca_service_should_return_get_list_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_list_instance_mock = Mock(spec=GetList)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetList", return_value=get_list_instance_mock)
    assert FipeMarcaService(http_client_mock).get_all("motos") is get_list_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/fipe/marcas/v1/motos",
        "deserializer_class": FipeMarca,
        "http_client": http_client_mock,
    }


def test__fipe_preco_service_should_return_get_list_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_list_instance_mock = Mock(spec=GetList)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetList", return_value=get_list_instance_mock)
    assert FipePrecoService(http_client_mock).get_all("001004-9") is get_list_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/fipe/preco/v1/001004-9",
        "deserializer_class": FipePreco,
        "http_client": http_client_mock,
    }


def test__fipe_tabela_service_should_return_get_list_object(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    get_list_instance_mock = Mock(spec=GetList)
    get_one_class_mock = mocker.patch(f"{_module_path}.GetList", return_value=get_list_instance_mock)
    assert FipeTabelaService(http_client_mock).get_all() is get_list_instance_mock
    assert {
        "path": get_one_class_mock.call_args[1]["path"],
        "deserializer_class": get_one_class_mock.call_args[1]["deserializer_class"],
        "http_client": get_one_class_mock.call_args[1]["http_client"],
    } == {
        "path": "/fipe/tabelas/v1",
        "deserializer_class": FipeTabela,
        "http_client": http_client_mock,
    }
