from config_data import config

class Main_table_markup:
    def __init__(self):
        self.head_size = 80
        self.offset_size = {"x": 0, "dx": 60}
        self.place_size = {"x": 60, "dx": 60}
        self.name_size = {"x": 120, "dx": 350}
        self.tours_size = {"x": 470, "dx": 710}
        self.sum_size = {"x": 1180, "dx": 100}
        self.dy = (config.image_height - self.head_size) / config.NUMBER_OF_PLAYERS
        self.tours_dx = self.tours_size["dx"] / config.COUNT_TOUR_IN_TABLE


class Points_tour_markup:
    def __init__(self):
        self.place_size = {"x": 0, "dx": 150}
        self.name_size = {"x": 150, "dx": 930}
        self.points_size = {"x": 1080, "dx": 200}
        self.dy = 720 / (config.NUMBER_OF_PLAYERS + 1)


class Result_tour_markup:
    def __init__(self):
        self.head_size = 100
        self.total_size = 100
        self.dy = (config.image_height - self.head_size - self.total_size) / (config.COUNT_MATCHES_IN_TOUR + 1)
        self.match_size = {"x": 0, "dx": 640}
        self.result_size = {"x": 640, "dx": 230}
        self.forecast_size = {"x": 870, "dx": 230}
        self.points_size = {"x": 1100, "dx": 180}