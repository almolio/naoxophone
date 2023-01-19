; Auto-generated. Do not edit!


(cl:in-package nao_control_tutorial_1-srv)


;//! \htmlinclude MoveJoints-request.msg.html

(cl:defclass <MoveJoints-request> (roslisp-msg-protocol:ros-message)
  ((joint_name
    :reader joint_name
    :initarg :joint_name
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
    :initform 0.0)
   (relative
    :reader relative
    :initarg :relative
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MoveJoints-request (<MoveJoints-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveJoints-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveJoints-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control_tutorial_1-srv:<MoveJoints-request> is deprecated: use nao_control_tutorial_1-srv:MoveJoints-request instead.")))

(cl:ensure-generic-function 'joint_name-val :lambda-list '(m))
(cl:defmethod joint_name-val ((m <MoveJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:joint_name-val is deprecated.  Use nao_control_tutorial_1-srv:joint_name instead.")
  (joint_name m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <MoveJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:angle-val is deprecated.  Use nao_control_tutorial_1-srv:angle instead.")
  (angle m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <MoveJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:speed-val is deprecated.  Use nao_control_tutorial_1-srv:speed instead.")
  (speed m))

(cl:ensure-generic-function 'relative-val :lambda-list '(m))
(cl:defmethod relative-val ((m <MoveJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:relative-val is deprecated.  Use nao_control_tutorial_1-srv:relative instead.")
  (relative m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveJoints-request>) ostream)
  "Serializes a message object of type '<MoveJoints-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'joint_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'joint_name))
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
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'relative) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveJoints-request>) istream)
  "Deserializes a message object of type '<MoveJoints-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'joint_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'joint_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
    (cl:setf (cl:slot-value msg 'relative) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveJoints-request>)))
  "Returns string type for a service object of type '<MoveJoints-request>"
  "nao_control_tutorial_1/MoveJointsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveJoints-request)))
  "Returns string type for a service object of type 'MoveJoints-request"
  "nao_control_tutorial_1/MoveJointsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveJoints-request>)))
  "Returns md5sum for a message object of type '<MoveJoints-request>"
  "4e50cd843f7a75f4fe9793a5badaf911")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveJoints-request)))
  "Returns md5sum for a message object of type 'MoveJoints-request"
  "4e50cd843f7a75f4fe9793a5badaf911")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveJoints-request>)))
  "Returns full string definition for message of type '<MoveJoints-request>"
  (cl:format cl:nil "~%~%string joint_name~%float32 angle~%float32 speed~%bool relative~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveJoints-request)))
  "Returns full string definition for message of type 'MoveJoints-request"
  (cl:format cl:nil "~%~%string joint_name~%float32 angle~%float32 speed~%bool relative~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveJoints-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'joint_name))
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveJoints-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveJoints-request
    (cl:cons ':joint_name (joint_name msg))
    (cl:cons ':angle (angle msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':relative (relative msg))
))
;//! \htmlinclude MoveJoints-response.msg.html

(cl:defclass <MoveJoints-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MoveJoints-response (<MoveJoints-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveJoints-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveJoints-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control_tutorial_1-srv:<MoveJoints-response> is deprecated: use nao_control_tutorial_1-srv:MoveJoints-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <MoveJoints-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:status-val is deprecated.  Use nao_control_tutorial_1-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveJoints-response>) ostream)
  "Serializes a message object of type '<MoveJoints-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'status) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveJoints-response>) istream)
  "Deserializes a message object of type '<MoveJoints-response>"
    (cl:setf (cl:slot-value msg 'status) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveJoints-response>)))
  "Returns string type for a service object of type '<MoveJoints-response>"
  "nao_control_tutorial_1/MoveJointsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveJoints-response)))
  "Returns string type for a service object of type 'MoveJoints-response"
  "nao_control_tutorial_1/MoveJointsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveJoints-response>)))
  "Returns md5sum for a message object of type '<MoveJoints-response>"
  "4e50cd843f7a75f4fe9793a5badaf911")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveJoints-response)))
  "Returns md5sum for a message object of type 'MoveJoints-response"
  "4e50cd843f7a75f4fe9793a5badaf911")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveJoints-response>)))
  "Returns full string definition for message of type '<MoveJoints-response>"
  (cl:format cl:nil "~%~%bool status~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveJoints-response)))
  "Returns full string definition for message of type 'MoveJoints-response"
  (cl:format cl:nil "~%~%bool status~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveJoints-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveJoints-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveJoints-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MoveJoints)))
  'MoveJoints-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MoveJoints)))
  'MoveJoints-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveJoints)))
  "Returns string type for a service object of type '<MoveJoints>"
  "nao_control_tutorial_1/MoveJoints")