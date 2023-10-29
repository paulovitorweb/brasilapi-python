from unittest.mock import AsyncMock

import pytest
from pytest_mock import MockerFixture

from brasilapi import BrasilAPI
from brasilapi.services.bank import BankService
from brasilapi.services.cep import CEPService
from brasilapi.services.ddd import DDDService
from brasilapi.services.feriado import FeriadoNacionalService
from brasilapi.services.fipe import FipeWrapper

_module_path = BrasilAPI.__module__


async def test__client_should_instantiation_should_instantiate_http_client(mocker: MockerFixture):
    http_client_mock = mocker.patch(f"{_module_path}.DEFAULT_HTTP_CLIENT_CLASS")
    _ = BrasilAPI()
    http_client_mock.call_count == 1


async def test__client_async_context_manager_should_succeed(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    mocker.patch(f"{_module_path}.DEFAULT_HTTP_CLIENT_CLASS", return_value=http_client_mock)
    async with BrasilAPI():
        assert http_client_mock.close.call_count == 0
    assert http_client_mock.close.call_count == 1


async def test__client_should_raise_error_when_using_sync_context_manager():
    with pytest.raises(TypeError, match="Use async with instead"):
        with BrasilAPI():
            pass


async def test__client_should_provide_bank_service(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    mocker.patch(f"{_module_path}.DEFAULT_HTTP_CLIENT_CLASS", return_value=http_client_mock)
    async with BrasilAPI() as client:
        assert isinstance(client.banks, BankService)


async def test__client_should_provide_cep_service(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    mocker.patch(f"{_module_path}.DEFAULT_HTTP_CLIENT_CLASS", return_value=http_client_mock)
    async with BrasilAPI() as client:
        assert isinstance(client.ceps, CEPService)


async def test__client_should_provide_ddd_service(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    mocker.patch(f"{_module_path}.DEFAULT_HTTP_CLIENT_CLASS", return_value=http_client_mock)
    async with BrasilAPI() as client:
        assert isinstance(client.ddd, DDDService)


async def test__client_should_provide_feriado_service(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    mocker.patch(f"{_module_path}.DEFAULT_HTTP_CLIENT_CLASS", return_value=http_client_mock)
    async with BrasilAPI() as client:
        assert isinstance(client.feriados, FeriadoNacionalService)


async def test__client_should_provide_fipe_wrapper_service(mocker: MockerFixture):
    http_client_mock = AsyncMock()
    mocker.patch(f"{_module_path}.DEFAULT_HTTP_CLIENT_CLASS", return_value=http_client_mock)
    async with BrasilAPI() as client:
        assert isinstance(client.fipe, FipeWrapper)
