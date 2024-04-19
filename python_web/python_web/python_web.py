import reflex as rx
from python_web.components.navbar import navbar
from python_web.views.header.header import header
from python_web.views.links.links import links
from python_web.components.footer import footer
from python_web.views.sponsors.sponsors import sponsors
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
            navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
        )
        
        ),
    rx.center(footer())
    )


app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS
)
app.add_page(
    index,
    title="FranParraDev"
)
