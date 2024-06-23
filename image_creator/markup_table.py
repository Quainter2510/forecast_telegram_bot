from config_data import config

class Main_table_markup:
    def __init__(self):
        self.head_size = 80
        self.offset_size = {"x": 0, "dx": 0}
        self.place_size = {"x": 0, "dx": 80}
        self.name_size = {"x": 80, "dx": 540}
        self.tours_size = {"x": 620, "dx": 1180}
        self.sum_size = {"x": 1800, "dx": 120}
        self.dy = (config.image_height - self.head_size) / config.NUMBER_OF_PLAYERS
        self.tours_dx = self.tours_size["dx"] / config.COUNT_TOUR_IN_TABLE


class Points_tour_markup:
    def __init__(self):
        self.place_size = {"x": 0, "dx": 150}
        self.name_size = {"x": 150, "dx": 1570}
        self.points_size = {"x": 1720, "dx": 200}
        self.dy = config.image_height / (config.NUMBER_OF_PLAYERS + 1)


class Result_tour_markup:
    def __init__(self):
        self.head_size = 150
        self.total_size = 150
        self.dy = (1080 - self.head_size - self.total_size) / (config.COUNT_MATCHES_IN_TOUR + 1)
        self.match_size = {"x": 0, "dx": 900}
        self.result_size = {"x": 900, "dx": 400}
        self.forecast_size = {"x": 1300, "dx": 400}
        self.points_size = {"x": 1700, "dx": 220}