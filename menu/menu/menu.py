import reflex as rx
from menu.views.links.links import links
import menu.styles.styles as styles
from menu.views.horario import horario
from menu.views.calendar_view import calendar_view
from menu.views.pruebas import boton

def index() -> rx.Component:
    return rx.vstack(
        links(),
        horario(),
    )


def calendario() -> rx.Component:
    return rx.vstack(
        links(),
        calendar_view(),
        
    )
    
def prueba() -> rx.Component:
    return rx.vstack(
        links(),
        boton()
        
    )


app = rx.App(
    style=styles.BASE_STYLE,
)
app.add_page(index)
app.add_page(calendario)
app.add_page(prueba)
