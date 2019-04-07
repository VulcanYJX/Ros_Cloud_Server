#!/usr/bin/env python
# coding:utf-8
import rospy
from service_demo.srv import *

def server_srv():
    rospy.init_node("greetings_server")
    s = rospy.Service("greetings", Greeting, handle_function)
    rospy.loginfo("Ready to handle the request:")
    rospy.spin()
def handle_function(req):
    rospy.loginfo( 'Request from %s with age %d', req.name, req.age)
    return GreetingResponse("Hi %s. I' server!"%req.name)
if __name__=="__main__":
    server_srv()
