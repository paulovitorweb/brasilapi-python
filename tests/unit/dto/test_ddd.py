from brasilapi.dto.ddd import DDD


def test__ddd_dto_should_deserialize():
    assert DDD.model_validate(
        {
            "state": "SP",
            "cities": [
                "EMBU",
                "VÁRZEA PAULISTA",
                "VARGEM GRANDE PAULISTA",
                "VARGEM",
                "TUIUTI",
                "TABOÃO DA SERRA",
                "SUZANO",
                "SÃO ROQUE",
                "SÃO PAULO",
            ],
        }
    ) == DDD(
        state="SP",
        cities=[
            "EMBU",
            "VÁRZEA PAULISTA",
            "VARGEM GRANDE PAULISTA",
            "VARGEM",
            "TUIUTI",
            "TABOÃO DA SERRA",
            "SUZANO",
            "SÃO ROQUE",
            "SÃO PAULO",
        ],
    )
