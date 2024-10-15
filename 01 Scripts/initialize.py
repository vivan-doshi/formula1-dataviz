import pandas as pd
import fastf1
from fastf1.core import Laps

#load session from qualifying session of the 10th race in 2024
session = fastf1.get_session(2024, 10, "Q")
session.load()

#load best lap from driver
LapNor = session.laps.pick_driver("NOR").pick_fastest()
LapVer = session.laps.pick_driver("VER").pick_fastest()
LapHam = session.laps.pick_driver("HAM").pick_fastest()
LapSar = session.laps.pick_driver("SAR").pick_fastest()

#get telemetry of each lap
NOR = LapNor.get_telemetry()
VER = LapVer.get_telemetry()
HAM = LapHam.get_telemetry()
SAR = LapSar.get_telemetry()