# MetaKGR

Source codes and datasets for EMNLP 2019 paper [Adapting Meta Knowledge Graph Information for Multi-Hop Reasoning over Few-Shot Relations](https://arxiv.org/pdf/1908.11513.pdf)

## Requirements

- python3 (tested on 3.6.6)
- pytorch (tested on 0.4.1)

### Installation

``` bash
python3 -m pip install -r requirements.txt
```

## Data Preparation

Unpack the data files

``` bash
unzip data.zip
```

and there will be two datasets under folder `data`.

``` bash
# dataset FB15K-237
data/FB15K-237

# dataset NELL-995
data/NE
```

## Pretrain Knowledge Graph Embedding

``` bash
./experiment-emb.sh configs/<dataset>-<model>.sh --train <gpu-ID>
```

`dataset` is the name of datasets and `model` is the name of knowledge graph embedding model. In our experiments, `dataset` could be `fb15k-237` and `NE`, `model` could be `conve` and `distmult`. `<gpu-ID>` is a non-negative integer number representing the GPU index.

## Meta Learning

``` bash
# take FB15K-237 for example
./experiment-rs.sh configs/fb15k-237-rs.sh --train <gpu-ID> --few_shot
```

## Fast Adaptation

``` bash
# take FB15K-237 for example
./experiment-rs.sh configs/fb15k-237-rs.sh --train <gpu-ID> --adaptation --checkpoint_path model/FB15K-237-point.rs.conve-xavier-n/a-200-200-3-0.001-0.3-0.1-0.5-400-0.02/checkpoint-<Epoch>.tar
```

`<Epoch>` is a non-negative integer number representing the training epoch for meta-learning. We can assign `<Epoch>` to be 25 on FB15K-237.

## Test

``` bash
# take FB15K-237 for example
./experiment-rs.sh configs/fb15k-237-rs.sh --inference <gpu-ID> --few_shot --checkpoint_path model/FB15K-237-point.rs.conve-xavier-n/a-200-200-3-0.001-0.3-0.1-0.5-400-0.02/checkpoint-<Epoch_Adapt>-[relation].tar
```

`<Epoch_Adapt>` is a non-negative integer number representing the training epoch for fast adaptation. We can assign `<Epoch_Adapt>` to be 39 on FB15K-237.

## Cite 

If you use the code, please cite this paper:

Xin Lv, Yuxian Gu, Xu Han, Lei Hou, Juanzi Li, Zhiyuan Liu. Adapting Meta Knowledge Graph Information for Multi-Hop Reasoning over Few-Shot Relations. *The Conference on Empirical Methods in Natural Language Processing (EMNLP 2019)*.
