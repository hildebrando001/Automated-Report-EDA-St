import streamlit as st


def main():
    """Exploratory Data Analysis(EDA) Application with Streamlit Component
    """
    menu = ["Home", "Pandas Profile", "Sweetviz", "About"]
    choice = st.sidebar.select("Menu", menu)

    if choice == "Pandas Profile":
        st.subheader("Automated EDA with Pandas")

    elif choice == "Sweetviz":
        st.subheader("Automated EDA with Sweetviz")

    elif choice == "About":
        st.subheader("About")

    else:
        st.subheader("Home")


if __main__ == '__main__':
    main()
