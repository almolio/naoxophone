
(cl:in-package :asdf)

(defsystem "nao_control_tutorial_1-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "jointAngle" :depends-on ("_package_jointAngle"))
    (:file "_package_jointAngle" :depends-on ("_package"))
    (:file "timedInterpolation" :depends-on ("_package_timedInterpolation"))
    (:file "_package_timedInterpolation" :depends-on ("_package"))
  ))