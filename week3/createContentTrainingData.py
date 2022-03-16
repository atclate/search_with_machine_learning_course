import argparse
import os
import random
import xml.etree.ElementTree as ET
from nltk import stem
import nltk
nltk.download('stopwords')
import string
from pathlib import Path

def transform_name(product_name):
    lowerCase = product_name.lower()
    punctuationRemoved = lowerCase.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))) 
    stemmer = stem.SnowballStemmer("english")
    return stemmer.stem(punctuationRemoved)

# Directory for product data
directory = r'/workspace/search_with_machine_learning_course/data/pruned_products/'

parser = argparse.ArgumentParser(description='Process some integers.')
general = parser.add_argument_group("general")
general.add_argument("--input", default=directory,  help="The directory containing product data")
general.add_argument("--output", default="/workspace/datasets/fasttext/output.fasttext", help="the file to output to")

# Consuming all of the product data will take over an hour! But we still want to be able to obtain a representative sample.
general.add_argument("--sample_rate", default=1.0, type=float, help="The rate at which to sample input (default is 1.0)")

# IMPLEMENT: Setting min_products removes infrequent categories and makes the classifier's task easier.
general.add_argument("--min_products", default=0, type=int, help="The minimum number of products per category (default is 0).")

args = parser.parse_args()
output_file = args.output
path = Path(output_file)
output_dir = path.parent
if os.path.isdir(output_dir) == False:
        os.mkdir(output_dir)

if args.input:
    directory = args.input
# IMPLEMENT:  Track the number of items in each category and only output if above the min
min_products = args.min_products
sample_rate = args.sample_rate

def extract_category(element):
    if (element.find('categoryPath') is not None and len(element.find('categoryPath')) > 0):
        return element.find('categoryPath')[min(2, len(element.find('categoryPath'))) - 1][0].text
    return None

categoryProductMap = {}
print("Writing results to %s" % output_file)
with open(output_file, 'w') as output:
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            print("Processing %s" % filename)
            f = os.path.join(directory, filename)
            tree = ET.parse(f)
            root = tree.getroot()
            for child in root:
                if random.random() > sample_rate:
                    continue
                # Check to make sure category name is valid
                if (child.find('name') is not None and child.find('name').text is not None and
                    extract_category(child) is not None):
                      # Choose last element in categoryPath as the leaf categoryId
                      cat = extract_category(child)
                      # Replace newline chars with spaces so fastText doesn't complain
                      name = child.find('name').text.replace('\n', ' ')
                      categoryList = categoryProductMap.get(cat, [])
                      categoryList.append(name)
                      categoryProductMap[cat] = categoryList
                    #   output.write("__label__%s %s\n" % (cat, transform_name(name)))
    for category in categoryProductMap:
        if (len(categoryProductMap[category]) > min_products):
            for name in categoryProductMap[category]:
                output.write("__label__%s %s\n" % (category, transform_name(name)))
    

