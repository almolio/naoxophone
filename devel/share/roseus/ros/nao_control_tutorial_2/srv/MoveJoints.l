;; Auto-generated. Do not edit!


(when (boundp 'nao_control_tutorial_2::MoveJoints)
  (if (not (find-package "NAO_CONTROL_TUTORIAL_2"))
    (make-package "NAO_CONTROL_TUTORIAL_2"))
  (shadow 'MoveJoints (find-package "NAO_CONTROL_TUTORIAL_2")))
(unless (find-package "NAO_CONTROL_TUTORIAL_2::MOVEJOINTS")
  (make-package "NAO_CONTROL_TUTORIAL_2::MOVEJOINTS"))
(unless (find-package "NAO_CONTROL_TUTORIAL_2::MOVEJOINTSREQUEST")
  (make-package "NAO_CONTROL_TUTORIAL_2::MOVEJOINTSREQUEST"))
(unless (find-package "NAO_CONTROL_TUTORIAL_2::MOVEJOINTSRESPONSE")
  (make-package "NAO_CONTROL_TUTORIAL_2::MOVEJOINTSRESPONSE"))

(in-package "ROS")





(defclass nao_control_tutorial_2::MoveJointsRequest
  :super ros::object
  :slots (_joint_name _x_pos _y_pos _z_pos _x_rot _y_rot _z_rot _max_vel _exe_time ))

(defmethod nao_control_tutorial_2::MoveJointsRequest
  (:init
   (&key
    ((:joint_name __joint_name) "")
    ((:x_pos __x_pos) "")
    ((:y_pos __y_pos) "")
    ((:z_pos __z_pos) "")
    ((:x_rot __x_rot) "")
    ((:y_rot __y_rot) "")
    ((:z_rot __z_rot) "")
    ((:max_vel __max_vel) "")
    ((:exe_time __exe_time) "")
    )
   (send-super :init)
   (setq _joint_name (string __joint_name))
   (setq _x_pos (string __x_pos))
   (setq _y_pos (string __y_pos))
   (setq _z_pos (string __z_pos))
   (setq _x_rot (string __x_rot))
   (setq _y_rot (string __y_rot))
   (setq _z_rot (string __z_rot))
   (setq _max_vel (string __max_vel))
   (setq _exe_time (string __exe_time))
   self)
  (:joint_name
   (&optional __joint_name)
   (if __joint_name (setq _joint_name __joint_name)) _joint_name)
  (:x_pos
   (&optional __x_pos)
   (if __x_pos (setq _x_pos __x_pos)) _x_pos)
  (:y_pos
   (&optional __y_pos)
   (if __y_pos (setq _y_pos __y_pos)) _y_pos)
  (:z_pos
   (&optional __z_pos)
   (if __z_pos (setq _z_pos __z_pos)) _z_pos)
  (:x_rot
   (&optional __x_rot)
   (if __x_rot (setq _x_rot __x_rot)) _x_rot)
  (:y_rot
   (&optional __y_rot)
   (if __y_rot (setq _y_rot __y_rot)) _y_rot)
  (:z_rot
   (&optional __z_rot)
   (if __z_rot (setq _z_rot __z_rot)) _z_rot)
  (:max_vel
   (&optional __max_vel)
   (if __max_vel (setq _max_vel __max_vel)) _max_vel)
  (:exe_time
   (&optional __exe_time)
   (if __exe_time (setq _exe_time __exe_time)) _exe_time)
  (:serialization-length
   ()
   (+
    ;; string _joint_name
    4 (length _joint_name)
    ;; string _x_pos
    4 (length _x_pos)
    ;; string _y_pos
    4 (length _y_pos)
    ;; string _z_pos
    4 (length _z_pos)
    ;; string _x_rot
    4 (length _x_rot)
    ;; string _y_rot
    4 (length _y_rot)
    ;; string _z_rot
    4 (length _z_rot)
    ;; string _max_vel
    4 (length _max_vel)
    ;; string _exe_time
    4 (length _exe_time)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _joint_name
       (write-long (length _joint_name) s) (princ _joint_name s)
     ;; string _x_pos
       (write-long (length _x_pos) s) (princ _x_pos s)
     ;; string _y_pos
       (write-long (length _y_pos) s) (princ _y_pos s)
     ;; string _z_pos
       (write-long (length _z_pos) s) (princ _z_pos s)
     ;; string _x_rot
       (write-long (length _x_rot) s) (princ _x_rot s)
     ;; string _y_rot
       (write-long (length _y_rot) s) (princ _y_rot s)
     ;; string _z_rot
       (write-long (length _z_rot) s) (princ _z_rot s)
     ;; string _max_vel
       (write-long (length _max_vel) s) (princ _max_vel s)
     ;; string _exe_time
       (write-long (length _exe_time) s) (princ _exe_time s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _joint_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _joint_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _x_pos
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _x_pos (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _y_pos
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _y_pos (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _z_pos
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _z_pos (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _x_rot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _x_rot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _y_rot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _y_rot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _z_rot
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _z_rot (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _max_vel
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _max_vel (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _exe_time
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _exe_time (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass nao_control_tutorial_2::MoveJointsResponse
  :super ros::object
  :slots (_x_pos _y_pos _z_pos _x_rot _y_rot _z_rot ))

(defmethod nao_control_tutorial_2::MoveJointsResponse
  (:init
   (&key
    ((:x_pos __x_pos) 0.0)
    ((:y_pos __y_pos) 0.0)
    ((:z_pos __z_pos) 0.0)
    ((:x_rot __x_rot) 0.0)
    ((:y_rot __y_rot) 0.0)
    ((:z_rot __z_rot) 0.0)
    )
   (send-super :init)
   (setq _x_pos (float __x_pos))
   (setq _y_pos (float __y_pos))
   (setq _z_pos (float __z_pos))
   (setq _x_rot (float __x_rot))
   (setq _y_rot (float __y_rot))
   (setq _z_rot (float __z_rot))
   self)
  (:x_pos
   (&optional __x_pos)
   (if __x_pos (setq _x_pos __x_pos)) _x_pos)
  (:y_pos
   (&optional __y_pos)
   (if __y_pos (setq _y_pos __y_pos)) _y_pos)
  (:z_pos
   (&optional __z_pos)
   (if __z_pos (setq _z_pos __z_pos)) _z_pos)
  (:x_rot
   (&optional __x_rot)
   (if __x_rot (setq _x_rot __x_rot)) _x_rot)
  (:y_rot
   (&optional __y_rot)
   (if __y_rot (setq _y_rot __y_rot)) _y_rot)
  (:z_rot
   (&optional __z_rot)
   (if __z_rot (setq _z_rot __z_rot)) _z_rot)
  (:serialization-length
   ()
   (+
    ;; float32 _x_pos
    4
    ;; float32 _y_pos
    4
    ;; float32 _z_pos
    4
    ;; float32 _x_rot
    4
    ;; float32 _y_rot
    4
    ;; float32 _z_rot
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x_pos
       (sys::poke _x_pos (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_pos
       (sys::poke _y_pos (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z_pos
       (sys::poke _z_pos (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _x_rot
       (sys::poke _x_rot (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_rot
       (sys::poke _y_rot (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z_rot
       (sys::poke _z_rot (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x_pos
     (setq _x_pos (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_pos
     (setq _y_pos (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z_pos
     (setq _z_pos (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _x_rot
     (setq _x_rot (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_rot
     (setq _y_rot (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z_rot
     (setq _z_rot (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass nao_control_tutorial_2::MoveJoints
  :super ros::object
  :slots ())

(setf (get nao_control_tutorial_2::MoveJoints :md5sum-) "998e30efad9a2f14084aad7450a533af")
(setf (get nao_control_tutorial_2::MoveJoints :datatype-) "nao_control_tutorial_2/MoveJoints")
(setf (get nao_control_tutorial_2::MoveJoints :request) nao_control_tutorial_2::MoveJointsRequest)
(setf (get nao_control_tutorial_2::MoveJoints :response) nao_control_tutorial_2::MoveJointsResponse)

(defmethod nao_control_tutorial_2::MoveJointsRequest
  (:response () (instance nao_control_tutorial_2::MoveJointsResponse :init)))

(setf (get nao_control_tutorial_2::MoveJointsRequest :md5sum-) "998e30efad9a2f14084aad7450a533af")
(setf (get nao_control_tutorial_2::MoveJointsRequest :datatype-) "nao_control_tutorial_2/MoveJointsRequest")
(setf (get nao_control_tutorial_2::MoveJointsRequest :definition-)
      "
string joint_name
string x_pos
string y_pos
string z_pos
string x_rot
string y_rot
string z_rot
string max_vel
string exe_time
---

float32 x_pos
float32 y_pos
float32 z_pos
float32 x_rot
float32 y_rot
float32 z_rot

")

(setf (get nao_control_tutorial_2::MoveJointsResponse :md5sum-) "998e30efad9a2f14084aad7450a533af")
(setf (get nao_control_tutorial_2::MoveJointsResponse :datatype-) "nao_control_tutorial_2/MoveJointsResponse")
(setf (get nao_control_tutorial_2::MoveJointsResponse :definition-)
      "
string joint_name
string x_pos
string y_pos
string z_pos
string x_rot
string y_rot
string z_rot
string max_vel
string exe_time
---

float32 x_pos
float32 y_pos
float32 z_pos
float32 x_rot
float32 y_rot
float32 z_rot

")



(provide :nao_control_tutorial_2/MoveJoints "998e30efad9a2f14084aad7450a533af")


