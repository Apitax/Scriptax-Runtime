from apitaxcore.logs.Log import Log
from apitaxcore.logs.StandardLog import StandardLog
from apitaxcore.models.State import State
from apitaxcore.models.Options import Options
from apitaxcore.flow.LoadedDrivers import LoadedDrivers
from apitaxcore.drivers.Drivers import Drivers
from scriptax.parser.utils.BoilerPlate import customizable_parser, read_string, read_file
from scriptax.models.BlockStatus import BlockStatus
from typing import Tuple
from scriptax.parser.Visitor import AhVisitor
from scriptax_runtime.ScriptaxDriver import ScriptaxDriver

State.log = Log(StandardLog(), logColorize=False)
State.log.log("")


def execute(file: str, debug: bool = False) -> Tuple[BlockStatus, AhVisitor]:
    Drivers.add("scriptax", ScriptaxDriver(path=file))
    LoadedDrivers.load("scriptax")
    return customizable_parser(read_file(file), file=file, options=Options(debug=debug))