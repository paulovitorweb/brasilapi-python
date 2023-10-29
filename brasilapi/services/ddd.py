from brasilapi.dto.ddd import DDD
from brasilapi.services.base import BaseService, GetOne


class DDDService(BaseService):
    base_path: str = "/ddd/v1"

    def get(self, ddd: str) -> GetOne[DDD]:
        path = f"{self.base_path}/{ddd}"
        return GetOne(path=path, deserializer_class=DDD, http_client=self._http_client)
