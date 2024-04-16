import reflex as rx
from python_web.components.link_buttons import link_buttons

def links() -> rx.Component:
    return rx.vstack(
        link_buttons("Twitch","https://www.twitch.tv/"),
        link_buttons("Youtube","https://www.youtube.es/"),
        link_buttons("Youtube(canal secundario)","https://www.youtube.es/"),
        link_buttons("instagram","https://www.instagram.com/")
    )