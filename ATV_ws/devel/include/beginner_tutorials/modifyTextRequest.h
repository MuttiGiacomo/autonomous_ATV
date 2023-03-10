// Generated by gencpp from file beginner_tutorials/modifyTextRequest.msg
// DO NOT EDIT!


#ifndef BEGINNER_TUTORIALS_MESSAGE_MODIFYTEXTREQUEST_H
#define BEGINNER_TUTORIALS_MESSAGE_MODIFYTEXTREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace beginner_tutorials
{
template <class ContainerAllocator>
struct modifyTextRequest_
{
  typedef modifyTextRequest_<ContainerAllocator> Type;

  modifyTextRequest_()
    : inputString()  {
    }
  modifyTextRequest_(const ContainerAllocator& _alloc)
    : inputString(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _inputString_type;
  _inputString_type inputString;





  typedef boost::shared_ptr< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> const> ConstPtr;

}; // struct modifyTextRequest_

typedef ::beginner_tutorials::modifyTextRequest_<std::allocator<void> > modifyTextRequest;

typedef boost::shared_ptr< ::beginner_tutorials::modifyTextRequest > modifyTextRequestPtr;
typedef boost::shared_ptr< ::beginner_tutorials::modifyTextRequest const> modifyTextRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator1> & lhs, const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator2> & rhs)
{
  return lhs.inputString == rhs.inputString;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator1> & lhs, const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace beginner_tutorials

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "998e350d95d4a84f3e250cb220ede566";
  }

  static const char* value(const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x998e350d95d4a84fULL;
  static const uint64_t static_value2 = 0x3e250cb220ede566ULL;
};

template<class ContainerAllocator>
struct DataType< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "beginner_tutorials/modifyTextRequest";
  }

  static const char* value(const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#request\n"
"string inputString\n"
;
  }

  static const char* value(const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.inputString);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct modifyTextRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::beginner_tutorials::modifyTextRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::beginner_tutorials::modifyTextRequest_<ContainerAllocator>& v)
  {
    s << indent << "inputString: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.inputString);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEGINNER_TUTORIALS_MESSAGE_MODIFYTEXTREQUEST_H
