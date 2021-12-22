# NerLTR-DTA
# INSTALLATION

# Requirements:

Python 3.7x (may work with earlier versions, not tested)

Sklearn 0.0

Numpy 1.17.0

Pandas  1.2.3

Java environment


# Usage

1.RankLib-2.16.jar([download](https://sourceforge.net/p/lemur/wiki/RankLib/))

train:  
```
java -jar RankLib-2.16.jar -train train.txt   -ranker 0    -metric2t NDCG@50    -tree 500  -leaf 300  -shrinkage 0.03   
                           -mls 5   -tc 256 -save t_model.txt -out t_out.txt
```
test:  
```
java -jar RankLib-2.16.jar -load t_model.txt -rank test.txt -indri test_rank.txt
```

2.index_available.py -- Get the index of the data that satisfies the constraint

3.AAF.py/SAF.py -- Extract features


# Evaluation criteria:

MSE

CI

Rm2


##### Feature:

The characteristics of drugs and proteins are obtained in the same way, and the code only lists one

##### Note:

Some data processing is done with linux commands,the code is simple, therefore the specific code is not listed.

sharing-sharing matrix --data processing.py

rm2 refers to the code in DeepDTA(Öztürk H, Özgür A, Ozkirimli E. DeepDTA: deep drug–target binding affinity prediction[J]. Bioinformatics, 2018, 34(17): i821-i829.)
