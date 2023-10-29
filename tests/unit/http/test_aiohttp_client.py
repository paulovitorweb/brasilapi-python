from unittest.mock import Mock, AsyncMock

import pytest
from pytest_mock import MockerFixture
from aiohttp.client import ClientTimeout, ClientSession, ClientResponseError

from brasilapi.http import AioHttpClient
from brasilapi.exception import RequestException

_module_path = AioHttpClient.__module__


def test__client_instantiation_should_instantiate_aiohttp_client_session(mocker: MockerFixture):
    aiohttp_client_session_mock = mocker.patch(f"{_module_path}.ClientSession")
    _ = AioHttpClient()
    assert aiohttp_client_session_mock.call_args[1] == dict(
        base_url="https://brasilapi.com.br",
        timeout=ClientTimeout(60),
    )


async def test__client_close_should_close_client_session(mocker: MockerFixture):
    aiohttp_client_session_mock = Mock(spec=ClientSession)
    mocker.patch(f"{_module_path}.ClientSession", return_value=aiohttp_client_session_mock)
    client = AioHttpClient()
    await client.close()
    assert aiohttp_client_session_mock.close.call_count == 1


async def test__client_get_should_succeed(mocker: MockerFixture):
    aiohttp_client_session_mock = Mock(spec=ClientSession)
    aiohttp_get_mock = AsyncMock()
    aiohttp_response_mock = AsyncMock(raise_for_status=Mock(), json=AsyncMock(return_value={"foo": "bar"}))
    aiohttp_get_mock.return_value.__aenter__.return_value = aiohttp_response_mock
    aiohttp_client_session_mock.get = aiohttp_get_mock
    mocker.patch(f"{_module_path}.ClientSession", return_value=aiohttp_client_session_mock)
    client = AioHttpClient()
    response = await client.get("/banks")
    assert aiohttp_client_session_mock.get.call_args[0][0] == "/api/banks"
    assert aiohttp_response_mock.raise_for_status.call_count == 1
    assert response == {"foo": "bar"}


async def test__client_get_should_raise_error(mocker: MockerFixture):
    aiohttp_client_session_mock = Mock(spec=ClientSession)
    aiohttp_get_mock = AsyncMock()
    aiohttp_response_mock = AsyncMock(
        raise_for_status=Mock(side_effect=ClientResponseError(Mock(real_url="test"), None))
    )
    aiohttp_get_mock.return_value.__aenter__.return_value = aiohttp_response_mock
    aiohttp_client_session_mock.get = aiohttp_get_mock
    mocker.patch(f"{_module_path}.ClientSession", return_value=aiohttp_client_session_mock)
    client = AioHttpClient()
    with pytest.raises(RequestException):
        await client.get("/banks")
