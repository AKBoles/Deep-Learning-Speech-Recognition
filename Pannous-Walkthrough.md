Pannous Description / Implementation
====================================

### Introduction ###

#### Who is Pannous? ###

Pannous is a collaboration working on improving Speech Recognition. Primarily, I will be working with their Tensorflow repository (link given below).

Please see this link for more information on Pannous: https://github.com/pannous/tensorflow-speech-recognition

#### To-be-Implemented ####

First file to be implemented is the `speaker_classifier_tflearn.py` script. This script trains on a dataset of 15 speakers and then makes a prediction as to who is speaking on an input audio sample.

#### Description of Data ####

In this script, Pannous uses data from the following link: http://pannous.net/files/spoken_numbers_pcm.tar

This tar file contains 15 different speakers, each saying 10 different phrases, each phrase sampled at 16 different frequencies.

    Note that the phrases are the English numbers: 0-9.
    
    Note that the sample rates are from 100 - 400 in 20 [unit] increments.

This shows that there are 2400 different audio files to train over. The files are in the following format in the directory:

    NumberSpoken_PersonSpeaking_SampleRate.wav   

### Walkthrough of Script ###

Essentially, assuming the data is already downloaded, the script does the following:

1. Creates an array of the different speakers in `speakers`, where the length of this array is the number of classes used for training.

2. Divides the training data set into different batches using `batch=data.wave_batch_generator(batch_size=1000,source=WORD_WAVs,target=data.Target.speaker)`

    This function does a few things. 
    
    First, the Target of the script tells the function what the target of the parent script is: either speaker classification or digit classification. In our current case: `target=speaker`.
    
    Next, the function shuffles the dataset and then creates different `chunks` of wav files that are used to fill the batches until the size is equal to `batch_size`. 
    
    The `source` variable is used to download the data if it is not already present in the folder.
    
    The output of the function is a collection of wav file batches and their associated labels. These are put into the variables `X` and `Y`, respectively.

3. The actual deep learning is done using `TFLearn`. This is found at the following link: http://tflearn.org/. Once the graph is iniatiated using `tflearn.init_graph()`, it can then be defined. The following is the network description used in this script:

    ~~~python
    net = tflearn.input_data(shape=[None, 8192]) #Two wave chunks --> each wave at size 4096
    net = tflearn.fully_connected(net, 64)
    net = tflearn.dropout(net, 0.5)
    net = tflearn.fully_connected(net, number_classes, activation='softmax')
    net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')
    ~~~
    
    These lines are defining a network that looks like the following image:
