__author__ = 'albertogonzalezpaje'


import pandas as pd


topics = pd.read_csv('topics.csv')
print topics[1:5]
posts_by_topic = pd.read_csv('post_by_topic.csv')
print posts_by_topic[1:5]

print len(topics)
print len(posts_by_topic)


topics_posts = pd.concat([topics, posts_by_topic], axis=1)
print topics_posts[1:10]
topics_posts.to_csv('topics_post.csv',encoding='utf-8',index=False)


