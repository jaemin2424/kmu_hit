
"use strict";

let GetCurrentModel = require('./GetCurrentModel.js')
let SetCurrentModel = require('./SetCurrentModel.js')
let SetCurrentDirection = require('./SetCurrentDirection.js')
let GetOriginSphericalCoord = require('./GetOriginSphericalCoord.js')
let SetOriginSphericalCoord = require('./SetOriginSphericalCoord.js')
let TransformToSphericalCoord = require('./TransformToSphericalCoord.js')
let SetCurrentVelocity = require('./SetCurrentVelocity.js')
let TransformFromSphericalCoord = require('./TransformFromSphericalCoord.js')

module.exports = {
  GetCurrentModel: GetCurrentModel,
  SetCurrentModel: SetCurrentModel,
  SetCurrentDirection: SetCurrentDirection,
  GetOriginSphericalCoord: GetOriginSphericalCoord,
  SetOriginSphericalCoord: SetOriginSphericalCoord,
  TransformToSphericalCoord: TransformToSphericalCoord,
  SetCurrentVelocity: SetCurrentVelocity,
  TransformFromSphericalCoord: TransformFromSphericalCoord,
};
