/workspace/fastText/fasttext skipgram -input /workspace/datasets/fasttext/titles.txt -output /workspace/datasets/fasttext/title_model -minCount 20
/workspace/fastText/fasttext nn /workspace/datasets/fasttext/title_model.bin
