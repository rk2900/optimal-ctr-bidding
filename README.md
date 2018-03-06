# Optimal CTR bidding
An experimental framework to support experiments in CIKM 2016 paper "User Response Learning for Directly Optimizing Campaign Performance in Display Advertising". [PDF](http://apex.sjtu.edu.cn/public/files/papers/20160817/opt-ctr-bid.pdf)

If you have any problem, please [send an E-mail](mailto:kren@apex.sjtu.edu.cn) to [Kan Ren](http://apex.sjtu.edu.cn/members/kren).

## Datasets
* `iPinYou` has been decribed in [this page](https://github.com/wnzhang/make-ipinyou-data).
* `YOYI` is the newly published dataset in our CIKM paper. The detail of this dataset is [here](http://apex.sjtu.edu.cn/datasets/7).

## Format of data
We use `yzx` data structure to formalize bidding logs.
Each record contains
* `y`: true label of user response (1 for positive and 0 otherwise).
* `z`: the market price of this sample.
* `x`: pre-processed features of the bid request.

Other details of `yzx` data can be found in [this benchmarking paper](http://arxiv.org/abs/1407.7073)

## Prepare the dataset
* Clone and prepare `iPinYou` dataset as described [here](https://github.com/wnzhang/make-ipinyou-data). Note that, please put `make-ipinyou-data` folder in the same parent folder as `optimal-ctr-bidding` project.
```
|-- code-folder
----|-- make-ipinyou-data
--------|-- yoyi-data
--------|-- 1458
--------|-- 2259
--------...
----|-- optimal-ctr-bidding
--------|-- python
--------|-- scripts
--------|-- README.md
```
* (optional) Download `YOYI` dataset and put the folder in `make-ipinyou-data`.

## Run the code
* Go to `script` folder and execute `run_MODEL` scripts, where `MODEL` is a placeholder of model names including "lr", "sqlr", "eu" and "rr". Details of the models can be found in our paper.
* Example: ```sh run-lr.sh "1458 2261 2821"```

## Citation
```
@inproceedings{ren2016user,
  title={User response learning for directly optimizing campaign performance in display advertising},
  author={Ren, Kan and Zhang, Weinan and Rong, Yifei and Zhang, Haifeng and Yu, Yong and Wang, Jun},
  booktitle={Proceedings of the 25th ACM International on Conference on Information and Knowledge Management},
  pages={679--688},
  year={2016},
  organization={ACM}
}
```
