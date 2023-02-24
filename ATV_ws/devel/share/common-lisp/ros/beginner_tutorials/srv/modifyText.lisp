; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-srv)


;//! \htmlinclude modifyText-request.msg.html

(cl:defclass <modifyText-request> (roslisp-msg-protocol:ros-message)
  ((inputString
    :reader inputString
    :initarg :inputString
    :type cl:string
    :initform ""))
)

(cl:defclass modifyText-request (<modifyText-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <modifyText-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'modifyText-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-srv:<modifyText-request> is deprecated: use beginner_tutorials-srv:modifyText-request instead.")))

(cl:ensure-generic-function 'inputString-val :lambda-list '(m))
(cl:defmethod inputString-val ((m <modifyText-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:inputString-val is deprecated.  Use beginner_tutorials-srv:inputString instead.")
  (inputString m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <modifyText-request>) ostream)
  "Serializes a message object of type '<modifyText-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'inputString))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'inputString))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <modifyText-request>) istream)
  "Deserializes a message object of type '<modifyText-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'inputString) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'inputString) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<modifyText-request>)))
  "Returns string type for a service object of type '<modifyText-request>"
  "beginner_tutorials/modifyTextRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'modifyText-request)))
  "Returns string type for a service object of type 'modifyText-request"
  "beginner_tutorials/modifyTextRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<modifyText-request>)))
  "Returns md5sum for a message object of type '<modifyText-request>"
  "2ea50b9bce33ae6fad63d90c193917b0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'modifyText-request)))
  "Returns md5sum for a message object of type 'modifyText-request"
  "2ea50b9bce33ae6fad63d90c193917b0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<modifyText-request>)))
  "Returns full string definition for message of type '<modifyText-request>"
  (cl:format cl:nil "#request~%string inputString~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'modifyText-request)))
  "Returns full string definition for message of type 'modifyText-request"
  (cl:format cl:nil "#request~%string inputString~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <modifyText-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'inputString))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <modifyText-request>))
  "Converts a ROS message object to a list"
  (cl:list 'modifyText-request
    (cl:cons ':inputString (inputString msg))
))
;//! \htmlinclude modifyText-response.msg.html

(cl:defclass <modifyText-response> (roslisp-msg-protocol:ros-message)
  ((modifiedString
    :reader modifiedString
    :initarg :modifiedString
    :type cl:string
    :initform ""))
)

(cl:defclass modifyText-response (<modifyText-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <modifyText-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'modifyText-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-srv:<modifyText-response> is deprecated: use beginner_tutorials-srv:modifyText-response instead.")))

(cl:ensure-generic-function 'modifiedString-val :lambda-list '(m))
(cl:defmethod modifiedString-val ((m <modifyText-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:modifiedString-val is deprecated.  Use beginner_tutorials-srv:modifiedString instead.")
  (modifiedString m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <modifyText-response>) ostream)
  "Serializes a message object of type '<modifyText-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'modifiedString))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'modifiedString))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <modifyText-response>) istream)
  "Deserializes a message object of type '<modifyText-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'modifiedString) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'modifiedString) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<modifyText-response>)))
  "Returns string type for a service object of type '<modifyText-response>"
  "beginner_tutorials/modifyTextResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'modifyText-response)))
  "Returns string type for a service object of type 'modifyText-response"
  "beginner_tutorials/modifyTextResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<modifyText-response>)))
  "Returns md5sum for a message object of type '<modifyText-response>"
  "2ea50b9bce33ae6fad63d90c193917b0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'modifyText-response)))
  "Returns md5sum for a message object of type 'modifyText-response"
  "2ea50b9bce33ae6fad63d90c193917b0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<modifyText-response>)))
  "Returns full string definition for message of type '<modifyText-response>"
  (cl:format cl:nil "#response~%string modifiedString~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'modifyText-response)))
  "Returns full string definition for message of type 'modifyText-response"
  (cl:format cl:nil "#response~%string modifiedString~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <modifyText-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'modifiedString))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <modifyText-response>))
  "Converts a ROS message object to a list"
  (cl:list 'modifyText-response
    (cl:cons ':modifiedString (modifiedString msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'modifyText)))
  'modifyText-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'modifyText)))
  'modifyText-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'modifyText)))
  "Returns string type for a service object of type '<modifyText>"
  "beginner_tutorials/modifyText")