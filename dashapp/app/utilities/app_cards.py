

from dash import html, dcc


def content_card(
    id,
    title,
    content
):
    header = html.Div(
        className="content_header",
        children=[
            html.Div(
                title,
                style = {
                    "front-size": 15,
                    "font-wight": "bond",
                    "color": "#004A96"
                }
            )
        ],
        style={"display": "flex"}
    )
    card = html.Div(
        id=id,
        children=[header, *content],
        style={
            "box-shadow": "rgba(99, 99, 99, 0.2) 0px 2px 8px 0px",
            #"box-shadow": "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px",
            "padding": "10px",
            "height": "500px",
            "width": "500px"
        }
    )

    return card



def mini_card(text, a_function):
    output = html.Div(
        className="mini_card_class",
        children=[
            html.Span(text),
            html.H3(""),
            a_function
        ],
        style = {
            "box-shadow": "rgba(99, 99, 99, 0.2) 0px 2px 8px 0px",
            "padding": "10px",
            "height": "70px",
            "width": "150px"
        }
    )
    return output


