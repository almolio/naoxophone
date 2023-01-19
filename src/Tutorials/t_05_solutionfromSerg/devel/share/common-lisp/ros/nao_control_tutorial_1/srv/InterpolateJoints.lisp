; Auto-generated. Do not edit!


(cl:in-package nao_control_tutorial_1-srv)


;//! \htmlinclude InterpolateJoints-request.msg.html

(cl:defclass <InterpolateJoints-request> (roslisp-msg-protocol:ros-message)
  ((joint_names
    :reader joint_names
    :initarg :joint_names
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (steps
    :reader steps
    :initarg :steps
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (angles
    :reader angles
    :initarg :angles
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (times
    :reader times
    :initarg :times
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (relative
    :reader relative
    :initarg :relative
    :type cl:boolean
    :initform cl:nil)
   (blocking
    :reader blocking
    :initarg :blocking
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass InterpolateJoints-request (<InterpolateJoints-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <InterpolateJoints-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'InterpolateJoints-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control_tutorial_1-srv:<InterpolateJoints-request> is deprecated: use nao_control_tutorial_1-srv:InterpolateJoints-request instead.")))

(cl:ensure-generic-function 'joint_names-val :lambda-list '(m))
(cl:defmethod joint_names-val ((m <InterpolateJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:joint_names-val is deprecated.  Use nao_control_tutorial_1-srv:joint_names instead.")
  (joint_names m))

(cl:ensure-generic-function 'steps-val :lambda-list '(m))
(cl:defmethod steps-val ((m <InterpolateJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:steps-val is deprecated.  Use nao_control_tutorial_1-srv:steps instead.")
  (steps m))

(cl:ensure-generic-function 'angles-val :lambda-list '(m))
(cl:defmethod angles-val ((m <InterpolateJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:angles-val is deprecated.  Use nao_control_tutorial_1-srv:angles instead.")
  (angles m))

(cl:ensure-generic-function 'times-val :lambda-list '(m))
(cl:defmethod times-val ((m <InterpolateJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:times-val is deprecated.  Use nao_control_tutorial_1-srv:times instead.")
  (times m))

(cl:ensure-generic-function 'relative-val :lambda-list '(m))
(cl:defmethod relative-val ((m <InterpolateJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:relative-val is deprecated.  Use nao_control_tutorial_1-srv:relative instead.")
  (relative m))

(cl:ensure-generic-function 'blocking-val :lambda-list '(m))
(cl:defmethod blocking-val ((m <InterpolateJoints-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:blocking-val is deprecated.  Use nao_control_tutorial_1-srv:blocking instead.")
  (blocking m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <InterpolateJoints-request>) ostream)
  "Serializes a message object of type '<InterpolateJoints-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'joint_names))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'joint_names))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'steps))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'steps))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'angles))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'angles))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'times))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'times))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'relative) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'blocking) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <InterpolateJoints-request>) istream)
  "Deserializes a message object of type '<InterpolateJoints-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'joint_names) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'joint_names)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'steps) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'steps)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'angles) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'angles)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'times) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'times)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
    (cl:setf (cl:slot-value msg 'relative) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'blocking) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<InterpolateJoints-request>)))
  "Returns string type for a service object of type '<InterpolateJoints-request>"
  "nao_control_tutorial_1/InterpolateJointsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'InterpolateJoints-request)))
  "Returns string type for a service object of type 'InterpolateJoints-request"
  "nao_control_tutorial_1/InterpolateJointsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<InterpolateJoints-request>)))
  "Returns md5sum for a message object of type '<InterpolateJoints-request>"
  "d23b0af1b474d5848e69b3a31bdacede")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'InterpolateJoints-request)))
  "Returns md5sum for a message object of type 'InterpolateJoints-request"
  "d23b0af1b474d5848e69b3a31bdacede")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<InterpolateJoints-request>)))
  "Returns full string definition for message of type '<InterpolateJoints-request>"
  (cl:format cl:nil "~%~%string[] joint_names~%int32[] steps~%float32[] angles~%float32[] times~%bool relative~%bool blocking~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'InterpolateJoints-request)))
  "Returns full string definition for message of type 'InterpolateJoints-request"
  (cl:format cl:nil "~%~%string[] joint_names~%int32[] steps~%float32[] angles~%float32[] times~%bool relative~%bool blocking~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <InterpolateJoints-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'joint_names) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'steps) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'angles) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'times) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <InterpolateJoints-request>))
  "Converts a ROS message object to a list"
  (cl:list 'InterpolateJoints-request
    (cl:cons ':joint_names (joint_names msg))
    (cl:cons ':steps (steps msg))
    (cl:cons ':angles (angles msg))
    (cl:cons ':times (times msg))
    (cl:cons ':relative (relative msg))
    (cl:cons ':blocking (blocking msg))
))
;//! \htmlinclude InterpolateJoints-response.msg.html

(cl:defclass <InterpolateJoints-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass InterpolateJoints-response (<InterpolateJoints-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <InterpolateJoints-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'InterpolateJoints-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control_tutorial_1-srv:<InterpolateJoints-response> is deprecated: use nao_control_tutorial_1-srv:InterpolateJoints-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <InterpolateJoints-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control_tutorial_1-srv:status-val is deprecated.  Use nao_control_tutorial_1-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <InterpolateJoints-response>) ostream)
  "Serializes a message object of type '<InterpolateJoints-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'status) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <InterpolateJoints-response>) istream)
  "Deserializes a message object of type '<InterpolateJoints-response>"
    (cl:setf (cl:slot-value msg 'status) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<InterpolateJoints-response>)))
  "Returns string type for a service object of type '<InterpolateJoints-response>"
  "nao_control_tutorial_1/InterpolateJointsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'InterpolateJoints-response)))
  "Returns string type for a service object of type 'InterpolateJoints-response"
  "nao_control_tutorial_1/InterpolateJointsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<InterpolateJoints-response>)))
  "Returns md5sum for a message object of type '<InterpolateJoints-response>"
  "d23b0af1b474d5848e69b3a31bdacede")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'InterpolateJoints-response)))
  "Returns md5sum for a message object of type 'InterpolateJoints-response"
  "d23b0af1b474d5848e69b3a31bdacede")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<InterpolateJoints-response>)))
  "Returns full string definition for message of type '<InterpolateJoints-response>"
  (cl:format cl:nil "~%~%bool status~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'InterpolateJoints-response)))
  "Returns full string definition for message of type 'InterpolateJoints-response"
  (cl:format cl:nil "~%~%bool status~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <InterpolateJoints-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <InterpolateJoints-response>))
  "Converts a ROS message object to a list"
  (cl:list 'InterpolateJoints-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'InterpolateJoints)))
  'InterpolateJoints-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'InterpolateJoints)))
  'InterpolateJoints-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'InterpolateJoints)))
  "Returns string type for a service object of type '<InterpolateJoints>"
  "nao_control_tutorial_1/InterpolateJoints")