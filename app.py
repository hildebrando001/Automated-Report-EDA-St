import streamlit as st
import pandas as pd
import codecs # Helps to load file
import streamlit.components.v1 as components # version 1

def main():
    """Exploratory Data Analysis(EDA) Application with Streamlit Component
    """
    menu = ["Home", "Pandas Profile", "Sweetviz", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Pandas Profile":
        st.subheader("Automated EDA with Pandas")

    elif choice == "Sweetviz":
        st.subheader("Automated EDA with Sweetviz")

    elif choice == "About":
        st.subheader("About")

    else:
        st.subheader("Home")
        components.html("<p style='color:red;'> Streamlit components is awosome. </p>")


# It makes possible to know if a script is coming from an importation or 
# if it's coming from of the principal application
if __name__ == '__main__':
    main()
