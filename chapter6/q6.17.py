class Television:
    def __init__(self, current_channel=1):
        self.current_channel = current_channel
        self.prev_channel = None
        self.favorite_channels = []

    def change_channel(self, new_channel):
        self.prev_channel = self.current_channel
        self.current_channel = new_channel

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

    def __str__(self):
        return f"Current Channel: {self.current_channel},\nFavorites: {self.favorite_channels}\n"


tv = Television()
tv.change_channel(5)
tv.add_to_favorites()

tv.change_channel(8)
tv.add_to_favorites()

tv.change_channel(15)
tv.add_to_favorites()
print(tv)

tv.change_channel(8)
tv.remove_from_favorites()
print(tv)
