; Auto-generated. Do not edit!


(cl:in-package nao_control_tutorial_1-srv)


;//! \htmlinclude timedInterpolation-request.msg.html

(cl:defclass <timedInterpolation-request> (roslisp-msg-protocol:ros-message)
  ((names
    :reader names
    :initarg :names
    :type cl:string
    :initform "")
   (angleLists
    :reader angleLists
    :initarg :angleLists
    :type cl:string
    :initform "")
   (times
    :reader times
    :initarg :times
    :type cl:string
    :initform ""))
)

(cl:defclass timedInterpolation-request (<timedInterpolation-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <timedInterpolation-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'timedInterpolation-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control_tutorial_1-srv:<timedInterpolation-request> is deprecated: use nao_control_tutorial_1-srv:timedInterpolation-request instead.")))

(cl:ensure-generic-function 'names-val :lambda-list '(m))
(cl:defmethod names-val ((m <timedInterpolation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:names-val is deprecated.  Use nao_control_tutorial_1-srv:names instead.")
  (names m))

(cl:ensure-generic-function 'angleLists-val :lambda-list '(m))
(cl:defmethod angleLists-val ((m <timedInterpolation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:angleLists-val is deprecated.  Use nao_control_tutorial_1-srv:angleLists instead.")
  (angleLists m))

(cl:ensure-generic-function 'times-val :lambda-list '(m))
(cl:defmethod times-val ((m <timedInterpolation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:times-val is deprecated.  Use nao_control_tutorial_1-srv:times instead.")
  (times m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <timedInterpolation-request>) ostream)
  "Serializes a message object of type '<timedInterpolation-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'names))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'names))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'angleLists))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'angleLists))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'times))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'times))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <timedInterpolation-request>) istream)
  "Deserializes a message object of type '<timedInterpolation-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'names) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'names) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angleLists) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'angleLists) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'times) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'times) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<timedInterpolation-request>)))
  "Returns string type for a service object of type '<timedInterpolation-request>"
  "nao_control_tutorial_1/timedInterpolationRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'timedInterpolation-request)))
  "Returns string type for a service object of type 'timedInterpolation-request"
  "nao_control_tutorial_1/timedInterpolationRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<timedInterpolation-request>)))
  "Returns md5sum for a message object of type '<timedInterpolation-request>"
  "062c7554adac44a703a2883e86bbb559")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'timedInterpolation-request)))
  "Returns md5sum for a message object of type 'timedInterpolation-request"
  "062c7554adac44a703a2883e86bbb559")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<timedInterpolation-request>)))
  "Returns full string definition for message of type '<timedInterpolation-request>"
  (cl:format cl:nil "~%string      names~%string      angleLists~%string      times~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'timedInterpolation-request)))
  "Returns full string definition for message of type 'timedInterpolation-request"
  (cl:format cl:nil "~%string      names~%string      angleLists~%string      times~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <timedInterpolation-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'names))
     4 (cl:length (cl:slot-value msg 'angleLists))
     4 (cl:length (cl:slot-value msg 'times))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <timedInterpolation-request>))
  "Converts a ROS message object to a list"
  (cl:list 'timedInterpolation-request
    (cl:cons ':names (names msg))
    (cl:cons ':angleLists (angleLists msg))
    (cl:cons ':times (times msg))
))
;//! \htmlinclude timedInterpolation-response.msg.html

(cl:defclass <timedInterpolation-response> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass timedInterpolation-response (<timedInterpolation-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <timedInterpolation-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'timedInterpolation-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control_tutorial_1-srv:<timedInterpolation-response> is deprecated: use nao_control_tutorial_1-srv:timedInterpolation-response instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <timedInterpolation-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:angle-val is deprecated.  Use nao_control_tutorial_1-srv:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <timedInterpolation-response>) ostream)
  "Serializes a message object of type '<timedInterpolation-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <timedInterpolation-response>) istream)
  "Deserializes a message object of type '<timedInterpolation-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<timedInterpolation-response>)))
  "Returns string type for a service object of type '<timedInterpolation-response>"
  "nao_control_tutorial_1/timedInterpolationResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'timedInterpolation-response)))
  "Returns string type for a service object of type 'timedInterpolation-response"
  "nao_control_tutorial_1/timedInterpolationResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<timedInterpolation-response>)))
  "Returns md5sum for a message object of type '<timedInterpolation-response>"
  "062c7554adac44a703a2883e86bbb559")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'timedInterpolation-response)))
  "Returns md5sum for a message object of type 'timedInterpolation-response"
  "062c7554adac44a703a2883e86bbb559")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<timedInterpolation-response>)))
  "Returns full string definition for message of type '<timedInterpolation-response>"
  (cl:format cl:nil "~%float32    angle~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'timedInterpolation-response)))
  "Returns full string definition for message of type 'timedInterpolation-response"
  (cl:format cl:nil "~%float32    angle~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <timedInterpolation-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <timedInterpolation-response>))
  "Converts a ROS message object to a list"
  (cl:list 'timedInterpolation-response
    (cl:cons ':angle (angle msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'timedInterpolation)))
  'timedInterpolation-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'timedInterpolation)))
  'timedInterpolation-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'timedInterpolation)))
  "Returns string type for a service object of type '<timedInterpolation>"
  "nao_control_tutorial_1/timedInterpolation")