// Generated by gencpp from file nao_control_tutorial_1/timedInterpolationRequest.msg
// DO NOT EDIT!


#ifndef NAO_CONTROL_TUTORIAL_1_MESSAGE_TIMEDINTERPOLATIONREQUEST_H
#define NAO_CONTROL_TUTORIAL_1_MESSAGE_TIMEDINTERPOLATIONREQUEST_H


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
struct timedInterpolationRequest_
{
  typedef timedInterpolationRequest_<ContainerAllocator> Type;

  timedInterpolationRequest_()
    : names()
    , angleLists()
    , times()  {
    }
  timedInterpolationRequest_(const ContainerAllocator& _alloc)
    : names(_alloc)
    , angleLists(_alloc)
    , times(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _names_type;
  _names_type names;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _angleLists_type;
  _angleLists_type angleLists;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _times_type;
  _times_type times;





  typedef boost::shared_ptr< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> const> ConstPtr;

}; // struct timedInterpolationRequest_

typedef ::nao_control_tutorial_1::timedInterpolationRequest_<std::allocator<void> > timedInterpolationRequest;

typedef boost::shared_ptr< ::nao_control_tutorial_1::timedInterpolationRequest > timedInterpolationRequestPtr;
typedef boost::shared_ptr< ::nao_control_tutorial_1::timedInterpolationRequest const> timedInterpolationRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "14f1208cf1fdbcb6fb75913ee7ea20cb";
  }

  static const char* value(const ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x14f1208cf1fdbcb6ULL;
  static const uint64_t static_value2 = 0xfb75913ee7ea20cbULL;
};

template<class ContainerAllocator>
struct DataType< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "nao_control_tutorial_1/timedInterpolationRequest";
  }

  static const char* value(const ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
string      names\n\
string      angleLists\n\
string      times\n\
\n\
";
  }

  static const char* value(const ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.names);
      stream.next(m.angleLists);
      stream.next(m.times);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct timedInterpolationRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::nao_control_tutorial_1::timedInterpolationRequest_<ContainerAllocator>& v)
  {
    s << indent << "names: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.names);
    s << indent << "angleLists: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.angleLists);
    s << indent << "times: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.times);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NAO_CONTROL_TUTORIAL_1_MESSAGE_TIMEDINTERPOLATIONREQUEST_H
