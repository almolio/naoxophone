// Auto-generated. Do not edit!

// (in-package nao_control_tutorial_1.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class InterpolateJointsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.joint_names = null;
      this.steps = null;
      this.angles = null;
      this.times = null;
      this.relative = null;
      this.blocking = null;
    }
    else {
      if (initObj.hasOwnProperty('joint_names')) {
        this.joint_names = initObj.joint_names
      }
      else {
        this.joint_names = [];
      }
      if (initObj.hasOwnProperty('steps')) {
        this.steps = initObj.steps
      }
      else {
        this.steps = [];
      }
      if (initObj.hasOwnProperty('angles')) {
        this.angles = initObj.angles
      }
      else {
        this.angles = [];
      }
      if (initObj.hasOwnProperty('times')) {
        this.times = initObj.times
      }
      else {
        this.times = [];
      }
      if (initObj.hasOwnProperty('relative')) {
        this.relative = initObj.relative
      }
      else {
        this.relative = false;
      }
      if (initObj.hasOwnProperty('blocking')) {
        this.blocking = initObj.blocking
      }
      else {
        this.blocking = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type InterpolateJointsRequest
    // Serialize message field [joint_names]
    bufferOffset = _arraySerializer.string(obj.joint_names, buffer, bufferOffset, null);
    // Serialize message field [steps]
    bufferOffset = _arraySerializer.int32(obj.steps, buffer, bufferOffset, null);
    // Serialize message field [angles]
    bufferOffset = _arraySerializer.float32(obj.angles, buffer, bufferOffset, null);
    // Serialize message field [times]
    bufferOffset = _arraySerializer.float32(obj.times, buffer, bufferOffset, null);
    // Serialize message field [relative]
    bufferOffset = _serializer.bool(obj.relative, buffer, bufferOffset);
    // Serialize message field [blocking]
    bufferOffset = _serializer.bool(obj.blocking, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type InterpolateJointsRequest
    let len;
    let data = new InterpolateJointsRequest(null);
    // Deserialize message field [joint_names]
    data.joint_names = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [steps]
    data.steps = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [angles]
    data.angles = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [times]
    data.times = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [relative]
    data.relative = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [blocking]
    data.blocking = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.joint_names.forEach((val) => {
      length += 4 + val.length;
    });
    length += 4 * object.steps.length;
    length += 4 * object.angles.length;
    length += 4 * object.times.length;
    return length + 18;
  }

  static datatype() {
    // Returns string type for a service object
    return 'nao_control_tutorial_1/InterpolateJointsRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3993511ed99026e2e0304c1be844a63e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    string[] joint_names
    int32[] steps
    float32[] angles
    float32[] times
    bool relative
    bool blocking
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new InterpolateJointsRequest(null);
    if (msg.joint_names !== undefined) {
      resolved.joint_names = msg.joint_names;
    }
    else {
      resolved.joint_names = []
    }

    if (msg.steps !== undefined) {
      resolved.steps = msg.steps;
    }
    else {
      resolved.steps = []
    }

    if (msg.angles !== undefined) {
      resolved.angles = msg.angles;
    }
    else {
      resolved.angles = []
    }

    if (msg.times !== undefined) {
      resolved.times = msg.times;
    }
    else {
      resolved.times = []
    }

    if (msg.relative !== undefined) {
      resolved.relative = msg.relative;
    }
    else {
      resolved.relative = false
    }

    if (msg.blocking !== undefined) {
      resolved.blocking = msg.blocking;
    }
    else {
      resolved.blocking = false
    }

    return resolved;
    }
};

class InterpolateJointsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.status = null;
    }
    else {
      if (initObj.hasOwnProperty('status')) {
        this.status = initObj.status
      }
      else {
        this.status = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type InterpolateJointsResponse
    // Serialize message field [status]
    bufferOffset = _serializer.bool(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type InterpolateJointsResponse
    let len;
    let data = new InterpolateJointsResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'nao_control_tutorial_1/InterpolateJointsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3a1255d4d998bd4d6585c64639b5ee9a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    bool status
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new InterpolateJointsResponse(null);
    if (msg.status !== undefined) {
      resolved.status = msg.status;
    }
    else {
      resolved.status = false
    }

    return resolved;
    }
};

module.exports = {
  Request: InterpolateJointsRequest,
  Response: InterpolateJointsResponse,
  md5sum() { return 'd23b0af1b474d5848e69b3a31bdacede'; },
  datatype() { return 'nao_control_tutorial_1/InterpolateJoints'; }
};
