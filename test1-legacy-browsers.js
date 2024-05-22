/************** 
 * Test1 *
 **************/


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
flowScheduler.add(red0_75RoutineBegin());
flowScheduler.add(red0_75RoutineEachFrame());
flowScheduler.add(red0_75RoutineEnd());
flowScheduler.add(red0_875RoutineBegin());
flowScheduler.add(red0_875RoutineEachFrame());
flowScheduler.add(red0_875RoutineEnd());
flowScheduler.add(red1RoutineBegin());
flowScheduler.add(red1RoutineEachFrame());
flowScheduler.add(red1RoutineEnd());
flowScheduler.add(yellow0_5RoutineBegin());
flowScheduler.add(yellow0_5RoutineEachFrame());
flowScheduler.add(yellow0_5RoutineEnd());
flowScheduler.add(yellow0_625RoutineBegin());
flowScheduler.add(yellow0_625RoutineEachFrame());
flowScheduler.add(yellow0_625RoutineEnd());
flowScheduler.add(yellow0_75RoutineBegin());
flowScheduler.add(yellow0_75RoutineEachFrame());
flowScheduler.add(yellow0_75RoutineEnd());
flowScheduler.add(yellow0_875RoutineBegin());
flowScheduler.add(yellow0_875RoutineEachFrame());
flowScheduler.add(yellow0_875RoutineEnd());
flowScheduler.add(yellow1RoutineBegin());
flowScheduler.add(yellow1RoutineEachFrame());
flowScheduler.add(yellow1RoutineEnd());
flowScheduler.add(blue0_5RoutineBegin());
flowScheduler.add(blue0_5RoutineEachFrame());
flowScheduler.add(blue0_5RoutineEnd());
flowScheduler.add(blue0_625RoutineBegin());
flowScheduler.add(blue0_625RoutineEachFrame());
flowScheduler.add(blue0_625RoutineEnd());
flowScheduler.add(blue0_75RoutineBegin());
flowScheduler.add(blue0_75RoutineEachFrame());
flowScheduler.add(blue0_75RoutineEnd());
flowScheduler.add(blue0_875RoutineBegin());
flowScheduler.add(blue0_875RoutineEachFrame());
flowScheduler.add(blue0_875RoutineEnd());
flowScheduler.add(blue1RoutineBegin());
flowScheduler.add(blue1RoutineEachFrame());
flowScheduler.add(blue1RoutineEnd());
flowScheduler.add(green0_5RoutineBegin());
flowScheduler.add(green0_5RoutineEachFrame());
flowScheduler.add(green0_5RoutineEnd());
flowScheduler.add(green0_625RoutineBegin());
flowScheduler.add(green0_625RoutineEachFrame());
flowScheduler.add(green0_625RoutineEnd());
flowScheduler.add(green0_75RoutineBegin());
flowScheduler.add(green0_75RoutineEachFrame());
flowScheduler.add(green0_75RoutineEnd());
flowScheduler.add(green0_875RoutineBegin());
flowScheduler.add(green0_875RoutineEachFrame());
flowScheduler.add(green0_875RoutineEnd());
flowScheduler.add(green1RoutineBegin());
flowScheduler.add(green1RoutineEachFrame());
flowScheduler.add(green1RoutineEnd());
flowScheduler.add(purple0_5RoutineBegin());
flowScheduler.add(purple0_5RoutineEachFrame());
flowScheduler.add(purple0_5RoutineEnd());
flowScheduler.add(purple0_625RoutineBegin());
flowScheduler.add(purple0_625RoutineEachFrame());
flowScheduler.add(purple0_625RoutineEnd());
flowScheduler.add(purple0_75RoutineBegin());
flowScheduler.add(purple0_75RoutineEachFrame());
flowScheduler.add(purple0_75RoutineEnd());
flowScheduler.add(purple0_875RoutineBegin());
flowScheduler.add(purple0_875RoutineEachFrame());
flowScheduler.add(purple0_875RoutineEnd());
flowScheduler.add(purple1RoutineBegin());
flowScheduler.add(purple1RoutineEachFrame());
flowScheduler.add(purple1RoutineEnd());
flowScheduler.add(orange0_5RoutineBegin());
flowScheduler.add(orange0_5RoutineEachFrame());
flowScheduler.add(orange0_5RoutineEnd());
flowScheduler.add(orange0_625RoutineBegin());
flowScheduler.add(orange0_625RoutineEachFrame());
flowScheduler.add(orange0_625RoutineEnd());
flowScheduler.add(orange0_75RoutineBegin());
flowScheduler.add(orange0_75RoutineEachFrame());
flowScheduler.add(orange0_75RoutineEnd());
flowScheduler.add(orange0_875RoutineBegin());
flowScheduler.add(orange0_875RoutineEachFrame());
flowScheduler.add(orange0_875RoutineEnd());
flowScheduler.add(orange1RoutineBegin());
flowScheduler.add(orange1RoutineEachFrame());
flowScheduler.add(orange1RoutineEnd());
flowScheduler.add(audiointroRoutineBegin());
flowScheduler.add(audiointroRoutineEachFrame());
flowScheduler.add(audiointroRoutineEnd());
flowScheduler.add(audiotestRoutineBegin());
flowScheduler.add(audiotestRoutineEachFrame());
flowScheduler.add(audiotestRoutineEnd());
flowScheduler.add(audiotestpassedRoutineBegin());
flowScheduler.add(audiotestpassedRoutineEachFrame());
flowScheduler.add(audiotestpassedRoutineEnd());
flowScheduler.add(audio_500Hz_0_25RoutineBegin());
flowScheduler.add(audio_500Hz_0_25RoutineEachFrame());
flowScheduler.add(audio_500Hz_0_25RoutineEnd());
flowScheduler.add(audio_500HzRoutineBegin());
flowScheduler.add(audio_500HzRoutineEachFrame());
flowScheduler.add(audio_500HzRoutineEnd());
flowScheduler.add(audio_2500HzRoutineBegin());
flowScheduler.add(audio_2500HzRoutineEachFrame());
flowScheduler.add(audio_2500HzRoutineEnd());
flowScheduler.add(audio_5000HzRoutineBegin());
flowScheduler.add(audio_5000HzRoutineEachFrame());
flowScheduler.add(audio_5000HzRoutineEnd());
flowScheduler.add(audio_7500HzRoutineBegin());
flowScheduler.add(audio_7500HzRoutineEachFrame());
flowScheduler.add(audio_7500HzRoutineEnd());
flowScheduler.add(audio_10000HzRoutineBegin());
flowScheduler.add(audio_10000HzRoutineEachFrame());
flowScheduler.add(audio_10000HzRoutineEnd());
flowScheduler.add(audio_12500HzRoutineBegin());
flowScheduler.add(audio_12500HzRoutineEachFrame());
flowScheduler.add(audio_12500HzRoutineEnd());
flowScheduler.add(audio_15000HzRoutineBegin());
flowScheduler.add(audio_15000HzRoutineEachFrame());
flowScheduler.add(audio_15000HzRoutineEnd());
flowScheduler.add(outroRoutineBegin());
flowScheduler.add(outroRoutineEachFrame());
flowScheduler.add(outroRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'audio files/2500.wav', 'path': 'audio files/2500.wav'},
    {'name': 'audio files/500.wav', 'path': 'audio files/500.wav'},
    {'name': 'audio files/5000.wav', 'path': 'audio files/5000.wav'},
    {'name': 'audio files/7500.wav', 'path': 'audio files/7500.wav'},
    {'name': 'audio files/10000.wav', 'path': 'audio files/10000.wav'},
    {'name': 'audio files/12500.wav', 'path': 'audio files/12500.wav'},
    {'name': 'audio files/15000.wav', 'path': 'audio files/15000.wav'},
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
var res_intro;
var howitworksClock;
var text_howitworks;
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
var red0_75Clock;
var polygon_red_0_75;
var res_red_0_75;
var red0_875Clock;
var polygon_red_0_875;
var res_red_0_875;
var red1Clock;
var polygon_red_1;
var res_red_1;
var yellow0_5Clock;
var polygon_0_5;
var res_yellow_0_5;
var yellow0_625Clock;
var polygon_yellow_0_625;
var res_yellow_0_625;
var yellow0_75Clock;
var polygon_yellow_0_75;
var res_yellow_0_75;
var yellow0_875Clock;
var polygon_yellow_0_875;
var res_yellow_0_875;
var yellow1Clock;
var polygon_yellow_1;
var res_yellow_1;
var blue0_5Clock;
var polygon_blue_0_5;
var res_blue_0_5;
var blue0_625Clock;
var polygon_blue_0_625;
var res_blue_0_625;
var blue0_75Clock;
var polygon_blue_0_75;
var res_blue_0_75;
var blue0_875Clock;
var polygon_blue_0_875;
var res_blue_0_875;
var blue1Clock;
var polygon_blue_1;
var res_blue_1;
var green0_5Clock;
var polygon_green_0_5;
var res_green_0_5;
var green0_625Clock;
var polygon_green_0_625;
var res_green_0_625;
var green0_75Clock;
var polygon_green_0_75;
var res_green_0_75;
var green0_875Clock;
var polygon_green_0_875;
var res_green_0_875;
var green1Clock;
var polygon_green_1;
var res_green_1;
var purple0_5Clock;
var polygon_purple_0_5;
var res_purple_0_5;
var purple0_625Clock;
var polygon_purple_0_625;
var res_purple_0_625;
var purple0_75Clock;
var polygon_purple_0_75;
var res_purple_0_75;
var purple0_875Clock;
var polygon_purple_0_875;
var res_purple_0_875;
var purple1Clock;
var polygon_purple_1;
var res_purple_1;
var orange0_5Clock;
var polygon_orange_0_5;
var res_orange_0_5;
var orange0_625Clock;
var polygon_orange_0_625;
var res_orange_0_625;
var orange0_75Clock;
var polygon_orange_0_75;
var res_orange_0_75;
var orange0_875Clock;
var polygon_res_0_875;
var res_orange_0_875;
var orange1Clock;
var polygon_orange_1;
var res_orange_1;
var audiointroClock;
var audiotext;
var audiointro_res;
var audiotestClock;
var sound_testrun;
var res_audio_testrun;
var audiotestpassedClock;
var autest_passed;
var res_testpassed;
var audio_500Hz_0_25Clock;
var sound_500Hz_0_25;
var res_500Hz_0_25;
var audio_500HzClock;
var sound_500Hz;
var res_500Hz;
var audio_2500HzClock;
var sound_2500Hz;
var res_2500Hz;
var audio_5000HzClock;
var sound_5000Hz;
var res_5000Hz;
var audio_7500HzClock;
var sound_7500Hz;
var res_7500Hz;
var audio_10000HzClock;
var sound_10000Hz;
var res_10000Hz;
var audio_12500HzClock;
var sound_12500;
var res_12500;
var audio_15000HzClock;
var sound_15000;
var res_15000Hz;
var outroClock;
var text_outro;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Hello\n\nWelcome to the PsychoPy script developed by Eli, for testing average reaction time depending on different colours. I really appreciate your participation as every piece of data contributes to the final conclusion\n\nPress the space bar when you have finished reading',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  res_intro = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "howitworks"
  howitworksClock = new util.Clock();
  text_howitworks = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_howitworks',
    text: 'This test is made of two parts\nVisual and Auditory\n\nThis test aims to test your reaction time. When you hear the sound being played or the image being shown, press the space bar on the keyboard as soon as you can. Do not try to predict the time that the stimulus will start as all stimuli are generated at random timings\n\nPlease move the mouse cursor to the edge of the screen or off screen to reduce interference. If the computer stops working during the test, please tell me\n\nThe first one will be the test run for you familiarise with this test\n\nPress the space bar when you have finished reading\n',
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
  
  // Initialize components for Routine "red0_75"
  red0_75Clock = new util.Clock();
  polygon_red_0_75 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_red_0_75', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.5, (- 1.0), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_red_0_75 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "red0_875"
  red0_875Clock = new util.Clock();
  polygon_red_0_875 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_red_0_875', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.75, (- 1.0), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_red_0_875 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "red1"
  red1Clock = new util.Clock();
  polygon_red_1 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_red_1', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([1.0, (- 1.0), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_red_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "yellow0_5"
  yellow0_5Clock = new util.Clock();
  polygon_0_5 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_0_5', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_yellow_0_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "yellow0_625"
  yellow0_625Clock = new util.Clock();
  polygon_yellow_0_625 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_yellow_0_625', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.25, 0.25, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_yellow_0_625 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "yellow0_75"
  yellow0_75Clock = new util.Clock();
  polygon_yellow_0_75 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_yellow_0_75', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.5, 0.5, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_yellow_0_75 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "yellow0_875"
  yellow0_875Clock = new util.Clock();
  polygon_yellow_0_875 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_yellow_0_875', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.75, 0.75, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_yellow_0_875 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "yellow1"
  yellow1Clock = new util.Clock();
  polygon_yellow_1 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_yellow_1', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([1.0, 1.0, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_yellow_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  
  // Initialize components for Routine "blue0_75"
  blue0_75Clock = new util.Clock();
  polygon_blue_0_75 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_blue_0_75', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 0.0), 0.5]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_blue_0_75 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blue0_875"
  blue0_875Clock = new util.Clock();
  polygon_blue_0_875 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_blue_0_875', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), 0.1667, 0.75]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_blue_0_875 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blue1"
  blue1Clock = new util.Clock();
  polygon_blue_1 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_blue_1', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), 0.3333, 1.0]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_blue_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  
  // Initialize components for Routine "green0_75"
  green0_75Clock = new util.Clock();
  polygon_green_0_75 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_green_0_75', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 0.5), 0.5, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_green_0_75 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "green0_875"
  green0_875Clock = new util.Clock();
  polygon_green_0_875 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_green_0_875', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 0.4167), 0.75, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_green_0_875 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "green1"
  green1Clock = new util.Clock();
  polygon_green_1 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_green_1', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 0.3333), 1.0, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_green_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  
  // Initialize components for Routine "purple0_75"
  purple0_75Clock = new util.Clock();
  polygon_purple_0_75 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_purple_0_75', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.5, (- 1.0), 0.5]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_purple_0_75 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "purple0_875"
  purple0_875Clock = new util.Clock();
  polygon_purple_0_875 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_purple_0_875', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.75, (- 1.0), 0.75]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_purple_0_875 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "purple1"
  purple1Clock = new util.Clock();
  polygon_purple_1 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_purple_1', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([1.0, (- 1.0), 1.0]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_purple_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "orange0_5"
  orange0_5Clock = new util.Clock();
  polygon_orange_0_5 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_orange_0_5', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, (- 0.4167), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_orange_0_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "orange0_625"
  orange0_625Clock = new util.Clock();
  polygon_orange_0_625 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_orange_0_625', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.25, (- 0.2708), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_orange_0_625 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "orange0_75"
  orange0_75Clock = new util.Clock();
  polygon_orange_0_75 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_orange_0_75', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.5, (- 0.125), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_orange_0_75 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "orange0_875"
  orange0_875Clock = new util.Clock();
  polygon_res_0_875 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_res_0_875', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.75, 0.0208, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_orange_0_875 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "orange1"
  orange1Clock = new util.Clock();
  polygon_orange_1 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_orange_1', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([1.0, 0.1667, (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  res_orange_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audiointro"
  audiointroClock = new util.Clock();
  audiotext = new visual.TextStim({
    win: psychoJS.window,
    name: 'audiotext',
    text: 'You have now finished all visual stimuli \n\nThe next part is made of a series of sound stimuli with different frequencies. As you did for the visual stimuli, press the space bar when you hear the sound. \n\nThe first stimulus is your test run for you to familiarise with the test\n\nPress space bar when you have finished reading\n\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  audiointro_res = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audiotest"
  audiotestClock = new util.Clock();
  sound_testrun = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/2500.wav',
      secs: (- 1),
      });
  sound_testrun.setVolume(1.0);
  res_audio_testrun = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audiotestpassed"
  audiotestpassedClock = new util.Clock();
  autest_passed = new visual.TextStim({
    win: psychoJS.window,
    name: 'autest_passed',
    text: 'You have done the testrun\n\n\n\nPress the space bar when you have finished reading',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  res_testpassed = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audio_500Hz_0_25"
  audio_500Hz_0_25Clock = new util.Clock();
  sound_500Hz_0_25 = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/500.wav',
      secs: (- 1),
      });
  sound_500Hz_0_25.setVolume(0.25);
  res_500Hz_0_25 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audio_500Hz"
  audio_500HzClock = new util.Clock();
  sound_500Hz = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/500.wav',
      secs: (- 1),
      });
  sound_500Hz.setVolume(1.0);
  res_500Hz = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audio_2500Hz"
  audio_2500HzClock = new util.Clock();
  sound_2500Hz = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/2500.wav',
      secs: (- 1),
      });
  sound_2500Hz.setVolume(1.0);
  res_2500Hz = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audio_5000Hz"
  audio_5000HzClock = new util.Clock();
  sound_5000Hz = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/5000.wav',
      secs: (- 1),
      });
  sound_5000Hz.setVolume(1.0);
  res_5000Hz = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audio_7500Hz"
  audio_7500HzClock = new util.Clock();
  sound_7500Hz = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/7500.wav',
      secs: (- 1),
      });
  sound_7500Hz.setVolume(1.0);
  res_7500Hz = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audio_10000Hz"
  audio_10000HzClock = new util.Clock();
  sound_10000Hz = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/10000.wav',
      secs: (- 1),
      });
  sound_10000Hz.setVolume(1.0);
  res_10000Hz = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audio_12500Hz"
  audio_12500HzClock = new util.Clock();
  sound_12500 = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/12500.wav',
      secs: (- 1),
      });
  sound_12500.setVolume(1.0);
  res_12500 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "audio_15000Hz"
  audio_15000HzClock = new util.Clock();
  sound_15000 = new sound.Sound({
      win: psychoJS.window,
      value: 'audio files/15000.wav',
      secs: (- 1),
      });
  sound_15000.setVolume(1.0);
  res_15000Hz = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "outro"
  outroClock = new util.Clock();
  text_outro = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_outro',
    text: 'You have now finished the whole test\n\nThank you to your participation in the experiment\n\nPlease do not forget to apply hand sanitiser on the way out\n\nYou may press Esc to end the test',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _res_intro_allKeys;
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
    res_intro.keys = undefined;
    res_intro.rt = undefined;
    _res_intro_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(text);
    introComponents.push(res_intro);
    
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    
    // *res_intro* updates
    if (t >= 2.0 && res_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_intro.tStart = t;  // (not accounting for frame time here)
      res_intro.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_intro.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_intro.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_intro.clearEvents(); });
    }
    
    if (res_intro.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_intro.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_intro_allKeys = _res_intro_allKeys.concat(theseKeys);
      if (_res_intro_allKeys.length > 0) {
        res_intro.keys = _res_intro_allKeys[_res_intro_allKeys.length - 1].name;  // just the last key pressed
        res_intro.rt = _res_intro_allKeys[_res_intro_allKeys.length - 1].rt;
        res_intro.duration = _res_intro_allKeys[_res_intro_allKeys.length - 1].duration;
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
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('intro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_intro.corr, level);
    }
    psychoJS.experiment.addData('res_intro.keys', res_intro.keys);
    if (typeof res_intro.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_intro.rt', res_intro.rt);
        psychoJS.experiment.addData('res_intro.duration', res_intro.duration);
        routineTimer.reset();
        }
    
    res_intro.stop();
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
    howitworksComponents.push(text_howitworks);
    howitworksComponents.push(endhowitworks);
    
    howitworksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *text_howitworks* updates
    if (t >= 0.0 && text_howitworks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_howitworks.tStart = t;  // (not accounting for frame time here)
      text_howitworks.frameNStart = frameN;  // exact frame index
      
      text_howitworks.setAutoDraw(true);
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
    howitworksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    howitworksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    testComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    testComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    testComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    test_passedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    test_passedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    test_passedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    red0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    red0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    red0_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    red0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    red0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    red0_625Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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


var _res_red_0_75_allKeys;
var red0_75Components;
function red0_75RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'red0_75' ---
    t = 0;
    red0_75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('red0_75.started', globalClock.getTime());
    res_red_0_75.keys = undefined;
    res_red_0_75.rt = undefined;
    _res_red_0_75_allKeys = [];
    // keep track of which components have finished
    red0_75Components = [];
    red0_75Components.push(polygon_red_0_75);
    red0_75Components.push(res_red_0_75);
    
    red0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function red0_75RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'red0_75' ---
    // get current time
    t = red0_75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_red_0_75* updates
    if (t >= 2 && polygon_red_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_red_0_75.tStart = t;  // (not accounting for frame time here)
      polygon_red_0_75.frameNStart = frameN;  // exact frame index
      
      polygon_red_0_75.setAutoDraw(true);
    }
    
    
    // *res_red_0_75* updates
    if (t >= 2 && res_red_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_red_0_75.tStart = t;  // (not accounting for frame time here)
      res_red_0_75.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_red_0_75.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_red_0_75.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_red_0_75.clearEvents(); });
    }
    
    if (res_red_0_75.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_red_0_75.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_red_0_75_allKeys = _res_red_0_75_allKeys.concat(theseKeys);
      if (_res_red_0_75_allKeys.length > 0) {
        res_red_0_75.keys = _res_red_0_75_allKeys[_res_red_0_75_allKeys.length - 1].name;  // just the last key pressed
        res_red_0_75.rt = _res_red_0_75_allKeys[_res_red_0_75_allKeys.length - 1].rt;
        res_red_0_75.duration = _res_red_0_75_allKeys[_res_red_0_75_allKeys.length - 1].duration;
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
    red0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function red0_75RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'red0_75' ---
    red0_75Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('red0_75.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_red_0_75.corr, level);
    }
    psychoJS.experiment.addData('res_red_0_75.keys', res_red_0_75.keys);
    if (typeof res_red_0_75.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_red_0_75.rt', res_red_0_75.rt);
        psychoJS.experiment.addData('res_red_0_75.duration', res_red_0_75.duration);
        routineTimer.reset();
        }
    
    res_red_0_75.stop();
    // the Routine "red0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_red_0_875_allKeys;
var red0_875Components;
function red0_875RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'red0_875' ---
    t = 0;
    red0_875Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('red0_875.started', globalClock.getTime());
    res_red_0_875.keys = undefined;
    res_red_0_875.rt = undefined;
    _res_red_0_875_allKeys = [];
    // keep track of which components have finished
    red0_875Components = [];
    red0_875Components.push(polygon_red_0_875);
    red0_875Components.push(res_red_0_875);
    
    red0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function red0_875RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'red0_875' ---
    // get current time
    t = red0_875Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_red_0_875* updates
    if (t >= 2 && polygon_red_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_red_0_875.tStart = t;  // (not accounting for frame time here)
      polygon_red_0_875.frameNStart = frameN;  // exact frame index
      
      polygon_red_0_875.setAutoDraw(true);
    }
    
    
    // *res_red_0_875* updates
    if (t >= 2 && res_red_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_red_0_875.tStart = t;  // (not accounting for frame time here)
      res_red_0_875.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_red_0_875.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_red_0_875.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_red_0_875.clearEvents(); });
    }
    
    if (res_red_0_875.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_red_0_875.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_red_0_875_allKeys = _res_red_0_875_allKeys.concat(theseKeys);
      if (_res_red_0_875_allKeys.length > 0) {
        res_red_0_875.keys = _res_red_0_875_allKeys[_res_red_0_875_allKeys.length - 1].name;  // just the last key pressed
        res_red_0_875.rt = _res_red_0_875_allKeys[_res_red_0_875_allKeys.length - 1].rt;
        res_red_0_875.duration = _res_red_0_875_allKeys[_res_red_0_875_allKeys.length - 1].duration;
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
    red0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function red0_875RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'red0_875' ---
    red0_875Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('red0_875.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_red_0_875.corr, level);
    }
    psychoJS.experiment.addData('res_red_0_875.keys', res_red_0_875.keys);
    if (typeof res_red_0_875.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_red_0_875.rt', res_red_0_875.rt);
        psychoJS.experiment.addData('res_red_0_875.duration', res_red_0_875.duration);
        routineTimer.reset();
        }
    
    res_red_0_875.stop();
    // the Routine "red0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_red_1_allKeys;
var red1Components;
function red1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'red1' ---
    t = 0;
    red1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('red1.started', globalClock.getTime());
    res_red_1.keys = undefined;
    res_red_1.rt = undefined;
    _res_red_1_allKeys = [];
    // keep track of which components have finished
    red1Components = [];
    red1Components.push(polygon_red_1);
    red1Components.push(res_red_1);
    
    red1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function red1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'red1' ---
    // get current time
    t = red1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_red_1* updates
    if (t >= 2 && polygon_red_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_red_1.tStart = t;  // (not accounting for frame time here)
      polygon_red_1.frameNStart = frameN;  // exact frame index
      
      polygon_red_1.setAutoDraw(true);
    }
    
    
    // *res_red_1* updates
    if (t >= 2 && res_red_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_red_1.tStart = t;  // (not accounting for frame time here)
      res_red_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_red_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_red_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_red_1.clearEvents(); });
    }
    
    if (res_red_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_red_1.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_red_1_allKeys = _res_red_1_allKeys.concat(theseKeys);
      if (_res_red_1_allKeys.length > 0) {
        res_red_1.keys = _res_red_1_allKeys[_res_red_1_allKeys.length - 1].name;  // just the last key pressed
        res_red_1.rt = _res_red_1_allKeys[_res_red_1_allKeys.length - 1].rt;
        res_red_1.duration = _res_red_1_allKeys[_res_red_1_allKeys.length - 1].duration;
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
    red1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function red1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'red1' ---
    red1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('red1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_red_1.corr, level);
    }
    psychoJS.experiment.addData('res_red_1.keys', res_red_1.keys);
    if (typeof res_red_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_red_1.rt', res_red_1.rt);
        psychoJS.experiment.addData('res_red_1.duration', res_red_1.duration);
        routineTimer.reset();
        }
    
    res_red_1.stop();
    // the Routine "red1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_yellow_0_5_allKeys;
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
    res_yellow_0_5.keys = undefined;
    res_yellow_0_5.rt = undefined;
    _res_yellow_0_5_allKeys = [];
    // keep track of which components have finished
    yellow0_5Components = [];
    yellow0_5Components.push(polygon_0_5);
    yellow0_5Components.push(res_yellow_0_5);
    
    yellow0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *polygon_0_5* updates
    if (t >= 2 && polygon_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_0_5.tStart = t;  // (not accounting for frame time here)
      polygon_0_5.frameNStart = frameN;  // exact frame index
      
      polygon_0_5.setAutoDraw(true);
    }
    
    
    // *res_yellow_0_5* updates
    if (t >= 2 && res_yellow_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_yellow_0_5.tStart = t;  // (not accounting for frame time here)
      res_yellow_0_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_yellow_0_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_0_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_0_5.clearEvents(); });
    }
    
    if (res_yellow_0_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_yellow_0_5.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_yellow_0_5_allKeys = _res_yellow_0_5_allKeys.concat(theseKeys);
      if (_res_yellow_0_5_allKeys.length > 0) {
        res_yellow_0_5.keys = _res_yellow_0_5_allKeys[_res_yellow_0_5_allKeys.length - 1].name;  // just the last key pressed
        res_yellow_0_5.rt = _res_yellow_0_5_allKeys[_res_yellow_0_5_allKeys.length - 1].rt;
        res_yellow_0_5.duration = _res_yellow_0_5_allKeys[_res_yellow_0_5_allKeys.length - 1].duration;
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
    yellow0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    yellow0_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('yellow0_5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_yellow_0_5.corr, level);
    }
    psychoJS.experiment.addData('res_yellow_0_5.keys', res_yellow_0_5.keys);
    if (typeof res_yellow_0_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_yellow_0_5.rt', res_yellow_0_5.rt);
        psychoJS.experiment.addData('res_yellow_0_5.duration', res_yellow_0_5.duration);
        routineTimer.reset();
        }
    
    res_yellow_0_5.stop();
    // the Routine "yellow0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_yellow_0_625_allKeys;
var yellow0_625Components;
function yellow0_625RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'yellow0_625' ---
    t = 0;
    yellow0_625Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('yellow0_625.started', globalClock.getTime());
    res_yellow_0_625.keys = undefined;
    res_yellow_0_625.rt = undefined;
    _res_yellow_0_625_allKeys = [];
    // keep track of which components have finished
    yellow0_625Components = [];
    yellow0_625Components.push(polygon_yellow_0_625);
    yellow0_625Components.push(res_yellow_0_625);
    
    yellow0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function yellow0_625RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'yellow0_625' ---
    // get current time
    t = yellow0_625Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_yellow_0_625* updates
    if (t >= 2 && polygon_yellow_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_yellow_0_625.tStart = t;  // (not accounting for frame time here)
      polygon_yellow_0_625.frameNStart = frameN;  // exact frame index
      
      polygon_yellow_0_625.setAutoDraw(true);
    }
    
    
    // *res_yellow_0_625* updates
    if (t >= 2 && res_yellow_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_yellow_0_625.tStart = t;  // (not accounting for frame time here)
      res_yellow_0_625.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_yellow_0_625.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_0_625.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_0_625.clearEvents(); });
    }
    
    if (res_yellow_0_625.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_yellow_0_625.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_yellow_0_625_allKeys = _res_yellow_0_625_allKeys.concat(theseKeys);
      if (_res_yellow_0_625_allKeys.length > 0) {
        res_yellow_0_625.keys = _res_yellow_0_625_allKeys[_res_yellow_0_625_allKeys.length - 1].name;  // just the last key pressed
        res_yellow_0_625.rt = _res_yellow_0_625_allKeys[_res_yellow_0_625_allKeys.length - 1].rt;
        res_yellow_0_625.duration = _res_yellow_0_625_allKeys[_res_yellow_0_625_allKeys.length - 1].duration;
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
    yellow0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function yellow0_625RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'yellow0_625' ---
    yellow0_625Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('yellow0_625.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_yellow_0_625.corr, level);
    }
    psychoJS.experiment.addData('res_yellow_0_625.keys', res_yellow_0_625.keys);
    if (typeof res_yellow_0_625.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_yellow_0_625.rt', res_yellow_0_625.rt);
        psychoJS.experiment.addData('res_yellow_0_625.duration', res_yellow_0_625.duration);
        routineTimer.reset();
        }
    
    res_yellow_0_625.stop();
    // the Routine "yellow0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_yellow_0_75_allKeys;
var yellow0_75Components;
function yellow0_75RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'yellow0_75' ---
    t = 0;
    yellow0_75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('yellow0_75.started', globalClock.getTime());
    res_yellow_0_75.keys = undefined;
    res_yellow_0_75.rt = undefined;
    _res_yellow_0_75_allKeys = [];
    // keep track of which components have finished
    yellow0_75Components = [];
    yellow0_75Components.push(polygon_yellow_0_75);
    yellow0_75Components.push(res_yellow_0_75);
    
    yellow0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function yellow0_75RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'yellow0_75' ---
    // get current time
    t = yellow0_75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_yellow_0_75* updates
    if (t >= 2 && polygon_yellow_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_yellow_0_75.tStart = t;  // (not accounting for frame time here)
      polygon_yellow_0_75.frameNStart = frameN;  // exact frame index
      
      polygon_yellow_0_75.setAutoDraw(true);
    }
    
    
    // *res_yellow_0_75* updates
    if (t >= 2 && res_yellow_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_yellow_0_75.tStart = t;  // (not accounting for frame time here)
      res_yellow_0_75.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_yellow_0_75.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_0_75.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_0_75.clearEvents(); });
    }
    
    if (res_yellow_0_75.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_yellow_0_75.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_yellow_0_75_allKeys = _res_yellow_0_75_allKeys.concat(theseKeys);
      if (_res_yellow_0_75_allKeys.length > 0) {
        res_yellow_0_75.keys = _res_yellow_0_75_allKeys[_res_yellow_0_75_allKeys.length - 1].name;  // just the last key pressed
        res_yellow_0_75.rt = _res_yellow_0_75_allKeys[_res_yellow_0_75_allKeys.length - 1].rt;
        res_yellow_0_75.duration = _res_yellow_0_75_allKeys[_res_yellow_0_75_allKeys.length - 1].duration;
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
    yellow0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function yellow0_75RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'yellow0_75' ---
    yellow0_75Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('yellow0_75.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_yellow_0_75.corr, level);
    }
    psychoJS.experiment.addData('res_yellow_0_75.keys', res_yellow_0_75.keys);
    if (typeof res_yellow_0_75.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_yellow_0_75.rt', res_yellow_0_75.rt);
        psychoJS.experiment.addData('res_yellow_0_75.duration', res_yellow_0_75.duration);
        routineTimer.reset();
        }
    
    res_yellow_0_75.stop();
    // the Routine "yellow0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_yellow_0_875_allKeys;
var yellow0_875Components;
function yellow0_875RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'yellow0_875' ---
    t = 0;
    yellow0_875Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('yellow0_875.started', globalClock.getTime());
    res_yellow_0_875.keys = undefined;
    res_yellow_0_875.rt = undefined;
    _res_yellow_0_875_allKeys = [];
    // keep track of which components have finished
    yellow0_875Components = [];
    yellow0_875Components.push(polygon_yellow_0_875);
    yellow0_875Components.push(res_yellow_0_875);
    
    yellow0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function yellow0_875RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'yellow0_875' ---
    // get current time
    t = yellow0_875Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_yellow_0_875* updates
    if (t >= 2 && polygon_yellow_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_yellow_0_875.tStart = t;  // (not accounting for frame time here)
      polygon_yellow_0_875.frameNStart = frameN;  // exact frame index
      
      polygon_yellow_0_875.setAutoDraw(true);
    }
    
    
    // *res_yellow_0_875* updates
    if (t >= 2 && res_yellow_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_yellow_0_875.tStart = t;  // (not accounting for frame time here)
      res_yellow_0_875.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_yellow_0_875.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_0_875.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_0_875.clearEvents(); });
    }
    
    if (res_yellow_0_875.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_yellow_0_875.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_yellow_0_875_allKeys = _res_yellow_0_875_allKeys.concat(theseKeys);
      if (_res_yellow_0_875_allKeys.length > 0) {
        res_yellow_0_875.keys = _res_yellow_0_875_allKeys[_res_yellow_0_875_allKeys.length - 1].name;  // just the last key pressed
        res_yellow_0_875.rt = _res_yellow_0_875_allKeys[_res_yellow_0_875_allKeys.length - 1].rt;
        res_yellow_0_875.duration = _res_yellow_0_875_allKeys[_res_yellow_0_875_allKeys.length - 1].duration;
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
    yellow0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function yellow0_875RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'yellow0_875' ---
    yellow0_875Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('yellow0_875.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_yellow_0_875.corr, level);
    }
    psychoJS.experiment.addData('res_yellow_0_875.keys', res_yellow_0_875.keys);
    if (typeof res_yellow_0_875.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_yellow_0_875.rt', res_yellow_0_875.rt);
        psychoJS.experiment.addData('res_yellow_0_875.duration', res_yellow_0_875.duration);
        routineTimer.reset();
        }
    
    res_yellow_0_875.stop();
    // the Routine "yellow0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_yellow_1_allKeys;
var yellow1Components;
function yellow1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'yellow1' ---
    t = 0;
    yellow1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('yellow1.started', globalClock.getTime());
    res_yellow_1.keys = undefined;
    res_yellow_1.rt = undefined;
    _res_yellow_1_allKeys = [];
    // keep track of which components have finished
    yellow1Components = [];
    yellow1Components.push(polygon_yellow_1);
    yellow1Components.push(res_yellow_1);
    
    yellow1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function yellow1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'yellow1' ---
    // get current time
    t = yellow1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_yellow_1* updates
    if (t >= 2 && polygon_yellow_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_yellow_1.tStart = t;  // (not accounting for frame time here)
      polygon_yellow_1.frameNStart = frameN;  // exact frame index
      
      polygon_yellow_1.setAutoDraw(true);
    }
    
    
    // *res_yellow_1* updates
    if (t >= 2 && res_yellow_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_yellow_1.tStart = t;  // (not accounting for frame time here)
      res_yellow_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_yellow_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_yellow_1.clearEvents(); });
    }
    
    if (res_yellow_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_yellow_1.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_yellow_1_allKeys = _res_yellow_1_allKeys.concat(theseKeys);
      if (_res_yellow_1_allKeys.length > 0) {
        res_yellow_1.keys = _res_yellow_1_allKeys[_res_yellow_1_allKeys.length - 1].name;  // just the last key pressed
        res_yellow_1.rt = _res_yellow_1_allKeys[_res_yellow_1_allKeys.length - 1].rt;
        res_yellow_1.duration = _res_yellow_1_allKeys[_res_yellow_1_allKeys.length - 1].duration;
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
    yellow1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function yellow1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'yellow1' ---
    yellow1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('yellow1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_yellow_1.corr, level);
    }
    psychoJS.experiment.addData('res_yellow_1.keys', res_yellow_1.keys);
    if (typeof res_yellow_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_yellow_1.rt', res_yellow_1.rt);
        psychoJS.experiment.addData('res_yellow_1.duration', res_yellow_1.duration);
        routineTimer.reset();
        }
    
    res_yellow_1.stop();
    // the Routine "yellow1" was not non-slip safe, so reset the non-slip timer
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
    
    blue0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    blue0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    blue0_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    blue0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    blue0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    blue0_625Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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


var _res_blue_0_75_allKeys;
var blue0_75Components;
function blue0_75RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blue0_75' ---
    t = 0;
    blue0_75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('blue0_75.started', globalClock.getTime());
    res_blue_0_75.keys = undefined;
    res_blue_0_75.rt = undefined;
    _res_blue_0_75_allKeys = [];
    // keep track of which components have finished
    blue0_75Components = [];
    blue0_75Components.push(polygon_blue_0_75);
    blue0_75Components.push(res_blue_0_75);
    
    blue0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function blue0_75RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blue0_75' ---
    // get current time
    t = blue0_75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_blue_0_75* updates
    if (t >= 2 && polygon_blue_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_blue_0_75.tStart = t;  // (not accounting for frame time here)
      polygon_blue_0_75.frameNStart = frameN;  // exact frame index
      
      polygon_blue_0_75.setAutoDraw(true);
    }
    
    
    // *res_blue_0_75* updates
    if (t >= 2 && res_blue_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_blue_0_75.tStart = t;  // (not accounting for frame time here)
      res_blue_0_75.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_blue_0_75.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_blue_0_75.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_blue_0_75.clearEvents(); });
    }
    
    if (res_blue_0_75.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_blue_0_75.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_blue_0_75_allKeys = _res_blue_0_75_allKeys.concat(theseKeys);
      if (_res_blue_0_75_allKeys.length > 0) {
        res_blue_0_75.keys = _res_blue_0_75_allKeys[_res_blue_0_75_allKeys.length - 1].name;  // just the last key pressed
        res_blue_0_75.rt = _res_blue_0_75_allKeys[_res_blue_0_75_allKeys.length - 1].rt;
        res_blue_0_75.duration = _res_blue_0_75_allKeys[_res_blue_0_75_allKeys.length - 1].duration;
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
    blue0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blue0_75RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blue0_75' ---
    blue0_75Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('blue0_75.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_blue_0_75.corr, level);
    }
    psychoJS.experiment.addData('res_blue_0_75.keys', res_blue_0_75.keys);
    if (typeof res_blue_0_75.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_blue_0_75.rt', res_blue_0_75.rt);
        psychoJS.experiment.addData('res_blue_0_75.duration', res_blue_0_75.duration);
        routineTimer.reset();
        }
    
    res_blue_0_75.stop();
    // the Routine "blue0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_blue_0_875_allKeys;
var blue0_875Components;
function blue0_875RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blue0_875' ---
    t = 0;
    blue0_875Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('blue0_875.started', globalClock.getTime());
    res_blue_0_875.keys = undefined;
    res_blue_0_875.rt = undefined;
    _res_blue_0_875_allKeys = [];
    // keep track of which components have finished
    blue0_875Components = [];
    blue0_875Components.push(polygon_blue_0_875);
    blue0_875Components.push(res_blue_0_875);
    
    blue0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function blue0_875RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blue0_875' ---
    // get current time
    t = blue0_875Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_blue_0_875* updates
    if (t >= 2 && polygon_blue_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_blue_0_875.tStart = t;  // (not accounting for frame time here)
      polygon_blue_0_875.frameNStart = frameN;  // exact frame index
      
      polygon_blue_0_875.setAutoDraw(true);
    }
    
    
    // *res_blue_0_875* updates
    if (t >= 2 && res_blue_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_blue_0_875.tStart = t;  // (not accounting for frame time here)
      res_blue_0_875.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_blue_0_875.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_blue_0_875.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_blue_0_875.clearEvents(); });
    }
    
    if (res_blue_0_875.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_blue_0_875.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_blue_0_875_allKeys = _res_blue_0_875_allKeys.concat(theseKeys);
      if (_res_blue_0_875_allKeys.length > 0) {
        res_blue_0_875.keys = _res_blue_0_875_allKeys[_res_blue_0_875_allKeys.length - 1].name;  // just the last key pressed
        res_blue_0_875.rt = _res_blue_0_875_allKeys[_res_blue_0_875_allKeys.length - 1].rt;
        res_blue_0_875.duration = _res_blue_0_875_allKeys[_res_blue_0_875_allKeys.length - 1].duration;
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
    blue0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blue0_875RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blue0_875' ---
    blue0_875Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('blue0_875.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_blue_0_875.corr, level);
    }
    psychoJS.experiment.addData('res_blue_0_875.keys', res_blue_0_875.keys);
    if (typeof res_blue_0_875.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_blue_0_875.rt', res_blue_0_875.rt);
        psychoJS.experiment.addData('res_blue_0_875.duration', res_blue_0_875.duration);
        routineTimer.reset();
        }
    
    res_blue_0_875.stop();
    // the Routine "blue0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_blue_1_allKeys;
var blue1Components;
function blue1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blue1' ---
    t = 0;
    blue1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('blue1.started', globalClock.getTime());
    res_blue_1.keys = undefined;
    res_blue_1.rt = undefined;
    _res_blue_1_allKeys = [];
    // keep track of which components have finished
    blue1Components = [];
    blue1Components.push(polygon_blue_1);
    blue1Components.push(res_blue_1);
    
    blue1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function blue1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blue1' ---
    // get current time
    t = blue1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_blue_1* updates
    if (t >= 2 && polygon_blue_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_blue_1.tStart = t;  // (not accounting for frame time here)
      polygon_blue_1.frameNStart = frameN;  // exact frame index
      
      polygon_blue_1.setAutoDraw(true);
    }
    
    
    // *res_blue_1* updates
    if (t >= 2 && res_blue_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_blue_1.tStart = t;  // (not accounting for frame time here)
      res_blue_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_blue_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_blue_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_blue_1.clearEvents(); });
    }
    
    if (res_blue_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_blue_1.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_blue_1_allKeys = _res_blue_1_allKeys.concat(theseKeys);
      if (_res_blue_1_allKeys.length > 0) {
        res_blue_1.keys = _res_blue_1_allKeys[_res_blue_1_allKeys.length - 1].name;  // just the last key pressed
        res_blue_1.rt = _res_blue_1_allKeys[_res_blue_1_allKeys.length - 1].rt;
        res_blue_1.duration = _res_blue_1_allKeys[_res_blue_1_allKeys.length - 1].duration;
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
    blue1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blue1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blue1' ---
    blue1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('blue1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_blue_1.corr, level);
    }
    psychoJS.experiment.addData('res_blue_1.keys', res_blue_1.keys);
    if (typeof res_blue_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_blue_1.rt', res_blue_1.rt);
        psychoJS.experiment.addData('res_blue_1.duration', res_blue_1.duration);
        routineTimer.reset();
        }
    
    res_blue_1.stop();
    // the Routine "blue1" was not non-slip safe, so reset the non-slip timer
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
    
    green0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    green0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    green0_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    green0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    green0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    green0_625Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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


var _res_green_0_75_allKeys;
var green0_75Components;
function green0_75RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'green0_75' ---
    t = 0;
    green0_75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('green0_75.started', globalClock.getTime());
    res_green_0_75.keys = undefined;
    res_green_0_75.rt = undefined;
    _res_green_0_75_allKeys = [];
    // keep track of which components have finished
    green0_75Components = [];
    green0_75Components.push(polygon_green_0_75);
    green0_75Components.push(res_green_0_75);
    
    green0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function green0_75RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'green0_75' ---
    // get current time
    t = green0_75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_green_0_75* updates
    if (t >= 2 && polygon_green_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_green_0_75.tStart = t;  // (not accounting for frame time here)
      polygon_green_0_75.frameNStart = frameN;  // exact frame index
      
      polygon_green_0_75.setAutoDraw(true);
    }
    
    
    // *res_green_0_75* updates
    if (t >= 2 && res_green_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_green_0_75.tStart = t;  // (not accounting for frame time here)
      res_green_0_75.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_green_0_75.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_green_0_75.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_green_0_75.clearEvents(); });
    }
    
    if (res_green_0_75.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_green_0_75.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_green_0_75_allKeys = _res_green_0_75_allKeys.concat(theseKeys);
      if (_res_green_0_75_allKeys.length > 0) {
        res_green_0_75.keys = _res_green_0_75_allKeys[_res_green_0_75_allKeys.length - 1].name;  // just the last key pressed
        res_green_0_75.rt = _res_green_0_75_allKeys[_res_green_0_75_allKeys.length - 1].rt;
        res_green_0_75.duration = _res_green_0_75_allKeys[_res_green_0_75_allKeys.length - 1].duration;
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
    green0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function green0_75RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'green0_75' ---
    green0_75Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('green0_75.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_green_0_75.corr, level);
    }
    psychoJS.experiment.addData('res_green_0_75.keys', res_green_0_75.keys);
    if (typeof res_green_0_75.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_green_0_75.rt', res_green_0_75.rt);
        psychoJS.experiment.addData('res_green_0_75.duration', res_green_0_75.duration);
        routineTimer.reset();
        }
    
    res_green_0_75.stop();
    // the Routine "green0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_green_0_875_allKeys;
var green0_875Components;
function green0_875RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'green0_875' ---
    t = 0;
    green0_875Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('green0_875.started', globalClock.getTime());
    res_green_0_875.keys = undefined;
    res_green_0_875.rt = undefined;
    _res_green_0_875_allKeys = [];
    // keep track of which components have finished
    green0_875Components = [];
    green0_875Components.push(polygon_green_0_875);
    green0_875Components.push(res_green_0_875);
    
    green0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function green0_875RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'green0_875' ---
    // get current time
    t = green0_875Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_green_0_875* updates
    if (t >= 2 && polygon_green_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_green_0_875.tStart = t;  // (not accounting for frame time here)
      polygon_green_0_875.frameNStart = frameN;  // exact frame index
      
      polygon_green_0_875.setAutoDraw(true);
    }
    
    
    // *res_green_0_875* updates
    if (t >= 2 && res_green_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_green_0_875.tStart = t;  // (not accounting for frame time here)
      res_green_0_875.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_green_0_875.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_green_0_875.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_green_0_875.clearEvents(); });
    }
    
    if (res_green_0_875.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_green_0_875.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_green_0_875_allKeys = _res_green_0_875_allKeys.concat(theseKeys);
      if (_res_green_0_875_allKeys.length > 0) {
        res_green_0_875.keys = _res_green_0_875_allKeys[_res_green_0_875_allKeys.length - 1].name;  // just the last key pressed
        res_green_0_875.rt = _res_green_0_875_allKeys[_res_green_0_875_allKeys.length - 1].rt;
        res_green_0_875.duration = _res_green_0_875_allKeys[_res_green_0_875_allKeys.length - 1].duration;
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
    green0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function green0_875RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'green0_875' ---
    green0_875Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('green0_875.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_green_0_875.corr, level);
    }
    psychoJS.experiment.addData('res_green_0_875.keys', res_green_0_875.keys);
    if (typeof res_green_0_875.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_green_0_875.rt', res_green_0_875.rt);
        psychoJS.experiment.addData('res_green_0_875.duration', res_green_0_875.duration);
        routineTimer.reset();
        }
    
    res_green_0_875.stop();
    // the Routine "green0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_green_1_allKeys;
var green1Components;
function green1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'green1' ---
    t = 0;
    green1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('green1.started', globalClock.getTime());
    res_green_1.keys = undefined;
    res_green_1.rt = undefined;
    _res_green_1_allKeys = [];
    // keep track of which components have finished
    green1Components = [];
    green1Components.push(polygon_green_1);
    green1Components.push(res_green_1);
    
    green1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function green1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'green1' ---
    // get current time
    t = green1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_green_1* updates
    if (t >= 2 && polygon_green_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_green_1.tStart = t;  // (not accounting for frame time here)
      polygon_green_1.frameNStart = frameN;  // exact frame index
      
      polygon_green_1.setAutoDraw(true);
    }
    
    
    // *res_green_1* updates
    if (t >= 2 && res_green_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_green_1.tStart = t;  // (not accounting for frame time here)
      res_green_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_green_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_green_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_green_1.clearEvents(); });
    }
    
    if (res_green_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_green_1.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_green_1_allKeys = _res_green_1_allKeys.concat(theseKeys);
      if (_res_green_1_allKeys.length > 0) {
        res_green_1.keys = _res_green_1_allKeys[_res_green_1_allKeys.length - 1].name;  // just the last key pressed
        res_green_1.rt = _res_green_1_allKeys[_res_green_1_allKeys.length - 1].rt;
        res_green_1.duration = _res_green_1_allKeys[_res_green_1_allKeys.length - 1].duration;
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
    green1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function green1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'green1' ---
    green1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('green1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_green_1.corr, level);
    }
    psychoJS.experiment.addData('res_green_1.keys', res_green_1.keys);
    if (typeof res_green_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_green_1.rt', res_green_1.rt);
        psychoJS.experiment.addData('res_green_1.duration', res_green_1.duration);
        routineTimer.reset();
        }
    
    res_green_1.stop();
    // the Routine "green1" was not non-slip safe, so reset the non-slip timer
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
    
    purple0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    purple0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    purple0_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    purple0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    purple0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    purple0_625Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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


var _res_purple_0_75_allKeys;
var purple0_75Components;
function purple0_75RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'purple0_75' ---
    t = 0;
    purple0_75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('purple0_75.started', globalClock.getTime());
    res_purple_0_75.keys = undefined;
    res_purple_0_75.rt = undefined;
    _res_purple_0_75_allKeys = [];
    // keep track of which components have finished
    purple0_75Components = [];
    purple0_75Components.push(polygon_purple_0_75);
    purple0_75Components.push(res_purple_0_75);
    
    purple0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function purple0_75RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'purple0_75' ---
    // get current time
    t = purple0_75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_purple_0_75* updates
    if (t >= 2 && polygon_purple_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_purple_0_75.tStart = t;  // (not accounting for frame time here)
      polygon_purple_0_75.frameNStart = frameN;  // exact frame index
      
      polygon_purple_0_75.setAutoDraw(true);
    }
    
    
    // *res_purple_0_75* updates
    if (t >= 2 && res_purple_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_purple_0_75.tStart = t;  // (not accounting for frame time here)
      res_purple_0_75.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_purple_0_75.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_purple_0_75.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_purple_0_75.clearEvents(); });
    }
    
    if (res_purple_0_75.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_purple_0_75.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_purple_0_75_allKeys = _res_purple_0_75_allKeys.concat(theseKeys);
      if (_res_purple_0_75_allKeys.length > 0) {
        res_purple_0_75.keys = _res_purple_0_75_allKeys[_res_purple_0_75_allKeys.length - 1].name;  // just the last key pressed
        res_purple_0_75.rt = _res_purple_0_75_allKeys[_res_purple_0_75_allKeys.length - 1].rt;
        res_purple_0_75.duration = _res_purple_0_75_allKeys[_res_purple_0_75_allKeys.length - 1].duration;
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
    purple0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function purple0_75RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'purple0_75' ---
    purple0_75Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('purple0_75.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_purple_0_75.corr, level);
    }
    psychoJS.experiment.addData('res_purple_0_75.keys', res_purple_0_75.keys);
    if (typeof res_purple_0_75.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_purple_0_75.rt', res_purple_0_75.rt);
        psychoJS.experiment.addData('res_purple_0_75.duration', res_purple_0_75.duration);
        routineTimer.reset();
        }
    
    res_purple_0_75.stop();
    // the Routine "purple0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_purple_0_875_allKeys;
var purple0_875Components;
function purple0_875RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'purple0_875' ---
    t = 0;
    purple0_875Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('purple0_875.started', globalClock.getTime());
    res_purple_0_875.keys = undefined;
    res_purple_0_875.rt = undefined;
    _res_purple_0_875_allKeys = [];
    // keep track of which components have finished
    purple0_875Components = [];
    purple0_875Components.push(polygon_purple_0_875);
    purple0_875Components.push(res_purple_0_875);
    
    purple0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function purple0_875RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'purple0_875' ---
    // get current time
    t = purple0_875Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_purple_0_875* updates
    if (t >= 2 && polygon_purple_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_purple_0_875.tStart = t;  // (not accounting for frame time here)
      polygon_purple_0_875.frameNStart = frameN;  // exact frame index
      
      polygon_purple_0_875.setAutoDraw(true);
    }
    
    
    // *res_purple_0_875* updates
    if (t >= 2 && res_purple_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_purple_0_875.tStart = t;  // (not accounting for frame time here)
      res_purple_0_875.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_purple_0_875.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_purple_0_875.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_purple_0_875.clearEvents(); });
    }
    
    if (res_purple_0_875.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_purple_0_875.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_purple_0_875_allKeys = _res_purple_0_875_allKeys.concat(theseKeys);
      if (_res_purple_0_875_allKeys.length > 0) {
        res_purple_0_875.keys = _res_purple_0_875_allKeys[_res_purple_0_875_allKeys.length - 1].name;  // just the last key pressed
        res_purple_0_875.rt = _res_purple_0_875_allKeys[_res_purple_0_875_allKeys.length - 1].rt;
        res_purple_0_875.duration = _res_purple_0_875_allKeys[_res_purple_0_875_allKeys.length - 1].duration;
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
    purple0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function purple0_875RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'purple0_875' ---
    purple0_875Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('purple0_875.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_purple_0_875.corr, level);
    }
    psychoJS.experiment.addData('res_purple_0_875.keys', res_purple_0_875.keys);
    if (typeof res_purple_0_875.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_purple_0_875.rt', res_purple_0_875.rt);
        psychoJS.experiment.addData('res_purple_0_875.duration', res_purple_0_875.duration);
        routineTimer.reset();
        }
    
    res_purple_0_875.stop();
    // the Routine "purple0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_purple_1_allKeys;
var purple1Components;
function purple1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'purple1' ---
    t = 0;
    purple1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('purple1.started', globalClock.getTime());
    res_purple_1.keys = undefined;
    res_purple_1.rt = undefined;
    _res_purple_1_allKeys = [];
    // keep track of which components have finished
    purple1Components = [];
    purple1Components.push(polygon_purple_1);
    purple1Components.push(res_purple_1);
    
    purple1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function purple1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'purple1' ---
    // get current time
    t = purple1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_purple_1* updates
    if (t >= 2 && polygon_purple_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_purple_1.tStart = t;  // (not accounting for frame time here)
      polygon_purple_1.frameNStart = frameN;  // exact frame index
      
      polygon_purple_1.setAutoDraw(true);
    }
    
    
    // *res_purple_1* updates
    if (t >= 2 && res_purple_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_purple_1.tStart = t;  // (not accounting for frame time here)
      res_purple_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_purple_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_purple_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_purple_1.clearEvents(); });
    }
    
    if (res_purple_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_purple_1.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_purple_1_allKeys = _res_purple_1_allKeys.concat(theseKeys);
      if (_res_purple_1_allKeys.length > 0) {
        res_purple_1.keys = _res_purple_1_allKeys[_res_purple_1_allKeys.length - 1].name;  // just the last key pressed
        res_purple_1.rt = _res_purple_1_allKeys[_res_purple_1_allKeys.length - 1].rt;
        res_purple_1.duration = _res_purple_1_allKeys[_res_purple_1_allKeys.length - 1].duration;
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
    purple1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function purple1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'purple1' ---
    purple1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('purple1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_purple_1.corr, level);
    }
    psychoJS.experiment.addData('res_purple_1.keys', res_purple_1.keys);
    if (typeof res_purple_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_purple_1.rt', res_purple_1.rt);
        psychoJS.experiment.addData('res_purple_1.duration', res_purple_1.duration);
        routineTimer.reset();
        }
    
    res_purple_1.stop();
    // the Routine "purple1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_orange_0_5_allKeys;
var orange0_5Components;
function orange0_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'orange0_5' ---
    t = 0;
    orange0_5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('orange0_5.started', globalClock.getTime());
    res_orange_0_5.keys = undefined;
    res_orange_0_5.rt = undefined;
    _res_orange_0_5_allKeys = [];
    // keep track of which components have finished
    orange0_5Components = [];
    orange0_5Components.push(polygon_orange_0_5);
    orange0_5Components.push(res_orange_0_5);
    
    orange0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function orange0_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'orange0_5' ---
    // get current time
    t = orange0_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_orange_0_5* updates
    if (t >= 2 && polygon_orange_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_orange_0_5.tStart = t;  // (not accounting for frame time here)
      polygon_orange_0_5.frameNStart = frameN;  // exact frame index
      
      polygon_orange_0_5.setAutoDraw(true);
    }
    
    
    // *res_orange_0_5* updates
    if (t >= 2 && res_orange_0_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_orange_0_5.tStart = t;  // (not accounting for frame time here)
      res_orange_0_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_orange_0_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_orange_0_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_orange_0_5.clearEvents(); });
    }
    
    if (res_orange_0_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_orange_0_5.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_orange_0_5_allKeys = _res_orange_0_5_allKeys.concat(theseKeys);
      if (_res_orange_0_5_allKeys.length > 0) {
        res_orange_0_5.keys = _res_orange_0_5_allKeys[_res_orange_0_5_allKeys.length - 1].name;  // just the last key pressed
        res_orange_0_5.rt = _res_orange_0_5_allKeys[_res_orange_0_5_allKeys.length - 1].rt;
        res_orange_0_5.duration = _res_orange_0_5_allKeys[_res_orange_0_5_allKeys.length - 1].duration;
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
    orange0_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function orange0_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'orange0_5' ---
    orange0_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('orange0_5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_orange_0_5.corr, level);
    }
    psychoJS.experiment.addData('res_orange_0_5.keys', res_orange_0_5.keys);
    if (typeof res_orange_0_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_orange_0_5.rt', res_orange_0_5.rt);
        psychoJS.experiment.addData('res_orange_0_5.duration', res_orange_0_5.duration);
        routineTimer.reset();
        }
    
    res_orange_0_5.stop();
    // the Routine "orange0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_orange_0_625_allKeys;
var orange0_625Components;
function orange0_625RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'orange0_625' ---
    t = 0;
    orange0_625Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('orange0_625.started', globalClock.getTime());
    res_orange_0_625.keys = undefined;
    res_orange_0_625.rt = undefined;
    _res_orange_0_625_allKeys = [];
    // keep track of which components have finished
    orange0_625Components = [];
    orange0_625Components.push(polygon_orange_0_625);
    orange0_625Components.push(res_orange_0_625);
    
    orange0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function orange0_625RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'orange0_625' ---
    // get current time
    t = orange0_625Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_orange_0_625* updates
    if (t >= 2 && polygon_orange_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_orange_0_625.tStart = t;  // (not accounting for frame time here)
      polygon_orange_0_625.frameNStart = frameN;  // exact frame index
      
      polygon_orange_0_625.setAutoDraw(true);
    }
    
    
    // *res_orange_0_625* updates
    if (t >= 2 && res_orange_0_625.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_orange_0_625.tStart = t;  // (not accounting for frame time here)
      res_orange_0_625.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_orange_0_625.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_orange_0_625.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_orange_0_625.clearEvents(); });
    }
    
    if (res_orange_0_625.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_orange_0_625.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_orange_0_625_allKeys = _res_orange_0_625_allKeys.concat(theseKeys);
      if (_res_orange_0_625_allKeys.length > 0) {
        res_orange_0_625.keys = _res_orange_0_625_allKeys[_res_orange_0_625_allKeys.length - 1].name;  // just the last key pressed
        res_orange_0_625.rt = _res_orange_0_625_allKeys[_res_orange_0_625_allKeys.length - 1].rt;
        res_orange_0_625.duration = _res_orange_0_625_allKeys[_res_orange_0_625_allKeys.length - 1].duration;
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
    orange0_625Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function orange0_625RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'orange0_625' ---
    orange0_625Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('orange0_625.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_orange_0_625.corr, level);
    }
    psychoJS.experiment.addData('res_orange_0_625.keys', res_orange_0_625.keys);
    if (typeof res_orange_0_625.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_orange_0_625.rt', res_orange_0_625.rt);
        psychoJS.experiment.addData('res_orange_0_625.duration', res_orange_0_625.duration);
        routineTimer.reset();
        }
    
    res_orange_0_625.stop();
    // the Routine "orange0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_orange_0_75_allKeys;
var orange0_75Components;
function orange0_75RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'orange0_75' ---
    t = 0;
    orange0_75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('orange0_75.started', globalClock.getTime());
    res_orange_0_75.keys = undefined;
    res_orange_0_75.rt = undefined;
    _res_orange_0_75_allKeys = [];
    // keep track of which components have finished
    orange0_75Components = [];
    orange0_75Components.push(polygon_orange_0_75);
    orange0_75Components.push(res_orange_0_75);
    
    orange0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function orange0_75RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'orange0_75' ---
    // get current time
    t = orange0_75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_orange_0_75* updates
    if (t >= 2 && polygon_orange_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_orange_0_75.tStart = t;  // (not accounting for frame time here)
      polygon_orange_0_75.frameNStart = frameN;  // exact frame index
      
      polygon_orange_0_75.setAutoDraw(true);
    }
    
    
    // *res_orange_0_75* updates
    if (t >= 2 && res_orange_0_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_orange_0_75.tStart = t;  // (not accounting for frame time here)
      res_orange_0_75.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_orange_0_75.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_orange_0_75.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_orange_0_75.clearEvents(); });
    }
    
    if (res_orange_0_75.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_orange_0_75.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_orange_0_75_allKeys = _res_orange_0_75_allKeys.concat(theseKeys);
      if (_res_orange_0_75_allKeys.length > 0) {
        res_orange_0_75.keys = _res_orange_0_75_allKeys[_res_orange_0_75_allKeys.length - 1].name;  // just the last key pressed
        res_orange_0_75.rt = _res_orange_0_75_allKeys[_res_orange_0_75_allKeys.length - 1].rt;
        res_orange_0_75.duration = _res_orange_0_75_allKeys[_res_orange_0_75_allKeys.length - 1].duration;
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
    orange0_75Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function orange0_75RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'orange0_75' ---
    orange0_75Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('orange0_75.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_orange_0_75.corr, level);
    }
    psychoJS.experiment.addData('res_orange_0_75.keys', res_orange_0_75.keys);
    if (typeof res_orange_0_75.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_orange_0_75.rt', res_orange_0_75.rt);
        psychoJS.experiment.addData('res_orange_0_75.duration', res_orange_0_75.duration);
        routineTimer.reset();
        }
    
    res_orange_0_75.stop();
    // the Routine "orange0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_orange_0_875_allKeys;
var orange0_875Components;
function orange0_875RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'orange0_875' ---
    t = 0;
    orange0_875Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('orange0_875.started', globalClock.getTime());
    res_orange_0_875.keys = undefined;
    res_orange_0_875.rt = undefined;
    _res_orange_0_875_allKeys = [];
    // keep track of which components have finished
    orange0_875Components = [];
    orange0_875Components.push(polygon_res_0_875);
    orange0_875Components.push(res_orange_0_875);
    
    orange0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function orange0_875RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'orange0_875' ---
    // get current time
    t = orange0_875Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_res_0_875* updates
    if (t >= 2 && polygon_res_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_res_0_875.tStart = t;  // (not accounting for frame time here)
      polygon_res_0_875.frameNStart = frameN;  // exact frame index
      
      polygon_res_0_875.setAutoDraw(true);
    }
    
    
    // *res_orange_0_875* updates
    if (t >= 2 && res_orange_0_875.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_orange_0_875.tStart = t;  // (not accounting for frame time here)
      res_orange_0_875.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_orange_0_875.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_orange_0_875.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_orange_0_875.clearEvents(); });
    }
    
    if (res_orange_0_875.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_orange_0_875.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_orange_0_875_allKeys = _res_orange_0_875_allKeys.concat(theseKeys);
      if (_res_orange_0_875_allKeys.length > 0) {
        res_orange_0_875.keys = _res_orange_0_875_allKeys[_res_orange_0_875_allKeys.length - 1].name;  // just the last key pressed
        res_orange_0_875.rt = _res_orange_0_875_allKeys[_res_orange_0_875_allKeys.length - 1].rt;
        res_orange_0_875.duration = _res_orange_0_875_allKeys[_res_orange_0_875_allKeys.length - 1].duration;
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
    orange0_875Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function orange0_875RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'orange0_875' ---
    orange0_875Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('orange0_875.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_orange_0_875.corr, level);
    }
    psychoJS.experiment.addData('res_orange_0_875.keys', res_orange_0_875.keys);
    if (typeof res_orange_0_875.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_orange_0_875.rt', res_orange_0_875.rt);
        psychoJS.experiment.addData('res_orange_0_875.duration', res_orange_0_875.duration);
        routineTimer.reset();
        }
    
    res_orange_0_875.stop();
    // the Routine "orange0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_orange_1_allKeys;
var orange1Components;
function orange1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'orange1' ---
    t = 0;
    orange1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('orange1.started', globalClock.getTime());
    res_orange_1.keys = undefined;
    res_orange_1.rt = undefined;
    _res_orange_1_allKeys = [];
    // keep track of which components have finished
    orange1Components = [];
    orange1Components.push(polygon_orange_1);
    orange1Components.push(res_orange_1);
    
    orange1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function orange1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'orange1' ---
    // get current time
    t = orange1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_orange_1* updates
    if (t >= 2 && polygon_orange_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_orange_1.tStart = t;  // (not accounting for frame time here)
      polygon_orange_1.frameNStart = frameN;  // exact frame index
      
      polygon_orange_1.setAutoDraw(true);
    }
    
    
    // *res_orange_1* updates
    if (t >= 2 && res_orange_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_orange_1.tStart = t;  // (not accounting for frame time here)
      res_orange_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_orange_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_orange_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_orange_1.clearEvents(); });
    }
    
    if (res_orange_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_orange_1.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_orange_1_allKeys = _res_orange_1_allKeys.concat(theseKeys);
      if (_res_orange_1_allKeys.length > 0) {
        res_orange_1.keys = _res_orange_1_allKeys[_res_orange_1_allKeys.length - 1].name;  // just the last key pressed
        res_orange_1.rt = _res_orange_1_allKeys[_res_orange_1_allKeys.length - 1].rt;
        res_orange_1.duration = _res_orange_1_allKeys[_res_orange_1_allKeys.length - 1].duration;
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
    orange1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function orange1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'orange1' ---
    orange1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('orange1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_orange_1.corr, level);
    }
    psychoJS.experiment.addData('res_orange_1.keys', res_orange_1.keys);
    if (typeof res_orange_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_orange_1.rt', res_orange_1.rt);
        psychoJS.experiment.addData('res_orange_1.duration', res_orange_1.duration);
        routineTimer.reset();
        }
    
    res_orange_1.stop();
    // the Routine "orange1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _audiointro_res_allKeys;
var audiointroComponents;
function audiointroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audiointro' ---
    t = 0;
    audiointroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audiointro.started', globalClock.getTime());
    audiointro_res.keys = undefined;
    audiointro_res.rt = undefined;
    _audiointro_res_allKeys = [];
    // keep track of which components have finished
    audiointroComponents = [];
    audiointroComponents.push(audiotext);
    audiointroComponents.push(audiointro_res);
    
    audiointroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audiointroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audiointro' ---
    // get current time
    t = audiointroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *audiotext* updates
    if (t >= 0.0 && audiotext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      audiotext.tStart = t;  // (not accounting for frame time here)
      audiotext.frameNStart = frameN;  // exact frame index
      
      audiotext.setAutoDraw(true);
    }
    
    
    // *audiointro_res* updates
    if (t >= 2 && audiointro_res.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      audiointro_res.tStart = t;  // (not accounting for frame time here)
      audiointro_res.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { audiointro_res.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { audiointro_res.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { audiointro_res.clearEvents(); });
    }
    
    if (audiointro_res.status === PsychoJS.Status.STARTED) {
      let theseKeys = audiointro_res.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _audiointro_res_allKeys = _audiointro_res_allKeys.concat(theseKeys);
      if (_audiointro_res_allKeys.length > 0) {
        audiointro_res.keys = _audiointro_res_allKeys[_audiointro_res_allKeys.length - 1].name;  // just the last key pressed
        audiointro_res.rt = _audiointro_res_allKeys[_audiointro_res_allKeys.length - 1].rt;
        audiointro_res.duration = _audiointro_res_allKeys[_audiointro_res_allKeys.length - 1].duration;
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
    audiointroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audiointroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audiointro' ---
    audiointroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audiointro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(audiointro_res.corr, level);
    }
    psychoJS.experiment.addData('audiointro_res.keys', audiointro_res.keys);
    if (typeof audiointro_res.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('audiointro_res.rt', audiointro_res.rt);
        psychoJS.experiment.addData('audiointro_res.duration', audiointro_res.duration);
        routineTimer.reset();
        }
    
    audiointro_res.stop();
    // the Routine "audiointro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_audio_testrun_allKeys;
var audiotestComponents;
function audiotestRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audiotest' ---
    t = 0;
    audiotestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audiotest.started', globalClock.getTime());
    sound_testrun.setVolume(1.0);
    res_audio_testrun.keys = undefined;
    res_audio_testrun.rt = undefined;
    _res_audio_testrun_allKeys = [];
    // keep track of which components have finished
    audiotestComponents = [];
    audiotestComponents.push(sound_testrun);
    audiotestComponents.push(res_audio_testrun);
    
    audiotestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audiotestRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audiotest' ---
    // get current time
    t = audiotestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_testrun
    if (t >= 2 && sound_testrun.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_testrun.tStart = t;  // (not accounting for frame time here)
      sound_testrun.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_testrun.play(); });  // screen flip
      sound_testrun.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_testrun.getDuration() + sound_testrun.tStart)     && sound_testrun.status === PsychoJS.Status.STARTED) {
      sound_testrun.stop();  // stop the sound (if longer than duration)
      sound_testrun.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_audio_testrun* updates
    if (t >= 2 && res_audio_testrun.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_audio_testrun.tStart = t;  // (not accounting for frame time here)
      res_audio_testrun.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_audio_testrun.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_audio_testrun.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_audio_testrun.clearEvents(); });
    }
    
    if (res_audio_testrun.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_audio_testrun.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_audio_testrun_allKeys = _res_audio_testrun_allKeys.concat(theseKeys);
      if (_res_audio_testrun_allKeys.length > 0) {
        res_audio_testrun.keys = _res_audio_testrun_allKeys[_res_audio_testrun_allKeys.length - 1].name;  // just the last key pressed
        res_audio_testrun.rt = _res_audio_testrun_allKeys[_res_audio_testrun_allKeys.length - 1].rt;
        res_audio_testrun.duration = _res_audio_testrun_allKeys[_res_audio_testrun_allKeys.length - 1].duration;
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
    audiotestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audiotestRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audiotest' ---
    audiotestComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audiotest.stopped', globalClock.getTime());
    sound_testrun.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_audio_testrun.corr, level);
    }
    psychoJS.experiment.addData('res_audio_testrun.keys', res_audio_testrun.keys);
    if (typeof res_audio_testrun.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_audio_testrun.rt', res_audio_testrun.rt);
        psychoJS.experiment.addData('res_audio_testrun.duration', res_audio_testrun.duration);
        routineTimer.reset();
        }
    
    res_audio_testrun.stop();
    // the Routine "audiotest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_testpassed_allKeys;
var audiotestpassedComponents;
function audiotestpassedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audiotestpassed' ---
    t = 0;
    audiotestpassedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audiotestpassed.started', globalClock.getTime());
    res_testpassed.keys = undefined;
    res_testpassed.rt = undefined;
    _res_testpassed_allKeys = [];
    // keep track of which components have finished
    audiotestpassedComponents = [];
    audiotestpassedComponents.push(autest_passed);
    audiotestpassedComponents.push(res_testpassed);
    
    audiotestpassedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audiotestpassedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audiotestpassed' ---
    // get current time
    t = audiotestpassedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *autest_passed* updates
    if (t >= 0 && autest_passed.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      autest_passed.tStart = t;  // (not accounting for frame time here)
      autest_passed.frameNStart = frameN;  // exact frame index
      
      autest_passed.setAutoDraw(true);
    }
    
    
    // *res_testpassed* updates
    if (t >= 2 && res_testpassed.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_testpassed.tStart = t;  // (not accounting for frame time here)
      res_testpassed.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_testpassed.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_testpassed.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_testpassed.clearEvents(); });
    }
    
    if (res_testpassed.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_testpassed.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_testpassed_allKeys = _res_testpassed_allKeys.concat(theseKeys);
      if (_res_testpassed_allKeys.length > 0) {
        res_testpassed.keys = _res_testpassed_allKeys[_res_testpassed_allKeys.length - 1].name;  // just the last key pressed
        res_testpassed.rt = _res_testpassed_allKeys[_res_testpassed_allKeys.length - 1].rt;
        res_testpassed.duration = _res_testpassed_allKeys[_res_testpassed_allKeys.length - 1].duration;
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
    audiotestpassedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audiotestpassedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audiotestpassed' ---
    audiotestpassedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audiotestpassed.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_testpassed.corr, level);
    }
    psychoJS.experiment.addData('res_testpassed.keys', res_testpassed.keys);
    if (typeof res_testpassed.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_testpassed.rt', res_testpassed.rt);
        psychoJS.experiment.addData('res_testpassed.duration', res_testpassed.duration);
        routineTimer.reset();
        }
    
    res_testpassed.stop();
    // the Routine "audiotestpassed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_500Hz_0_25_allKeys;
