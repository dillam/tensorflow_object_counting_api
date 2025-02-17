#----------------------------------------------
#--- Author         : Ahmet Ozlu
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 27th July 2019
#----------------------------------------------

# Imports
import tensorflow as tf

# Object detection imports
from utils import backbone
from api import object_counting_api

# By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt')

is_color_recognition_enabled = 0
write_csv = True # Use True to write outputs to csv file

object_counting_api.object_counting_webcam(detection_graph, category_index, is_color_recognition_enabled, write_csv)
