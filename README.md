# culture-expressivity
How Culture Shapes Nonverbal Expressivity: Informing the Design of Robot Mimicry Systems

The goal of our project is to understand how homogeneous culture vs. heterogenous
culture affects facial synchrony. To that end, we built an analysis pipeline that
produces several models. We tested synchrony using dynamic time warping, comparing
the facial similarity between participants.

## Pipeline
Our analysis starts with using the open source library Openface. We then feed
the facial landmarks into either an autoencoder model (simple or alt) or PCA.
Next we feed the resulting feature vectors (and the facial landmarks themselves)
into a second layer of dimensionality reduction.

Then to test synchrony, we input a pair of feature vectors (one for each participant)
into an open source dynamic time warping library. The resulting cost matrix and
distances can be used to infer synchrony between participants (lower cost generally
means more synchrony).

Please refer to this diagram of our pipeline,

![Image of our model pipeline](https://github.com/curthenrichs/culture-expressivity/blob/master/pipeline.png?raw=true)

Our code was primarily written in python using jupyter notebooks. We also have a
bit of R analysis code at the end.

For the larger notebooks Github cannot load then in their viewer, please use [https://nbviewer.jupyter.org/](https://nbviewer.jupyter.org/) instead.
