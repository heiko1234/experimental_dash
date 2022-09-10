

from dash import Dash, html, dcc
import base64

import dash

# from app.pages.landing.main import landing_page


# session store
a_session_store = dcc.Store(
    id = "a_session_store", storage_type="session"
)


app = Dash(__name__, use_pages=True)


img_path = str("./dashapp/app/assets/arrow_growth.png")
encoded_img = base64.b64encode(open(img_path, "rb").read())


sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("Sidebar", style={"color": "black"}),
            ],
            className="sidebar-header",
            ),
        html.Div(
            dcc.Link('1st', href=dash.page_registry['pages.home']['path'])
            # dcc.Link('personas', href="./home")
            ),
        html.Div(
            dcc.Link('2nd', href=dash.page_registry['pages.secondpage']['path'])
            ),
        # html.Div([
        #     html.Img(src='data:image/png;base64,{}'.format(encoded_img.decode())
        #     ),
        #     html.Span("growth")
        #     ], style={"display": "flex", "height": "30px", "width": "30px", "background": "black"}
        # ),
        dcc.Link(className="nav_link",
            children=[
            html.Img(src='data:image/png;base64,{}'.format(encoded_img.decode()),
            style={"display": "flex", "height": "50px", "width": "50px", "background": "black"}
            ),
            html.Span("growth")
            ], 
            href=dash.page_registry['pages.secondpage']['path'],
            style={"display": "flex"}
        ),
    ],
    className="sidebar"
)


app.layout = html.Div(
    [
        sidebar,
        html.Div(
            [
                dash.page_container
            ],
            className="content",
        ),
    ]
)




# app.layout = html.Div([
# 	html.H1('Multi-page app with Dash Pages'),

#     html.Div(
#         [
#             html.Div(
#                 dcc.Link(
#                     f"{page['name']} - {page['path']}", href=page["relative_path"]    # {page['relative_path']}
#                     )
#                 )
#                 for page in dash.page_registry.values()
#         ]
#     ),

# 	dash.page_container
# ])


# if __name__ == "__main__":
#     app.run_server(port=8050, debug=True)



