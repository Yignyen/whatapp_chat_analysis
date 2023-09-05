import re
import pandas as pd
def preprocess(data):
    pattern = '\[\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{2}:\d{2}\]\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format="[%d/%m/%y, %H:%M:%S] ")

    df.rename(columns={'message_date': 'date'}, inplace=True)
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # separate users and msgs
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    # spliting the date into year
    df['year'] = df['date'].dt.year#to find months from number
    df['month'] = df['date'].dt.month_name()
    df['days'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['second'] = df['date'].dt.second

    return df