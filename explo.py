import pandas as pd 
import json

PATH = '/Users/tavo/code/dubio/'
KEEP_COLUMNS = ['id', 'title', 'content', 'url', 'scraped_at']

def load_data(path, chunksize):
    path = path + 'FakeNewsCorpus/news_cleaned_2018_02_13.csv'
    print(path)
    corpus = pd.read_csv(path, chunksize=chunksize, index_col=0)

    # extract chunks
    for chunk in corpus:
        corpus = chunk.copy()
        break
    
    # mis of reliable and unreliable
    corpus_nonreliable = corpus[corpus.type != 'reliable'].sample(400)
    corpus_reliable = corpus[corpus.type == 'reliable']
    corpus_all = pd.concat([corpus_nonreliable, corpus_reliable])

    # save to dir
    corpus_all.to_csv(PATH + "articles_dataset/data/dummy_news_dataset.csv")

    return corpus_all

def columns_as_schema(df, keep_columns):
    #change column names to make it consistent with current tables
    '''
    ArticleId binary(16) NOT NULL,  id
    Title varchar(255) NOT NULL,    title
	Content TEXT NOT NULL,          content
	SuspiciousIndex float NOT NULL, 
	UrgentIndex float NOT NULL,
	ReportCreated bit NOT NULL,
    '''

    '''
    ArticleId binary(16) NOT NULL,
	UserId binary(16) NOT NULL,
	Comments json,
	Links json,	
	Score int NOT NULL,                 textualRating, reviewRating
	CreationDate datetime NOT NULL,     reviewDate
    '''

    '''
    FakeNewsCorpus
    'id', 'domain', 'type', 'url', 'content', 'scraped_at', 'inserted_at',
       'updated_at', 'title', 'authors', 'keywords', 'meta_keywords',
       'meta_description', 'tags', 'summary', 'source'
    '''
    keep_columns = keep_columns
    new_names = ['ArticleId', 'Title', 'Content', 'Url', 'ScrapedAt']
    corpus = df.copy()
    corpus = corpus[keep_columns]
    corpus.columns = new_names
    corpus.to_csv(PATH + "articles_dataset/data/dummy_news_dataset_cols.csv")
    return corpus

def columns_as_claimreview():
    # change column names so they are consistent with the ClaimReview schema
    '''
    {
    "publisher": {
        object (Publisher)
    },
    "url": string,
    "title": string,
    "reviewDate": string,
    "textualRating": string,
    "languageCode": string
    }
    '''

    return



corpus = load_data(PATH, 10000)

corpus = columns_as_schema(corpus, KEEP_COLUMNS)


corpus.groupby('type').count()
corpus.head()

to_keep =  ['id', 'domain', 'type', 'url', 'content', 'scraped_at',
            'inserted_at', 'updated_at', 'title']
            ['articleId', 'articleDomain', 'articleTag', 'articleUrl', 
            'articleContent', 'scrapedAt',
            'insertedAt', 'updatedAt', 'articleTitle']
corpus = corpus[to_keep]


#### superintendent
!pip install superintendent
!jupyter nbextension enable --py --sys-prefix ipyevents

####
from superintendent import ClassLabeller
import pandas as pd
from IPython import display

labelling_widget = ClassLabeller(
    features=headlines,
    display_func=lambda x: display.display(display.Markdown("# " + x)),
    options=['professional', 'not professional'],
)

labelling_widget

################3





obj = corpus.to_json(orient='records')
jdata = json.loads(obj)

#for d in jdata:
#    for key, value in d.iteritems():
#        print key, value


# compare documents
from gensim.models import doc2vec
from scipy import spatial

# model file is the embedding trained with a dataset: 
# example: all our reviewed documents up to a certain date.
d2v_model = doc2vec.Doc2Vec.load(model_file)

# then you input two docuemnts that are 'sent' to that embedding to get a vector each
first_text = 'hello world'
second_text = 'hello many worlds'

vec1 = d2v_model.infer_vector(first_text.split())
vec2 = d2v_model.infer_vector(second_text.split())

# and we compre the vectors
similarity = spatial.distance.cosine(vec1, vec2)

# 


