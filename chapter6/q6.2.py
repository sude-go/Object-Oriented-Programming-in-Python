"""
class Radio():  -> Removed unnecessary parentheses
    def init(self): -> __init__
        self._powerOn = False
        self._volume = 5
        self._station = 90.7
        self._presets = [90.7, 92.3, 94.7, 98.1, 105.7, 107.7]

    def togglePower(self):
        self._powerOn = not self._powerOn

    def setPreset(self, ind):
        self._presets[ind] = _station  -> To define need to add self

    def gotoPreset(self, ind):
        self._station = self._presets[ind]

    def increaseVolume(self): (
        self._volume) = self._volume + 1 -> Removed unnecessary parentheses

    def decreaseVolume(self): (
        self._volume) = self._volume - 1 -> Removed unnecessary parentheses

    def increaseStation(self):
        self._station = self._station + .2 -> Corrected the syntax

    def decreaseStation(self):
        self._station = self._station − .2 -> Corrected the syntax

"""


class Radio:
    def __init__(self):
        self._powerOn = False
        self._volume = 5
        self._station = 90.7
        self._presets = [90.7, 92.3, 94.7, 98.1, 105.7, 107.7]

    def toggle_power(self):
        self._powerOn = not self._powerOn

    def set_preset(self, ind):
        if 0 <= ind < len(self._presets):
            self._presets[ind] = self._station
            return f"Preset {ind} set to current station {self._station}"
        else:
            return f"Invalid preset index {ind}"

    def go_to_preset(self, ind):
        if 0 <= ind < len(self._presets):
            self._station = self._presets[ind]
            return f"Station set to preset {ind}: {self._station}"
        else:
            return f"Invalid preset index {ind}"

    def increase_volume(self):
        self._volume += 1
        return "Volume is increased by 1"

    def decrease_volume(self):
        self._volume -= 1
        return "Volume is decreased by 1"

    def increase_station(self):
        self._station += 0.2

    def decrease_station(self):
        self._station -= 0.2

    def __str__(self):
        return (
            f"Power: {self._powerOn},\n"
            f"Volume: {self._volume},\n"
            f"Station: {self._station},\n"
            f"Presets: {self._presets}\n"
        )


# Test cases
test_radio = Radio()
print(test_radio)

test_radio.toggle_power()

test_radio.increase_volume()
test_radio.decrease_volume()

print(test_radio.set_preset(1))
print(test_radio.go_to_preset(1))

test_radio.increase_station()
test_radio.decrease_station()

test_radio.toggle_power()

print(test_radio)
