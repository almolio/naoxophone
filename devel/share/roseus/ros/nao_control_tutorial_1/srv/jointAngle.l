;; Auto-generated. Do not edit!


(when (boundp 'nao_control_tutorial_1::jointAngle)
  (if (not (find-package "NAO_CONTROL_TUTORIAL_1"))
    (make-package "NAO_CONTROL_TUTORIAL_1"))
  (shadow 'jointAngle (find-package "NAO_CONTROL_TUTORIAL_1")))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::JOINTANGLE")
  (make-package "NAO_CONTROL_TUTORIAL_1::JOINTANGLE"))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::JOINTANGLEREQUEST")
  (make-package "NAO_CONTROL_TUTORIAL_1::JOINTANGLEREQUEST"))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::JOINTANGLERESPONSE")
  (make-package "NAO_CONTROL_TUTORIAL_1::JOINTANGLERESPONSE"))

(in-package "ROS")





(defclass nao_control_tutorial_1::jointAngleRequest
  :super ros::object
  :slots (_name _angle _speed ))

(defmethod nao_control_tutorial_1::jointAngleRequest
  (:init
   (&key
    ((:name __name) "")
    ((:angle __angle) 0.0)
    ((:speed __speed) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _angle (float __angle))
   (setq _speed (float __speed))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; float32 _angle
    4
    ;; float32 _speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass nao_control_tutorial_1::jointAngleResponse
  :super ros::object
  :slots (_angle ))

(defmethod nao_control_tutorial_1::jointAngleResponse
  (:init
   (&key
    ((:angle __angle) 0.0)
    )
   (send-super :init)
   (setq _angle (float __angle))
   self)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:serialization-length
   ()
   (+
    ;; float32 _angle
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass nao_control_tutorial_1::jointAngle
  :super ros::object
  :slots ())

(setf (get nao_control_tutorial_1::jointAngle :md5sum-) "9f94ee84ff234477d8bfe4add39a302f")
(setf (get nao_control_tutorial_1::jointAngle :datatype-) "nao_control_tutorial_1/jointAngle")
(setf (get nao_control_tutorial_1::jointAngle :request) nao_control_tutorial_1::jointAngleRequest)
(setf (get nao_control_tutorial_1::jointAngle :response) nao_control_tutorial_1::jointAngleResponse)

(defmethod nao_control_tutorial_1::jointAngleRequest
  (:response () (instance nao_control_tutorial_1::jointAngleResponse :init)))

(setf (get nao_control_tutorial_1::jointAngleRequest :md5sum-) "9f94ee84ff234477d8bfe4add39a302f")
(setf (get nao_control_tutorial_1::jointAngleRequest :datatype-) "nao_control_tutorial_1/jointAngleRequest")
(setf (get nao_control_tutorial_1::jointAngleRequest :definition-)
      "
string      name
float32    angle
float32    speed

---
float32 angle

")

(setf (get nao_control_tutorial_1::jointAngleResponse :md5sum-) "9f94ee84ff234477d8bfe4add39a302f")
(setf (get nao_control_tutorial_1::jointAngleResponse :datatype-) "nao_control_tutorial_1/jointAngleResponse")
(setf (get nao_control_tutorial_1::jointAngleResponse :definition-)
      "
string      name
float32    angle
float32    speed

---
float32 angle

")



(provide :nao_control_tutorial_1/jointAngle "9f94ee84ff234477d8bfe4add39a302f")


