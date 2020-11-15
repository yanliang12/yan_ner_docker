# yan_ner_docker

start the docker and enter python3

```bash
docker pull yanliang12/yan_ner_docker:1.0.1

docker run -it yanliang12/yan_ner_docker:1.0.1 bash

python3
```

extract entities from a Arabic text

```python
>>> from yan_ner_arabic import arabic_ner
2020-11-15 11:05:14 INFO: Loading these models for language: ar (Arabic):
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
2020-11-15 11:05:14 INFO: Use device: cpu
2020-11-15 11:05:14 INFO: Loading: tokenize
2020-11-15 11:05:14 INFO: Loading: mwt
2020-11-15 11:05:14 INFO: Loading: pos
2020-11-15 11:05:15 INFO: Loading: lemma
2020-11-15 11:05:15 INFO: Loading: depparse
2020-11-15 11:05:17 INFO: Loading: ner
2020-11-15 11:05:18 INFO: Done loading processors!
>>> 
>>> text = u"""
... لقاءنا الثامن في سلسلة لقاءات افتراضية مع باحثين في #معالجة_اللغة_العربية مع
... أ.د. نزار حبش و م.أسامة عبيد
... 
... عنوان اللقاء:
... أدوات كامل: مجموعة أدوات مفتوحة المصدر بلغة بايثون لمعالجة اللغة العربية 
... 
... يوم الأربعاء 11 نوفمبر الساعة 8م بتوقيت مكة 
... 
... للتسجيل 👇
... """
>>> 
>>> print(arabic_ner(text))
[{'text': 'نزار حبش', 'type': 'PER', 'start_char': 83, 'end_char': 91}, {'text': 'أسامة عبيد', 'type': 'PER', 'start_char': 96, 'end_char': 106}, {'text': 'بايثون', 'type': 'MISC', 'start_char': 166, 'end_char': 172}, {'text': 'مكة', 'type': 'LOC', 'start_char': 237, 'end_char': 240}]
>>> 
```
