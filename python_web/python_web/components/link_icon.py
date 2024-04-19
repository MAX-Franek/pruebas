import reflex as rx
import python_web.styles.styles as styles

def link_icon(url: str, tag: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=tag
        ),
        href= url,
        is_external=True
    )