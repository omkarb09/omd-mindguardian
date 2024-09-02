import streamlit as st
from streamlit_option_menu import option_menu
from chatbot import Chatbot

# Function to create new object of chatbot
def initialize_chatbot():
    st.session_state['chatbot'] = Chatbot()

# Function to clear chat memory by creating a new object of chatbot
def clear_chat_history():
    st.session_state.messages = []
    intro = '''Hello, I am Mindguardian, a mental health counseling chatbot designed to provide professional guidance and support. 
    My purpose is to offer a safe, non-judgmental, and empathetic space for you to explore your thoughts, feelings, and concerns. How can I help you today?'''
    st.session_state.messages.append({"role": "assistant", "content": intro})
    initialize_chatbot()  # Reinitialize the Chatbot instance

# Adding clear history button on sidebar
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

st.image("omdenaLogo.png",
        caption="Creating Impact through AI",
        width=240)

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home", "Problem Statement", "Goals and Outcomes", "Collaborators"],
        icons = ["house", "file-earmark", "list-check", "person-circle"],
        menu_icon = "cast"
    )

if selected == "Problem Statement":
    st.title("Problem Statement - MindGuardian")
    st.header("A Chatbot Companion for Gen Z Well-Being")
    st.subheader("Background")
    st.write("The rise of digital technology has revolutionised the way people interact,\
             work, and entertain themselves. Among the most affected demographic groups \
             are Generation Z (Gen Z), typically defined as individuals born between the \
             mid-1990s and early 2010s. This generation has grown up surrounded by \
             digital devices, such as smartphones, tablets, and computers, which have \
             become integral to their daily lives. According to a report by Amin et al. \
             (2020), Bangladesh has experienced a rapid increase in internet penetration, \
             with a significant portion of the population accessing the internet via \
             smartphones. This widespread availability of digital devices has led to \
             extensive use among young people, including Gen Z. In recent years, the \
             pervasive use of digital devices among Generation Z (Gen Z) has raised \
             concerns globally. Bangladesh, like many other countries, has witnessed \
             a surge in digital device addiction (DDA) among its young population. \
             This addiction has multifaceted repercussions, ranging from diminished \
             academic performance to compromised mental well-being. Understanding the \
             scope and consequences of DDA among Gen Z in Bangladesh is crucial for \
             devising effective intervention strategies.")
    st.divider()
    st.subheader("Problem")
    st.write("The COVID-19 pandemic has heightened levels of social isolation and \
             reliance on digital technologies for communication and entertainment.")
    st.write("Generation Z individuals in Bangladesh face significant challenges \
             related to depression and overwhelming digital device use. \
             Traditional mental health interventions may be inaccessible or \
             stigmatised, exacerbating the problem. Mihelič et el. (2023) explores \
             various factors contributing to cyberloafing behaviour among Generation Z \
             (Gen Z) students and suggests several solutions to address this issue. \
             There is a pressing need for innovative, accessible, and culturally sensitive \
             solutions to support the mental well-being of Gen Z in Bangladesh.")
    st.divider()

if selected == "Goals and Outcomes":
    st.title("Goals and Outcomes")
    st.header("Project Goals")
    st.markdown("- Develop comprehensive survey questionnaires to assess the perceptions, \
                experiences, and preferences of Gen Z individuals regarding depression, \
                digital device usage, and potential intervention strategies.")
    st.markdown("- Collect and analyse survey data to identify common themes, challenges, \
                and preferences related to mental health and digital device management among \
                Gen Z in Bangladesh.")
    st.markdown("- Utilise survey findings to inform the design and development of an \
                AI-powered chatbot tailored to address the specific needs and preferences \
                of Gen Z individuals in combating depression and device addiction.")
    st.markdown("- Implement and evaluate the effectiveness of the chatbot in providing \
                personalised support, guidance, and resources to Gen Z users, with a focus \
                on improving mental well-being and promoting healthier digital habits.")
    st.divider()
    st.header("Learning Outcomes")
    st.markdown("- Comprehensive survey questionnaires provide valuable insights into the \
                perceptions, experiences, and preferences of Gen Z individuals regarding \
                depression and device addiction in Bangladesh.")
    st.markdown("- Development and implementation of an AI-powered chatbot tailored to \
                address the specific needs and preferences of Gen Z users, with the \
                potential to provide accessible and personalized support for combating \
                depression and device addiction.")
    st.markdown("- Improved awareness, engagement, and utilisation of mental health \
                resources and support mechanisms among Gen Z individuals in Bangladesh,     \
                leading to enhanced mental well-being and healthier digital habits.")
    st.divider()

if selected == "Collaborators":
    st.title("Collaborators")
    st.html("./collaborators.html")

if selected == "Home":
    st.title("Mindguardian by Omdena")
    # Initialize chatbot object
    if "chatbot" not in st.session_state:
        st.session_state['chatbot'] = Chatbot()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        intro = '''Hello, I am Mindguardian, a mental health counseling chatbot designed to provide professional guidance and support. 
        My purpose is to offer a safe, non-judgmental, and empathetic space for you to explore your thoughts, feelings, and concerns. How can I help you today?'''
        st.session_state.messages.append({"role": "assistant", "content": intro})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Enter your query here"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        #print(prompt)
        response = st.session_state['chatbot'].run_chatbot(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})