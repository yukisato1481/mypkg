# SPDX-FileCopyrightText: 2022 Yuki Sato s21C1056FY@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msg.msg import Person

def cb(msg):
	global node
	node.get_logger().info("Listen: %s" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "person", cb, 10)

rclpy.spin(node)
