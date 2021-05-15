from BackTranslation import BackTranslation
import pandas as pd

trans = BackTranslation(url=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

def backtranslate(text):
    try:
        result = trans.translate(text, src='en', tmp = 'fr')
        result = result.result_text
    except:
        result = '0'
    finally:
        return result

train = pd.read_csv('dataset.csv')
train = train.loc[:,['comment_text','toxic']]
train1 = train[train['toxic'] == 1]

vals = []

print(train1.shape)

k=0
for i,row in train1.iterrows():
    print(k)
    k+=1
    t = backtranslate(row['comment_text'])
    if len(t) > 1:
        vals.append(t)
    else:
        print("NO:",k)

df = pd.DataFrame(vals)
df.to_csv('data_backtranslated.csv', index=False)

# print(vals)