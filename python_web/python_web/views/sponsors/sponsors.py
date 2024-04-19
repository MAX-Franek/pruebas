import reflex as rx
from python_web.components.title import title
from python_web.components.link_sponsor import link_sponsor

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor(
                "Elgato.png",
                "https://www.elgato.com/es/es"
            ),
            link_sponsor(
                "mvp.png",
                "https://www.elgato.com/es/es"
            ),
            spacing="4"
        ),
        width="100%",
        spacing="4"
    )