import requests


class SFSClient:
    """
    Base client for SFSControl Mod Server.
    Handles HTTP session and basic GET/POST mechanics.
    """
    def __init__(self, host: str = '127.0.0.1', port: int = 27772):
        """
        Initialize the client.

        Parameters:
            host (str): Server host address.
            port (int): Server port number.
        """
        self.base_url = f"http://{host}:{port}"
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def _get(self, path: str, params: dict = None) -> dict:
        """
        Internal GET request wrapper.

        Parameters:
            path (str): API path (e.g., '/rockets').
            params (dict): Query parameters.

        Returns:
            dict: Parsed JSON response.
        """
        response = self.session.get(f"{self.base_url}{path}", params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, method: str, args: list = None) -> dict:
        """
        Internal POST request wrapper for control APIs.

        Parameters:
            method (str): Control method name (e.g., 'Stage').
            args (list): List of method arguments.

        Returns:
            dict: Parsed JSON response.
        """
        data = {"method": method, "args": args or []}
        response = self.session.post(f"{self.base_url}/control", json=data)
        response.raise_for_status()
        return response.json()