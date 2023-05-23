;; Auto-generated. Do not edit!


(when (boundp 'wireless_remote_controller::movement)
  (if (not (find-package "WIRELESS_REMOTE_CONTROLLER"))
    (make-package "WIRELESS_REMOTE_CONTROLLER"))
  (shadow 'movement (find-package "WIRELESS_REMOTE_CONTROLLER")))
(unless (find-package "WIRELESS_REMOTE_CONTROLLER::MOVEMENT")
  (make-package "WIRELESS_REMOTE_CONTROLLER::MOVEMENT"))

(in-package "ROS")
;;//! \htmlinclude movement.msg.html


(defclass wireless_remote_controller::movement
  :super ros::object
  :slots (_speed_command _angle_of_correction _forward_reverse ))

(defmethod wireless_remote_controller::movement
  (:init
   (&key
    ((:speed_command __speed_command) 0)
    ((:angle_of_correction __angle_of_correction) 0)
    ((:forward_reverse __forward_reverse) "")
    )
   (send-super :init)
   (setq _speed_command (round __speed_command))
   (setq _angle_of_correction (round __angle_of_correction))
   (setq _forward_reverse (string __forward_reverse))
   self)
  (:speed_command
   (&optional __speed_command)
   (if __speed_command (setq _speed_command __speed_command)) _speed_command)
  (:angle_of_correction
   (&optional __angle_of_correction)
   (if __angle_of_correction (setq _angle_of_correction __angle_of_correction)) _angle_of_correction)
  (:forward_reverse
   (&optional __forward_reverse)
   (if __forward_reverse (setq _forward_reverse __forward_reverse)) _forward_reverse)
  (:serialization-length
   ()
   (+
    ;; uint16 _speed_command
    2
    ;; int16 _angle_of_correction
    2
    ;; string _forward_reverse
    4 (length _forward_reverse)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _speed_command
       (write-word _speed_command s)
     ;; int16 _angle_of_correction
       (write-word _angle_of_correction s)
     ;; string _forward_reverse
       (write-long (length _forward_reverse) s) (princ _forward_reverse s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _speed_command
     (setq _speed_command (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _angle_of_correction
     (setq _angle_of_correction (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; string _forward_reverse
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _forward_reverse (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get wireless_remote_controller::movement :md5sum-) "0c6fee59201861cdecc9b5d349f15d08")
(setf (get wireless_remote_controller::movement :datatype-) "wireless_remote_controller/movement")
(setf (get wireless_remote_controller::movement :definition-)
      "uint16 speed_command
int16 angle_of_correction
string forward_reverse

")



(provide :wireless_remote_controller/movement "0c6fee59201861cdecc9b5d349f15d08")

