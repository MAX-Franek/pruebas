from enum import Enum
import reflex as rx
from .colors import color as color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#Constants
MAX_WIDTH = "600px"

#Sizes  
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERYBIG = "4em"

#Styles

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color" : color.BACKGROUND.value,
    rx.button: {
        "width" : "100%",
        "height" : "100%",
        "display" : "block",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color" : color.CONTENT.value,
        "_hover" : {
            "background_color" : color.SECONDARY.value,
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover" : {}
    }
}
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
    font_family=Font.TITLE.value,
    color = TextColor.HEADER.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_family=Font.TITLE.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color = TextColor.BODY.value
)