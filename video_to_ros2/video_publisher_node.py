import time

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class VideoPublisher(Node):
    def __init__(self):
        super().__init__(node_name="video_publisher")
        # TODO - change parameters
        self.declare_parameter("otopic_video", "/video")
        self.otopic_video = self.get_parameter("otopic_video").value

        self.cv_bridge = CvBridge()

        self.frame_publisher = self.create_publisher(
            Image,
            self.otopic_video,
            0
        )

        self.declare_parameter("ifile_video", "videos/video.mp4")
        self.ifile_video = self.get_parameter("ifile_video").value

        self.load_video()

    def publish_frames(self, opencv_img):
        img_msg: Image = self.cv_bridge.cv2_to_imgmsg(opencv_img, encoding="passthrough")

        self.frame_publisher.publish(img_msg)

    def load_video(self):
        capture = cv2.VideoCapture(self.ifile_video)

        if not capture.isOpened():
            self.get_logger().error("Failed to open video file...")
            return

        video_fps = capture.get(cv2.CAP_PROP_FPS)

        video_frame_time = (1.0 / video_fps) * 1000.0
        self.get_logger().info(f"Using video fps {video_fps}, frametime {video_frame_time}")

        while capture.isOpened():

            next_frame = time.time() + video_frame_time

            ret, frame = capture.read()
            self.publish_frames(frame)

            curr_time = time.time()

            # Wait if still not time for next frame
            if curr_time < next_frame:
                wait_time = next_frame - curr_time
                # self.get_logger().info(f"Loading took less time than expected. Waiting {wait_time} ms")
                time.sleep(1.0/wait_time)


            if not ret:
                break

        capture.release()
        self.get_logger().info("Video finished.")


def main(args=None):
    rclpy.init(args=args)
    reciever = VideoPublisher()
    rclpy.spin(reciever)
    reciever.destroy_node()
    rclpy.shutdown()
