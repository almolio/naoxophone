// Generated by gencpp from file nao_control_tutorial_2/MoveJointsRequest.msg
// DO NOT EDIT!


#ifndef NAO_CONTROL_TUTORIAL_2_MESSAGE_MOVEJOINTSREQUEST_H
#define NAO_CONTROL_TUTORIAL_2_MESSAGE_MOVEJOINTSREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace nao_control_tutorial_2
{
template <class ContainerAllocator>
struct MoveJointsRequest_
{
  typedef MoveJointsRequest_<ContainerAllocator> Type;

  MoveJointsRequest_()
    : joint_name()
    , x_pos()
    , y_pos()
    , z_pos()
    , x_rot()
    , y_rot()
    , z_rot()
    , max_vel()
    , exe_time()  {
    }
  MoveJointsRequest_(const ContainerAllocator& _alloc)
    : joint_name(_alloc)
    , x_pos(_alloc)
    , y_pos(_alloc)
    , z_pos(_alloc)
    , x_rot(_alloc)
    , y_rot(_alloc)
    , z_rot(_alloc)
    , max_vel(_alloc)
    , exe_time(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _joint_name_type;
  _joint_name_type joint_name;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _x_pos_type;
  _x_pos_type x_pos;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _y_pos_type;
  _y_pos_type y_pos;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _z_pos_type;
  _z_pos_type z_pos;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _x_rot_type;
  _x_rot_type x_rot;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _y_rot_type;
  _y_rot_type y_rot;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _z_rot_type;
  _z_rot_type z_rot;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _max_vel_type;
  _max_vel_type max_vel;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _exe_time_type;
  _exe_time_type exe_time;





  typedef boost::shared_ptr< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MoveJointsRequest_

typedef ::nao_control_tutorial_2::MoveJointsRequest_<std::allocator<void> > MoveJointsRequest;

typedef boost::shared_ptr< ::nao_control_tutorial_2::MoveJointsRequest > MoveJointsRequestPtr;
typedef boost::shared_ptr< ::nao_control_tutorial_2::MoveJointsRequest const> MoveJointsRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace nao_control_tutorial_2

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bdc252503ebb73978a5304b525aec785";
  }

  static const char* value(const ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbdc252503ebb7397ULL;
  static const uint64_t static_value2 = 0x8a5304b525aec785ULL;
};

template<class ContainerAllocator>
struct DataType< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "nao_control_tutorial_2/MoveJointsRequest";
  }

  static const char* value(const ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
string joint_name\n\
string x_pos\n\
string y_pos\n\
string z_pos\n\
string x_rot\n\
string y_rot\n\
string z_rot\n\
string max_vel\n\
string exe_time\n\
";
  }

  static const char* value(const ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.joint_name);
      stream.next(m.x_pos);
      stream.next(m.y_pos);
      stream.next(m.z_pos);
      stream.next(m.x_rot);
      stream.next(m.y_rot);
      stream.next(m.z_rot);
      stream.next(m.max_vel);
      stream.next(m.exe_time);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveJointsRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::nao_control_tutorial_2::MoveJointsRequest_<ContainerAllocator>& v)
  {
    s << indent << "joint_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.joint_name);
    s << indent << "x_pos: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.x_pos);
    s << indent << "y_pos: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.y_pos);
    s << indent << "z_pos: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.z_pos);
    s << indent << "x_rot: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.x_rot);
    s << indent << "y_rot: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.y_rot);
    s << indent << "z_rot: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.z_rot);
    s << indent << "max_vel: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.max_vel);
    s << indent << "exe_time: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.exe_time);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NAO_CONTROL_TUTORIAL_2_MESSAGE_MOVEJOINTSREQUEST_H
