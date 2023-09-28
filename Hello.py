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
        What's up? Here is a new open-source app called samberubz2023invest. 
        It was built specifically for Stock Investing across three exchanges : NYSE, NASDAQ and TSX.
        
        **👈 Select a tab from the sidebar** to start investing!
        ### Want to fund this project?
        - You can reach out to me via Linkedin [Linkedin](www.linkedin.com/in/samuel-bérubé-21b1a0127)
        - You should talk about this app to other Stock Market enthusiasts !
        
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
