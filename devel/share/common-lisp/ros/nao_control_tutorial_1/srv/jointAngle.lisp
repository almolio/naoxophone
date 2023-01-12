; Auto-generated. Do not edit!


(cl:in-package nao_control_tutorial_1-srv)


;//! \htmlinclude jointAngle-request.msg.html

(cl:defclass <jointAngle-request> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0))
)

(cl:defclass jointAngle-request (<jointAngle-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <jointAngle-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'jointAngle-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control_tutorial_1-srv:<jointAngle-request> is deprecated: use nao_control_tutorial_1-srv:jointAngle-request instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <jointAngle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:name-val is deprecated.  Use nao_control_tutorial_1-srv:name instead.")
  (name m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <jointAngle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:angle-val is deprecated.  Use nao_control_tutorial_1-srv:angle instead.")
  (angle m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <jointAngle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:speed-val is deprecated.  Use nao_control_tutorial_1-srv:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <jointAngle-request>) ostream)
  "Serializes a message object of type '<jointAngle-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <jointAngle-request>) istream)
  "Deserializes a message object of type '<jointAngle-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<jointAngle-request>)))
  "Returns string type for a service object of type '<jointAngle-request>"
  "nao_control_tutorial_1/jointAngleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'jointAngle-request)))
  "Returns string type for a service object of type 'jointAngle-request"
  "nao_control_tutorial_1/jointAngleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<jointAngle-request>)))
  "Returns md5sum for a message object of type '<jointAngle-request>"
  "9f94ee84ff234477d8bfe4add39a302f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'jointAngle-request)))
  "Returns md5sum for a message object of type 'jointAngle-request"
  "9f94ee84ff234477d8bfe4add39a302f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<jointAngle-request>)))
  "Returns full string definition for message of type '<jointAngle-request>"
  (cl:format cl:nil "~%string      name~%float32    angle~%float32    speed~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'jointAngle-request)))
  "Returns full string definition for message of type 'jointAngle-request"
  (cl:format cl:nil "~%string      name~%float32    angle~%float32    speed~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <jointAngle-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <jointAngle-request>))
  "Converts a ROS message object to a list"
  (cl:list 'jointAngle-request
    (cl:cons ':name (name msg))
    (cl:cons ':angle (angle msg))
    (cl:cons ':speed (speed msg))
))
;//! \htmlinclude jointAngle-response.msg.html

(cl:defclass <jointAngle-response> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass jointAngle-response (<jointAngle-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <jointAngle-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'jointAngle-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control_tutorial_1-srv:<jointAngle-response> is deprecated: use nao_control_tutorial_1-srv:jointAngle-response instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <jointAngle-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:angle-val is deprecated.  Use nao_control_tutorial_1-srv:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <jointAngle-response>) ostream)
  "Serializes a message object of type '<jointAngle-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <jointAngle-response>) istream)
  "Deserializes a message object of type '<jointAngle-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<jointAngle-response>)))
  "Returns string type for a service object of type '<jointAngle-response>"
  "nao_control_tutorial_1/jointAngleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'jointAngle-response)))
  "Returns string type for a service object of type 'jointAngle-response"
  "nao_control_tutorial_1/jointAngleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<jointAngle-response>)))
  "Returns md5sum for a message object of type '<jointAngle-response>"
  "9f94ee84ff234477d8bfe4add39a302f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'jointAngle-response)))
  "Returns md5sum for a message object of type 'jointAngle-response"
  "9f94ee84ff234477d8bfe4add39a302f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<jointAngle-response>)))
  "Returns full string definition for message of type '<jointAngle-response>"
  (cl:format cl:nil "float32 angle~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'jointAngle-response)))
  "Returns full string definition for message of type 'jointAngle-response"
  (cl:format cl:nil "float32 angle~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <jointAngle-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <jointAngle-response>))
  "Converts a ROS message object to a list"
  (cl:list 'jointAngle-response
    (cl:cons ':angle (angle msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'jointAngle)))
  'jointAngle-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'jointAngle)))
  'jointAngle-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'jointAngle)))
  "Returns string type for a service object of type '<jointAngle>"
  "nao_control_tutorial_1/jointAngle")