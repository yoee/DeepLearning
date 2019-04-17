# Softmax classification: Multinomial classification

</br>

## Multinominal Classification

binary로 나누는 방법에 대하여 배웠다. 근데, 만약 A와 B 둘을 구분 짓는 것이 아닌, ABC를 구분 짓는 경우는 어떻게 할까? 

얘는 A와 A 아닌 것, B와 B 아닌 것, C와 C 아닌 것. 이렇게 구분해서 3가지를 나눠버릴 수 있다. 그래서 logistic regression과 비슷하게, 그러나 인자가 여러개이니까, 독립된 classifier들을 모아 matrix로 만들어서 계산해버리면 된다.

</br>

## Softmax

그럼 y예측 값이 나올 것이다. 2, 1, 0.1 이런식으로… 근데 이건 좀 판단하기 이상하니, 얘를 Softmax 에 넣어 확률로 만들어버린다. softmax는 score를 probability로 변환. 우리는 이제 0.7, 0.2, 0.1 같은… 확률들을 얻었고, one-hot encoding으로 (1, 0, 0) 같은 값을 얻어내면 된다.

</br>

## Cost Function, Cross Entropy

그렇다면 cost function은 뭘쓸까? Cross entropy를 쓴다. 수식은… 놋북으로 적기 불편해서 지금은 안쓸랭ㅠ 여하간, D(S, L)을 최소로 하도록 하면 되는데, cross entropy에 경우들을 넣어보면 왜 정당한 지 알 수 있다. 

</br>

## Logistc Cost vs Cross Entropy

이 둘은 같다. 이건, y = p_i로, 1-y = q_i 로 치환해서 식 써보면 알 수 있당.

</br>

## Cost Function for Multinominal Classificaton

위에 만든 loss함수의 평균으로 구하면 된당!

