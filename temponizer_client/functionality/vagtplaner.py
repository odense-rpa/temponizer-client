from temponizer_client.client import TemponizerClient
from typing import Optional
from datetime import date

class VagtplanerClient:
    def __init__(self, client: TemponizerClient):
        self._client = client
    
    def hent_vagtplan(self, startdato: date, slutdato: date, plantype: str) -> Optional[dict]:
        """
        Henter vagtplan af en bestemt type inden for et dato spænd

        """

        endpoint = f"/shift/admin/{plantype}"
        params = {
            'startdate': startdato.isoformat(),
            'enddate': slutdato.isoformat()
        }
        response = self._client.get(endpoint, params=params)
        if response.status_code == 404:
            return None
        return response.json()
    

