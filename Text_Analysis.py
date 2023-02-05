import pandas as pd
import nltk

from nltk.stem.snowball import SnowballStemmer
    
def nlp(text):
    
    
    excel_data=pd.read_excel(r'C:\Users\Ali\Desktop\data.xlsx')
    data = pd.DataFrame(excel_data, columns=['word_arabic', 'word_english',])

    x=data['word_arabic']
    #print(x)
    y=data['word_english']
    #print(y)

    test_str=nltk.word_tokenize(text)
    #if test_str[len(test_str)-1] != ".":
        #text=text + " ."
    #for the three words
    sentances = [sent for sent in test_str if sent.isalpha()] #normalization
    stem_sentence=[]
    s_stemmer = SnowballStemmer(language='arabic')
    for word in sentances:
        stem_sentence.append(s_stemmer.stem(word))
    "".join(stem_sentence)

    Stmming_Text = stem_sentence
    for i in range(len(Stmming_Text)):
        if Stmming_Text[i] == 'جاف':
            Stmming_Text[i] = Stmming_Text[i].replace('جاف', 'جافا')
        if Stmming_Text[i] == 'ايث':
            Stmming_Text[i] = Stmming_Text[i].replace('ايث', 'بايثون')
        if Stmming_Text[i] == 'اررا':
            Stmming_Text[i] = Stmming_Text[i].replace('اررا', 'ارراي')
        if Stmming_Text[i] == 'ورلوب':
            Stmming_Text[i] = Stmming_Text[i].replace('ورلوب', 'فورلوب')
        if Stmming_Text[i] == 'دات':
            Stmming_Text[i] = Stmming_Text[i].replace('دات', 'داتا')
        if Stmming_Text[i] == 'ديت':
            Stmming_Text[i] = Stmming_Text[i].replace('ديت', 'ديتا')
        if Stmming_Text[i] == 'ريبل':
            Stmming_Text[i] = Stmming_Text[i].replace('ريبل', 'فريبل')
        if Stmming_Text[i] == 'ربيل':
            Stmming_Text[i] = Stmming_Text[i].replace('ربيل', 'فربيل')
        if Stmming_Text[i] == 'دار':
            Stmming_Text[i] = Stmming_Text[i].replace('دار', 'دارت')
        if Stmming_Text[i] == 'ونستن':
            Stmming_Text[i] = Stmming_Text[i].replace('ونستن', 'كونستنت')
        if Stmming_Text[i] == 'ونستان':
            Stmming_Text[i] = Stmming_Text[i].replace('ونستان', 'كونستانت')
        if Stmming_Text[i] == 'اينر':
            Stmming_Text[i] = Stmming_Text[i].replace('اينر', 'باينري')
        if Stmming_Text[i] == 'فلو':
            Stmming_Text[i] = Stmming_Text[i].replace('فلو', 'فلوت')

    if Stmming_Text[len(Stmming_Text)-1] != ".":
        text=text + " ."

#for the three words
    result=[]
    for i in range(1,len(Stmming_Text)-1):
        data=''.join(Stmming_Text[t+i-1]+" " for t in range(3))
        result.append(data)
        #result.append(data.replace("ال",""))
        #result.append(data.replace("ل",""))
#print(result)
    
    if len(result)==1:
        for j in range(len(x)-1):
            r=str(x[j])+" "
            if r == str(result[0]) :
                text=text.replace(r,str(y[j]))
        
    for i in range(len(result)):
        for j in range(len(x)-1):
            r=str(x[j])
            if r ==str(result[i]) :
                text=text.replace(r,str(y[j])+" ")
#print(text)
  
    
    #for the two words
    
    result=[]
    for i in range(1,len(Stmming_Text)-1):
        data=''.join(Stmming_Text[t+i-1]+" " for t in range(2))
        result.append(data)
        #result.append(data.replace("ال",""))
     #result.append(data.replace("ل",""))
#print(result)
    
    if len(result)==1:
        for j in range(len(x)-1):
            r=str(x[j])+" "
            if r == str(result[0]) :
                text=text.replace(r,str(y[j]))
        
    for i in range(len(result)):
        for j in range(len(x)-1):
            r=str(x[j]) +" "
            if r ==str(result[i]) :
                text=text.replace(r,str(y[j])+" ")
    
     #for the one words
    
    result=[]
    for i in range(len(Stmming_Text)):
        data=''.join(Stmming_Text[t+i-1]+" " for t in range(1))
        result.append(data)
        #result.append(data.replace("ال",""))
        #result.append(data.replace("ل",""))
    print(result)
    
    if len(result)==1:
        for j in range(len(x)-1):
            r=str(x[j])+" "
            if r == str(result[0]) :
                text=text.replace(r,str(y[j]))
        
    for i in range(len(result)):
        for j in range(len(x)-1):
            r=str(x[j])+" "
            if r == str(result[i]) :
                text=text.replace(r,str(y[j])+" ")
                

    return(text)
    
nlp("أنا أحب بروقرام بايثون")