# -*- coding: utf-8 -*-
"""traffic-sign-verification.ipynb

Automatically generated by Colaboratory.
"""

import os
import cv2
import random
import glob
import xml.etree.ElementTree as ET


def read_xml_file(xml_file: str):
  tree = ET.parse(xml_file)
  root = tree.getroot()

  list_with_all_boxes = []

  for boxes in root.iter('object'):

    # filename = root.find('filename').text
    
    label_name = None
    ymin, xmin, ymax, xmax = None, None, None, None

    for box in boxes.findall('name'):
      label_name = box.text

    for box in boxes.findall("bndbox"):
      ymin = int(box.find("ymin").text)
      xmin = int(box.find("xmin").text)
      ymax = int(box.find("ymax").text)
      xmax = int(box.find("xmax").text)

    single_object = {label_name: [xmin, ymin, xmax, ymax]}
    list_with_all_boxes.append(single_object)

  return list_with_all_boxes

def plot_one_box(x, img, color=None, label=None, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

DATA_FOLDER = "data"
RESULT_FOLDER = "result"

for folder in os.listdir(DATA_FOLDER):
  current_path = os.path.join(DATA_FOLDER, folder)
  if os.path.isdir(current_path):
    print('Working on {} folder'.format(folder))
    result_path = os.path.join(current_path, RESULT_FOLDER)
    if not os.path.exists(result_path):
      os.mkdir(result_path)

    for xml in glob.glob('{}/*.xml'.format(current_path)):
      image = ''.join(xml.split('.')[:-1]) + '.jpg'
      # print(image.name)
      if os.path.exists(image):
        result = read_xml_file(xml)
        img = cv2.imread(image)
        for obj in result:
          for name, coor in obj.items():
            plot_one_box(coor, img, label=name)
        cv2.imwrite(os.path.join(result_path, os.path.basename(image)), img)
      else:
        print('File not found {}'.format(image))


