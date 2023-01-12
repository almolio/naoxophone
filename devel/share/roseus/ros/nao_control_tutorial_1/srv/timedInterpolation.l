;; Auto-generated. Do not edit!


(when (boundp 'nao_control_tutorial_1::timedInterpolation)
  (if (not (find-package "NAO_CONTROL_TUTORIAL_1"))
    (make-package "NAO_CONTROL_TUTORIAL_1"))
  (shadow 'timedInterpolation (find-package "NAO_CONTROL_TUTORIAL_1")))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::TIMEDINTERPOLATION")
  (make-package "NAO_CONTROL_TUTORIAL_1::TIMEDINTERPOLATION"))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::TIMEDINTERPOLATIONREQUEST")
  (make-package "NAO_CONTROL_TUTORIAL_1::TIMEDINTERPOLATIONREQUEST"))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::TIMEDINTERPOLATIONRESPONSE")
  (make-package "NAO_CONTROL_TUTORIAL_1::TIMEDINTERPOLATIONRESPONSE"))

(in-package "ROS")





(defclass nao_control_tutorial_1::timedInterpolationRequest
  :super ros::object
  :slots (_names _angleLists _times ))

(defmethod nao_control_tutorial_1::timedInterpolationRequest
  (:init
   (&key
    ((:names __names) "")
    ((:angleLists __angleLists) "")
    ((:times __times) "")
    )
   (send-super :init)
   (setq _names (string __names))
   (setq _angleLists (string __angleLists))
   (setq _times (string __times))
   self)
  (:names
   (&optional __names)
   (if __names (setq _names __names)) _names)
  (:angleLists
   (&optional __angleLists)
   (if __angleLists (setq _angleLists __angleLists)) _angleLists)
  (:times
   (&optional __times)
   (if __times (setq _times __times)) _times)
  (:serialization-length
   ()
   (+
    ;; string _names
    4 (length _names)
    ;; string _angleLists
    4 (length _angleLists)
    ;; string _times
    4 (length _times)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _names
       (write-long (length _names) s) (princ _names s)
     ;; string _angleLists
       (write-long (length _angleLists) s) (princ _angleLists s)
     ;; string _times
       (write-long (length _times) s) (princ _times s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _names
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _names (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _angleLists
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _angleLists (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _times
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _times (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass nao_control_tutorial_1::timedInterpolationResponse
  :super ros::object
  :slots (_angle ))

(defmethod nao_control_tutorial_1::timedInterpolationResponse
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

(defclass nao_control_tutorial_1::timedInterpolation
  :super ros::object
  :slots ())

(setf (get nao_control_tutorial_1::timedInterpolation :md5sum-) "062c7554adac44a703a2883e86bbb559")
(setf (get nao_control_tutorial_1::timedInterpolation :datatype-) "nao_control_tutorial_1/timedInterpolation")
(setf (get nao_control_tutorial_1::timedInterpolation :request) nao_control_tutorial_1::timedInterpolationRequest)
(setf (get nao_control_tutorial_1::timedInterpolation :response) nao_control_tutorial_1::timedInterpolationResponse)

(defmethod nao_control_tutorial_1::timedInterpolationRequest
  (:response () (instance nao_control_tutorial_1::timedInterpolationResponse :init)))

(setf (get nao_control_tutorial_1::timedInterpolationRequest :md5sum-) "062c7554adac44a703a2883e86bbb559")
(setf (get nao_control_tutorial_1::timedInterpolationRequest :datatype-) "nao_control_tutorial_1/timedInterpolationRequest")
(setf (get nao_control_tutorial_1::timedInterpolationRequest :definition-)
      "
string      names
string      angleLists
string      times

---

float32    angle

")

(setf (get nao_control_tutorial_1::timedInterpolationResponse :md5sum-) "062c7554adac44a703a2883e86bbb559")
(setf (get nao_control_tutorial_1::timedInterpolationResponse :datatype-) "nao_control_tutorial_1/timedInterpolationResponse")
(setf (get nao_control_tutorial_1::timedInterpolationResponse :definition-)
      "
string      names
string      angleLists
string      times

---

float32    angle

")



(provide :nao_control_tutorial_1/timedInterpolation "062c7554adac44a703a2883e86bbb559")


