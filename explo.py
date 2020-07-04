import pandas as pd 
import json

PATH = '/Users/Tavo/code/FakeNewsCorpus/'

def load_data(path, chunksize):
    path = path + 'data/news_cleaned_2018_02_13.csv'
    corpus = pd.read_csv(path, chunksize=chunksize, index_col=0)

    # extract chunks
    for chunk in corpus:
        corpus = chunk.copy()
        break
    
    # save to dir
    corpus.to_csv(PATH + "data/dummy_news_dataset.csv")

    return

load_data(PATH, 1000)
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


