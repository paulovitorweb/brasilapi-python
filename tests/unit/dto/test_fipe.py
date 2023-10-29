from brasilapi.dto.fipe import FipeMarca, FipePreco, FipeTabela


def test__fipe_marca_dto_should_deserialize():
    assert FipeMarca.model_validate({"nome": "AGRALE", "valor": "102"}) == FipeMarca(nome="AGRALE", valor=102)


def test__fipe_preco_dto_should_deserialize():
    assert FipePreco.model_validate(
        {
            "valor": "R$ 6.022,00",
            "marca": "Fiat",
            "modelo": "Palio EX 1.0 mpi 2p",
            "anoModelo": 1998,
            "combustivel": "Álcool",
            "codigoFipe": "001004-9",
            "mesReferencia": "junho de 2021",
            "tipoVeiculo": 1,
            "siglaCombustivel": "Á",
            "dataConsulta": "segunda-feira, 7 de junho de 2021 23:05",
        }
    ) == FipePreco(
        valor="R$ 6.022,00",
        marca="Fiat",
        modelo="Palio EX 1.0 mpi 2p",
        ano_modelo=1998,
        combustivel="Álcool",
        codigo_fipe="001004-9",
        mes_referencia="junho de 2021",
        tipo_veiculo=1,
        sigla_combustivel="Á",
        data_consulta="segunda-feira, 7 de junho de 2021 23:05",
    )


def test__fipe_tabela_dto_should_deserialize():
    assert FipeTabela.model_validate({"codigo": 271, "mes": "junho/2021"}) == FipeTabela(codigo=271, mes="junho/2021")
