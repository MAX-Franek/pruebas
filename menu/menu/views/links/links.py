import reflex as rx
from menu.Components.link_navbar import link_navbar
from menu.styles.colors import color

def links() -> rx.Component:
    return rx.hstack(
        link_navbar(
            "Inicio",
            ".."
        ),
                link_navbar(
            "Calendario",
            "calendario"
        ),
                link_navbar(
            "Prueba",
            "prueba"
        ),
                link_navbar(
            "Hola",
            "https://google.com/"
        ),
        background_color=color.CONTENT.value,
        width="100%"
    )
