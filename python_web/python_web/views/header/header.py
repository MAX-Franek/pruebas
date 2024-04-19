import reflex as rx
from python_web.components.link_icon import link_icon
from python_web.styles.styles import Size as Size
from python_web.components.info_text import info_text
from python_web.styles.colors import TextColor as TextColor
from python_web.styles.fonts import Font, FontWeight
from python_web.styles.colors import color as color

def header() -> rx.Component:
        return rx.vstack(
                rx.hstack(
                    rx.avatar(
                            size="7",
                            src="avatar.jpg",
                            radius="full",
                            padding="2px"
                        ),
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "Fran Parra",
                                size="6",
                                color=TextColor.HEADER.value,
                                font_family=Font.TITLE.value,
                                font_weight= FontWeight.MEDIUM.value,
                            ),
                            rx.text(
                                "@franparradev",
                                color=color.PRIMARY.value
                            ),  
                            spacing="0"  
                        ),
                        
                            rx.hstack(
                                link_icon("https://instagram.com/","instagram"),
                                link_icon("https://instagram.com/","youtube"),
                                link_icon("https://instagram.com/","instagram"),
                                color=TextColor.BODY.value                                    
                            ),
                    ),
                    spacing="5"                 
                ),

            rx.flex(
                    info_text("+13","años de experiencia"),
                    rx.spacer(),
                    info_text("+13","años de experiencia"),
                    rx.spacer(),
                    info_text("+13","años de experiencia"),
                    width="100%",
            ),
            rx.text("""Soy ingeniero de software y actualmente trabajo como freelance full-stack developer iOS y Android.
                     Además, creo contenido formativo sobre programación en redes.
                     Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!""",
                    color=TextColor.BODY.value,
                    font_size="0.9EM"
            ),
            spacing="6",
            align_items="start"
        )
