python createContentTrainingData.py --output /workspace/datasets/categories/output.fasttext --sample_rate 0.5 --min_products 10
gshuf /workspace/datasets/categories/output.fasttext > /workspace/datasets/fasttext/shuffled.fasttext
head -n 10000 /workspace/datasets/fasttext/shuffled.fasttext > /workspace/datasets/fasttext/train.fasttext
tail -n 10000 /workspace/datasets/fasttext/shuffled.fasttext > /workspace/datasets/fasttext/test.fasttext
/workspace/fastText/fasttext supervised -input /workspace/datasets/fasttext/train.fasttext -output products -epoch 50 -wordNgrams 2 -lr 2
/workspace/fastText/fasttext test products.bin /workspace/datasets/fasttext/test.fasttext
