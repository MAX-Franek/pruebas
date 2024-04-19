import reflex as rx
from menu.Components.tabla import tabla

def horario() ->rx.Component:
    return rx.vstack(
        tabla("Planas","manolo")
        
    )