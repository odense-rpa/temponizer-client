from temponizer_client.manager import TemponizerClientManager

def test_hent_institution(temponizer_manager: TemponizerClientManager):
    
    institution = temponizer_manager.institutioner.hent_institution(87)

    assert institution["name_short"] == "Holluf Pile Bo- og Særforanstaltning"