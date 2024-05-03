from __future__ import annotations

from fastui import AnyComponent
from fastui import components as c
from fastui.events import BackEvent, GoToEvent

SIGNUP_BUTTON = c.Button(text="SignUp", on_click=GoToEvent(url="/signup"))
PROFILE_BUTTON = c.Button(text="Profile", on_click=GoToEvent(url="/profile"))


def home_page() -> list[c.Div]:
    """
    Home page of the app.
    """
    return [
        c.Div(
            components=[
                c.Button(text="Create", on_click=GoToEvent(url="/create")),
            ],
            class_name="border-top mt-3 pt-1",
        ),
    ]


def get_navbar(user: str | None = None) -> c.Navbar:
    """
    Get navbar with correct user profile link.
    """
    return c.Navbar(
        start_links=[
            c.Link(
                components=[c.Button(text="Back")],
                on_click=BackEvent(),
            ),
            c.Link(
                components=[c.Heading(text="Dairy", level=2)],
            ),
            c.Link(
                components=[
                    c.Image(
                        src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png",
                        width="40px",
                        height="40px",
                    ),
                ],
                on_click=GoToEvent(url="https://github.com/SaraFarron"),
            ),
            c.Link(
                components=[PROFILE_BUTTON if user else SIGNUP_BUTTON],
            ),
        ],
    )


def dairy_page(components: list[AnyComponent], title: str | None = None, user: str | None = None) -> list[AnyComponent]:
    """
    Base page for the app.

    Includes title, navbar and footer.
    """
    return [
        c.PageTitle(text=f"Dairy - {title}" if title else "Dairy"),
        get_navbar(user),
        c.Page(
            components=components,
        ),
        c.Footer(
            extra_text="Made with ❤️ by Nikita",
            links=[
                c.Link(
                    components=[c.Text(text="Source code")],
                    on_click=GoToEvent(url="https://github.com/SaraFarron/dairy"),
                ),
            ],
        ),
    ]
