import reflex as rx


def index() -> rx.Component:
    return rx.container(
        rx.center(
            rx.text("probando")
        )
    )


app = rx.App()
app.add_page(index)