var audio_500Hz_0_25Components;
function audio_500Hz_0_25RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audio_500Hz_0_25' ---
    t = 0;
    audio_500Hz_0_25Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audio_500Hz_0_25.started', globalClock.getTime());
    sound_500Hz_0_25.setVolume(0.25);
    res_500Hz_0_25.keys = undefined;
    res_500Hz_0_25.rt = undefined;
    _res_500Hz_0_25_allKeys = [];
    // keep track of which components have finished
    audio_500Hz_0_25Components = [];
    audio_500Hz_0_25Components.push(sound_500Hz_0_25);
    audio_500Hz_0_25Components.push(res_500Hz_0_25);
    
    audio_500Hz_0_25Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_500Hz_0_25RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audio_500Hz_0_25' ---
    // get current time
    t = audio_500Hz_0_25Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_500Hz_0_25
    if (t >= 2 && sound_500Hz_0_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_500Hz_0_25.tStart = t;  // (not accounting for frame time here)
      sound_500Hz_0_25.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_500Hz_0_25.play(); });  // screen flip
      sound_500Hz_0_25.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_500Hz_0_25.getDuration() + sound_500Hz_0_25.tStart)     && sound_500Hz_0_25.status === PsychoJS.Status.STARTED) {
      sound_500Hz_0_25.stop();  // stop the sound (if longer than duration)
      sound_500Hz_0_25.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_500Hz_0_25* updates
    if (t >= 2 && res_500Hz_0_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_500Hz_0_25.tStart = t;  // (not accounting for frame time here)
      res_500Hz_0_25.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_500Hz_0_25.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_500Hz_0_25.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_500Hz_0_25.clearEvents(); });
    }
    
    if (res_500Hz_0_25.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_500Hz_0_25.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_500Hz_0_25_allKeys = _res_500Hz_0_25_allKeys.concat(theseKeys);
      if (_res_500Hz_0_25_allKeys.length > 0) {
        res_500Hz_0_25.keys = _res_500Hz_0_25_allKeys[_res_500Hz_0_25_allKeys.length - 1].name;  // just the last key pressed
        res_500Hz_0_25.rt = _res_500Hz_0_25_allKeys[_res_500Hz_0_25_allKeys.length - 1].rt;
        res_500Hz_0_25.duration = _res_500Hz_0_25_allKeys[_res_500Hz_0_25_allKeys.length - 1].duration;
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
    audio_500Hz_0_25Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_500Hz_0_25RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audio_500Hz_0_25' ---
    audio_500Hz_0_25Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audio_500Hz_0_25.stopped', globalClock.getTime());
    sound_500Hz_0_25.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_500Hz_0_25.corr, level);
    }
    psychoJS.experiment.addData('res_500Hz_0_25.keys', res_500Hz_0_25.keys);
    if (typeof res_500Hz_0_25.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_500Hz_0_25.rt', res_500Hz_0_25.rt);
        psychoJS.experiment.addData('res_500Hz_0_25.duration', res_500Hz_0_25.duration);
        routineTimer.reset();
        }
    
    res_500Hz_0_25.stop();
    // the Routine "audio_500Hz_0_25" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_500Hz_allKeys;
