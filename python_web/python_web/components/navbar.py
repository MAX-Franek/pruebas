import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size
from python_web.styles.colors import color as color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.text("FranParra", color=color.PRIMARY.value),
            rx.text("Dev", color=color.SECONDARY.value),
            spacing="0",
            style=styles.navbar_title_style

        ),
        position="sticky",
        bg=color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    ) 