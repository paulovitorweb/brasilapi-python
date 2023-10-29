from pydantic_core import ValidationError


class ValidationException(Exception):
    """Request error"""

    def __init__(self, raw_response: dict, resource: str, errors: list[ValidationError]) -> None:
        self.raw_response: dict = raw_response
        self.resource: str = resource
        self.errors: list[ValidationError] = errors

    def __str__(self) -> str:
        errors = ",".join([str(error) for error in self.errors])
        return f"Error when deserializing response from BrasilAPI[resource={self.resource} errors={errors}"
