#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from ATV_control.msg import Steer
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Control Your Car!
---------------------------
Moving around:
        w
   a    s    d
        x

w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
space key, s : force stop
CTRL-C to quit
"""

moveBindings = {
        'w':(1,0),
        'x':(-1,0),
        'a':(0,1),
        'd':(0,-1),
    }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'e':(1.1,.9),
        'c':(.9,1.1),
        ' ':(0,0)
    }

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 5
turn = 20

def vels(speed,turn):
    return "currently:\tspeed %s\tturn radius %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('keyboard_teleop')
    pub = rospy.Publisher('/cmd_steer', Steer, queue_size=1)

    x = 0
    r = 0
    status = 0

    max_vel = 50
    min_r = 3

    try:
        print(msg)
        print(vels(speed,turn))
        while(1):
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]*speed
                r = moveBindings[key][1]*turn
                if (r>0 and r<3) or (r>-3 and r<0):
                    r = 100000
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]

                print(vels(speed,turn))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
            else:
                x = 0
                r = 1000
                if (key == '\x03'):
                    break
            steer = Steer()
            steer.lin_velocity = min(x*speed,max_vel)
            steer.turn_radius = max(r*turn,min_r)
            pub.publish(steer)

    except Exception as e:
        print(e)

    finally:
        steer = Steer()
        steer.lin_velocity = 0
        steer.turn_radius = 1000
        pub.publish(steer)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
