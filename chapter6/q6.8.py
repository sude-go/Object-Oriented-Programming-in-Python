class Television:
    def __init__(self):
        self._power_on = False
        self._volume = 5
        self._channel = 1
        self._mute = False

    def toggle_power(self):
        self._power_on = not self._power_on

    def set_volume(self, volume):
        if 0 <= volume <= 10:
            self._volume = volume

    def increase_volume(self):
        if self._volume < 10:
            self._volume += 1

    def decrease_volume(self):
        if self._volume > 0:
            self._volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 100:
            self._channel = channel

    def toggle_mute(self):
        self._mute = not self._mute

    def is_muted(self):
        return self._mute

    def __str__(self):
        power_status = "ON" if self._power_on else "OFF"
        mute_status = "Muted" if self._mute else "Unmuted"
        return f"Power: {power_status}, Volume: {self._volume}, Channel: {self._channel}, {mute_status}"


tv = Television()
print(tv)

tv.toggle_power()
tv.set_volume(8)
tv.set_channel(3)
tv.toggle_mute()
print(tv)

tv.toggle_power()
tv.toggle_power()
print(tv)
