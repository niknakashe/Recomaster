import streamlit as st

# Background image styling
page_bg_img = '''
<style>
body {
background-image: url("https://your-background-image-link.jpg");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Page Title and Subtitle
st.title("About Us")
st.subheader("Diet Recommendations for Healthier Living")

# Introduction
st.write("""
In today's fast-paced world, people are increasingly focused on improving their health and lifestyle. However, simply avoiding junk food and exercising is not enough; a balanced diet is crucial for overall well-being. A diet tailored to one's height, weight, and age can help maintain a healthy weight, reduce the risk of chronic diseases like heart disease and cancer, and enhance overall health.
""")

# How It Works
st.subheader("How It Works")
st.write("""
We personalize meals by considering your:
- Diet Preferences (Vegetarian, Non-Vegetarian)
- Activity Level
- Nutritional Needs

Get meal plans that are nutritious, balanced, and delicious.
""")



