#This is the basic streamlit programs & commands that will be used most
#Use this to jog memory and remember the most important commands
#Not all commands are included but the most important ones are here
#These are the webpage designing commands for streamlit program

import streamlit as st

#Basic text types
st.header("Hello World")
st.subheader("Hello World")
st.text("Hello World")
st.caption("Hello World")

st.divider() #Creates a gap and a line (Divider)

st.markdown("Hello World *Hello World* **Hello World**") #Equivilant to text
st.caption("Hello World *Hello World* **Hello World**") #Directly format for caption

st.divider()

st.text_input("Input text!") #Create a text input with text
st.button("Click!") #Create a button with text
st.camera_input("Camera Input") #Adds an area with a camera input template
st.audio_input("Audio Input") #Adds sound recording bar template
st.file_uploader("Upload File area") #Adds file upload area template


st.chat_input("Input message") #Creates a Chat input template
st.text_area("Input Area") #Adds a text area with scroll

st.sidebar.write("Sidebar") #Adds a sidebar template on the left with the text Sidebar

st.divider()

column1, column2, column3 = st.columns(3) #Creates an area with 3 columns 
# the things in the front are variables that can be renamed

with column1:
    st.header("Hello World")
    st.button("Column 1 Button") #Put in column 1
with column2:
    st.header("Hello World")
    st.button("Column 2 Button") #Put in column 2
with column3:
    st.header("Hello World")
    st.button("Column 3 Button") #Put in column 3

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"]) #Create a tab template with 3 tabs named Tab 1, Tab2, and Tab 3

with tab1: #in 1
    st.divider()
    st.header("Tab 1 Input")
    st.divider()
with tab2: #in 2
    st.divider()
    st.header("Tab 2 Input")
    st.divider()
with tab3: #in 3
    st.divider()
    st.header("Tab 3 Input")
    st.divider()

with st.expander("Info Here:"): #Add an expander dropdown thingy that shows more text when pressed
    st.header("HELLO WORLD! *HELLO WORLD!* **HELLO WORLD!**")
    st.write("HELLO WORLD! *HELLO WORLD!* **HELLO WORLD!**") #write is pretty much text with format

st.video("https://www.youtube.com/watch?v=Qx8EEteoDdI", autoplay = False)
#Adds a video section on the website playing the video from the yt link added

#st.audio("", autoplay = False)
#Adds a sound audio section on the website playing the sound from link (In this case a random alarm sound from soundcloud)
#At the moment IT DOESNT WORK so its commented out. Figure out later

st.image("cat_stock.webp"
         , caption="Cat"
         , width="stretch")
#Adds an image section of the website with the image showing from the image through the relpath
