import yfinance as yf
import streamlit as st
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Dashboard",
        page_icon="👋",
    )

    st.write("# Making money should be free 👋")

    st.sidebar.success("Select a tab above.")

    st.markdown(
        """
        samberubz2023invest is an open-source app built specifically for
        Stock Investing (NYSE, NASDAQ and TSX) and for the use of AI.
        **👈 Select a tab from the sidebar** to start investing!
        ### Want to fund this project?
        - You can reach out to me via Linkedin [Linkedin](www.linkedin.com/in/samuel-bérubé-21b1a0127)
        - 
        
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
