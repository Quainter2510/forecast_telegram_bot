from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from image_creator.markup_table import Main_table_markup, Result_tour_markup, Points_tour_markup
from config_data import config


dark_factor = 0.1
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
    mk = Points_tour_markup()
    img = Image.open("images/table_templates/dark_background.png")
    imdraw = ImageDraw.Draw(img)
    imdraw.line((mk.name_size["x"], 0, mk.name_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((mk.points_size["x"], 0, mk.points_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((0, mk.dy, config.image_width, mk.dy), fill="white", width=wide_line)

    for i in range(1, config.NUMBER_OF_PLAYERS + 1):
        imdraw.line((0, mk.dy * i, config.image_width, mk.dy * i), fill="white", width=thin_line)
        drawtext(imdraw, mk.place_size["x"], mk.dy * i, mk.place_size["dx"], mk.dy, str(i))

    drawtext(imdraw, mk.place_size["x"], 0, mk.place_size["dx"], mk.dy, "Место")
    drawtext(imdraw, mk.name_size["x"], 0, mk.name_size["dx"], mk.dy, "Имя")
    drawtext(imdraw, mk.points_size["x"], 0, mk.points_size["dx"], mk.dy, "Очки")

    # img.show()
    img.save("images/table_templates/template_points_tour.png", "png")

def create_template_result_tour():
    mk = Result_tour_markup()
    img = Image.open("images/table_templates/dark_background.png")
    imdraw = ImageDraw.Draw(img)
    imdraw.line((0, mk.head_size, config.image_width, mk.head_size), fill="white", width=wide_line)    
    imdraw.line((0, config.image_height - mk.head_size, config.image_width, config.image_height - mk.head_size), fill="white", width=wide_line) 
    imdraw.line((0, mk.head_size + mk.dy, config.image_width, mk.head_size + mk.dy), fill="white", width=wide_line)  

    for i in range(1, config.COUNT_MATCHES_IN_TOUR + 1):
        imdraw.line((0, mk.head_size +mk.dy * i, config.image_width, mk.head_size + mk.dy * i), fill="white", width=thin_line)  

    imdraw.line((mk.result_size["x"], mk.head_size, mk.result_size["x"], config.image_height - mk.total_size), fill="white", width=wide_line) 
    imdraw.line((mk.forecast_size["x"], mk.head_size, mk.forecast_size["x"], config.image_height - mk.total_size), fill="white", width=wide_line) 
    imdraw.line((mk.points_size["x"], mk.head_size, mk.points_size["x"], config.image_height), fill="white", width=wide_line) 

    drawtext(imdraw, mk.match_size["x"], mk.head_size, mk.match_size["dx"], mk.dy, "Матч")
    drawtext(imdraw, mk.result_size["x"], mk.head_size, mk.result_size["dx"], mk.dy, "Результат")
    drawtext(imdraw, mk.forecast_size["x"], mk.head_size, mk.forecast_size["dx"], mk.dy, "Прогноз")
    drawtext(imdraw, mk.points_size["x"], mk.head_size, mk.points_size["dx"], mk.dy, "Очки")
    drawtext(imdraw, mk.match_size["x"], config.image_height - mk.total_size, mk.points_size["x"], mk.total_size, "Итог за тур")

    # img.show()
    img.save("images/table_templates/template_result_tour.png", "png")

def craete_template_main_table():
    mk = Main_table_markup()

    img = Image.open("images/table_templates/dark_background.png")
    imdraw = ImageDraw.Draw(img)
    imdraw.line((0, mk.head_size, config.image_width, mk.head_size), fill="white", width=wide_line)
    imdraw.line((mk.place_size["x"], 0, mk.place_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((mk.name_size["x"], 0, mk.name_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((mk.tours_size["x"], 0, mk.tours_size["x"], config.image_height), fill="white", width=wide_line)
    imdraw.line((mk.sum_size["x"], 0, mk.sum_size["x"], config.image_height), fill="white", width=wide_line)

    for i in range(1, config.NUMBER_OF_PLAYERS + 1):
        imdraw.line((0, mk.head_size + mk.dy * i, config.image_width, mk.head_size + mk.dy * i), fill="white", width=thin_line)
        drawtext(imdraw, mk.place_size["x"], mk.head_size + mk.dy * (i - 1), mk.place_size["dx"], mk.dy, str(i))

    tours_dx = mk.tours_size["dx"] / config.NUMBER_OF_TOUR

    for i in range(1, config.NUMBER_OF_TOUR + 1):
        imdraw.line((mk.tours_size["x"] + tours_dx * i, 0, mk.tours_size["x"] + tours_dx * i, config.image_height))
        drawtext(imdraw, mk.tours_size["x"] + tours_dx * (i - 1), 0, tours_dx, mk.head_size, "День\n" + str(i))

    drawtext(imdraw, mk.place_size["x"], 0, mk.place_size["dx"], mk.head_size, "№")
    drawtext(imdraw, mk.name_size["x"], 0, mk.name_size["dx"], mk.head_size, "Имя")
    drawtext(imdraw, mk.sum_size["x"], 0, mk.sum_size["dx"], mk.head_size, "Итог")
    # drawtext(imdraw, mk.offset_size["x"], 0, mk.offset_size["dx"], mk.head_size, "+/-")

    # img.show()
    img.save("images/table_templates/template_main_table.png", "png")




create_background()
create_template_points_tour()
create_template_result_tour()
craete_template_main_table()
