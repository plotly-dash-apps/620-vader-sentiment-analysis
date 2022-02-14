import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



##### Define button style
button_style = {'background-color': 'darkblue',
                    'color': 'white',
                    'textAlign': 'center',
                }


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
    response2=f"Sentence rated as {round(sentiment_dict['neg']*100, 2)}% Negative"
    response3=f"Sentence rated as {round(sentiment_dict['neu']*100, 2)}% Neutral"
    response4=f"Sentence rated as {round(sentiment_dict['pos']*100,2 )}% Positive"
    response5=f"Sentence Overall Rated As {final}"
    return response1, response2, response3, response4, response5


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2('Input:'),
    dcc.Input(id='user-input', value=initial_value, type='text', style={'width':'80%'}),
    html.Button('Analyze!', id='submit-val', n_clicks=0, style=button_style),
    html.H2('Output:'),
    html.Div(id='output-div-1'),
    html.Div(id='output-div-2'),
    html.Div(id='output-div-3'),
    html.Div(id='output-div-4'),
    html.H4(id='output-div-5'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(
    Output(component_id='output-div-1', component_property='children'),
    Output(component_id='output-div-2', component_property='children'),
    Output(component_id='output-div-3', component_property='children'),
    Output(component_id='output-div-4', component_property='children'),
    Output(component_id='output-div-5', component_property='children'),
    Input('submit-val', 'n_clicks'),
    State(component_id='user-input', component_property='value')
)
def update_output(n_clicks, sentence):
    if n_clicks==0:
        message = 'Waiting for inputs','','','',''
        return message
    else:
        message = sentiment_scores(sentence)
        return message



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