var audio_500HzComponents;
function audio_500HzRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audio_500Hz' ---
    t = 0;
    audio_500HzClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audio_500Hz.started', globalClock.getTime());
    sound_500Hz.setVolume(1.0);
    res_500Hz.keys = undefined;
    res_500Hz.rt = undefined;
    _res_500Hz_allKeys = [];
    // keep track of which components have finished
    audio_500HzComponents = [];
    audio_500HzComponents.push(sound_500Hz);
    audio_500HzComponents.push(res_500Hz);
    
    audio_500HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_500HzRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audio_500Hz' ---
    // get current time
    t = audio_500HzClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_500Hz
    if (t >= 2 && sound_500Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_500Hz.tStart = t;  // (not accounting for frame time here)
      sound_500Hz.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_500Hz.play(); });  // screen flip
      sound_500Hz.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_500Hz.getDuration() + sound_500Hz.tStart)     && sound_500Hz.status === PsychoJS.Status.STARTED) {
      sound_500Hz.stop();  // stop the sound (if longer than duration)
      sound_500Hz.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_500Hz* updates
    if (t >= 2 && res_500Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_500Hz.tStart = t;  // (not accounting for frame time here)
      res_500Hz.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_500Hz.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_500Hz.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_500Hz.clearEvents(); });
    }
    
    if (res_500Hz.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_500Hz.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_500Hz_allKeys = _res_500Hz_allKeys.concat(theseKeys);
      if (_res_500Hz_allKeys.length > 0) {
        res_500Hz.keys = _res_500Hz_allKeys[_res_500Hz_allKeys.length - 1].name;  // just the last key pressed
        res_500Hz.rt = _res_500Hz_allKeys[_res_500Hz_allKeys.length - 1].rt;
        res_500Hz.duration = _res_500Hz_allKeys[_res_500Hz_allKeys.length - 1].duration;
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
    audio_500HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_500HzRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audio_500Hz' ---
    audio_500HzComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audio_500Hz.stopped', globalClock.getTime());
    sound_500Hz.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_500Hz.corr, level);
    }
    psychoJS.experiment.addData('res_500Hz.keys', res_500Hz.keys);
    if (typeof res_500Hz.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_500Hz.rt', res_500Hz.rt);
        psychoJS.experiment.addData('res_500Hz.duration', res_500Hz.duration);
        routineTimer.reset();
        }
    
    res_500Hz.stop();
    // the Routine "audio_500Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_2500Hz_allKeys;
