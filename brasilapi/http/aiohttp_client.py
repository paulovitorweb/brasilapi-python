from typing import Any, Union

from aiohttp.client import ClientSession, ClientTimeout, ClientResponseError

from brasilapi.exception import RequestException


class AioHttpClient:
    def __init__(self) -> None:
        self.__session: ClientSession = ClientSession(
            base_url="https://brasilapi.com.br",
            timeout=ClientTimeout(total=1 * 60),
        )

    async def get(self, path: str) -> Union[dict[str, Any], list[Any]]:
        async with await self.__session.get(f"/api{path}") as response:
            try:
                response.raise_for_status()
            except ClientResponseError as err:
                raise RequestException(status=err.status, resource=path) from err
            json = await response.json()
            return json

    async def close(self) -> None:
        await self.__session.close()
