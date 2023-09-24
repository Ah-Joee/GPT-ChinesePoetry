# GPT-ChinesePoetry

## Reference and Credit
Note that most of the codes in this repository are not original and are followed largely from Andrej Karpathy's nanoGPT repository (source: https://github.com/karpathy/nanoGPT).

This respository aims to use the nanoGPT model as a foundation, feed in the Chinese poetry, and ask the trained-model to produce poetry that written in Chinese.

## Quick Start
First, we generate ChinesePoetry.txt from the dataset by running the following in the GPT-ChinesePoetry in the command line: 
```
python ./data/ChinesePoetry/get_data.py
```

Second, we turn the raw text into integers for encoding:
```
python ./data/ChinesePoetry/prepare.py
```
This creates a ```train.bin``` and ```val.bin``` in the data directory.

Third, we train our GPT by running:
```
python ./train.py ./config/ChinesePoetry.py
```

Lastly, we generate a sample:
```
python ./sample.py
```

Notice that is you don't have a GPU that supports CUDA, run the following instead:
```
python ./sample.py --device=cpu
```