var audio_2500HzComponents;
function audio_2500HzRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audio_2500Hz' ---
    t = 0;
    audio_2500HzClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audio_2500Hz.started', globalClock.getTime());
    sound_2500Hz.setVolume(1.0);
    res_2500Hz.keys = undefined;
    res_2500Hz.rt = undefined;
    _res_2500Hz_allKeys = [];
    // keep track of which components have finished
    audio_2500HzComponents = [];
    audio_2500HzComponents.push(sound_2500Hz);
    audio_2500HzComponents.push(res_2500Hz);
    
    audio_2500HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_2500HzRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audio_2500Hz' ---
    // get current time
    t = audio_2500HzClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_2500Hz
    if (t >= 2 && sound_2500Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_2500Hz.tStart = t;  // (not accounting for frame time here)
      sound_2500Hz.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_2500Hz.play(); });  // screen flip
      sound_2500Hz.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_2500Hz.getDuration() + sound_2500Hz.tStart)     && sound_2500Hz.status === PsychoJS.Status.STARTED) {
      sound_2500Hz.stop();  // stop the sound (if longer than duration)
      sound_2500Hz.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_2500Hz* updates
    if (t >= 2 && res_2500Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_2500Hz.tStart = t;  // (not accounting for frame time here)
      res_2500Hz.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_2500Hz.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_2500Hz.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_2500Hz.clearEvents(); });
    }
    
    if (res_2500Hz.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_2500Hz.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_2500Hz_allKeys = _res_2500Hz_allKeys.concat(theseKeys);
      if (_res_2500Hz_allKeys.length > 0) {
        res_2500Hz.keys = _res_2500Hz_allKeys[_res_2500Hz_allKeys.length - 1].name;  // just the last key pressed
        res_2500Hz.rt = _res_2500Hz_allKeys[_res_2500Hz_allKeys.length - 1].rt;
        res_2500Hz.duration = _res_2500Hz_allKeys[_res_2500Hz_allKeys.length - 1].duration;
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
    audio_2500HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_2500HzRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audio_2500Hz' ---
    audio_2500HzComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audio_2500Hz.stopped', globalClock.getTime());
    sound_2500Hz.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_2500Hz.corr, level);
    }
    psychoJS.experiment.addData('res_2500Hz.keys', res_2500Hz.keys);
    if (typeof res_2500Hz.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_2500Hz.rt', res_2500Hz.rt);
        psychoJS.experiment.addData('res_2500Hz.duration', res_2500Hz.duration);
        routineTimer.reset();
        }
    
    res_2500Hz.stop();
    // the Routine "audio_2500Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_5000Hz_allKeys;
