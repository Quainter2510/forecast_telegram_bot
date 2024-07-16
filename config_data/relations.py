from config_data.config import NUMBER_OF_TOUR

TOUR_DCT = {i: f"tour{i}" for i in range(1, NUMBER_OF_TOUR + 1)}

DATES_DCT = {f"tour{i}": i for i in range(1, NUMBER_OF_TOUR + 1)}

HUMAN_DCT = {f"{i} тур": i for i in range(1, NUMBER_OF_TOUR + 1)}

