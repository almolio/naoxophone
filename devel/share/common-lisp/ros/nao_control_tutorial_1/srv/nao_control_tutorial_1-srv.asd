
(cl:in-package :asdf)

(defsystem "nao_control_tutorial_1-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "InterpolateJoints" :depends-on ("_package_InterpolateJoints"))
    (:file "_package_InterpolateJoints" :depends-on ("_package"))
    (:file "MoveJoints" :depends-on ("_package_MoveJoints"))
    (:file "_package_MoveJoints" :depends-on ("_package"))
  ))