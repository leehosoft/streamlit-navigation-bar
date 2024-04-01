import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
from streamlit_option_menu import option_menu


st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Stock", "AI", "Game", "Examples", "Community", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "cubes.svg")
urls = {"GitHub": "https://github.com/gabrieltempass/streamlit-navigation-bar"}
styles = {
    "nav": {
        # "background-color": "royalblue",
        "background-color": "black",
        "secondary-background-color":"yellow",
        "text-color":"yello",
        "justify-content": "left",
    },
    "div": {
        "max-width": "32rem",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "color": "var(--text-color)",
        "background-color": "white",
        "font-weight": "normal",
        "padding": "14px",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    }
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    # urls=urls,
    styles=styles,
    # options=True,
    options={"show_sidebar": True},
)

functions = {
    "Home": pg.show_home,
    "Stock": pg.show_install,
    "AI": pg.show_user_guide,
    "Game": pg.show_api,
    "Examples": pg.show_examples,
    "Community": pg.show_community,
}
go_to = functions.get(page)
if go_to:
    go_to()

 
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

# 2. horizontal menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2 
    
# with st.sidebar:
#     tabs = on_hover_tabs(tabName=['Dashboard', 'Money', 'Economy'], 
#                          iconName=['dashboard', 'money', 'economy'], default_choice=0)

# if tabs =='Dashboard':
#     st.title("Navigation Bar")
#     st.write('Name of option is {}'.format(tabs))

# elif tabs == 'Money':
#     st.title("Paper")
#     st.write('Name of option is {}'.format(tabs))

# elif tabs == 'Economy':
#     st.title("Tom")
#     st.write('Name of option is {}'.format(tabs))    

# with st.sidebar:
#     st.write("Sidebar")    
