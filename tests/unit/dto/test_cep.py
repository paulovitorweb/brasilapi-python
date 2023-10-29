from brasilapi.dto.cep import CEP, CEPv1, CEPLocation


def test__cep_v1_dto_should_deserialize():
    assert CEPv1.model_validate(
        {
            "cep": "89010025",
            "state": "SC",
            "city": "Blumenau",
            "neighborhood": "Centro",
            "street": "Rua Doutor Luiz de Freitas Melro",
            "service": "viacep",
        }
    ) == CEPv1(
        cep="89010025",
        state="SC",
        city="Blumenau",
        neighborhood="Centro",
        street="Rua Doutor Luiz de Freitas Melro",
        service="viacep",
    )


def test__cep_v2_dto_should_deserialize():
    assert CEP.model_validate(
        {
            "cep": "89010025",
            "state": "SC",
            "city": "Blumenau",
            "neighborhood": "Centro",
            "street": "Rua Doutor Luiz de Freitas Melro",
            "service": "viacep",
            "location": {"type": "Point", "coordinates": {"longitude": "-49.0629788", "latitude": "-26.9244749"}},
        }
    ) == CEP(
        cep="89010025",
        state="SC",
        city="Blumenau",
        neighborhood="Centro",
        street="Rua Doutor Luiz de Freitas Melro",
        service="viacep",
        location=CEPLocation(type="Point", coordinates={"longitude": "-49.0629788", "latitude": "-26.9244749"}),
    )


def test__cep_v2_dto_should_deserialize_without_coordinates():
    assert CEP.model_validate(
        {
            "cep": "89010025",
            "state": "SC",
            "city": "Blumenau",
            "neighborhood": "Centro",
            "street": "Rua Doutor Luiz de Freitas Melro",
            "service": "viacep",
            "location": {"type": "Point", "coordinates": {}},
        }
    ) == CEP(
        cep="89010025",
        state="SC",
        city="Blumenau",
        neighborhood="Centro",
        street="Rua Doutor Luiz de Freitas Melro",
        service="viacep",
        location=CEPLocation(type="Point", coordinates=None),
    )