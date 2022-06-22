# streamlit app basic template with docker 
import streamlit as st

st.set_page_config(
     page_title="Linkedin",
     page_icon='✌️',
     layout="wide",
     initial_sidebar_state="expanded")


def main():
    st.write('Welcome to streamlit with docker')



if __name__ == '__main__':
    main()







