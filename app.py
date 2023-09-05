import streamlit as st
import preprocessor,helper
st.sidebar.title("whatsapp chat analyzer")

uploaded_file = st.sidebar.file_uploader("chose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    #convert bytecode to string
    data = bytes_data.decode("utf-8")
    #show data in screen
    #st.text(data)


    #using preprocessor.py function preprocess and passing data - gives dataframe
    df = preprocessor.preprocess(data)
    #to display datafrom in streamlit
    st.dataframe(df)

    #fetch unique user
    user_list = df['user'].unique().tolist()
    #remove group notifiction for group chats
    #user_list.remove("group_notification")
    user_list.sort()
    #adding overall word at first (oth position)- put position first and then data
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("show analysis with resoect to:", user_list)

    if st.sidebar.button("show analysis"):


        num_messages = helper.fetch_stats(selected_user,df)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Total messages")
            st.title(num_messages)