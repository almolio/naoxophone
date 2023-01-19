#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
#include <ros/ros.h>
#include "sensor_msgs/JointState.h"
#include <std_srvs/Empty.h>
#include "nao_control_tutorial_1/MoveJoints.h"
#include "nao_control_tutorial_1/InterpolateJoints.h"
#include <string.h>

#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/features2d.hpp>
#include <opencv2/core/matx.hpp>
#include <opencv2/video/tracking.hpp>
#include <aruco/aruco.h>

const char MODE_1[] = "move_arms";
const char MODE_2[] = "interpolate";
const char MODE_3[] = "tracker";



static const std::string OPENCV_WINDOW = "RGB";
aruco::CameraParameters cp;
ros::ServiceClient move_client;
ros::ServiceClient interpolate_client;

void enable_stiffness(ros::NodeHandle &n)
{
    std_srvs::Empty a;
    ros::ServiceClient stiffness_enable = n.serviceClient<std_srvs::Empty>("/body_stiffness/enable");
    stiffness_enable.call(a);
}

void disable_stiffness(ros::NodeHandle &n)
{   
    std_srvs::Empty a;
    ros::ServiceClient stiffness_disable = n.serviceClient<std_srvs::Empty>("/body_stiffness/disable");
    stiffness_disable.call(a);
} 

void move_arms(ros::NodeHandle &n)
{
    //enable_stiffness(n);

    // Move joints
    ros::ServiceClient move_client = n.serviceClient<nao_control_tutorial_1::MoveJoints>("/move_server");
    nao_control_tutorial_1::MoveJoints srv;
    srv.request.joint_name = "LShoulderPitch";
    srv.request.angle = -100.0;
    srv.request.speed = 0.5;
    srv.request.relative = false;
    move_client.call(srv);

    srv.request.joint_name = "RShoulderPitch";
    srv.request.angle = -100.0;
    move_client.call(srv);

    ros::Duration(3.0).sleep();
    //disable_stiffness(n);
}

void move_arms_interpolated(ros::NodeHandle &n)
{
    ros::ServiceClient interpolate_client = n.serviceClient<nao_control_tutorial_1::InterpolateJoints>("/interpolate_server");

    std::vector<std::string> names;
    names.push_back("LShoulderRoll");
    names.push_back("LShoulderPitch");
    
    std::vector<float> angles;
    angles.push_back(30.0);
    angles.push_back(0.0);
    std::vector<float> times;
    times.push_back(2.0);
    times.push_back(1.0);
    std::vector<int> steps;
    steps.push_back(1);
    steps.push_back(1);
    
    nao_control_tutorial_1::InterpolateJoints srv;
    srv.request.joint_names = names;
    srv.request.angles = angles;
    srv.request.times = times;
    srv.request.steps = steps;
    srv.request.relative = false;
    srv.request.blocking = true;

    interpolate_client.call(srv);
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

    cp.setParams(cameraP,dist,cv::Size(640,480));
    cp.resize(cv::Size(640,480));
}

void move_head(double yawOffset, double pitchOffset)
{
    // Move joints
    nao_control_tutorial_1::MoveJoints srv;
    srv.request.joint_name = "HeadPitch";
    srv.request.angle = pitchOffset;
    srv.request.speed = 0.05;
    srv.request.relative = true;
    move_client.call(srv);

    srv.request.joint_name = "HeadYaw";
    srv.request.angle = yawOffset;
    srv.request.relative = true;
    move_client.call(srv);

   //ros::Duration(3.0).sleep();
}

void move_head_interpolate(double yawOffset, double pitchOffset)
{
    std::vector<std::string> names;
    names.push_back("HeadPitch");
    names.push_back("HeadYaw");
    
    std::vector<float> angles;
    angles.push_back(pitchOffset);
    angles.push_back(yawOffset);
    std::vector<float> times;
    times.push_back(0.2);
    times.push_back(0.2);
    std::vector<int> steps;
    steps.push_back(1);
    steps.push_back(1);
    
    nao_control_tutorial_1::InterpolateJoints srv;
    srv.request.joint_names = names;
    srv.request.angles = angles;
    srv.request.times = times;
    srv.request.steps = steps;
    srv.request.relative = true;
    srv.request.blocking = false;

    interpolate_client.call(srv);
}

void runMarkerTracking(cv_bridge::CvImagePtr cv_ptr)
  {
    cv::Mat img = cv_ptr->image.clone();

    // detect markers
    std::vector<aruco::Marker> detectedMarkers;
    double yawOffset, pitchOffset;

    aruco::MarkerDetector detector = aruco::MarkerDetector();
    detector.detect(img, detectedMarkers, cp, 0.1);
    
    // Draw markers on image and print position
    for (int i = 0; i < detectedMarkers.size(); i++)
    {
        detectedMarkers[i].draw(img, cv::Scalar(0,0,255));

        double pos[3], orie[4];
        detectedMarkers[i].OgreGetPoseParameters(pos,orie);

        //std::cout << "pos [x: " << pos[0] <<", y: "<<pos[1]<<", z: "<<pos[2] <<"]"  << std::endl ;


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

    if(detectedMarkers.size() > 0)
    {
        // move_head(yawOffset, pitchOffset);
        move_head_interpolate(yawOffset, pitchOffset);
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

    std::string OPENCV_WINDOW = "RGB";
    cv::imshow(OPENCV_WINDOW,cv_ptr->image);
    cv::moveWindow(OPENCV_WINDOW, 1300, 700);
    cv::waitKey(3);
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "move_client");
    ros::NodeHandle n;
    move_client = n.serviceClient<nao_control_tutorial_1::MoveJoints>("/move_server");
    interpolate_client = n.serviceClient<nao_control_tutorial_1::InterpolateJoints>("/interpolate_server");

    if (argc < 2)
    {
        ROS_ERROR("Please Specify Action from: move_arms, interpolate, tracker");
    }
    
    std::cout << argv[0] << " " << argv[1] << std::endl;

    if (strcmp(argv[1], MODE_1) == 0)
    {   
        ROS_INFO("in move arms");
        move_arms(n);        
    } else if (strcmp(argv[1], MODE_2) == 0) 
    {
        ROS_INFO("in interpolate arms.");
        move_arms_interpolated(n);
    } else if (strcmp(argv[1], MODE_3) == 0)
    {
        initTopCamParams();

        ros::Subscriber image_sub_top;
        image_sub_top = n.subscribe("/nao_robot/camera/top/camera/image_raw", 1, topImageCb);
        ros::spin();
    }

    
  return 0;
}



