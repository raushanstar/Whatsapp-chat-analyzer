# import streamlit as st
# import preprocessor , helper
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.sidebar.title('Whatsapp chat analyzer')
# uploaded_file = st.sidebar.file_uploader("Choose a file")
# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     data=bytes_data.decode('utf-8')
#     df=preprocessor.preprocessor(data)
#     #fetch user name
#     user_list=df['user'].unique().tolist()
#     user_list.remove('group_notification')
#     user_list.sort()
#     user_list.insert(0,"overall")
#     selected_user=st.sidebar.selectbox("Show analysis wrt ",user_list)
#     if st.sidebar.button('show analysis'):
#         user, num_message,total_words,no_of_media,links=helper.fetch(selected_user,df)
#         col1,col2,col3,col4,col5=st.columns(5)
#         with col1:
#             st.header('Total User')
#             st.title(user)
#         with col2:
#             st.header('Total Message')
#             st.title(num_message)
#         with col3:
#             st.header('Total Words')
#             st.title(total_words)
#         with col4:
#             st.header('Total Media')
#             st.title(no_of_media)
#         with col5:
#             st.header('Total Links')
#             st.title(links)
#         #timeline
#         st.title('Monthly timeline')
#         timeline=helper.monthly_timeline(selected_user,df)
#         fig,ax=plt.subplots()
#         ax.plot(timeline['time'], timeline['message'],color='red')
#         plt.xticks(rotation='vertical')
#         st.pyplot(fig)
#         #activity_map
#         st.title('Activity Map')
#         col1,col2=st.columns(2)
#         with col1:
#             st.header('Most busy day')
#             busy_day=helper.week_activity_map(selected_user,df)
#             fig,ax=plt.subplots()
#             ax.bar(busy_day.index,busy_day.values,color='purple')
#             plt.xticks(rotation='vertical')
#             st.pyplot(fig)
#         with col2:
#             st.header('Most busy month')
#             busy_month=helper.month_activity_map(selected_user,df)
#             fig,ax=plt.subplots()
#             ax.bar(busy_month.index,busy_month.values,color='orange')
#             plt.xticks(rotation='vertical')
#             st.pyplot(fig)
# # heatmap
#         st.title('Weekly activity map')
#         user_heatmap=helper.activity_heatmap(selected_user,df)
#         fig,ax=plt.subplots()
#         ax=sns.heatmap(user_heatmap)
#         st.pyplot(fig)

#         #bar chart of most busy user
#         if selected_user=='overall':

#             x,all_percent=helper.most_busy_users(df)
#             fig,ax=plt.subplots()


#             col1,col2=st.columns(2)
#             with col1:
#                 st.title('Most Busy user')
#                 ax.bar(x.index, x.values,color='red')
#                 plt.xticks(rotation='vertical')
#                 st.pyplot(fig)
#             with col2:
#                 st.title('users percent')
#                 st.dataframe(all_percent)
#         #wordcloud
#         st.title('Wordcloud')
#         df_wc=helper.create_wordcloud(selected_user,df)
#         fig,ax=plt.subplots()
#         ax.imshow(df_wc)
#         st.pyplot(fig)
#         #most_common_word
#         st.title('Most common word')
#         most_common_word=helper.most_common_word(selected_user,df)
#         st.dataframe(most_common_word)
#         #emoji
#         st.title('Total emoji')
#         emoji_df=helper.emoji_count(selected_user,df)
#         col1,col2=st.columns(2)
#         with col1:
#             st.dataframe(emoji_df)
#         with col2:
#             fig,ax=plt.subplots()
#             ax.pie(emoji_df[1],labels=emoji_df[0],autopct="%0.2f")
#             st.pyplot(fig)

















import streamlit as st
import preprocessor , helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title('Whatsapp chat analyzer')
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=preprocessor.preprocessor(data)
    #fetch user name
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"overall")
    selected_user=st.sidebar.selectbox("Show analysis wrt ",user_list)
    if st.sidebar.button('show analysis'):
        user, num_message,total_words,no_of_media,links=helper.fetch(selected_user,df)
        col1,col2,col3,col4,col5=st.columns(5)
        with col1:
            st.header('Total User')
            st.title(user)
        with col2:
            st.header('Total Message')
            st.title(num_message)
        with col3:
            st.header('Total Words')
            st.title(total_words)
        with col4:
            st.header('Total Media')
            st.title(no_of_media)
        with col5:
            st.header('Total Links')
            st.title(links)
        #timeline
        st.title('Monthly timeline')
        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        #activity_map
        st.title('Activity Map')
        col1,col2=st.columns(2)
        with col1:
            st.header('Most busy day')
            busy_day=helper.week_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header('Most busy month')
            busy_month=helper.month_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_month.index,busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
# heatmap
        st.title('Weekly activity map')
        user_heatmap=helper.activity_heatmap(selected_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(user_heatmap)
        st.pyplot(fig)

        #bar chart of most busy user
        if selected_user=='overall':

            x,all_percent=helper.most_busy_users(df)
            fig,ax=plt.subplots()


            col1,col2=st.columns(2)
            with col1:
                st.title('Most Busy user')
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.title('users percent')
                st.dataframe(all_percent)
        #wordcloud
        st.title('Wordcloud')
        df_wc=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
        #most_common_word
        st.title('Most common word')
        most_common_word=helper.most_common_word(selected_user,df)
        st.dataframe(most_common_word)
        #emoji
        st.title('Total emoji')
        emoji_df=helper.emoji_count(selected_user,df)
        col1,col2=st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax=plt.subplots()
            ax.pie(emoji_df[1],labels=emoji_df[0],autopct="%0.2f")
            st.pyplot(fig)
