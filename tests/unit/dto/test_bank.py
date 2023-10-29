from brasilapi.dto.bank import Bank


def test__bank_dto_should_deserialize():
    assert Bank.model_validate(
        {"ispb": "00000000", "name": "BCO DO BRASIL S.A.", "code": 1, "fullName": "Banco do Brasil S.A."}
    ) == Bank(ispb="00000000", name="BCO DO BRASIL S.A.", code=1, fullName="Banco do Brasil S.A.")
