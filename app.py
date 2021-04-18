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
    components.html(page, width=width, height=height, scrolling=True)

def main():
    """Exploratory Data Analysis(EDA) Application with Streamlit Component
    """
    menu = ["Home", "Pandas Profile", "Sweetviz", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Pandas Profile":
        st.subheader("**Pandas Profile** - Automated EDA with Pandas Profile")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())

            profile = ProfileReport(df)
            st_profile_report(profile)

    elif choice == "Sweetviz":
        st.subheader("**Sweetviz** - Automated EDA with Sweetviz")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())
            if st.button("Generate Sweetviz Report"):
                # Normal Workflow
                report = sv.analyze(df)
                report.show_html('analyze.html', open_browser=False) # "custom name.html" in case you'd like to custom the report file name
                st_display_sweetviz("analyze.html")

            
    elif choice == "About":
        st.subheader("**About**")
        # components.iframe('https://google.com') # with iframe, it is possible to insert in a live frame
        html_temp = """
        <div style="background-color:#B1CDFF;padding:10px;border-radius:10px">
            <h3 style="color:#013187;text-align:center;font-family: Arial, Helvetica, sans-serif;">
                This Data App provides you two reports based on Pandas Profiling and Sweetviz libraries.
            </h3>
        </div>
        """
        components.html(html_temp)



    else:
        st.subheader("**Home**")

        html_temp = """
        <div style="background-color:#B1CDFF;padding:10px;border-radius:10px">
            <h3 style="color:#013187;text-align:center; font-family: Arial, Helvetica, sans-serif;">
                Simple Automated Exploratory Data Analysis (EDA)
            </h3>
        </div>
        """
        components.html(html_temp)

        

# It makes possible to know if a script is coming from an importation or 
# if it's coming from of the principal application
if __name__ == '__main__':
    main()
