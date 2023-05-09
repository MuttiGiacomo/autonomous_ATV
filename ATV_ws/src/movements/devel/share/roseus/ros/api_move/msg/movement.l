;; Auto-generated. Do not edit!


(when (boundp 'api_move::movement)
  (if (not (find-package "API_MOVE"))
    (make-package "API_MOVE"))
  (shadow 'movement (find-package "API_MOVE")))
(unless (find-package "API_MOVE::MOVEMENT")
  (make-package "API_MOVE::MOVEMENT"))

(in-package "ROS")
;;//! \htmlinclude movement.msg.html


(defclass api_move::movement
  :super ros::object
  :slots (_speed_command _angle_of_correction _forward_reverse ))

(defmethod api_move::movement
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

(setf (get api_move::movement :md5sum-) "0c6fee59201861cdecc9b5d349f15d08")
(setf (get api_move::movement :datatype-) "api_move/movement")
(setf (get api_move::movement :definition-)
      "uint16 speed_command
int16 angle_of_correction
string forward_reverse

")



(provide :api_move/movement "0c6fee59201861cdecc9b5d349f15d08")


