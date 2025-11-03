
"use strict";

let ClearWaypoints = require('./ClearWaypoints.js')
let SetPIDParams = require('./SetPIDParams.js')
let GetSMControllerParams = require('./GetSMControllerParams.js')
let Hold = require('./Hold.js')
let SwitchToAutomatic = require('./SwitchToAutomatic.js')
let SetSMControllerParams = require('./SetSMControllerParams.js')
let GetPIDParams = require('./GetPIDParams.js')
let AddWaypoint = require('./AddWaypoint.js')
let GoToIncremental = require('./GoToIncremental.js')
let GetWaypoints = require('./GetWaypoints.js')
let StartTrajectory = require('./StartTrajectory.js')
let InitHelicalTrajectory = require('./InitHelicalTrajectory.js')
let InitCircularTrajectory = require('./InitCircularTrajectory.js')
let ResetController = require('./ResetController.js')
let SwitchToManual = require('./SwitchToManual.js')
let SetMBSMControllerParams = require('./SetMBSMControllerParams.js')
let InitWaypointSet = require('./InitWaypointSet.js')
let InitWaypointsFromFile = require('./InitWaypointsFromFile.js')
let IsRunningTrajectory = require('./IsRunningTrajectory.js')
let GetMBSMControllerParams = require('./GetMBSMControllerParams.js')
let GoTo = require('./GoTo.js')
let InitRectTrajectory = require('./InitRectTrajectory.js')

module.exports = {
  ClearWaypoints: ClearWaypoints,
  SetPIDParams: SetPIDParams,
  GetSMControllerParams: GetSMControllerParams,
  Hold: Hold,
  SwitchToAutomatic: SwitchToAutomatic,
  SetSMControllerParams: SetSMControllerParams,
  GetPIDParams: GetPIDParams,
  AddWaypoint: AddWaypoint,
  GoToIncremental: GoToIncremental,
  GetWaypoints: GetWaypoints,
  StartTrajectory: StartTrajectory,
  InitHelicalTrajectory: InitHelicalTrajectory,
  InitCircularTrajectory: InitCircularTrajectory,
  ResetController: ResetController,
  SwitchToManual: SwitchToManual,
  SetMBSMControllerParams: SetMBSMControllerParams,
  InitWaypointSet: InitWaypointSet,
  InitWaypointsFromFile: InitWaypointsFromFile,
  IsRunningTrajectory: IsRunningTrajectory,
  GetMBSMControllerParams: GetMBSMControllerParams,
  GoTo: GoTo,
  InitRectTrajectory: InitRectTrajectory,
};
