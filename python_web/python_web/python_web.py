import reflex as rx
from python_web.components.navbar import navbar
from python_web.views.header.header import header
from python_web.views.links.links import links
from python_web.components.footer import footer


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
            navbar(),
        rx.vstack(
        header(),
        links()
        ),
    footer()
    )


app = rx.App()
app.add_page(index)
app.compile()