# api_get.py
from .client import SFSClient
from typing import Any, Dict, Optional, Union

class SFSGetAPI(SFSClient):
    """
    Wrapper for SFSControl Mod Server HTTP GET information APIs.
    """

    def rockets(self) -> Dict[str, Any]:
        """
        Get a list of all rockets in the scene.

        Returns:
            dict: JSON response containing rocket list.
        """
        return self._get("/rockets")

    def rocket_sim(self, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Get detailed simulation info for the specified rocket.

        Parameters:
            rocketIdOrName (int|str|None): Rocket ID or name. Defaults to current rocket.

        Returns:
            dict: JSON response with simulation details.
        """
        params = {"rocketIdOrName": rocketIdOrName} if rocketIdOrName is not None else None
        return self._get("/rocket_sim", params)

    def rocket(self, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Get the save info of a specific rocket.

        Parameters:
            rocketIdOrName (int|str|None): Rocket ID or name. Defaults to current rocket.

        Returns:
            dict: JSON response with rocket save info.
        """
        params = {"rocketIdOrName": rocketIdOrName} if rocketIdOrName is not None else None
        return self._get("/rocket", params)

    def planets(self) -> Dict[str, Any]:
        """
        Get detailed info for all planets.

        Returns:
            dict: JSON response containing planet list.
        """
        return self._get("/planets")

    def planet(self, codename: Optional[str] = None) -> Dict[str, Any]:
        """
        Get detailed info of the specified planet.

        Parameters:
            codename (str|None): Planet code name. Defaults to current planet.

        Returns:
            dict: JSON response with planet details.
        """
        params = {"codename": codename} if codename is not None else None
        return self._get("/planet", params)

    def other(self, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Get miscellaneous info (transfer window ΔV, fuel bars, nav target, etc.) for a rocket.

        Parameters:
            rocketIdOrName (int|str|None): Rocket ID or name. Defaults to current rocket.

        Returns:
            dict: JSON response with miscellaneous data.
        """
        params = {"rocketIdOrName": rocketIdOrName} if rocketIdOrName is not None else None
        return self._get("/other", params)

    def debuglog(self) -> Dict[str, Any]:
        """
        Get the game console log.

        Returns:
            dict: JSON response with debug log entries.
        """
        return self._get("/debuglog")

    def mission(self) -> Dict[str, Any]:
        """
        Get current mission status and mission log.

        Returns:
            dict: JSON response with mission data.
        """
        return self._get("/mission")

    def planet_terrain(
        self,
        planetCode: str,
        start: Optional[float] = None,
        end: Optional[float] = None,
        count: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Get an array of terrain heights for the specified planet.

        Parameters:
            planetCode (str): Planet code (e.g., "Moon").
            start (float|None): Start degree.
            end (float|None): End degree.
            count (int|None): Number of samples (use -1 for max precision).

        Returns:
            dict: JSON response with terrain height array.
        """
        params: Dict[str, Any] = {"planetCode": planetCode}
        if start is not None: params["start"] = start
        if end is not None:   params["end"] = end
        if count is not None: params["count"] = count
        return self._get("/planet_terrain", params)

    def rcall(self, type_name: str, method_name: str, call_args: list) -> Dict[str, Any]:
        """
        Perform a reflective call: invoke any public static method on the SFS side.

        WARNING: Use with caution.

        Parameters:
            type_name (str): Full type name (e.g., "Namespace.ClassName").
            method_name (str): Method name to call.
            call_args (list): List of arguments for the call.

        Returns:
            dict: JSON response with the result of the method invocation.
        """
        data = {"type": type_name, "methodName": method_name, "callArgs": call_args}
        # Note: This uses POST rather than GET
        response = self.session.post(f"{self.base_url}/rcall", json=data)
        response.raise_for_status()
        return response.json()

    def screenshot(self) -> Dict[str, Any]:
        """
        Get a screenshot of the SFS game window in PNG format.
    
        Requires 'allowScreenshot' to be enabled in the game settings.

        Returns:
            dict
        """
        # Send a GET request to the /screenshot endpoint
        return self._get("/screenshot")

