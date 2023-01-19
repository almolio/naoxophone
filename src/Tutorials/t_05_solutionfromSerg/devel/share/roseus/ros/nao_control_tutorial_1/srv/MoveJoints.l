;; Auto-generated. Do not edit!


(when (boundp 'nao_control_tutorial_1::MoveJoints)
  (if (not (find-package "NAO_CONTROL_TUTORIAL_1"))
    (make-package "NAO_CONTROL_TUTORIAL_1"))
  (shadow 'MoveJoints (find-package "NAO_CONTROL_TUTORIAL_1")))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::MOVEJOINTS")
  (make-package "NAO_CONTROL_TUTORIAL_1::MOVEJOINTS"))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::MOVEJOINTSREQUEST")
  (make-package "NAO_CONTROL_TUTORIAL_1::MOVEJOINTSREQUEST"))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::MOVEJOINTSRESPONSE")
  (make-package "NAO_CONTROL_TUTORIAL_1::MOVEJOINTSRESPONSE"))

(in-package "ROS")





(defclass nao_control_tutorial_1::MoveJointsRequest
  :super ros::object
  :slots (_joint_name _angle _speed _relative ))

(defmethod nao_control_tutorial_1::MoveJointsRequest
  (:init
   (&key
    ((:joint_name __joint_name) "")
    ((:angle __angle) 0.0)
    ((:speed __speed) 0.0)
    ((:relative __relative) nil)
    )
   (send-super :init)
   (setq _joint_name (string __joint_name))
   (setq _angle (float __angle))
   (setq _speed (float __speed))
   (setq _relative __relative)
   self)
  (:joint_name
   (&optional __joint_name)
   (if __joint_name (setq _joint_name __joint_name)) _joint_name)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:relative
   (&optional __relative)
   (if __relative (setq _relative __relative)) _relative)
  (:serialization-length
   ()
   (+
    ;; string _joint_name
    4 (length _joint_name)
    ;; float32 _angle
    4
    ;; float32 _speed
    4
    ;; bool _relative
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _joint_name
       (write-long (length _joint_name) s) (princ _joint_name s)
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _relative
       (if _relative (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _joint_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _joint_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _relative
     (setq _relative (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass nao_control_tutorial_1::MoveJointsResponse
  :super ros::object
  :slots (_status ))

(defmethod nao_control_tutorial_1::MoveJointsResponse
  (:init
   (&key
    ((:status __status) nil)
    )
   (send-super :init)
   (setq _status __status)
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:serialization-length
   ()
   (+
    ;; bool _status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _status
       (if _status (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _status
     (setq _status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass nao_control_tutorial_1::MoveJoints
  :super ros::object
  :slots ())

(setf (get nao_control_tutorial_1::MoveJoints :md5sum-) "4e50cd843f7a75f4fe9793a5badaf911")
(setf (get nao_control_tutorial_1::MoveJoints :datatype-) "nao_control_tutorial_1/MoveJoints")
(setf (get nao_control_tutorial_1::MoveJoints :request) nao_control_tutorial_1::MoveJointsRequest)
(setf (get nao_control_tutorial_1::MoveJoints :response) nao_control_tutorial_1::MoveJointsResponse)

(defmethod nao_control_tutorial_1::MoveJointsRequest
  (:response () (instance nao_control_tutorial_1::MoveJointsResponse :init)))

(setf (get nao_control_tutorial_1::MoveJointsRequest :md5sum-) "4e50cd843f7a75f4fe9793a5badaf911")
(setf (get nao_control_tutorial_1::MoveJointsRequest :datatype-) "nao_control_tutorial_1/MoveJointsRequest")
(setf (get nao_control_tutorial_1::MoveJointsRequest :definition-)
      "

string joint_name
float32 angle
float32 speed
bool relative

---


bool status
")

(setf (get nao_control_tutorial_1::MoveJointsResponse :md5sum-) "4e50cd843f7a75f4fe9793a5badaf911")
(setf (get nao_control_tutorial_1::MoveJointsResponse :datatype-) "nao_control_tutorial_1/MoveJointsResponse")
(setf (get nao_control_tutorial_1::MoveJointsResponse :definition-)
      "

string joint_name
float32 angle
float32 speed
bool relative

---


bool status
")



(provide :nao_control_tutorial_1/MoveJoints "4e50cd843f7a75f4fe9793a5badaf911")


