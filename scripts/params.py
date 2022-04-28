#!/usr/bin/env python
import rospy

if __name__ == '__main__':
    rospy.init_node('parameter_getter', anonymous=True)
    if rospy.has_param('my_param'):
        value = rospy.get_param('my_param', 'default_value')
        rospy.loginfo(f'my_param: {value}')

    else:
        rospy.logwarn('my_param is not set, setting default in server: hello ')
        rospy.set_param('my_param', 'hello')
