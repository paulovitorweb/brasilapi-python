from typing import Literal, Optional

from brasilapi.http import AsyncHttpClient
from brasilapi.dto.fipe import FipePreco, FipeTabela, FipeMarca
from brasilapi.services.base import BaseService, GetList


class FipeMarcaService(BaseService):
    base_path: str = "/fipe/marcas/v1"

    def get_all(self, vehicle_type: Optional[Literal["caminhoes", "carros", "motos"]] = None) -> GetList[FipeMarca]:
        path = {self.base_path}
        if vehicle_type:
            path = f"{self.base_path}/{vehicle_type}"
        return GetList(path=path, deserializer_class=FipeMarca, http_client=self._http_client)


class FipePrecoService(BaseService):
    base_path: str = "/fipe/preco/v1"

    def get_all(self, fipe_code: str) -> GetList[FipePreco]:
        path = f"{self.base_path}/{fipe_code}"
        return GetList(path=path, deserializer_class=FipePreco, http_client=self._http_client)


class FipeTabelaService(BaseService):
    base_path: str = "/fipe/tabelas/v1"

    def get_all(self) -> GetList[FipeTabela]:
        path = self.base_path
        return GetList(path=path, deserializer_class=FipeTabela, http_client=self._http_client)


class FipeWrapper:
    def __init__(self, http_client: AsyncHttpClient) -> None:
        self._http_client = http_client

    @property
    def marcas(self) -> FipeMarcaService:
        return FipeMarcaService(self._http_client)

    @property
    def preco(self) -> FipePrecoService:
        return FipePrecoService(self._http_client)

    @property
    def tabelas(self) -> FipeTabelaService:
        return FipeTabelaService(self._http_client)
