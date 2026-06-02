import rclpy # importe la bibliothèque principale de ROS2 (ensemble des outils nécéssaire en application robotique)
from rclpy.node import Node # importe une classe node 
from std_msgs.msg import String # permet d'importer le type du message et indique avec msgs.msg que le message envoyé est une chaine de caractères 

class MinimalPublisher(Node):# Création de la classe Noeud publisher 

    def __init__(self):
        super().__init__('minimal_publisher')# donne un nom au noeud à travers le constructeur de la classe mère Node 
        self.publisher_ = self.create_publisher(String, 'topic', 10)# permet la création du publisher en lui apportant le type de message envoyé, le nom du topic et le nombre de paquets qui peut stationner en file d'attente (paramètre QoS)
        timer_period = 0.5 # permet de définir la période d'envoi du message du timer. Par exemple ici on enverra un message toute les demi secondes
        self.timer = self.create_timer(timer_period, self.timer_callback)# permet la création du timer (self.timer_callbck signifie que le timer sera rappelé automatiquement)
        self.i = 0 # initialise un compteur à 0 (initialisation du timer)

    def timer_callback(self):
        msg=String() # créer un message avec le tyoe String
        msg.data = 'Hello World: %d' % self.i = # définition du contenu du message puis définition du compteur qui permettra de savoir combien de fois on a envoyé le message
        self.publisher_.publish(msg) # envoie un message sur le topic
        self.get_logger().info('Publishing: "%s"' % msg.data) # permet d'avoir des logins messages. Autrement dit cela permet de voir si le message a été publié
        self.i +=1 # Augmente le compteur de 1. 

def main(args=None):# Fonction permettant l'execution du programme
    rclpy.init(args=args)#Permet d'initier la communication en ROS2
    minimal_publisher = MinimalPublisher()# permet la création de l'objet publisher 
    rclpy.spin(minimal_publisher)# maintien l objet publisher actif et permet entre temps à ROS2 de surveiller l'envoi des message et lancer timer callback
    minimal_publisher.destroy_node() # permet de détruire le publisher et le timer crée
    rclpy.shutdown()# fermeture du système ROS2

if __name__ == '__main__':
    main()