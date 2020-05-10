import praw
from praw.models import MoreComments
from datetime import datetime
import csv



reddit = praw.Reddit(client_id='5wOmJrlqfM9TgA', client_secret='YOgwS4ImA6kt1IF-gf0L-Alzn2Q', user_agent='wangxinyi')

# get 10 hot posts from the MachineLearning subreddit
#hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
#for post in hot_posts:
    #print(post.title)

#print(reddit.user.me())
submission = reddit.submission(url="https://www.reddit.com/r/worldnews/comments/fmeplj/confirmed_coronavirus_cases_are_growing_faster_in/")

# or 
#submission = reddit.submission(id="a3p0uq")

#for top_level_comment in submission.comments:
    #print(top_level_comment.body)

#submission
submission.comments.replace_more(limit=0)
#for top_level_comment in submission.comments:
#    print(top_level_comment.body)

result = {}
headers = ['date', 'comment']

top_level_comments = list(submission.comments)
all_comments = submission.comments.list()

with open('test.csv', 'w')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    for all_comments in submission.comments.list():
        if isinstance(all_comments, MoreComments):
            continue
        _date = datetime.fromtimestamp(all_comments.created_utc)
        _date = _date.strftime('%Y-%m-%d')
        print('{} : [{}]'.format(_date, all_comments.body))
        f_csv.writerow([_date, all_comments.body])
#     if _date in result and result.get(_date):
#         result[_date] = result.get(_date).append(top_level_comment.body)
#     else:
#         result[_date] = [top_level_comment.body]
#
# print(result)







