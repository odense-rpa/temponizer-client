from temponizer_client.client import TemponizerClient
from typing import Optional
from datetime import date
from enum import Enum

class PlanType(Enum):
    RECENT = "recent"
    UPCOMING = "upcoming"
    ONGOING = "ongoing"
    HELD_UNAPPROVED = "held_unapproved"
    HELD_APPROVED = "held_approved"
    OBSERVE = "observe"
    CANCELLED_FILLED = "cancelled_filled"
    EXCLUDED_FROM_INVOICING = "excluded_from_invoicing"

class VagtplanerClient:
    def __init__(self, client: TemponizerClient):
        self._client = client
    
    def hent_vagtplan(self, startdato: date, slutdato: date, plantype: PlanType) -> Optional[dict]:
        """
        Henter vagtplan af en bestemt type inden for et dato spænd

        Tidspunkter i svaret returneres i UTC (med ``Z``-suffix). De er derfor
        2 timer bagud i forhold til dansk sommertid og 1 time bagud i forhold
        til dansk normaltid. Konverter dem til lokal tid ved visning.

        """

        endpoint = f"/shift/admin/{plantype.value}"
        params = {
            'from_date': startdato.isoformat(),
            'to_date': slutdato.isoformat()
        }
        response = self._client.get(endpoint, params=params)
        if response.status_code == 404:
            return None
        return response.json()
    