var audio_5000HzComponents;
function audio_5000HzRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audio_5000Hz' ---
    t = 0;
    audio_5000HzClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audio_5000Hz.started', globalClock.getTime());
    sound_5000Hz.setVolume(1.0);
    res_5000Hz.keys = undefined;
    res_5000Hz.rt = undefined;
    _res_5000Hz_allKeys = [];
    // keep track of which components have finished
    audio_5000HzComponents = [];
    audio_5000HzComponents.push(sound_5000Hz);
    audio_5000HzComponents.push(res_5000Hz);
    
    audio_5000HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_5000HzRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audio_5000Hz' ---
    // get current time
    t = audio_5000HzClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_5000Hz
    if (t >= 2 && sound_5000Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_5000Hz.tStart = t;  // (not accounting for frame time here)
      sound_5000Hz.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_5000Hz.play(); });  // screen flip
      sound_5000Hz.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_5000Hz.getDuration() + sound_5000Hz.tStart)     && sound_5000Hz.status === PsychoJS.Status.STARTED) {
      sound_5000Hz.stop();  // stop the sound (if longer than duration)
      sound_5000Hz.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_5000Hz* updates
    if (t >= 2 && res_5000Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_5000Hz.tStart = t;  // (not accounting for frame time here)
      res_5000Hz.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_5000Hz.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_5000Hz.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_5000Hz.clearEvents(); });
    }
    
    if (res_5000Hz.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_5000Hz.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_5000Hz_allKeys = _res_5000Hz_allKeys.concat(theseKeys);
      if (_res_5000Hz_allKeys.length > 0) {
        res_5000Hz.keys = _res_5000Hz_allKeys[_res_5000Hz_allKeys.length - 1].name;  // just the last key pressed
        res_5000Hz.rt = _res_5000Hz_allKeys[_res_5000Hz_allKeys.length - 1].rt;
        res_5000Hz.duration = _res_5000Hz_allKeys[_res_5000Hz_allKeys.length - 1].duration;
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
    audio_5000HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_5000HzRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audio_5000Hz' ---
    audio_5000HzComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audio_5000Hz.stopped', globalClock.getTime());
    sound_5000Hz.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_5000Hz.corr, level);
    }
    psychoJS.experiment.addData('res_5000Hz.keys', res_5000Hz.keys);
    if (typeof res_5000Hz.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_5000Hz.rt', res_5000Hz.rt);
        psychoJS.experiment.addData('res_5000Hz.duration', res_5000Hz.duration);
        routineTimer.reset();
        }
    
    res_5000Hz.stop();
    // the Routine "audio_5000Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_7500Hz_allKeys;
