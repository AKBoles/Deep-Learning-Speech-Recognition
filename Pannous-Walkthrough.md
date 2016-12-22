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
    
    As can be seen, the data is first input into the first fully connected layer and then into the dropout and the second fully connected layer. Note that the second fully connected layer is the first to connect to the accuracy and cross entropy steps. This is because the second fully connected layer feeds directly into a regression that uses cross entropy.
    
4. The next step in the script is to train the model using the defined network. Using TFLearn, this only requires two lines of code:

    ~~~python
    model = tflearn.DNN(net)
    model.fit(X, Y, n_epoch=100, show_metric=True, snapshot_step=100)
    ~~~
    
    The first line defined the Deep Neural Network model as `tflearn.DNN(net)` where `net` is defined in the step above.
    
    The second line defines the input data / labels to feed into the model, as well as the number of epochs to train over. Additional output information is defined as well with the `show_metric` and `snapshot_step` arguments. These two simply tell the script to output the metric and show a snapshot of the training every `snapshot_step` number of training steps.
    
5. Finally, the trained model is tested using a sample audio file. As far as I could tell, the file being used was also in the training dataset. I did not think this was appropriate so I removed the specified file from the training data set and placed it aside for testing after the model was trained.

    The following lines of code show how the model is tested with a new value:
    
    ~~~python
    demo_file = "8_Bruce_260.wav"
    demo=data.load_wav_file(demo_file)
    result=model.predict([demo])
    result=data.one_hot_to_item(result,speakers)
    print("predicted speaker for %s : result = %s "%(demo_file,result))
    ~~~
    
    As can be seen, the `demo_file` is fed into `model.predict`. This creates a one-hot vector which is then converted into an individual speaker using `one_hot_to_item`. 
    
    The result was as hoped: Bruce was speaking and Bruce was predicted! That is good news. The next step is to perform this architecture using a different data set.

    It should be noted that this architecture performs exceptionally well on a training set but not so great on the testing set. As such, other methods have been explored such as using the MFCC information to train a stronger classification network.
