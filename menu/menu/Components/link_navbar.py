import reflex as rx
from menu.styles.styles import Size as Size

def link_navbar(text: str, url: str,) -> rx.Component:
    return rx.link(
        rx.text(text),
        href=url,
        margin=Size.DEFAULT.value,

    )