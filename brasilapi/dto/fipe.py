from pydantic import BaseModel, Field, AliasChoices


class FipeMarca(BaseModel):
    nome: str
    valor: int


class FipePreco(BaseModel):
    valor: str
    marca: str
    modelo: str
    ano_modelo: int = Field(alias=AliasChoices("anoModelo", "ano_modelo"))
    combustivel: str
    codigo_fipe: str = Field(alias=AliasChoices("codigoFipe", "codigo_fipe"))
    mes_referencia: str = Field(alias=AliasChoices("mesReferencia", "mes_referencia"))
    tipo_veiculo: int = Field(alias=AliasChoices("tipoVeiculo", "tipo_veiculo"))
    sigla_combustivel: str = Field(alias=AliasChoices("siglaCombustivel", "sigla_combustivel"))
    data_consulta: str = Field(alias=AliasChoices("dataConsulta", "data_consulta"))


class FipeTabela(BaseModel):
    codigo: int
    mes: str
