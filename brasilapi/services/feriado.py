from brasilapi.dto.feriado import FeriadoNacional
from brasilapi.services.base import BaseService, GetList


class FeriadoNacionalService(BaseService):
    base_path: str = "/feriados/v1"

    def get_all(self, year: int) -> GetList[FeriadoNacional]:
        path = f"{self.base_path}/{year}"
        return GetList(path=path, deserializer_class=FeriadoNacional, http_client=self._http_client)