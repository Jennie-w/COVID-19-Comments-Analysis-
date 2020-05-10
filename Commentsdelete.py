import praw
from praw.models import MoreComments
from datetime import datetime
import csv
import re
from stop_words import get_stop_words
import nltk
import re

reddit = praw.Reddit(client_id='5wOmJrlqfM9TgA', client_secret='YOgwS4ImA6kt1IF-gf0L-Alzn2Q', user_agent='wangxinyi')
submission = reddit.submission(url="https://www.reddit.com/r/worldnews/comments/fpj9km/united_states_surpasses_china_in_coronavirus/")
submission.comments.replace_more(limit=0)

result = {}
headers = ['id', 'date', 'comment', 'parent_id']

word_dict = {}
word_re = re.compile(r'[\w]+')

stop_words = get_stop_words('english')
content_append = ''


with open('test.csv', 'w')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        # print(top_level_comment)
        _date = datetime.fromtimestamp(top_level_comment.created_utc)
        _date = _date.strftime('%Y-%m-%d')
        # print('{}, {} : [{}], {}'.format(top_level_comment.id, _date, top_level_comment.body, top_level_comment.parent_id))
        f_csv.writerow([top_level_comment.id, _date, top_level_comment.body, top_level_comment.parent_id])
        content_append += top_level_comment.body
        # words = word_re.findall(top_level_comment.body)
        # for word in words:
        #     if word in stop_words:
        #         continue
        #     if word not in word_dict:
        #         word_dict[word] = 1  # 从1为索引保存单词
        #     else:
        #         word_dict[word] += 1


pattern = re.compile('\W|https+')

tokens = nltk.wordpunct_tokenize(content_append)
finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)
# bigram_measures = nltk.collocations.BigramAssocMeasures()
finder.apply_word_filter(lambda x: pattern.match(x))
finder.apply_word_filter(lambda x: x in stop_words)
# finder.apply_ngram_filter(lambda w1,w2: w1 in [',', '.'] and w2 in [',', '.'] )
word_count_list = sorted(finder.ngram_fd.items(), key=lambda t: (-t[1], t[0]))[:100]
with open('word_count.csv', 'w')as f2:
    word_csv = csv.writer(f2)
    word_csv.writerow(['word', 'count'])
    for each in word_count_list:
        print('word <({})> appears {} times'.format(each[0], each[1]))
        word_csv.writerow([each[0], each[1]])









