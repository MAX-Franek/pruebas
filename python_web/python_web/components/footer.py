import reflex as rx
import datetime
from python_web.styles.styles import Size as Size
from python_web.styles.colors import TextColor as Textcolor

def footer() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.image(
                src="logo.png",
                height=Size.VERYBIG.value
            ),
            width="100%"
        ),
        rx.center(
            rx.link(
            f"2014-{datetime.date.today().year} MoureDev by Brais Moure v4.",
            href="https://moureDev.com",
            is_external=True,
        ),
        width="100%"
        ),
        rx.text(
            "BUILDING SOFTWARE WITH FROM GALICIA TO THE WORLD.",
            font_size=Size.MEDIUM.value
            ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color = Textcolor.FOOTER.value,
    )