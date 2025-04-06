import streamlit as st

# Alt + Shift + F to format the code
st.html(
    """<div style="text-align: center; margin-x: 20px; padding: 20px; border: 2px solid #0078D7; border-radius: 15px; background-color: #121212; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
    <h1 style="color: #66c2ff; font-family: 'Arial', sans-serif;">Welcome to My Unit Converter</h1>
</div>
"""
)
st.title("-<<Choose your units to convert>>-")

# Create four columns
col0, col1, col2, col3 = st.columns(4)

# Add content to the first column
with col0:
    st.header("Input")
    val = st.number_input('Enter the value to convert',)

# Add content to the second column
with col1:
    st.header("From")
    frm = st.selectbox("Select Unit From", ["Kilometer", "Meter", "Centimeter"])

# Add content to the third column
with col2:
    st.header("To")
    to = st.selectbox("Select Unit To", ["Meter", "Centimeter", "Kilometer"])

# Add content to the fourth column
with col3:
    st.header("Output")
    # Perform the unit conversion based on selection
    if to == "Kilometer" and frm == "Meter":
        output = val / 1000
    elif to == "Meter" and frm == "Kilometer":
        output = val * 1000
    elif to == "Centimeter" and frm == "Meter":
        output = val * 100
    elif to == "Meter" and frm == "Centimeter":
        output = val / 100
    elif to == "Kilometer" and frm == "Centimeter":
        output = val / 100000
    elif to == "Centimeter" and frm == "Kilometer":
        output = val * 100000
    elif to == frm :
        output = val
    else:
        output = None

    # Display the conversion output
    if output is not None:
        st.html("Conversion Output:"f"""
            <div style="background-color: rgb(38, 39, 48); height: 43px; width: 150px;  display: flex; align-items: center; justify-content: center; border-radius: 10px;">{output} {to}</div>
        """)
    else:
        st.write("Invalid conversion")

# Footer Section with Links
st.html(
    """
    <div style="text-align: center; margin-top: 30%; padding: 20px; border-top: 2px solid #0078D7; background-color: #121212; color: #66c2ff;">
        <p>Thank you for using the Unit Converter! 🌟</p>
        <p>Created by 𝔐𝔲𝔥𝔞𝔪𝔪𝔞𝔡 ͯś𝔲𝔥𝔞𝔦𝔟</p>
    </div>
    """
)
