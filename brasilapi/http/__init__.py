# pragma: no cover

from typing import Protocol, Union, Any

from .aiohttp_client import AioHttpClient


class AsyncHttpClient(Protocol):
    async def get(self, path: str) -> Union[dict[str, Any], list[Any]]:
        ...

    async def close(self) -> None:
        ...


DEFAULT_HTTP_CLIENT_CLASS: AsyncHttpClient = AioHttpClient
