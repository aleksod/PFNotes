class TV():
    """
    brand            - str holding the brand of the television ('Sony', 'LG', etc.)
    on_status        - bool holding whether or not the television is on. This should default to False (e.g. off).
    current_channel  - int holding the current channel number. If the television is off, then the current_channel should be 0. Given that on_status defaults to off, what does that mean the current_channel should default to?
    life_perc        - float holding the percentage of life left in the TV. This should start out at 100% (i.e. default to 100).
    """
    def __init__(self, brand, on_status = False, current_channel = 0, life_perc = 100):
        self.brand = brand
        self.on_status = on_status
        self.current_channel = current_channel
        if self.on_status == True:
            self.current_channel = 1
        self.life_perc = life_perc

    def hit_power(self):
        self.on_status = not self.on_status
        if self.on_status == False:
            self.current_channel = 0
            self.life_perc -= 0.01

    def change_channel(self, channel):
        if self.on_status == False:
            print "Television is not on!"
        else:
            self.current_channel = channel
