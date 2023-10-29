from types import TracebackType
from typing import Self, Optional

from brasilapi.http import AsyncHttpClient, DEFAULT_HTTP_CLIENT_CLASS
from brasilapi.services.bank import BankService
from brasilapi.services.cep import CEPService
from brasilapi.services.ddd import DDDService
from brasilapi.services.feriado import FeriadoNacionalService
from brasilapi.services.fipe import FipeWrapper


class BrasilAPI:
    def __init__(self) -> None:
        self.__http_client: AsyncHttpClient = DEFAULT_HTTP_CLIENT_CLASS()

    def __enter__(self) -> None:
        raise TypeError("Use async with instead")

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        pass  # pragma: no cover

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        exc_traceback: Optional[TracebackType] = None,
    ) -> None:
        await self.__http_client.close()

    @property
    def banks(self) -> BankService:
        return BankService(self.__http_client)

    @property
    def ceps(self) -> CEPService:
        return CEPService(self.__http_client)

    @property
    def ddd(self) -> DDDService:
        return DDDService(self.__http_client)

    @property
    def feriados(self) -> FeriadoNacionalService:
        return FeriadoNacionalService(self.__http_client)

    @property
    def fipe(self) -> FipeWrapper:
        return FipeWrapper(self.__http_client)
