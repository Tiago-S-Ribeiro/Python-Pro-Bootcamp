import os

TOKEN = os.environ.get("TOKEN")
USER = os.environ.get("USER")
G_ID = os.environ.get("G_ID")

PXL_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PXL_ENDPOINT}/{USER}/graphs"
NEW_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{G_ID}"