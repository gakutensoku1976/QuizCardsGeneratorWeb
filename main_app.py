import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import os

# フォントの表示名とファイル名の対応
FONT_OPTIONS = {
    "Noto Sans": "NotoSansJP-Regular.ttf",
    "BIZ UDP ゴシック": "BIZUDPGothic-Regular.ttf",
    "Kosugi Maru": "KosugiMaru-Regular.ttf",
}

# 各フォントのライセンス情報
FONT_LICENSE_URLS = {
    "Noto Sans": "https://fonts.google.com/noto/specimen/Noto+Sans+JP/license?lang=ja_Jpan",
    "BIZ UDP ゴシック": "https://fonts.google.com/specimen/BIZ+UDPGothic/license?query=BIZ+UDP&lang=ja_Jpan",
    "Kosugi Maru": "https://fonts.google.com/specimen/Kosugi+Maru/license?query=Kosugi+Maru&lang=ja_Jpan",
}


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


def draw_multiline(
    draw,
    text,
    font,
    area_top,
    area_height,
    x_margin,
    max_width,
    fill,
    outline_fill=None,
):
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
            offsets = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1),
            ]
            for dx, dy in offsets:
                draw.text((x + dx, y + dy), line, font=font, fill=outline_fill)
        draw.text((x, y), line, font=font, fill=fill)


def create_image(
    background_image,
    brightness,
    contrast,
    blur,
    title_text_color,
    title_outline_color,
    question_text_color,
    question_outline_color,
    answer_text_color,
    answer_outline_color,
    title_size,
    question_size,
    answer_size,
):
    width = 1200
    height = 630
    x_margin = 30

    background = background_image.convert("RGB").resize((width, height))

    if brightness != 1.0:
        background = ImageEnhance.Brightness(background).enhance(brightness)
    if contrast != 1.0:
        background = ImageEnhance.Contrast(background).enhance(contrast)
    if blur > 0:
        background = background.filter(ImageFilter.GaussianBlur(radius=blur))

    draw = ImageDraw.Draw(background)

    font_path = FONT_OPTIONS[st.session_state.selected_font_display_name]
    font_title = ImageFont.truetype(font_path, title_size)
    font_question = ImageFont.truetype(font_path, question_size)
    font_answer = ImageFont.truetype(font_path, answer_size)

    max_text_width = width - x_margin * 2

    header_height = int(height * 0.05)
    title_height = int(height * 0.20)
    question_height = int(height * 0.50)
    answer_height = int(height * 0.20)

    draw_multiline(
        draw,
        st.session_state.title,
        font_title,
        header_height,
        title_height,
        x_margin,
        max_text_width,
        title_text_color,
        title_outline_color,
    )
    draw_multiline(
        draw,
        st.session_state.question,
        font_question,
        header_height + title_height,
        question_height,
        x_margin,
        max_text_width,
        question_text_color,
        question_outline_color,
    )
    draw_multiline(
        draw,
        st.session_state.answer,
        font_answer,
        header_height + title_height + question_height,
        answer_height,
        x_margin,
        max_text_width,
        answer_text_color,
        answer_outline_color,
    )

    return background


# ------------------------------------------
# Streamlitアプリ本体
# ------------------------------------------

st.title("QuizCardGenerator")

if "background_image" not in st.session_state:
    st.session_state.background_image = None
if "selected_font_display_name" not in st.session_state:
    st.session_state.selected_font_display_name = list(FONT_OPTIONS.keys())[0]
if "title" not in st.session_state:
    st.session_state.title = "例題 1問目"
if "question" not in st.session_state:
    st.session_state.question = "明日の天気は何でしょう?"
if "answer" not in st.session_state:
    st.session_state.answer = "Ans. 晴れ時々曇り"

# 背景画像アップロード
st.sidebar.header("背景画像アップロード")
uploaded_file = st.sidebar.file_uploader(
    "背景画像を選択してください", type=["jpg", "jpeg", "png"]
)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.session_state.background_image = image

if st.session_state.background_image is None:
    st.warning("背景画像をアップロードしてください。")
    st.stop()

left, center, right = st.columns([1, 2, 1])
with center:
    st.image(st.session_state.background_image, caption="背景画像", width=352)


# クイズ内容入力
st.sidebar.header("クイズ内容入力")
title_input = st.sidebar.text_input("タイトル", value=st.session_state.title)
question_input = st.sidebar.text_input("問題文", value=st.session_state.question)
answer_input = st.sidebar.text_input("答え", value=st.session_state.answer)

if st.sidebar.button("テキストを反映して再描画"):
    st.session_state.title = title_input
    st.session_state.question = question_input
    st.session_state.answer = answer_input


# フォント選択とライセンスリンク
st.sidebar.header("フォント選択")
selected_font_display_name = st.sidebar.selectbox(
    "フォントを選択してください",
    options=list(FONT_OPTIONS.keys()),
    index=list(FONT_OPTIONS.keys()).index(st.session_state.selected_font_display_name),
    key="font_dropdown",
)
st.session_state.selected_font_display_name = selected_font_display_name

# ライセンスリンクを下に表示
license_url = FONT_LICENSE_URLS[selected_font_display_name]
st.sidebar.markdown(
    f'<a href="{license_url}" target="_blank">🔗 このフォントのライセンスを見る</a>',
    unsafe_allow_html=True,
)

# フォントサイズ設定
st.sidebar.header("フォントサイズ設定")
title_size = st.sidebar.slider("タイトル", 10, 100, 42)
question_size = st.sidebar.slider("問題文", 10, 100, 36)
answer_size = st.sidebar.slider("答え", 10, 100, 36)

# 色設定
st.sidebar.header("文字色・縁取り色設定")
col1, col2 = st.sidebar.columns(2)
with col1:
    title_text_color = st.color_picker("タイトル文字色", "#FFFFFF")
with col2:
    title_outline_color = st.color_picker("タイトル縁取り色", "#000000")
with col1:
    question_text_color = st.color_picker("問題文文字色", "#FFFFFF")
with col2:
    question_outline_color = st.color_picker("問題文縁取り色", "#000000")
with col1:
    answer_text_color = st.color_picker("答え文字色", "#FFFF00")
with col2:
    answer_outline_color = st.color_picker("答え縁取り色", "#000000")

# 画像調整
st.sidebar.header("画像調整")
brightness = st.sidebar.slider("明るさ", 0.0, 2.0, 1.0, 0.05)
contrast = st.sidebar.slider("コントラスト", 0.0, 2.0, 1.0, 0.05)
blur = st.sidebar.slider("ぼかし", 0.0, 32.0, 0.0, 1.0)

# 出力画像作成と表示
output_image = create_image(
    st.session_state.background_image,
    brightness,
    contrast,
    blur,
    title_text_color,
    title_outline_color,
    question_text_color,
    question_outline_color,
    answer_text_color,
    answer_outline_color,
    title_size,
    question_size,
    answer_size,
)
st.image(output_image, caption="Quiz Card")
