# install
```
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch-nightly -c nvidia
pip install transformers==3.1.0
pip install pytorch-lightning==1.9.4
```
alternatively, you can use the original tested versions
```
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
pip install transformers==3.1.0
pip install pytorch-lightning==1.0.3
```

```
cd zero-shot-dst/T5DST/
sh run.sh
```# t5dst
