## SigmoidCrossEntropyLoss


### [SigmoidCrossEntropyLoss](http://caffe.berkeleyvision.org/tutorial/layers/sigmoidcrossentropyloss.html)
```
layer {
    name: "loss"
    type: "SigmoidCrossEntropyLoss"
    bottom: "x"
    bottom: "label"
    top: "loss"
}
```


### [paddle.fluid.layers.sigmoid_cross_entropy_with_logits](http://paddlepaddle.org/documentation/docs/zh/1.4/api_cn/layers_cn.html#permalink-163-sigmoid_cross_entropy_with_logits)
```python
paddle.fluid.layers.sigmoid_cross_entropy_with_logits(
    x, 
    label, 
    ignore_index=-100, 
    name=None, 
    normalize=False
)
```  

### 功能差异
#### 输入数据
Caffe：输入数据（`x`）的维度最大是4维（`N*C*H*W`）；                 
PaddlePaddle：输入数据(`x`和`label`)的维度只能是2维（`N*K`）。
#### 输出结果
Caffe：输出的数据大小是`1*1*1*1`，即将所有位置上的loss取均值；                      
PaddlePaddle：输出和输入大小一致，即`N*H`。
#### 其他差异
Caffe：无`ignore_index`和`normalize`参数；  
PaddlePaddle：可以通过设定`ignore_index`来确定忽略的目标值，同时它有一个`normalize`参数进行归一化。

