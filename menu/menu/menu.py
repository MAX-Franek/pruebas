import reflex as rx
from menu.views.links.links import links
import menu.styles.styles as styles
from menu.views.horario import horario

def index() -> rx.Component:
    return rx.vstack(
        links(),
        horario(),
    )



app = rx.App(
    style=styles.BASE_STYLE,
)
app.add_page(index)
