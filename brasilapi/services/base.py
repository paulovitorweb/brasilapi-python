from typing import Generic, TypeVar, Generator, Any

from pydantic import BaseModel
from pydantic_core import ValidationError

from brasilapi.http import AsyncHttpClient
from brasilapi.exception.validation_exception import ValidationException


T = TypeVar("T", bound=BaseModel)


class BaseService:
    base_path: str

    def __init__(self, http_client: AsyncHttpClient) -> None:
        self._http_client = http_client


class GetList(Generic[T]):
    def __init__(self, path: str, deserializer_class: type[T], http_client: AsyncHttpClient) -> None:
        self.__path: str = path
        self.__deserializer_class: type[T] = deserializer_class
        self.__http_client: AsyncHttpClient = http_client

    def __await__(self) -> Generator[Any, None, list[T]]:
        return self.__get_all().__await__()

    def with_deserializer_class(self, deserializer_class: type[T]) -> "GetList[T]":
        return GetList(path=self.__path, deserializer_class=deserializer_class, http_client=self.__http_client)

    async def __get_all(self) -> list[T]:
        resource = self.__path
        response = await self.__http_client.get(resource)
        deserialized_response = []
        errors: list[ValidationError] = []
        for item in response:
            try:
                deserialized_response.append(self.__deserializer_class.model_validate(item))
            except ValidationError as err:
                errors.append(err)
        if errors:
            raise ValidationException(raw_response=response, resource=resource, errors=errors)
        return deserialized_response


class GetOne(Generic[T]):
    def __init__(self, path: str, deserializer_class: type[T], http_client: AsyncHttpClient) -> None:
        self.__path: str = path
        self.__deserializer_class: type[T] = deserializer_class
        self.__http_client: AsyncHttpClient = http_client

    def __await__(self) -> Generator[Any, None, T]:
        return self.__get().__await__()

    def with_deserializer_class(self, deserializer_class: type[T]) -> "GetOne[T]":
        return GetOne(path=self.__path, deserializer_class=deserializer_class, http_client=self.__http_client)

    async def __get(self) -> T:
        resource = self.__path
        response = await self.__http_client.get(resource)
        try:
            return self.__deserializer_class.model_validate(response)
        except ValidationError as err:
            raise ValidationException(raw_response=response, resource=resource, errors=[err]) from err
