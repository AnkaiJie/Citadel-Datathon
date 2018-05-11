import pandas as pd
from sqlalchemy import create_engine

HOST = 'ec2-18-218-16-108.us-east-2.compute.amazonaws.com'
USERNAME = 'datathon'
PASSWORD = 'datathon'
DB = 'datathon'
url = 'postgresql://%s:%s@%s:5432/%s' % (USERNAME, PASSWORD, HOST, DB)
ENGINE = create_engine(url)


def df_qualities(df):
	print("Size %d" % df.shape[0])
	print(df.dtypes)

def get_create_table(tableName, path, keys=[], allString=False):
	textReader = pd.read_csv(path, chunksize=1000)
	df = None
	for chunk in textReader:
		df = chunk
		break
	df.columns = df.columns.str.lower()
	initial = pd.io.sql.get_schema(df, tableName, keys=keys)

	if allString:
		initial = initial.replace('INTEGER', 'text').replace('REAL','text')
	else:
		initial = initial.replace('INTEGER', 'int').replace('REAL','DECIMAL')
	print(',\n'.join(['NULLIF(' + a + ', \'\')' for a in list(df.columns)]))
	print(initial)
	return (df, initial)

def insert_data(path, tableName):
	textReader = pd.read_csv(path, chunksize=50000)
	df = None
	for chunk in textReader:
		chunk.to_sql(tableName, ENGINE, if_exists='replace')
	


path = 'datafest.csv'
tableName = 'datafest'
(dfchunk, initial) = get_create_table(tableName, path, keys=['date', 'companyid', 'jobid'], allString=False)

#insert_data(path, tableName)
