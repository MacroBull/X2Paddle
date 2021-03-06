""" a custom layer for 'reshape', maybe we should implement this in standard way.
    more info can be found here: http://caffe.berkeleyvision.org/tutorial/layers/reshape.html
"""
from .register import register
from functools import reduce


def import_fluid():
    import paddle.fluid as fluid
    return fluid


def reshape_shape(input_sp, shape, axis=0, num_axes=-1):
    """ calculate the output shape of this layer using input shape

    Args:
        @input_shape (list of num): a list of number which represents the input shape
        @shape (object): parameter from caffe's Reshape layer
        @axis (int): parameter from caffe's Reshape layer
        @num_axes(int): parameter from caffe's Reshape layer

    Returns:
        @output_shape (list of num): a list of numbers represent the output shape
    """

    def count(num_list):
        return reduce(lambda a, b: a * b, num_list)

    input_shape = list(input_sp)
    input_count = count(input_shape)

    input_num_axes = len(input_shape)

    input_start_axis = axis
    start_axis = input_start_axis if input_start_axis >= 0 \
            else input_num_axes + input_start_axis + 1

    assert start_axis >= 0, "[Reshape]axis %d out of range" % (input_start_axis)
    assert start_axis <= input_num_axes, "[Reshape]axis %d out of range for %d-D input data"\
            % (input_start_axis, input_num_axes)

    assert num_axes >= -1, "[Reshape]num_axes must be >= 0, or -1 for all"

    end_axis = input_num_axes if num_axes == -1 else start_axis + num_axes
    assert end_axis <= input_num_axes, "end_axis[%d] = axis[%d] + num_axes[%d] is out of range"\
            % (end_axis, start_axis, num_axes)

    num_axes_replaced = end_axis - start_axis
    num_axes_retained = input_num_axes - num_axes_replaced
    num_new_axes = len(shape['dim'])
    output_shape = []

    for i in range(start_axis):
        output_shape.append(input_shape[i])

    for i in range(num_new_axes):
        output_shape.append(shape['dim'][i])

    for i in range(end_axis, input_num_axes):
        output_shape.append(input_shape[i])

    assert len(output_shape) == num_axes_retained + num_new_axes,\
            "[Reshape]invalid dims of output shape[%s]" % (str(output_shape))

    return output_shape


def reshape_layer(input, name, shape, axis=0, num_axes=-1):
    """ build a layer of type 'Flatten' using fluid

    Args:
        @input (variable): input fluid variable for this layer
        @name (str): name for this layer
        @shape (object): parameter from caffe's Reshape layer
        @axis (int): parameter from caffe's Reshape layer
        @num_axes(int): parameter from caffe's Reshape layer

    Returns:
        output (variable): output variable for this layer
    """
    fluid = import_fluid()
    input_shape = list(input.shape)
    if input_shape[0] == -1:
        input_shape[0] = 0
        output_shape = reshape_shape(input_shape, shape, axis, num_axes)
    else:
        output_shape = reshape_shape(input_shape, shape, axis, num_axes)
    output = fluid.layers.reshape(input, shape=output_shape, name=name)

    return output


register(kind='Reshape', shape=reshape_shape, layer=reshape_layer)

