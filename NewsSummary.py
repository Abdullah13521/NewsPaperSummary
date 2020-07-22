import newspaper
from tqdm import tqdm
import pandas as pd
import time

# list with the news papers you want to get articles from
newspapers = ['https://www.nytimes.com/', 'https://edition.cnn.com/', 'https://www.foxnews.com/', 'https://news.yahoo.com/',
             'https://www.nbcnews.com/', 'https://www.washingtonpost.com/']

titles = []
summaries = []

# loop through each news paper
for newpaper in tqdm(newspapers):
    paper = newspaper.build(newpaper)
    
    # loop through each article
    for article in tqdm(paper.articles):
        
        # check if there's an article exception error
        try:
            article.download()
            article.parse()
            article.nlp()
            titles.append(article.title)
            summaries.append(article.summary)
        except newspaper.article.ArticleException:
            continue

# check the lengths of both columns is the same
print(len(titles))
print(len(summaries))

# create a pandas data frame with titles and summaries
df = pd.DataFrame(list(zip(titles, summaries)), columns=['Title', 'Summary'])

# Add a new column for publishing date that depends on the given day
df['Publishing Date'] = time.strftime("%m/%d/%Y")

# remove the rows with empty summaries
df = df[df.Summary != '']

# export to a csv file
df_clean.to_csv('newsSummary.csv', index=False)
