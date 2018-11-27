# coreml-emotion-converter
Tutorial on converting a caffe model into coreml

Based on [meghaphone's gathered data](https://github.com/meghaphone/emotion-recognition-mlmodel)

The model details, info on development and paper details can be found [here](https://gist.github.com/GilLevi/54aee1b8b0397721aa4b)

1. Download the [model](https://drive.google.com/file/d/0BydFau0VP3XSNVYtWnNPMU1TOGM/view)

2. Move the model in the root folder of this project (in the same place as `convert.py`)

3. Install `virtualenv` and `coremltools` and run

```
pip install --upgrade pip
pip install virtualenv
cd [working project folder]
virtualenv --python=/usr/bin/python2.7 coreml
source coreml/bin/activate
pip install -U coremltools

python convert.py
```

After it's done just run `deactivate` to exit virtualenv
