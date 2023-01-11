import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoReceiver(Node):
    def __init__(self):
        super().__init__(node_name="video_preview")
        # TODO - change parameters
        self.declare_parameter("itopic_video", "/video")
        self.itopic_video = self.get_parameter("itopic_video").value

        self.cv_bridge = CvBridge()

        self.frame_subscriber = self.create_subscription(
            Image,
            self.itopic_video,
            self.frame_received,
            0
        )

    def frame_received(self, img_msg: Image):
        img = self.cv_bridge.imgmsg_to_cv2(img_msg)
        cv2.imshow("Video preview", img)
        cv2.waitKey(1)



def main(args=None):
    rclpy.init(args=args)
    reciever = VideoReceiver()
    rclpy.spin(reciever)
    reciever.destroy_node()
    rclpy.shutdown()