var audio_7500HzComponents;
function audio_7500HzRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audio_7500Hz' ---
    t = 0;
    audio_7500HzClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audio_7500Hz.started', globalClock.getTime());
    sound_7500Hz.setVolume(1.0);
    res_7500Hz.keys = undefined;
    res_7500Hz.rt = undefined;
    _res_7500Hz_allKeys = [];
    // keep track of which components have finished
    audio_7500HzComponents = [];
    audio_7500HzComponents.push(sound_7500Hz);
    audio_7500HzComponents.push(res_7500Hz);
    
    audio_7500HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_7500HzRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audio_7500Hz' ---
    // get current time
    t = audio_7500HzClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_7500Hz
    if (t >= 2 && sound_7500Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_7500Hz.tStart = t;  // (not accounting for frame time here)
      sound_7500Hz.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_7500Hz.play(); });  // screen flip
      sound_7500Hz.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_7500Hz.getDuration() + sound_7500Hz.tStart)     && sound_7500Hz.status === PsychoJS.Status.STARTED) {
      sound_7500Hz.stop();  // stop the sound (if longer than duration)
      sound_7500Hz.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_7500Hz* updates
    if (t >= 2 && res_7500Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_7500Hz.tStart = t;  // (not accounting for frame time here)
      res_7500Hz.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_7500Hz.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_7500Hz.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_7500Hz.clearEvents(); });
    }
    
    if (res_7500Hz.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_7500Hz.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_7500Hz_allKeys = _res_7500Hz_allKeys.concat(theseKeys);
      if (_res_7500Hz_allKeys.length > 0) {
        res_7500Hz.keys = _res_7500Hz_allKeys[_res_7500Hz_allKeys.length - 1].name;  // just the last key pressed
        res_7500Hz.rt = _res_7500Hz_allKeys[_res_7500Hz_allKeys.length - 1].rt;
        res_7500Hz.duration = _res_7500Hz_allKeys[_res_7500Hz_allKeys.length - 1].duration;
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
    audio_7500HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_7500HzRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audio_7500Hz' ---
    audio_7500HzComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audio_7500Hz.stopped', globalClock.getTime());
    sound_7500Hz.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_7500Hz.corr, level);
    }
    psychoJS.experiment.addData('res_7500Hz.keys', res_7500Hz.keys);
    if (typeof res_7500Hz.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_7500Hz.rt', res_7500Hz.rt);
        psychoJS.experiment.addData('res_7500Hz.duration', res_7500Hz.duration);
        routineTimer.reset();
        }
    
    res_7500Hz.stop();
    // the Routine "audio_7500Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_10000Hz_allKeys;
