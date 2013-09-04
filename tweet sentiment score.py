import json

data = []
score_dict = {}
sentiment_score = 0

#Note from looking at this months 
#after writing this: I clearly did 
#not truly understand the split method
# given the function below! Hah

def next_word(sentence): 
    space_spot = sentence.find(" ")
    if space_spot > -1:
        word = sentence[:space_spot]
        sentiment_score = sentiment_score + score_dict[word]
        next_word(sentence[space_spot+1:])
    else:
        word = sentence

with open('smalloutput.json') as f:
    for line in f:
        try:
            if json.loads(line)['lang'] == 'en':
                data.append(json.loads(line)['text'])
        
        except:
            pass

with open("AFINN-111.txt") as afinn:
    for line in afinn:
        term, score = line.split("\t") 
        score_dict[term] = int(score)
        
for item in data:
    next_word(item)
        


