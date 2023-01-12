// Auto-generated. Do not edit!

// (in-package nao_control_tutorial_2.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class MoveJointsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.joint_name = null;
      this.x_pos = null;
      this.y_pos = null;
      this.z_pos = null;
      this.x_rot = null;
      this.y_rot = null;
      this.z_rot = null;
      this.max_vel = null;
      this.exe_time = null;
    }
    else {
      if (initObj.hasOwnProperty('joint_name')) {
        this.joint_name = initObj.joint_name
      }
      else {
        this.joint_name = '';
      }
      if (initObj.hasOwnProperty('x_pos')) {
        this.x_pos = initObj.x_pos
      }
      else {
        this.x_pos = '';
      }
      if (initObj.hasOwnProperty('y_pos')) {
        this.y_pos = initObj.y_pos
      }
      else {
        this.y_pos = '';
      }
      if (initObj.hasOwnProperty('z_pos')) {
        this.z_pos = initObj.z_pos
      }
      else {
        this.z_pos = '';
      }
      if (initObj.hasOwnProperty('x_rot')) {
        this.x_rot = initObj.x_rot
      }
      else {
        this.x_rot = '';
      }
      if (initObj.hasOwnProperty('y_rot')) {
        this.y_rot = initObj.y_rot
      }
      else {
        this.y_rot = '';
      }
      if (initObj.hasOwnProperty('z_rot')) {
        this.z_rot = initObj.z_rot
      }
      else {
        this.z_rot = '';
      }
      if (initObj.hasOwnProperty('max_vel')) {
        this.max_vel = initObj.max_vel
      }
      else {
        this.max_vel = '';
      }
      if (initObj.hasOwnProperty('exe_time')) {
        this.exe_time = initObj.exe_time
      }
      else {
        this.exe_time = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MoveJointsRequest
    // Serialize message field [joint_name]
    bufferOffset = _serializer.string(obj.joint_name, buffer, bufferOffset);
    // Serialize message field [x_pos]
    bufferOffset = _serializer.string(obj.x_pos, buffer, bufferOffset);
    // Serialize message field [y_pos]
    bufferOffset = _serializer.string(obj.y_pos, buffer, bufferOffset);
    // Serialize message field [z_pos]
    bufferOffset = _serializer.string(obj.z_pos, buffer, bufferOffset);
    // Serialize message field [x_rot]
    bufferOffset = _serializer.string(obj.x_rot, buffer, bufferOffset);
    // Serialize message field [y_rot]
    bufferOffset = _serializer.string(obj.y_rot, buffer, bufferOffset);
    // Serialize message field [z_rot]
    bufferOffset = _serializer.string(obj.z_rot, buffer, bufferOffset);
    // Serialize message field [max_vel]
    bufferOffset = _serializer.string(obj.max_vel, buffer, bufferOffset);
    // Serialize message field [exe_time]
    bufferOffset = _serializer.string(obj.exe_time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveJointsRequest
    let len;
    let data = new MoveJointsRequest(null);
    // Deserialize message field [joint_name]
    data.joint_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [x_pos]
    data.x_pos = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [y_pos]
    data.y_pos = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [z_pos]
    data.z_pos = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [x_rot]
    data.x_rot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [y_rot]
    data.y_rot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [z_rot]
    data.z_rot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [max_vel]
    data.max_vel = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [exe_time]
    data.exe_time = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.joint_name.length;
    length += object.x_pos.length;
    length += object.y_pos.length;
    length += object.z_pos.length;
    length += object.x_rot.length;
    length += object.y_rot.length;
    length += object.z_rot.length;
    length += object.max_vel.length;
    length += object.exe_time.length;
    return length + 36;
  }

  static datatype() {
    // Returns string type for a service object
    return 'nao_control_tutorial_2/MoveJointsRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bdc252503ebb73978a5304b525aec785';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    string joint_name
    string x_pos
    string y_pos
    string z_pos
    string x_rot
    string y_rot
    string z_rot
    string max_vel
    string exe_time
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MoveJointsRequest(null);
    if (msg.joint_name !== undefined) {
      resolved.joint_name = msg.joint_name;
    }
    else {
      resolved.joint_name = ''
    }

    if (msg.x_pos !== undefined) {
      resolved.x_pos = msg.x_pos;
    }
    else {
      resolved.x_pos = ''
    }

    if (msg.y_pos !== undefined) {
      resolved.y_pos = msg.y_pos;
    }
    else {
      resolved.y_pos = ''
    }

    if (msg.z_pos !== undefined) {
      resolved.z_pos = msg.z_pos;
    }
    else {
      resolved.z_pos = ''
    }

    if (msg.x_rot !== undefined) {
      resolved.x_rot = msg.x_rot;
    }
    else {
      resolved.x_rot = ''
    }

    if (msg.y_rot !== undefined) {
      resolved.y_rot = msg.y_rot;
    }
    else {
      resolved.y_rot = ''
    }

    if (msg.z_rot !== undefined) {
      resolved.z_rot = msg.z_rot;
    }
    else {
      resolved.z_rot = ''
    }

    if (msg.max_vel !== undefined) {
      resolved.max_vel = msg.max_vel;
    }
    else {
      resolved.max_vel = ''
    }

    if (msg.exe_time !== undefined) {
      resolved.exe_time = msg.exe_time;
    }
    else {
      resolved.exe_time = ''
    }

    return resolved;
    }
};

class MoveJointsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_pos = null;
      this.y_pos = null;
      this.z_pos = null;
      this.x_rot = null;
      this.y_rot = null;
      this.z_rot = null;
    }
    else {
      if (initObj.hasOwnProperty('x_pos')) {
        this.x_pos = initObj.x_pos
      }
      else {
        this.x_pos = 0.0;
      }
      if (initObj.hasOwnProperty('y_pos')) {
        this.y_pos = initObj.y_pos
      }
      else {
        this.y_pos = 0.0;
      }
      if (initObj.hasOwnProperty('z_pos')) {
        this.z_pos = initObj.z_pos
      }
      else {
        this.z_pos = 0.0;
      }
      if (initObj.hasOwnProperty('x_rot')) {
        this.x_rot = initObj.x_rot
      }
      else {
        this.x_rot = 0.0;
      }
      if (initObj.hasOwnProperty('y_rot')) {
        this.y_rot = initObj.y_rot
      }
      else {
        this.y_rot = 0.0;
      }
      if (initObj.hasOwnProperty('z_rot')) {
        this.z_rot = initObj.z_rot
      }
      else {
        this.z_rot = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MoveJointsResponse
    // Serialize message field [x_pos]
    bufferOffset = _serializer.float32(obj.x_pos, buffer, bufferOffset);
    // Serialize message field [y_pos]
    bufferOffset = _serializer.float32(obj.y_pos, buffer, bufferOffset);
    // Serialize message field [z_pos]
    bufferOffset = _serializer.float32(obj.z_pos, buffer, bufferOffset);
    // Serialize message field [x_rot]
    bufferOffset = _serializer.float32(obj.x_rot, buffer, bufferOffset);
    // Serialize message field [y_rot]
    bufferOffset = _serializer.float32(obj.y_rot, buffer, bufferOffset);
    // Serialize message field [z_rot]
    bufferOffset = _serializer.float32(obj.z_rot, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveJointsResponse
    let len;
    let data = new MoveJointsResponse(null);
    // Deserialize message field [x_pos]
    data.x_pos = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_pos]
    data.y_pos = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [z_pos]
    data.z_pos = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [x_rot]
    data.x_rot = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_rot]
    data.y_rot = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [z_rot]
    data.z_rot = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'nao_control_tutorial_2/MoveJointsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '918e787cb9bd62a96492d36d89fef46a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    float32 x_pos
    float32 y_pos
    float32 z_pos
    float32 x_rot
    float32 y_rot
    float32 z_rot
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MoveJointsResponse(null);
    if (msg.x_pos !== undefined) {
      resolved.x_pos = msg.x_pos;
    }
    else {
      resolved.x_pos = 0.0
    }

    if (msg.y_pos !== undefined) {
      resolved.y_pos = msg.y_pos;
    }
    else {
      resolved.y_pos = 0.0
    }

    if (msg.z_pos !== undefined) {
      resolved.z_pos = msg.z_pos;
    }
    else {
      resolved.z_pos = 0.0
    }

    if (msg.x_rot !== undefined) {
      resolved.x_rot = msg.x_rot;
    }
    else {
      resolved.x_rot = 0.0
    }

    if (msg.y_rot !== undefined) {
      resolved.y_rot = msg.y_rot;
    }
    else {
      resolved.y_rot = 0.0
    }

    if (msg.z_rot !== undefined) {
      resolved.z_rot = msg.z_rot;
    }
    else {
      resolved.z_rot = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: MoveJointsRequest,
  Response: MoveJointsResponse,
  md5sum() { return '998e30efad9a2f14084aad7450a533af'; },
  datatype() { return 'nao_control_tutorial_2/MoveJoints'; }
};
