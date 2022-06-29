# streamlit app basic template with docker 
import streamlit as st

st.set_page_config(
     page_title="Streamlit App",
     page_icon='✌️',
     layout="wide",
     initial_sidebar_state="expanded")


def main():
    st.write('Welcome to Streamlit in Docker')



if __name__ == '__main__':
    main()







