# Caffe to Tensorflow

</br>

## 사전 조사

### 블로그

- [[Tip] Caffe Model을 Tensorflow Model로 바꾸기](https://leaped.tistory.com/5)
  - 이 사람은 정확도를 위하여 caffe model 가중치를 numpy로 바꾸며 손수 변환함
  - 변환하면서 겪은 뻘짓들 정리해 놓음
  - [caffe model param -> numpy's 변환기](https://github.com/nilboy/extract-caffe-params)

- [Caffe-TensorFlow 사용법](https://blog.limerainne.win/18)
  - caffe model -> tensorflow model
  - 근데 정확도가 높지 않았다 (원래도 79%인데 변환해보니 변환한 것은 더 낮은 78%)
  - [Caffe-tensorflow 이용](https://github.com/ethereon/caffe-tensorflow)
- 해외 사이트들 ([Caffe-tensorflow 이용](https://github.com/ethereon/caffe-tensorflow))
  - [Converting a Caffe model to TensorFlow](<https://ndres.me/post/convert-caffe-to-tensorflow/>)
    - caffe model(places365??) -> tensorflow model
  - [A simple tutorial about Caffe-TensorFlow model conversion](<https://blog.wildcat.io/2018/04/a-simple-tutorial-about-caffe-tensorflow-model-conversion/>)
  - 

### 라이브러리들

- model conversion
  - [Caffe-tensorflow](https://github.com/ethereon/caffe-tensorflow)
- param conversion
  - [extract-caffe-params](https://github.com/nilboy/extract-caffe-params)

- [MSDNN](<https://github.com/Microsoft/MMdnn#conversion>)
  - [caffee readme](https://github.com/Microsoft/MMdnn/blob/master/mmdnn/conversion/caffe/README.md)
  - 





