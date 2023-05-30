
class TV():
    vol = 15
    channel = 7

    def __init__(self, is_on: bool, tv):
        self.tv = tv
        is_on = False

    def tv_is_on (self, is_on: bool):
        is_on = True

    def change_channel(num, tv, is_on, channel = 7):
     if tv == is_on:
        channel += 1