# -*- coding: UTF-8 -*-
import wad.detection

# 探测器
det = wad.detection.Detector()
url = input()
print(det.detect(url))
