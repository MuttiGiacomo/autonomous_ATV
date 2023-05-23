# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from wireless_remote_controller/movement.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class movement(genpy.Message):
  _md5sum = "0c6fee59201861cdecc9b5d349f15d08"
  _type = "wireless_remote_controller/movement"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint16 speed_command
int16 angle_of_correction
string forward_reverse
"""
  __slots__ = ['speed_command','angle_of_correction','forward_reverse']
  _slot_types = ['uint16','int16','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       speed_command,angle_of_correction,forward_reverse

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(movement, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.speed_command is None:
        self.speed_command = 0
      if self.angle_of_correction is None:
        self.angle_of_correction = 0
      if self.forward_reverse is None:
        self.forward_reverse = ''
    else:
      self.speed_command = 0
      self.angle_of_correction = 0
      self.forward_reverse = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_Hh().pack(_x.speed_command, _x.angle_of_correction))
      _x = self.forward_reverse
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.speed_command, _x.angle_of_correction,) = _get_struct_Hh().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.forward_reverse = str[start:end].decode('utf-8')
      else:
        self.forward_reverse = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_Hh().pack(_x.speed_command, _x.angle_of_correction))
      _x = self.forward_reverse
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.speed_command, _x.angle_of_correction,) = _get_struct_Hh().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.forward_reverse = str[start:end].decode('utf-8')
      else:
        self.forward_reverse = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Hh = None
def _get_struct_Hh():
    global _struct_Hh
    if _struct_Hh is None:
        _struct_Hh = struct.Struct("<Hh")
    return _struct_Hh