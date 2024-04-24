import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

# Initialize Spark session
spark = SparkSession.builder.appName("Word Count").getOrCreate()

# Define function to count words in a file
def count_words(file_path):
    # Read text file as DataFrame
    df = spark.read.text(file_path)

    # Tokenize words using whitespace tokenizer
    words_df = df.select(explode(split(df.value, "\s+")).alias("word"))

    # Count occurrences of each word
    word_counts = words_df.groupBy("word").count().orderBy("count", ascending=False)

    return word_counts

# Example usage
if __name__ == "__main__":
    file_path = "data/biographies.list"
    word_counts = count_words(file_path)
    word_counts.show(10)
