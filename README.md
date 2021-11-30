# culture-expressivity
How Culture Shapes Nonverbal Expressivity: Informing the Design of Robot Mimicry Systems

The goal of our project is to understand how homogeneous culture vs. heterogenous culture affects facial synchrony. To that end, we built an analysis pipeline that produces several models. We tested synchrony using dynamic time warping, comparing the facial similarity between participants.

In understanding synchrony we hope to produce models that inform the design of robotic systems that interact with humans. This portion is future work.

## Pipeline
Our analysis starts with using the open source library Openface. We then feed the facial landmarks into either an autoencoder model (simple or alt) or PCA. Next we feed the resulting feature vectors (and the facial landmarks themselves) into a second layer of dimensionality reduction.

Then to test synchrony, we input a pair of feature vectors (one for each participant) into an open source dynamic time warping library. The resulting cost matrix and distances can be used to infer synchrony between participants (lower cost generally means more synchrony).

Please refer to this diagram of our pipeline,

![Image of our model pipeline](https://github.com/fangyunzhao/culture-expressivity/blob/master/pipeline.png?raw=true)

Our code was primarily written in python using jupyter notebooks. Significance tests were performed in R.

For the larger notebooks, Github cannot load then in their viewer, please use [https://nbviewer.jupyter.org/](https://nbviewer.jupyter.org/) instead. Or use on device editor.

## Installation
### Environment
Ideally you will be running the model on Ubuntu, no garuntees if running on Windows / Mac.

We will require both Rstudio and Jupyternotebooks installed on device. I recommend installing these in [Anaconda](https://www.anaconda.com/).

- [RStudio](https://www.rstudio.com/)
- [Jupyter Notebooks](https://jupyter.org/)

### Libraries
First, please install [openface](https://github.com/TadasBaltrusaitis/OpenFace). Their wiki is [here](https://github.com/TadasBaltrusaitis/OpenFace/wiki).

(Optional) install EmoPy as a submodule. Enter
```
cd <this repo directory>
git submodule update --init --recursive
```

Next install python dependencies
- keras
    - tensorflow (for CPU / GPU - depending on system)
- scikit-learn
- matplotlib
- numpy
- pandas
- cv2 (openCV python bindings)
- umap
- tqdm
- dtw

## Execution
### Pre-Processing
Our dataset starts with a set of videos. These need to be processed by Openface for feature points. The following code snippet will perform this processing step
```
python3 process_vids.py <number of processing threads> <video directory> <result directory>
```
Note that number of threads does not work at this point. It is safest to just put `1` as the input.


(Optionally) we can use EmoPy to generate a set of emotion classifications on each video. This will produce an alternate set of training data where DTW can be run against the emotion state (not recommended).
```
python3 process_emotions.py <video directory> <result directory>
```

The end result of this step will be CSV files for each video file with openface features annotated for each frame and human participant.

### Dataset Construction
To construct the training, test, and validation sets please execute the following notebook. Your pathing may be different if you use a directory other than `data`.

```
nb_dataset_create_model_training_data.ipynb
```

For the alternate dataset (using the old study protocol)
```
nb_dataset_create_alt_model_training_Data.ipynb
```

The end result of this step will be CSV files for (`train`, `test`, and `validation`) sets for each task (*1 - task1_sandwich_openface*, *2 - task2_bart_openface*, *3 - task3_jenga_openface*) and *All Data*.

### Training
We will be training several models in multiple substeps according to the pipeline diagram earlier in the documentation.

First for each task we have a set of basic models training in these notebooks
```
- nb_model_task1.ipynb
- nb_model_task2.ipynb
- nb_model_task3.ipynb
- nb_model_all.ipynb
```

Separately (and mostly for completeness) we train the tSNE model. This one fails to finish training for larger datasets hence why its separate.
```
nb_model_tSNE.ipynb
```

Also for the alternate (old protocol) dataset we have the following models trained.
```
- nb_model_autoencoder_alt.ipynb
```

End result of this step is a set of saved models in the `models` subdirectory.

### Results
Now we can finally apply our models to the entire dataset. At this point we need to pair up participants in the dataset. This may require fiddling with file names to bring them into a consistent format (either do this early on or just rename the openface csv files now). You may also write custom pairing code to handle these issues. 

Run the following code:
```
- nb_results_action_uints.ipynb
- nb_results_encoder_model.ipynb
- nb_results_pca_model.ipynb
- nb_results_umap_pca_model.ipynb
- nb_model_umap.ipynb
```

Also for the alternate (old protocol) dataset we have the following results to be processed
```
- nb_results_alt_encoder_model.ipynb
```

At the end of this step we will have CSV results of the dynamic time warping for each pair of participants tested.

Note at this point, we also have a couple of test codes used to pathfind the pipeline
```
- nb_dtw_test.ipynb
- nb_dtw_umap_test.ipynb
- original_dtw_script.r
```

### Post-Analysis
We used R to run significance tests on each model for predictive synchrony against cultural dyad conditions.
```
analysis.Rmd
```