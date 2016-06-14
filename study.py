import datetime 
import pandas 

def hammer(x):
	body = x['Close'] - x['Open']
	tail = x['High'] - x['Low']
	return( x['High']==x['Close'] )
	

df = pandas.read_csv( 'nifty.csv' )
df['hammer'] = df.apply( hammer , axis=1 )
print len(df[ df['hammer'] ])
print (df[ df['hammer'] ])
