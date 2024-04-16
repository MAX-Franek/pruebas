import reflex as rx

def header() -> rx.Component:
        return rx.vstack(
            rx.avatar(fallback="RX", size="5"),
            rx.text("@franparradev"),
            rx.text("""Soy ingeniero de software y actualmente trabajo como freelance full-stack developer iOS y Android.
                     Además, creo contenido formativo sobre programación en redes.
                     Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!""")
        )
