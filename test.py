import pandas as pd
all_text=pd.read_csv("../test.csv",sep=';')
with open('all_text.txt','w') as f:
	for i in all_text['text']:
		f.write('\"')
		f.write(i)
		f.write('\"')
		f.write('\n')
