#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on June 10, 2020, at 14:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'vSearchAlpha5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\v-search-alpha5\\vSearchAlpha5_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction1"
instruction1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text="In this task you will see sets of shapes made of four different shapes as outlined below. Only press the 's' key if you see the “T” shape, which is the last shape. Otherwise, press the 'k' key. There will be 6, 12, or 18 shapes to observe in each trial. Press space to continue.",
    font='Arial',
    pos=[0,0.15], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp1 = keyboard.Keyboard()
l1ex = visual.ImageStim(
    win=win,
    name='l1ex', 
    image='L1.png', mask=None,
    ori=0, pos=(-0.3, -0.15), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
l2ex = visual.ImageStim(
    win=win,
    name='l2ex', 
    image='L2.png', mask=None,
    ori=0, pos=(-0.1, -0.15), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
t1ex = visual.ImageStim(
    win=win,
    name='t1ex', 
    image='T1.png', mask=None,
    ori=0, pos=(0.1, -0.15), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tTex = visual.ImageStim(
    win=win,
    name='tTex', 
    image='TT.png', mask=None,
    ori=0, pos=(0.3, -0.15), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
trial1Fix = visual.TextStim(win=win, name='trial1Fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial1L11 = visual.ImageStim(
    win=win,
    name='trial1L11', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial1L12 = visual.ImageStim(
    win=win,
    name='trial1L12', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trial1L21 = visual.ImageStim(
    win=win,
    name='trial1L21', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trial1L22 = visual.ImageStim(
    win=win,
    name='trial1L22', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trial1T11 = visual.ImageStim(
    win=win,
    name='trial1T11', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trial1T12 = visual.ImageStim(
    win=win,
    name='trial1T12', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trial1L13 = visual.ImageStim(
    win=win,
    name='trial1L13', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trial1L14 = visual.ImageStim(
    win=win,
    name='trial1L14', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
trial1L23 = visual.ImageStim(
    win=win,
    name='trial1L23', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
trial1L24 = visual.ImageStim(
    win=win,
    name='trial1L24', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
trial1T13 = visual.ImageStim(
    win=win,
    name='trial1T13', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
trial1T14 = visual.ImageStim(
    win=win,
    name='trial1T14', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
trial1L15 = visual.ImageStim(
    win=win,
    name='trial1L15', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
trial1L16 = visual.ImageStim(
    win=win,
    name='trial1L16', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
trial1L25 = visual.ImageStim(
    win=win,
    name='trial1L25', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
trial1L26 = visual.ImageStim(
    win=win,
    name='trial1L26', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
trial1T15 = visual.ImageStim(
    win=win,
    name='trial1T15', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
trial1T16 = visual.ImageStim(
    win=win,
    name='trial1T16', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
trial1TT = visual.ImageStim(
    win=win,
    name='trial1TT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
trial1Resp = keyboard.Keyboard()

# Initialize components for Routine "breakTime1"
breakTime1Clock = core.Clock()
breakText1 = visual.TextStim(win=win, name='breakText1',
    text="A quick break before the next set of trials. Remember, only press the 's' key if you see the “T” shape, which is the last shape. Otherwise, press the 'k' key. There will be 6, 12, or 18 shapes to observe in each trial. Press space to continue.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
breakResp1 = keyboard.Keyboard()

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
trial2Fix = visual.TextStim(win=win, name='trial2Fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial2L11 = visual.ImageStim(
    win=win,
    name='trial2L11', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial2L12 = visual.ImageStim(
    win=win,
    name='trial2L12', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trial2L21 = visual.ImageStim(
    win=win,
    name='trial2L21', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trial2L22 = visual.ImageStim(
    win=win,
    name='trial2L22', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trial2T11 = visual.ImageStim(
    win=win,
    name='trial2T11', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trial2T12 = visual.ImageStim(
    win=win,
    name='trial2T12', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trial2L13 = visual.ImageStim(
    win=win,
    name='trial2L13', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trial2L14 = visual.ImageStim(
    win=win,
    name='trial2L14', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
trial2L23 = visual.ImageStim(
    win=win,
    name='trial2L23', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
trial2L24 = visual.ImageStim(
    win=win,
    name='trial2L24', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
trial2T13 = visual.ImageStim(
    win=win,
    name='trial2T13', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
trial2T14 = visual.ImageStim(
    win=win,
    name='trial2T14', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
trial2L15 = visual.ImageStim(
    win=win,
    name='trial2L15', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
trial2L16 = visual.ImageStim(
    win=win,
    name='trial2L16', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
trial2L25 = visual.ImageStim(
    win=win,
    name='trial2L25', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
trial2L26 = visual.ImageStim(
    win=win,
    name='trial2L26', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
trial2T15 = visual.ImageStim(
    win=win,
    name='trial2T15', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
trial2T16 = visual.ImageStim(
    win=win,
    name='trial2T16', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
trial2TT = visual.ImageStim(
    win=win,
    name='trial2TT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
trial2Resp = keyboard.Keyboard()

# Initialize components for Routine "breakTime2"
breakTime2Clock = core.Clock()
breakText2 = visual.TextStim(win=win, name='breakText2',
    text="A quick break before the next set of trials. Remember, only press the 's' key if you see the “T” shape, which is the last shape. Otherwise, press the 'k' key. There will be 6, 12, or 18 shapes to observe in each trial. Press space to continue.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
breakResp2 = keyboard.Keyboard()

# Initialize components for Routine "trial3"
trial3Clock = core.Clock()
trial3Fix = visual.TextStim(win=win, name='trial3Fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial3L11 = visual.ImageStim(
    win=win,
    name='trial3L11', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial3L12 = visual.ImageStim(
    win=win,
    name='trial3L12', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trial3L21 = visual.ImageStim(
    win=win,
    name='trial3L21', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trial3L22 = visual.ImageStim(
    win=win,
    name='trial3L22', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trial3T11 = visual.ImageStim(
    win=win,
    name='trial3T11', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trial3T12 = visual.ImageStim(
    win=win,
    name='trial3T12', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trial3L13 = visual.ImageStim(
    win=win,
    name='trial3L13', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trial3L14 = visual.ImageStim(
    win=win,
    name='trial3L14', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
trial3L23 = visual.ImageStim(
    win=win,
    name='trial3L23', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
trial3L24 = visual.ImageStim(
    win=win,
    name='trial3L24', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
trial3T13 = visual.ImageStim(
    win=win,
    name='trial3T13', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
trial3T14 = visual.ImageStim(
    win=win,
    name='trial3T14', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
trial3L15 = visual.ImageStim(
    win=win,
    name='trial3L15', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
trial3L16 = visual.ImageStim(
    win=win,
    name='trial3L16', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
trial3L25 = visual.ImageStim(
    win=win,
    name='trial3L25', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
trial3L26 = visual.ImageStim(
    win=win,
    name='trial3L26', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
trial3T15 = visual.ImageStim(
    win=win,
    name='trial3T15', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
trial3T16 = visual.ImageStim(
    win=win,
    name='trial3T16', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
trial3TT = visual.ImageStim(
    win=win,
    name='trial3TT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
trial3Resp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='This is the end of the experiment.\nThank you for your time.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction1"-------
continueRoutine = True
# update component parameters for each repeat
keyResp1.keys = []
keyResp1.rt = []
_keyResp1_allKeys = []
# keep track of which components have finished
instruction1Components = [instr1, keyResp1, l1ex, l2ex, t1ex, tTex]
for thisComponent in instruction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction1"-------
while continueRoutine:
    # get current time
    t = instruction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *keyResp1* updates
    waitOnFlip = False
    if keyResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp1.frameNStart = frameN  # exact frame index
        keyResp1.tStart = t  # local t and not account for scr refresh
        keyResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp1, 'tStartRefresh')  # time at next scr refresh
        keyResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['space'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *l1ex* updates
    if l1ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l1ex.frameNStart = frameN  # exact frame index
        l1ex.tStart = t  # local t and not account for scr refresh
        l1ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l1ex, 'tStartRefresh')  # time at next scr refresh
        l1ex.setAutoDraw(True)
    
    # *l2ex* updates
    if l2ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l2ex.frameNStart = frameN  # exact frame index
        l2ex.tStart = t  # local t and not account for scr refresh
        l2ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l2ex, 'tStartRefresh')  # time at next scr refresh
        l2ex.setAutoDraw(True)
    
    # *t1ex* updates
    if t1ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        t1ex.frameNStart = frameN  # exact frame index
        t1ex.tStart = t  # local t and not account for scr refresh
        t1ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(t1ex, 'tStartRefresh')  # time at next scr refresh
        t1ex.setAutoDraw(True)
    
    # *tTex* updates
    if tTex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tTex.frameNStart = frameN  # exact frame index
        tTex.tStart = t  # local t and not account for scr refresh
        tTex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tTex, 'tStartRefresh')  # time at next scr refresh
        tTex.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction1"-------
for thisComponent in instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# check responses
if keyResp1.keys in ['', [], None]:  # No response was made
    keyResp1.keys = None
thisExp.addData('keyResp1.keys',keyResp1.keys)
if keyResp1.keys != None:  # we had a response
    thisExp.addData('keyResp1.rt', keyResp1.rt)
thisExp.addData('keyResp1.started', keyResp1.tStartRefresh)
thisExp.addData('keyResp1.stopped', keyResp1.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('l1ex.started', l1ex.tStartRefresh)
thisExp.addData('l1ex.stopped', l1ex.tStopRefresh)
thisExp.addData('l2ex.started', l2ex.tStartRefresh)
thisExp.addData('l2ex.stopped', l2ex.tStopRefresh)
thisExp.addData('t1ex.started', t1ex.tStartRefresh)
thisExp.addData('t1ex.stopped', t1ex.tStopRefresh)
thisExp.addData('tTex.started', tTex.tStartRefresh)
thisExp.addData('tTex.stopped', tTex.tStopRefresh)
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchCond1.xlsx'),
    seed=None, name='trials1')
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1:
        exec('{} = thisTrials1[paramName]'.format(paramName))

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            exec('{} = thisTrials1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial1L11.setPos([loc1,loc2])
    trial1L12.setPos([loc3,loc4])
    trial1L21.setPos([loc5,loc6])
    trial1L22.setPos([loc7,loc8])
    trial1T11.setPos([loc9,loc10])
    trial1T12.setPos([loc11,loc12])
    trial1L13.setPos((loc13, loc14))
    trial1L14.setPos((loc15, loc16))
    trial1L23.setPos((loc17, loc18))
    trial1L24.setPos((loc19, loc20))
    trial1T13.setPos((loc21, loc22))
    trial1T14.setPos((loc23, loc24))
    trial1L15.setPos((loc25, loc26))
    trial1L16.setPos((loc27, loc28))
    trial1L25.setPos((loc29, loc30))
    trial1L26.setPos((loc31, loc32))
    trial1T15.setPos((loc33, loc34))
    trial1T16.setPos((loc35, loc36))
    trial1TT.setPos([loc37,loc38])
    trial1Resp.keys = []
    trial1Resp.rt = []
    _trial1Resp_allKeys = []
    # keep track of which components have finished
    trial1Components = [trial1Fix, trial1L11, trial1L12, trial1L21, trial1L22, trial1T11, trial1T12, trial1L13, trial1L14, trial1L23, trial1L24, trial1T13, trial1T14, trial1L15, trial1L16, trial1L25, trial1L26, trial1T15, trial1T16, trial1TT, trial1Resp]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial1Fix* updates
        if trial1Fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Fix.frameNStart = frameN  # exact frame index
            trial1Fix.tStart = t  # local t and not account for scr refresh
            trial1Fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Fix, 'tStartRefresh')  # time at next scr refresh
            trial1Fix.setAutoDraw(True)
        if trial1Fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1Fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1Fix.tStop = t  # not accounting for scr refresh
                trial1Fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1Fix, 'tStopRefresh')  # time at next scr refresh
                trial1Fix.setAutoDraw(False)
        
        # *trial1L11* updates
        if trial1L11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L11.frameNStart = frameN  # exact frame index
            trial1L11.tStart = t  # local t and not account for scr refresh
            trial1L11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L11, 'tStartRefresh')  # time at next scr refresh
            trial1L11.setAutoDraw(True)
        
        # *trial1L12* updates
        if trial1L12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L12.frameNStart = frameN  # exact frame index
            trial1L12.tStart = t  # local t and not account for scr refresh
            trial1L12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L12, 'tStartRefresh')  # time at next scr refresh
            trial1L12.setAutoDraw(True)
        
        # *trial1L21* updates
        if trial1L21.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L21.frameNStart = frameN  # exact frame index
            trial1L21.tStart = t  # local t and not account for scr refresh
            trial1L21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L21, 'tStartRefresh')  # time at next scr refresh
            trial1L21.setAutoDraw(True)
        
        # *trial1L22* updates
        if trial1L22.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L22.frameNStart = frameN  # exact frame index
            trial1L22.tStart = t  # local t and not account for scr refresh
            trial1L22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L22, 'tStartRefresh')  # time at next scr refresh
            trial1L22.setAutoDraw(True)
        
        # *trial1T11* updates
        if trial1T11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1T11.frameNStart = frameN  # exact frame index
            trial1T11.tStart = t  # local t and not account for scr refresh
            trial1T11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1T11, 'tStartRefresh')  # time at next scr refresh
            trial1T11.setAutoDraw(True)
        
        # *trial1T12* updates
        if trial1T12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1T12.frameNStart = frameN  # exact frame index
            trial1T12.tStart = t  # local t and not account for scr refresh
            trial1T12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1T12, 'tStartRefresh')  # time at next scr refresh
            trial1T12.setAutoDraw(True)
        
        # *trial1L13* updates
        if trial1L13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L13.frameNStart = frameN  # exact frame index
            trial1L13.tStart = t  # local t and not account for scr refresh
            trial1L13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L13, 'tStartRefresh')  # time at next scr refresh
            trial1L13.setAutoDraw(True)
        
        # *trial1L14* updates
        if trial1L14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L14.frameNStart = frameN  # exact frame index
            trial1L14.tStart = t  # local t and not account for scr refresh
            trial1L14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L14, 'tStartRefresh')  # time at next scr refresh
            trial1L14.setAutoDraw(True)
        
        # *trial1L23* updates
        if trial1L23.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L23.frameNStart = frameN  # exact frame index
            trial1L23.tStart = t  # local t and not account for scr refresh
            trial1L23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L23, 'tStartRefresh')  # time at next scr refresh
            trial1L23.setAutoDraw(True)
        
        # *trial1L24* updates
        if trial1L24.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L24.frameNStart = frameN  # exact frame index
            trial1L24.tStart = t  # local t and not account for scr refresh
            trial1L24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L24, 'tStartRefresh')  # time at next scr refresh
            trial1L24.setAutoDraw(True)
        
        # *trial1T13* updates
        if trial1T13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1T13.frameNStart = frameN  # exact frame index
            trial1T13.tStart = t  # local t and not account for scr refresh
            trial1T13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1T13, 'tStartRefresh')  # time at next scr refresh
            trial1T13.setAutoDraw(True)
        
        # *trial1T14* updates
        if trial1T14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1T14.frameNStart = frameN  # exact frame index
            trial1T14.tStart = t  # local t and not account for scr refresh
            trial1T14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1T14, 'tStartRefresh')  # time at next scr refresh
            trial1T14.setAutoDraw(True)
        
        # *trial1L15* updates
        if trial1L15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L15.frameNStart = frameN  # exact frame index
            trial1L15.tStart = t  # local t and not account for scr refresh
            trial1L15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L15, 'tStartRefresh')  # time at next scr refresh
            trial1L15.setAutoDraw(True)
        
        # *trial1L16* updates
        if trial1L16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L16.frameNStart = frameN  # exact frame index
            trial1L16.tStart = t  # local t and not account for scr refresh
            trial1L16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L16, 'tStartRefresh')  # time at next scr refresh
            trial1L16.setAutoDraw(True)
        
        # *trial1L25* updates
        if trial1L25.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L25.frameNStart = frameN  # exact frame index
            trial1L25.tStart = t  # local t and not account for scr refresh
            trial1L25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L25, 'tStartRefresh')  # time at next scr refresh
            trial1L25.setAutoDraw(True)
        
        # *trial1L26* updates
        if trial1L26.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1L26.frameNStart = frameN  # exact frame index
            trial1L26.tStart = t  # local t and not account for scr refresh
            trial1L26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1L26, 'tStartRefresh')  # time at next scr refresh
            trial1L26.setAutoDraw(True)
        
        # *trial1T15* updates
        if trial1T15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1T15.frameNStart = frameN  # exact frame index
            trial1T15.tStart = t  # local t and not account for scr refresh
            trial1T15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1T15, 'tStartRefresh')  # time at next scr refresh
            trial1T15.setAutoDraw(True)
        
        # *trial1T16* updates
        if trial1T16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1T16.frameNStart = frameN  # exact frame index
            trial1T16.tStart = t  # local t and not account for scr refresh
            trial1T16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1T16, 'tStartRefresh')  # time at next scr refresh
            trial1T16.setAutoDraw(True)
        
        # *trial1TT* updates
        if trial1TT.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1TT.frameNStart = frameN  # exact frame index
            trial1TT.tStart = t  # local t and not account for scr refresh
            trial1TT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1TT, 'tStartRefresh')  # time at next scr refresh
            trial1TT.setAutoDraw(True)
        
        # *trial1Resp* updates
        waitOnFlip = False
        if trial1Resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Resp.frameNStart = frameN  # exact frame index
            trial1Resp.tStart = t  # local t and not account for scr refresh
            trial1Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Resp, 'tStartRefresh')  # time at next scr refresh
            trial1Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial1Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial1Resp.status == STARTED and not waitOnFlip:
            theseKeys = trial1Resp.getKeys(keyList=['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease=False)
            _trial1Resp_allKeys.extend(theseKeys)
            if len(_trial1Resp_allKeys):
                trial1Resp.keys = _trial1Resp_allKeys[-1].name  # just the last key pressed
                trial1Resp.rt = _trial1Resp_allKeys[-1].rt
                # was this correct?
                if (trial1Resp.keys == str(corrAns)) or (trial1Resp.keys == corrAns):
                    trial1Resp.corr = 1
                else:
                    trial1Resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials1.addData('trial1Fix.started', trial1Fix.tStartRefresh)
    trials1.addData('trial1Fix.stopped', trial1Fix.tStopRefresh)
    trials1.addData('trial1L11.started', trial1L11.tStartRefresh)
    trials1.addData('trial1L11.stopped', trial1L11.tStopRefresh)
    trials1.addData('trial1L12.started', trial1L12.tStartRefresh)
    trials1.addData('trial1L12.stopped', trial1L12.tStopRefresh)
    trials1.addData('trial1L21.started', trial1L21.tStartRefresh)
    trials1.addData('trial1L21.stopped', trial1L21.tStopRefresh)
    trials1.addData('trial1L22.started', trial1L22.tStartRefresh)
    trials1.addData('trial1L22.stopped', trial1L22.tStopRefresh)
    trials1.addData('trial1T11.started', trial1T11.tStartRefresh)
    trials1.addData('trial1T11.stopped', trial1T11.tStopRefresh)
    trials1.addData('trial1T12.started', trial1T12.tStartRefresh)
    trials1.addData('trial1T12.stopped', trial1T12.tStopRefresh)
    trials1.addData('trial1L13.started', trial1L13.tStartRefresh)
    trials1.addData('trial1L13.stopped', trial1L13.tStopRefresh)
    trials1.addData('trial1L14.started', trial1L14.tStartRefresh)
    trials1.addData('trial1L14.stopped', trial1L14.tStopRefresh)
    trials1.addData('trial1L23.started', trial1L23.tStartRefresh)
    trials1.addData('trial1L23.stopped', trial1L23.tStopRefresh)
    trials1.addData('trial1L24.started', trial1L24.tStartRefresh)
    trials1.addData('trial1L24.stopped', trial1L24.tStopRefresh)
    trials1.addData('trial1T13.started', trial1T13.tStartRefresh)
    trials1.addData('trial1T13.stopped', trial1T13.tStopRefresh)
    trials1.addData('trial1T14.started', trial1T14.tStartRefresh)
    trials1.addData('trial1T14.stopped', trial1T14.tStopRefresh)
    trials1.addData('trial1L15.started', trial1L15.tStartRefresh)
    trials1.addData('trial1L15.stopped', trial1L15.tStopRefresh)
    trials1.addData('trial1L16.started', trial1L16.tStartRefresh)
    trials1.addData('trial1L16.stopped', trial1L16.tStopRefresh)
    trials1.addData('trial1L25.started', trial1L25.tStartRefresh)
    trials1.addData('trial1L25.stopped', trial1L25.tStopRefresh)
    trials1.addData('trial1L26.started', trial1L26.tStartRefresh)
    trials1.addData('trial1L26.stopped', trial1L26.tStopRefresh)
    trials1.addData('trial1T15.started', trial1T15.tStartRefresh)
    trials1.addData('trial1T15.stopped', trial1T15.tStopRefresh)
    trials1.addData('trial1T16.started', trial1T16.tStartRefresh)
    trials1.addData('trial1T16.stopped', trial1T16.tStopRefresh)
    trials1.addData('trial1TT.started', trial1TT.tStartRefresh)
    trials1.addData('trial1TT.stopped', trial1TT.tStopRefresh)
    # check responses
    if trial1Resp.keys in ['', [], None]:  # No response was made
        trial1Resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial1Resp.corr = 1;  # correct non-response
        else:
           trial1Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials1 (TrialHandler)
    trials1.addData('trial1Resp.keys',trial1Resp.keys)
    trials1.addData('trial1Resp.corr', trial1Resp.corr)
    if trial1Resp.keys != None:  # we had a response
        trials1.addData('trial1Resp.rt', trial1Resp.rt)
    trials1.addData('trial1Resp.started', trial1Resp.tStartRefresh)
    trials1.addData('trial1Resp.stopped', trial1Resp.tStopRefresh)
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials1'


# ------Prepare to start Routine "breakTime1"-------
continueRoutine = True
# update component parameters for each repeat
breakResp1.keys = []
breakResp1.rt = []
_breakResp1_allKeys = []
# keep track of which components have finished
breakTime1Components = [breakText1, breakResp1]
for thisComponent in breakTime1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
breakTime1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "breakTime1"-------
while continueRoutine:
    # get current time
    t = breakTime1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=breakTime1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *breakText1* updates
    if breakText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakText1.frameNStart = frameN  # exact frame index
        breakText1.tStart = t  # local t and not account for scr refresh
        breakText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakText1, 'tStartRefresh')  # time at next scr refresh
        breakText1.setAutoDraw(True)
    
    # *breakResp1* updates
    waitOnFlip = False
    if breakResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakResp1.frameNStart = frameN  # exact frame index
        breakResp1.tStart = t  # local t and not account for scr refresh
        breakResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakResp1, 'tStartRefresh')  # time at next scr refresh
        breakResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(breakResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(breakResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if breakResp1.status == STARTED and not waitOnFlip:
        theseKeys = breakResp1.getKeys(keyList=['space'], waitRelease=False)
        _breakResp1_allKeys.extend(theseKeys)
        if len(_breakResp1_allKeys):
            breakResp1.keys = _breakResp1_allKeys[-1].name  # just the last key pressed
            breakResp1.rt = _breakResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in breakTime1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "breakTime1"-------
for thisComponent in breakTime1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('breakText1.started', breakText1.tStartRefresh)
thisExp.addData('breakText1.stopped', breakText1.tStopRefresh)
# check responses
if breakResp1.keys in ['', [], None]:  # No response was made
    breakResp1.keys = None
thisExp.addData('breakResp1.keys',breakResp1.keys)
if breakResp1.keys != None:  # we had a response
    thisExp.addData('breakResp1.rt', breakResp1.rt)
thisExp.addData('breakResp1.started', breakResp1.tStartRefresh)
thisExp.addData('breakResp1.stopped', breakResp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "breakTime1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchCond2.xlsx'),
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2:
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial2L11.setPos([loc1,loc2])
    trial2L12.setPos([loc3,loc4])
    trial2L21.setPos([loc5,loc6])
    trial2L22.setPos([loc7,loc8])
    trial2T11.setPos([loc9,loc10])
    trial2T12.setPos([loc11,loc12])
    trial2L13.setPos((loc13, loc14))
    trial2L14.setPos((loc15, loc16))
    trial2L23.setPos((loc17, loc18))
    trial2L24.setPos((loc19, loc20))
    trial2T13.setPos((loc21, loc22))
    trial2T14.setPos((loc23, loc24))
    trial2L15.setPos((loc25, loc26))
    trial2L16.setPos((loc27, loc28))
    trial2L25.setPos((loc29, loc30))
    trial2L26.setPos((loc31, loc32))
    trial2T15.setPos((loc33, loc34))
    trial2T16.setPos((loc35, loc36))
    trial2TT.setPos([loc37,loc38])
    trial2Resp.keys = []
    trial2Resp.rt = []
    _trial2Resp_allKeys = []
    # keep track of which components have finished
    trial2Components = [trial2Fix, trial2L11, trial2L12, trial2L21, trial2L22, trial2T11, trial2T12, trial2L13, trial2L14, trial2L23, trial2L24, trial2T13, trial2T14, trial2L15, trial2L16, trial2L25, trial2L26, trial2T15, trial2T16, trial2TT, trial2Resp]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial2"-------
    while continueRoutine:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial2Fix* updates
        if trial2Fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Fix.frameNStart = frameN  # exact frame index
            trial2Fix.tStart = t  # local t and not account for scr refresh
            trial2Fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Fix, 'tStartRefresh')  # time at next scr refresh
            trial2Fix.setAutoDraw(True)
        if trial2Fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2Fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2Fix.tStop = t  # not accounting for scr refresh
                trial2Fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2Fix, 'tStopRefresh')  # time at next scr refresh
                trial2Fix.setAutoDraw(False)
        
        # *trial2L11* updates
        if trial2L11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L11.frameNStart = frameN  # exact frame index
            trial2L11.tStart = t  # local t and not account for scr refresh
            trial2L11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L11, 'tStartRefresh')  # time at next scr refresh
            trial2L11.setAutoDraw(True)
        
        # *trial2L12* updates
        if trial2L12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L12.frameNStart = frameN  # exact frame index
            trial2L12.tStart = t  # local t and not account for scr refresh
            trial2L12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L12, 'tStartRefresh')  # time at next scr refresh
            trial2L12.setAutoDraw(True)
        
        # *trial2L21* updates
        if trial2L21.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L21.frameNStart = frameN  # exact frame index
            trial2L21.tStart = t  # local t and not account for scr refresh
            trial2L21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L21, 'tStartRefresh')  # time at next scr refresh
            trial2L21.setAutoDraw(True)
        
        # *trial2L22* updates
        if trial2L22.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L22.frameNStart = frameN  # exact frame index
            trial2L22.tStart = t  # local t and not account for scr refresh
            trial2L22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L22, 'tStartRefresh')  # time at next scr refresh
            trial2L22.setAutoDraw(True)
        
        # *trial2T11* updates
        if trial2T11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2T11.frameNStart = frameN  # exact frame index
            trial2T11.tStart = t  # local t and not account for scr refresh
            trial2T11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2T11, 'tStartRefresh')  # time at next scr refresh
            trial2T11.setAutoDraw(True)
        
        # *trial2T12* updates
        if trial2T12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2T12.frameNStart = frameN  # exact frame index
            trial2T12.tStart = t  # local t and not account for scr refresh
            trial2T12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2T12, 'tStartRefresh')  # time at next scr refresh
            trial2T12.setAutoDraw(True)
        
        # *trial2L13* updates
        if trial2L13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L13.frameNStart = frameN  # exact frame index
            trial2L13.tStart = t  # local t and not account for scr refresh
            trial2L13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L13, 'tStartRefresh')  # time at next scr refresh
            trial2L13.setAutoDraw(True)
        
        # *trial2L14* updates
        if trial2L14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L14.frameNStart = frameN  # exact frame index
            trial2L14.tStart = t  # local t and not account for scr refresh
            trial2L14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L14, 'tStartRefresh')  # time at next scr refresh
            trial2L14.setAutoDraw(True)
        
        # *trial2L23* updates
        if trial2L23.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L23.frameNStart = frameN  # exact frame index
            trial2L23.tStart = t  # local t and not account for scr refresh
            trial2L23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L23, 'tStartRefresh')  # time at next scr refresh
            trial2L23.setAutoDraw(True)
        
        # *trial2L24* updates
        if trial2L24.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L24.frameNStart = frameN  # exact frame index
            trial2L24.tStart = t  # local t and not account for scr refresh
            trial2L24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L24, 'tStartRefresh')  # time at next scr refresh
            trial2L24.setAutoDraw(True)
        
        # *trial2T13* updates
        if trial2T13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2T13.frameNStart = frameN  # exact frame index
            trial2T13.tStart = t  # local t and not account for scr refresh
            trial2T13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2T13, 'tStartRefresh')  # time at next scr refresh
            trial2T13.setAutoDraw(True)
        
        # *trial2T14* updates
        if trial2T14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2T14.frameNStart = frameN  # exact frame index
            trial2T14.tStart = t  # local t and not account for scr refresh
            trial2T14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2T14, 'tStartRefresh')  # time at next scr refresh
            trial2T14.setAutoDraw(True)
        
        # *trial2L15* updates
        if trial2L15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L15.frameNStart = frameN  # exact frame index
            trial2L15.tStart = t  # local t and not account for scr refresh
            trial2L15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L15, 'tStartRefresh')  # time at next scr refresh
            trial2L15.setAutoDraw(True)
        
        # *trial2L16* updates
        if trial2L16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L16.frameNStart = frameN  # exact frame index
            trial2L16.tStart = t  # local t and not account for scr refresh
            trial2L16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L16, 'tStartRefresh')  # time at next scr refresh
            trial2L16.setAutoDraw(True)
        
        # *trial2L25* updates
        if trial2L25.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L25.frameNStart = frameN  # exact frame index
            trial2L25.tStart = t  # local t and not account for scr refresh
            trial2L25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L25, 'tStartRefresh')  # time at next scr refresh
            trial2L25.setAutoDraw(True)
        
        # *trial2L26* updates
        if trial2L26.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2L26.frameNStart = frameN  # exact frame index
            trial2L26.tStart = t  # local t and not account for scr refresh
            trial2L26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2L26, 'tStartRefresh')  # time at next scr refresh
            trial2L26.setAutoDraw(True)
        
        # *trial2T15* updates
        if trial2T15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2T15.frameNStart = frameN  # exact frame index
            trial2T15.tStart = t  # local t and not account for scr refresh
            trial2T15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2T15, 'tStartRefresh')  # time at next scr refresh
            trial2T15.setAutoDraw(True)
        
        # *trial2T16* updates
        if trial2T16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2T16.frameNStart = frameN  # exact frame index
            trial2T16.tStart = t  # local t and not account for scr refresh
            trial2T16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2T16, 'tStartRefresh')  # time at next scr refresh
            trial2T16.setAutoDraw(True)
        
        # *trial2TT* updates
        if trial2TT.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2TT.frameNStart = frameN  # exact frame index
            trial2TT.tStart = t  # local t and not account for scr refresh
            trial2TT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2TT, 'tStartRefresh')  # time at next scr refresh
            trial2TT.setAutoDraw(True)
        
        # *trial2Resp* updates
        waitOnFlip = False
        if trial2Resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Resp.frameNStart = frameN  # exact frame index
            trial2Resp.tStart = t  # local t and not account for scr refresh
            trial2Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Resp, 'tStartRefresh')  # time at next scr refresh
            trial2Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial2Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial2Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial2Resp.status == STARTED and not waitOnFlip:
            theseKeys = trial2Resp.getKeys(keyList=['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease=False)
            _trial2Resp_allKeys.extend(theseKeys)
            if len(_trial2Resp_allKeys):
                trial2Resp.keys = _trial2Resp_allKeys[-1].name  # just the last key pressed
                trial2Resp.rt = _trial2Resp_allKeys[-1].rt
                # was this correct?
                if (trial2Resp.keys == str(corrAns)) or (trial2Resp.keys == corrAns):
                    trial2Resp.corr = 1
                else:
                    trial2Resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials2.addData('trial2Fix.started', trial2Fix.tStartRefresh)
    trials2.addData('trial2Fix.stopped', trial2Fix.tStopRefresh)
    trials2.addData('trial2L11.started', trial2L11.tStartRefresh)
    trials2.addData('trial2L11.stopped', trial2L11.tStopRefresh)
    trials2.addData('trial2L12.started', trial2L12.tStartRefresh)
    trials2.addData('trial2L12.stopped', trial2L12.tStopRefresh)
    trials2.addData('trial2L21.started', trial2L21.tStartRefresh)
    trials2.addData('trial2L21.stopped', trial2L21.tStopRefresh)
    trials2.addData('trial2L22.started', trial2L22.tStartRefresh)
    trials2.addData('trial2L22.stopped', trial2L22.tStopRefresh)
    trials2.addData('trial2T11.started', trial2T11.tStartRefresh)
    trials2.addData('trial2T11.stopped', trial2T11.tStopRefresh)
    trials2.addData('trial2T12.started', trial2T12.tStartRefresh)
    trials2.addData('trial2T12.stopped', trial2T12.tStopRefresh)
    trials2.addData('trial2L13.started', trial2L13.tStartRefresh)
    trials2.addData('trial2L13.stopped', trial2L13.tStopRefresh)
    trials2.addData('trial2L14.started', trial2L14.tStartRefresh)
    trials2.addData('trial2L14.stopped', trial2L14.tStopRefresh)
    trials2.addData('trial2L23.started', trial2L23.tStartRefresh)
    trials2.addData('trial2L23.stopped', trial2L23.tStopRefresh)
    trials2.addData('trial2L24.started', trial2L24.tStartRefresh)
    trials2.addData('trial2L24.stopped', trial2L24.tStopRefresh)
    trials2.addData('trial2T13.started', trial2T13.tStartRefresh)
    trials2.addData('trial2T13.stopped', trial2T13.tStopRefresh)
    trials2.addData('trial2T14.started', trial2T14.tStartRefresh)
    trials2.addData('trial2T14.stopped', trial2T14.tStopRefresh)
    trials2.addData('trial2L15.started', trial2L15.tStartRefresh)
    trials2.addData('trial2L15.stopped', trial2L15.tStopRefresh)
    trials2.addData('trial2L16.started', trial2L16.tStartRefresh)
    trials2.addData('trial2L16.stopped', trial2L16.tStopRefresh)
    trials2.addData('trial2L25.started', trial2L25.tStartRefresh)
    trials2.addData('trial2L25.stopped', trial2L25.tStopRefresh)
    trials2.addData('trial2L26.started', trial2L26.tStartRefresh)
    trials2.addData('trial2L26.stopped', trial2L26.tStopRefresh)
    trials2.addData('trial2T15.started', trial2T15.tStartRefresh)
    trials2.addData('trial2T15.stopped', trial2T15.tStopRefresh)
    trials2.addData('trial2T16.started', trial2T16.tStartRefresh)
    trials2.addData('trial2T16.stopped', trial2T16.tStopRefresh)
    trials2.addData('trial2TT.started', trial2TT.tStartRefresh)
    trials2.addData('trial2TT.stopped', trial2TT.tStopRefresh)
    # check responses
    if trial2Resp.keys in ['', [], None]:  # No response was made
        trial2Resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial2Resp.corr = 1;  # correct non-response
        else:
           trial2Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials2 (TrialHandler)
    trials2.addData('trial2Resp.keys',trial2Resp.keys)
    trials2.addData('trial2Resp.corr', trial2Resp.corr)
    if trial2Resp.keys != None:  # we had a response
        trials2.addData('trial2Resp.rt', trial2Resp.rt)
    trials2.addData('trial2Resp.started', trial2Resp.tStartRefresh)
    trials2.addData('trial2Resp.stopped', trial2Resp.tStopRefresh)
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'


# ------Prepare to start Routine "breakTime2"-------
continueRoutine = True
# update component parameters for each repeat
breakResp2.keys = []
breakResp2.rt = []
_breakResp2_allKeys = []
# keep track of which components have finished
breakTime2Components = [breakText2, breakResp2]
for thisComponent in breakTime2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
breakTime2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "breakTime2"-------
while continueRoutine:
    # get current time
    t = breakTime2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=breakTime2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *breakText2* updates
    if breakText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakText2.frameNStart = frameN  # exact frame index
        breakText2.tStart = t  # local t and not account for scr refresh
        breakText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakText2, 'tStartRefresh')  # time at next scr refresh
        breakText2.setAutoDraw(True)
    
    # *breakResp2* updates
    waitOnFlip = False
    if breakResp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breakResp2.frameNStart = frameN  # exact frame index
        breakResp2.tStart = t  # local t and not account for scr refresh
        breakResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakResp2, 'tStartRefresh')  # time at next scr refresh
        breakResp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(breakResp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(breakResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if breakResp2.status == STARTED and not waitOnFlip:
        theseKeys = breakResp2.getKeys(keyList=['space'], waitRelease=False)
        _breakResp2_allKeys.extend(theseKeys)
        if len(_breakResp2_allKeys):
            breakResp2.keys = _breakResp2_allKeys[-1].name  # just the last key pressed
            breakResp2.rt = _breakResp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in breakTime2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "breakTime2"-------
for thisComponent in breakTime2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('breakText2.started', breakText2.tStartRefresh)
thisExp.addData('breakText2.stopped', breakText2.tStopRefresh)
# check responses
if breakResp2.keys in ['', [], None]:  # No response was made
    breakResp2.keys = None
thisExp.addData('breakResp2.keys',breakResp2.keys)
if breakResp2.keys != None:  # we had a response
    thisExp.addData('breakResp2.rt', breakResp2.rt)
thisExp.addData('breakResp2.started', breakResp2.tStartRefresh)
thisExp.addData('breakResp2.stopped', breakResp2.tStopRefresh)
thisExp.nextEntry()
# the Routine "breakTime2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchCond3.xlsx'),
    seed=None, name='trials3')
thisExp.addLoop(trials3)  # add the loop to the experiment
thisTrials3 = trials3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
if thisTrials3 != None:
    for paramName in thisTrials3:
        exec('{} = thisTrials3[paramName]'.format(paramName))

for thisTrials3 in trials3:
    currentLoop = trials3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
    if thisTrials3 != None:
        for paramName in thisTrials3:
            exec('{} = thisTrials3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial3"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial3L11.setPos([loc1,loc2])
    trial3L12.setPos([loc3,loc4])
    trial3L21.setPos([loc5,loc6])
    trial3L22.setPos([loc7,loc8])
    trial3T11.setPos([loc9,loc10])
    trial3T12.setPos([loc11,loc12])
    trial3L13.setPos((loc13, loc14))
    trial3L14.setPos((loc15, loc16))
    trial3L23.setPos((loc17, loc18))
    trial3L24.setPos((loc19, loc20))
    trial3T13.setPos((loc21, loc22))
    trial3T14.setPos((loc23, loc24))
    trial3L15.setPos((loc25, loc26))
    trial3L16.setPos((loc27, loc28))
    trial3L25.setPos((loc29, loc30))
    trial3L26.setPos((loc31, loc32))
    trial3T15.setPos((loc33, loc34))
    trial3T16.setPos((loc35, loc36))
    trial3TT.setPos([loc37,loc38])
    trial3Resp.keys = []
    trial3Resp.rt = []
    _trial3Resp_allKeys = []
    # keep track of which components have finished
    trial3Components = [trial3Fix, trial3L11, trial3L12, trial3L21, trial3L22, trial3T11, trial3T12, trial3L13, trial3L14, trial3L23, trial3L24, trial3T13, trial3T14, trial3L15, trial3L16, trial3L25, trial3L26, trial3T15, trial3T16, trial3TT, trial3Resp]
    for thisComponent in trial3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial3"-------
    while continueRoutine:
        # get current time
        t = trial3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial3Fix* updates
        if trial3Fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial3Fix.frameNStart = frameN  # exact frame index
            trial3Fix.tStart = t  # local t and not account for scr refresh
            trial3Fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3Fix, 'tStartRefresh')  # time at next scr refresh
            trial3Fix.setAutoDraw(True)
        if trial3Fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial3Fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial3Fix.tStop = t  # not accounting for scr refresh
                trial3Fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial3Fix, 'tStopRefresh')  # time at next scr refresh
                trial3Fix.setAutoDraw(False)
        
        # *trial3L11* updates
        if trial3L11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L11.frameNStart = frameN  # exact frame index
            trial3L11.tStart = t  # local t and not account for scr refresh
            trial3L11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L11, 'tStartRefresh')  # time at next scr refresh
            trial3L11.setAutoDraw(True)
        
        # *trial3L12* updates
        if trial3L12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L12.frameNStart = frameN  # exact frame index
            trial3L12.tStart = t  # local t and not account for scr refresh
            trial3L12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L12, 'tStartRefresh')  # time at next scr refresh
            trial3L12.setAutoDraw(True)
        
        # *trial3L21* updates
        if trial3L21.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L21.frameNStart = frameN  # exact frame index
            trial3L21.tStart = t  # local t and not account for scr refresh
            trial3L21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L21, 'tStartRefresh')  # time at next scr refresh
            trial3L21.setAutoDraw(True)
        
        # *trial3L22* updates
        if trial3L22.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L22.frameNStart = frameN  # exact frame index
            trial3L22.tStart = t  # local t and not account for scr refresh
            trial3L22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L22, 'tStartRefresh')  # time at next scr refresh
            trial3L22.setAutoDraw(True)
        
        # *trial3T11* updates
        if trial3T11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3T11.frameNStart = frameN  # exact frame index
            trial3T11.tStart = t  # local t and not account for scr refresh
            trial3T11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3T11, 'tStartRefresh')  # time at next scr refresh
            trial3T11.setAutoDraw(True)
        
        # *trial3T12* updates
        if trial3T12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3T12.frameNStart = frameN  # exact frame index
            trial3T12.tStart = t  # local t and not account for scr refresh
            trial3T12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3T12, 'tStartRefresh')  # time at next scr refresh
            trial3T12.setAutoDraw(True)
        
        # *trial3L13* updates
        if trial3L13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L13.frameNStart = frameN  # exact frame index
            trial3L13.tStart = t  # local t and not account for scr refresh
            trial3L13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L13, 'tStartRefresh')  # time at next scr refresh
            trial3L13.setAutoDraw(True)
        
        # *trial3L14* updates
        if trial3L14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L14.frameNStart = frameN  # exact frame index
            trial3L14.tStart = t  # local t and not account for scr refresh
            trial3L14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L14, 'tStartRefresh')  # time at next scr refresh
            trial3L14.setAutoDraw(True)
        
        # *trial3L23* updates
        if trial3L23.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L23.frameNStart = frameN  # exact frame index
            trial3L23.tStart = t  # local t and not account for scr refresh
            trial3L23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L23, 'tStartRefresh')  # time at next scr refresh
            trial3L23.setAutoDraw(True)
        
        # *trial3L24* updates
        if trial3L24.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L24.frameNStart = frameN  # exact frame index
            trial3L24.tStart = t  # local t and not account for scr refresh
            trial3L24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L24, 'tStartRefresh')  # time at next scr refresh
            trial3L24.setAutoDraw(True)
        
        # *trial3T13* updates
        if trial3T13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3T13.frameNStart = frameN  # exact frame index
            trial3T13.tStart = t  # local t and not account for scr refresh
            trial3T13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3T13, 'tStartRefresh')  # time at next scr refresh
            trial3T13.setAutoDraw(True)
        
        # *trial3T14* updates
        if trial3T14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3T14.frameNStart = frameN  # exact frame index
            trial3T14.tStart = t  # local t and not account for scr refresh
            trial3T14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3T14, 'tStartRefresh')  # time at next scr refresh
            trial3T14.setAutoDraw(True)
        
        # *trial3L15* updates
        if trial3L15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L15.frameNStart = frameN  # exact frame index
            trial3L15.tStart = t  # local t and not account for scr refresh
            trial3L15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L15, 'tStartRefresh')  # time at next scr refresh
            trial3L15.setAutoDraw(True)
        
        # *trial3L16* updates
        if trial3L16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L16.frameNStart = frameN  # exact frame index
            trial3L16.tStart = t  # local t and not account for scr refresh
            trial3L16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L16, 'tStartRefresh')  # time at next scr refresh
            trial3L16.setAutoDraw(True)
        
        # *trial3L25* updates
        if trial3L25.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L25.frameNStart = frameN  # exact frame index
            trial3L25.tStart = t  # local t and not account for scr refresh
            trial3L25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L25, 'tStartRefresh')  # time at next scr refresh
            trial3L25.setAutoDraw(True)
        
        # *trial3L26* updates
        if trial3L26.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3L26.frameNStart = frameN  # exact frame index
            trial3L26.tStart = t  # local t and not account for scr refresh
            trial3L26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3L26, 'tStartRefresh')  # time at next scr refresh
            trial3L26.setAutoDraw(True)
        
        # *trial3T15* updates
        if trial3T15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3T15.frameNStart = frameN  # exact frame index
            trial3T15.tStart = t  # local t and not account for scr refresh
            trial3T15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3T15, 'tStartRefresh')  # time at next scr refresh
            trial3T15.setAutoDraw(True)
        
        # *trial3T16* updates
        if trial3T16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3T16.frameNStart = frameN  # exact frame index
            trial3T16.tStart = t  # local t and not account for scr refresh
            trial3T16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3T16, 'tStartRefresh')  # time at next scr refresh
            trial3T16.setAutoDraw(True)
        
        # *trial3TT* updates
        if trial3TT.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3TT.frameNStart = frameN  # exact frame index
            trial3TT.tStart = t  # local t and not account for scr refresh
            trial3TT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3TT, 'tStartRefresh')  # time at next scr refresh
            trial3TT.setAutoDraw(True)
        
        # *trial3Resp* updates
        waitOnFlip = False
        if trial3Resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3Resp.frameNStart = frameN  # exact frame index
            trial3Resp.tStart = t  # local t and not account for scr refresh
            trial3Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3Resp, 'tStartRefresh')  # time at next scr refresh
            trial3Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial3Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial3Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial3Resp.status == STARTED and not waitOnFlip:
            theseKeys = trial3Resp.getKeys(keyList=['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease=False)
            _trial3Resp_allKeys.extend(theseKeys)
            if len(_trial3Resp_allKeys):
                trial3Resp.keys = _trial3Resp_allKeys[-1].name  # just the last key pressed
                trial3Resp.rt = _trial3Resp_allKeys[-1].rt
                # was this correct?
                if (trial3Resp.keys == str(corrAns)) or (trial3Resp.keys == corrAns):
                    trial3Resp.corr = 1
                else:
                    trial3Resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial3"-------
    for thisComponent in trial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials3.addData('trial3Fix.started', trial3Fix.tStartRefresh)
    trials3.addData('trial3Fix.stopped', trial3Fix.tStopRefresh)
    trials3.addData('trial3L11.started', trial3L11.tStartRefresh)
    trials3.addData('trial3L11.stopped', trial3L11.tStopRefresh)
    trials3.addData('trial3L12.started', trial3L12.tStartRefresh)
    trials3.addData('trial3L12.stopped', trial3L12.tStopRefresh)
    trials3.addData('trial3L21.started', trial3L21.tStartRefresh)
    trials3.addData('trial3L21.stopped', trial3L21.tStopRefresh)
    trials3.addData('trial3L22.started', trial3L22.tStartRefresh)
    trials3.addData('trial3L22.stopped', trial3L22.tStopRefresh)
    trials3.addData('trial3T11.started', trial3T11.tStartRefresh)
    trials3.addData('trial3T11.stopped', trial3T11.tStopRefresh)
    trials3.addData('trial3T12.started', trial3T12.tStartRefresh)
    trials3.addData('trial3T12.stopped', trial3T12.tStopRefresh)
    trials3.addData('trial3L13.started', trial3L13.tStartRefresh)
    trials3.addData('trial3L13.stopped', trial3L13.tStopRefresh)
    trials3.addData('trial3L14.started', trial3L14.tStartRefresh)
    trials3.addData('trial3L14.stopped', trial3L14.tStopRefresh)
    trials3.addData('trial3L23.started', trial3L23.tStartRefresh)
    trials3.addData('trial3L23.stopped', trial3L23.tStopRefresh)
    trials3.addData('trial3L24.started', trial3L24.tStartRefresh)
    trials3.addData('trial3L24.stopped', trial3L24.tStopRefresh)
    trials3.addData('trial3T13.started', trial3T13.tStartRefresh)
    trials3.addData('trial3T13.stopped', trial3T13.tStopRefresh)
    trials3.addData('trial3T14.started', trial3T14.tStartRefresh)
    trials3.addData('trial3T14.stopped', trial3T14.tStopRefresh)
    trials3.addData('trial3L15.started', trial3L15.tStartRefresh)
    trials3.addData('trial3L15.stopped', trial3L15.tStopRefresh)
    trials3.addData('trial3L16.started', trial3L16.tStartRefresh)
    trials3.addData('trial3L16.stopped', trial3L16.tStopRefresh)
    trials3.addData('trial3L25.started', trial3L25.tStartRefresh)
    trials3.addData('trial3L25.stopped', trial3L25.tStopRefresh)
    trials3.addData('trial3L26.started', trial3L26.tStartRefresh)
    trials3.addData('trial3L26.stopped', trial3L26.tStopRefresh)
    trials3.addData('trial3T15.started', trial3T15.tStartRefresh)
    trials3.addData('trial3T15.stopped', trial3T15.tStopRefresh)
    trials3.addData('trial3T16.started', trial3T16.tStartRefresh)
    trials3.addData('trial3T16.stopped', trial3T16.tStopRefresh)
    trials3.addData('trial3TT.started', trial3TT.tStartRefresh)
    trials3.addData('trial3TT.stopped', trial3TT.tStopRefresh)
    # check responses
    if trial3Resp.keys in ['', [], None]:  # No response was made
        trial3Resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial3Resp.corr = 1;  # correct non-response
        else:
           trial3Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials3 (TrialHandler)
    trials3.addData('trial3Resp.keys',trial3Resp.keys)
    trials3.addData('trial3Resp.corr', trial3Resp.corr)
    if trial3Resp.keys != None:  # we had a response
        trials3.addData('trial3Resp.rt', trial3Resp.rt)
    trials3.addData('trial3Resp.started', trial3Resp.tStartRefresh)
    trials3.addData('trial3Resp.stopped', trial3Resp.tStopRefresh)
    # the Routine "trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials3'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thanks]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
