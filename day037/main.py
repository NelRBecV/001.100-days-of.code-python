import requests
import webbrowser
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

USERNAME = ""
U_TOKEN = ""
endpoint = "https://pixe.la/v1/users"
PIXELA_PARAMS = {"username":USERNAME,
                 "token":U_TOKEN,
                 "agreeTermsOfService":"yes",
                 "notMinor":"yes",

}

#see pixela's API docs page
endpoint_graph = f"{endpoint}/{USERNAME}/graphs"
head = {"X-USER-TOKEN": U_TOKEN}
my_graphs_id = "my-first-graph"
PIXELA_GRAPH_P = {
                  "id": my_graphs_id,
                  "name":"first-graph",
                  "unit":"meters",
                  "type":"float",
                  "color":"sora"}#'blue' in japanesse


my_graph = f"{endpoint_graph}/{my_graphs_id}"
current_date = datetime(day=1, month=4, year=2025)
date_activity = current_date.strftime('%Y%m%d')
#strftime accepts any other date separator you wanna use (i.e. .strftime('%Y-%m-%'))
quantity = "5"
activity = {
            'quantity':quantity
            }


my_graph_change = requests.delete(url=f"{my_graph}/{date_activity}", headers=head)
graph = webbrowser.open(f"{my_graph}.html")
