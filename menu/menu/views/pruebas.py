import reflex as rx
import calendar
from datetime import datetime, timedelta

tiempo= datetime.now()

hoy = datetime.now()
mes_actual = hoy.month
año_actual = hoy.year

_, dias_en_mes = calendar.monthrange(año_actual, mes_actual)

for dia in range(1, dias_en_mes + 1):
    fila = []
    for i in range(30):
        siguiente_dia = hoy + timedelta(days=i)
        if siguiente_dia.day <= dias_en_mes:
            fila.append(str(siguiente_dia.day))





def boton():
    return rx.vstack(
        rx.heading("title"),
        rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell(""),
            rx.table.column_header_cell(f"{fila[0]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[1]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[2]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[3]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[4]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[5]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[6]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[7]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[8]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[9]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[10]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[11]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[12]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[13]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[14]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[15]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[16]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[17]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[18]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[19]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[20]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[21]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[22]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[23]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[24]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[25]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[26]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[27]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[28]}",col_span="2"),
            rx.table.column_header_cell(f"{fila[29]}",col_span="2"),
            
        ),
        ),
            
        
        rx.table.body(
        rx.table.row(
            rx.table.row_header_cell(""),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
            rx.table.cell("Id"),
            rx.table.cell("Nombre"),
        ),
        ),
        size="3",
        variant="surface",
        ),
    )

