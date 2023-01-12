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

class timedInterpolationRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.names = null;
      this.angleLists = null;
      this.times = null;
    }
    else {
      if (initObj.hasOwnProperty('names')) {
        this.names = initObj.names
      }
      else {
        this.names = '';
      }
      if (initObj.hasOwnProperty('angleLists')) {
        this.angleLists = initObj.angleLists
      }
      else {
        this.angleLists = '';
      }
      if (initObj.hasOwnProperty('times')) {
        this.times = initObj.times
      }
      else {
        this.times = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type timedInterpolationRequest
    // Serialize message field [names]
    bufferOffset = _serializer.string(obj.names, buffer, bufferOffset);
    // Serialize message field [angleLists]
    bufferOffset = _serializer.string(obj.angleLists, buffer, bufferOffset);
    // Serialize message field [times]
    bufferOffset = _serializer.string(obj.times, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type timedInterpolationRequest
    let len;
    let data = new timedInterpolationRequest(null);
    // Deserialize message field [names]
    data.names = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [angleLists]
    data.angleLists = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [times]
    data.times = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.names.length;
    length += object.angleLists.length;
    length += object.times.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'nao_control_tutorial_1/timedInterpolationRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '14f1208cf1fdbcb6fb75913ee7ea20cb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    string      names
    string      angleLists
    string      times
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new timedInterpolationRequest(null);
    if (msg.names !== undefined) {
      resolved.names = msg.names;
    }
    else {
      resolved.names = ''
    }

    if (msg.angleLists !== undefined) {
      resolved.angleLists = msg.angleLists;
    }
    else {
      resolved.angleLists = ''
    }

    if (msg.times !== undefined) {
      resolved.times = msg.times;
    }
    else {
      resolved.times = ''
    }

    return resolved;
    }
};

class timedInterpolationResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.angle = null;
    }
    else {
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type timedInterpolationResponse
    // Serialize message field [angle]
    bufferOffset = _serializer.float32(obj.angle, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type timedInterpolationResponse
    let len;
    let data = new timedInterpolationResponse(null);
    // Deserialize message field [angle]
    data.angle = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'nao_control_tutorial_1/timedInterpolationResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2d11dcdbe5a6f73dd324353dc52315ab';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    float32    angle
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new timedInterpolationResponse(null);
    if (msg.angle !== undefined) {
      resolved.angle = msg.angle;
    }
    else {
      resolved.angle = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: timedInterpolationRequest,
  Response: timedInterpolationResponse,
  md5sum() { return '062c7554adac44a703a2883e86bbb559'; },
  datatype() { return 'nao_control_tutorial_1/timedInterpolation'; }
};
