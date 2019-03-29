##  

# Linear Regression

[수식 보는 방법](<https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related?hl=en>)

</br>

## (Linear) Hypothesis

이전 시간에 배웠던, predicting exam score: regression를 그래프에 표현한다고 생각해보면, 선형 그래프로 표현할 수 있을 것. 이런 식으로, 선형적인 그래프가 도출되는 것이 linear regression.
$$
H (x) = W x + b
$$
선형식은 알다 시피 위와 같은데, 가장 알맞은 W, b 값을 구하는 과정이 필요할 것.

</br>

## Cost function

그래서 나온 것이, cost function(== loss function) 개념. 실제 data와 hypothesis에서 나온 값의 차이를 최소화 하는 W, b를 찾는 것. 
$$
cost(W, b) = \frac{1}{m}\sum_{i=1}^m (H(x^{(i)})-y^{(i)})^2
$$
참고로, 여기서 `H(x) - y` 값을 제곱 시켜준 것은, 양수/음수의 경우 상관 없이 하기 위하여 + 차이가 클 때 더 큰 패널티를 주기 위한 것.

결론적으로 우리가 해야하는 것은.. cost를 최소화하는 W, b 찾는 것. 그것이 가장 적절한 Hypothesis를 찾는 방법!
$$
\underset{cost}{minimize}(W, b)
$$
