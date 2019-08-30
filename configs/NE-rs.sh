#!/usr/bin/env bash

data_dir="data/NE"
model="point.rs.distmult"
group_examples_by_query="False"
use_action_space_bucketing="True"

bandwidth=256
entity_dim=200
relation_dim=200
history_dim=200
history_num_layers=3
num_rollouts=20
num_rollout_steps=3
num_epochs=50
num_wait_epochs=5
num_peek_epochs=2
bucket_interval=10
batch_size=12
train_batch_size=12
dev_batch_size=1
learning_rate=0.003
baseline="n/a"
grad_norm=5
emb_dropout_rate=0.1
ff_dropout_rate=0.1
action_dropout_rate=0.1
action_dropout_anneal_interval=1000
reward_shaping_threshold=0
beta=0.05
relation_only="False"
beam_size=512

distmult_state_dict_path="model/NE-distmult-xavier-200-200-0.003-0.3-0.1/checkpoint-999.tar"
conve_state_dict_path="model/NE-conve-RV-xavier-200-200-0.003-32-3-0.3-0.3-0.2-0.1/checkpoint-999.tar"

num_paths_per_entity=-1
margin=-1
