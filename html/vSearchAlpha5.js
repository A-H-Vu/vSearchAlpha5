/********************** 
 * Vsearchalpha5 Test *
 **********************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'vSearchAlpha5';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
flowScheduler.add(instruction1RoutineBegin());
flowScheduler.add(instruction1RoutineEachFrame());
flowScheduler.add(instruction1RoutineEnd());
const trials1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials1LoopBegin, trials1LoopScheduler);
flowScheduler.add(trials1LoopScheduler);
flowScheduler.add(trials1LoopEnd);
flowScheduler.add(breakTime1RoutineBegin());
flowScheduler.add(breakTime1RoutineEachFrame());
flowScheduler.add(breakTime1RoutineEnd());
const trials2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials2LoopBegin, trials2LoopScheduler);
flowScheduler.add(trials2LoopScheduler);
flowScheduler.add(trials2LoopEnd);
flowScheduler.add(breakTime2RoutineBegin());
flowScheduler.add(breakTime2RoutineEachFrame());
flowScheduler.add(breakTime2RoutineEnd());
const trials3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials3LoopBegin, trials3LoopScheduler);
flowScheduler.add(trials3LoopScheduler);
flowScheduler.add(trials3LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instruction1Clock;
var instr1;
var keyResp1;
var l1ex;
var l2ex;
var t1ex;
var tTex;
var trial1Clock;
var trial1Fix;
var trial1L11;
var trial1L12;
var trial1L21;
var trial1L22;
var trial1T11;
var trial1T12;
var trial1L13;
var trial1L14;
var trial1L23;
var trial1L24;
var trial1T13;
var trial1T14;
var trial1L15;
var trial1L16;
var trial1L25;
var trial1L26;
var trial1T15;
var trial1T16;
var trial1TT;
var trial1Resp;
var breakTime1Clock;
var breakText1;
var breakResp1;
var trial2Clock;
var trial2Fix;
var trial2L11;
var trial2L12;
var trial2L21;
var trial2L22;
var trial2T11;
var trial2T12;
var trial2L13;
var trial2L14;
var trial2L23;
var trial2L24;
var trial2T13;
var trial2T14;
var trial2L15;
var trial2L16;
var trial2L25;
var trial2L26;
var trial2T15;
var trial2T16;
var trial2TT;
var trial2Resp;
var breakTime2Clock;
var breakText2;
var breakResp2;
var trial3Clock;
var trial3Fix;
var trial3L11;
var trial3L12;
var trial3L21;
var trial3L22;
var trial3T11;
var trial3T12;
var trial3L13;
var trial3L14;
var trial3L23;
var trial3L24;
var trial3T13;
var trial3T14;
var trial3L15;
var trial3L16;
var trial3L25;
var trial3L26;
var trial3T15;
var trial3T16;
var trial3TT;
var trial3Resp;
var endClock;
var thanks;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruction1"
  instruction1Clock = new util.Clock();
  instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr1',
    text: "In this task you will see sets of shapes made of four different shapes as outlined below. Only press the 's' key if you see the “T” shape, which is the last shape. Otherwise, press the 'k' key. There will be 6, 12, or 18 shapes to observe in each trial. Press space to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyResp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  l1ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l1ex', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.15)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  l2ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l2ex', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [(- 0.1), (- 0.15)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  t1ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 't1ex', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0.1, (- 0.15)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  tTex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tTex', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0.3, (- 0.15)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "trial1"
  trial1Clock = new util.Clock();
  trial1Fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial1Fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trial1L11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L11', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  trial1L12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L12', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  trial1L21 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L21', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  trial1L22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L22', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  trial1T11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1T11', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  trial1T12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1T12', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  trial1L13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L13', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  trial1L14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L14', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  trial1L23 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L23', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  trial1L24 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L24', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  trial1T13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1T13', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  trial1T14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1T14', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -12.0 
  });
  trial1L15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L15', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -13.0 
  });
  trial1L16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L16', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -14.0 
  });
  trial1L25 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L25', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -15.0 
  });
  trial1L26 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1L26', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -16.0 
  });
  trial1T15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1T15', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -17.0 
  });
  trial1T16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1T16', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -18.0 
  });
  trial1TT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial1TT', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -19.0 
  });
  trial1Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "breakTime1"
  breakTime1Clock = new util.Clock();
  breakText1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'breakText1',
    text: "A quick break before the next set of trials. Remember, only press the 's' key if you see the “T” shape, which is the last shape. Otherwise, press the 'k' key. There will be 6, 12, or 18 shapes to observe in each trial. Press space to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  breakResp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial2"
  trial2Clock = new util.Clock();
  trial2Fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial2Fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trial2L11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L11', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  trial2L12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L12', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  trial2L21 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L21', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  trial2L22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L22', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  trial2T11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2T11', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  trial2T12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2T12', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  trial2L13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L13', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  trial2L14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L14', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  trial2L23 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L23', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  trial2L24 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L24', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  trial2T13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2T13', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  trial2T14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2T14', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -12.0 
  });
  trial2L15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L15', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -13.0 
  });
  trial2L16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L16', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -14.0 
  });
  trial2L25 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L25', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -15.0 
  });
  trial2L26 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2L26', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -16.0 
  });
  trial2T15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2T15', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -17.0 
  });
  trial2T16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2T16', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -18.0 
  });
  trial2TT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial2TT', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -19.0 
  });
  trial2Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "breakTime2"
  breakTime2Clock = new util.Clock();
  breakText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'breakText2',
    text: "A quick break before the next set of trials. Remember, only press the 's' key if you see the “T” shape, which is the last shape. Otherwise, press the 'k' key. There will be 6, 12, or 18 shapes to observe in each trial. Press space to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  breakResp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial3"
  trial3Clock = new util.Clock();
  trial3Fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial3Fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trial3L11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L11', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  trial3L12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L12', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  trial3L21 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L21', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  trial3L22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L22', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  trial3T11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3T11', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  trial3T12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3T12', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  trial3L13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L13', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  trial3L14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L14', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  trial3L23 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L23', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  trial3L24 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L24', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  trial3T13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3T13', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  trial3T14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3T14', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -12.0 
  });
  trial3L15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L15', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -13.0 
  });
  trial3L16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L16', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -14.0 
  });
  trial3L25 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L25', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -15.0 
  });
  trial3L26 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3L26', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -16.0 
  });
  trial3T15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3T15', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -17.0 
  });
  trial3T16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3T16', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -18.0 
  });
  trial3TT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial3TT', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -19.0 
  });
  trial3Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  thanks = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks',
    text: 'This is the end of the experiment.\nThank you for your time.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _keyResp1_allKeys;
var instruction1Components;
function instruction1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instruction1'-------
    t = 0;
    instruction1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyResp1.keys = undefined;
    keyResp1.rt = undefined;
    _keyResp1_allKeys = [];
    // keep track of which components have finished
    instruction1Components = [];
    instruction1Components.push(instr1);
    instruction1Components.push(keyResp1);
    instruction1Components.push(l1ex);
    instruction1Components.push(l2ex);
    instruction1Components.push(t1ex);
    instruction1Components.push(tTex);
    
    for (const thisComponent of instruction1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instruction1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instruction1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instruction1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr1* updates
    if (t >= 0.0 && instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr1.tStart = t;  // (not accounting for frame time here)
      instr1.frameNStart = frameN;  // exact frame index
      
      instr1.setAutoDraw(true);
    }

    
    // *keyResp1* updates
    if (t >= 0.0 && keyResp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp1.tStart = t;  // (not accounting for frame time here)
      keyResp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyResp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyResp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyResp1.clearEvents(); });
    }

    if (keyResp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp1.getKeys({keyList: ['space'], waitRelease: false});
      _keyResp1_allKeys = _keyResp1_allKeys.concat(theseKeys);
      if (_keyResp1_allKeys.length > 0) {
        keyResp1.keys = _keyResp1_allKeys[_keyResp1_allKeys.length - 1].name;  // just the last key pressed
        keyResp1.rt = _keyResp1_allKeys[_keyResp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *l1ex* updates
    if (t >= 0.0 && l1ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l1ex.tStart = t;  // (not accounting for frame time here)
      l1ex.frameNStart = frameN;  // exact frame index
      
      l1ex.setAutoDraw(true);
    }

    
    // *l2ex* updates
    if (t >= 0.0 && l2ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l2ex.tStart = t;  // (not accounting for frame time here)
      l2ex.frameNStart = frameN;  // exact frame index
      
      l2ex.setAutoDraw(true);
    }

    
    // *t1ex* updates
    if (t >= 0.0 && t1ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t1ex.tStart = t;  // (not accounting for frame time here)
      t1ex.frameNStart = frameN;  // exact frame index
      
      t1ex.setAutoDraw(true);
    }

    
    // *tTex* updates
    if (t >= 0.0 && tTex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tTex.tStart = t;  // (not accounting for frame time here)
      tTex.frameNStart = frameN;  // exact frame index
      
      tTex.setAutoDraw(true);
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
    for (const thisComponent of instruction1Components)
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


function instruction1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instruction1'-------
    for (const thisComponent of instruction1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('keyResp1.keys', keyResp1.keys);
    if (typeof keyResp1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyResp1.rt', keyResp1.rt);
        routineTimer.reset();
        }
    
    keyResp1.stop();
    // the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials1;
var currentLoop;
function trials1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'vSearchCond1.xlsx',
    seed: undefined, name: 'trials1'
  });
  psychoJS.experiment.addLoop(trials1); // add the loop to the experiment
  currentLoop = trials1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials1 of trials1) {
    const snapshot = trials1.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trial1RoutineBegin(snapshot));
    thisScheduler.add(trial1RoutineEachFrame(snapshot));
    thisScheduler.add(trial1RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials1LoopEnd() {
  psychoJS.experiment.removeLoop(trials1);

  return Scheduler.Event.NEXT;
}


var trials2;
function trials2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'vSearchCond2.xlsx',
    seed: undefined, name: 'trials2'
  });
  psychoJS.experiment.addLoop(trials2); // add the loop to the experiment
  currentLoop = trials2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials2 of trials2) {
    const snapshot = trials2.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trial2RoutineBegin(snapshot));
    thisScheduler.add(trial2RoutineEachFrame(snapshot));
    thisScheduler.add(trial2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials2LoopEnd() {
  psychoJS.experiment.removeLoop(trials2);

  return Scheduler.Event.NEXT;
}


var trials3;
function trials3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'vSearchCond3.xlsx',
    seed: undefined, name: 'trials3'
  });
  psychoJS.experiment.addLoop(trials3); // add the loop to the experiment
  currentLoop = trials3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials3 of trials3) {
    const snapshot = trials3.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trial3RoutineBegin(snapshot));
    thisScheduler.add(trial3RoutineEachFrame(snapshot));
    thisScheduler.add(trial3RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials3LoopEnd() {
  psychoJS.experiment.removeLoop(trials3);

  return Scheduler.Event.NEXT;
}


var _trial1Resp_allKeys;
var trial1Components;
function trial1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial1'-------
    t = 0;
    trial1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    trial1L11.setPos([loc1, loc2]);
    trial1L12.setPos([loc3, loc4]);
    trial1L21.setPos([loc5, loc6]);
    trial1L22.setPos([loc7, loc8]);
    trial1T11.setPos([loc9, loc10]);
    trial1T12.setPos([loc11, loc12]);
    trial1L13.setPos([loc13, loc14]);
    trial1L14.setPos([loc15, loc16]);
    trial1L23.setPos([loc17, loc18]);
    trial1L24.setPos([loc19, loc20]);
    trial1T13.setPos([loc21, loc22]);
    trial1T14.setPos([loc23, loc24]);
    trial1L15.setPos([loc25, loc26]);
    trial1L16.setPos([loc27, loc28]);
    trial1L25.setPos([loc29, loc30]);
    trial1L26.setPos([loc31, loc32]);
    trial1T15.setPos([loc33, loc34]);
    trial1T16.setPos([loc35, loc36]);
    trial1TT.setPos([loc37, loc38]);
    trial1Resp.keys = undefined;
    trial1Resp.rt = undefined;
    _trial1Resp_allKeys = [];
    // keep track of which components have finished
    trial1Components = [];
    trial1Components.push(trial1Fix);
    trial1Components.push(trial1L11);
    trial1Components.push(trial1L12);
    trial1Components.push(trial1L21);
    trial1Components.push(trial1L22);
    trial1Components.push(trial1T11);
    trial1Components.push(trial1T12);
    trial1Components.push(trial1L13);
    trial1Components.push(trial1L14);
    trial1Components.push(trial1L23);
    trial1Components.push(trial1L24);
    trial1Components.push(trial1T13);
    trial1Components.push(trial1T14);
    trial1Components.push(trial1L15);
    trial1Components.push(trial1L16);
    trial1Components.push(trial1L25);
    trial1Components.push(trial1L26);
    trial1Components.push(trial1T15);
    trial1Components.push(trial1T16);
    trial1Components.push(trial1TT);
    trial1Components.push(trial1Resp);
    
    for (const thisComponent of trial1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function trial1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial1Fix* updates
    if (t >= 0.0 && trial1Fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1Fix.tStart = t;  // (not accounting for frame time here)
      trial1Fix.frameNStart = frameN;  // exact frame index
      
      trial1Fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial1Fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial1Fix.setAutoDraw(false);
    }
    
    // *trial1L11* updates
    if (t >= 1.0 && trial1L11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L11.tStart = t;  // (not accounting for frame time here)
      trial1L11.frameNStart = frameN;  // exact frame index
      
      trial1L11.setAutoDraw(true);
    }

    
    // *trial1L12* updates
    if (t >= 1.0 && trial1L12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L12.tStart = t;  // (not accounting for frame time here)
      trial1L12.frameNStart = frameN;  // exact frame index
      
      trial1L12.setAutoDraw(true);
    }

    
    // *trial1L21* updates
    if (t >= 1.0 && trial1L21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L21.tStart = t;  // (not accounting for frame time here)
      trial1L21.frameNStart = frameN;  // exact frame index
      
      trial1L21.setAutoDraw(true);
    }

    
    // *trial1L22* updates
    if (t >= 1.0 && trial1L22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L22.tStart = t;  // (not accounting for frame time here)
      trial1L22.frameNStart = frameN;  // exact frame index
      
      trial1L22.setAutoDraw(true);
    }

    
    // *trial1T11* updates
    if (t >= 1.0 && trial1T11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1T11.tStart = t;  // (not accounting for frame time here)
      trial1T11.frameNStart = frameN;  // exact frame index
      
      trial1T11.setAutoDraw(true);
    }

    
    // *trial1T12* updates
    if (t >= 1.0 && trial1T12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1T12.tStart = t;  // (not accounting for frame time here)
      trial1T12.frameNStart = frameN;  // exact frame index
      
      trial1T12.setAutoDraw(true);
    }

    
    // *trial1L13* updates
    if (t >= 1.0 && trial1L13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L13.tStart = t;  // (not accounting for frame time here)
      trial1L13.frameNStart = frameN;  // exact frame index
      
      trial1L13.setAutoDraw(true);
    }

    
    // *trial1L14* updates
    if (t >= 1.0 && trial1L14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L14.tStart = t;  // (not accounting for frame time here)
      trial1L14.frameNStart = frameN;  // exact frame index
      
      trial1L14.setAutoDraw(true);
    }

    
    // *trial1L23* updates
    if (t >= 1.0 && trial1L23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L23.tStart = t;  // (not accounting for frame time here)
      trial1L23.frameNStart = frameN;  // exact frame index
      
      trial1L23.setAutoDraw(true);
    }

    
    // *trial1L24* updates
    if (t >= 1.0 && trial1L24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L24.tStart = t;  // (not accounting for frame time here)
      trial1L24.frameNStart = frameN;  // exact frame index
      
      trial1L24.setAutoDraw(true);
    }

    
    // *trial1T13* updates
    if (t >= 1.0 && trial1T13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1T13.tStart = t;  // (not accounting for frame time here)
      trial1T13.frameNStart = frameN;  // exact frame index
      
      trial1T13.setAutoDraw(true);
    }

    
    // *trial1T14* updates
    if (t >= 1.0 && trial1T14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1T14.tStart = t;  // (not accounting for frame time here)
      trial1T14.frameNStart = frameN;  // exact frame index
      
      trial1T14.setAutoDraw(true);
    }

    
    // *trial1L15* updates
    if (t >= 1.0 && trial1L15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L15.tStart = t;  // (not accounting for frame time here)
      trial1L15.frameNStart = frameN;  // exact frame index
      
      trial1L15.setAutoDraw(true);
    }

    
    // *trial1L16* updates
    if (t >= 1.0 && trial1L16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L16.tStart = t;  // (not accounting for frame time here)
      trial1L16.frameNStart = frameN;  // exact frame index
      
      trial1L16.setAutoDraw(true);
    }

    
    // *trial1L25* updates
    if (t >= 1.0 && trial1L25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L25.tStart = t;  // (not accounting for frame time here)
      trial1L25.frameNStart = frameN;  // exact frame index
      
      trial1L25.setAutoDraw(true);
    }

    
    // *trial1L26* updates
    if (t >= 1.0 && trial1L26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1L26.tStart = t;  // (not accounting for frame time here)
      trial1L26.frameNStart = frameN;  // exact frame index
      
      trial1L26.setAutoDraw(true);
    }

    
    // *trial1T15* updates
    if (t >= 1.0 && trial1T15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1T15.tStart = t;  // (not accounting for frame time here)
      trial1T15.frameNStart = frameN;  // exact frame index
      
      trial1T15.setAutoDraw(true);
    }

    
    // *trial1T16* updates
    if (t >= 1.0 && trial1T16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1T16.tStart = t;  // (not accounting for frame time here)
      trial1T16.frameNStart = frameN;  // exact frame index
      
      trial1T16.setAutoDraw(true);
    }

    
    // *trial1TT* updates
    if (t >= 1.0 && trial1TT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1TT.tStart = t;  // (not accounting for frame time here)
      trial1TT.frameNStart = frameN;  // exact frame index
      
      trial1TT.setAutoDraw(true);
    }

    
    // *trial1Resp* updates
    if (t >= 1.0 && trial1Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial1Resp.tStart = t;  // (not accounting for frame time here)
      trial1Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trial1Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trial1Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trial1Resp.clearEvents(); });
    }

    if (trial1Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = trial1Resp.getKeys({keyList: ['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease: false});
      _trial1Resp_allKeys = _trial1Resp_allKeys.concat(theseKeys);
      if (_trial1Resp_allKeys.length > 0) {
        trial1Resp.keys = _trial1Resp_allKeys[_trial1Resp_allKeys.length - 1].name;  // just the last key pressed
        trial1Resp.rt = _trial1Resp_allKeys[_trial1Resp_allKeys.length - 1].rt;
        // was this correct?
        if (trial1Resp.keys == corrAns) {
            trial1Resp.corr = 1;
        } else {
            trial1Resp.corr = 0;
        }
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
    for (const thisComponent of trial1Components)
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


function trial1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial1'-------
    for (const thisComponent of trial1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (trial1Resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         trial1Resp.corr = 1;  // correct non-response
      } else {
         trial1Resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('trial1Resp.keys', trial1Resp.keys);
    psychoJS.experiment.addData('trial1Resp.corr', trial1Resp.corr);
    if (typeof trial1Resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trial1Resp.rt', trial1Resp.rt);
        routineTimer.reset();
        }
    
    trial1Resp.stop();
    // the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _breakResp1_allKeys;
var breakTime1Components;
function breakTime1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'breakTime1'-------
    t = 0;
    breakTime1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    breakResp1.keys = undefined;
    breakResp1.rt = undefined;
    _breakResp1_allKeys = [];
    // keep track of which components have finished
    breakTime1Components = [];
    breakTime1Components.push(breakText1);
    breakTime1Components.push(breakResp1);
    
    for (const thisComponent of breakTime1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function breakTime1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'breakTime1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = breakTime1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *breakText1* updates
    if (t >= 0.0 && breakText1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breakText1.tStart = t;  // (not accounting for frame time here)
      breakText1.frameNStart = frameN;  // exact frame index
      
      breakText1.setAutoDraw(true);
    }

    
    // *breakResp1* updates
    if (t >= 0.0 && breakResp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breakResp1.tStart = t;  // (not accounting for frame time here)
      breakResp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { breakResp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { breakResp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { breakResp1.clearEvents(); });
    }

    if (breakResp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = breakResp1.getKeys({keyList: ['space'], waitRelease: false});
      _breakResp1_allKeys = _breakResp1_allKeys.concat(theseKeys);
      if (_breakResp1_allKeys.length > 0) {
        breakResp1.keys = _breakResp1_allKeys[_breakResp1_allKeys.length - 1].name;  // just the last key pressed
        breakResp1.rt = _breakResp1_allKeys[_breakResp1_allKeys.length - 1].rt;
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
    for (const thisComponent of breakTime1Components)
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


function breakTime1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'breakTime1'-------
    for (const thisComponent of breakTime1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('breakResp1.keys', breakResp1.keys);
    if (typeof breakResp1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('breakResp1.rt', breakResp1.rt);
        routineTimer.reset();
        }
    
    breakResp1.stop();
    // the Routine "breakTime1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _trial2Resp_allKeys;
var trial2Components;
function trial2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial2'-------
    t = 0;
    trial2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    trial2L11.setPos([loc1, loc2]);
    trial2L12.setPos([loc3, loc4]);
    trial2L21.setPos([loc5, loc6]);
    trial2L22.setPos([loc7, loc8]);
    trial2T11.setPos([loc9, loc10]);
    trial2T12.setPos([loc11, loc12]);
    trial2L13.setPos([loc13, loc14]);
    trial2L14.setPos([loc15, loc16]);
    trial2L23.setPos([loc17, loc18]);
    trial2L24.setPos([loc19, loc20]);
    trial2T13.setPos([loc21, loc22]);
    trial2T14.setPos([loc23, loc24]);
    trial2L15.setPos([loc25, loc26]);
    trial2L16.setPos([loc27, loc28]);
    trial2L25.setPos([loc29, loc30]);
    trial2L26.setPos([loc31, loc32]);
    trial2T15.setPos([loc33, loc34]);
    trial2T16.setPos([loc35, loc36]);
    trial2TT.setPos([loc37, loc38]);
    trial2Resp.keys = undefined;
    trial2Resp.rt = undefined;
    _trial2Resp_allKeys = [];
    // keep track of which components have finished
    trial2Components = [];
    trial2Components.push(trial2Fix);
    trial2Components.push(trial2L11);
    trial2Components.push(trial2L12);
    trial2Components.push(trial2L21);
    trial2Components.push(trial2L22);
    trial2Components.push(trial2T11);
    trial2Components.push(trial2T12);
    trial2Components.push(trial2L13);
    trial2Components.push(trial2L14);
    trial2Components.push(trial2L23);
    trial2Components.push(trial2L24);
    trial2Components.push(trial2T13);
    trial2Components.push(trial2T14);
    trial2Components.push(trial2L15);
    trial2Components.push(trial2L16);
    trial2Components.push(trial2L25);
    trial2Components.push(trial2L26);
    trial2Components.push(trial2T15);
    trial2Components.push(trial2T16);
    trial2Components.push(trial2TT);
    trial2Components.push(trial2Resp);
    
    for (const thisComponent of trial2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trial2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial2Fix* updates
    if (t >= 0.0 && trial2Fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2Fix.tStart = t;  // (not accounting for frame time here)
      trial2Fix.frameNStart = frameN;  // exact frame index
      
      trial2Fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial2Fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial2Fix.setAutoDraw(false);
    }
    
    // *trial2L11* updates
    if (t >= 1.0 && trial2L11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L11.tStart = t;  // (not accounting for frame time here)
      trial2L11.frameNStart = frameN;  // exact frame index
      
      trial2L11.setAutoDraw(true);
    }

    
    // *trial2L12* updates
    if (t >= 1.0 && trial2L12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L12.tStart = t;  // (not accounting for frame time here)
      trial2L12.frameNStart = frameN;  // exact frame index
      
      trial2L12.setAutoDraw(true);
    }

    
    // *trial2L21* updates
    if (t >= 1.0 && trial2L21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L21.tStart = t;  // (not accounting for frame time here)
      trial2L21.frameNStart = frameN;  // exact frame index
      
      trial2L21.setAutoDraw(true);
    }

    
    // *trial2L22* updates
    if (t >= 1.0 && trial2L22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L22.tStart = t;  // (not accounting for frame time here)
      trial2L22.frameNStart = frameN;  // exact frame index
      
      trial2L22.setAutoDraw(true);
    }

    
    // *trial2T11* updates
    if (t >= 1.0 && trial2T11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2T11.tStart = t;  // (not accounting for frame time here)
      trial2T11.frameNStart = frameN;  // exact frame index
      
      trial2T11.setAutoDraw(true);
    }

    
    // *trial2T12* updates
    if (t >= 1.0 && trial2T12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2T12.tStart = t;  // (not accounting for frame time here)
      trial2T12.frameNStart = frameN;  // exact frame index
      
      trial2T12.setAutoDraw(true);
    }

    
    // *trial2L13* updates
    if (t >= 1.0 && trial2L13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L13.tStart = t;  // (not accounting for frame time here)
      trial2L13.frameNStart = frameN;  // exact frame index
      
      trial2L13.setAutoDraw(true);
    }

    
    // *trial2L14* updates
    if (t >= 1.0 && trial2L14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L14.tStart = t;  // (not accounting for frame time here)
      trial2L14.frameNStart = frameN;  // exact frame index
      
      trial2L14.setAutoDraw(true);
    }

    
    // *trial2L23* updates
    if (t >= 1.0 && trial2L23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L23.tStart = t;  // (not accounting for frame time here)
      trial2L23.frameNStart = frameN;  // exact frame index
      
      trial2L23.setAutoDraw(true);
    }

    
    // *trial2L24* updates
    if (t >= 1.0 && trial2L24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L24.tStart = t;  // (not accounting for frame time here)
      trial2L24.frameNStart = frameN;  // exact frame index
      
      trial2L24.setAutoDraw(true);
    }

    
    // *trial2T13* updates
    if (t >= 1.0 && trial2T13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2T13.tStart = t;  // (not accounting for frame time here)
      trial2T13.frameNStart = frameN;  // exact frame index
      
      trial2T13.setAutoDraw(true);
    }

    
    // *trial2T14* updates
    if (t >= 1.0 && trial2T14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2T14.tStart = t;  // (not accounting for frame time here)
      trial2T14.frameNStart = frameN;  // exact frame index
      
      trial2T14.setAutoDraw(true);
    }

    
    // *trial2L15* updates
    if (t >= 1.0 && trial2L15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L15.tStart = t;  // (not accounting for frame time here)
      trial2L15.frameNStart = frameN;  // exact frame index
      
      trial2L15.setAutoDraw(true);
    }

    
    // *trial2L16* updates
    if (t >= 1.0 && trial2L16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L16.tStart = t;  // (not accounting for frame time here)
      trial2L16.frameNStart = frameN;  // exact frame index
      
      trial2L16.setAutoDraw(true);
    }

    
    // *trial2L25* updates
    if (t >= 1.0 && trial2L25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L25.tStart = t;  // (not accounting for frame time here)
      trial2L25.frameNStart = frameN;  // exact frame index
      
      trial2L25.setAutoDraw(true);
    }

    
    // *trial2L26* updates
    if (t >= 1.0 && trial2L26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2L26.tStart = t;  // (not accounting for frame time here)
      trial2L26.frameNStart = frameN;  // exact frame index
      
      trial2L26.setAutoDraw(true);
    }

    
    // *trial2T15* updates
    if (t >= 1.0 && trial2T15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2T15.tStart = t;  // (not accounting for frame time here)
      trial2T15.frameNStart = frameN;  // exact frame index
      
      trial2T15.setAutoDraw(true);
    }

    
    // *trial2T16* updates
    if (t >= 1.0 && trial2T16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2T16.tStart = t;  // (not accounting for frame time here)
      trial2T16.frameNStart = frameN;  // exact frame index
      
      trial2T16.setAutoDraw(true);
    }

    
    // *trial2TT* updates
    if (t >= 1.0 && trial2TT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2TT.tStart = t;  // (not accounting for frame time here)
      trial2TT.frameNStart = frameN;  // exact frame index
      
      trial2TT.setAutoDraw(true);
    }

    
    // *trial2Resp* updates
    if (t >= 1.0 && trial2Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial2Resp.tStart = t;  // (not accounting for frame time here)
      trial2Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trial2Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trial2Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trial2Resp.clearEvents(); });
    }

    if (trial2Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = trial2Resp.getKeys({keyList: ['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease: false});
      _trial2Resp_allKeys = _trial2Resp_allKeys.concat(theseKeys);
      if (_trial2Resp_allKeys.length > 0) {
        trial2Resp.keys = _trial2Resp_allKeys[_trial2Resp_allKeys.length - 1].name;  // just the last key pressed
        trial2Resp.rt = _trial2Resp_allKeys[_trial2Resp_allKeys.length - 1].rt;
        // was this correct?
        if (trial2Resp.keys == corrAns) {
            trial2Resp.corr = 1;
        } else {
            trial2Resp.corr = 0;
        }
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
    for (const thisComponent of trial2Components)
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


function trial2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial2'-------
    for (const thisComponent of trial2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (trial2Resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         trial2Resp.corr = 1;  // correct non-response
      } else {
         trial2Resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('trial2Resp.keys', trial2Resp.keys);
    psychoJS.experiment.addData('trial2Resp.corr', trial2Resp.corr);
    if (typeof trial2Resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trial2Resp.rt', trial2Resp.rt);
        routineTimer.reset();
        }
    
    trial2Resp.stop();
    // the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _breakResp2_allKeys;
var breakTime2Components;
function breakTime2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'breakTime2'-------
    t = 0;
    breakTime2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    breakResp2.keys = undefined;
    breakResp2.rt = undefined;
    _breakResp2_allKeys = [];
    // keep track of which components have finished
    breakTime2Components = [];
    breakTime2Components.push(breakText2);
    breakTime2Components.push(breakResp2);
    
    for (const thisComponent of breakTime2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function breakTime2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'breakTime2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = breakTime2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *breakText2* updates
    if (t >= 0.0 && breakText2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breakText2.tStart = t;  // (not accounting for frame time here)
      breakText2.frameNStart = frameN;  // exact frame index
      
      breakText2.setAutoDraw(true);
    }

    
    // *breakResp2* updates
    if (t >= 0.0 && breakResp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breakResp2.tStart = t;  // (not accounting for frame time here)
      breakResp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { breakResp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { breakResp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { breakResp2.clearEvents(); });
    }

    if (breakResp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = breakResp2.getKeys({keyList: ['space'], waitRelease: false});
      _breakResp2_allKeys = _breakResp2_allKeys.concat(theseKeys);
      if (_breakResp2_allKeys.length > 0) {
        breakResp2.keys = _breakResp2_allKeys[_breakResp2_allKeys.length - 1].name;  // just the last key pressed
        breakResp2.rt = _breakResp2_allKeys[_breakResp2_allKeys.length - 1].rt;
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
    for (const thisComponent of breakTime2Components)
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


function breakTime2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'breakTime2'-------
    for (const thisComponent of breakTime2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('breakResp2.keys', breakResp2.keys);
    if (typeof breakResp2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('breakResp2.rt', breakResp2.rt);
        routineTimer.reset();
        }
    
    breakResp2.stop();
    // the Routine "breakTime2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _trial3Resp_allKeys;
var trial3Components;
function trial3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial3'-------
    t = 0;
    trial3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    trial3L11.setPos([loc1, loc2]);
    trial3L12.setPos([loc3, loc4]);
    trial3L21.setPos([loc5, loc6]);
    trial3L22.setPos([loc7, loc8]);
    trial3T11.setPos([loc9, loc10]);
    trial3T12.setPos([loc11, loc12]);
    trial3L13.setPos([loc13, loc14]);
    trial3L14.setPos([loc15, loc16]);
    trial3L23.setPos([loc17, loc18]);
    trial3L24.setPos([loc19, loc20]);
    trial3T13.setPos([loc21, loc22]);
    trial3T14.setPos([loc23, loc24]);
    trial3L15.setPos([loc25, loc26]);
    trial3L16.setPos([loc27, loc28]);
    trial3L25.setPos([loc29, loc30]);
    trial3L26.setPos([loc31, loc32]);
    trial3T15.setPos([loc33, loc34]);
    trial3T16.setPos([loc35, loc36]);
    trial3TT.setPos([loc37, loc38]);
    trial3Resp.keys = undefined;
    trial3Resp.rt = undefined;
    _trial3Resp_allKeys = [];
    // keep track of which components have finished
    trial3Components = [];
    trial3Components.push(trial3Fix);
    trial3Components.push(trial3L11);
    trial3Components.push(trial3L12);
    trial3Components.push(trial3L21);
    trial3Components.push(trial3L22);
    trial3Components.push(trial3T11);
    trial3Components.push(trial3T12);
    trial3Components.push(trial3L13);
    trial3Components.push(trial3L14);
    trial3Components.push(trial3L23);
    trial3Components.push(trial3L24);
    trial3Components.push(trial3T13);
    trial3Components.push(trial3T14);
    trial3Components.push(trial3L15);
    trial3Components.push(trial3L16);
    trial3Components.push(trial3L25);
    trial3Components.push(trial3L26);
    trial3Components.push(trial3T15);
    trial3Components.push(trial3T16);
    trial3Components.push(trial3TT);
    trial3Components.push(trial3Resp);
    
    for (const thisComponent of trial3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trial3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial3Fix* updates
    if (t >= 0.0 && trial3Fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3Fix.tStart = t;  // (not accounting for frame time here)
      trial3Fix.frameNStart = frameN;  // exact frame index
      
      trial3Fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial3Fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial3Fix.setAutoDraw(false);
    }
    
    // *trial3L11* updates
    if (t >= 1.0 && trial3L11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L11.tStart = t;  // (not accounting for frame time here)
      trial3L11.frameNStart = frameN;  // exact frame index
      
      trial3L11.setAutoDraw(true);
    }

    
    // *trial3L12* updates
    if (t >= 1.0 && trial3L12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L12.tStart = t;  // (not accounting for frame time here)
      trial3L12.frameNStart = frameN;  // exact frame index
      
      trial3L12.setAutoDraw(true);
    }

    
    // *trial3L21* updates
    if (t >= 1.0 && trial3L21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L21.tStart = t;  // (not accounting for frame time here)
      trial3L21.frameNStart = frameN;  // exact frame index
      
      trial3L21.setAutoDraw(true);
    }

    
    // *trial3L22* updates
    if (t >= 1.0 && trial3L22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L22.tStart = t;  // (not accounting for frame time here)
      trial3L22.frameNStart = frameN;  // exact frame index
      
      trial3L22.setAutoDraw(true);
    }

    
    // *trial3T11* updates
    if (t >= 1.0 && trial3T11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3T11.tStart = t;  // (not accounting for frame time here)
      trial3T11.frameNStart = frameN;  // exact frame index
      
      trial3T11.setAutoDraw(true);
    }

    
    // *trial3T12* updates
    if (t >= 1.0 && trial3T12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3T12.tStart = t;  // (not accounting for frame time here)
      trial3T12.frameNStart = frameN;  // exact frame index
      
      trial3T12.setAutoDraw(true);
    }

    
    // *trial3L13* updates
    if (t >= 1.0 && trial3L13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L13.tStart = t;  // (not accounting for frame time here)
      trial3L13.frameNStart = frameN;  // exact frame index
      
      trial3L13.setAutoDraw(true);
    }

    
    // *trial3L14* updates
    if (t >= 1.0 && trial3L14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L14.tStart = t;  // (not accounting for frame time here)
      trial3L14.frameNStart = frameN;  // exact frame index
      
      trial3L14.setAutoDraw(true);
    }

    
    // *trial3L23* updates
    if (t >= 1.0 && trial3L23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L23.tStart = t;  // (not accounting for frame time here)
      trial3L23.frameNStart = frameN;  // exact frame index
      
      trial3L23.setAutoDraw(true);
    }

    
    // *trial3L24* updates
    if (t >= 1.0 && trial3L24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L24.tStart = t;  // (not accounting for frame time here)
      trial3L24.frameNStart = frameN;  // exact frame index
      
      trial3L24.setAutoDraw(true);
    }

    
    // *trial3T13* updates
    if (t >= 1.0 && trial3T13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3T13.tStart = t;  // (not accounting for frame time here)
      trial3T13.frameNStart = frameN;  // exact frame index
      
      trial3T13.setAutoDraw(true);
    }

    
    // *trial3T14* updates
    if (t >= 1.0 && trial3T14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3T14.tStart = t;  // (not accounting for frame time here)
      trial3T14.frameNStart = frameN;  // exact frame index
      
      trial3T14.setAutoDraw(true);
    }

    
    // *trial3L15* updates
    if (t >= 1.0 && trial3L15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L15.tStart = t;  // (not accounting for frame time here)
      trial3L15.frameNStart = frameN;  // exact frame index
      
      trial3L15.setAutoDraw(true);
    }

    
    // *trial3L16* updates
    if (t >= 1.0 && trial3L16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L16.tStart = t;  // (not accounting for frame time here)
      trial3L16.frameNStart = frameN;  // exact frame index
      
      trial3L16.setAutoDraw(true);
    }

    
    // *trial3L25* updates
    if (t >= 1.0 && trial3L25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L25.tStart = t;  // (not accounting for frame time here)
      trial3L25.frameNStart = frameN;  // exact frame index
      
      trial3L25.setAutoDraw(true);
    }

    
    // *trial3L26* updates
    if (t >= 1.0 && trial3L26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3L26.tStart = t;  // (not accounting for frame time here)
      trial3L26.frameNStart = frameN;  // exact frame index
      
      trial3L26.setAutoDraw(true);
    }

    
    // *trial3T15* updates
    if (t >= 1.0 && trial3T15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3T15.tStart = t;  // (not accounting for frame time here)
      trial3T15.frameNStart = frameN;  // exact frame index
      
      trial3T15.setAutoDraw(true);
    }

    
    // *trial3T16* updates
    if (t >= 1.0 && trial3T16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3T16.tStart = t;  // (not accounting for frame time here)
      trial3T16.frameNStart = frameN;  // exact frame index
      
      trial3T16.setAutoDraw(true);
    }

    
    // *trial3TT* updates
    if (t >= 1.0 && trial3TT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3TT.tStart = t;  // (not accounting for frame time here)
      trial3TT.frameNStart = frameN;  // exact frame index
      
      trial3TT.setAutoDraw(true);
    }

    
    // *trial3Resp* updates
    if (t >= 1.0 && trial3Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial3Resp.tStart = t;  // (not accounting for frame time here)
      trial3Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trial3Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trial3Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trial3Resp.clearEvents(); });
    }

    if (trial3Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = trial3Resp.getKeys({keyList: ['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease: false});
      _trial3Resp_allKeys = _trial3Resp_allKeys.concat(theseKeys);
      if (_trial3Resp_allKeys.length > 0) {
        trial3Resp.keys = _trial3Resp_allKeys[_trial3Resp_allKeys.length - 1].name;  // just the last key pressed
        trial3Resp.rt = _trial3Resp_allKeys[_trial3Resp_allKeys.length - 1].rt;
        // was this correct?
        if (trial3Resp.keys == corrAns) {
            trial3Resp.corr = 1;
        } else {
            trial3Resp.corr = 0;
        }
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
    for (const thisComponent of trial3Components)
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


function trial3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial3'-------
    for (const thisComponent of trial3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (trial3Resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         trial3Resp.corr = 1;  // correct non-response
      } else {
         trial3Resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('trial3Resp.keys', trial3Resp.keys);
    psychoJS.experiment.addData('trial3Resp.corr', trial3Resp.corr);
    if (typeof trial3Resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trial3Resp.rt', trial3Resp.rt);
        routineTimer.reset();
        }
    
    trial3Resp.stop();
    // the Routine "trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var endComponents;
function endRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(thanks);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function endRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thanks* updates
    if (t >= 0.0 && thanks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thanks.tStart = t;  // (not accounting for frame time here)
      thanks.frameNStart = frameN;  // exact frame index
      
      thanks.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (thanks.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      thanks.setAutoDraw(false);
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
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end'-------
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
