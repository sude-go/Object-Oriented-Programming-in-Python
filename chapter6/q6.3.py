class Television:
    def __init__(self):
        self.current_channel = 1

    def set_channel(self, channel):
        if channel == self.current_channel:
            print("Television is already tuned to channel", channel)
        else:
            self.current_channel = channel
            print("Television tuned to channel", channel)


# Example usage
tv = Television()
channel = int(input("Set channel to: "))
tv.set_channel(channel)
