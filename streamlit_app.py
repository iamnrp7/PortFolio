import streamlit as st

def main():
    st.title("Nihar Prajapati's Portfolio")
    
    # Displaying your photo and social media icons in a horizontal layout
    col1, col2 = st.beta_columns([2, 1])
    with col1:
        st.image("my_pic.jpeg", use_column_width=True) 
        st.write("""
        ## About Me
        Digital Sage | Electronics and Communication Engineering Student 
        """)
    with col2:
        st.write("""
        [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/iamnrp7)
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nihar-prajapati/)
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/iamnrp7)
        [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/NiharRPrajapati)
        """)

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
