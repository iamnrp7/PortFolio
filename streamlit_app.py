import streamlit as st

def main():
    st.set_page_config(layout="wide")
    st.title("Nihar Prajapati's Portfolio")
    
    # Creating columns for layout
    col1, col2 = st.columns([1, 1])
    
    # Displaying your photo and social media icons in a horizontal layout
    with col1:
        st.image("my_pic.jpeg", width=200) 
        st.write("""
        ## About Me
        Digital Sage | Electronics and Communication Engineering Student 
        """)
        
    with col2:
        st.markdown("""
        <div style="margin-bottom: 10px;"><a href="https://www.instagram.com/iamnrp7" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" style="margin-right: 10px;"></a></div>
        <div style="margin-bottom: 10px;"><a href="https://www.linkedin.com/in/nihar-prajapati/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" style="margin-right: 10px;"></a></div>
        <div style="margin-bottom: 10px;"><a href="https://github.com/iamnrp7" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" style="margin-right: 10px;"></a></div>
        <div style="margin-bottom: 10px;"><a href="https://twitter.com/NiharRPrajapati" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter" style="margin-right: 10px;"></a></div>
        """, unsafe_allow_html=True)
    st.write("""
    ## Skills
    BUILDING
    """)

    st.write("""
    ## Education
    - B.Tech in Electronics and Communication Engineering, Pandit Deendayal Energy University (2023--Present), 
    - Class XII (CBSE), Green Valley : School for Children, Gandhinagar (2023), Percentage: 84.6%
    - Class X (CBSE), Shree Swaminarayan Public School, Gandhinagar (2020), Percentage: 89.8%
    """)

    st.write("""
    ## Experience
    BUILDING
    """)

    st.write("""
    ## Projects
    BUILDING
    """)

    st.write("""
    ## Achievements
    BUILDING
    """)

if __name__ == "__main__":
    main()
