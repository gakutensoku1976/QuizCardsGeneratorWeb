import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter,ImageDraw,ImageFont

def wrap_text_japanese(text, font, max_width, draw):
    lines = []
    line = ""
    for char in text:
        test_line = line + char
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_width = bbox[2] - bbox[0]
        if line_width <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = char
    if line:
        lines.append(line)
    return lines


def draw_multiline(draw, text, font, area_top, area_height, x_margin, max_width, fill, outline_fill=None):
    line_spacing_ratio = 1.4
    lines = wrap_text_japanese(text, font, max_width, draw)
    base_line_height = font.getbbox("あ")[3]
    line_spacing = int(base_line_height * line_spacing_ratio)
    total_text_height = len(lines) * line_spacing
    y_start = area_top + (area_height - total_text_height) // 2

    for i, line in enumerate(lines):
        y = y_start + i * line_spacing
        x = x_margin
        if outline_fill:
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dx, dy in offsets:
                draw.text((x + dx, y + dy), line, font=font, fill=outline_fill)
        draw.text((x, y), line, font=font, fill=fill)


def create_image(title, question, answer, background_image, brightness, contrast, blur):
    # width = CONFIG["image"]["width"]
    # height = CONFIG["image"]["height"]
    # background_color = CONFIG["image"].get("background_color", "#000000")
    width = 1200
    height = 630
    title_size = 42
    question_size = 36
    answer_size = 36
    x_margin = 30
    background_color = "#000000"

    title_text_color = 'white'
    title_outline_color = 'black'

    question_text_color = 'white'
    question_outline_color = 'black'

    answer_text_color = 'yellow'
    answer_outline_color = 'black'

    background = background_image.convert("RGB").resize((width, height))

    if brightness != 1.0:
        background = ImageEnhance.Brightness(background).enhance(brightness)
    if contrast != 1.0:
        background = ImageEnhance.Contrast(background).enhance(contrast)
    if blur > 0:
        background = background.filter(ImageFilter.GaussianBlur(radius=blur))

    draw = ImageDraw.Draw(background)

    header_height = int(height * 0.05)
    title_height = int(height * 0.20)
    question_height = int(height * 0.50)
    answer_height = int(height * 0.20)

    font_path = 'ipaexg.ttf'

    font_title = ImageFont.truetype(font_path, title_size)
    font_question = ImageFont.truetype(font_path, question_size)
    font_answer = ImageFont.truetype(font_path, answer_size)

    max_text_width = width - x_margin * 2

    draw_multiline(draw, title, font_title, header_height, title_height, x_margin, max_text_width,
                   title_text_color, title_outline_color)
    draw_multiline(draw, question, font_question, header_height + title_height, question_height, x_margin, max_text_width,
                   question_text_color, question_outline_color)
    draw_multiline(draw, f"Ans. : {answer}", font_answer, header_height + title_height + question_height,
                   answer_height, x_margin, max_text_width, answer_text_color, answer_outline_color)

    return background


st.title("QuizCardGenerator")
image = Image.open("quiz_card.jpg")
# st.image(image, caption="Quiz Card Template", width=352)
st.image(image, caption="Quiz Card Template")

with st.form(key='quiz_form'):
    # st.subheader("Quiz Card Generator")
    # st.write("Please fill in the details below:")
    
    # Input fields for quiz card details
    title = st.text_input('タイトル')
    question = st.text_input('問題文') 
    answer = st.text_input('答え')

    brightness = st.slider('明るさ', 0.0, 2.0, 1.0, 0.1)
    contrast = st.slider('コントラスト', 0.0, 2.0, 1.0, 0.1)
    blur = st.slider('ぼかし', 0.0, 10.0, 0.0, 0.1)

    create_button = st.form_submit_button(label='Quiz Cardを作成')
    if create_button:
        output_image = create_image(title, question, answer, image, brightness, contrast, blur)
        # st.image(output_image, caption="Quiz Card Template", width=352)

        st.image(output_image, caption="Quiz Card")
        
