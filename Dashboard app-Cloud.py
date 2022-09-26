
"""
Created on Fri May  6 03:28:51 2022
@author: Bayan

Edited 06/28/2022
@editor: Alexandre

"""

import dash
from dash import dcc
from dash import html
from dash_table import DataTable
from dash_table import FormatTemplate
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import csv
import numpy as np
import math




#//////////////////////////////////////////////////////////////////////////////////////






def round_didgit(dataset,variable,round_lvl):
    for index, row in dataset.iterrows():
        if math.isnan(dataset[variable].loc[index]):
            pass
        else:
            dataset[variable].loc[index]=round(dataset[variable].loc[index],round_lvl)
            
def display_formating(df__di):
    
    df_d=df__di.copy()
    
    for name, values in df_d.iteritems():
    
        if name != 'date2':
            if df_d[name].dtype==np.int64 or df_d[name].dtype==np.float64:
                df_d.rename(columns = {name:str(name)+' ($ Millions)'}, inplace = True)

                for index, row in df_d.iterrows():
                    if math.isnan(df_d[str(name)+' ($ Millions)'].loc[index]):
                        pass
                    else:
                        numform=df_d[str(name)+' ($ Millions)'].loc[index]/1000000
                        numform=int(numform)
                        df_d[str(name)+' ($ Millions)'].loc[index]=numform
                    
    return df_d

def average_df(df_,tck):
    df_hypo_float=df_[df_['Ticker']==tck].select_dtypes('float')
    df_hypo=df_hypo_float.mean()
    return df_hypo



#//////////////////////////////////////////////////////////////////////////////////////


yahoo_logo = 'https://raw.githubusercontent.com//Bayan2019/TCC/main/Yahoo-Finance-3.png'
tcc_logo = 'https://raw.githubusercontent.com//Bayan2019/TCC/main/Logo_Curve_BG-Blue1.png'

CaaSWalletIPhone_bg = 'url(https://raw.githubusercontent.com//Bayan2019/TCC_Dashboard/main/pictures/CaaSWallet2_2.png)'

InventoryCard = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/InventoryCard.png)'
FactoringCard = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/FactoringCard.png)'
SupplierCard = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/SupplierCard.png)'

TCC = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Logo_Curve_BG-Blue1.png)'
header = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Header.png)'
header2='url(https://raw.githubusercontent.com/alexandre-tcc/CaaS_Calculator/CaaS Calculator header.png)'

Finance3 = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Finance3.png)'

ebitda = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/ebitda2.png)'
debt = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/debt2.png)'
wc = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/WORKINGCAPITAL.png)'
revenue = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Revenue.jpeg)'
GP = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/GrossProfit.png)'
cash = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/cash2.png)'
yahoo = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Yahoo.png)'
inventory = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/inventory.png)'

# Data Files

ucr_csv_annual = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_ws.csv'
ucr_csv_annual_new = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_new_ws.csv'
ucr_csv_quartal = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_quartal_ws.csv'

df_annual = pd.read_csv(ucr_csv_annual)
df_annual_new = pd.read_csv(ucr_csv_annual_new)
df_quartal = pd.read_csv(ucr_csv_quartal)

ucr_csv_annual_usd = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_usd_ws.csv'
ucr_csv_annual_new_usd = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_new_usd_ws.csv'
ucr_csv_quartal_usd = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_quartal_usd_ws.csv'

df_annual_usd = pd.read_csv(ucr_csv_annual_usd)
df_annual_new_usd = pd.read_csv(ucr_csv_annual_new_usd)
df_quartal_usd = pd.read_csv(ucr_csv_quartal_usd)

src1 = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/list_comp_fs_yahoo_ws.csv'

tickers = pd.read_csv(src1)

ucr_ratios = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_new_ratios.csv'

ratios = pd.read_csv(ucr_ratios)
ratios['Date_formated']=ratios['date'].astype(str).str[0:4]

round_didgit(ratios,'DIO',1)
round_didgit(ratios,'DPO',1)
round_didgit(ratios,'DSO',1)
round_didgit(ratios,'InventoryTurnover',1)
round_didgit(ratios,'CCC',1)
round_didgit(ratios,'ROCE',3)
round_didgit(ratios,'ROIC',3)

Big_df_annual = df_annual
Big_df_annual = Big_df_annual.drop(['ticker', 'date', 'name', 'sector', 'subsector',
                                    'currency'], axis=1)

All_columns0 = list(Big_df_annual.columns)

Big_df_annual = df_annual
Big_df_annual = Big_df_annual.drop(['name', 'sector', 'subsector',
                                    'currency'], axis=1)

Big_df_melt = pd.melt(Big_df_annual, id_vars=['date', 'ticker'])
Big_df_melt = Big_df_melt.dropna()

All_columns = []

for col in All_columns0:
    if (col in list(Big_df_melt['variable'])): All_columns.append(col)

All_columns_pos = []

for col in All_columns:
    if (Big_df_annual[col].dropna() > 0.1).all(): All_columns_pos.append(col)
All_columns_pos1 = All_columns_pos + ['inventory_to_assets']

options_period = [{'label': 'Annual', 'value': 'annual'}, {'label': 'Quartal', 'value': 'quarterly'}]

options_ratio_tcc = [{'label': 'EBIT to Interest Expense', 'value': 'EBIT to Interest Expense'}, 
                    {'label': 'EBITDA to Interest Expense', 'value': 'EBITDA to Interest Expense'},
                    {'label': 'Return On Capital', 'value': 'Return On Capital'},
                    {'label': 'EBITDA to Revenue', 'value': 'EBITDA to Revenue'},
                    {'label': 'Free Operating Cash Flow to Total Debt', 'value': 'Free Operating Cash Flow to Total Debt'},
                    {'label': 'Funds From Operations to Total Debt', 'value': 'Funds From Operations to Total Debt'},]

options_fin_tcc = [{'label': 'EBITDA', 'value': 'ebitda'},
                   {'label': 'EBIT', 'value': 'ebit'},
                    {'label': 'Total Debt', 'value': 'TotalDebt'},
                    {'label': 'Operating Income', 'value': 'operatingIncome'},
                    {'label': 'Interest Expense', 'value': 'interestExpense'}]



options_ticker = [{'label': tickers.loc[i, 'name'],
                   'value': tickers.loc[i, 'ticker']}
                  for i in tickers.sort_values(['name']).index]

options_columns = [{'label': col, 'value': col} for col in All_columns]

options_columns_pos = [{'label': col, 'value': col} for col in All_columns_pos]

options_columns_pos1 = [{'label': col, 'value': col} for col in All_columns_pos1]

options_tickers_exclude = [tickers.loc[i, 'ticker'] for i in tickers.index]

sectors_exclude = list(tickers['sector'].dropna().unique())
sectors_exclude.sort()
sectors_table = pd.DataFrame({'Sectors': sectors_exclude})

sectors_focus = sectors_exclude + ['All']
sectors_focus.sort()

subsectors_exclude = list(tickers['subsector'].dropna().unique())
subsectors_exclude.sort()

subsectors_focus = subsectors_exclude + ['All']
subsectors_focus.sort()

countries_exclude = list(tickers['country'].dropna().unique())
countries_exclude.sort()

countries_focus = countries_exclude + ['All']
countries_focus.sort()

tickers_geo = tickers[['ticker', 'name', 'country', 'latitude', 'longitude']].dropna()

tickers_geo.index = range(tickers_geo.shape[0])

geo_tickers_exclude = DataTable(
    id='geo_tickers_exclude',
    columns=[{'name': 'ticker', 'id': 'ticker'},
             {'name': 'name', 'id': 'name'},
             {'name': 'country', 'id': 'country'}],
    data=tickers_geo.to_dict('records'),
    cell_selectable=False,
    sort_action='native',
    filter_action='native',
    page_action='native',
    page_current=0,
    page_size=12,
    row_selectable='multi',
    style_cell=({'textAlign': 'left', 'background-color': 'white', 'color': 'rgb(6, 0, 45)'}),
    style_header={'textAlign': 'center','background-color': 'white', 'color': 'rgb(79, 79, 79)'},
    style_data={'whiteSpace': 'normal', 'height': 'auto'}
)

geo_tickers_focus = DataTable(
    id='geo_tickers_focus',
    columns=[{'name': 'ticker', 'id': 'ticker'},
             {'name': 'name', 'id': 'name'},
             {'name': 'country', 'id': 'country'}],
    data=tickers_geo.to_dict('records'),
    cell_selectable=False,
    sort_action='native',
    filter_action='native',
    style_table={'height': '450px', 'overflowY': 'auto'},
    row_selectable='single',
    style_cell=({'textAlign': 'left', 'background-color': 'rgb(245,245,245)', 'color': 'rgb(6, 0, 45)'}),
    style_header={'background-color': 'rgb(255, 154, 38)', 'color': 'rgb(79, 79, 79)','font-family':'sans-serif' ,
                  'fontSize': 25},
    style_data={'whiteSpace': 'normal', 'height': 'auto','font-family':'sans-serif' ,
                  'fontSize': 20}
)

treemap_tickers_exclude = DataTable(
    id='treemap_tickers_exclude',
    columns=[{'name': 'Ticker', 'id': 'ticker'}, {'name': 'Name', 'id': 'name'},
             {'name': 'Sector', 'id': 'sector'}, {'name': 'Subsector', 'id': 'subsector'},
             {'name': 'Country', 'id': 'country'}],
    data=tickers.to_dict('records'),
    cell_selectable=False,
    sort_action='native',
    fixed_rows={'headers': True},
    filter_action='native',
    style_table={'height': '450px', 'overflowY': 'auto'},
    row_selectable='multi',
    style_cell=({'textAlign': 'left', 'background-color': 'rgb(245,245,245)', 'color': 'rgb(6, 0, 45)'}),
    style_header={'textAlign': 'center','background-color': 'rgb(255, 154, 38)', 'color': 'rgb(79, 79, 79)','font-family':'sans-serif' ,
                  'fontSize': 25},
    style_data={'whiteSpace': 'normal', 'height': 'auto','font-family':'sans-serif' ,
                  'fontSize': 20}
)


def get_title(ticker):
    df = tickers.set_index('ticker')
    title = df.loc[ticker, 'name']

    return title

def plot_style(paper_bg='white', plot_bg='rgb(237, 239, 255)', font='rgb(79, 79, 79)'):
    plot_style = {'paper_bgcolor': paper_bg, 'plot_bgcolor': plot_bg,
                  'font': {'color': font , 'size' : 14, 'family':'sans-serif'}}
    return plot_style

def plot_style_treemap(paper_bg='white', plot_bg='rgb(237, 239, 255)', font='rgb(79, 79, 79)'):
    plot_style = {'paper_bgcolor': paper_bg, 'plot_bgcolor': plot_bg,
                  'font': {'color': font , 'size' : 18, 'family':'sans-serif'}}
    return plot_style

def plot_style_blue(paper_bg='rgb(232, 241, 255)', plot_bg='rgb(247, 249, 255)', font='rgb(79, 79, 79)'):
    plot_style = {'paper_bgcolor': paper_bg, 'plot_bgcolor': plot_bg,
                  'font': {'color': font , 'size' : 18, 'family':'sans-serif'}}
    return plot_style


#//////////////////////////////////////////////////////////////////////////////////////


def stand_years(df_,year_name_format,ticker_name_format):
    df_r=df_.copy()
    df_r.fillna(0)
    lst_years=[2017,2018,2019,2020,2021,2022]
    #print('list year : ', lst_r)
    lst_ticker=df_r[ticker_name_format].unique()
    
    lst_dummy= [0]*df_r.shape[1]  
    #print(lst_dummy)
    
    for tck in lst_ticker:
        df_tck = df_r[df_r[ticker_name_format]==tck]
        lst_years_tck=df_tck[year_name_format].unique()
        add_years=np.setdiff1d(lst_years, lst_years_tck)
        for year in add_years:
            df_r.loc[df_r.shape[0]]=lst_dummy
            df_r.at[df_r.shape[0]-1, year_name_format]= year
            df_r.at[df_r.shape[0]-1, ticker_name_format]= tck

    return df_r

def space_upper(text):
    new_text = ''

    for i, letter in enumerate(text):
        if i and letter.isupper():
            new_text += ' '

        new_text += letter

    return new_text

def format_columns(dft,limit):
    for row in dft.itertuples():
        if row.Index < limit:
            name=space_upper(dft.columns[row.Index]).capitalize()
            dft = dft.rename(columns={dft.columns[row.Index]: name})
    return dft

df_annual_usd_formated=format_columns(df_annual_usd,78)
df_annual_formated=format_columns(df_annual,77)
df_quartal_formated=format_columns(df_quartal,77)
df_annual_formated['Date_formated']=df_annual_formated['Date'].astype(str).str[0:4]#-------------------------------------
df_annual_new_formated=format_columns(df_annual_new,77)

df_annual_usd_formated = df_annual_usd_formated.rename(columns={'Total liab': 'Total liabilities'})
df_annual_formated = df_annual_formated.rename(columns={'Total liab': 'Total liabilities'})
df_quartal_formated = df_quartal_formated.rename(columns={'Total liab': 'Total liabilities'})
df_annual_new_formated = df_annual_new_formated.rename(columns={'Total liab': 'Total liabilities'})

