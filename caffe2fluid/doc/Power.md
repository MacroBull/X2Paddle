## Power


### [Power](http://caffe.berkeleyvision.org/tutorial/layers/power.html)
```
layer {
    name: "power"
    type: "Power"
    bottom: "data"
    top: "power"	
    power_param {
	power: 1
	scale: 1
	shift: 0
    }
}
```


### [paddle.fluid.layers.pow](http://paddlepaddle.org/documentation/docs/zh/1.4/api_cn/layers_cn.html#permalink-121-pow)
```python
paddle.fluid.layers.pow(
    x,
    factor=1.0,
    name=None
)
```  

### 功能差异
#### 计算机制
Caffe：计算公式如下所示，
$$y=(shift+scale \times x)^2$$            
PaddlePaddle：计算公式如下所示，
$$y=x^{factor}$$
