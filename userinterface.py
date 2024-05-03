import flet as ft
from router import views_handler


def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        page.views.append(views_handler(page)[page.route])

    page.on_route_change = route_change

    page.go('/login')


if __name__ == '__main__':
    ft.app(target=main)
