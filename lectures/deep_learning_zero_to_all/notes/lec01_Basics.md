# Machine Learning Basics

</br>

## Machine Learning

> "Field of study that gives computers the ability to learn without being explicitly programmed”
>
> \- Arthur Samuel (1959)

- 필요성
  - explicit programming(미리 만들어 놓은 로직대로 동작하는 일반적인 프로그램을 작성하는 것)의 한계를 극복하기 위한 것이다. 
    - 스팸 메일을 거르는 프로그램 : 끊임 없이 엄청 많은 필터링 요소들이 생겨날텐데, 애초에 만들어 놓은 규칙들을 가지고 모든 스팸 메일을 커버할 순 없을 것.
    - 자율 주행 : 수없이 많은 도로의 상황이 있을텐데, 이를 다 커버하는 프로그램을 명시적으로 짜기 힘들 것.
- 그러니, 개발자가 일일이 정하지 않고, 프로그램이 자체적으로 학습해서 동작하면 어떨까? -> "Machine Learning"

</br>

## Supervised/Unsupervised learning

### Supervised learning

- 정의
  - learning with **labeled** examples - **training set**
  - (machine은 training set을 학습하고, 모델을 만든다. 이후, input을 넣으면 그 모델에 따라 output 알랴줌)

- 예시
  - 고양이/강아지 사진 -> 고양이? 강아지? 판별하는 프로그램 : 고양이 사진 엄청 많이 넣고, 얘가 고양이라고 학습 시킴. 강아지 사진 엄청 많이 넣고, 얘가 강아지라고 학습시킴. 그리고, 이 input/output 자료가 training set.

- 종류
  - **regression**
    - 예) 시간에 따른 성적(0~100) 추측하기 : X(hours) -> Y(score)
  - **binary classification**
    - 예) 시간에 따른 성적(P/F) 추측하기 :  X(hours) -> Y(bool)
  - **multi-label classification**
    - 예) 시간에 따른 성적(A, B, C, D, F) 추측하기 :  X(hours) -> Y(one of {A, B, C, D, F})

### Unsupervised learning

- learning with **un-labeled** data
  - Google news grouping : 뉴스 하나 하나에 태그/카테고리를 달..순 있겠지만, 좀 힘들겠죠? 얘는 자동적으로 비슷한 뉴스를 찾아줄 수 있다.
  - Word clustering : 얘가 얘와 비슷하다… 이런 데이터 없이, 알아서 비슷한 단어 모으기.