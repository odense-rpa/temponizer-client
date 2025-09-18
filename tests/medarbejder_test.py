from temponizer_client.manager import TemponizerClientManager

def test_hent_medarbejder(temponizer_manager: TemponizerClientManager):
    
    medarbjeder = temponizer_manager.medarbejder.hent_medarbejder(907)

    assert medarbjeder["name"].startswith("Anne Mette")
