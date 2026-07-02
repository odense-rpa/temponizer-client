import os
import pytest
from temponizer_client.manager import TemponizerClientManager

def test_hent_medarbejder(temponizer_manager: TemponizerClientManager):
    medarbejder_id = os.getenv("TEST_MEDARBEJDER_ID")
    if not medarbejder_id:
        pytest.skip("TEST_MEDARBEJDER_ID not set")

    medarbejder = temponizer_manager.medarbejder.hent_medarbejder(int(medarbejder_id))

    assert medarbejder.get("name")
