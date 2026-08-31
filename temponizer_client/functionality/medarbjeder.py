from temponizer_client.client import TemponizerClient
from typing import Optional

class MedarbjederClient:
    def __init__(self, client: TemponizerClient) -> None:
        self._client = client

    def hent_medarbejder(self, medarbejderId: int) -> Optional[dict]:
        """
        Henter en specifik medarbejder baseret på medarbejder ID.
        
        :param medarbejderId: ID på medarbejderen der skal hentes
        :return: Dictionary med medarbejder data eller None hvis ikke fundet
        """
        endpoint = f"/worker/{medarbejderId}"
        
        response = self._client.get(endpoint)
        
        if response.status_code == 404:
            return None
        return response.json()

    def hent_alle_medarbejdere(self) -> Optional[list]:
        """
        Henter alle medarbejdere.
        
        :return: Liste af medarbejder dictionaries eller None hvis ingen fundet
        """
        endpoint = "/worker"
        
        response = self._client.get(endpoint)
        
        if response.status_code == 404:
            return None
        return response.json()

    def hent_medarbejder_uddannelse(self, medarbejderId: int) -> Optional[dict]:
        endpoint = f"/worker/{medarbejderId}/education"

        response = self._client.get(endpoint)

        if response.status_code == 404:
            return None
        return response.json()

    def hent_medarbejder_skill(self, medarbejderId: int) -> Optional[dict]:
        endpoint = f"/worker/{medarbejderId}/skill"

        response = self._client.get(endpoint)

        if response.status_code == 404:
            return None
        return response.json()