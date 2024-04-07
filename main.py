from langchain_helper import get_few_shot_db_chain
import streamlit as st

st.markdown("<h2 style='text-align: center;'>TeeVogue T-Shirts: Stock Inquiry Desk</h2>", unsafe_allow_html=True)

# Brief information about TeeVogue shop
st.markdown("""
When searching for queries, make sure to include keywords related to stock availability, such as brand names like Van Huesen, Levi, Nike and Adidas. Color options including Red, Blue, Black and White with sizes ranging from XS to XL and price ranges from 1000 to 5000 rupees. You can also search for discounts to further refine your inventory management. By incorporating these keywords, you'll effectively monitor your stock and make informed decisions to optimize your inventory.
""")

question = st.text_input("Ask a Question:")

# Centering the Submit button
col1, col2, col3 = st.columns([8, 10, 1])
with col2:
    submit_button = st.button("Submit", key="submit_button")

if submit_button:
    if question:
        chain = get_few_shot_db_chain()
        answer = chain.run(question)
        st.header("Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")

# Adding space to align the footer
st.write("<div style='margin-top: px'></div>", unsafe_allow_html=True)

# Add a centered footer
st.markdown("---", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developed by Human Intelligence, utilizing the power of Artificial Intelligence (LLM).</p>", unsafe_allow_html=True)
