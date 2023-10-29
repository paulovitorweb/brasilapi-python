from brasilapi.dto.bank import Bank
from brasilapi.services.base import BaseService, GetOne, GetList


class BankService(BaseService):
    base_path: str = "/banks/v1"

    def get(self, code: int) -> GetOne[Bank]:
        path = f"{self.base_path}/{code}"
        return GetOne(path=path, deserializer_class=Bank, http_client=self._http_client)

    def get_all(self) -> GetList[Bank]:
        path = self.base_path
        return GetList(path=path, deserializer_class=Bank, http_client=self._http_client)