var audio_10000HzComponents;
function audio_10000HzRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audio_10000Hz' ---
    t = 0;
    audio_10000HzClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audio_10000Hz.started', globalClock.getTime());
    sound_10000Hz.setVolume(1.0);
    res_10000Hz.keys = undefined;
    res_10000Hz.rt = undefined;
    _res_10000Hz_allKeys = [];
    // keep track of which components have finished
    audio_10000HzComponents = [];
    audio_10000HzComponents.push(sound_10000Hz);
    audio_10000HzComponents.push(res_10000Hz);
    
    audio_10000HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_10000HzRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audio_10000Hz' ---
    // get current time
    t = audio_10000HzClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_10000Hz
    if (t >= 2 && sound_10000Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_10000Hz.tStart = t;  // (not accounting for frame time here)
      sound_10000Hz.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_10000Hz.play(); });  // screen flip
      sound_10000Hz.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_10000Hz.getDuration() + sound_10000Hz.tStart)     && sound_10000Hz.status === PsychoJS.Status.STARTED) {
      sound_10000Hz.stop();  // stop the sound (if longer than duration)
      sound_10000Hz.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_10000Hz* updates
    if (t >= 2 && res_10000Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_10000Hz.tStart = t;  // (not accounting for frame time here)
      res_10000Hz.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_10000Hz.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_10000Hz.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_10000Hz.clearEvents(); });
    }
    
    if (res_10000Hz.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_10000Hz.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_10000Hz_allKeys = _res_10000Hz_allKeys.concat(theseKeys);
      if (_res_10000Hz_allKeys.length > 0) {
        res_10000Hz.keys = _res_10000Hz_allKeys[_res_10000Hz_allKeys.length - 1].name;  // just the last key pressed
        res_10000Hz.rt = _res_10000Hz_allKeys[_res_10000Hz_allKeys.length - 1].rt;
        res_10000Hz.duration = _res_10000Hz_allKeys[_res_10000Hz_allKeys.length - 1].duration;
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
    audio_10000HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_10000HzRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audio_10000Hz' ---
    audio_10000HzComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audio_10000Hz.stopped', globalClock.getTime());
    sound_10000Hz.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_10000Hz.corr, level);
    }
    psychoJS.experiment.addData('res_10000Hz.keys', res_10000Hz.keys);
    if (typeof res_10000Hz.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_10000Hz.rt', res_10000Hz.rt);
        psychoJS.experiment.addData('res_10000Hz.duration', res_10000Hz.duration);
        routineTimer.reset();
        }
    
    res_10000Hz.stop();
    // the Routine "audio_10000Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_12500_allKeys;
