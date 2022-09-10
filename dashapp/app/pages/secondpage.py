import dash
from dash import html, dcc

from utilities.app_cards import (
    mini_card,
    content_card
)

second_content = content_card(
    id="second_card",
    title="my second card",
    content=dcc.Loading(id="second_loading")
)

other_content=content_card(
    id="other_card",
    title="other card",
    content=[
        html.Div(
            children=[
                mini_card(text="1. try", a_function=dcc.Input(id="a_input", value="10", type="number", placeholder="", style={"width": "100px"})),
                mini_card(text="2. try", a_function=dcc.Input(id="b_input", value="10", type="number", min=5, max=15, placeholder="", style={"width": "100px"})),
            ],
            style={"display": "flex"}
        )
    ]
)

one_more = mini_card(text="3. try", a_function=dcc.Input(id="c_input", value="10", type="number", placeholder="", style={"width": "100px"}))

dash.register_page(__name__,)


# dash.register_page(
#     __name__,
#     path='/second',
#     title='Home Dashboard',
#     name='Home Dashboard'
# )


layout = html.Div(children=[

    second_content,
    other_content,
    one_more,


    html.H1(children='This is our second page'),

    html.Div(children='''
        This is our second page content.
        '''),
    ],
)
