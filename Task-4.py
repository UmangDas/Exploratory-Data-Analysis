# %%
# Importing Libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# %%
# Loaded CSV File and stored it in data
# Displayed data in tabular form
# Displayed first 10 rows of data

data = pd.read_csv(r"C:\Users\anony\Desktop\CODING\JupyterNotebook\USvideos.csv")
data.head(10)

# %%
# Dropped duplicate rows
# Displayed shape of data

data = data.drop_duplicates()
data.shape

# %%
# Described data

data.describe()

# %%
# Information of data

data.info()

# %%
# Columns to be removed


columns_to_remove = ['thumbnail_link','description']
data = data.drop(columns = columns_to_remove)

# %%
# Information of data

data.info()

# %%
# Imported datetime 
# show first 3 rows

from datetime import datetime
import datetime
data['trending_date'] = data['trending_date'].apply(lambda x: datetime.datetime.strptime(x,'%y.%d.%m'))
data.head(3)

# %%
# Converted publish_time to datetime
# show first 2 rows

data['publish_time'] = pd.to_datetime(data['publish_time'])
data.head(2)

# %%
# Added publish_month, publish_day, publish_hour
# show first 2 rows

data['publish_month'] = data['publish_time'].dt.month
data['publish_day'] = data['publish_time'].dt.day
data['publish_hour'] = data['publish_time'].dt.hour
data.head(2)

# %%
# Sorted unique values of category_id

print(sorted(data['category_id'].unique()))
[1,2,10,15,17,19,20,222,23,24,25,26,27,28,29,30,43]

# %%
# Added category_name
# Show first 5 rows

data['category_name'] = np.nan
data.loc[(data['category_id'] == 1), 'category_name'] = 'Film & Animation'
data.loc[(data['category_id'] == 2), 'category_name'] = 'Autos & Vehicles'
data.loc[(data['category_id'] == 10), 'category_name'] = 'Music'
data.loc[(data['category_id'] == 15), 'category_name'] = 'Pets & Animals'
data.loc[(data['category_id'] == 17), 'category_name'] = 'Sports'
data.loc[(data['category_id'] == 19), 'category_name'] = 'Travel & Events'
data.loc[(data['category_id'] == 20), 'category_name'] = 'Gaming'
data.loc[(data['category_id'] == 22), 'category_name'] = 'People & Blogs'
data.loc[(data['category_id'] == 23), 'category_name'] = 'Comedy'
data.loc[(data['category_id'] == 24), 'category_name'] = 'Entertainment'
data.loc[(data['category_id'] == 25), 'category_name'] = 'News & Politics'
data.loc[(data['category_id'] == 26), 'category_name'] = 'How to & Style'
data.loc[(data['category_id'] == 27), 'category_name'] = 'Education'
data.loc[(data['category_id'] == 28), 'category_name'] = 'Science & Technology'
data.loc[(data['category_id'] == 29), 'category_name'] = 'Non profits & Activism'
data.loc[(data['category_id'] == 30), 'category_name'] = 'Movies'
data.loc[(data['category_id'] == 43), 'category_name'] = 'Shows'

data.head()

# %%
data['year'] = data['publish_time'].dt.year
yearly_counts = data.groupby('year')['video_id'].count()

# create a bar chart
yearly_counts.plot(kind='bar', xlabel='year', ylabel='Total publish Count', title='Total publish videos per year')

# display the chart
plt.show()


# %%
yearly_views = data.groupby('year')['views'].sum()

# create a bar chart

yearly_views.plot(kind='bar', xlabel='year', ylabel='Total Views', title='Total views per year')
plt.xticks(rotation=0)
plt.tight_layout()

# display the chart 
plt.show()

# %%
# group the data by 'category_name' and calculate the sum of 'views' for each category

category_views = data.groupby('category_name')['views'].sum().reset_index()

# Sort the categories by 'views' in descending order

top_categories = category_views.sort_values(by='views', ascending=False).head(5)

# create a bar plot to visualize the top 5 categories

plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel('category Name', fontsize=12)
plt.ylabel('Total Views', fontsize=12)
plt.title('Top 5 categories with highest total views', fontsize=15)
plt.tight_layout()
plt.show()

# %%
# count the number of videos per category

plt.figure(figsize=(12, 6))
sns.countplot(x= 'category_name', data = data, order =data['category_name'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Views count by category')
plt.show()

# %%
# counr the number of videos published per hour

videos_per_hour = data['publish_hour'].value_counts().sort_index()

# create a bar plot

plt.figure(figsize=(12, 6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, palette='rocket')

plt.title('Number of videos published per hour')
plt.xlabel('Hour of day')
plt.ylabel('Number of videos')
plt.xticks(rotation=45)
plt.show()

# %%
#  graph the number of videos published over time

data['publish_time'] = pd.to_datetime(data['publish_time'])
data['publish_date'] = data['publish_time'].dt.date
video_count_by_data = data.groupby('publish_date').size()
plt.figure(figsize=(12, 6))
sns.lineplot(data=video_count_by_data)
plt.title('videos Publish Over Time')
plt.xlabel('Publish Date')
plt.ylabel('Number of videos')
plt.xticks(rotation=45)
plt.show()

# %%
# scatter plot bewteen 'views' and 'likes'

sns.scatterplot(data=data, x= 'views', y= 'likes')
plt.title('Views VS Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()

# %%
# Showed comments disabled and ratings disabled and video error or removed in the dataset

plt.figure(figsize=(14, 8))
plt.subplots_adjust(wspace = 0.2, hspace = 0.4, top = 0.9)
plt.subplot(2,2,1)
g = sns.countplot(x='comments_disabled', data=data)
g.set_title('Comments Disabled', fontsize = 16)
plt.subplot(2,2,2)
g1 = sns.countplot(x='ratings_disabled', data=data)
g1.set_title('Ratings Disabled', fontsize = 16)
plt.subplot(2,2,3)
g2 = sns.countplot(x='video_error_or_removed', data=data)
g2.set_title('Video Error or Removed', fontsize = 16)
plt.show()

# %%
# correlation between 'views' and 'likes'

corr_matrix = data['views'].corr(data['likes'])
corr_matrix



