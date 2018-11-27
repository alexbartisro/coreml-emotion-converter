import coremltools

print 'loading model\n'
coreml_model = ('EmotiW_VGG_S.caffemodel', 'deploy.prototxt')

print 'loading labels\n'
labels = 'labels.txt'

print 'converting'
coreml_model_converter = coremltools.converters.caffe.convert(coreml_model,class_labels=labels,image_input_names='data')

print 'saving'
coreml_model_converter.save('EmotiClassifier.mlmodel')