var audio_12500HzComponents;
function audio_12500HzRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audio_12500Hz' ---
    t = 0;
    audio_12500HzClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audio_12500Hz.started', globalClock.getTime());
    sound_12500.setVolume(1.0);
    res_12500.keys = undefined;
    res_12500.rt = undefined;
    _res_12500_allKeys = [];
    // keep track of which components have finished
    audio_12500HzComponents = [];
    audio_12500HzComponents.push(sound_12500);
    audio_12500HzComponents.push(res_12500);
    
    audio_12500HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_12500HzRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audio_12500Hz' ---
    // get current time
    t = audio_12500HzClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_12500
    if (t >= 2 && sound_12500.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_12500.tStart = t;  // (not accounting for frame time here)
      sound_12500.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_12500.play(); });  // screen flip
      sound_12500.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_12500.getDuration() + sound_12500.tStart)     && sound_12500.status === PsychoJS.Status.STARTED) {
      sound_12500.stop();  // stop the sound (if longer than duration)
      sound_12500.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_12500* updates
    if (t >= 2 && res_12500.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_12500.tStart = t;  // (not accounting for frame time here)
      res_12500.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_12500.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_12500.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_12500.clearEvents(); });
    }
    
    if (res_12500.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_12500.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_12500_allKeys = _res_12500_allKeys.concat(theseKeys);
      if (_res_12500_allKeys.length > 0) {
        res_12500.keys = _res_12500_allKeys[_res_12500_allKeys.length - 1].name;  // just the last key pressed
        res_12500.rt = _res_12500_allKeys[_res_12500_allKeys.length - 1].rt;
        res_12500.duration = _res_12500_allKeys[_res_12500_allKeys.length - 1].duration;
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
    audio_12500HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_12500HzRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audio_12500Hz' ---
    audio_12500HzComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audio_12500Hz.stopped', globalClock.getTime());
    sound_12500.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_12500.corr, level);
    }
    psychoJS.experiment.addData('res_12500.keys', res_12500.keys);
    if (typeof res_12500.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_12500.rt', res_12500.rt);
        psychoJS.experiment.addData('res_12500.duration', res_12500.duration);
        routineTimer.reset();
        }
    
    res_12500.stop();
    // the Routine "audio_12500Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _res_15000Hz_allKeys;
var audio_15000HzComponents;
function audio_15000HzRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'audio_15000Hz' ---
    t = 0;
    audio_15000HzClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('audio_15000Hz.started', globalClock.getTime());
    sound_15000.setVolume(1.0);
    res_15000Hz.keys = undefined;
    res_15000Hz.rt = undefined;
    _res_15000Hz_allKeys = [];
    // keep track of which components have finished
    audio_15000HzComponents = [];
    audio_15000HzComponents.push(sound_15000);
    audio_15000HzComponents.push(res_15000Hz);
    
    audio_15000HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function audio_15000HzRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'audio_15000Hz' ---
    // get current time
    t = audio_15000HzClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_15000
    if (t >= 2 && sound_15000.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_15000.tStart = t;  // (not accounting for frame time here)
      sound_15000.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_15000.play(); });  // screen flip
      sound_15000.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_15000.getDuration() + sound_15000.tStart)     && sound_15000.status === PsychoJS.Status.STARTED) {
      sound_15000.stop();  // stop the sound (if longer than duration)
      sound_15000.status = PsychoJS.Status.FINISHED;
    }
    
    // *res_15000Hz* updates
    if (t >= 2 && res_15000Hz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      res_15000Hz.tStart = t;  // (not accounting for frame time here)
      res_15000Hz.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { res_15000Hz.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { res_15000Hz.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { res_15000Hz.clearEvents(); });
    }
    
    if (res_15000Hz.status === PsychoJS.Status.STARTED) {
      let theseKeys = res_15000Hz.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _res_15000Hz_allKeys = _res_15000Hz_allKeys.concat(theseKeys);
      if (_res_15000Hz_allKeys.length > 0) {
        res_15000Hz.keys = _res_15000Hz_allKeys[_res_15000Hz_allKeys.length - 1].name;  // just the last key pressed
        res_15000Hz.rt = _res_15000Hz_allKeys[_res_15000Hz_allKeys.length - 1].rt;
        res_15000Hz.duration = _res_15000Hz_allKeys[_res_15000Hz_allKeys.length - 1].duration;
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
    audio_15000HzComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function audio_15000HzRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'audio_15000Hz' ---
    audio_15000HzComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('audio_15000Hz.stopped', globalClock.getTime());
    sound_15000.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(res_15000Hz.corr, level);
    }
    psychoJS.experiment.addData('res_15000Hz.keys', res_15000Hz.keys);
    if (typeof res_15000Hz.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('res_15000Hz.rt', res_15000Hz.rt);
        psychoJS.experiment.addData('res_15000Hz.duration', res_15000Hz.duration);
        routineTimer.reset();
        }
    
    res_15000Hz.stop();
    // the Routine "audio_15000Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var outroComponents;
function outroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'outro' ---
    t = 0;
    outroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('outro.started', globalClock.getTime());
    // keep track of which components have finished
    outroComponents = [];
    outroComponents.push(text_outro);
    
    outroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function outroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'outro' ---
    // get current time
    t = outroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_outro* updates
    if (t >= 0.0 && text_outro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_outro.tStart = t;  // (not accounting for frame time here)
      text_outro.frameNStart = frameN;  // exact frame index
      
      text_outro.setAutoDraw(true);
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
    outroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function outroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'outro' ---
    outroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('outro.stopped', globalClock.getTime());
    // the Routine "outro" was not non-slip safe, so reset the non-slip timer
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
