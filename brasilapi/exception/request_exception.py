class RequestException(Exception):
    """Request error"""

    def __init__(self, status: int, resource: str) -> None:
        self.status = status
        self.resource = resource

    def __str__(self) -> str:
        return f"Error in request to BrasilAPI, resource={self.resource}, status={self.status}"
