/************** 
 * Test1 *
 **************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'test1';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
flowScheduler.add(howitworksRoutineBegin());
flowScheduler.add(howitworksRoutineEachFrame());
flowScheduler.add(howitworksRoutineEnd());
flowScheduler.add(testRoutineBegin());
flowScheduler.add(testRoutineEachFrame());
flowScheduler.add(testRoutineEnd());
flowScheduler.add(test_passedRoutineBegin());
flowScheduler.add(test_passedRoutineEachFrame());
flowScheduler.add(test_passedRoutineEnd());
flowScheduler.add(red0_5RoutineBegin());
flowScheduler.add(red0_5RoutineEachFrame());
flowScheduler.add(red0_5RoutineEnd());
flowScheduler.add(red0_625RoutineBegin());
flowScheduler.add(red0_625RoutineEachFrame());
flowScheduler.add(red0_625RoutineEnd());
flowScheduler.add(yellow0_5RoutineBegin());
flowScheduler.add(yellow0_5RoutineEachFrame());
flowScheduler.add(yellow0_5RoutineEnd());
flowScheduler.add(blue0_5RoutineBegin());
flowScheduler.add(blue0_5RoutineEachFrame());
flowScheduler.add(blue0_5RoutineEnd());
flowScheduler.add(blue0_625RoutineBegin());
flowScheduler.add(blue0_625RoutineEachFrame());
flowScheduler.add(blue0_625RoutineEnd());
flowScheduler.add(green0_5RoutineBegin());
flowScheduler.add(green0_5RoutineEachFrame());
flowScheduler.add(green0_5RoutineEnd());
flowScheduler.add(green0_625RoutineBegin());
flowScheduler.add(green0_625RoutineEachFrame());
flowScheduler.add(green0_625RoutineEnd());
flowScheduler.add(purple0_5RoutineBegin());
flowScheduler.add(purple0_5RoutineEachFrame());
flowScheduler.add(purple0_5RoutineEnd());
flowScheduler.add(purple0_625RoutineBegin());
flowScheduler.add(purple0_625RoutineEachFrame());
flowScheduler.add(purple0_625RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var introClock;
var text;
var endintro;
var howitworksClock;
var text_2;
var endhowitworks;
var testClock;
var testpolygon;
var key_resp;
var test_passedClock;
var text_3;
var key_resp_2;
var red0_5Clock;
var res_red_0_5;
var polygon_red_0_5;
var red0_625Clock;
var polygon_red_0_625;
var res_red_0_625;
var yellow0_5Clock;
var polygon_yellow_0_5;
var blue0_5Clock;
var polygon_blue_0_5;
var res_blue_0_5;
var blue0_625Clock;
var polygon_blue_0_625;
var res_blue_0_625;
var green0_5Clock;
var polygon_green_0_5;
var res_green_0_5;
var green0_625Clock;
var polygon_green_0_625;
var res_green_0_625;
var purple0_5Clock;
var polygon_purple_0_5;
var res_purple_0_5;
var purple0_625Clock;
var polygon_purple_0_625;
var res_purple_0_625;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Hello\n\nWelcome to the PsychoPy script developed by Eli, for testing the human reaction time. I really appreciate your participation as every piece of data contributes to the final conclusion\n\nPress the space bar when you have finished reading',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  endintro = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "howitworks"
  howitworksClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'This test is made of two parts\nVisual and Ad\n\nThis test aims to test your reaction time. When you hear the sound being played or the image being shown, press the space bar on the keyboard as soon as you can. Do not try to predict the time that the stimulus will start as all stimuli are generated at random timings\n\nThe first one will be the test run for you familiarise with this test\n\nPress the space bar when you have finished reading\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  endhowitworks = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test"
  testClock = new util.Clock();
  testpolygon = new visual.Polygon({
    win: psychoJS.window, name: 'testpolygon', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('red'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test_passed"
  test_passedClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Congrats!!!! You have done you test run\n\nPress space bar to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "red0_5"
  red0_5Clock = new util.Clock();
  res_red_0_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  polygon_red_0_5 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_red_0_5', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0039, (- 1.0), (- 1.0)]),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "red0_625"
  red0_625Clock = new util.Clock();
  polygon_red_0_625 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_red_0_625', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.2471, (- 1.0), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_red_0_625 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "yellow0_5"
  yellow0_5Clock = new util.Clock();
  polygon_yellow_0_5 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_yellow_0_5', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "blue0_5"
  blue0_5Clock = new util.Clock();
  polygon_blue_0_5 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_blue_0_5', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 0.3333), 0.0]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_blue_0_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blue0_625"
  blue0_625Clock = new util.Clock();
  polygon_blue_0_625 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_blue_0_625', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 0.1667), 0.25]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_blue_0_625 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "green0_5"
  green0_5Clock = new util.Clock();
  polygon_green_0_5 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_green_0_5', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 0.6667), 0.0, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_green_0_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "green0_625"
  green0_625Clock = new util.Clock();
  polygon_green_0_625 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_green_0_625', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 0.5833), 0.25, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_green_0_625 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "purple0_5"
  purple0_5Clock = new util.Clock();
  polygon_purple_0_5 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_purple_0_5', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, (- 1.0), 0.0]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_purple_0_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "purple0_625"
  purple0_625Clock = new util.Clock();
  polygon_purple_0_625 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_purple_0_625', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.25, (- 1.0), 0.25]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_purple_0_625 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _endintro_allKeys;
var introComponents;
function introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro' ---
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('intro.started', globalClock.getTime());
    endintro.keys = undefined;
    endintro.rt = undefined;
    _endintro_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(text);
    introComponents.push(endintro);
    
    for (const thisComponent of introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro' ---
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *endintro* updates
    if (t >= 2.0 && endintro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endintro.tStart = t;  // (not accounting for frame time here)
      endintro.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endintro.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endintro.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endintro.clearEvents(); });
    }
    
    if (endintro.status === PsychoJS.Status.STARTED) {
      let theseKeys = endintro.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _endintro_allKeys = _endintro_allKeys.concat(theseKeys);
      if (_endintro_allKeys.length > 0) {
        endintro.keys = _endintro_allKeys[_endintro_allKeys.length - 1].name;  // just the last key pressed
        endintro.rt = _endintro_allKeys[_endintro_allKeys.length - 1].rt;
        endintro.duration = _endintro_allKeys[_endintro_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro' ---
    for (const thisComponent of introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('intro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endintro.corr, level);
    }
    psychoJS.experiment.addData('endintro.keys', endintro.keys);
    if (typeof endintro.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endintro.rt', endintro.rt);
        psychoJS.experiment.addData('endintro.duration', endintro.duration);
        routineTimer.reset();
        }
    
    endintro.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _endhowitworks_allKeys;
var howitworksComponents;
function howitworksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'howitworks' ---
    t = 0;
    howitworksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('howitworks.started', globalClock.getTime());
    endhowitworks.keys = undefined;
    endhowitworks.rt = undefined;
    _endhowitworks_allKeys = [];
    // keep track of which components have finished
    howitworksComponents = [];
    howitworksComponents.push(text_2);
    howitworksComponents.push(endhowitworks);
    
    for (const thisComponent of howitworksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function howitworksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'howitworks' ---
    // get current time
    t = howitworksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // *endhowitworks* updates
    if (t >= 5.0 && endhowitworks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endhowitworks.tStart = t;  // (not accounting for frame time here)
      endhowitworks.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endhowitworks.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endhowitworks.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endhowitworks.clearEvents(); });
    }
    
    if (endhowitworks.status === PsychoJS.Status.STARTED) {
      let theseKeys = endhowitworks.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _endhowitworks_allKeys = _endhowitworks_allKeys.concat(theseKeys);
      if (_endhowitworks_allKeys.length > 0) {
        endhowitworks.keys = _endhowitworks_allKeys[_endhowitworks_allKeys.length - 1].name;  // just the last key pressed
        endhowitworks.rt = _endhowitworks_allKeys[_endhowitworks_allKeys.length - 1].rt;
        endhowitworks.duration = _endhowitworks_allKeys[_endhowitworks_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of howitworksComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function howitworksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'howitworks' ---
    for (const thisComponent of howitworksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('howitworks.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endhowitworks.corr, level);
    }
    psychoJS.experiment.addData('endhowitworks.keys', endhowitworks.keys);
    if (typeof endhowitworks.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endhowitworks.rt', endhowitworks.rt);
        psychoJS.experiment.addData('endhowitworks.duration', endhowitworks.duration);
        routineTimer.reset();
        }
    
    endhowitworks.stop();
    // the Routine "howitworks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var testComponents;
function testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test' ---
    t = 0;
    testClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('test.started', globalClock.getTime());
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    testComponents = [];
    testComponents.push(testpolygon);
    testComponents.push(key_resp);
    
    for (const thisComponent of testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test' ---
    // get current time
    t = testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *testpolygon* updates
    if (t >= 2.0 && testpolygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      testpolygon.tStart = t;  // (not accounting for frame time here)
      testpolygon.frameNStart = frameN;  // exact frame index
      
      testpolygon.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 2.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of testComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test' ---
    for (const thisComponent of testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var test_passedComponents;
function test_passedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test_passed' ---
    t = 0;
    test_passedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('test_passed.started', globalClock.getTime());
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    test_passedComponents = [];
    test_passedComponents.push(text_3);
    test_passedComponents.push(key_resp_2);
    
    for (const thisComponent of test_passedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function test_passedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test_passed' ---
    // get current time
    t = test_passedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 1 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 1 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test_passedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test_passedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test_passed' ---
    for (const thisComponent of test_passedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test_passed.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "test_passed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_red_0_5_allKeys;
var red0_5Components;
function red0_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'red0_5' ---
    t = 0;
    red0_5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('red0_5.started', globalClock.getTime());
    res_red_0_5.keys = undefined;
    res_red_0_5.rt = undefined;
    _res_red_0_5_allKeys = [];
    // keep track of which components have finished
    red0_5Components = [];
    red0_5Components.push(res_red_0_5);
    red0_5Components.push(polygon_red_0_5);
    
    for (const thisComponent of red0_5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function red0_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'red0_5' ---
    // get current time
    t = red0_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *res_red_0_5* updates
    if (t >= 2 && res_red_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_red_0_5.tStart = t;  // (not accounting for frame time here)
      res_red_0_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_red_0_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_red_0_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_red_0_5.clearEvents(); });
    }
    
    if (res_red_0_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_red_0_5.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_red_0_5_allKeys = _res_red_0_5_allKeys.concat(theseKeys);
      if (_res_red_0_5_allKeys.length > 0) {
        res_red_0_5.keys = _res_red_0_5_allKeys[_res_red_0_5_allKeys.length - 1].name;  // just the last key pressed
        res_red_0_5.rt = _res_red_0_5_allKeys[_res_red_0_5_allKeys.length - 1].rt;
        res_red_0_5.duration = _res_red_0_5_allKeys[_res_red_0_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *polygon_red_0_5* updates
    if (t >= 2 && polygon_red_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_red_0_5.tStart = t;  // (not accounting for frame time here)
      polygon_red_0_5.frameNStart = frameN;  // exact frame index
      
      polygon_red_0_5.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of red0_5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function red0_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'red0_5' ---
    for (const thisComponent of red0_5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('red0_5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_red_0_5.corr, level);
    }
    psychoJS.experiment.addData('res_red_0_5.keys', res_red_0_5.keys);
    if (typeof res_red_0_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_red_0_5.rt', res_red_0_5.rt);
        psychoJS.experiment.addData('res_red_0_5.duration', res_red_0_5.duration);
        routineTimer.reset();
        }
    
    res_red_0_5.stop();
    // the Routine "red0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_red_0_625_allKeys;
var red0_625Components;
function red0_625RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'red0_625' ---
    t = 0;
    red0_625Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('red0_625.started', globalClock.getTime());
    res_red_0_625.keys = undefined;
    res_red_0_625.rt = undefined;
    _res_red_0_625_allKeys = [];
    // keep track of which components have finished
    red0_625Components = [];
    red0_625Components.push(polygon_red_0_625);
    red0_625Components.push(res_red_0_625);
    
    for (const thisComponent of red0_625Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function red0_625RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'red0_625' ---
    // get current time
    t = red0_625Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_red_0_625* updates
    if (t >= 2 && polygon_red_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_red_0_625.tStart = t;  // (not accounting for frame time here)
      polygon_red_0_625.frameNStart = frameN;  // exact frame index
      
      polygon_red_0_625.setAutoDraw(true);
    }
    
    
    // *res_red_0_625* updates
    if (t >= 2 && res_red_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_red_0_625.tStart = t;  // (not accounting for frame time here)
      res_red_0_625.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_red_0_625.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_red_0_625.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_red_0_625.clearEvents(); });
    }
    
    if (res_red_0_625.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_red_0_625.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_red_0_625_allKeys = _res_red_0_625_allKeys.concat(theseKeys);
      if (_res_red_0_625_allKeys.length > 0) {
        res_red_0_625.keys = _res_red_0_625_allKeys[_res_red_0_625_allKeys.length - 1].name;  // just the last key pressed
        res_red_0_625.rt = _res_red_0_625_allKeys[_res_red_0_625_allKeys.length - 1].rt;
        res_red_0_625.duration = _res_red_0_625_allKeys[_res_red_0_625_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of red0_625Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function red0_625RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'red0_625' ---
    for (const thisComponent of red0_625Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('red0_625.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_red_0_625.corr, level);
    }
    psychoJS.experiment.addData('res_red_0_625.keys', res_red_0_625.keys);
    if (typeof res_red_0_625.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_red_0_625.rt', res_red_0_625.rt);
        psychoJS.experiment.addData('res_red_0_625.duration', res_red_0_625.duration);
        routineTimer.reset();
        }
    
    res_red_0_625.stop();
    // the Routine "red0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var yellow0_5Components;
function yellow0_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'yellow0_5' ---
    t = 0;
    yellow0_5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('yellow0_5.started', globalClock.getTime());
    // keep track of which components have finished
    yellow0_5Components = [];
    yellow0_5Components.push(polygon_yellow_0_5);
    
    for (const thisComponent of yellow0_5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function yellow0_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'yellow0_5' ---
    // get current time
    t = yellow0_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_yellow_0_5* updates
    if (t >= 2 && polygon_yellow_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_yellow_0_5.tStart = t;  // (not accounting for frame time here)
      polygon_yellow_0_5.frameNStart = frameN;  // exact frame index
      
      polygon_yellow_0_5.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of yellow0_5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function yellow0_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'yellow0_5' ---
    for (const thisComponent of yellow0_5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('yellow0_5.stopped', globalClock.getTime());
    // the Routine "yellow0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_blue_0_5_allKeys;
var blue0_5Components;
function blue0_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blue0_5' ---
    t = 0;
    blue0_5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('blue0_5.started', globalClock.getTime());
    res_blue_0_5.keys = undefined;
    res_blue_0_5.rt = undefined;
    _res_blue_0_5_allKeys = [];
    // keep track of which components have finished
    blue0_5Components = [];
    blue0_5Components.push(polygon_blue_0_5);
    blue0_5Components.push(res_blue_0_5);
    
    for (const thisComponent of blue0_5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blue0_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blue0_5' ---
    // get current time
    t = blue0_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_blue_0_5* updates
    if (t >= 2 && polygon_blue_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_blue_0_5.tStart = t;  // (not accounting for frame time here)
      polygon_blue_0_5.frameNStart = frameN;  // exact frame index
      
      polygon_blue_0_5.setAutoDraw(true);
    }
    
    
    // *res_blue_0_5* updates
    if (t >= 2 && res_blue_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_blue_0_5.tStart = t;  // (not accounting for frame time here)
      res_blue_0_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_blue_0_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_blue_0_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_blue_0_5.clearEvents(); });
    }
    
    if (res_blue_0_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_blue_0_5.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_blue_0_5_allKeys = _res_blue_0_5_allKeys.concat(theseKeys);
      if (_res_blue_0_5_allKeys.length > 0) {
        res_blue_0_5.keys = _res_blue_0_5_allKeys[_res_blue_0_5_allKeys.length - 1].name;  // just the last key pressed
        res_blue_0_5.rt = _res_blue_0_5_allKeys[_res_blue_0_5_allKeys.length - 1].rt;
        res_blue_0_5.duration = _res_blue_0_5_allKeys[_res_blue_0_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blue0_5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blue0_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blue0_5' ---
    for (const thisComponent of blue0_5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blue0_5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_blue_0_5.corr, level);
    }
    psychoJS.experiment.addData('res_blue_0_5.keys', res_blue_0_5.keys);
    if (typeof res_blue_0_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_blue_0_5.rt', res_blue_0_5.rt);
        psychoJS.experiment.addData('res_blue_0_5.duration', res_blue_0_5.duration);
        routineTimer.reset();
        }
    
    res_blue_0_5.stop();
    // the Routine "blue0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_blue_0_625_allKeys;
var blue0_625Components;
function blue0_625RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blue0_625' ---
    t = 0;
    blue0_625Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('blue0_625.started', globalClock.getTime());
    res_blue_0_625.keys = undefined;
    res_blue_0_625.rt = undefined;
    _res_blue_0_625_allKeys = [];
    // keep track of which components have finished
    blue0_625Components = [];
    blue0_625Components.push(polygon_blue_0_625);
    blue0_625Components.push(res_blue_0_625);
    
    for (const thisComponent of blue0_625Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blue0_625RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blue0_625' ---
    // get current time
    t = blue0_625Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_blue_0_625* updates
    if (t >= 2 && polygon_blue_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_blue_0_625.tStart = t;  // (not accounting for frame time here)
      polygon_blue_0_625.frameNStart = frameN;  // exact frame index
      
      polygon_blue_0_625.setAutoDraw(true);
    }
    
    
    // *res_blue_0_625* updates
    if (t >= 2 && res_blue_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_blue_0_625.tStart = t;  // (not accounting for frame time here)
      res_blue_0_625.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_blue_0_625.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_blue_0_625.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_blue_0_625.clearEvents(); });
    }
    
    if (res_blue_0_625.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_blue_0_625.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_blue_0_625_allKeys = _res_blue_0_625_allKeys.concat(theseKeys);
      if (_res_blue_0_625_allKeys.length > 0) {
        res_blue_0_625.keys = _res_blue_0_625_allKeys[_res_blue_0_625_allKeys.length - 1].name;  // just the last key pressed
        res_blue_0_625.rt = _res_blue_0_625_allKeys[_res_blue_0_625_allKeys.length - 1].rt;
        res_blue_0_625.duration = _res_blue_0_625_allKeys[_res_blue_0_625_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blue0_625Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blue0_625RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blue0_625' ---
    for (const thisComponent of blue0_625Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blue0_625.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_blue_0_625.corr, level);
    }
    psychoJS.experiment.addData('res_blue_0_625.keys', res_blue_0_625.keys);
    if (typeof res_blue_0_625.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_blue_0_625.rt', res_blue_0_625.rt);
        psychoJS.experiment.addData('res_blue_0_625.duration', res_blue_0_625.duration);
        routineTimer.reset();
        }
    
    res_blue_0_625.stop();
    // the Routine "blue0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_green_0_5_allKeys;
var green0_5Components;
function green0_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'green0_5' ---
    t = 0;
    green0_5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('green0_5.started', globalClock.getTime());
    res_green_0_5.keys = undefined;
    res_green_0_5.rt = undefined;
    _res_green_0_5_allKeys = [];
    // keep track of which components have finished
    green0_5Components = [];
    green0_5Components.push(polygon_green_0_5);
    green0_5Components.push(res_green_0_5);
    
    for (const thisComponent of green0_5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function green0_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'green0_5' ---
    // get current time
    t = green0_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_green_0_5* updates
    if (t >= 2 && polygon_green_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_green_0_5.tStart = t;  // (not accounting for frame time here)
      polygon_green_0_5.frameNStart = frameN;  // exact frame index
      
      polygon_green_0_5.setAutoDraw(true);
    }
    
    
    // *res_green_0_5* updates
    if (t >= 2 && res_green_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_green_0_5.tStart = t;  // (not accounting for frame time here)
      res_green_0_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_green_0_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_green_0_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_green_0_5.clearEvents(); });
    }
    
    if (res_green_0_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_green_0_5.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_green_0_5_allKeys = _res_green_0_5_allKeys.concat(theseKeys);
      if (_res_green_0_5_allKeys.length > 0) {
        res_green_0_5.keys = _res_green_0_5_allKeys[_res_green_0_5_allKeys.length - 1].name;  // just the last key pressed
        res_green_0_5.rt = _res_green_0_5_allKeys[_res_green_0_5_allKeys.length - 1].rt;
        res_green_0_5.duration = _res_green_0_5_allKeys[_res_green_0_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of green0_5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function green0_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'green0_5' ---
    for (const thisComponent of green0_5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('green0_5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_green_0_5.corr, level);
    }
    psychoJS.experiment.addData('res_green_0_5.keys', res_green_0_5.keys);
    if (typeof res_green_0_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_green_0_5.rt', res_green_0_5.rt);
        psychoJS.experiment.addData('res_green_0_5.duration', res_green_0_5.duration);
        routineTimer.reset();
        }
    
    res_green_0_5.stop();
    // the Routine "green0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_green_0_625_allKeys;
var green0_625Components;
function green0_625RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'green0_625' ---
    t = 0;
    green0_625Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('green0_625.started', globalClock.getTime());
    res_green_0_625.keys = undefined;
    res_green_0_625.rt = undefined;
    _res_green_0_625_allKeys = [];
    // keep track of which components have finished
    green0_625Components = [];
    green0_625Components.push(polygon_green_0_625);
    green0_625Components.push(res_green_0_625);
    
    for (const thisComponent of green0_625Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function green0_625RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'green0_625' ---
    // get current time
    t = green0_625Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_green_0_625* updates
    if (t >= 2 && polygon_green_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_green_0_625.tStart = t;  // (not accounting for frame time here)
      polygon_green_0_625.frameNStart = frameN;  // exact frame index
      
      polygon_green_0_625.setAutoDraw(true);
    }
    
    
    // *res_green_0_625* updates
    if (t >= 2 && res_green_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_green_0_625.tStart = t;  // (not accounting for frame time here)
      res_green_0_625.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_green_0_625.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_green_0_625.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_green_0_625.clearEvents(); });
    }
    
    if (res_green_0_625.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_green_0_625.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_green_0_625_allKeys = _res_green_0_625_allKeys.concat(theseKeys);
      if (_res_green_0_625_allKeys.length > 0) {
        res_green_0_625.keys = _res_green_0_625_allKeys[_res_green_0_625_allKeys.length - 1].name;  // just the last key pressed
        res_green_0_625.rt = _res_green_0_625_allKeys[_res_green_0_625_allKeys.length - 1].rt;
        res_green_0_625.duration = _res_green_0_625_allKeys[_res_green_0_625_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of green0_625Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function green0_625RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'green0_625' ---
    for (const thisComponent of green0_625Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('green0_625.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_green_0_625.corr, level);
    }
    psychoJS.experiment.addData('res_green_0_625.keys', res_green_0_625.keys);
    if (typeof res_green_0_625.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_green_0_625.rt', res_green_0_625.rt);
        psychoJS.experiment.addData('res_green_0_625.duration', res_green_0_625.duration);
        routineTimer.reset();
        }
    
    res_green_0_625.stop();
    // the Routine "green0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_purple_0_5_allKeys;
var purple0_5Components;
function purple0_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'purple0_5' ---
    t = 0;
    purple0_5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('purple0_5.started', globalClock.getTime());
    res_purple_0_5.keys = undefined;
    res_purple_0_5.rt = undefined;
    _res_purple_0_5_allKeys = [];
    // keep track of which components have finished
    purple0_5Components = [];
    purple0_5Components.push(polygon_purple_0_5);
    purple0_5Components.push(res_purple_0_5);
    
    for (const thisComponent of purple0_5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function purple0_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'purple0_5' ---
    // get current time
    t = purple0_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_purple_0_5* updates
    if (t >= 2 && polygon_purple_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_purple_0_5.tStart = t;  // (not accounting for frame time here)
      polygon_purple_0_5.frameNStart = frameN;  // exact frame index
      
      polygon_purple_0_5.setAutoDraw(true);
    }
    
    
    // *res_purple_0_5* updates
    if (t >= 2 && res_purple_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_purple_0_5.tStart = t;  // (not accounting for frame time here)
      res_purple_0_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_purple_0_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_purple_0_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_purple_0_5.clearEvents(); });
    }
    
    if (res_purple_0_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_purple_0_5.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_purple_0_5_allKeys = _res_purple_0_5_allKeys.concat(theseKeys);
      if (_res_purple_0_5_allKeys.length > 0) {
        res_purple_0_5.keys = _res_purple_0_5_allKeys[_res_purple_0_5_allKeys.length - 1].name;  // just the last key pressed
        res_purple_0_5.rt = _res_purple_0_5_allKeys[_res_purple_0_5_allKeys.length - 1].rt;
        res_purple_0_5.duration = _res_purple_0_5_allKeys[_res_purple_0_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of purple0_5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function purple0_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'purple0_5' ---
    for (const thisComponent of purple0_5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('purple0_5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_purple_0_5.corr, level);
    }
    psychoJS.experiment.addData('res_purple_0_5.keys', res_purple_0_5.keys);
    if (typeof res_purple_0_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_purple_0_5.rt', res_purple_0_5.rt);
        psychoJS.experiment.addData('res_purple_0_5.duration', res_purple_0_5.duration);
        routineTimer.reset();
        }
    
    res_purple_0_5.stop();
    // the Routine "purple0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_purple_0_625_allKeys;
var purple0_625Components;
function purple0_625RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'purple0_625' ---
    t = 0;
    purple0_625Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('purple0_625.started', globalClock.getTime());
    res_purple_0_625.keys = undefined;
    res_purple_0_625.rt = undefined;
    _res_purple_0_625_allKeys = [];
    // keep track of which components have finished
    purple0_625Components = [];
    purple0_625Components.push(polygon_purple_0_625);
    purple0_625Components.push(res_purple_0_625);
    
    for (const thisComponent of purple0_625Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function purple0_625RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'purple0_625' ---
    // get current time
    t = purple0_625Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_purple_0_625* updates
    if (t >= 2 && polygon_purple_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_purple_0_625.tStart = t;  // (not accounting for frame time here)
      polygon_purple_0_625.frameNStart = frameN;  // exact frame index
      
      polygon_purple_0_625.setAutoDraw(true);
    }
    
    
    // *res_purple_0_625* updates
    if (t >= 2 && res_purple_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_purple_0_625.tStart = t;  // (not accounting for frame time here)
      res_purple_0_625.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_purple_0_625.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_purple_0_625.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_purple_0_625.clearEvents(); });
    }
    
    if (res_purple_0_625.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_purple_0_625.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_purple_0_625_allKeys = _res_purple_0_625_allKeys.concat(theseKeys);
      if (_res_purple_0_625_allKeys.length > 0) {
        res_purple_0_625.keys = _res_purple_0_625_allKeys[_res_purple_0_625_allKeys.length - 1].name;  // just the last key pressed
        res_purple_0_625.rt = _res_purple_0_625_allKeys[_res_purple_0_625_allKeys.length - 1].rt;
        res_purple_0_625.duration = _res_purple_0_625_allKeys[_res_purple_0_625_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of purple0_625Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function purple0_625RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'purple0_625' ---
    for (const thisComponent of purple0_625Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('purple0_625.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_purple_0_625.corr, level);
    }
    psychoJS.experiment.addData('res_purple_0_625.keys', res_purple_0_625.keys);
    if (typeof res_purple_0_625.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_purple_0_625.rt', res_purple_0_625.rt);
        psychoJS.experiment.addData('res_purple_0_625.duration', res_purple_0_625.duration);
        routineTimer.reset();
        }
    
    res_purple_0_625.stop();
    // the Routine "purple0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
