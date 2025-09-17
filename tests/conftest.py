import pytest
import os

from dotenv import load_dotenv
from temponizer_client.manager import TemponizerClientManager

load_dotenv()

@pytest.fixture(scope="session")
def temponizer_manager():
    """
    Pytest fixture that provides a TemponizerClientManager instance for testing.
    
    Reads configuration from environment variables:
    - INSTANCE: The Temponizer instance name
    - CLIENT_ID: OAuth2 client ID
    - CLIENT_SECRET: OAuth2 client secret
    - MAIL: Email address for authentication (used as username)
    - PASSWORD: Password for authentication
    """
    instance = os.getenv("INSTANCE")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    username = os.getenv("MAIL")  # Email is used as username
    password = os.getenv("PASSWORD")
    
    # Ensure all required environment variables are set
    if not all([instance, client_id, client_secret, username, password]):
        pytest.skip("Missing required environment variables for Temponizer client")
    
    return TemponizerClientManager(
        instance=instance,
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password
    )


@pytest.fixture(scope="session")
def base_client(temponizer_manager):
    """Returns the underlying TemponizerClient."""
    return temponizer_manager.client


@pytest.fixture(scope="session")
def vagtplaner_client(temponizer_manager):
    """Returns the VagtplanerClient for shift plan operations."""
    return temponizer_manager.vagtplaner


