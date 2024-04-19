import reflex as rx
from python_web.components.link_buttons import link_buttons
from python_web.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_buttons("Twitch",
                     "Directos todos los dias de la semana",
                     "https://www.twitch.tv/",
                     "twitch"
                ),
        link_buttons("Youtube",
                     "Videos todos los viernes sobre los directos",
                     "https://www.youtube.es/",
                     "youtube"
                ),
        link_buttons("Youtube(canal secundario)",
                     "Videos cada dos semanas",
                     "https://www.youtube.es/",
                     "youtube"
                ),
        link_buttons("Instagram",
                     "Publicacion cada semana",
                     "https://www.instagram.com/",
                     "twitch"
                ),
        title("Comunidad"),
        link_buttons("Twitch",
                     "Directos todos los dias de la semana",
                     "https://www.twitch.tv/",
                     "twitch"
                ),
        link_buttons("Youtube",
                     "Videos todos los viernes sobre los directos",
                     "https://www.youtube.es/",
                     "twitch"
                ),
        link_buttons("Youtube(canal secundario)",
                     "Videos cada dos semanas",
                     "https://www.youtube.es/",
                     "twitch"
                ),
        link_buttons("Instagram",
                     "Publicacion cada semana",
                     "https://www.instagram.com/",
                     "twitch"
                ),
        title("Contacto"),      
        link_buttons("MiPublicIndex",
                     "Respuesta rapida y con preferencia",
                     "https://www.youtube.es/",
                     "twitch"
                ),
        link_buttons("Email",
                     "Publicacion cada semana",
                     "https://www.instagram.com/",
                     "twitch"
                ),
        width = "100%",
        spacing="3"
    )