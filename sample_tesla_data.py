import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(tesla_data, tesla_revenue, title="Tesla"):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    tesla_data_specific = tesla_data[tesla_data.Date <= '2021-06-14']
    tesla_revenue_specific = tesla_revenue[tesla_revenue.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(tesla_data_specific.Date, infer_datetime_format=True), y=tesla_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(tesla_revenue_specific.Date, infer_datetime_format=True), y=tesla_revenue_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=title,
    xaxis_rangeslider_visible=True)
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data2 = requests.request("GET", url=url).text

soup = BeautifulSoup(html_data2, 'html5lib')

table_body = soup.find_all("tbody")[1]
dates = []
revenues = []
for row in table_body.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace(',',"").replace('$',"")
        if revenue != '':  # skip empty entries
            dates.append(date)
            revenues.append(revenue)
gme_revenue = pd.DataFrame({"Date": dates, "Revenue": revenues})

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)


make_graph(tesla_data, gme_revenue, "TESLA")