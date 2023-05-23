// Auto-generated. Do not edit!

// (in-package api_move.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class movement {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.speed_command = null;
      this.angle_of_correction = null;
      this.forward_reverse = null;
    }
    else {
      if (initObj.hasOwnProperty('speed_command')) {
        this.speed_command = initObj.speed_command
      }
      else {
        this.speed_command = 0;
      }
      if (initObj.hasOwnProperty('angle_of_correction')) {
        this.angle_of_correction = initObj.angle_of_correction
      }
      else {
        this.angle_of_correction = 0;
      }
      if (initObj.hasOwnProperty('forward_reverse')) {
        this.forward_reverse = initObj.forward_reverse
      }
      else {
        this.forward_reverse = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type movement
    // Serialize message field [speed_command]
    bufferOffset = _serializer.uint16(obj.speed_command, buffer, bufferOffset);
    // Serialize message field [angle_of_correction]
    bufferOffset = _serializer.int16(obj.angle_of_correction, buffer, bufferOffset);
    // Serialize message field [forward_reverse]
    bufferOffset = _serializer.string(obj.forward_reverse, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type movement
    let len;
    let data = new movement(null);
    // Deserialize message field [speed_command]
    data.speed_command = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [angle_of_correction]
    data.angle_of_correction = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [forward_reverse]
    data.forward_reverse = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.forward_reverse.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'api_move/movement';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0c6fee59201861cdecc9b5d349f15d08';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint16 speed_command
    int16 angle_of_correction
    string forward_reverse
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new movement(null);
    if (msg.speed_command !== undefined) {
      resolved.speed_command = msg.speed_command;
    }
    else {
      resolved.speed_command = 0
    }

    if (msg.angle_of_correction !== undefined) {
      resolved.angle_of_correction = msg.angle_of_correction;
    }
    else {
      resolved.angle_of_correction = 0
    }

    if (msg.forward_reverse !== undefined) {
      resolved.forward_reverse = msg.forward_reverse;
    }
    else {
      resolved.forward_reverse = ''
    }

    return resolved;
    }
};

module.exports = movement;
