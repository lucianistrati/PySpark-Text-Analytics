# PySpark Text Analytics

This PySpark script efficiently counts the number of words in very large files using Spark's distributed computing capabilities. It leverages the power of Apache Spark to process large files in parallel, making it suitable for handling massive datasets.

## Features

- **Scalable Word Counting**: Utilizes Spark's distributed processing to efficiently count the occurrences of each word in large text files.
- **Flexible Input**: Works with text files of any size, making it suitable for processing massive datasets.
- **Simple Usage**: Provides a user-friendly interface for counting words in files, with easy-to-understand code.

## Requirements

- Python 3.x
- Apache Spark
- PySpark
- nltk (Natural Language Toolkit) for tokenization (optional)

## Usage

1. Ensure you have Apache Spark installed and configured.
2. Install the required Python dependencies using pip:

   ```
   pip install pyspark nltk
   ```

3. Run the `word_count_pyspark.py` script, providing the path to the text file you want to analyze:

   ```
   python main.py <file_path>
   ```

   Example:
   
   ```
   python main.py data/biographies.list
   ```

4. The script will output the top 10 most common words along with their counts.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua)
