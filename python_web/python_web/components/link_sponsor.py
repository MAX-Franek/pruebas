import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size

def link_sponsor(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            height=Size.VERYBIG.value,
            src=imagen,
            width="auto"
        ),
        href=url,
        is_external=True
    )