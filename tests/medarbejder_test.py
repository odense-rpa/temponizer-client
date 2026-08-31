import os
import pytest
from temponizer_client.manager import TemponizerClientManager

def test_hent_medarbejder(temponizer_manager: TemponizerClientManager):
    medarbejder_id = os.getenv("TEST_MEDARBEJDER_ID")
    if not medarbejder_id:
        pytest.skip("TEST_MEDARBEJDER_ID not set")

    medarbejder = temponizer_manager.medarbejder.hent_medarbejder(int(medarbejder_id))

    assert medarbejder.get("name")


def test_hent_medarbejder_uddannelse(temponizer_manager: TemponizerClientManager):
    medarbejder_id = os.getenv("TEST_MEDARBEJDER_ID")
    if not medarbejder_id:
        pytest.skip("TEST_MEDARBEJDER_ID not set")

    uddannelsesinfo = temponizer_manager.medarbejder.hent_medarbejder_uddannelse(int(medarbejder_id))

    assert uddannelsesinfo is not None

def test_hent_medarbejder_skill(temponizer_manager: TemponizerClientManager):
    medarbejder_id = os.getenv("TEST_MEDARBEJDER_ID")
    if not medarbejder_id:
        pytest.skip("TEST_MEDARBEJDER_ID not set")

    evner = temponizer_manager.medarbejder.hent_medarbejder_skill(int(medarbejder_id))

    assert evner is not None

