import httpx
import logging

from urllib.parse import urljoin
from .hooks import create_response_logging_hook
from authlib.integrations.httpx_client import OAuth2Client

class TemponizerClient:
    def __init__(self, instance: str, client_id: str, client_secret: str, username: str, password: str) -> None:
       
        self.logger = logging.getLogger(__name__)
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("httpcore").setLevel(logging.WARNING)

        # Create response logging hook
        response_hook = create_response_logging_hook(logger=self.logger)
        hooks = {'response': [response_hook]}

        self.instance = instance.rstrip('/')
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password

        self.token_url = f"https://{instance}.temponizer.dk/Temponizer/API/index.php/api/v3/oauth/token"
        self.base_url = f"https://{instance}.temponizer.dk/Temponizer/API/index.php/api/v3/"
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        
        self._client = OAuth2Client(
            client_id=client_id,
            client_secret=client_secret,
            content_type='application/x-www-form-urlencoded',
            token_endpoint=self.token_url,
            event_hooks=hooks
        )

        self._client.fetch_token(
            url=self.token_url,
            grant_type='password',
            username=username,
            password=password,
            scope='application:read customer:full workers:full shifts:full admin:export',
            auth=None  # disables Basic Auth so client_id/secret goes in the body
        )
    
    def _normalize_url(self, endpoint: str) -> str:
        """Ensure the URL is absolute, handling relative URLs."""
        if endpoint.startswith("http://") or endpoint.startswith("https://"):
            return endpoint
        
        # Remove leading slash from endpoint to avoid urljoin replacing the base path
        endpoint = endpoint.lstrip("/")
        return urljoin(self.base_url + "/", endpoint)
    

    def get(self, endpoint: str, **kwargs) -> httpx.Response:
        """
        Perform GET request to the specified endpoint.

        :param endpoint: API endpoint (relative or absolute URL)
        :param kwargs: Additional arguments passed to httpx
        :return: HTTP response
        """
        url = self._normalize_url(endpoint)
        response = self._client.get(url, **kwargs)
        response.raise_for_status()
        return response

    def post(self, endpoint: str, json: dict | None = None, **kwargs) -> httpx.Response:
        """
        Perform POST request to the specified endpoint.

        :param endpoint: API endpoint (relative or absolute URL)
        :param json: JSON data to send in request body
        :param kwargs: Additional arguments passed to httpx
        :return: HTTP response
        """
        url = self._normalize_url(endpoint)
        response = self._client.post(url, json=json, **kwargs)
        response.raise_for_status()
        return response

    def put(self, endpoint: str, json: dict | None = None, **kwargs) -> httpx.Response:
        """
        Perform PUT request to the specified endpoint.

        :param endpoint: API endpoint (relative or absolute URL)
        :param json: JSON data to send in request body
        :param kwargs: Additional arguments passed to httpx
        :return: HTTP response
        """
        url = self._normalize_url(endpoint)
        response = self._client.put(url, json=json, **kwargs)
        response.raise_for_status()
        return response

    def delete(self, endpoint: str, **kwargs) -> httpx.Response:
        """
        Perform DELETE request to the specified endpoint.

        :param endpoint: API endpoint (relative or absolute URL)
        :param kwargs: Additional arguments passed to httpx
        :return: HTTP response
        """
        url = self._normalize_url(endpoint)
        response = self._client.delete(url, **kwargs)
        response.raise_for_status()
        return response

    

