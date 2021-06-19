# string_searching_algorithms

String-searching algorithms implementation by Ivan Razzhivin:
1. Boyer-Moore-Horspool; 
2. Karp–Rabin; 
3. Knuth–Morris–Pratt; 
4. Aho–Corasick;
5. Naive Pattern Searching;

# Algo runtime results
```python
knuth_morris_pratt
Test N 1 time: 0.0001096788341332508
Test N 2 time: 0.0001233411376914098
Test N 3 time: 0.000689840316772461
Test N 4 time: 0.003001117706298828
Test N 5 time: 0.000263524055480957
Test N 6 time: 0.0005009174346923828
Test N 7 time: 0.0013851165771484376
Test N 8 time: 0.004727649688720703

naive
Test N 1 time: 0.0
Test N 2 time: 0.00023691654205322267
Test N 3 time: 0.027048659324645997
Test N 4 time: 1.465348482131958
Test N 5 time: 0.0002749919891357422
Test N 6 time: 0.00045857429504394533
Test N 7 time: 0.002371811866760254
Test N 8 time: 0.004924201965332031

aho_corasick
Test N 1 time: 0.00010758666992191723
Test N 2 time: 0.00023496150970458984
Test N 3 time: 0.005228185653686523
Test N 4 time: 0.30330030918121337
Test N 5 time: 0.000731205940246582
Test N 6 time: 0.004023432731628418
Test N 7 time: 0.055155277252197266
Test N 8 time: 0.010457134246826172

boyer_moore_horspool
Test N 1 time: 0.0
Test N 2 time: 0.000194741821289113426
Test N 3 time: 0.00048720836639404297
Test N 4 time: 0.0026867866516113283
Test N 5 time: 0.000299945068359423451
Test N 6 time: 6.0510635375976565e-05
Test N 7 time: 0.00019390583038330077
Test N 8 time: 0.00036027431488037107

rabin_karp
Test N 1 time: 0.0
Test N 2 time: 0.000101766967773456251
Test N 3 time: 0.00045900344848632814
Test N 4 time: 0.0024184942245483398
Test N 5 time: 0.00037424564361572267
Test N 6 time: 0.0006479978561401367
Test N 7 time: 0.0032538175582885742
Test N 8 time: 0.007049036026000976
```

#Comparison counter

```python
knuth_morris_pratt
Test N 1 comparison count: 18 & positions:  [8]
Test N 2 comparison count: 190 & positions:  [90]
Test N 3 comparison count: 1900 & positions:  [900]
Test N 4 comparison count: 9000 & positions:  [4000]
Test N 5 comparison count: 697 & positions:  [599]
Test N 6 comparison count: 1074 & positions:  [610]
Test N 7 comparison count: 3150 & positions:  [1629]
Test N 8 comparison count: 10623 & positions:  [9522]

naive
Test N 1 comparison count: 19 & positions:  [8]
Test N 2 comparison count: 955 & positions:  [90]
Test N 3 comparison count: 95050 & positions:  [900]
Test N 4 comparison count: 4500500 & positions:  [4000]
Test N 5 comparison count: 714 & positions:  [599]
Test N 6 comparison count: 1158 & positions:  [610]
Test N 7 comparison count: 3554 & positions:  [1629]
Test N 8 comparison count: 10714 & positions:  [9522]

aho_corasick
Test N 1 comparison count: 18 & positions:  {'ab': [8]}
Test N 2 comparison count: 190 & positions:  {'aaaaaaaaab': [90]}
Test N 3 comparison count: 1900 & positions:  {'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab': [900]}
Test N 4 comparison count: 9000 & positions:  {'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab': [4000]}
Test N 5 comparison count: 714 & positions:  {'сын князя Василия': [599]}
Test N 6 comparison count: 1159 & positions:  {'Да, я слышал про его план вечного мира, и это очень интересно, но едва ли возможно...': [610]}
Test N 7 comparison count: 3540 & positions:  {'вспоминал свое обещание, но тут же, как это бывает с людьми, называемыми бесхарактерными, ему так страстно захотелось войти взглянуть еще раз на эту столь знакомую и надоевшую ему беспутную жизнь, и невольно пришла в голову мысль, что данное слово ничего не значит, к тому же, еще прежде, чем князю Андрею, он дал также Анатолю слово привезти долг; наконец, он подумал, что все эти': [1629]}
Test N 8 comparison count: 10715 & positions:  {'Бутылка рому была принесена; раму, не пускавшую сесть на наружный откос окна, выламывали два': [9522]}

boyer_moore_horspool
Test N 1 comparison count: 31 & positions:  [8]
Test N 2 comparison count: 293 & positions:  [90]
Test N 3 comparison count: 2903 & positions:  [900]
Test N 4 comparison count: 14003 & positions:  [4000]
Test N 5 comparison count: 231 & positions:  [599]
Test N 6 comparison count: 283 & positions:  [610]
Test N 7 comparison count: 987 & positions:  [1629]
Test N 8 comparison count: 1520 & positions:  [9522]

rabin_karp
Test N 1 comparison count: 29 & positions:  [8]
Test N 2 comparison count: 283 & positions:  [90]
Test N 3 comparison count: 2803 & positions:  [900]
Test N 4 comparison count: 13003 & positions:  [4000]
Test N 5 comparison count: 2053 & positions:  [599]
Test N 6 comparison count: 3325 & positions:  [610]
Test N 7 comparison count: 9607 & positions:  [1629]
Test N 8 comparison count: 32193 & positions:  [9522]
```
