; Auto-generated. Do not edit!


(cl:in-package tutorial7-msg)


;//! \htmlinclude blinkGoal.msg.html

(cl:defclass <blinkGoal> (roslisp-msg-protocol:ros-message)
  ((colors
    :reader colors
    :initarg :colors
    :type (cl:vector std_msgs-msg:ColorRGBA)
   :initform (cl:make-array 0 :element-type 'std_msgs-msg:ColorRGBA :initial-element (cl:make-instance 'std_msgs-msg:ColorRGBA)))
   (bg_color
    :reader bg_color
    :initarg :bg_color
    :type std_msgs-msg:ColorRGBA
    :initform (cl:make-instance 'std_msgs-msg:ColorRGBA))
   (blink_duration
    :reader blink_duration
    :initarg :blink_duration
    :type cl:real
    :initform 0)
   (blink_rate_mean
    :reader blink_rate_mean
    :initarg :blink_rate_mean
    :type cl:float
    :initform 0.0)
   (blink_rate_sd
    :reader blink_rate_sd
    :initarg :blink_rate_sd
    :type cl:float
    :initform 0.0))
)

(cl:defclass blinkGoal (<blinkGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <blinkGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'blinkGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tutorial7-msg:<blinkGoal> is deprecated: use tutorial7-msg:blinkGoal instead.")))

(cl:ensure-generic-function 'colors-val :lambda-list '(m))
(cl:defmethod colors-val ((m <blinkGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial7-msg:colors-val is deprecated.  Use tutorial7-msg:colors instead.")
  (colors m))

(cl:ensure-generic-function 'bg_color-val :lambda-list '(m))
(cl:defmethod bg_color-val ((m <blinkGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial7-msg:bg_color-val is deprecated.  Use tutorial7-msg:bg_color instead.")
  (bg_color m))

(cl:ensure-generic-function 'blink_duration-val :lambda-list '(m))
(cl:defmethod blink_duration-val ((m <blinkGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial7-msg:blink_duration-val is deprecated.  Use tutorial7-msg:blink_duration instead.")
  (blink_duration m))

(cl:ensure-generic-function 'blink_rate_mean-val :lambda-list '(m))
(cl:defmethod blink_rate_mean-val ((m <blinkGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial7-msg:blink_rate_mean-val is deprecated.  Use tutorial7-msg:blink_rate_mean instead.")
  (blink_rate_mean m))

(cl:ensure-generic-function 'blink_rate_sd-val :lambda-list '(m))
(cl:defmethod blink_rate_sd-val ((m <blinkGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial7-msg:blink_rate_sd-val is deprecated.  Use tutorial7-msg:blink_rate_sd instead.")
  (blink_rate_sd m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <blinkGoal>) ostream)
  "Serializes a message object of type '<blinkGoal>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'colors))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'colors))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'bg_color) ostream)
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'blink_duration)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'blink_duration) (cl:floor (cl:slot-value msg 'blink_duration)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'blink_rate_mean))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'blink_rate_sd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <blinkGoal>) istream)
  "Deserializes a message object of type '<blinkGoal>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'colors) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'colors)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'std_msgs-msg:ColorRGBA))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'bg_color) istream)
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'blink_duration) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'blink_rate_mean) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'blink_rate_sd) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<blinkGoal>)))
  "Returns string type for a message object of type '<blinkGoal>"
  "tutorial7/blinkGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'blinkGoal)))
  "Returns string type for a message object of type 'blinkGoal"
  "tutorial7/blinkGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<blinkGoal>)))
  "Returns md5sum for a message object of type '<blinkGoal>"
  "5e5d3c2ba9976dc121a0bb6ef7c66d79")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'blinkGoal)))
  "Returns md5sum for a message object of type 'blinkGoal"
  "5e5d3c2ba9976dc121a0bb6ef7c66d79")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<blinkGoal>)))
  "Returns full string definition for message of type '<blinkGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal ~%~%std_msgs/ColorRGBA[] colors  ~%std_msgs/ColorRGBA bg_color  ## background  ~%duration blink_duration~%float32 blink_rate_mean~%float32 blink_rate_sd~%~%~%================================================================================~%MSG: std_msgs/ColorRGBA~%float32 r~%float32 g~%float32 b~%float32 a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'blinkGoal)))
  "Returns full string definition for message of type 'blinkGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal ~%~%std_msgs/ColorRGBA[] colors  ~%std_msgs/ColorRGBA bg_color  ## background  ~%duration blink_duration~%float32 blink_rate_mean~%float32 blink_rate_sd~%~%~%================================================================================~%MSG: std_msgs/ColorRGBA~%float32 r~%float32 g~%float32 b~%float32 a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <blinkGoal>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'colors) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'bg_color))
     8
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <blinkGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'blinkGoal
    (cl:cons ':colors (colors msg))
    (cl:cons ':bg_color (bg_color msg))
    (cl:cons ':blink_duration (blink_duration msg))
    (cl:cons ':blink_rate_mean (blink_rate_mean msg))
    (cl:cons ':blink_rate_sd (blink_rate_sd msg))
))
