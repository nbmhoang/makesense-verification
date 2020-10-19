# -*- coding: utf-8 -*-

import os
import glob
import xml.etree.ElementTree as ET


def update_xml_file(xml_file: str):
  tree = ET.parse(xml_file)
  root = tree.getroot()
  for obj in root.findall('object'):
      # print('Found a object')
      for ele in obj:
        if ele.tag in ('truncated', 'difficult'):
          ele.text = '0'
  tree.write(xml_file)

if __name__ == "__main__":
  DATA = 'rewrite'
  for folder in os.listdir(DATA):
    current_path = os.path.join(DATA, folder)
    if os.path.isdir(current_path):
      print('Working on {} folder'.format(folder))
      for xml in glob.glob('{}/{}/*.xml'.format(DATA, folder)):
        update_xml_file(xml)
