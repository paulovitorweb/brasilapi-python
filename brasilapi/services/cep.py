from typing import Literal, overload, Union

from brasilapi.dto.cep import CEP, CEPv1
from brasilapi.services.base import BaseService, GetOne


class CEPService(BaseService):
    base_path: str = "/cep"

    @overload
    def get(self, cep: str, api_version: Literal["v1"]) -> GetOne[CEPv1]:  # pragma: no cover
        ...

    @overload
    def get(self, cep: str, api_version: Literal["v2"]) -> GetOne[CEP]:  # pragma: no cover
        ...

    @overload
    def get(self, cep: str, api_version: Literal["v2"] = "v2") -> GetOne[CEP]:  # pragma: no cover
        ...

    def get(self, cep: str, api_version: Literal["v1", "v2"] = "v2") -> Union[GetOne[CEP], GetOne[CEPv1]]:
        path = f"{self.base_path}/{api_version}/{cep}"
        match api_version:
            case "v1":
                return GetOne(path=path, deserializer_class=CEPv1, http_client=self._http_client)
            case "v2":
                return GetOne(path=path, deserializer_class=CEP, http_client=self._http_client)
            case _:
                raise ValueError("api_version must be v1 or v2")
