
# coding: utf-8

# In[32]:
#Make a new empty dictionary.
w_freq = dict()

abhishika = open('Data')  #open a connection to the input file

for lines in abhishika:
    print(lines)


    lines=lines.strip() # the strip() function removes spaces, tabs, and 'line change'
    columns=lines.split('@') #delimeter
    name=columns[0] #fetch data
    day=columns[1]
    desc=columns[2]
    
    word=desc.split(' ')
    print(word)
    for w in word:
        if(w in w_freq):
            w_freq[w]=w_freq[w]+1 #increment the count by 1
        else:
            w_freq[w]=1 #initialize the word to count= 1

for w in w_freq:
    print(w,w_freq[w])
    
maxim=0
maxword = 'My'
for m in w_freq:
    if(w_freq[m]>maxim):
        maxim= w_freq[m]
        maxword=m
    else:
        continue
        
print(maxim)
print(maxword)


# In[ ]:




# In[ ]:




# In[ ]:



