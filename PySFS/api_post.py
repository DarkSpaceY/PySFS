# api_post.py
from .client import SFSClient
from typing import Any, Dict, List, Optional, Union

class SFSPostAPI(SFSClient):
    """
    Wrapper for SFSControl Mod Server HTTP POST control APIs.
    """

    def set_throttle(self, size: float, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Set the rocket's throttle (engine power).

        Parameters:
            size (float): Throttle value between 0.0 and 1.0.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict: JSON response from the server.
        """
        return self._post("SetThrottle", [size, rocketIdOrName])

    def set_rcs(self, on: bool, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Toggle the RCS (Reaction Control System).

        Parameters:
            on (bool): True to enable RCS, False to disable.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("SetRCS", [on, rocketIdOrName])

    def stage(self, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Activate the next stage of the rocket.

        Parameters:
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("Stage", [rocketIdOrName])

    def rotate(
        self,
        is_target: bool,
        angle: float,
        reference: Optional[str] = None,
        direction: str = "left",
        rocketIdOrName: Optional[Union[int, str]] = None
    ) -> Dict[str, Any]:
        """
        Rotate the rocket or set orientation target.

        Parameters:
            is_target (bool): Whether it's a target angle or continuous rotation.
            angle (float): Angle in degrees.
            reference (str|None): Reference frame ('surface', 'orbit', etc.).
            direction (str): 'left', 'right', or 'auto'.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("Rotate", [is_target, angle, reference, direction, rocketIdOrName])

    def stop_rotate(self, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Force stop rocket rotation.

        Parameters:
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("StopRotate", [rocketIdOrName])

    def use_part(self, partId: int, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Use (activate) a specific rocket part.

        Parameters:
            partId (int): ID of the part to activate.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("UsePart", [partId, rocketIdOrName])

    def clear_debris(self) -> Dict[str, Any]:
        """
        Clear all debris from the scene.

        Returns:
            dict
        """
        return self._post("ClearDebris")

    def build(self, blueprint_json: str) -> Dict[str, Any]:
        """
        Build a rocket from blueprint JSON.

        Parameters:
            blueprint_json (str): Rocket blueprint in JSON string format.

        Returns:
            dict
        """
        return self._post("Build", [blueprint_json])

    def rcs_thrust(self, direction: str, seconds: float, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Apply RCS thrust for a duration.

        Parameters:
            direction (str): 'up', 'down', 'left', 'right', etc.
            seconds (float): Duration of thrust in seconds.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("RcsThrust", [direction, seconds, rocketIdOrName])

    def switch_to_build(self) -> Dict[str, Any]:
        """
        Switch the scene to build mode.

        Returns:
            dict
        """
        return self._post("SwitchToBuild")

    def clear_blueprint(self) -> Dict[str, Any]:
        """
        Clear current blueprint.

        Returns:
            dict
        """
        return self._post("ClearBlueprint")

    def set_rotation(self, angle: float, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Directly set the rocket's rotation angle.

        Parameters:
            angle (float): Angle in degrees.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("SetRotation", [angle, rocketIdOrName])

    def set_state(
        self,
        x: float,
        y: float,
        vx: float,
        vy: float,
        angularVelocity: float,
        blueprintJson: Optional[str] = None,
        rocketIdOrName: Optional[Union[int, str]] = None
    ) -> Dict[str, Any]:
        """
        Set the entire rocket state (position, velocity, blueprint).

        Parameters:
            x, y (float): Position coordinates.
            vx, vy (float): Velocity components.
            angularVelocity (float): Angular velocity.
            blueprintJson (str|None): Blueprint JSON to apply.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("SetState", [x, y, vx, vy, angularVelocity, blueprintJson, rocketIdOrName])

    def launch(self) -> Dict[str, Any]:
        """
        Launch the rocket from the build scene.

        Returns:
            dict
        """
        return self._post("Launch")

    def switch_rocket(self, idOrName: Union[int, str]) -> Dict[str, Any]:
        """
        Switch controlled rocket.

        Parameters:
            idOrName (int|str): Rocket ID or name to switch to.

        Returns:
            dict
        """
        return self._post("SwitchRocket", [idOrName])

    def rename_rocket(self, idOrName: Union[int, str], new_name: str) -> Dict[str, Any]:
        """
        Rename a rocket.

        Parameters:
            idOrName (int|str): Rocket identifier.
            new_name (str): New name.

        Returns:
            dict
        """
        return self._post("RenameRocket", [idOrName, new_name])

    def set_target(self, nameOrIndex: Union[int, str]) -> Dict[str, Any]:
        """
        Set navigation target.

        Parameters:
            nameOrIndex (int|str): Name or index of planet/rocket.

        Returns:
            dict
        """
        return self._post("SetTarget", [nameOrIndex])

    def clear_target(self) -> Dict[str, Any]:
        """
        Clear the current navigation target.

        Returns:
            dict
        """
        return self._post("ClearTarget")

    def timewarp_plus(self) -> Dict[str, Any]:
        """
        Increase timewarp speed by one level.

        Returns:
            dict
        """
        return self._post("TimewarpPlus")

    def timewarp_minus(self) -> Dict[str, Any]:
        """
        Decrease timewarp speed by one level.

        Returns:
            dict
        """
        return self._post("TimewarpMinus")

    def set_timewarp(self, speed: float, realtimePhysics: bool = False, showMessage: bool = True) -> Dict[str, Any]:
        """
        Set the simulation timewarp speed.

        Parameters:
            speed (float): Timewarp multiplier (e.g., 1.0, 1000.0).
            realtimePhysics (bool): True for real physics sim, False for rail.
            showMessage (bool): Whether to show an in-game message.

        Returns:
            dict
        """
        return self._post("SetTimewarp", [speed, realtimePhysics, showMessage])

    def wait(self, mode: Optional[str] = None) -> Dict[str, Any]:
        """
        Wait for transfer or rendezvous window.

        Parameters:
            mode (str|None): "transfer" or "rendezvous". Defaults to "transfer".

        Returns:
            dict
        """
        return self._post("Wait", [mode] if mode else [])

    def set_main_engine_on(self, on: bool, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Turn the main engine on or off.

        Parameters:
            on (bool): True to activate engine, False to stop.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("SetMainEngineOn", [on, rocketIdOrName])

    def set_orbit(
        self,
        radius: float,
        eccentricity: float,
        trueAnomaly: float,
        counterclockwise: bool,
        planetCode: str,
        rocketIdOrName: Optional[Union[int, str]] = None
    ) -> Dict[str, Any]:
        """
        Set the rocket's orbit.

        Parameters:
            radius (float): Orbital radius.
            eccentricity (float): Orbital eccentricity.
            trueAnomaly (float): True anomaly in degrees.
            counterclockwise (bool): True for CCW, False for CW.
            planetCode (str): Central body code.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("SetOrbit", [radius, eccentricity, trueAnomaly, counterclockwise, planetCode, rocketIdOrName])

    def delete_rocket(self, idOrName: Union[int, str]) -> Dict[str, Any]:
        """
        Delete a rocket.

        Parameters:
            idOrName (int|str): Rocket ID or name.

        Returns:
            dict
        """
        return self._post("DeleteRocket", [idOrName])

    def complete_challenge(self, challengeId: str) -> Dict[str, Any]:
        """
        Complete a mission challenge.

        Parameters:
            challengeId (str): Challenge identifier.

        Returns:
            dict
        """
        return self._post("CompleteChallenge", [challengeId])

    def track(self, nameOrIndex: Union[int, str]) -> Dict[str, Any]:
        """
        Set map focus to a rocket or planet.

        Parameters:
            nameOrIndex (int|str): Name or index.

        Returns:
            dict
        """
        return self._post("Track", [nameOrIndex])

    def switch_map_view(self, on: Optional[bool] = None) -> Dict[str, Any]:
        """
        Switch between map and world view.

        Parameters:
            on (bool|None): True=map, False=world. None to toggle.

        Returns:
            dict
        """
        args: List[Any] = [on] if on is not None else []
        return self._post("SwitchMapView", args)

    def unfocus(self) -> Dict[str, Any]:
        """
        Clear current map focus.

        Returns:
            dict
        """
        return self._post("Unfocus")

    def transfer_fuel(self, fromTankId: int, toTankId: int, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Transfer fuel between tanks.

        Parameters:
            fromTankId (int): Source tank ID.
            toTankId (int): Destination tank ID.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("TransferFuel", [fromTankId, toTankId, rocketIdOrName])

    def stop_fuel_transfer(self, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Stop all ongoing fuel transfers.

        Parameters:
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("StopFuelTransfer", [rocketIdOrName])

    def quicksave_manager(self, operation: str, name: Optional[str] = None) -> Dict[str, Any]:
        """
        Manage quicksaves: save, load, delete, rename.

        Parameters:
            operation (str): One of 'save', 'load', 'delete', 'rename'.
            name (str|None): Save name (for load/delete/rename).

        Returns:
            dict
        """
        args: List[Any] = [operation]
        if name is not None:
            args.append(name)
        return self._post("QuicksaveManager", args)

    def show_toast(self, message: str) -> Dict[str, Any]:
        """
        Show an in-game toast popup message.

        Parameters:
            message (str): Text to display.

        Returns:
            dict
        """
        return self._post("ShowToast", [message])

    def add_stage(self, index: int, partIds: List[int], rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Add a stage to the rocket.

        Parameters:
            index (int): Stage index.
            partIds (list of int): List of part IDs in this stage.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("AddStage", [index, partIds, rocketIdOrName])

    def remove_stage(self, index: int, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Remove a stage from the rocket.

        Parameters:
            index (int): Stage index to remove.
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        return self._post("RemoveStage", [index, rocketIdOrName])

    def log_message(self, type_str: str, message: str) -> Dict[str, Any]:
        """
        Write a message to the in-game debug log.

        Parameters:
            type_str (str): Message type ('log', 'warn', 'error').
            message (str): Message content.

        Returns:
            dict
        """
        return self._post("LogMessage", [type_str, message])

    def set_cheat(self, cheat_name: str, enabled: bool = True) -> Dict[str, Any]:
        """
        Enable or disable a cheat (e.g., infiniteFuel).

        Parameters:
            cheat_name (str): Cheat name.
            enabled (bool): True to enable, False to disable.

        Returns:
            dict
        """
        return self._post("SetCheat", [cheat_name, enabled])

    def revert(self, revert_type: str) -> Dict[str, Any]:
        """
        Revert the game to a previous state.

        Parameters:
            revert_type (str): One of 'launch', '30s', '3min', 'build'.

        Returns:
            dict
        """
        return self._post("Revert", [revert_type])

    def wheel_control(self, enable: Optional[bool] = None, turn_axis: float, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Control the direction of rover wheels.

        Parameters:
            enable (bool|None): Optional, True to enable wheel control, False to disable.
            turn_axis (float): Required, the axis to turn the wheels (-1 to 1).
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        params = [enable, turn_axis, rocketIdOrName]
        return self._post("WheelControl", params)
    
    def set_map_icon_color(self, rgba_value: str, rocketIdOrName: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        """
        Set the color of the rocket's map icon.

        Parameters:
            rgba_value (str): The color in rgba format (e.g., "#FF0000").
            rocketIdOrName (int|str|None): Optional rocket ID or name.

        Returns:
            dict
        """
        params = [rgba_value, rocketIdOrName]
        return self._post("SetMapIconColor", params)
    
    def create_rocket(self, planet_code: str, blueprint_json: str, rocket_name: Optional[str] = None, 
                  x: Optional[float] = None, y: Optional[float] = None, 
                  vx: Optional[float] = None, vy: Optional[float] = None, 
                  vr: Optional[float] = None) -> Dict[str, Any]:
        """
        Create a rocket from a blueprint at a specified location.

        Parameters:
            planet_code (str): Code of the planet where the rocket will be created.
            blueprint_json (str): JSON string representing the rocket's blueprint.
            rocket_name (str|None): Optional name for the new rocket.
            x (float|None): Optional x-coordinate for the rocket's position.
            y (float|None): Optional y-coordinate for the rocket's position.
            vx (float|None): Optional x-component of the rocket's initial velocity.
            vy (float|None): Optional y-component of the rocket's initial velocity.
            vr (float|None): Optional initial angular velocity of the rocket.

        Returns:
            dict
        """
        params = [planet_code, blueprint_json, rocket_name, x, y, vx, vy, vr]
        return self._post("CreateRocket", params)
    
    def create_object(self, object_type: str, planet_code: str, 
                  x: Optional[float] = None, y: Optional[float] = None, 
                  object_name: Optional[str] = None, hidden: Optional[bool] = None, 
                  explosion_size: Optional[float] = None, create_sound: Optional[bool] = None, 
                  create_shake: Optional[bool] = None, rotation: Optional[float] = None, 
                  angular_velocity: Optional[float] = None, ragdoll: Optional[bool] = None, 
                  fuel_percent: Optional[float] = None, temperature: Optional[float] = None, 
                  flag_direction: Optional[int] = None, show_flag_animation: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create various objects (e.g., astronauts, explosions) with full parameter control.

        Parameters:
            object_type (str): Type of object to create (e.g., "astronaut").
            planet_code (str): Code of the planet where the object will be created.
            x (float|None): Optional x-coordinate for the object's position.
            y (float|None): Optional y-coordinate for the object's position.
            object_name (str|None): Optional name for the new object.
            hidden (bool|None): Optional, True to hide the object initially.
            explosion_size (float|None): Optional size of the explosion (if applicable).
            create_sound (bool|None): Optional, True to create a sound effect.
            create_shake (bool|None): Optional, True to create a screen shake effect.
            rotation (float|None): Optional initial rotation of the object.
            angular_velocity (float|None): Optional initial angular velocity of the object.
            ragdoll (bool|None): Optional, True to enable ragdoll physics.
            fuel_percent (float|None): Optional fuel percentage (if applicable).
            temperature (float|None): Optional initial temperature of the object.
            flag_direction (int|None): Optional direction for the flag (if applicable).
            show_flag_animation (bool|None): Optional, True to show flag animation.

        Returns:
            dict
        """
        params = [object_type, planet_code, x, y, object_name, hidden, explosion_size, create_sound, create_shake, rotation, angular_velocity, ragdoll, fuel_percent, temperature, flag_direction, show_flag_animation]
        return self._post("CreateObject", params)