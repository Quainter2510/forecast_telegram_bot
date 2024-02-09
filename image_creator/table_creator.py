from PIL import Image, ImageDraw, ImageFont
from config_data import config


def main_table(table, tour):
    img = Image.open("images/table_templates/template_main_table.png")
    imdraw = ImageDraw.Draw(img)
    dx = [44, 336, 395, 452, 510, 568, 626, 682, 739, 799, 855, 913, 970, 1031, 1090, 1146, 1205, 1280]
    font = ImageFont.truetype("images/Fonts/consolas.ttf", size=28)
    for i in range(14):
        for j in range(len(table[0])):
            if j < tour or j == len(table[0]) - 1:
                msg = str(table[i][j]) 
            else:
                msg = "-"
            _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
            imdraw.text((dx[j] + (dx[j + 1] - dx[j] - w) // 2, 70 + 46.5 * i + (46.5 - h) // 2), msg, font=font)
    img.save("images/ready_tables/main_table.png")


def result_tour(res, tour, points, nickname=""):
    img = Image.open("images/table_templates/template_result_tour.png")
    imdraw = ImageDraw.Draw(img)
    
    dx = [0, 625, 883, 1110, 1280]
    if nickname == "":
        font = ImageFont.truetype("Fonts/consolas.ttf", size=54)
        msg = f'Итог {tour}'
    else:
        font = ImageFont.truetype("Fonts/consolas.ttf", size=42)
        msg = f'Прогноз {tour} от {nickname}'
    _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
    imdraw.text(((1280 - w) // 2, (65 - h) // 2), msg, font=font, fill=(0, 0, 0), stroke_width=1)
    msg = f'{points}'
    font = ImageFont.truetype("Fonts/BRITANIC.TTF", size=52)
    _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
    imdraw.text((1110 + (170 - w) // 2, 650 + (65 - h) // 2), msg, font=font)
    font = ImageFont.truetype("Fonts/consolas.ttf", size=40)
    for i in range(8):
        for j in range(4):
            msg = str(res[i][j])
            _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
            imdraw.text((dx[j] + (dx[j + 1] - dx[j] - w) // 2, 140 + 65 * i + (65 - h) // 2), msg,
                        font=font)
    img.save("images/ready_tables/result_tour.png")


def points_tour(data, tour):
    img = Image.open("images/table_templates/template_points_tour.png")
    imdraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Fonts/consolas.ttf", size=50)
    dx = [115, 1092, 1280]
    font = ImageFont.truetype("Fonts/consolas.ttf", size=30)
    for i in range(14):
        for j in range(2):
            msg = str(data[i][j])
            _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
            imdraw.text((dx[j] + (dx[j + 1] - dx[j] - w) // 2, 50 + 48 * i + (48 - h) // 2), msg,
                        font=font)
    img.save("images/ready_tables/points_tour.png")