import reflex as rx
import python_web.styles.styles as styles

def link_buttons(title: str, body: str, url: str, tag: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=tag,
                    width = styles.Size.LARGE.value,
                    heigth = styles.Size.LARGE.value,
                    margin = styles.Size.MEDIUM.value,

                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing = "0"
                )

            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )