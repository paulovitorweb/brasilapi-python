import datetime

from brasilapi.dto.feriado import FeriadoNacional


def test__feriado_dto_should_deserialize():
    assert FeriadoNacional.model_validate(
        {"date": "2021-01-01", "name": "Confraternização mundial", "type": "national"}
    ) == FeriadoNacional(date=datetime.date(2021, 1, 1), name="Confraternização mundial", type="national")
