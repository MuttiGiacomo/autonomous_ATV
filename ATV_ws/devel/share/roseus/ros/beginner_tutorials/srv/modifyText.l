;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::modifyText)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'modifyText (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::MODIFYTEXT")
  (make-package "BEGINNER_TUTORIALS::MODIFYTEXT"))
(unless (find-package "BEGINNER_TUTORIALS::MODIFYTEXTREQUEST")
  (make-package "BEGINNER_TUTORIALS::MODIFYTEXTREQUEST"))
(unless (find-package "BEGINNER_TUTORIALS::MODIFYTEXTRESPONSE")
  (make-package "BEGINNER_TUTORIALS::MODIFYTEXTRESPONSE"))

(in-package "ROS")





(defclass beginner_tutorials::modifyTextRequest
  :super ros::object
  :slots (_inputString ))

(defmethod beginner_tutorials::modifyTextRequest
  (:init
   (&key
    ((:inputString __inputString) "")
    )
   (send-super :init)
   (setq _inputString (string __inputString))
   self)
  (:inputString
   (&optional __inputString)
   (if __inputString (setq _inputString __inputString)) _inputString)
  (:serialization-length
   ()
   (+
    ;; string _inputString
    4 (length _inputString)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _inputString
       (write-long (length _inputString) s) (princ _inputString s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _inputString
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _inputString (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass beginner_tutorials::modifyTextResponse
  :super ros::object
  :slots (_modifiedString ))

(defmethod beginner_tutorials::modifyTextResponse
  (:init
   (&key
    ((:modifiedString __modifiedString) "")
    )
   (send-super :init)
   (setq _modifiedString (string __modifiedString))
   self)
  (:modifiedString
   (&optional __modifiedString)
   (if __modifiedString (setq _modifiedString __modifiedString)) _modifiedString)
  (:serialization-length
   ()
   (+
    ;; string _modifiedString
    4 (length _modifiedString)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _modifiedString
       (write-long (length _modifiedString) s) (princ _modifiedString s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _modifiedString
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _modifiedString (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass beginner_tutorials::modifyText
  :super ros::object
  :slots ())

(setf (get beginner_tutorials::modifyText :md5sum-) "2ea50b9bce33ae6fad63d90c193917b0")
(setf (get beginner_tutorials::modifyText :datatype-) "beginner_tutorials/modifyText")
(setf (get beginner_tutorials::modifyText :request) beginner_tutorials::modifyTextRequest)
(setf (get beginner_tutorials::modifyText :response) beginner_tutorials::modifyTextResponse)

(defmethod beginner_tutorials::modifyTextRequest
  (:response () (instance beginner_tutorials::modifyTextResponse :init)))

(setf (get beginner_tutorials::modifyTextRequest :md5sum-) "2ea50b9bce33ae6fad63d90c193917b0")
(setf (get beginner_tutorials::modifyTextRequest :datatype-) "beginner_tutorials/modifyTextRequest")
(setf (get beginner_tutorials::modifyTextRequest :definition-)
      "#request
string inputString
---
#response
string modifiedString

")

(setf (get beginner_tutorials::modifyTextResponse :md5sum-) "2ea50b9bce33ae6fad63d90c193917b0")
(setf (get beginner_tutorials::modifyTextResponse :datatype-) "beginner_tutorials/modifyTextResponse")
(setf (get beginner_tutorials::modifyTextResponse :definition-)
      "#request
string inputString
---
#response
string modifiedString

")



(provide :beginner_tutorials/modifyText "2ea50b9bce33ae6fad63d90c193917b0")


