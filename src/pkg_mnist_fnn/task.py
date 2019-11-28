# Parse arguments and call main function
import os
import json
import argparse
import shutil
from pprint import pprint 

from .model import train_and_evaluate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_path',
        help='GCS or local path to training data',
        required=True
    )
    parser.add_argument(
        '--output_dir',
        help='GCS location to write checkpoints and export models',
        required=True
    )
    parser.add_argument(
        '--train_batch_size',
        help='Batch size for training steps',
        type=int,
        default='128'
    )
    parser.add_argument(
        '--train_steps',
        help='Steps to run the training job for',
        type=int,
        default='200'
    )
    parser.add_argument(
        '--learning_rate',
        help='Learning Rate used for Adam',
        type=float,
        default='0.001'
    )
    parser.add_argument(
        '--hidden_units',
        help = 'Hidden layer sizes to use for DNN feature columns -- provide space-separated layers',
        type = str,
        default = "256 128 64"
    )   
    parser.add_argument(
        '--job_dir',
        help='this model ignores this field, but it is required by gcloud',
        default='junk'
    )
    # Eval arguments
    parser.add_argument(
        '--eval_delay_secs',
        help='How long to wait before running first evaluation',
        default=1,
        type=int
    )
    parser.add_argument(
        '--min_eval_frequency',
        help='Seconds between evaluations',
        default=5,
        type=int
    )

    args = parser.parse_args().__dict__
    pprint("Arguments:\n{}".format(args)) 
    args['hidden_units'] = [int(x) for x in args['hidden_units'].split(' ')]
    pprint("Arguments:\n{}".format(args)) 
    
    output_dir = args['output_dir']
    # Append trial_id to path if we are doing hptuning
    # This code can be removed if you are not using hyperparameter tuning
    args['output_dir'] = os.path.join(
        output_dir,
        json.loads(
            os.environ.get('TF_CONFIG', '{}')
        ).get('task', {}).get('trial', '')
    )
    print("Save output to: {}".format(args['output_dir']))
    # #######################################
    # # Train and Evaluate (use TensorBoard to visualize)
    train_and_evaluate(args)
