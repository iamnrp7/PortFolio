import streamlit as st

def main():
    st.title("My Portfolio")
    
    st.write("""
    ## About Me
    Hi, I'm [Your Name]! I'm passionate about [your interests or field].
    """)

    st.write("""
    ## Projects
    """)
    
    project_1 = {
        "title": "Project 1",
        "description": "Description of project 1.",
        "link": "https://project1link.com"
    }
    
    project_2 = {
        "title": "Project 2",
        "description": "Description of project 2.",
        "link": "https://project2link.com"
    }
    
    projects = [project_1, project_2]
    
    for project in projects:
        st.write(f"### [{project['title']}]({project['link']})")
        st.write(project['description'])
    
    st.write("""
    ## Contact Me
    Email: [your@email.com](mailto:your@email.com)
    """)
    
if __name__ == "__main__":
    main()
