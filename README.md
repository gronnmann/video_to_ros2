# video_to_ros2
Allows publishing video files to ros2 nodes, as well as previewing sensor_msgs/Image nodes.
Contains two nodes, video_publisher and video_preview.

## Requirements
The node requires ROS2, OpenCV as well as cv_bridge installed.

## video_publisher
Lets you push a file as a camera feed to ROS2. Also works with images, outputting them with 60 fps.
Parameters:
- otopic_video - Name of topic node publishes to (string)
  - default: "/video"
- ifile_video - Path to video to publish
  - default: "videos/video.mp4"

## video_preview
Lets you preview video form a camera feed in ROS2. 
Parameters:
- itopic_video - Name of topic node subscribes to (string)
  - default: "/video"
