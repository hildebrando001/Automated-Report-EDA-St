import streamlit as st
import pandas as pd
import codecs # Helps to load file
import streamlit.components.v1 as components # version 1

from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

import sweetviz as sv

# function that makes able to render a html file
def st_display_sweetviz(report_html, width=1000, height=500):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    components.html(page, width=width, height=height, sceolling=True)

def main():
    """Exploratory Data Analysis(EDA) Application with Streamlit Component
    """
    menu = ["Home", "Pandas Profile", "Sweetviz", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Pandas Profile":
        st.subheader("Simple Automated Exploratory Data Analysis")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())

            profile = ProfileReport(df)
            st_profile_report(profile)

    elif choice == "Sweetviz":
        st.subheader("Automated EDA with Sweetviz")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())

            # Normal Workflow
            report = sv.analyze(df)
            report.show_html()

    elif choice == "About":
        st.subheader("About")

    else:
        st.subheader("Home")
        html_temp = """
        <div style="background-color:royalblue;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">Simple EDA with Streamlit Components
        </div>
        """

        components.html(html_temp)



# It makes possible to know if a script is coming from an importation or 
# if it's coming from of the principal application
if __name__ == '__main__':
    main()
