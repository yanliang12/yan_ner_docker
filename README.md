# yan_ner_docker

```python
>>> from yan_ner_arabic import arabic_ner

2020-11-15 10:36:42 INFO: Loading these models for language: ar (Arabic):
=======================
| Processor | Package |
-----------------------
| tokenize  | padt    |
| mwt       | padt    |
| pos       | padt    |
| lemma     | padt    |
| depparse  | padt    |
| ner       | aqmar   |
=======================

/usr/local/lib/python3.7/dist-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0
2020-11-15 10:36:42 INFO: Use device: cpu
2020-11-15 10:36:42 INFO: Loading: tokenize
2020-11-15 10:36:42 INFO: Loading: mwt
2020-11-15 10:36:42 INFO: Loading: pos
2020-11-15 10:36:44 INFO: Loading: lemma
2020-11-15 10:36:44 INFO: Loading: depparse
2020-11-15 10:36:45 INFO: Loading: ner
2020-11-15 10:36:46 INFO: Done loading processors!
>>> 
>>> text = u"اسمي مشاري. انا اعمل في جامعة حائل. انا سعودي."
>>> 
>>> print(arabic_ner(text))
[{'text': 'مشاري', 'type': 'PER', 'start_char': 5, 'end_char': 10}, {'text': 'جامعة حائل', 'type': 'LOC', 'start_char': 24, 'end_char': 34}]
>>> 
```
