from urlextract import  URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji
extractor=URLExtract()
def fetch(selected_user,df):
    if selected_user !='overall':
        df=df[df['user'] == selected_user]
    #no of user
    user=df['user'].unique().shape[0]
    total_messsage = df.shape[0]
    word = []
    for message in df['message']:
        word.extend(message.split())
    # for all media
    no_of_media=df[df['message']=='<Media omitted>\n'].shape[0]

    # link in message
    link = []
    for message in df['message']:
        link.extend(extractor.find_urls(message))

    return user, total_messsage,len(word),no_of_media ,len(link)

def most_busy_users(df):
    x=df['user'].value_counts()[:5]
    all_percent=round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Name', 'user': 'percent'})
    return x, all_percent
#wordcloud
def create_wordcloud(selected_user,df):
    if selected_user != 'overall':
        df=df[df['user']==selected_user]

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc=wc.generate(df['message'].str.cat(sep=" "))
    return df_wc
#most_common_word
def most_common_word(selected_user,df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_user != 'overall':
        df=df[df['user']==selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common=pd.DataFrame(Counter(words).most_common(20))
    return most_common
# emoji count
def emoji_count(selected_user,df):
    if selected_user != 'overall':
        df=df[df['user']==selected_user]
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])
    total_df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return total_df
#timeline
def monthly_timeline(selected_user,df):
    if selected_user != 'overall':
        df=df[df['user']==selected_user]
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(len(timeline)):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time
    return timeline

#activity map
def week_activity_map(selected_user,df):
    if selected_user != 'overall':
        df=df[df['user']==selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'overall':
        df=df[df['user']==selected_user]
    return df['month'].value_counts()
# heatmap
def activity_heatmap(selected_user,df):

    if selected_user != 'overall':
        df=df[df['user']==selected_user]

    user_heatmap= df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0)
    return user_heatmap