#!/usr/bin/env python
import rospy
from primer_ejemplo.srv import AddTwoInts, AddTwoIntsRequest, AddTwoIntsResponse

def handle_add_two_ints(req):
    rospy.loginfo("Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b)) )
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
