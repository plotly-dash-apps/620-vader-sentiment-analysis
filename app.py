import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



##### Define button style
red_button_style = {'background-color': 'red',
                    'color': 'white',
                    'height': '50px',
                    'width': '100px',
                    'margin-top': '50px',
                    'margin-left': '50px'}


########### Define your variables ######

myheading1='Vader Sentiment Analysis'
initial_value='You have controlled your fear. Now, release your anger. Only your hatred can destroy me.'
tabtitle = 'Vader'
sourceurl = 'https://pypi.org/project/vaderSentiment/'
githublink = 'https://github.com/plotly-dash-apps/620-vader-sentiment-analysis'

####### Write your primary function here
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        final="Positive"
    elif sentiment_dict['compound'] <= - 0.05 :
        final="Negative"
    else :
        final="Neutral"
    # responses
    response1=f"Overall sentiment dictionary is : {sentiment_dict}"
    response2=f"sentence was rated as {sentiment_dict['neg']*100}% Negative"
    response3=f"sentence was rated as {sentiment_dict['neu']*100}% Neutral"
    response4=f"sentence was rated as {sentiment_dict['pos']*100}% Positive"
    response5=f"Sentence Overall Rated As {final}"
    # return (response1, response2, response3, response4, response5)
    return response5

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.Input(id='user-input', value=initial_value, type='text', style={'width':'80%'}),
    html.Button('Analyze!', id='submit-val', n_clicks=0, style=red_button_style),
    html.Div(id='output-div-1', children="Vader finds your lack of faith disturbing!"),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(
    Output(component_id='output-div-1', component_property='children'),
    [Input(component_id='user-input', component_property='value'),
    Input('submit-val', 'n_clicks')]
)
def update_output(sentence, n_clicks):
    if n_clicks==0:
        message = "Vader finds your lack of faith disturbing!"
    else:
        message = sentiment_scores(sentence)
        return message



############ Deploy
if __name__ == '__main__':
    app.run_server()
