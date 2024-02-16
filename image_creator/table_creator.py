from PIL import Image, ImageDraw, ImageFont
from config_data import config
from image_creator.markup_table import Main_table_markup, Result_tour_markup, Points_tour_markup


def drawtext(imdraw, x, y, dx, dy, text):
    font = ImageFont.truetype("images/Fonts/consolas.ttf", size=32)
    _, _, w, h = imdraw.textbbox((0, 0), text, font = font)
    text_x = (dx - w) // 2 + x
    text_y = (dy - h) // 2 + y
    imdraw.multiline_text((text_x, text_y), text, font=font, align="center")

def main_table(table, tour):
    img = Image.open("images/table_templates/template_main_table.png")
    imdraw = ImageDraw.Draw(img)

    mk = Main_table_markup()

    for i in range(config.NUMBER_OF_PLAYERS):
        drawtext(imdraw, mk.name_size["x"], mk.head_size + mk.dy * i, mk.name_size["dx"], mk.dy, str(table[i][0]))

        for j in range(config.COUNT_TOUR_IN_TABLE):
            if j < tour or j == len(table[0]) - 1:
                msg = str(table[i][j + 1])
            else:
                msg = "-"
            drawtext(imdraw, mk.tours_size["x"] + mk.tours_dx * j, mk.head_size + mk.dy * i, mk.tours_dx, mk.dy, msg)
        
        drawtext(imdraw, mk.sum_size["x"], mk.head_size + mk.dy * i, mk.sum_size["dx"], mk.dy, str(table[i][-1]))
    
    img.save("images/ready_tables/main_table.png")

def result_tour(data, tour, points, nickname=""):
    img = Image.open("images/table_templates/template_result_tour.png")
    imdraw = ImageDraw.Draw(img)

    mk = Result_tour_markup()

    if nickname == "":
        msg = f'Итог {tour}'
    else:
        msg = f'Прогноз {tour} от {nickname}'
    drawtext(imdraw, 0, 0, config.image_width, mk.head_size, msg)
    drawtext(imdraw, mk.points_size["x"], config.image_height - mk.total_size, mk.points_size["dx"], mk.total_size, str(points))
    for i, (match, res, forecast, pts) in enumerate(data, start=1):
        drawtext(imdraw, mk.match_size["x"], mk.head_size + mk.dy * i, mk.match_size["dx"], mk.dy, match)
        drawtext(imdraw, mk.result_size["x"], mk.head_size + mk.dy * i, mk.result_size["dx"], mk.dy, res)
        drawtext(imdraw, mk.forecast_size["x"], mk.head_size + mk.dy * i, mk.forecast_size["dx"], mk.dy, forecast)
        drawtext(imdraw, mk.points_size["x"], mk.head_size + mk.dy * i, mk.points_size["dx"], mk.dy, str(pts))
    img.save("images/ready_tables/result_tour.png")

def points_tour(data, tour):
    img = Image.open("images/table_templates/template_points_tour.png")
    imdraw = ImageDraw.Draw(img)

    mk = Points_tour_markup()

    for i, (name, pts) in enumerate(data):
        drawtext(imdraw, mk.name_size["x"], mk.dy * (i + 1), mk.name_size["dx"], mk.dy, name)
        drawtext(imdraw, mk.points_size["x"], mk.dy * (i + 1), mk.points_size["dx"], mk.dy, str(pts))
    img.save("images/ready_tables/points_tour.png")
        