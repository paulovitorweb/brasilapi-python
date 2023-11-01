<h1 align="center">brasilapi-python</h1>

<div align="center">
  <p>
    <strong>Um cliente Python assíncrono para o <a href="https://brasilapi.com.br/" target="_blank">Brasil  API</a></strong>
  </p>
  <p>
    <img src="https://github.com/paulovitorweb/brasilapi-python/actions/workflows/test.yml/badge.svg"></img> 
    <img src="./coverage.svg"></img>
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/brasilapi">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/brasilapi">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/brasilapi">
  </p>
</div>

## Motivação

Fornecer um cliente HTTP assíncrono de alto nível para acessar e desserializar recursos do BrasilAPI.

## Instalação

Com pip:

```
pip install brasilapi
```

Ou com Poetry:

```
poetry add brasilapi
```

## Uso

Este cliente fornece chamadas à API do BrasilAPI dentro de um gerenciador de contexto assíncrono para uma melhor performance.

Por exemplo, o seguinte programa:

```python
import asyncio
from brasilapi import BrasilAPI

async def run():
    async with BrasilAPI() as client:
        result = await client.ceps.get("89010025")
        print(repr(result))

if __name__ == "__main__":
    asyncio.run(run())
```

Fornece uma saída igual ou semelhante a:

```python
CEP(cep='89010025', state='SC', city='Blumenau', neighborhood='Centro', street='Rua Doutor Luiz de Freitas Melro', service='correios', location=CEPLocation(type='Point', coordinates={'longitude': '-49.0641133', 'latitude': '-26.9239862'}))
```

Chamadas dentro do gerenciador de contexto utilizam uma mesma sessão que só é fechada ao sair do bloco. Você pode optar por compartilhar o mesmo cliente e sessão durante o tratamento de uma solicitação no seu aplicativo (por exemplo, funciona muito bem retornar uma instância do BrasilAPI como uma dependência do FastAPI) ou enquanto fizer sentido para seu cenário.

## Modelos Pydantic

Os resultados das consultas são instâncias de modelos [Pydantic v2](https://github.com/pydantic/pydantic). Você pode aproveitar a consistência e todas as dicas de tipo.

Os modelos Pydantic foram construídos com base na [documentação oficial do BrasilAPI](https://brasilapi.com.br/docs) e os nomes dos serviços e atributos são iguais aos 
da documentação; portanto, alguns estão em inglês e outros em português. Excetuam-se mudanças de `camelCase` para `snake_case`. Mas você pode usar seu próprio modelo Pydantic:

```python
import asyncio
from pydantic import BaseModel, Field
from brasilapi import BrasilAPI

class CustomDDD(BaseModel):
    estado: str = Field(alias="state")
    cidades: list[str] = Field(alias="cities")

async def run():
    async with BrasilAPI() as client:
        ddd = await client.ddd.get("83").with_deserializer_class(CustomDDD)
        print(repr(ddd))

if __name__ == "__main__":
    asyncio.run(run())
```
