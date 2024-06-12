from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from config_data import config


dark_factor = 0.2
wide_line = 5
thin_line = 1

def drawtext(imdraw, x, y, dx, dy, text, font_size=34):
    font = ImageFont.truetype("images/Fonts/consolas.ttf", size=font_size)
    _, _, w, h = imdraw.textbbox((0, 0), text, font = font)
    text_x = (dx - w) // 2 + x
    text_y = (dy - h) // 2 + y
    imdraw.multiline_text((text_x, text_y), text, font=font, align="center")

def create_background():
    im = Image.open('images/table_templates/background.jpg')
    im = im.resize((config.image_width, config.image_height))

    img = ImageEnhance.Brightness(im).enhance(dark_factor)
    img.save("images/table_templates/dark_background.png", "png")

def create_template_points_tour():
    place_size = {"x": 0, "dx": 150}
    name_size = {"x": 150, "dx": 930}
    points_size = {"x": 1080, "dx": 200}
    dy = config.image_height / (config.NUMBER_OF_PLAYERS + 1)
    img = Image.open("images/table_templates/dark_background.png")
    imdraw = ImageDraw.Draw(img)
    imdraw.line((name_size["x"], 0, name_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((points_size["x"], 0, points_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((0, dy, config.image_width, dy), fill="white", width=wide_line)

    for i in range(1, config.NUMBER_OF_PLAYERS + 1):
        imdraw.line((0, dy * i, config.image_width, dy * i), fill="white", width=thin_line)
        drawtext(imdraw, place_size["x"], dy * i, place_size["dx"], dy, str(i))

    drawtext(imdraw, place_size["x"], 0, place_size["dx"], dy, "Место")
    drawtext(imdraw, name_size["x"], 0, name_size["dx"], dy, "Имя")
    drawtext(imdraw, points_size["x"], 0, points_size["dx"], dy, "Очки")

    # img.show()
    img.save("images/table_templates/template_points_tour.png", "png")

def create_template_result_tour():
    head_size = 100
    total_size = 100
    dy = (config.image_height - head_size - total_size) / (config.COUNT_MATCHES_IN_TOUR + 1)
    match_size = {"x": 0, "dx": 640}
    result_size = {"x": 640, "dx": 230}
    forecast_size = {"x": 870, "dx": 230}
    points_size = {"x": 1100, "dx": 180}
    img = Image.open("images/table_templates/dark_background.png")
    imdraw = ImageDraw.Draw(img)
    imdraw.line((0, head_size, config.image_width, head_size), fill="white", width=wide_line)    
    imdraw.line((0, config.image_height - head_size, config.image_width, config.image_height - head_size), fill="white", width=wide_line) 
    imdraw.line((0, head_size + dy, config.image_width, head_size + dy), fill="white", width=wide_line)  

    for i in range(1, config.COUNT_MATCHES_IN_TOUR + 1):
        imdraw.line((0, head_size + dy * i, config.image_width, head_size + dy * i), fill="white", width=thin_line)  

    imdraw.line((result_size["x"], head_size, result_size["x"], config.image_height - total_size), fill="white", width=wide_line) 
    imdraw.line((forecast_size["x"], head_size, forecast_size["x"], config.image_height - total_size), fill="white", width=wide_line) 
    imdraw.line((points_size["x"], head_size, points_size["x"], config.image_height), fill="white", width=wide_line) 

    drawtext(imdraw, match_size["x"], head_size, match_size["dx"], dy, "Матч")
    drawtext(imdraw, result_size["x"], head_size, result_size["dx"], dy, "Результат")
    drawtext(imdraw, forecast_size["x"], head_size, forecast_size["dx"], dy, "Прогноз")
    drawtext(imdraw, points_size["x"], head_size, points_size["dx"], dy, "Очки")
    drawtext(imdraw, match_size["x"], config.image_height - total_size, points_size["x"], total_size, "Итог за тур")

    # img.show()
    img.save("images/table_templates/template_result_tour.png", "png")

def craete_template_main_table():
    head_size = 80
    offset_size = {"x": 0, "dx": 60}
    place_size = {"x": 60, "dx": 60}
    name_size = {"x": 120, "dx": 350}
    tours_size = {"x": 470, "dx": 710}
    sum_size = {"x": 1180, "dx": 100}
    dy = (config.image_height - head_size) / config.NUMBER_OF_PLAYERS

    img = Image.open("images/table_templates/dark_background.png")
    imdraw = ImageDraw.Draw(img)
    imdraw.line((0, head_size, config.image_width, head_size), fill="white", width=wide_line)
    imdraw.line((place_size["x"], 0, place_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((name_size["x"], 0, name_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((tours_size["x"], 0, tours_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((sum_size["x"], 0, sum_size["x"], config.image_height), fill="white", width=wide_line)

    for i in range(1, config.NUMBER_OF_PLAYERS + 1):
        imdraw.line((0, head_size + dy * i, config.image_width, head_size + dy * i), fill="white", width=thin_line)
        drawtext(imdraw, place_size["x"], head_size + dy * (i - 1), place_size["dx"], dy, str(i))

    tours_dx = tours_size["dx"] / config.NUMBER_OF_TOUR

    for i in range(1, config.NUMBER_OF_TOUR + 1):
        imdraw.line((tours_size["x"] + tours_dx * i, 0, tours_size["x"] + tours_dx * i, config.image_height))
        drawtext(imdraw, tours_size["x"] + tours_dx * (i - 1), 0, tours_dx, head_size, "Тур\n" + str(i))

    drawtext(imdraw, place_size["x"], 0, place_size["dx"], head_size, "№")
    drawtext(imdraw, name_size["x"], 0, name_size["dx"], head_size, "Имя")
    drawtext(imdraw, sum_size["x"], 0, sum_size["dx"], head_size, "Итог")
    drawtext(imdraw, offset_size["x"], 0, offset_size["dx"], head_size, "+/-")

    # img.show()
    img.save("images/table_templates/template_main_table.png", "png")




create_background()
create_template_points_tour()
create_template_result_tour()
craete_template_main_table()
