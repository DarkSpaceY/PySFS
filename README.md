# 🛰️ PySFS

**PySFS** is a lightweight Python library to interact with the [Spaceflight Simulator Control Mod Server (SFSControl)](https://github.com/SFSPlayer-sys/SFSControl) via HTTP.
It provides high-level access to GET and POST endpoints for controlling rockets, retrieving telemetry, and issuing commands in real-time.

## 🚀 Features

* Simple client to connect to SFSControl server
* Built-in support for GET and POST API calls
* Typed, user-friendly method interfaces
* Lightweight, dependency-free except for `requests`

## 📦 Installation

```bash
pip install PySFS
```

> ⚠️ Requires the [SFSControl mod](https://github.com/SFSPlayer-sys/SFSControl) to be running in your SFS world at the specified IP and port.

## 🧠 Usage Example

```python
from PySFS import SFSGetAPI

# Initialize client (default: localhost:27772)
client = SFSGetAPI()

# GET: Retrieve current rocket state
rocket_data = client.rocket()
print("Rocket Data JSON:", rocket_data)
```

## 🧩 API Overview

### GET Methods

| Method                     | Description                                                                 | Parameters                                                                 |
|----------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `rockets()`                | Get a list of all rockets in the scene                                      | None                                                                       |
| `rocket_sim()`             | Get detailed simulation info for a rocket                                   | `rocketIdOrName`: Rocket ID or name (defaults to current rocket)           |
| `rocket()`                 | Get the save info of a specific rocket                                      | `rocketIdOrName`: Rocket ID or name (defaults to current rocket)           |
| `planets()`                | Get detailed info for all planets                                           | None                                                                       |
| `planet()`                 | Get detailed info of a specific planet                                      | `codename`: Planet code name (defaults to current planet)                  |
| `other()`                  | Get miscellaneous info (transfer window ΔV, fuel bars, etc.) for a rocket   | `rocketIdOrName`: Rocket ID or name (defaults to current rocket)           |
| `debuglog()`               | Get the game console log                                                    | None                                                                       |
| `mission()`                | Get current mission status and mission log                                  | None                                                                       |
| `planet_terrain()`         | Get terrain height data for a planet                                        | `planetCode`: Planet code, `start`: start degree, `end`: end degree, `count`: samples |
| `rcall()`                  | Perform a reflective call to invoke any public static method (USE WITH CAUTION) | `type_name`: Full type name, `method_name`: Method name, `call_args`: Arguments list |
| `screenshot()` | Get a screenshot of the SFS game window in PNG format (requires allowScreenshot enabled) | Returns: bytes (PNG image data) |


### POST Methods

| Method                          | Description                                                                 | Parameters                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `set_throttle(size)`            | Set rocket throttle (0.0-1.0)                                               | `size`: Throttle value, `rocketIdOrName`: Optional rocket identifier       |
| `set_rcs(on)`                   | Toggle RCS (Reaction Control System)                                        | `on`: True/False, `rocketIdOrName`: Optional rocket identifier             |
| `stage()`                       | Activate next stage                                                         | `rocketIdOrName`: Optional rocket identifier                               |
| `rotate(is_target, angle)`      | Rotate rocket or set target orientation                                     | `is_target`: Target/continuous, `angle`: Degrees, `reference`: Frame, `direction`: Left/right/auto |
| `stop_rotate()`                 | Stop all rotation                                                           | `rocketIdOrName`: Optional rocket identifier                               |
| `use_part(partId)`              | Activate specific rocket part                                               | `partId`: Part ID, `rocketIdOrName`: Optional rocket identifier            |
| `clear_debris()`                | Remove all debris from scene                                                | None                                                                       |
| `build(blueprint_json)`         | Build rocket from blueprint                                                 | `blueprint_json`: Rocket design in JSON                                    |
| `rcs_thrust(direction, seconds)`| Apply RCS thrust in direction for duration                                  | `direction`: Up/down/etc, `seconds`: Duration, `rocketIdOrName`: Optional  |
| `switch_to_build()`             | Switch to build mode                                                        | None                                                                       |
| `clear_blueprint()`             | Clear current blueprint                                                     | None                                                                       |
| `set_rotation(angle)`           | Directly set rocket rotation angle                                          | `angle`: Degrees, `rocketIdOrName`: Optional rocket identifier             |
| `set_state(x,y,vx,vy,...)`      | Set complete rocket state                                                   | Position, velocity, angular velocity, blueprint, optional rocket identifier|
| `launch()`                      | Launch rocket from build scene                                              | None                                                                       |
| `switch_rocket(idOrName)`       | Change controlled rocket                                                    | `idOrName`: Rocket identifier                                              |
| `rename_rocket(idOrName, name)` | Rename a rocket                                                             | `idOrName`: Current ID, `new_name`: New name                               |
| `set_target(nameOrIndex)`       | Set navigation target                                                       | `nameOrIndex`: Planet/rocket identifier                                    |
| `clear_target()`                | Clear navigation target                                                     | None                                                                       |
| `timewarp_plus()`               | Increase time warp                                                          | None                                                                       |
| `timewarp_minus()`              | Decrease time warp                                                          | None                                                                       |
| `set_timewarp(speed)`           | Set exact time warp speed                                                   | `speed`: Multiplier, `realtimePhysics`: True/False, `showMessage`: True/False |
| `wait(mode)`                    | Wait for transfer/rendezvous window                                         | `mode`: "transfer" or "rendezvous"                                         |
| `set_main_engine_on(on)`        | Toggle main engine                                                          | `on`: True/False, `rocketIdOrName`: Optional rocket identifier             |
| `set_orbit(params)`             | Set rocket orbit parameters                                                 | Radius, eccentricity, true anomaly, direction, planet code, optional rocket|
| `delete_rocket(idOrName)`       | Remove rocket from scene                                                    | `idOrName`: Rocket identifier                                              |
| `complete_challenge(challengeId)`| Complete mission challenge                                                  | `challengeId`: Challenge identifier                                        |
| `track(nameOrIndex)`            | Set map focus                                                               | `nameOrIndex`: Object identifier                                           |
| `switch_map_view(on)`           | Toggle map/world view                                                       | `on`: True=map, False=world, None=toggle                                   |
| `unfocus()`                     | Clear map focus                                                             | None                                                                       |
| `transfer_fuel(fromTank,toTank)`| Move fuel between tanks                                                     | Tank IDs, optional rocket identifier                                       |
| `stop_fuel_transfer()`          | Cancel all fuel transfers                                                   | `rocketIdOrName`: Optional rocket identifier                               |
| `quicksave_manager(op,name)`    | Manage quicksaves                                                           | `operation`: save/load/delete/rename, `name`: Save name                    |
| `show_toast(message)`           | Display popup message                                                       | `message`: Text to show                                                    |
| `add_stage(index, partIds)`     | Add new rocket stage                                                        | `index`: Stage position, `partIds`: List of parts, optional rocket         |
| `remove_stage(index)`           | Remove rocket stage                                                         | `index`: Stage to remove, optional rocket identifier                       |
| `log_message(type, message)`    | Write to debug log                                                          | `type`: log/warn/error, `message`: Content                                 |
| `set_cheat(name, enabled)`      | Enable/disable cheat                                                        | `cheat_name`: Cheat ID, `enabled`: True/False                              |
| `revert(type)`                  | Revert game state                                                           | `revert_type`: launch/30s/3min/build                                       |
| `wheel_control(enable, turn_axis, rocketIdOrName)` | Control rover wheel direction                                                 | `enable`: Optional bool (enable/disable), `turn_axis`: Required float (-1 to 1), `rocketIdOrName`: Optional int/str |
| `set_map_icon_color(rgba_value, rocketIdOrName)`    | Set rocket map icon color                                                   | `rgba_value`: str (e.g., "#FF0000"), `rocketIdOrName`: Optional int/str                                             |
| `create_rocket(planet_code, blueprint_json, ...)`   | Create rocket from blueprint at specified location                           | `planet_code`: str, `blueprint_json`: str, `rocket_name`: Optional str, `x`: Optional float, `y`: Optional float, `vx`: Optional float, `vy`: Optional float, `vr`: Optional float |
| `create_object(object_type, planet_code, ...)`      | Create various objects (e.g., astronauts, explosions) with full parameter control | `object_type`: str, `planet_code`: str, `x`: Optional float, `y`: Optional float, `object_name`: Optional str, `hidden`: Optional bool, `explosion_size`: Optional float, `create_sound`: Optional bool, `create_shake`: Optional bool, `rotation`: Optional float, `angular_velocity`: Optional float, `ragdoll`: Optional bool, `fuel_percent`: Optional float, `temperature`: Optional float, `flag_direction`: Optional int, `show_flag_animation`: Optional bool |


## ⚙️ Configuration

You can specify the server IP and port if different from default:

```python
client = SFSClient(host="192.168.1.10", port=27772)
```

## 📁 Project Structure

```text
PySFS/
├── PySFS/
│   ├── __init__.py
│   ├── client.py         # Main SFSClient class
│   ├── api_get.py        # GET interface
│   └── api_post.py       # POST interface
├── setup.py
├── pyproject.toml
└── README.md
```

## 🛡️ License

MIT License © 2025 [DarkSpaceY](https://github.com/DarkSpaceY)

## 🛰️ About SFSControl

This library communicates with the SFSControl mod for Spaceflight Simulator, which exposes an HTTP API for programmatic control and monitoring of in-game rockets.

> This library is not officially affiliated with SFS or its developers.
