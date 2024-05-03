import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, TextField
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment


def main(page: Page) -> None:
    page.title = 'Movie Rental'

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        #Login
        page.views.append(
            View(
                route='/login',
                controls=[

                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
        #Signup
        if page.route == '/signup':
            page.views.append(
                View(
                    route='/signup',
                    controls=[

                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )

        # Home
        if page.route == '/home':
            page.views.append(
                View(
                    route='/home',
                    controls=[
                        AppBar(title=Text('Home'), bgcolor='blue'),
                        Text(value='Home', size=30),
                        ElevatedButton(text='Go to store', on_click=lambda _: page.go('/store'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )

        # Store
        if page.route == '/store':
            page.views.append(
                View(
                    route='/store',
                    controls=[
                        AppBar(title=Text('Store'), bgcolor='blue'),
                        Text(value='Store', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/home'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )

        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)
