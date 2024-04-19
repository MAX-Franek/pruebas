import reflex as rx
from python_web.styles.styles import Size as Size
from python_web.styles.colors import TextColor as Textcolor
from python_web.styles.colors import color as color

def info_text(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            title,
            font_weight="bold",
            color=color.PRIMARY.value
        ),
        body, 
        font_size=Size.MEDIUM.value,
        color=Textcolor.BODY.value,
    )