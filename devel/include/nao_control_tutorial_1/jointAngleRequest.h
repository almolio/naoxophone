// Generated by gencpp from file nao_control_tutorial_1/jointAngleRequest.msg
// DO NOT EDIT!


#ifndef NAO_CONTROL_TUTORIAL_1_MESSAGE_JOINTANGLEREQUEST_H
#define NAO_CONTROL_TUTORIAL_1_MESSAGE_JOINTANGLEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace nao_control_tutorial_1
{
template <class ContainerAllocator>
struct jointAngleRequest_
{
  typedef jointAngleRequest_<ContainerAllocator> Type;

  jointAngleRequest_()
    : name()
    , angle(0.0)
    , speed(0.0)  {
    }
  jointAngleRequest_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , angle(0.0)
    , speed(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef float _angle_type;
  _angle_type angle;

   typedef float _speed_type;
  _speed_type speed;





  typedef boost::shared_ptr< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> const> ConstPtr;

}; // struct jointAngleRequest_

typedef ::nao_control_tutorial_1::jointAngleRequest_<std::allocator<void> > jointAngleRequest;

typedef boost::shared_ptr< ::nao_control_tutorial_1::jointAngleRequest > jointAngleRequestPtr;
typedef boost::shared_ptr< ::nao_control_tutorial_1::jointAngleRequest const> jointAngleRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace nao_control_tutorial_1

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "085e83dd6a2897e863bc27547862deee";
  }

  static const char* value(const ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x085e83dd6a2897e8ULL;
  static const uint64_t static_value2 = 0x63bc27547862deeeULL;
};

template<class ContainerAllocator>
struct DataType< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "nao_control_tutorial_1/jointAngleRequest";
  }

  static const char* value(const ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
string      name\n\
float32    angle\n\
float32    speed\n\
\n\
";
  }

  static const char* value(const ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.angle);
      stream.next(m.speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct jointAngleRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::nao_control_tutorial_1::jointAngleRequest_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "angle: ";
    Printer<float>::stream(s, indent + "  ", v.angle);
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NAO_CONTROL_TUTORIAL_1_MESSAGE_JOINTANGLEREQUEST_H
