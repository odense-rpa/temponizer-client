from temponizer_client.client import TemponizerClient
from typing import Optional

class InstitutionerClient:
    def __init__(self, client: TemponizerClient) -> None:
        self._client = client

    def hent_institution(self, institutionId: int) -> Optional[dict]:
        """
        Henter en specifik institution baseret på institution ID.
        
        :param institutionId: ID på institutionen der skal hentes
        :return: Dictionary med institution data eller None hvis ikke fundet
        """
        endpoint = f"/customer/{institutionId}"
        
        response = self._client.get(endpoint)
        
        if response.status_code == 404:
            return None
        return response.json()

    def hent_alle_institutioner(self) -> Optional[list]:
        """
        Henter alle institutioner.
        
        :return: Liste af institution dictionaries eller None hvis ingen fundet
        """
        endpoint = "/customer"
        
        response = self._client.get(endpoint)
        
        if response.status_code == 404:
            return None
        return response.json()