; Auto-generated. Do not edit!


(cl:in-package api_move-msg)


;//! \htmlinclude movement.msg.html

(cl:defclass <movement> (roslisp-msg-protocol:ros-message)
  ((speed_command
    :reader speed_command
    :initarg :speed_command
    :type cl:fixnum
    :initform 0)
   (angle_of_correction
    :reader angle_of_correction
    :initarg :angle_of_correction
    :type cl:fixnum
    :initform 0)
   (forward_reverse
    :reader forward_reverse
    :initarg :forward_reverse
    :type cl:string
    :initform ""))
)

(cl:defclass movement (<movement>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <movement>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'movement)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name api_move-msg:<movement> is deprecated: use api_move-msg:movement instead.")))

(cl:ensure-generic-function 'speed_command-val :lambda-list '(m))
(cl:defmethod speed_command-val ((m <movement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader api_move-msg:speed_command-val is deprecated.  Use api_move-msg:speed_command instead.")
  (speed_command m))

(cl:ensure-generic-function 'angle_of_correction-val :lambda-list '(m))
(cl:defmethod angle_of_correction-val ((m <movement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader api_move-msg:angle_of_correction-val is deprecated.  Use api_move-msg:angle_of_correction instead.")
  (angle_of_correction m))

(cl:ensure-generic-function 'forward_reverse-val :lambda-list '(m))
(cl:defmethod forward_reverse-val ((m <movement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader api_move-msg:forward_reverse-val is deprecated.  Use api_move-msg:forward_reverse instead.")
  (forward_reverse m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <movement>) ostream)
  "Serializes a message object of type '<movement>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed_command)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed_command)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'angle_of_correction)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'forward_reverse))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'forward_reverse))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <movement>) istream)
  "Deserializes a message object of type '<movement>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed_command)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed_command)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angle_of_correction) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'forward_reverse) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'forward_reverse) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<movement>)))
  "Returns string type for a message object of type '<movement>"
  "api_move/movement")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'movement)))
  "Returns string type for a message object of type 'movement"
  "api_move/movement")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<movement>)))
  "Returns md5sum for a message object of type '<movement>"
  "0c6fee59201861cdecc9b5d349f15d08")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'movement)))
  "Returns md5sum for a message object of type 'movement"
  "0c6fee59201861cdecc9b5d349f15d08")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<movement>)))
  "Returns full string definition for message of type '<movement>"
  (cl:format cl:nil "uint16 speed_command~%int16 angle_of_correction~%string forward_reverse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'movement)))
  "Returns full string definition for message of type 'movement"
  (cl:format cl:nil "uint16 speed_command~%int16 angle_of_correction~%string forward_reverse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <movement>))
  (cl:+ 0
     2
     2
     4 (cl:length (cl:slot-value msg 'forward_reverse))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <movement>))
  "Converts a ROS message object to a list"
  (cl:list 'movement
    (cl:cons ':speed_command (speed_command msg))
    (cl:cons ':angle_of_correction (angle_of_correction msg))
    (cl:cons ':forward_reverse (forward_reverse msg))
))
