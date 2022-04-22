#!/usr/bin/env python
import sys
import rospy
from primer_ejemplo.srv import AddTwoInts, AddTwoIntsRequest, AddTwoIntsResponse

def add_two_ints_client(x: int, y: int):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp: AddTwoIntsResponse = add_two_ints(x, y)
        return resp.sum
    except rospy.ServiceException as e:
        print('Service call failed: %s' % e)

def usage():
    return '%s [x y]' % sys.argv[0]
    
if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print('Requesting %d+%d' % (x, y))
    print('%d + %d = %d' % (x, y, add_two_ints_client(x, y)))
