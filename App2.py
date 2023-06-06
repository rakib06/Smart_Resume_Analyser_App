import streamlit as st

# Title and header
st.title('My Streamlit App')
st.header('Welcome!')

# Add content to your app
st.write('This is a sample Streamlit app.')

# Add an interactive widget
name = st.text_input('Enter your name')
st.write(f'Hello, {name}!')

# Display a plot
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 5])
st.pyplot(plt)

# # Run the app
# if __name__ == '__main__':
#     st.run()
