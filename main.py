# -*- coding: utf-8 -*-

import os
import yaml
import argparse
from keras import backend as K 

# GPU support is recommended.
os.environ["CUDA_VISIBLE_DEVICES"]="0"

# Arguments
parser = argparse.ArgumentParser(description='Training a vulnerability detection model.')
parser.add_argument('--config', type=str, help='Path to the configuration file.')
parser.add_argument('--data_dir', default='data/', type=str, help='The path of the code base for training.')
parser.add_argument('--output_dir', default='result/', type=str, help='The output path of the trained network model.')
parser.add_argument('--logdir', default='logs/', type=str, help='Logging path.', required=False)
parser.add_argument('--seed', default=42, type=int, help='Random seed for reproducable results.', required=False)
parser.add_argument('--test', action='store_true', help='Test the model.')
parser.add_argument('--trained_model', type=str, help='The path of the trained model for test.')
parser.add_argument('--verbose', default=1, help='Show all messages.')
paras = parser.parse_args()
config = yaml.safe_load(open(paras.config,'r'))

if not paras.test:
    # Train a vulnerability detection model
    from src.helper import Trainer as Helper
else:
    from src.helper import Tester as Helper
    
helper = Helper(config, paras)
helper.exec()

K.clear_session()
