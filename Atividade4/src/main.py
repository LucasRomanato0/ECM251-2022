# Lucas Romanato de Oliveira
# RA: 20.00313-7

import time
from src.views.login import login_page
from src.views.home import home_page
import streamlit as st

if "state" in st.session_state:
    st.session_state["state"]
else:
    st.session_state["state"]=False

class Main():
    def __init__(self) -> None:
        if st.session_state["state"]:
            time.sleep(1)
            home_page()
        else:
            login_page(self)

app = Main()