import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_3_layout = html.Div([
    html.H1('Page 3'),
    html.Div([
        html.Div([
            html.H6('How much do you like Python? (-10 to 10)'),
            dcc.Slider(
                id='page-3-slider',
                min=-10,
                max=10,
                step=0.5,
                marks={i:str(i) for i in range(-10, 11)},
                value=0,
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-3-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
