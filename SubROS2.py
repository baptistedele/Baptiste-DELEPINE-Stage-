## : signifie que la commande a déjà été expliquer sur le Pub ROS2

import rclpy ##
from rclpy.node import Node ##
from std_msgs.msg import String ##

class MinimalSubscriber(Node):##
    def __init__(self):##
        super().__init__('minimal_subscriber')##
        self.subscription = self.create_subscription(String,'topic', self.listener_callback, 10)# permet la création du subscriber en lui apportant le type de message envoyé, le nom du topic et le nombre de paquets qui peut stationner en file d'attente (paramètre QoS)


    def listener_callback(self,msg):##
        
        self.get_logger().info('I heard: "%s"' % msg.data)##

def main(args=None):##
    rclpy.init(args=args)##
    minimal_subscriber = MinimalSubscriber()##
    rclpy.spin(minimal_subscriber)##
    minimal_subscriber.destroy_node()##
    rclpy.shutdown()##

if __name__ == '__main__':
    main()