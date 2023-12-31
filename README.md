# Function-level Vulnerability Detection and Dataset


This is an open-source project (forked from [here](https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset)) We use the source code functions as inputs and implement Word2vec for generating code embeddings. The output is a probability of the corresponding input sample being vulnerable or not. This project includes 6 mianstream neural network models and can be easily extended to use other network models implemented using Keras or Tensorflow.    

For this project, we also collect vulnerable functions from 9 open-source software projects (written in C programming language). See [Dataset](https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset/blob/master/Vulnerable%20Functions%20Statistical%20Analysis.md) for more details. We have detailed the data collection and evaluation processes in a paper which is currently under review. When the review process is completed, we will publish all the data.

 
## Instructions & Usage
Unzip the zip file of this repository, one will see the following folders:
* The config folder -- containing the configuration file.
* The data folder -- containing the source code functions (vulnerable and non-vulnerable).
* The graph folder -- containing the sample results and data statistics.
* The src folder -- containing the code for model training and test.

And there are two Python script files:
* main.py -- for training and test a specified network model
* Word_to_vec_embedding.py -- for training a Word2vec embedding model.

### Step 1: Train a Word2vec model

To use the provided data samples for model training, we have to train a Word2vec model first. By executing the following command:
```
python Word_to_vec_embedding.py --data_dir <path to code base.> --output_dir <path to the output file.>
```
We can train a Word2vec model based on the code specified in the `<path to code base.>`. The purpose of training the Word2vec model is to convert source code tokens to meaningful embeddings for the neural network models to learn from.

To use data samples from other sources, modify the parameters of the `--data_dir` to point to the directory where the sources are stored. The parameters available for the ```Word_to_vec_embedding.py``` script are as follows:

| Options           | Description                                                               |
|-------------------|---------------------------------------------------------------------------|
| data_dir          | Path to the code base (can be obtained by download & unzip the files under data folder. By default, it is `data/`.)                 |
| output_dir      | The output path of the trained Word2vec model(two files. By default, it is `result/`.)                                                              |
| n_workers       | The number of threads for training. |
| size       | The dimensionality of the word vectors. This is also the Embedding dimension used in the subsequent steps. |
| window | The maximum distance between the current and predicted word within a sentence.                                                     |
| min_count        | Ignores all words with total frequency lower than this.                                                |
| algorithm       | Training algorithm: 1 for skip-gram; otherwise CBOW.                   |
| seed            | The seed for the random number generator                   
 
One may check the parameter type and default value by using the option ```--help``` for this script. For more detailed configurations for Word2vec training, please refer to: https://radimrehurek.com/gensim/models/word2vec.html. 

### Step 2: Train a neural network model

When the Word2vec model is ready. One can train a neural network model. The parameters related to experiment/model settings are stored in a yaml configuration file. This allows users to conveniently adjust the settings by just changing the configuration file. See [documentation and examples](config/) for more details.

Once the configuration file is ready, one may run the following command to train a neural network model.
```
Python main.py --config config\config.yaml --data_dir <path_to_your_code>
```
By default, the data used for training is at `data\` folder. The trained models will be placed at `result/models/` folder. The training logs will be at `logs/`. A user can use Tensorboard to visualize the training process by specifying the `logs\` folder to Tensorboard.

### Step 3: Test a trained neural network model

When training is completed, a user can test a network model on the test set by using following command: 
```
Python main.py --config config\config.yaml --test --trained_model D:\Path\of\the\trained_model.h5
```
Users can use their own test set by specifying the `using_separate_test_set` to True in the config.yaml file.

There are also some options available which are listed below:

| Options | Description                                                                                   |
|---------|-----------------------------------------------------------------------------------------------|
| config  | Path to the configuration file.                                                                        |
| seed    | Random seed for reproduction of the results.                                       |
| data_dir    | The path of the code base for training. (can be obtained by download & unzip the files under data folder. By default, it is `data/`.) |
| logdir  | Path to store training logs (log files for Tensorboard). By default, it is `logs/`                                                   |
| output_dir  | The output path of the trained network model. By default, it is `result/models/<model_name.h5>`                                                |
| trained_model   | The path of the trained model for test. By default, the trained models are in `result/models/`                                                      |                                                               |
| test   | Switch to the test mode.                                                               |
| verbose    | Show all messages. 

## Dataset and Results
 * [Dataset](https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset/blob/master/Vulnerable%20Functions%20Statistical%20Analysis.md) -- containing vulnerable and non-vulnerable functions labeled/collected from 9 open-source projects and data statistics.
 * [Training and Evaluation Results](https://github.com/Seahymn2019/Function-level-Vulnerability-Dataset/blob/master/Training%20and%20Results.md) -- containing test results for reference.


