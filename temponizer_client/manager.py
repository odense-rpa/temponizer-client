from .client import TemponizerClient
from .functionality.vagtplaner import VagtplanerClient
from typing import Optional

class TemponizerClientManager:
    def __init__(self, instance: str, client_id: str, client_secret: str, username: str, password: str) -> None:
        """
        Initialize the TemponizerClientManager with connection parameters.
        
        :param instance: The Temponizer instance name
        :param client_id: OAuth2 client ID
        :param client_secret: OAuth2 client secret
        :param username: Username for authentication
        :param password: Password for authentication
        """
        self.instance = instance
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self._client: Optional[TemponizerClient] = None
        self._vagtplaner: Optional[VagtplanerClient] = None


    @property
    def client(self) -> TemponizerClient:
        if self._client is None:
            self._client = TemponizerClient(
                instance=self.instance,
                client_id=self.client_id,
                client_secret=self.client_secret,
                username=self.username,
                password=self.password
            )
        return self._client

    @property
    def vagtplaner(self) -> VagtplanerClient:
        if self._vagtplaner is None:
            self._vagtplaner = VagtplanerClient(self.client)
        return self._vagtplaner