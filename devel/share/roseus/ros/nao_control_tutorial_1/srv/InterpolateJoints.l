;; Auto-generated. Do not edit!


(when (boundp 'nao_control_tutorial_1::InterpolateJoints)
  (if (not (find-package "NAO_CONTROL_TUTORIAL_1"))
    (make-package "NAO_CONTROL_TUTORIAL_1"))
  (shadow 'InterpolateJoints (find-package "NAO_CONTROL_TUTORIAL_1")))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::INTERPOLATEJOINTS")
  (make-package "NAO_CONTROL_TUTORIAL_1::INTERPOLATEJOINTS"))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::INTERPOLATEJOINTSREQUEST")
  (make-package "NAO_CONTROL_TUTORIAL_1::INTERPOLATEJOINTSREQUEST"))
(unless (find-package "NAO_CONTROL_TUTORIAL_1::INTERPOLATEJOINTSRESPONSE")
  (make-package "NAO_CONTROL_TUTORIAL_1::INTERPOLATEJOINTSRESPONSE"))

(in-package "ROS")





(defclass nao_control_tutorial_1::InterpolateJointsRequest
  :super ros::object
  :slots (_joint_names _steps _angles _times _relative _blocking ))

(defmethod nao_control_tutorial_1::InterpolateJointsRequest
  (:init
   (&key
    ((:joint_names __joint_names) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:steps __steps) (make-array 0 :initial-element 0 :element-type :integer))
    ((:angles __angles) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:times __times) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:relative __relative) nil)
    ((:blocking __blocking) nil)
    )
   (send-super :init)
   (setq _joint_names __joint_names)
   (setq _steps __steps)
   (setq _angles __angles)
   (setq _times __times)
   (setq _relative __relative)
   (setq _blocking __blocking)
   self)
  (:joint_names
   (&optional __joint_names)
   (if __joint_names (setq _joint_names __joint_names)) _joint_names)
  (:steps
   (&optional __steps)
   (if __steps (setq _steps __steps)) _steps)
  (:angles
   (&optional __angles)
   (if __angles (setq _angles __angles)) _angles)
  (:times
   (&optional __times)
   (if __times (setq _times __times)) _times)
  (:relative
   (&optional __relative)
   (if __relative (setq _relative __relative)) _relative)
  (:blocking
   (&optional __blocking)
   (if __blocking (setq _blocking __blocking)) _blocking)
  (:serialization-length
   ()
   (+
    ;; string[] _joint_names
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _joint_names)) 4
    ;; int32[] _steps
    (* 4    (length _steps)) 4
    ;; float32[] _angles
    (* 4    (length _angles)) 4
    ;; float32[] _times
    (* 4    (length _times)) 4
    ;; bool _relative
    1
    ;; bool _blocking
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _joint_names
     (write-long (length _joint_names) s)
     (dolist (elem _joint_names)
       (write-long (length elem) s) (princ elem s)
       )
     ;; int32[] _steps
     (write-long (length _steps) s)
     (dotimes (i (length _steps))
       (write-long (elt _steps i) s)
       )
     ;; float32[] _angles
     (write-long (length _angles) s)
     (dotimes (i (length _angles))
       (sys::poke (elt _angles i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _times
     (write-long (length _times) s)
     (dotimes (i (length _times))
       (sys::poke (elt _times i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; bool _relative
       (if _relative (write-byte -1 s) (write-byte 0 s))
     ;; bool _blocking
       (if _blocking (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _joint_names
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _joint_names (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _joint_names i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; int32[] _steps
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _steps (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _steps i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; float32[] _angles
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _angles (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _angles i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _times
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _times (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _times i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; bool _relative
     (setq _relative (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _blocking
     (setq _blocking (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass nao_control_tutorial_1::InterpolateJointsResponse
  :super ros::object
  :slots (_status ))

(defmethod nao_control_tutorial_1::InterpolateJointsResponse
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

(defclass nao_control_tutorial_1::InterpolateJoints
  :super ros::object
  :slots ())

(setf (get nao_control_tutorial_1::InterpolateJoints :md5sum-) "d23b0af1b474d5848e69b3a31bdacede")
(setf (get nao_control_tutorial_1::InterpolateJoints :datatype-) "nao_control_tutorial_1/InterpolateJoints")
(setf (get nao_control_tutorial_1::InterpolateJoints :request) nao_control_tutorial_1::InterpolateJointsRequest)
(setf (get nao_control_tutorial_1::InterpolateJoints :response) nao_control_tutorial_1::InterpolateJointsResponse)

(defmethod nao_control_tutorial_1::InterpolateJointsRequest
  (:response () (instance nao_control_tutorial_1::InterpolateJointsResponse :init)))

(setf (get nao_control_tutorial_1::InterpolateJointsRequest :md5sum-) "d23b0af1b474d5848e69b3a31bdacede")
(setf (get nao_control_tutorial_1::InterpolateJointsRequest :datatype-) "nao_control_tutorial_1/InterpolateJointsRequest")
(setf (get nao_control_tutorial_1::InterpolateJointsRequest :definition-)
      "

string[] joint_names
int32[] steps
float32[] angles
float32[] times
bool relative
bool blocking

---


bool status
")

(setf (get nao_control_tutorial_1::InterpolateJointsResponse :md5sum-) "d23b0af1b474d5848e69b3a31bdacede")
(setf (get nao_control_tutorial_1::InterpolateJointsResponse :datatype-) "nao_control_tutorial_1/InterpolateJointsResponse")
(setf (get nao_control_tutorial_1::InterpolateJointsResponse :definition-)
      "

string[] joint_names
int32[] steps
float32[] angles
float32[] times
bool relative
bool blocking

---


bool status
")



(provide :nao_control_tutorial_1/InterpolateJoints "d23b0af1b474d5848e69b3a31bdacede")


