import pyspark
from pyspark.sql import SparkSession
from collections import Counter
from pyspark.sql.functions import col
from nltk.tokenize import WhitespaceTokenizer
# from org.apache.spark.sql.functions import col

tk = WhitespaceTokenizer()

spark = SparkSession.builder.appName("Word Count").getOrCreate()

df = spark.read.text("data/biographies.list")#, wholetext=False)#, lineSep='\n')
# df.filter(col(col_name).startswith("BG:"))

print(df.head())

col_name = 'CRC: 0x72F64CB3  File: biographies.list  Date: Sat Dec 19 00:00:00 2015'

words = []

counter = Counter(words)
print(counter.most_common(10))