df_annual_formated2=display_formating(df_annual_formated)
df_annual_new_formated2=display_formating(df_annual_new_formated)


#---------------------FORMATED---------------------------

Big_df_annual = df_annual_new
Big_df_annual = Big_df_annual.drop([ 'name', 'sector', 'subsector',
                                    'currency'], axis=1)
Big_df_annual_formated=format_columns(Big_df_annual,71)
Big_df_annual_formated = Big_df_annual_formated.rename(columns={'Total liab': 'Total liabilities'})


All_columns0_formated = list(Big_df_annual_formated.columns)


Big_df_melt_formated = pd.melt(Big_df_annual_formated, id_vars=['Date', 'Ticker'])
Big_df_melt_formated = Big_df_melt_formated.dropna()

All_columns_formated = []

for col in All_columns0_formated:
    if (col in list(Big_df_melt_formated['variable'])): All_columns_formated.append(col)

All_columns_pos_formated = []

for col in All_columns_formated:
    if (Big_df_annual_formated[col].dropna() > 0.1).all(): All_columns_pos_formated.append(col)
All_columns_pos1_formated = All_columns_pos_formated + ['Inventory to assets']

options_period_formated = [{'label': 'Annual', 'value': 'annual'}, {'label': 'Quartal', 'value': 'quarterly'}]

options_ticker_formated = [{'label': tickers.loc[i, 'name'],
                   'value': tickers.loc[i, 'ticker']}
                  for i in tickers.sort_values(['name']).index]


# OPTIONS -----------------------

options_columns_formated = [{'label': col, 'value': col} for col in All_columns_formated]

options_columns_pos_formated = [{'label': col, 'value': col} for col in All_columns_pos_formated]

options_columns_pos1_formated = [{'label': col, 'value': col} for col in All_columns_pos1_formated]

options_tickers_exclude_formated = [tickers.loc[i, 'ticker'] for i in tickers.index]

days_op=ratios.copy()
days_op=days_op[['DIO','DPO','DSO','InventoryTurnover','CCC']]
days_col=list(days_op.columns)
options_days = [{'label': col, 'value': col} for col in days_col]

ratios_op=ratios.copy()
ratios_op.drop(columns=['ticker', 'date', 'date2', 'Date_formated', 'DIO','DPO','DSO','InventoryTurnover','CCC'],inplace=True)
ratio_col=list(ratios_op.columns)
options_ratios = [{'label': col, 'value': col} for col in ratio_col]

# YEARS---------------------------------------------

ratios_stand_year=stand_years(ratios,'Date_formated','ticker')
df_annual_formated2_stand_year=stand_years(df_annual_formated2,'Date_formated','Ticker')


#//////////////////////////////////////////////////////////////////////////////////////


# Create the Dash app

app = dash.Dash(__name__)

app.layout = html.Div([
    
    
    html.Header(
      children = [   
      html.Br(),
      html.Br(),
      html.Br(),
      html.Br(),
      html.H1(' ', style={'color':'rgb(254, 163, 27)', 'fontSize': 1,
                                          'display':'inline-block'})],
                 style={'width':'100%', 'height':'1px',
                        'background-image':header2, 'background-repeat':'no-repeat',
                'background-position':'left'}),
    
    
    html.Div(
        children=[
            #html.Img(src=TCC),
            html.Br(),
            html.H1('CaaS Calculator', style={'color': 'rgb(15, 13, 37)', 
                                            'textAlign': 'center','font-family':'sans-serif' ,'fontSize': 80,}),
            html.Br(),

        
        ]
        ,style={'background-color': 'rgb(255, 154, 38)'}
                                                  
        ),
    
  

    # Overall Summary
    dcc.Tabs(
        id="tabs_common_summary", value='tab_general',
        className='custom-tabs', vertical=False,
        children=[
            dcc.Tab(label='General info', value='tab_general', className='custom-tab',
                    selected_className='custom-tab--selected',style={'background-color':'rgb(250, 213, 165)'}),
            dcc.Tab(label='Company & industry', value='tab_comp_indus', className='custom-tab',
                    selected_className='custom-tab--selected',style={'background-color':'rgb(250, 213, 165)'}),
            dcc.Tab(label='CaaS Simulation', value='tab_calc', className='custom-tab',
                    selected_className='custom-tab--selected',style={'background-color':'rgb(250, 213, 165)'}),
        ], style={'height': '70px','font-family':'sans-serif','fontSize': 25,'color':'rgb(25, 25, 25)'}),
    html.Br(),
    html.Div(id='tabs_common_summary_content'),
    html.Br(),

    # Individual Summary
    dcc.Tabs(
        id="tabs_individual_summary", value='tab_scatter_figs',
        className='custom-tabs', vertical=False,
        children=[
            dcc.Tab(label='Trade Capital Corporation © 2022', value='tab_scatter_figs', className='custom-tab',
                    selected_className='custom-tab--selected'),
        ], style={'height': '44px'}),
    html.Br(),
    html.Div(id='tabs_individual_summary_content'),
    html.Br(),

    # Closing
    ],
    style={'text-align': 'center', 'display': 'inline-block', 'width': '100%',
           'background-color': 'rgb(245, 245, 245)', 'color': 'rgb(79, 79, 79)'})

# Overall Summary tabs





