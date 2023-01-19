#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/features2d.hpp>
#include <opencv2/core/matx.hpp>
#include <opencv2/video/tracking.hpp>
#include <math.h>
#include <aruco/aruco.h>

static const std::string OPENCV_WINDOW = "RGB";

class MarkerTracker
{
  // ros::NodeHandle nh_;
  image_transport::ImageTransport it_;
  image_transport::Subscriber image_sub_top;
  image_transport::Publisher image_pub_;
 
  // marker detection
  aruco::CameraParameters TheCameraParameters;
  std::vector<int> markerIds;
  std::vector<aruco::Marker> detectedMarkers;
  
public:
  MarkerTracker(ros::NodeHandle &n)
    : it_(n)
  {
    // Subscribe to input top video feed and show the 3 formats (RGB, grey, binary)
    cv::namedWindow(OPENCV_WINDOW);

    // it_ = n;

    // Init ArUco 3D Marker Detection
    initTopCamParams();

    image_sub_top = it_.subscribe("/nao_robot/camera/top/camera/image_raw", 1, &MarkerTracker::topImageCb, this); 
  }

  ~MarkerTracker()
  {
    cv::destroyWindow(OPENCV_WINDOW);
  }

  void initTopCamParams(){
    // load the parameter matrix in the constructor
    cv::Mat dist = cv::Mat(1,5,CV_32FC1);
    dist.at<float>(0,0)=-0.066494;
    dist.at<float>(0,1)=0.095481;
    dist.at<float>(0,2)=-0.000279;
    dist.at<float>(0,3)=0.002292;
    dist.at<float>(0,4)=0.000000;

    cv::Mat cameraP = cv::Mat(3,3,CV_32FC1);
    cameraP.at<float>(0,0)=551.543059;
    cameraP.at<float>(0,1)=0.000000;
    cameraP.at<float>(0,2)=327.382898;
    cameraP.at<float>(1,0)=0.000000;
    cameraP.at<float>(1,1)=553.736023;
    cameraP.at<float>(1,2)=225.026380;
    cameraP.at<float>(2,0)=0.000000;
    cameraP.at<float>(2,1)=0.000000;
    cameraP.at<float>(2,2)=1.000000;

    TheCameraParameters.setParams(cameraP,dist,cv::Size(640,480));
    TheCameraParameters.resize(cv::Size(640,480));
  }

  void runMarkerTracking(cv_bridge::CvImagePtr cv_ptr)
  {
    cv::Mat img = cv_ptr->image.clone();

    // detect markers
    aruco::MarkerDetector detector = aruco::MarkerDetector();
    detector.detect(img, detectedMarkers, TheCameraParameters, 0.09);
    
    // Draw markers on image and print position
    for (int i = 0; i < detectedMarkers.size(); i++)
    {
      detectedMarkers[i].draw(img, cv::Scalar(0,0,255));
      
      double pos[3], orie[4];
      detectedMarkers[i].OgreGetPoseParameters(pos,orie);
      
      std::cout << "pos [x: " <<pos[0] <<", y: "<<pos[1]<<", z: "<<pos[2] <<"]"  << std::endl ;
      
      double yawOffset, pitchOffset;
      double deadzone = 3.0;

      yawOffset = atan(pos[0]/pos[2]) * 180 / CV_PI;
      if (abs(yawOffset) < deadzone) {
        yawOffset = 0;
      } 

      pitchOffset = -atan(pos[1]/pos[2]) * 180 / CV_PI;
      if (abs(pitchOffset) < deadzone) {
        pitchOffset = 0;
      } 
      
      std::cout << "yaw: " << yawOffset <<", pitch: "<<pitchOffset << std::endl ;


    }
    
    cv::imshow(OPENCV_WINDOW,img);
    cv::moveWindow(OPENCV_WINDOW, 1300, 700);
  }

  void topImageCb(const sensor_msgs::ImageConstPtr& msg)
  {
      cv_bridge::CvImagePtr cv_ptr;
      try
      {
          cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
      }
      catch (cv_bridge::Exception& e)
      {
          ROS_ERROR("cv_bridge exception: %s", e.what());
          return;
      }

      //////// 3D MARKER DETECTION ////////
      runMarkerTracking(cv_ptr);

      cv::waitKey(3);
  }
};
