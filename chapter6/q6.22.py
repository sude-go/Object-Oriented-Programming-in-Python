from cs1graphics import *

tv_bg = {1: "red", 2: "green", 3: "blue", 4: "yellow", 5: "white", 6: "purple", 7: "gray"}


class Television:
    def __init__(self, current_channel=1):
        self.can = Canvas(400, 400, "black", "Television")

        self.channel_text = Text(f"Channel {current_channel}", 20, Point(200, 50))
        self.channel_text.setFontColor("white")
        self.can.add(self.channel_text)

        self.volume_text = Text("Volume \n ===-------", 20, Point(200, 350))
        self.volume_text.setFontColor("white")
        self.can.add(self.volume_text)

        self.tv_bg = Rectangle(200, 200, Point(200, 200))
        self.tv_bg.setFillColor(tv_bg[current_channel])
        self.can.add(self.tv_bg)

        self.current_channel = current_channel
        self.prev_channel = None

        self.favorite_channels = []
        self.volume = 3

    def change_channel(self, new_channel):
        if new_channel in tv_bg:
            self.prev_channel = self.current_channel
            self.current_channel = new_channel
            self.channel_text.setMessage(f"Channel {new_channel}")
            self.tv_bg.setFillColor(tv_bg[new_channel])

    def jump_prev_channel(self):
        if self.prev_channel is not None:
            self.change_channel(self.prev_channel)

    def add_to_favorites(self):
        if self.current_channel not in self.favorite_channels:
            self.favorite_channels.append(self.current_channel)
            self.favorite_channels.sort()

    def remove_from_favorites(self):
        if self.current_channel in self.favorite_channels:
            self.favorite_channels.remove(self.current_channel)

    def jump_to_favorite(self):
        if self.favorite_channels:
            higher_favorites = [fav for fav in self.favorite_channels if fav > self.current_channel]

            if higher_favorites:
                next_higher_channel = min(higher_favorites)
            else:
                next_higher_channel = min(self.favorite_channels)

            self.change_channel(next_higher_channel)

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
            self.volume_text.setMessage(f"Volume: {'=' * self.volume}{'-' * (10 - self.volume)}")
        else:
            raise ValueError("Invalid volume")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
            self.volume_text.setMessage(f"Volume: {'=' * self.volume}{'-' * (10 - self.volume)}")

    def set_volume(self, value):
        if 0 <= value <= 10:
            self.volume = value
            self.volume_text.setMessage(f"Volume: {'=' * self.volume}{'-' * (10 - self.volume)}")

    def __str__(self):
        return f"Current Channel: {self.current_channel},\nFavorites: {self.favorite_channels}\n"


tv = Television()

tv.change_channel(5)
tv.add_to_favorites()
tv.change_channel(7)
tv.add_to_favorites()
tv.change_channel(2)
tv.add_to_favorites()
tv.jump_prev_channel()
tv.set_volume(8)

tv.call_favorite()