@app.callback(
    Output('tabs_common_summary_content', 'children'),
    Input('tabs_common_summary', 'value'),
    #Input('comp_general', 'value')

)
def render_common_content(tab):
    if tab == 'tab_general':
        return html.Div(
            children=[

                # Treemap 1
                
                
                html.Br(),
                html.Br(),
                html.Div(
                    children=[
                        #--------------- PARAMM
                        html.H3('ECONOMY MAPPING',style={'color': 'black','font-family':'sans-serif','verticalAlign': 'top' ,'fontSize': 45,
                                                  'display': 'inline-block','horizontalAlign': 'center','margin': '30px 20px 10px 10px',}),
                        html.Br(),
                        html.Div(
                            children=[

                                html.H3('Parameters',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 40,
                                                          'display': 'inline-block','horizontalAlign': 'center','width': '450px'}),
                                html.Br(),

                                html.Div(
                                    children=[

                                        html.H3('Variable influencing the Colour:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '350px'}),
                                        dcc.Dropdown(id='treemap_column_c', options=options_columns_formated,
                                                     value='Inventory',
                                                     style={'width': '300px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),
                                    ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center',}),
                                html.Br(),
                                html.Br(),

                                html.Div(
                                    children=[

                                        html.H3('Companies HQ localisation:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '350px'}),
                                        dcc.Dropdown(id='treemap_countries_focus', options=countries_focus, value='All',
                                                     style={'width': '300px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),
                                    ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center',}),
                                html.Br(),
                                html.Br(),
                                
                                html.Div(
                                    children=[

                                        html.H3('Sector to Focus:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '350px'}),
                                        dcc.Dropdown(id='treemap_sectors_focus', options=sectors_focus, value='All',
                                                     style={'width': '300px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),
                                    ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center',}),
                                html.Br(),
                                html.Br(),
                                
                                html.Div(
                                    children=[

                                        html.H3('Subsector to Focus:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '350px'}),
                                        dcc.Dropdown(id='treemap_subsectors_focus', options=subsectors_focus, value='All',
                                                     style={'width': '300px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),
                                    ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center',}),
                                html.Br(),
                                html.Br(),
                                
                                html.Div(
                                    children=[

                                        html.H3('Select Volume Variable:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '350px'}),
                                        dcc.Dropdown(id='treemap_column_v', options=options_columns_pos1_formated, value='Inventory to assets',
                                                     style={'width': '300px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),
                                    ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center',}),
                                html.Br(),


                                html.Div(
                                    children=[

                                        html.Br(),
                                        html.Br(),
                                        html.H3('Companies to Exclude (select the ones you want to exclude):',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,'fontSize': 20,
                                                          'display': 'inline-block','horizontalAlign': 'center','width': '700px'}),
                                        treemap_tickers_exclude
                                    ], style={'width': '80%', 'height': '600px',
                                              'margin': '0px 10px 0px 10px', 'display': 'inline-block','horizontalAlign': 'center',}),

                                ],
                            style={'width': '75%', 'display': 'inline-block',
                                   'border': '3px solid orange','background-color':'rgb(255, 247, 237)', 'border-radius': 20,'margin': '20px 30px 20px 20px','padding': '20px 30px 20px 20px'}),

                        html.Div(
                            children=[
                                dcc.Graph(id='treemap1', style={'width':'100%','height': '1100px','margin': '20px 30px 20px 20px',
                                                                        })],
                            style={'width': '70%', 'display': 'inline-block','horizontalAlign': 'left',
                                   'margin': '0px 5px 0px 5px', 'verticalAlign': 'top'}),
                        html.Div(
                            
                            children=[
                                
                                html.H3('Outlier locality:',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                  'display': 'inline-block','margin': '50px 50px 50px 50px'}),
                                dcc.Graph(id='treemap2'),

                            ], style={'width': '20%', 'height': '98px',
                                      'margin': '0px 10px 0px 10px','horizontalAlign': 'right', 'display': 'inline-block'}),
                        #--------------- END
                        
                        html.Br(),
                        
                        
                        ],
                    style={'horizontalAlign': 'center','width': '90%','border':'3px solid orange','display': 'inline-block',
                      'background-color':'white', 'border-radius': 20,'margin': '20px 30px 20px 20px','padding': '20px 30px 20px 20px'}   ),
                
                
                
                html.Br(),            
                html.Br(),
                html.Br(),
                
                ])

    elif tab == 'tab_comp_indus':
        return(
        #-----------------------------------------------SELECT A COMPANY----------    
            html.Div(
                children=[
                    html.Div(
                            children=[

                                html.H3('Select a company:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                     'fontSize': 25,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                  'display': 'inline-block','horizontalAlign': 'left','width': '300px'}),
                                dcc.Dropdown(id='comp_general', options=options_ticker, #value='AME',
                                             style={'width': '400px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                    'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                    'font-family':'sans-serif' ,'fontSize': 20}),
                            ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center','margin' : '50px 50px 50px 50px'}),



                ]
                #,style={'background-color': 'rgb(255, 154, 38)'}

                ),
            html.Div(id='tab_compare'),
        #-----------------------------------------------SELECT A COMPANY----------  
        )


    elif tab == 'tab_calc':
        return(
        #-----------------------------------------------SELECT A COMPANY----------    
            html.Div(
                children=[
                    html.Div(
                            children=[

                                html.H3('Select a company:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                     'fontSize': 25,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                  'display': 'inline-block','horizontalAlign': 'left','width': '300px'}),
                                dcc.Dropdown(id='tcc1_ticker', options=options_ticker, #value='AME',
                                             style={'width': '400px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                    'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                    'font-family':'sans-serif' ,'fontSize': 20}),
                            ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center','margin' : '50px 50px 50px 50px'}),



                ]
                #,style={'background-color': 'rgb(255, 154, 38)'}

                ),
            html.Div(id='tab_simu'),
        #-----------------------------------------------SELECT A COMPANY----------  
        ) 


    
    
'''@app.callback(
    Output('hypo', 'children'),
    Input('tcc1_ticker', 'value')

)
def render_hypo(comp):
    df_hypo=average_df(df_annual_formated2,comp)
    var_list=set(df_hypo.dropna().index)
    rtr=(html.H3('Cash ($ Millions):',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),
                                        
                                        dcc.Input(id='hypo_cash', type='number', min=0, value=df_hypo["Cash ($ Millions)"], step=1,placeholder="($ Millions)",
                                                  style={'width': '400px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                    'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                    'font-family':'sans-serif' ,'fontSize': 20}),)
    return rtr'''
    
    
    
@app.callback(
    Output('radio_param', 'children'),
    Input('tcc1_radio', 'value')

)
def render_radio_param(radio):
    if radio=='pour':
        return(
        html.Br(),
        html.H3('Select (%)',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                     'fontSize': 25,'verticalAlign': 'top','margin' : '20px 20px 20px 20px',
                                                  'display': 'inline-block','horizontalAlign': 'left','width': '300px'}),
        dcc.Slider(id='tcc1_slider', min=0, max=100,
                   marks=None, value=50, step=1, 
                   tooltip={"placement": "bottom", "always_visible": True}),
        html.Br(),
        dcc.Input(id='tcc_amount', type='number', min=0, max=1000, value=0, step=1,placeholder="$ Millions",style={'height': '0px','width': '0px',
                                                    'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                    'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                    'font-family':'sans-serif','margin' : '20px 20px 20px 20px' ,'fontSize': 1}),
        html.Br(),
        )
        
    else:
        return(
        html.Br(),
        html.H3('Amount of inventory to fund ($ Millions)',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                     'fontSize': 25,'verticalAlign': 'top','margin' : '20px 20px 20px 20px',
                                                  'display': 'inline-block','horizontalAlign': 'left','width': '50%'}),
        html.Br(),
        dcc.Input(id='tcc_amount', type='number', min=0, max=1000, value=0, step=1,placeholder="$ Millions",style={'width': '300px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                    'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                    'font-family':'sans-serif','margin' : '20px 20px 20px 20px' ,'fontSize': 20}),
        html.Br(),
        dcc.Input(id='tcc1_slider', type='number', min=0, max=1000, value=0, step=1,placeholder="$ Millions",style={'height': '0px','width': '0px',
                                                'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                                'font-family':'sans-serif','margin' : '20px 20px 20px 20px' ,'fontSize': 1}),
        )
    
    
@app.callback(
    Output('tab_simu', 'children'),
    Input('tcc1_ticker', 'value')

)
def render_compare_content(comp):
    #return(html.H1('TEST TEST TES'),)
    if comp == None:
            return html.Div(children=[html.H3('Please select a Company',style={'color': 'rgb(207, 207, 207)','font-family':'sans-serif' ,
                                                             'fontSize': 40,'margin': '20px 30px 1000px 20px'})], )
        
    else: 
        return html.Div(
            children=[
                html.Br(),
                
                
                
                #---------------------------COMPARIZON COMP----------------------------------------
                
                html.Br(),
                html.Div(
                    children=[
                        
                          html.H3('Simulation',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 50,
                                                              'display': 'inline-block'}),
                                html.Br(),
                        
                        html.Div(
                            children=[
                                html.Br(),
                                html.H3('Inventory Funding Involment',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                                      'display': 'inline-block'}),

                                html.Br(),

                                html.Br(),
                                dcc.RadioItems(id='tcc1_radio', options={'pour': 'By Pourcentage','number': 'By specific Amount'}
                                               ,value='pour',labelStyle={'width':'200','margin':"10px 10px 10px 10px"},
                                               style={'color': 'black','font-family':'sans-serif' ,
                                                      'fontSize': 22,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                      'display': 'inline-block','horizontalAlign': 'left','width': '50%'}),
                                html.Br(),
                                
                                
                                html.Div(id='radio_param'),

                                

                            ],
                            style={'width': '60%', 'display': 'inline-block','border': '3px solid orange',
                               'horizontalAlign': 'center','border-radius': 20,'background-color':'rgb(255, 247, 237)'}),

                        
                        html.Br(),

                        
                        
                        html.Br(),
                    #*************************************
                        html.Div(
                    children=[
                        html.H3('Impact on Cash and Inventory',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                      'display': 'inline-block','horizontalAlign': 'center','width':'65%'}),


                        html.Br(),

                                html.Div(
                                    children=[dcc.Graph(id='tcc_inv_cash')],
                                    style={'width': '80%','horizontalAlign': 'center','display': 'inline-block','margin':'50px 0px 0px 0px'}),
                                html.Br(),


                        html.Br(),
                        html.Br(),


                        ],
                    style={'width': '90%', 'display': 'inline-block',
                           'border': '0px solid orange', 'border-radius': 20,'background-color':'rgb(232, 241, 255)','margin': '20px 30px 20px 20px'}),
                    html.Br(),
                    #*************************************
                        
                        
                    #*************************************
                        html.Div(
                    children=[
                        html.H3('Other Impacted Financials',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                      'display': 'inline-block','horizontalAlign': 'center','width':'65%'}),

                        html.Br(),

                        html.H3('Display specific financial:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),

                        html.Br(),
                        dcc.Dropdown(id='bar_fin_var' ,options=options_fin_tcc, value='TotalDebt',
                                                     style={'width': '400px','display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue','margin':'10px 0px 0px 0px',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),

                        html.Br(),

                                html.Div(
                                    children=[dcc.Graph(id='tcc_fin_fig')],
                                    style={'width': '80%','horizontalAlign': 'center','display': 'inline-block','margin':'50px 0px 0px 0px'}),
                                html.Br(),


                        html.Br(),
                        html.Br(),


                        ],
                    style={'width': '90%', 'display': 'inline-block',
                           'border': '0px solid orange', 'border-radius': 20,'background-color':'rgb(232, 241, 255)','margin': '20px 30px 20px 20px'}),
                    html.Br(),
                    #*************************************
                        
                    #*************************************
                        html.Div(
                    children=[
                        html.H3('Impact on Ratios',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                      'display': 'inline-block','horizontalAlign': 'center','width':'65%'}),

                        html.Br(),

                        html.H3('Display specific ratio:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),

                        html.Br(),
                        dcc.Dropdown(id='bar_ratio_var', multi=True ,options=options_ratio_tcc, value=['EBIT to Interest Expense','EBITDA to Interest Expense'],
                                                     style={'height':'100px', 'width': '400px','display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue','margin':'10px 0px 0px 0px',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),

                        html.Br(),

                                html.Div(
                                    children=[dcc.Graph(id='tcc_ratio_fig')],
                                    style={'width': '80%','horizontalAlign': 'center','display': 'inline-block','margin':'50px 0px 0px 0px'}),
                                html.Br(),


                        html.Br(),
                        html.Br(),


                        ],
                    style={'width': '90%', 'display': 'inline-block',
                           'border': '0px solid orange', 'border-radius': 20,'background-color':'rgb(232, 241, 255)','margin': '20px 30px 20px 20px'}),
                    html.Br(),
                    #*************************************
                        
                   
                        
                        
                    ],style={'width':'90%','display': 'inline-block','border': '3px solid orange',
                            'horizontalAlign': 'center','border-radius': 20,'background-color':'white',
                            'margin': '20px 30px 20px 20px'}),
                
                #----------------------------------------------------------------------------------------
                
                
                
                
                #html.Div(id='hypo'),
                
                
                
                                
                 ])
    

@app.callback(
    Output('tab_compare', 'children'),
    Input('comp_general', 'value')

)
def render_compare_content(comp):
    #return(html.H1('TEST TEST TES'),)
    if comp == None:
            return html.Div(children=[html.H3('Please select a Company',style={'color': 'rgb(207, 207, 207)','font-family':'sans-serif' ,
                                                             'fontSize': 40,'margin': '20px 30px 1000px 20px'})], )
        
    else:
        return html.Div(children=[
        html.Br(),
        html.H3('Ticker : '+comp,style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 50,
                                              'display': 'inline-block'}),


        html.Br(),
        html.Br(),
        html.Br(),



        # Debt_Rev

        html.Br(),
        html.Div(
            children=[
                html.H3('Company focus',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                              'display': 'inline-block','horizontalAlign': 'center','width':'65%'}),
                
                html.Br(),
                
                html.H3('Display specific variable:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                     'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                  'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),
                
                html.Br(),
                dcc.Dropdown(id='bar_focus_var', multi=True ,options=options_columns_formated, value=['Cash','Inventory','Total liabilities','Total assets'],
                                             style={'height':'100px', 'width': '400px','display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                    'color': 'blue','margin':'10px 0px 0px 0px',
                                                    'font-family':'sans-serif' ,'fontSize': 20}),
                
                html.Br(),
                        
                        html.Div(
                            children=[dcc.Graph(id='bar_fig4')],
                            style={'width': '80%','horizontalAlign': 'center','display': 'inline-block','margin':'50px 0px 0px 0px'}),
                        html.Br(),

                        
                html.Br(),
                html.Br(),


                ],
            style={'width': '90%', 'display': 'inline-block',
                   'border': '3px solid orange', 'border-radius': 20,'background-color':'white','margin': '20px 30px 20px 20px'}),





        # INDUSTRY---------------------------------------------------------------------------
        html.Br(),


        html.Div(
            children=[
                html.H3('Company compare to its industry',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                              'display': 'inline-block'}),
                html.Br(),
                html.Div(
                    children=[

                        html.H3('Variable to compare the industry with:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                          'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),
                        dcc.Dropdown(id='induscomp1_var', options=options_columns_formated, value='Cash',
                                     style={'width': '400px',  'display': 'inline-block','margin' : '0px 0px 0px 0px',
                                            'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                            'font-family':'sans-serif' ,'fontSize': 20}),
                    ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center',}),

                html.Div(
                    children=[dcc.Graph(id='induscomp1')],
                    style={'width': '80%','horizontalAlign': 'center','display': 'inline-block'}),
                ],
            style={'width': '90%', 'display': 'inline-block',
                   'border': '3px solid orange', 'border-radius': 20,'background-color':'white','margin': '20px 30px 20px 20px'}),


        # COMPANY vs COMPANY-----------------------------------------------------------------

        html.Br(),
        
        
        html.Div(
            children=[

                html.Div(
                    children=[
        
                html.H3('Comparizon with other Companies',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                  'display': 'inline-block'}),
                html.Br(),

                
                    
                html.Div(
                    children=[


                        html.H3('Organization to Compare with:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                          'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),
                        dcc.Dropdown(id='bar_columns_tickers', options=options_ticker, #value='TXT',
                                     style={'width': '400px',  'display': 'inline-block','margin' : '0px 0px 20px 0px',
                                            'color': 'blue', 'horizontalAlign': 'right','verticalAlign': 'top',
                                            'font-family':'sans-serif' ,'fontSize': 20}),
                    ],style={'width': '80%', 'display': 'inline-block','horizontalAlign': 'center',})
                        
                    ]
                ,style={'width': '60%', 'display': 'inline-block','margin' : '20px 0px 20px 0px',
                   'border': '3px solid orange', 'border-radius': 20,'background-color':'white','background-color':'rgb(255, 247, 237)','margin': '20px 30px 20px 20px','padding': '20px 30px 20px 20px'}),




                html.Br(),
                html.Br(),


       
                html.Br(),
                html.Div(
                    children=[
                        html.H3('Key Turnaround Days',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                      'display': 'inline-block','horizontalAlign': 'center','width':'65%'}),

                        html.Br(),

                        html.H3('Display specific variable:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),

                        html.Br(),
                        dcc.Dropdown(id='bar_days_var', multi=True ,options=options_days, value=['DIO','DSO','DPO'],
                                                     style={'height':'100px', 'width': '400px','display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue','margin':'10px 0px 0px 0px',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),

                        html.Br(),

                                html.Div(
                                    children=[dcc.Graph(id='bar_days')],
                                    style={'width': '80%','horizontalAlign': 'center','display': 'inline-block','margin':'50px 0px 0px 0px'}),
                                html.Br(),


                        html.Br(),
                        html.Br(),


                        ],
                    style={'width': '90%', 'display': 'inline-block',
                           'border': '0px solid orange', 'border-radius': 20,'background-color':'rgb(232, 241, 255)','margin': '20px 30px 20px 20px'}),
                    html.Br(),
#-------------------------------------------------------------------                
                
                html.Br(),
                html.Div(
                    children=[
                        html.H3('Key Ratios',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                      'display': 'inline-block','horizontalAlign': 'center','width':'65%'}),

                        html.Br(),

                        html.H3('Display specific variable:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),

                        html.Br(),
                        dcc.Dropdown(id='bar_ratio_var', multi=True ,options=options_ratios, value=['ROCE','ROIC'],
                                                     style={'height':'100px', 'width': '400px','display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue','margin':'10px 0px 0px 0px',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),

                        html.Br(),

                                html.Div(
                                    children=[dcc.Graph(id='bar_ratio')],
                                    style={'width': '80%','horizontalAlign': 'center','display': 'inline-block','margin':'50px 0px 0px 0px'}),
                                html.Br(),


                        html.Br(),
                        html.Br(),


                        ],
                    style={'width': '90%', 'display': 'inline-block',
                           'border': '0px solid orange', 'border-radius': 20,'background-color':'rgb(232, 241, 255)','margin': '20px 30px 20px 20px'}),
                    html.Br(),
#-------------------------------------------------------------------                
                
                html.Br(),
                html.Div(
                    children=[
                        html.H3('Bank/Income Statement values',style={'color': 'rgb(15, 13, 37)','font-family':'sans-serif' ,'fontSize': 35,
                                                      'display': 'inline-block','horizontalAlign': 'center','width':'65%'}),

                        html.Br(),

                        html.H3('Display specific variable:',style={'color': 'rgb(22, 73, 161)','font-family':'sans-serif' ,
                                                                             'fontSize': 20,'verticalAlign': 'top','margin' : '7px 0px 0px 0px',
                                                          'display': 'inline-block','horizontalAlign': 'left','width': '400px'}),

                        html.Br(),
                        dcc.Dropdown(id='bar_dol_var', multi=True ,options=options_columns_formated, value=['Cash','Inventory'],
                                                     style={'height':'100px', 'width': '400px','display': 'inline-block','margin' : '0px 0px 0px 0px',
                                                            'color': 'blue','margin':'10px 0px 0px 0px',
                                                            'font-family':'sans-serif' ,'fontSize': 20}),

                        html.Br(),

                                html.Div(
                                    children=[dcc.Graph(id='bar_dol')],
                                    style={'width': '80%','horizontalAlign': 'center','display': 'inline-block','margin':'50px 0px 0px 0px'}),
                                html.Br(),


                        html.Br(),
                        html.Br(),


                        ],
                    style={'width': '90%', 'display': 'inline-block',
                           'border': '0px solid orange', 'border-radius': 20,
                           'background-color':'rgb(232, 241, 255)','margin': '20px 30px 20px 20px'}),
                    html.Br(),

#-------------------------------------------------------------------

            ],
            style={'width': '90%', 'display': 'inline-block','border': '3px solid orange',
                   'horizontalAlign': 'center','border-radius': 20,'background-color':'white','margin':'20px 30px 20px 20px',
                   }),

        html.Br(),
        html.H3(' '),




         ])


#//////////////////////////////////////////////////////////////////////////////////////


# Geo plot

@app.callback(
    Output(component_id='geo', component_property='figure'),
    Input(component_id='geo_column_v', component_property='value'),
    Input(component_id='treemap_column_c', component_property='value'),
    #Input(component_id='geo_tickers_focus', component_property='selected_rows'),
    Input(component_id='treemap_tickers_exclude', component_property='selected_rows'),
    Input(component_id='treemap_countries_focus', component_property='value')
)
def update_geo(column_v, column_c, ticks, country):
    df = df_annual_usd_formated

    if ticks:
        tickers_list = list(tickers_geo.loc[ticks, 'Ticker'])
    else:
        tickers_list = []

    if (country == 'All'):

        df = df[['Name', 'Ticker', 'Longitude', 'Latitude', column_v, column_c, 'Date2']].dropna()

    else:
        df = df[['Name', 'Ticker', 'Longitude', 'Latitude', column_v, column_c, 'Date2']].dropna()
        tickers_list0 = list(tickers_geo[tickers_geo['Country'] == country]['Ticker'])

        df = df[df.Ticker.isin(tickers_list0)]

    df.sort_values(by=['Date2'], inplace=True)

    ddf = df[~df.Ticker.isin(tickers_list)]

    geo_fig = px.scatter_geo(ddf,
                             lat="Latitude", lon="Longitude", color=column_c,
                             color_continuous_scale='RdYlGn_r',
                             animation_frame="Date2",
                             hover_name="Name",
                             hover_data=['Ticker', 'Name'],
                             size=np.array(ddf[column_v]),
                             size_max=35,
                             projection="orthographic",
                             )
    geo_fig.update_layout(geo=dict(
        resolution=50,
        showland=True,
        showcountries=True,
        showocean=True,
        showrivers=True,
        showsubunits=True,
        countrywidth=0.5,
        landcolor='rgb(105, 139, 105)',
        lakecolor='rgb(151, 255, 255)',
        oceancolor='rgb(46, 83, 158)', subunitcolor='rgb(254, 163, 27)', subunitwidth=1))
    geo_fig.update_geos(bgcolor='white', rivercolor='rgb(151, 255, 255)', riverwidth=1)

    
    geo_fig.update_layout(plot_style())

    return geo_fig


# Scatter Figures 1

@app.callback(
    Output(component_id='Debt_Rev_fig', component_property='figure'),
    Input(component_id='Debt_Rev_tickers', component_property='value'),
    Input(component_id='debt_rev_sectors_focus', component_property='value'),
    Input(component_id='debt_rev_subsectors_focus', component_property='value')
)
def update_Debt_Rev(ticks, sector, subsector):
    tickers_list = ticks

    df = df_annual_new_usd[['ticker', 'date', 'TotalDebt', 'totalRevenue',
                            'ebitda', 'inventory', 'WorkingCapital', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Debt_Rev = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                          color='ebitda', size='inventory', size_max=50,
                          y='TotalDebt', x='totalRevenue', hover_name='name',
                          color_continuous_scale='RdYlGn_r', hover_data=['date', 'ticker'])

    Debt_Rev.update_layout(plot_style())

    return Debt_Rev


@app.callback(
    Output(component_id='Debt_EBITDA_fig', component_property='figure'),
    Input(component_id='Debt_EBITDA_tickers', component_property='value'),
    Input(component_id='debt_ebitda_sectors_focus', component_property='value'),
    Input(component_id='debt_ebitda_subsectors_focus', component_property='value')
)
def update_Debt_EBITDA(ticks, sector, subsector):
    tickers_list = ticks

    df = df_annual_new_usd[['ticker', 'date', 'TotalDebt', 'totalRevenue',
                            'ebitda', 'inventory', 'WorkingCapital', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Debt_EBITDA = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                             color='WorkingCapital', size='totalRevenue', size_max=50,
                             y='TotalDebt', x='ebitda', color_continuous_scale='RdYlGn_r',
                             hover_name='name', hover_data=['date', 'ticker'])
    Debt_EBITDA.update_layout(plot_style())

    return Debt_EBITDA


@app.callback(
    Output(component_id='WC_Rev_fig', component_property='figure'),
    Input(component_id='WC_Rev_tickers', component_property='value'),
    Input(component_id='wc_rev_sectors_focus', component_property='value'),
    Input(component_id='wc_rev_subsectors_focus', component_property='value')
)
def update_WC_Rev(ticks, sector, subsector):
    tickers_list = ticks

    df = df_annual_new_usd[['ticker', 'date', 'TotalDebt', 'totalRevenue',
                            'ebitda', 'inventory', 'WorkingCapital', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    WC_Rev = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                        color='inventory', size='TotalDebt', size_max=50,
                        y='WorkingCapital', x='totalRevenue', color_continuous_scale='RdYlGn_r',
                        hover_name='name', hover_data=['date', 'ticker'])
    WC_Rev.update_layout(plot_style())

    return WC_Rev


@app.callback(
    Output(component_id='WC_Inv_fig', component_property='figure'),
    Input(component_id='WC_Inv_tickers', component_property='value'),
    Input(component_id='wc_inv_sectors_focus', component_property='value'),
    Input(component_id='wc_inv_subsectors_focus', component_property='value')
)
def update_WC_Inv(ticks, sector, subsector):
    tickers_list = ticks

    df = df_annual_new_usd[['ticker', 'date', 'TotalDebt', 'totalRevenue',
                            'ebitda', 'inventory', 'WorkingCapital', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    WC_Inv = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                        color='TotalDebt', size='totalRevenue', size_max=50,
                        y='WorkingCapital', x='inventory', color_continuous_scale='RdYlGn_r',
                        hover_name='name', hover_data=['date', 'ticker'])
    WC_Inv.update_layout(plot_style())

    return WC_Inv


# Scatter Figures 2

@app.callback(
    Output(component_id='Inv_Rev_fig', component_property='figure'),
    Input(component_id='Inv_Rev_period', component_property='value'),
    Input(component_id='Inv_Rev_tickers', component_property='value'),
    Input(component_id='inv_rev_sectors_focus', component_property='value'),
    Input(component_id='inv_rev_subsectors_focus', component_property='value')
)
def update_Inv_Rev(per, ticks, sector, subsector):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    tickers_list = ticks

    df = df[
        ['ticker', 'date', 'cash', 'totalRevenue', 'grossProfit', 'inventory', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Inv_Rev = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                         color='grossProfit', size='cash', size_max=50,
                         y='inventory', x='totalRevenue', color_continuous_scale='RdYlGn_r',
                         hover_name='name', hover_data=['date', 'ticker'])
    Inv_Rev.update_layout(plot_style())

    return Inv_Rev


@app.callback(
    Output(component_id='Inv_Cash_fig', component_property='figure'),
    Input(component_id='Inv_Cash_period', component_property='value'),
    Input(component_id='Inv_Cash_tickers', component_property='value'),
    Input(component_id='inv_cash_sectors_focus', component_property='value'),
    Input(component_id='inv_cash_subsectors_focus', component_property='value')
)
def update_Inv_Cash(per, ticks, sector, subsector):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    tickers_list = ticks

    df = df[['ticker', 'date', 'cash', 'totalRevenue', 'grossProfit', 'inventory', 'name',
             'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Inv_Cash = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                          color='grossProfit', size='totalRevenue', size_max=50,
                          y='inventory', x='cash', color_continuous_scale='RdYlGn_r',
                          hover_name='name', hover_data=['date', 'ticker'])

    Inv_Cash.update_layout(plot_style())

    return Inv_Cash


@app.callback(
    Output(component_id='Gross_pr_Inv_fig', component_property='figure'),
    Input(component_id='Gross_pr_Inv_period', component_property='value'),
    Input(component_id='Gross_pr_Inv_tickers', component_property='value'),
    Input(component_id='gross_pr_inv_sectors_focus', component_property='value'),
    Input(component_id='gross_pr_inv_subsectors_focus', component_property='value')
)
def update_Gross_pr_Inv(per, ticks, sector, subsector):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    tickers_list = ticks

    df = df[['ticker', 'date', 'cash', 'totalRevenue', 'grossProfit', 'inventory', 'name',
             'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Gross_pr_Inv = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                              color='cash', size='totalRevenue', size_max=50,
                              y='grossProfit', x='inventory', color_continuous_scale='RdYlGn_r',
                              hover_name='name', hover_data=['date', 'ticker'])
    Gross_pr_Inv.update_layout(plot_style())

    return Gross_pr_Inv


@app.callback(
    Output(component_id='Gross_pr_Rev_fig', component_property='figure'),
    Input(component_id='Gross_pr_Rev_period', component_property='value'),
    Input(component_id='Gross_pr_Rev_tickers', component_property='value'),
    Input(component_id='gross_pr_rev_sectors_focus', component_property='value'),
    Input(component_id='gross_pr_rev_subsectors_focus', component_property='value')
)
def update_Gross_pr_Rev(per, ticks, sector, subsector):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    tickers_list = ticks

    df = df[['ticker', 'date', 'cash', 'totalRevenue', 'grossProfit', 'inventory', 'name',
             'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Gross_pr_Rev = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                              color='inventory', size='cash', size_max=50,
                              y='grossProfit', x='totalRevenue', color_continuous_scale='RdYlGn_r',
                              hover_name='name', hover_data=['date', 'ticker'])
    Gross_pr_Rev.update_layout(plot_style())

    return Gross_pr_Rev


# Treemap




@app.callback(
    Output(component_id='treemap1', component_property='figure'),
    Output(component_id='treemap2', component_property='figure'),
    Input(component_id='treemap_column_v', component_property='value'),
    Input(component_id='treemap_column_c', component_property='value'),
    Input(component_id='treemap_sectors_focus', component_property='value'),
    Input(component_id='treemap_subsectors_focus', component_property='value'),
    Input(component_id='treemap_tickers_exclude', component_property='selected_rows'),
    Input(component_id='treemap_countries_focus', component_property='value')
)
def update_treemap(vol_column, col_column, sector, subsector, ticks, country):
    pd.options.display.float_format = '{:,.2f}'.format
    df = df_annual_usd_formated
    
    country=[country]
        
    #if per == 'annual':df['date']=pd.to_datetime(df["date"].dt.strftime('%Y'))

    if ticks:
        tickers_list = list(tickers.loc[ticks, 'ticker'])
    else:
        tickers_list = []
        
    

    ddf = df.copy()
    ddf['Inventory to assets'] = ddf['Inventory'].div(ddf['Total assets'])#.round(3)
    #ddf=ddf.dropna()

    if (country == ['All']):
        dddf = ddf.copy()
    else:
        tickers_country = tickers[tickers['country'] == country[0]]
        if len(country)>0:
            for i in range(1,len(country)):
                tickers_country_add = tickers[tickers['country'] == country[i]]
                tickers_country=pd.concat([tickers_country,tickers_country_add])
        tickers_in_country = list(tickers_country['ticker'].dropna().unique())

        dddf = ddf[ddf.Ticker.isin(tickers_in_country)]

    if (subsector == 'All'):
        if (sector == 'All'):
            ddddf = dddf  # [~ddf.sector.isin(sectors_list)]
        else:
            ddddf = dddf[dddf['Sector'] == sector]
    else:
        ddddf = dddf[dddf['Subsector'] == subsector]
        
    #ddddf=ddddf.round(2)
    #ddddf['inventory_to_assets']=ddddf['inventory_to_assets'].round(3)
    #import numerize
    #for i,j in ddddf.iterrows():
    #    j['date']=j['date'].replace(str(j['date']),str(j['date'])+'-5')
    #    j['inventory']=numerize.numerize(j['inventory'])
    #    j['inventory_to_assets']=float('{:,.3f}'.format(j['inventory_to_assets']))
        #print(j['inventory_to_assets'])
        
    for i,j in ddddf.iterrows():
        ddddf['Date'].loc[i]=str(ddddf['Date'].loc[i])[:4]
        ddddf['Inventory to assets'].loc[i]=float(str(ddddf['Inventory to assets'].loc[i])[:6])
    
    #print(ddddf['date'])
    print(tickers_list)
    
    ddddf['Sector']=ddddf['Sector'].fillna('Others')
    ddddf['Subsector']=ddddf['Subsector'].fillna('Others')

    treemap1 = px.treemap(ddddf[~ddddf.Ticker.isin(tickers_list)],
                          path=[px.Constant('all sectors'), 'Sector', 'Subsector', 'Ticker', 'Date',vol_column],
                          values=vol_column,
                          color=col_column, hover_name='Name', color_continuous_scale='RdYlGn_r')
    treemap2 = px.treemap(ddddf[~ddddf.Ticker.isin(tickers_list)],
                          path=[px.Constant('all sectors'), 'Sector', 'Subsector', 'Ticker', 'Date',vol_column],
                          values='Total assets',
                          color=col_column, hover_name='Name', color_continuous_scale='RdYlGn_r')

    treemap1.update_layout(plot_style_treemap())
    #treemap1.update_coloraxes(colorbar_tickformat='$')
    treemap1.update_traces(hovertemplate='.')
    treemap2.update_layout(plot_style())
    #treemap2.update_coloraxes(colorbar_tickformat='$')
    

    return treemap1, treemap2


# Bar figures for Comparison

@app.callback(
    Output(component_id='bar_columns1', component_property='figure'),
    #Input(component_id='bar_columns_period', component_property='value'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='bar_columns_tickers', component_property='value'),
    Input(component_id='bar_columns_columns', component_property='value'),
)
def update_bar_columns( tickinitial, tickcompare, cols):
    tickers_list = [tickinitial,tickcompare]

    df = df_annual_formated

    columns_list = cols
    
    for i in range(len(cols)):
        cols[i]=cols[i]+' ($ Millions)'

    df_melt = pd.melt(df, id_vars=['Date_formated', 'Ticker'])

    df_melt_cols = df_melt[df_melt.variable.isin(columns_list)]

    df_melt_cols_ticks = df_melt_cols[df_melt_cols.Ticker.isin(tickers_list)]

    col11 = px.bar(df_melt_cols_ticks, y='value', color='variable',x='Date_formated',
                         height=600, width=1000,text_auto=True,
                          labels={
                                      "value":"Amount ($ Millions)",
                                      "variable":" ",
                                      "Date_formated": ""
                                 },
                         color_discrete_sequence=px.colors.qualitative.D3,
                        barmode="group", facet_row="Ticker", #custom_data=['Date'],hover_name='name'
                         )
    
    col11.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    col11.update_annotations(font_size=32)
    
    col11.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    
    col11.update_xaxes(tickvals = list(df_melt_cols_ticks['Date_formated']))
    
    col11.update_traces(textangle=0)

    col11.update_layout({"bargap": 0.3, 'bargroupgap': 0.12})
    
    col11.update_layout(xaxis = dict(tickfont = dict(size=25)))
    
    col11.update_layout(font=dict(size=18))

    col11.update_layout(plot_style_blue())

    return col11


@app.callback(
    Output(component_id='induscomp1', component_property='figure'),
    Input(component_id='induscomp1_var', component_property='value'),
    Input(component_id='comp_general', component_property='value')
)
def av_indus(vari,tck):
    vari=vari+' ($ Millions)'
    sector=df_annual_formated2.loc[df_annual_formated2.index[df_annual_formated2['Ticker']==tck].tolist()[0],'Sector']
    df_industry=df_annual_formated2[df_annual_formated2['Sector']==sector]
    df_tck=df_annual_formated2[df_annual_formated2['Ticker']==tck]
    tck_list=set(df_industry['Ticker'])
    list_av=[]
    list_av_mod=[]
    list_tck_indus_av=[]
    list_date=[]
    
    
    
    
    for i in range(df_tck.shape[0]):
        list_av.append([])
        list_tck_indus_av.append('('+sector+')'+' Average')
        list_date.append(df_tck['Date'].iloc[i])
    #-----------------------------------------------------------------////////////////////////////////
    
    for tick in tck_list:
        if df_industry[df_industry['Ticker']==tick].shape[0] == df_tck.shape[0]:
            for i in range(df_tck.shape[0]):
                list_av[i].append(df_industry[df_industry['Ticker']==tick][vari].iloc[i])
                
    for i in range(len(list_av)):
        new_list = [item for item in list_av[i] if not(math.isnan(item)) == True]
        list_av_mod.append(int((sum(new_list)/len(new_list))))
        
    for i in range(df_tck.shape[0]):
        list_av_mod.append(df_tck[vari].iloc[i])
        list_tck_indus_av.append(tck)
        list_date.append(df_tck['Date'].iloc[i])    

     #-----------------------------------------------------------------////////////////////////////////
   
    
       
    df_plot=pd.DataFrame({str(vari):list_av_mod, 'Ticker':list_tck_indus_av, 'Date':list_date})
    
    #print(df_plot)
    
    fig_ind=px.line(df_plot, x="Date", y=vari, title=vari +' evolution',color='Ticker',
                    labels={
                                      "Date": ""
                                 },
                    text=vari,height=600)
    
    fig_ind.update_xaxes(tickvals = list(df_plot['Date']))
    fig_ind.update_traces(textposition='top center')
    
    fig_ind.update_layout(plot_style())
    fig_ind.update_layout(xaxis = dict(tickfont = dict(size=25)))
    fig_ind.update_layout(xaxis= {'tickformat': '%Y'})
    fig_ind.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    
    return fig_ind


@app.callback(
    Output(component_id='ratios1', component_property='figure'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='bar_columns_tickers', component_property='value')
)
def update_ratios1(t1,t2):
    tickers_list = [t1,t2]

    ratios1 = ratios.drop(['date2'], axis=1)

    ratios_melt = pd.melt(ratios, id_vars=['ticker', 'Date_formated'])

    ratios_melt_cols = ratios_melt[ratios_melt.variable.isin(['DIO', 'DPO', 'DSO'])]

    ratios_melt_cols_ticks = ratios_melt_cols[ratios_melt_cols.ticker.isin(tickers_list)].dropna()

    for tick in tickers_list:
        ratios_melt_cols_ticks.loc[ratios_melt_cols_ticks['ticker'] == tick, 'name'] = get_title(tick)

    ratios1_fig = px.bar(ratios_melt_cols_ticks, x="Date_formated", y="value",
                          height=600, width=1000, text_auto=True,
                         labels={
                              "value":"Number of days",
                              "variable":" ",
                              "Date_formated": ""
                         },
                         color="variable", color_discrete_sequence=px.colors.qualitative.D3,
                         barmode="group", facet_row="ticker", hover_name='name')
    
    ratios1_fig.update_xaxes(tickvals = list(ratios_melt_cols_ticks['Date_formated']))
    ratios1_fig.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    ratios1_fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    ratios1_fig.update_annotations(font_size=32)
    
    ratios1_fig.update_layout(xaxis = dict(tickfont = dict(size=25)))
    ratios1_fig.update_layout({"bargap": 0.3, 'bargroupgap': 0.12})
    ratios1_fig.update_traces(textangle=0)
    ratios1_fig.update_layout(font=dict(size=18))
    ratios1_fig.update_layout(plot_style())
    #ratios1_fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))
    #ratios1_fig.for_each_trace(lambda t: t.update(name=t.name.split("=")[1]))
    #ratios1_fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)


    return ratios1_fig


@app.callback(
    Output(component_id='ratios2', component_property='figure'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='bar_columns_tickers', component_property='value')
)
def update_ratios2(t1,t2):
    tickers_list = [t1,t2]

    ratios2 = ratios.drop(['date2'], axis=1)

    ratios_melt = pd.melt(ratios2, id_vars=['ticker', 'Date_formated'])

    #ratios_melt['Date_formated'] = pd.to_datetime(ratios_melt['Date_formated'])

    ratios_melt_cols = ratios_melt[ratios_melt.variable.isin(['InventoryTurnover', 'CCC'])]

    ratios_melt_cols_ticks = ratios_melt_cols[ratios_melt_cols.ticker.isin(tickers_list)].dropna()

    for tick in tickers_list:
        ratios_melt_cols_ticks.loc[ratios_melt_cols_ticks['ticker'] == tick, 'name'] = get_title(tick)

    ratios2_fig = px.bar(ratios_melt_cols_ticks, x="Date_formated", y="value", height=600, width=1000,
                         color="variable", color_discrete_sequence=px.colors.qualitative.D3,text_auto=True,
                         labels={
                              "value":"Number of days",
                              "variable":" ",
                              "Date_formated": ""
                         },
                         barmode="group", facet_row="ticker", hover_name='name')
    
    ratios2_fig.update_xaxes(tickvals = list(ratios_melt_cols_ticks['Date_formated']))
    
    ratios2_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    ratios2_fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    ratios2_fig.update_annotations(font_size=32)
    ratios2_fig.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    
    ratios2_fig.update_layout(xaxis = dict(tickfont = dict(size=25)))
    
    ratios2_fig.update_traces(textangle=0)

    ratios2_fig.update_layout(plot_style())

    return ratios2_fig


@app.callback(
    Output(component_id='ratios3', component_property='figure'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='bar_columns_tickers', component_property='value')
)
def update_ratios3(t1,t2):
    tickers_list = [t1,t2]

    ratios3 = ratios.drop(['date2'], axis=1)

    ratios_melt = pd.melt(ratios3, id_vars=['ticker', 'Date_formated'])

    ratios_melt_cols = ratios_melt[ratios_melt.variable.isin(['ROCE', 'ROIC'])]

    ratios_melt_cols_ticks = ratios_melt_cols[ratios_melt_cols.ticker.isin(tickers_list)].dropna()

    for tick in tickers_list:
        ratios_melt_cols_ticks.loc[ratios_melt_cols_ticks['ticker'] == tick, 'name'] = get_title(tick)

    ratios3_fig = px.bar(ratios_melt_cols_ticks, x="Date_formated", y="value", height=600, width=1000,
                         color="variable", color_discrete_sequence=px.colors.qualitative.D3,text_auto=True,
                         labels={
                              "value":"Ratio",
                              "variable":" ",
                              "Date_formated": ""
                         },
                         barmode="group", facet_row="ticker", hover_name='name')
    
    ratios3_fig.update_xaxes(tickvals = list(ratios_melt_cols_ticks['Date_formated']))
    
    ratios3_fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    ratios3_fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    ratios3_fig.update_annotations(font_size=32)
    ratios3_fig.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    
    ratios3_fig.update_layout(xaxis = dict(tickfont = dict(size=25)))
    
    ratios3_fig.update_traces(textangle=0)

    ratios3_fig.update_layout(plot_style())

    return ratios3_fig


# Scatter and bar figures combined

# @app.callback(
# Output(component_id='column_y', component_property='options'),
# Output(component_id='column_c', component_property='options'),
# Output(component_id='column_r', component_property='options'),
# Input(component_id='scatter_bar_ticker', component_property='value'),
# Input(component_id='scatter_bar_period', component_property='value')
# )

# def update_columns(tick, per):
#    ticker=tick
#
#    if per=='annual': df = df_annual[df_annual['ticker']==ticker]
#    if per=='quarterly': df = df_quartal[df_quartal['ticker']==ticker]

#    df = df[df.columns.difference(['name', 'currency', 'sector', 'subsector', 'date2',
#                                              'Unnamed: 0', 'latitude', 'longitude'])]

#    columns0 = list(df.columns)

#    del columns0[columns0.index('date')]
#    del columns0[columns0.index('ticker')]

#    df_melt = pd.melt(df, id_vars=['date', 'ticker'])
#    df_melt = df_melt.dropna()

#    columns1 = []

#    for col in columns0:
#        if (col in list(df_melt['variable'])): columns1.append(col)

#    column_options = [{'label':x, 'value':x} for x in columns1]

#    positive_columns = []

#    for col in columns0:
#        if (df[col] > 0.1).all(): positive_columns.append(col)

#    column_r_options = [{'label':x, 'value':x} for x in positive_columns]

#    return column_options, column_options, column_r_options

@app.callback(
    #Output(component_id='scatter_fig', component_property='figure'),
    #Output(component_id='bar_fig1', component_property='figure'),
    #Output(component_id='bar_fig3', component_property='figure'),
    Output(component_id='bar_fig4', component_property='figure'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='bar_focus_var', component_property='value'),
    #Input(component_id='scatter_bar_period', component_property='value'),
    #Input(component_id='column_y', component_property='value'),
    #Input(component_id='column_c', component_property='value'),
    #Input(component_id='column_r', component_property='value')
)
def update_scatter(tick,focus_var):#, column_name_y, column_name_c, column_name_r):
    ticker = tick
    
    for i in range(len(focus_var)):
        focus_var[i]=focus_var[i]+' ($ Millions)'

    #if per == 'annual': df = df_annual_formated[df_annual_formated['Ticker'] == ticker]
    #if per == 'quarterly': df = df_quartal_formated[df_quartal_formated['Ticker'] == ticker]

    df = df_annual_formated2_stand_year[df_annual_formated2_stand_year['Ticker'] == ticker]
    

    df_melt1=pd.melt(df, id_vars=['Ticker', 'Date_formated'])
    df11=df_melt1[df_melt1.variable.isin(['Total assets ($ Millions)', 'Total liabilities ($ Millions)'])]
    
    bar_fig1 = px.bar(df11,
                      height=500, y='value', color='variable',text_auto=True,
                      color_discrete_sequence=px.colors.qualitative.D3,
                      labels={
                          "value":"Amount ($ Millions)",
                          "variable":" ",
                          "Date_formated": ""
                     },
                      x='Date_formated', barmode="group", custom_data=['Date_formated'])

    bar_fig1.update_layout({"bargap": 0.3, 'bargroupgap': 0.12})
    bar_fig1.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    bar_fig1.update_traces(textangle=0)
    bar_fig1.update_layout(plot_style())
    bar_fig1.update_layout(xaxis = dict(tickfont = dict(size=25)))
    bar_fig1.update_xaxes(tickvals = list(df11['Date_formated']))
    
    df_melt1=pd.melt(df, id_vars=['Ticker', 'Date_formated'])
    df3=df_melt1[df_melt1.variable.isin(['Inventory ($ Millions)','Cash ($ Millions)'])]
    
    bar_fig3 = px.bar(df3,
                      height=500, y='value', color='variable',text_auto=True,
                      color_discrete_sequence=px.colors.qualitative.D3,
                      labels={
                          "value":"Amount ($ Millions)",
                          "variable":" ",
                          "Date_formated": ""
                     },
                      x='Date_formated', barmode="group", custom_data=['Date_formated'])

    bar_fig3.update_layout({"bargap": 0.3, 'bargroupgap': 0.12})
    bar_fig3.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    bar_fig3.update_traces(textangle=0)
    bar_fig3.update_layout(plot_style())
    bar_fig3.update_xaxes(tickvals = list(df3['Date_formated']))
    bar_fig3.update_layout(xaxis = dict(tickfont = dict(size=25)))
    
    df4=df_melt1[df_melt1.variable.isin(focus_var)]
    
    bar_fig4 = px.bar(df4,
                      height=600, y='value', color='variable',text_auto=True,
                      color_discrete_sequence=px.colors.qualitative.D3,
                      labels={
                          "Date_formated": "",
                          "value": "Amount ($ Millions)"
                     },
                      x='Date_formated', barmode="group", custom_data=['Date_formated'])

    bar_fig4.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    bar_fig4.update_traces(textangle=0)
    bar_fig4.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    bar_fig4.update_xaxes(tickvals = list(df4['Date_formated']))
    bar_fig4.update_layout(xaxis = dict(tickfont = dict(size=25)))
    bar_fig4.update_layout(plot_style())

    return bar_fig4 #bar_fig1, bar_fig3, 


@app.callback(
    Output(component_id='bar_days', component_property='figure'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='bar_columns_tickers', component_property='value'),
    Input(component_id='bar_days_var', component_property='value'),

)
def update_bar_days(t1,t2,focus_var):
    tickers_list = [t2,t1]

    ratios_melt = pd.melt(ratios_stand_year, id_vars=['ticker', 'Date_formated'])

    ratios_melt_cols = ratios_melt[ratios_melt.variable.isin(focus_var)]

    df5 = ratios_melt_cols[ratios_melt_cols.ticker.isin(tickers_list)].dropna()
    
    for tick in tickers_list:
        df5.loc[df5['ticker'] == tick, 'name'] = get_title(tick)
    
    bar_days = px.bar(df5,
                      height=1000, y='value', color='variable',text_auto=True,
                      color_discrete_sequence=px.colors.qualitative.D3,
                      labels={
                          "Date_formated": "",
                          "value": "Number of days"
                     },
                      x='Date_formated', facet_row="ticker", barmode="group", custom_data=['Date_formated'])

    bar_days.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    bar_days.update_traces(textangle=0)
    bar_days.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    bar_days.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    bar_days.update_annotations(font_size=32)
    bar_days.update_xaxes(tickvals = list(df5['Date_formated']))
    bar_days.update_layout(xaxis = dict(tickfont = dict(size=25)))
    bar_days.update_layout(plot_style_blue())

    return bar_days

@app.callback(
    Output(component_id='bar_ratio', component_property='figure'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='bar_columns_tickers', component_property='value'),
    Input(component_id='bar_ratio_var', component_property='value'),

)
def update_car_ratio(t1,t2,focus_var):
    
    tickers_list = [t2,t1]

    ratios_melt = pd.melt(ratios_stand_year, id_vars=['ticker', 'Date_formated'])

    ratios_melt_cols = ratios_melt[ratios_melt.variable.isin(focus_var)]

    df4 = ratios_melt_cols[ratios_melt_cols.ticker.isin(tickers_list)].dropna()
    
    for tick in tickers_list:
        df4.loc[df4['ticker'] == tick, 'name'] = get_title(tick)
    
    
    bar_ratio = px.bar(df4,
                      height=1000, y='value', color='variable',text_auto=True,
                      color_discrete_sequence=px.colors.qualitative.D3,
                      labels={
                          "Date_formated": "",
                          "value": "RATIO"
                     },
                      x='Date_formated', facet_row="ticker", barmode="group", custom_data=['Date_formated'])

    bar_ratio.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    bar_ratio.update_traces(textangle=0)
    bar_ratio.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    bar_ratio.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    bar_ratio.update_annotations(font_size=32)
    bar_ratio.update_xaxes(tickvals = list(df4['Date_formated']))
    bar_ratio.update_layout(xaxis = dict(tickfont = dict(size=25)))
    bar_ratio.update_layout(plot_style_blue())

    return bar_ratio

@app.callback(
    Output(component_id='bar_dol', component_property='figure'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='bar_columns_tickers', component_property='value'),
    Input(component_id='bar_dol_var', component_property='value'),

)
def update_bar_dol(t1,t2,focus_var):#, column_name_y, column_name_c, column_name_r):
    for i in range(len(focus_var)):
        focus_var[i]=focus_var[i]+' ($ Millions)'
    
    
    tickers_list = [t2,t1]

    df = df_annual_formated2_stand_year

    columns_list = focus_var

    df_melt = pd.melt(df, id_vars=['Date_formated', 'Ticker'])

    df_melt_cols = df_melt[df_melt.variable.isin(columns_list)]

    df4 = df_melt_cols[df_melt_cols.Ticker.isin(tickers_list)]
    
    
    bar_dol = px.bar(df4,
                      height=1000, y='value', color='variable',text_auto=True,
                      color_discrete_sequence=px.colors.qualitative.D3,
                      labels={
                          "Date_formated": "",
                          "value": "Amount ($ Millions)"
                     },
                      x='Date_formated',facet_row="Ticker", barmode="group", custom_data=['Date_formated'])

    bar_dol.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    bar_dol.update_traces(textangle=0)
    bar_dol.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    bar_dol.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    bar_dol.update_annotations(font_size=32)
    bar_dol.update_xaxes(tickvals = list(df4['Date_formated']))
    bar_dol.update_layout(xaxis = dict(tickfont = dict(size=25)))
    bar_dol.update_layout(plot_style_blue())

    return bar_dol



@app.callback(
    Output(component_id='bar_fig2', component_property='figure'),
    Input(component_id='comp_general', component_property='value'),
    Input(component_id='scatter_bar_period', component_property='value'),
    Input(component_id='bar_fig1', component_property='clickData')
)
def update_bar2(tick, per, clickData):
    ticker = tick

    if per == 'annual': df = df_annual[df_annual['ticker'] == ticker]
    if per == 'quarterly': df = df_quartal[df_quartal['ticker'] == ticker]

    df = df[df.columns.difference(['ticker', 'name', 'currency', 'sector', 'subsector', 'date2',
                                   'Unnamed: 0', 'latitude', 'longitude'])]

    df['date'] = pd.to_datetime(df['date'])

    df.set_index('date', inplace=True)

    cdate = df.index[0]
    if clickData: cdate = pd.to_datetime(clickData['points'][0]['customdata'][0])

    ser = df.loc[cdate, :].astype('float')

    bar_fig2 = px.bar(ser, height=600, title=get_title(ticker))
    bar_fig2.update_layout(plot_style())
    bar_fig2.update_traces(marker_color='rgb(254, 163, 27)')

    return bar_fig2


@app.callback(
    Output(component_id='debt_rev_fig', component_property='figure'),
    Output(component_id='debt_ebitda_fig', component_property='figure'),
    Output(component_id='wc_rev_fig', component_property='figure'),
    Output(component_id='wc_inv_fig', component_property='figure'),
    Input(component_id='scatters_ticker1', component_property='value')
)
def update_scatter_figures1(tick):
    ticker = tick

    df = df_annual_new[df_annual_new['ticker'] == ticker]

    df['date'] = pd.to_datetime(df['date'])

    df_dropna = df[['ebitda', 'inventory', 'totalRevenue', 'ticker',
                    'WorkingCapital', 'TotalDebt', 'date']].dropna()

    debt_rev_fig = px.scatter(df_dropna,
                              color='ebitda', size='inventory', size_max=50,
                              y='TotalDebt', x='totalRevenue',
                              color_continuous_scale='RdYlGn_r', hover_data=['date', 'ticker'],
                              title=get_title(ticker))
    debt_rev_fig.update_layout(plot_style())

    debt_ebitda_fig = px.scatter(df_dropna,
                                 color='WorkingCapital', size='totalRevenue', size_max=50,
                                 y='TotalDebt', x='ebitda', color_continuous_scale='RdYlGn_r',
                                 hover_data=['date', 'ticker'], title=get_title(ticker))
    debt_ebitda_fig.update_layout(plot_style())

    wc_rev_fig = px.scatter(df_dropna,
                            color='inventory', size='TotalDebt', size_max=50,
                            y='WorkingCapital', x='totalRevenue', color_continuous_scale='RdYlGn_r',
                            hover_data=['date', 'ticker'], title=get_title(ticker))
    wc_rev_fig.update_layout(plot_style())

    wc_inv_fig = px.scatter(df_dropna,
                            color='TotalDebt', size='totalRevenue', size_max=50,
                            y='WorkingCapital', x='inventory', color_continuous_scale='RdYlGn_r',
                            hover_data=['date', 'ticker'], title=get_title(ticker))
    wc_inv_fig.update_layout(plot_style())

    return debt_rev_fig, debt_ebitda_fig, wc_rev_fig, wc_inv_fig


@app.callback(
    Output(component_id='inv_rev_fig', component_property='figure'),
    Output(component_id='inv_cash_fig', component_property='figure'),
    Output(component_id='gross_pr_inv_fig', component_property='figure'),
    Output(component_id='gross_pr_rev_fig', component_property='figure'),
    Input(component_id='scatters_ticker2', component_property='value'),
    Input(component_id='scatters_period', component_property='value')
)
def update_scatter_figures2(tick, per):
    ticker = tick

    if per == 'annual': df = df_annual[df_annual['ticker'] == ticker]
    if per == 'quarterly': df = df_quartal[df_quartal['ticker'] == ticker]

    df['date'] = pd.to_datetime(df['date'])

    df_dropna = df[['cash', 'inventory', 'totalRevenue', 'grossProfit', 'date']].dropna()

    inv_rev_fig = px.scatter(df_dropna, color='cash',
                             size='grossProfit', size_max=50,
                             y='inventory', x='totalRevenue',
                             color_continuous_scale='RdYlGn_r', hover_data=['date'],
                             title=get_title(ticker))
    inv_rev_fig.update_layout(plot_style())

    inv_cash_fig = px.scatter(df_dropna, color='totalRevenue',
                              size='grossProfit', size_max=50,
                              y='inventory', x='cash',
                              color_continuous_scale='RdYlGn_r', hover_data=['date'],
                              title=get_title(ticker))
    inv_cash_fig.update_layout(plot_style())

    gross_pr_inv_fig = px.scatter(df_dropna, color='cash',
                                  size='totalRevenue', size_max=50,
                                  y='grossProfit', x='inventory',
                                  color_continuous_scale='RdYlGn_r', hover_data=['date'],
                                  title=get_title(ticker))
    gross_pr_inv_fig.update_layout(plot_style())

    gross_pr_rev_fig = px.scatter(df_dropna, color='inventory',
                                  size='cash', size_max=50,
                                  y='grossProfit', x='totalRevenue',
                                  color_continuous_scale='RdYlGn_r', hover_data=['date'],
                                  title=get_title(ticker))
    gross_pr_rev_fig.update_layout(plot_style())

    return inv_rev_fig, inv_cash_fig, gross_pr_inv_fig, gross_pr_rev_fig


@app.callback(
    Output(component_id='tcc1_scatter', component_property='figure'),
    Input(component_id='tcc1_ticker', component_property='value'),
    Input(component_id='tcc1_slider', component_property='value'),
    Input(component_id='tcc_amount', component_property='value'),
    Input(component_id='tcc1_radio', component_property='value'),
    Input(component_id='scatter_y_value', component_property='value'),
    Input(component_id='scatter_color_value', component_property='value'),
    Input(component_id='scatter_size_value', component_property='value'),
)
def update_tcc_scatter(tick, Lambda_slider, Lambda_amount, radio, y_value,color_value,size_value):
    ticker = tick
    
    y_value=y_value+' ($ Millions)'
    color_value=color_value+' ($ Millions)'
    size_value=size_value+' ($ Millions)'

    df0 = df_annual_new_formated2[df_annual_new_formated2['Ticker']==ticker]
       
    df1 = df0.copy()
    
    df0['TCC'] = 'Without Inventory Funding'

    df1['TCC'] = 'With Inventory funding'

    if radio=='pour':
        Lambda=Lambda_slider/100
        df1['TotalDebt ($ Millions)'] = df0['TotalDebt ($ Millions)'].mul(1-Lambda)
        df1['Interest expense ($ Millions)'] = df0['Interest expense ($ Millions)'].mul(1-Lambda)
        df1['Operating income ($ Millions)'] = df0['Operating income ($ Millions)'] - abs(df0['Interest expense ($ Millions)']).mul(Lambda)
        df1['ebitda ($ Millions)'] = df0['ebitda ($ Millions)'] - abs(df0['Interest expense ($ Millions)']).mul(Lambda)
        df1['Inventory ($ Millions)']=df0['Inventory ($ Millions)'].mul(1-Lambda)
        df1['Cash ($ Millions)']=df0['Cash ($ Millions)']+df0['Inventory ($ Millions)'].mul(Lambda)
    else:
        Lambda=Lambda_slider/100
        df1['TotalDebt ($ Millions)'] = df0['TotalDebt ($ Millions)'].mul(1-Lambda)
        df1['Interest expense ($ Millions)'] = df0['Interest expense ($ Millions)'].mul(1-Lambda)
        df1['Operating income ($ Millions)'] = df0['Operating income ($ Millions)'] - abs(df0['Interest expense ($ Millions)']).mul(Lambda)
        df1['ebitda ($ Millions)'] = df0['ebitda ($ Millions)'] - abs(df0['Interest expense ($ Millions)']).mul(Lambda)
        df1['Inventory ($ Millions)']=df0['Inventory ($ Millions)'].mul(1-Lambda)
        df1['Cash ($ Millions)']=df0['Cash ($ Millions)']+df0['Inventory ($ Millions)'].mul(Lambda)

    
    df = pd.concat([df0, df1], axis=0)
    
    df['Date_formated']=df['Date'].astype(str).str[0:4]
    
    df['Return on Capital'] = (df['Operating income ($ Millions)']
                                      - df['Interest expense ($ Millions)']).divide(df['Total stockholder equity ($ Millions)']
                                                                       + df['TotalDebt ($ Millions)'] - df['Cash ($ Millions)'])
                                                          
    tcc1_scatter = px.scatter(df, x='Date_formated', y=y_value,
                              labels={"Date_formated": ""}, 
                      facet_col='TCC', color=color_value, hover_name='Date_formated',
                      color_continuous_scale='plotly3_r', size=size_value, size_max=50)
    tcc1_scatter.update_layout(plot_style_blue())
    
    tcc1_scatter.update_xaxes(tickvals = list(df['Date_formated']))
    tcc1_scatter.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    tcc1_scatter.update_annotations(font_size=22)
  
    return tcc1_scatter


@app.callback(
    Output(component_id='tcc_ratio_fig', component_property='figure'),
    Input(component_id='tcc1_ticker', component_property='value'),
    Input(component_id='bar_ratio_var', component_property='value'),
    Input(component_id='tcc1_slider', component_property='value'),
    Input(component_id='tcc_amount', component_property='value'),
    Input(component_id='tcc1_radio', component_property='value')
    
)
def update_tcc_ratio_fig(tick,focus_var ,Lambda_slider, Lambda_amount,radio):

    '''if Lambda_slider>99:
        Lambda_slider=99'''
    
    tickers_list = [tick]
        
    my_palette ={'ebit_to_interestExpense': '#FFA41B', 'ebitda_to_interestExpense': '#4C71DD'}

    df0 = df_annual_new[df_annual_new.ticker.isin(tickers_list)]

    df1 = df0.copy()


    df0['TCC'] = 'Without Inventory Funding'

    df1['TCC'] = 'With Inventory Funding'
    
    # Calcul with funding amount -----------------------------------------------------------------------------
    
    if radio=='pour':
        Lambda=Lambda_slider/100
        df1['TotalDebt'] = np.where(df0['inventory'].mul(Lambda)>df0['TotalDebt'], df0['TotalDebt'].mul(0.1), df0['TotalDebt']-(df0['inventory'].mul(Lambda)))
        df1['interestExpense'] = np.where(df0['inventory'].mul(Lambda)>df0['TotalDebt'], df0['interestExpense'].mul(0.1), ((df0['TotalDebt']-(df0['inventory'].mul(Lambda))).div(df0['TotalDebt'])).mul(df0['interestExpense']))
        #df1['operatingIncome'] = np.where(df0['inventory'].mul(Lambda)>df0['TotalDebt'], df0['operatingIncome'] - abs(df0['interestExpense']).mul(0.1), df0['operatingIncome'] - abs(((df0['TotalDebt']-(df0['inventory'].mul(Lambda))).div(df0['TotalDebt'])).mul(df0['interestExpense'])))
        df1['operatingIncome'] = np.where(df0['inventory'].mul(Lambda)>df0['TotalDebt'], df0['operatingIncome'] - abs(df0['interestExpense']).mul(0.1), df0['operatingIncome'] - abs(df0['interestExpense']).mul(1-((df0['TotalDebt']-(df0['inventory'].mul(Lambda))).div(df0['TotalDebt']))))
        df1['ebitda'] = np.where(df0['inventory'].mul(Lambda)>df0['TotalDebt'], df0['ebitda'] - abs(df0['interestExpense']).mul(1-0.1), df0['ebitda'] - abs(((df0['TotalDebt']-(df0['inventory'].mul(Lambda))).div(df0['TotalDebt'])).mul(df0['interestExpense'])))
        df1['ebit'] = np.where(df0['inventory'].mul(Lambda)>df0['TotalDebt'], df0['ebit'] - abs(df0['interestExpense']).mul(1-0.1), df0['ebit'] - abs(df0['interestExpense']-(((df0['TotalDebt']-(df0['inventory'].mul(Lambda))).div(df0['TotalDebt'])).mul(df0['interestExpense']))))

    else:
        Lambda=Lambda_amount
        df1['TotalDebt'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory']))>df0['TotalDebt'], df0['TotalDebt'].mul(0.1), df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory']))))
        df1['interestExpense'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory']))>df0['TotalDebt'], df0['interestExpense'].mul(0.1), ((df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])))).div(df0['TotalDebt'])).mul(df0['interestExpense']))
        df1['operatingIncome'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory']))>df0['TotalDebt'], df0['operatingIncome'] - abs(df0['interestExpense']).mul(0.1), df0['operatingIncome'] - abs(df0['interestExpense']).mul(1-((df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])))).div(df0['TotalDebt']))))
        df1['ebitda'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory']))>df0['TotalDebt'], df0['ebitda'] - abs(df0['interestExpense']).mul(1-0.1), df0['ebitda'] - abs(((df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])))).div(df0['TotalDebt'])).mul(df0['interestExpense'])))
        df1['ebit'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory']))>df0['TotalDebt'], df0['ebit'] - abs(df0['interestExpense']).mul(1-0.1), df0['ebit'] - abs(df0['interestExpense']-(((df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])))).div(df0['TotalDebt'])).mul(df0['interestExpense']))))

        #df1['TotalDebt'] = df0['TotalDebt'].mul(1 - (Lambda*1000000)/(df0['inventory']))
        #df1['interestExpense'] = df0['interestExpense'].mul(1 - (Lambda*1000000)/(df0['inventory']))
        #df1['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul((Lambda*1000000)/(df0['inventory']))
        #df1['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul((Lambda*1000000)/(df0['inventory']))
        #df1['ebit'] = df0['ebit'] - abs(df0['interestExpense']).mul((Lambda*1000000)/(df0['inventory']))

    #-----------------------------------------------------------------------------------------------------------
    



    df = pd.concat([df0, df1], axis=0)
    
    df['Date_formated']=df['date'].astype(str).str[0:4]

    df_ratios = df[['ticker', 'Date_formated', 'TCC', 'name']]


    # Updated ratios --------------------------------------------------------------------------  
    
    df_ratios['EBIT to Interest Expense'] = df['ebit'].divide(abs(df['interestExpense']))
    df_ratios['EBITDA to Interest Expense'] = (df['operatingIncome']
                                              + df['depreciation']).divide(abs(df['interestExpense']))
    df_ratios['Return On Capital'] = (df['operatingIncome']
                                      - df['incomeTaxExpense']).divide(df['totalStockholderEquity']
                                                                       + df['TotalDebt'] - df['cash'])
    df_ratios['EBITDA to Revenue'] = (df['operatingIncome'] + df['depreciation']).divide(df['totalRevenue'])
    df_ratios['Free Operating Cash Flow to Total Debt'] = (df['operatingIncome'] + df['depreciation']
                                            - df['capitalExpenditures']).divide(df['TotalDebt'])
    df_ratios['Funds From Operations to Total Debt'] = (df['operatingIncome']
                                     + df['depreciation'] + df['SaleOfPPE']).divide(df['TotalDebt'])
    
    
     # ------------------------------------------------------------------------------------------
        
    df_ratios=df_ratios.round(4)

    ratios_melt = pd.melt(df_ratios, id_vars=['ticker', 'Date_formated', 'TCC', 'name'])

    ratios_melt_cols3 = ratios_melt[ratios_melt.variable.isin(focus_var)]
    
    tcc3_bar = px.bar(ratios_melt_cols3, x="Date_formated", y="value", 
                          facet_col='TCC', hover_name='name', height=600,text_auto=True,
                          labels={
                                  "value":"Ratio",
                                  "variable":" ",
                                  "Date_formated": ""
                             },
                          color="variable", color_discrete_sequence=px.colors.qualitative.D3,
                          barmode="group")


    tcc3_bar.update_layout({"bargap": 0.2, 'bargroupgap': 0.1})
    tcc3_bar.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    tcc3_bar.update_traces(textangle=0)
    tcc3_bar.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.1,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))

    tcc3_bar.update_xaxes(tickvals = list(ratios_melt_cols3['Date_formated']))
    tcc3_bar.update_layout(plot_style_blue())
    tcc3_bar.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    tcc3_bar.update_annotations(font_size=22)

    return tcc3_bar


@app.callback(
    Output(component_id='tcc_fin_fig', component_property='figure'),
    Input(component_id='tcc1_ticker', component_property='value'),
    Input(component_id='bar_fin_var', component_property='value'),
    Input(component_id='tcc1_slider', component_property='value'),
    Input(component_id='tcc_amount', component_property='value'),
    Input(component_id='tcc1_radio', component_property='value')
    
)
def update_tcc_fin_fig(tick,focus_var ,Lambda_slider, Lambda_amount,radio):
    if Lambda_slider>99:
        Lambda_slider=99

    tickers_list = [tick]

    focus_var=[focus_var]

    df0 = df_annual_new[df_annual_new.ticker.isin(tickers_list)]

    df1 = df0.copy()

    df2 = df0.copy()

    df0['TCC'] = 'Without Inventory Funding'

    df1['TCC'] = 'With Inventory Funding'

    # Calcul with funding amount -----------------------------------------------------------------------------

    df0['TotalDebt'] = df1['TotalDebt'].div(1000000)
    df0['interestExpense'] =df1['interestExpense'].div(1000000)
    df0['operatingIncome'] = df1['operatingIncome'].div(1000000)
    df0['ebitda'] =df1['ebitda'].div(1000000)
    df0['ebit'] =df1['ebit'].div(1000000)


    if radio=='pour':
        Lambda=Lambda_slider/100
        df1['TotalDebt'] = np.where(df0['inventory'].mul(Lambda/1000000)>df0['TotalDebt'], df0['TotalDebt'].mul(0.1), df0['TotalDebt']-(df0['inventory'].mul(Lambda/1000000)))
        df1['interestExpense'] = np.where(df0['inventory'].mul(Lambda/1000000)>df0['TotalDebt'], df0['interestExpense'].mul(0.1), ((df0['TotalDebt']-(df0['inventory'].mul(Lambda/1000000))).div(df0['TotalDebt'])).mul(df0['interestExpense']))
        df1['operatingIncome'] = np.where(df0['inventory'].mul(Lambda/1000000)>df0['TotalDebt'], df0['operatingIncome'] - abs(df0['interestExpense']).mul(0.1), df0['operatingIncome'] - abs(df0['interestExpense']).mul(1-((df0['TotalDebt']-(df0['inventory'].mul(Lambda/1000000))).div(df0['TotalDebt']))))
        df1['ebitda'] = np.where(df0['inventory'].mul(Lambda/1000000)>df0['TotalDebt'], df0['ebitda'] - abs(df0['interestExpense']).mul(1-0.1), df0['ebitda'] - abs(((df0['TotalDebt']-(df0['inventory'].mul(Lambda/1000000))).div(df0['TotalDebt'])).mul(df0['interestExpense'])))
        df1['ebit'] = np.where(df0['inventory'].mul(Lambda/1000000)>df0['TotalDebt'], df0['ebit'] - abs(df0['interestExpense']).mul(1-0.1), df0['ebit'] - abs(df0['interestExpense']-(((df0['TotalDebt']-(df0['inventory'].mul(Lambda/1000000))).div(df0['TotalDebt'])).mul(df0['interestExpense']))))

    else:
        Lambda=Lambda_amount
        df1['TotalDebt'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000)>df0['TotalDebt'], df0['TotalDebt'].mul(0.1), df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000)))
        df1['interestExpense'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000)>df0['TotalDebt'], df0['interestExpense'].mul(0.1), ((df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000))).div(df0['TotalDebt'])).mul(df0['interestExpense']))
        df1['operatingIncome'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000)>df0['TotalDebt'], df0['operatingIncome'] - abs(df0['interestExpense']).mul(0.1), df0['operatingIncome'] - abs(df0['interestExpense']).mul(1-((df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000))).div(df0['TotalDebt']))))
        df1['ebitda'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000)>df0['TotalDebt'], df0['ebitda'] - abs(df0['interestExpense']).mul(1-0.1), df0['ebitda'] - abs(((df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000))).div(df0['TotalDebt'])).mul(df0['interestExpense'])))
        df1['ebit'] = np.where(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000)>df0['TotalDebt'], df0['ebit'] - abs(df0['interestExpense']).mul(1-0.1), df0['ebit'] - abs(df0['interestExpense']-(((df0['TotalDebt']-(df0['inventory'].mul((Lambda*1000000)/(df0['inventory'])/1000000))).div(df0['TotalDebt'])).mul(df0['interestExpense']))))

        #df1['TotalDebt'] = df0['TotalDebt'].mul(1 - (Lambda*1000000)/(df0['inventory']))
        #df1['interestExpense'] = df0['interestExpense'].mul(1 - (Lambda*1000000)/(df0['inventory']))
        #df1['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul((Lambda*1000000)/(df0['inventory']))
        #df1['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul((Lambda*1000000)/(df0['inventory']))
        #df1['ebit'] = df0['ebit'] - abs(df0['interestExpense']).mul((Lambda*1000000)/(df0['inventory']))


    df1['TotalDebt']=df1['TotalDebt'].astype(int)
    df1['interestExpense']=df1['interestExpense'].astype(int)
    df1['operatingIncome']=df1['operatingIncome'].astype(int)
    df1['ebitda']=df1['ebitda'].astype(int)
    df1['ebit']=df1['ebit'].astype(int)

    df0['TotalDebt']=df0['TotalDebt'].astype(int)
    df0['interestExpense']=df0['interestExpense'].astype(int)
    df0['operatingIncome']=df0['operatingIncome'].astype(int)
    df0['ebitda']=df0['ebitda'].astype(int)
    df0['ebit']=df0['ebit'].astype(int)

    #-----------------------------------------------------------------------------------------------------------

    df = pd.concat([df0, df1], axis=0)

    df['Date_formated']=df['date'].astype(str).str[0:4]

    ratios_melt = pd.melt(df, id_vars=['ticker', 'Date_formated', 'TCC', 'name'])

    #df[focus_var[0]]=df[focus_var[0]].astype(int)

    ratios_melt_cols3 = ratios_melt[ratios_melt.variable.isin(focus_var)]

    tcc3_bar = px.bar(ratios_melt_cols3, x="Date_formated", y="value", 
                          facet_col='TCC', hover_name='name', height=600,text_auto=True,
                          labels={
                                          "value":"Amount ($ Millions)",
                                          "variable":" ",
                                          "Date_formated": ""
                                     },
                          color="variable", color_discrete_sequence=px.colors.qualitative.D3,
                          barmode="group")


    tcc3_bar.update_layout({"bargap": 0.2, 'bargroupgap': 0.1})

    tcc3_bar.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    tcc3_bar.update_traces(textangle=0)
    tcc3_bar.update_layout(showlegend=False)
    tcc3_bar.update_layout(plot_style_blue())
    tcc3_bar.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    tcc3_bar.update_annotations(font_size=22)

    return tcc3_bar


@app.callback(
    Output(component_id='tcc4_bar', component_property='figure'),
    Input(component_id='tcc1_ticker', component_property='value'),
    Input(component_id='tcc_comp_ticker', component_property='value'),
    Input(component_id='tcc1_slider', component_property='value')
)
def update_tcc_bar4(tick,tick_comp, Lambda_u):
    Lambda=Lambda_u/100
    tickers_list = [tick_comp,tick]
    
    my_palette2 ={'FreeOperCF_to_TotalDebt': '#FFA41B', 'FFO_to_TotalDebt': '#4C71DD'}

    df0 = df_annual_new[df_annual_new.ticker.isin(tickers_list)]

    df1 = df0.copy()

    df2 = df0.copy()

    df0['TCC'] = 'Without TCC'

    df1['TCC'] = 'With TCC'

    df1['TotalDebt'] = df0['TotalDebt'].mul(1 - Lambda)
    df1['interestExpense'] = df0['interestExpense'].mul(1 - Lambda)
    df1['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(Lambda)
    df1['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(Lambda)

    df2['TotalDebt'] = df0['TotalDebt'].mul(1 - 0.8)
    df2['interestExpense'] = df0['interestExpense'].mul(1 - 0.8)
    df2['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(0.8)
    df2['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(0.8)

    df = pd.concat([df0, df1], axis=0)

    df['date'] = pd.to_datetime(df['date'])

    df_ratios = df[['ticker', 'date', 'TCC', 'name']]
    df_ratios2 = df[['ticker', 'date']]

    # df = df[['ticker', 'date', 'interestExpense', 'TotalDebt', 'ebitda', 'operatingIncome']]

    df_ratios['FreeOperCF_to_TotalDebt'] = (df['operatingIncome'] + df['depreciation']
                                            - df['capitalExpenditures']).divide(df['TotalDebt'])
    df_ratios['FFO_to_TotalDebt'] = (df['operatingIncome']
                                     + df['depreciation'] + df['SaleOfPPE']).divide(df['TotalDebt'])

    df_ratios2['FreeOperCF_to_TotalDebt'] = (df2['operatingIncome'] + df2['depreciation']
                                             - df2['capitalExpenditures']).divide(df2['TotalDebt'])
    df_ratios2['FFO_to_TotalDebt'] = (df2['operatingIncome']
                                      + df2['depreciation'] + df2['SaleOfPPE']).divide(df2['TotalDebt'])

    tcc4_max = max(df_ratios2['FreeOperCF_to_TotalDebt'].max(),
                   df_ratios2['FFO_to_TotalDebt'].max())

    ratios_melt = pd.melt(df_ratios, id_vars=['ticker', 'date', 'TCC', 'name'])

    ratios_melt['date'] = pd.to_datetime(ratios_melt['date'])

    ratios_melt_cols4 = ratios_melt[ratios_melt.variable.isin(['FreeOperCF_to_TotalDebt', 'FFO_to_TotalDebt'])]

    if (Lambda < 0.8):
        tcc4_bar = px.bar(ratios_melt_cols4, x="date", y="value", facet_row='ticker',
                          facet_col='TCC', hover_name='name', height=600, width=1000,
                          color="variable", range_y=[-0.1 * tcc4_max, 1.1 * tcc4_max],
                          color_discrete_sequence=px.colors.qualitative.D3, barmode="group")
    else:
        tcc4_bar = px.bar(ratios_melt_cols4, x="date", y="value", facet_row='ticker',
                          facet_col='TCC', hover_name='name', height=600, width=1000,
                          color="variable", color_discrete_sequence=px.colors.qualitative.D3, barmode="group")

    tcc4_bar.update_layout({"bargap": 0.2, 'bargroupgap': 0.1})

    tcc4_bar.update_layout(plot_style())

    return tcc4_bar


@app.callback(
    Output(component_id='tcc5_bar', component_property='figure'),
    Input(component_id='tcc1_ticker', component_property='value'),
    Input(component_id='tcc_comp_ticker', component_property='value'),
    Input(component_id='tcc1_slider', component_property='value')
)
def update_tcc_bar5(tick,tick_comp, Lambda_u):
    Lambda=Lambda_u/100
    tickers_list = [tick_comp,tick]
    
    my_palette3 ={'Return_on_Capital': '#FFA41B', 'ebitda_to_Revenue': '#4C71DD'}

    df0 = df_annual_new[df_annual_new.ticker.isin(tickers_list)]

    df1 = df0.copy()

    df2 = df0.copy()

    df0['TCC'] = 'Without TCC'

    df1['TCC'] = 'With TCC'

    df1['TotalDebt'] = df0['TotalDebt'].mul(1 - Lambda)
    df1['interestExpense'] = df0['interestExpense'].mul(1 - Lambda)
    df1['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(Lambda)
    df1['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(Lambda)

    df = pd.concat([df0, df1], axis=0)

    df['date'] = pd.to_datetime(df['date'])

    df_ratios = df[['ticker', 'date', 'TCC', 'name']]

    # df = df[['ticker', 'date', 'interestExpense', 'TotalDebt', 'ebitda', 'operatingIncome']]

    df_ratios['Return_on_Capital'] = (df['operatingIncome']
                                      - df['incomeTaxExpense']).divide(df['totalStockholderEquity']
                                                                       + df['TotalDebt'] - df['cash'])
    df_ratios['ebitda_to_Revenue'] = (df['operatingIncome'] + df['depreciation']).divide(df['totalRevenue'])

    ratios_melt = pd.melt(df_ratios, id_vars=['ticker', 'date', 'TCC', 'name'])

    ratios_melt['date'] = pd.to_datetime(ratios_melt['date'])

    ratios_melt_cols5 = ratios_melt[ratios_melt.variable.isin(['Return_on_Capital', 'ebitda_to_Revenue'])]

    tcc5_bar = px.bar(ratios_melt_cols5, x="date", y="value", facet_row='ticker',
                      facet_col='TCC', hover_name='name', height=600, width=1000,
                      color="variable", color_discrete_sequence=px.colors.qualitative.D3, barmode="group")

    tcc5_bar.update_layout({"bargap": 0.2, 'bargroupgap': 0.1})

    tcc5_bar.update_layout(plot_style())

    return tcc5_bar

@app.callback(
    Output(component_id='tcc_inv_cash', component_property='figure'),
    Input(component_id='tcc1_ticker', component_property='value'),
    Input(component_id='tcc1_slider', component_property='value'),
    Input(component_id='tcc_amount', component_property='value'),
    Input(component_id='tcc1_radio', component_property='value')
    
)
def update_tcc_inv_cash(tick, Lambda_slider, Lambda_amount,radio):
    
    tickers_list = [tick]
        
    df0 = df_annual_new_formated2[df_annual_new_formated2.Ticker.isin(tickers_list)]
    
    df0['Date_formated']=df0['Date'].astype(str).str[0:4]
    
    df1 = df0.copy()

    df2 = df0.copy()

    df0['TCC'] = 'Without Inventory Funding'

    df1['TCC'] = 'With Inventory funding'
    
    if radio=='pour':
        Lambda=Lambda_slider/100
        df0['Cash ($ Millions) dsp']=df0['Cash ($ Millions)']
        df1['Cash ($ Millions) dsp']=df0['Cash ($ Millions)'].add(df0['Inventory ($ Millions)'].mul(Lambda))

        df0['Inventory ($ Millions) dsp']=df0['Inventory ($ Millions)']
        df1['Inventory ($ Millions) dsp']=df0['Inventory ($ Millions)'].mul(1-Lambda)
        
    else:
        Lambda=Lambda_amount
        df0['Cash ($ Millions) dsp']=df0['Cash ($ Millions)']
        df1['Cash ($ Millions) dsp']=df0['Cash ($ Millions)'].add(Lambda)

        df0['Inventory ($ Millions) dsp']=df0['Inventory ($ Millions)']
        df1['Inventory ($ Millions) dsp']=df0['Inventory ($ Millions)'].sub(Lambda)
        

    df = pd.concat([df0, df1], axis=0)

    #df['Date'] = pd.to_datetime(df['Date'])

    df_ratios = df[['Ticker', 'Date_formated', 'TCC', 'Name']]
    df_ratios2 = df[['Ticker', 'Date_formated']]

    df_ratios['Inventory ($ Millions)'] = df['Inventory ($ Millions) dsp']
    df_ratios['Cash ($ Millions)'] = df['Cash ($ Millions) dsp']

    ratios_melt = pd.melt(df_ratios, id_vars=['Ticker', 'Date_formated', 'TCC', 'Name'])

    ratios_melt['Date'] = pd.to_datetime(ratios_melt['Date_formated'])

    ratios_melt_cols3 = ratios_melt[ratios_melt.variable.isin(['Inventory ($ Millions)',
                                                               'Cash ($ Millions)'])]


    tcc3_bar = px.bar(ratios_melt_cols3, x="Date_formated", y="value", 
                      facet_col='TCC', hover_name='Name', height=600, 
                      labels={
                              "Date_formated": "",
                              "value": "Amount ($ Millions)"
                         }, text_auto=True,
                      color="variable", color_discrete_sequence=px.colors.qualitative.D3,
                      barmode="group")


    tcc3_bar.update_layout({"bargap": 0.2, 'bargroupgap': 0.1})
    
    tcc3_bar.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})
    tcc3_bar.update_traces(textangle=0)
    tcc3_bar.update_layout(legend=dict(
        orientation="h",
        title= None,
        yanchor="bottom",
        y=1.1,
        xanchor="right",
        x=1,
        font=dict(
            size=18,
            color="black"
        ),
    ))
    tcc3_bar.update_xaxes(tickvals = list(ratios_melt_cols3['Date_formated']))
    tcc3_bar.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    tcc3_bar.update_annotations(font_size=22)
    tcc3_bar.update_layout(plot_style_blue())

    return tcc3_bar


#//////////////////////////////////////////////////////////////////////////////////////


app.run_server(port=8000, debug=True, use_reloader=False)


#//////////////////////////////////////////////////////////////////////////////////////





#//////////////////////////////////////////////////////////////////////////////////////


# In[ ]:




