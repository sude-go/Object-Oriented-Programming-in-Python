class Television:
    def __init__(self):
        self._powerOn = False
        self._muted = False
        self._volume = 5
        self._channel = 2
        self._prevChan = 2

    def togglePower(self):
        """
        Toggles the power of the television.
        """
        self._powerOn = not self._powerOn
        return self._powerOn

    def toggleMute(self):
        """
        Toggles the mute setting of the television.
        """
        if self._powerOn:
            self._muted = not self._muted
        return self._muted

    def volumeUp(self):
        """
        Increases the volume by 1.
        If the maximum volume is reached,
        the volume remains unchanged.
        """
        if self._powerOn:
            if self._volume < 10:
                self._volume += 1
            self._muted = False
        return self._volume

    def volumeDown(self):
        """
        Decreases the volume by 1.
        If the minimum volume is reached,
        the volume remains unchanged.
        """
        if self._powerOn:
            if self._volume > 0:
                self._volume -= 1
            self._muted = False
        return self._volume

    def channelUp(self):
        """
        Increases the channel by 1.
        If the maximum channel is reached,
        the channel wraps around to 2.
        """
        if self._powerOn:
            self._prevChan = self._channel
            if self._channel == 99:
                self._channel = 2
            else:
                self._channel += 1
        return self._channel

    def channelDown(self):
        """
        Decreases the channel by 1.
        If the minimum channel is reached,
        the channel wraps around to 99.
        """
        if self._powerOn:
            self._prevChan = self._channel
            if self._channel == 2:
                self._channel = 99
            else:
                self._channel -= 1
        return self._channel

    def setChannel(self, number):
        """
        Sets the channel to the given number.
        If the number is outside the valid range (2-99),
        the channel remains unchanged.
        """
        if self._powerOn:
            if 2 <= number <= 99:
                self._prevChan = self._channel
                self._channel = number
        return self._channel

    def jumpPrevChannel(self):
        """
        Switches the channel to the previous channel.
        If the previous channel was 2, the channel wraps around to 99.
        """
        if self._powerOn:
            incoming = self._channel
            self._channel = self._prevChan
            self._prevChan = incoming
        return self._channel

    def __str__(self):
        """
        Returns a string that represents the current state of the television.
        """
        display = 'Power setting is currently ' + str(self._powerOn) + '\n'
        display += 'Channel setting is currently ' + str(self._channel) + '\n'
        display += 'Volume setting is currently ' + str(self._volume) + '\n'
        display += 'Mute is currently ' + str(self._muted)
        return display
