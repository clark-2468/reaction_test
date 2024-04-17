#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.1),
    on April 17, 2024, at 13:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.1'
expName = 'test1'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Eli L\\Documents\\PsychoPy\\test1_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=(1024, 768), fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('endintro') is None:
        # initialise endintro
        endintro = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='endintro',
        )
    if deviceManager.getDevice('endhowitworks') is None:
        # initialise endhowitworks
        endhowitworks = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='endhowitworks',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('res_red_0_5') is None:
        # initialise res_red_0_5
        res_red_0_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_red_0_5',
        )
    if deviceManager.getDevice('res_red_0_625') is None:
        # initialise res_red_0_625
        res_red_0_625 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_red_0_625',
        )
    if deviceManager.getDevice('res_blue_0_5') is None:
        # initialise res_blue_0_5
        res_blue_0_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_blue_0_5',
        )
    if deviceManager.getDevice('res_blue_0_625') is None:
        # initialise res_blue_0_625
        res_blue_0_625 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_blue_0_625',
        )
    if deviceManager.getDevice('res_green_0_5') is None:
        # initialise res_green_0_5
        res_green_0_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_green_0_5',
        )
    if deviceManager.getDevice('res_green_0_625') is None:
        # initialise res_green_0_625
        res_green_0_625 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_green_0_625',
        )
    if deviceManager.getDevice('res_purple_0_5') is None:
        # initialise res_purple_0_5
        res_purple_0_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_purple_0_5',
        )
    if deviceManager.getDevice('res_purple_0_625') is None:
        # initialise res_purple_0_625
        res_purple_0_625 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_purple_0_625',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "intro" ---
    text = visual.TextStim(win=win, name='text',
        text='Hello\n\nWelcome to the PsychoPy script developed by Eli, for testing the human reaction time. I really appreciate your participation as every piece of data contributes to the final conclusion\n\nPress the space bar when you have finished reading',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    endintro = keyboard.Keyboard(deviceName='endintro')
    
    # --- Initialize components for Routine "howitworks" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='This test is made of two parts\nVisual and Ad\n\nThis test aims to test your reaction time. When you hear the sound being played or the image being shown, press the space bar on the keyboard as soon as you can. Do not try to predict the time that the stimulus will start as all stimuli are generated at random timings\n\nThe first one will be the test run for you familiarise with this test\n\nPress the space bar when you have finished reading\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    endhowitworks = keyboard.Keyboard(deviceName='endhowitworks')
    
    # --- Initialize components for Routine "test" ---
    testpolygon = visual.ShapeStim(
        win=win, name='testpolygon',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
        opacity=None, depth=0.0, interpolate=True)
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "test_passed" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Congrats!!!! You have done you test run\n\nPress space bar to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "red0_5" ---
    res_red_0_5 = keyboard.Keyboard(deviceName='res_red_0_5')
    polygon_red_0_5 = visual.ShapeStim(
        win=win, name='polygon_red_0_5',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0039, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "red0_625" ---
    polygon_red_0_625 = visual.ShapeStim(
        win=win, name='polygon_red_0_625',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2471, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_red_0_625 = keyboard.Keyboard(deviceName='res_red_0_625')
    
    # --- Initialize components for Routine "blue0_5" ---
    polygon_blue_0_5 = visual.ShapeStim(
        win=win, name='polygon_blue_0_5',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -0.3333, 0.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_blue_0_5 = keyboard.Keyboard(deviceName='res_blue_0_5')
    
    # --- Initialize components for Routine "blue0_625" ---
    polygon_blue_0_625 = visual.ShapeStim(
        win=win, name='polygon_blue_0_625',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -0.1667, 0.2500],
        opacity=None, depth=0.0, interpolate=True)
    res_blue_0_625 = keyboard.Keyboard(deviceName='res_blue_0_625')
    
    # --- Initialize components for Routine "green0_5" ---
    polygon_green_0_5 = visual.ShapeStim(
        win=win, name='polygon_green_0_5',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-0.6667, 0.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_green_0_5 = keyboard.Keyboard(deviceName='res_green_0_5')
    
    # --- Initialize components for Routine "green0_625" ---
    polygon_green_0_625 = visual.ShapeStim(
        win=win, name='polygon_green_0_625',
        size=(0.5, 0.5), vertices='triangle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-0.5833, 0.2500, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_green_0_625 = keyboard.Keyboard(deviceName='res_green_0_625')
    
    # --- Initialize components for Routine "purple0_5" ---
    polygon_purple_0_5 = visual.ShapeStim(
        win=win, name='polygon_purple_0_5',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, -1.0000, 0.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_purple_0_5 = keyboard.Keyboard(deviceName='res_purple_0_5')
    
    # --- Initialize components for Routine "purple0_625" ---
    polygon_purple_0_625 = visual.ShapeStim(
        win=win, name='polygon_purple_0_625',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2500, -1.0000, 0.2500],
        opacity=None, depth=0.0, interpolate=True)
    res_purple_0_625 = keyboard.Keyboard(deviceName='res_purple_0_625')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "intro" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('intro.started', globalClock.getTime(format='float'))
    endintro.keys = []
    endintro.rt = []
    _endintro_allKeys = []
    # keep track of which components have finished
    introComponents = [text, endintro]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *endintro* updates
        waitOnFlip = False
        
        # if endintro is starting this frame...
        if endintro.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            endintro.frameNStart = frameN  # exact frame index
            endintro.tStart = t  # local t and not account for scr refresh
            endintro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endintro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endintro.started')
            # update status
            endintro.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endintro.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endintro.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endintro.status == STARTED and not waitOnFlip:
            theseKeys = endintro.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _endintro_allKeys.extend(theseKeys)
            if len(_endintro_allKeys):
                endintro.keys = _endintro_allKeys[-1].name  # just the last key pressed
                endintro.rt = _endintro_allKeys[-1].rt
                endintro.duration = _endintro_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro" ---
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('intro.stopped', globalClock.getTime(format='float'))
    # check responses
    if endintro.keys in ['', [], None]:  # No response was made
        endintro.keys = None
    thisExp.addData('endintro.keys',endintro.keys)
    if endintro.keys != None:  # we had a response
        thisExp.addData('endintro.rt', endintro.rt)
        thisExp.addData('endintro.duration', endintro.duration)
    thisExp.nextEntry()
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "howitworks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('howitworks.started', globalClock.getTime(format='float'))
    endhowitworks.keys = []
    endhowitworks.rt = []
    _endhowitworks_allKeys = []
    # keep track of which components have finished
    howitworksComponents = [text_2, endhowitworks]
    for thisComponent in howitworksComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "howitworks" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # *endhowitworks* updates
        waitOnFlip = False
        
        # if endhowitworks is starting this frame...
        if endhowitworks.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            endhowitworks.frameNStart = frameN  # exact frame index
            endhowitworks.tStart = t  # local t and not account for scr refresh
            endhowitworks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endhowitworks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endhowitworks.started')
            # update status
            endhowitworks.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endhowitworks.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endhowitworks.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endhowitworks.status == STARTED and not waitOnFlip:
            theseKeys = endhowitworks.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _endhowitworks_allKeys.extend(theseKeys)
            if len(_endhowitworks_allKeys):
                endhowitworks.keys = _endhowitworks_allKeys[-1].name  # just the last key pressed
                endhowitworks.rt = _endhowitworks_allKeys[-1].rt
                endhowitworks.duration = _endhowitworks_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in howitworksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "howitworks" ---
    for thisComponent in howitworksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('howitworks.stopped', globalClock.getTime(format='float'))
    # check responses
    if endhowitworks.keys in ['', [], None]:  # No response was made
        endhowitworks.keys = None
    thisExp.addData('endhowitworks.keys',endhowitworks.keys)
    if endhowitworks.keys != None:  # we had a response
        thisExp.addData('endhowitworks.rt', endhowitworks.rt)
        thisExp.addData('endhowitworks.duration', endhowitworks.duration)
    thisExp.nextEntry()
    # the Routine "howitworks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "test" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('test.started', globalClock.getTime(format='float'))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    testComponents = [testpolygon, key_resp]
    for thisComponent in testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "test" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testpolygon* updates
        
        # if testpolygon is starting this frame...
        if testpolygon.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            testpolygon.frameNStart = frameN  # exact frame index
            testpolygon.tStart = t  # local t and not account for scr refresh
            testpolygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testpolygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'testpolygon.started')
            # update status
            testpolygon.status = STARTED
            testpolygon.setAutoDraw(True)
        
        # if testpolygon is active this frame...
        if testpolygon.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "test" ---
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('test.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "test_passed" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('test_passed.started', globalClock.getTime(format='float'))
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    test_passedComponents = [text_3, key_resp_2]
    for thisComponent in test_passedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "test_passed" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_passedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "test_passed" ---
    for thisComponent in test_passedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('test_passed.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "test_passed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "red0_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('red0_5.started', globalClock.getTime(format='float'))
    res_red_0_5.keys = []
    res_red_0_5.rt = []
    _res_red_0_5_allKeys = []
    # keep track of which components have finished
    red0_5Components = [res_red_0_5, polygon_red_0_5]
    for thisComponent in red0_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "red0_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *res_red_0_5* updates
        waitOnFlip = False
        
        # if res_red_0_5 is starting this frame...
        if res_red_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_red_0_5.frameNStart = frameN  # exact frame index
            res_red_0_5.tStart = t  # local t and not account for scr refresh
            res_red_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_red_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_red_0_5.started')
            # update status
            res_red_0_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_red_0_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_red_0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_red_0_5.status == STARTED and not waitOnFlip:
            theseKeys = res_red_0_5.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_red_0_5_allKeys.extend(theseKeys)
            if len(_res_red_0_5_allKeys):
                res_red_0_5.keys = _res_red_0_5_allKeys[-1].name  # just the last key pressed
                res_red_0_5.rt = _res_red_0_5_allKeys[-1].rt
                res_red_0_5.duration = _res_red_0_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *polygon_red_0_5* updates
        
        # if polygon_red_0_5 is starting this frame...
        if polygon_red_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_red_0_5.frameNStart = frameN  # exact frame index
            polygon_red_0_5.tStart = t  # local t and not account for scr refresh
            polygon_red_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_red_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_red_0_5.started')
            # update status
            polygon_red_0_5.status = STARTED
            polygon_red_0_5.setAutoDraw(True)
        
        # if polygon_red_0_5 is active this frame...
        if polygon_red_0_5.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in red0_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "red0_5" ---
    for thisComponent in red0_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('red0_5.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_red_0_5.keys in ['', [], None]:  # No response was made
        res_red_0_5.keys = None
    thisExp.addData('res_red_0_5.keys',res_red_0_5.keys)
    if res_red_0_5.keys != None:  # we had a response
        thisExp.addData('res_red_0_5.rt', res_red_0_5.rt)
        thisExp.addData('res_red_0_5.duration', res_red_0_5.duration)
    thisExp.nextEntry()
    # the Routine "red0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "red0_625" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('red0_625.started', globalClock.getTime(format='float'))
    res_red_0_625.keys = []
    res_red_0_625.rt = []
    _res_red_0_625_allKeys = []
    # keep track of which components have finished
    red0_625Components = [polygon_red_0_625, res_red_0_625]
    for thisComponent in red0_625Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "red0_625" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_red_0_625* updates
        
        # if polygon_red_0_625 is starting this frame...
        if polygon_red_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_red_0_625.frameNStart = frameN  # exact frame index
            polygon_red_0_625.tStart = t  # local t and not account for scr refresh
            polygon_red_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_red_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_red_0_625.started')
            # update status
            polygon_red_0_625.status = STARTED
            polygon_red_0_625.setAutoDraw(True)
        
        # if polygon_red_0_625 is active this frame...
        if polygon_red_0_625.status == STARTED:
            # update params
            pass
        
        # *res_red_0_625* updates
        waitOnFlip = False
        
        # if res_red_0_625 is starting this frame...
        if res_red_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_red_0_625.frameNStart = frameN  # exact frame index
            res_red_0_625.tStart = t  # local t and not account for scr refresh
            res_red_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_red_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_red_0_625.started')
            # update status
            res_red_0_625.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_red_0_625.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_red_0_625.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_red_0_625.status == STARTED and not waitOnFlip:
            theseKeys = res_red_0_625.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_red_0_625_allKeys.extend(theseKeys)
            if len(_res_red_0_625_allKeys):
                res_red_0_625.keys = _res_red_0_625_allKeys[-1].name  # just the last key pressed
                res_red_0_625.rt = _res_red_0_625_allKeys[-1].rt
                res_red_0_625.duration = _res_red_0_625_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in red0_625Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "red0_625" ---
    for thisComponent in red0_625Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('red0_625.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_red_0_625.keys in ['', [], None]:  # No response was made
        res_red_0_625.keys = None
    thisExp.addData('res_red_0_625.keys',res_red_0_625.keys)
    if res_red_0_625.keys != None:  # we had a response
        thisExp.addData('res_red_0_625.rt', res_red_0_625.rt)
        thisExp.addData('res_red_0_625.duration', res_red_0_625.duration)
    thisExp.nextEntry()
    # the Routine "red0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blue0_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blue0_5.started', globalClock.getTime(format='float'))
    res_blue_0_5.keys = []
    res_blue_0_5.rt = []
    _res_blue_0_5_allKeys = []
    # keep track of which components have finished
    blue0_5Components = [polygon_blue_0_5, res_blue_0_5]
    for thisComponent in blue0_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blue0_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_blue_0_5* updates
        
        # if polygon_blue_0_5 is starting this frame...
        if polygon_blue_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_blue_0_5.frameNStart = frameN  # exact frame index
            polygon_blue_0_5.tStart = t  # local t and not account for scr refresh
            polygon_blue_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_blue_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_blue_0_5.started')
            # update status
            polygon_blue_0_5.status = STARTED
            polygon_blue_0_5.setAutoDraw(True)
        
        # if polygon_blue_0_5 is active this frame...
        if polygon_blue_0_5.status == STARTED:
            # update params
            pass
        
        # *res_blue_0_5* updates
        waitOnFlip = False
        
        # if res_blue_0_5 is starting this frame...
        if res_blue_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_blue_0_5.frameNStart = frameN  # exact frame index
            res_blue_0_5.tStart = t  # local t and not account for scr refresh
            res_blue_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_blue_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_blue_0_5.started')
            # update status
            res_blue_0_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_blue_0_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_blue_0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_blue_0_5.status == STARTED and not waitOnFlip:
            theseKeys = res_blue_0_5.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_blue_0_5_allKeys.extend(theseKeys)
            if len(_res_blue_0_5_allKeys):
                res_blue_0_5.keys = _res_blue_0_5_allKeys[-1].name  # just the last key pressed
                res_blue_0_5.rt = _res_blue_0_5_allKeys[-1].rt
                res_blue_0_5.duration = _res_blue_0_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blue0_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blue0_5" ---
    for thisComponent in blue0_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blue0_5.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_blue_0_5.keys in ['', [], None]:  # No response was made
        res_blue_0_5.keys = None
    thisExp.addData('res_blue_0_5.keys',res_blue_0_5.keys)
    if res_blue_0_5.keys != None:  # we had a response
        thisExp.addData('res_blue_0_5.rt', res_blue_0_5.rt)
        thisExp.addData('res_blue_0_5.duration', res_blue_0_5.duration)
    thisExp.nextEntry()
    # the Routine "blue0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blue0_625" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blue0_625.started', globalClock.getTime(format='float'))
    res_blue_0_625.keys = []
    res_blue_0_625.rt = []
    _res_blue_0_625_allKeys = []
    # keep track of which components have finished
    blue0_625Components = [polygon_blue_0_625, res_blue_0_625]
    for thisComponent in blue0_625Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blue0_625" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_blue_0_625* updates
        
        # if polygon_blue_0_625 is starting this frame...
        if polygon_blue_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_blue_0_625.frameNStart = frameN  # exact frame index
            polygon_blue_0_625.tStart = t  # local t and not account for scr refresh
            polygon_blue_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_blue_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_blue_0_625.started')
            # update status
            polygon_blue_0_625.status = STARTED
            polygon_blue_0_625.setAutoDraw(True)
        
        # if polygon_blue_0_625 is active this frame...
        if polygon_blue_0_625.status == STARTED:
            # update params
            pass
        
        # *res_blue_0_625* updates
        waitOnFlip = False
        
        # if res_blue_0_625 is starting this frame...
        if res_blue_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_blue_0_625.frameNStart = frameN  # exact frame index
            res_blue_0_625.tStart = t  # local t and not account for scr refresh
            res_blue_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_blue_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_blue_0_625.started')
            # update status
            res_blue_0_625.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_blue_0_625.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_blue_0_625.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_blue_0_625.status == STARTED and not waitOnFlip:
            theseKeys = res_blue_0_625.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_blue_0_625_allKeys.extend(theseKeys)
            if len(_res_blue_0_625_allKeys):
                res_blue_0_625.keys = _res_blue_0_625_allKeys[-1].name  # just the last key pressed
                res_blue_0_625.rt = _res_blue_0_625_allKeys[-1].rt
                res_blue_0_625.duration = _res_blue_0_625_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blue0_625Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blue0_625" ---
    for thisComponent in blue0_625Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blue0_625.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_blue_0_625.keys in ['', [], None]:  # No response was made
        res_blue_0_625.keys = None
    thisExp.addData('res_blue_0_625.keys',res_blue_0_625.keys)
    if res_blue_0_625.keys != None:  # we had a response
        thisExp.addData('res_blue_0_625.rt', res_blue_0_625.rt)
        thisExp.addData('res_blue_0_625.duration', res_blue_0_625.duration)
    thisExp.nextEntry()
    # the Routine "blue0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "green0_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('green0_5.started', globalClock.getTime(format='float'))
    res_green_0_5.keys = []
    res_green_0_5.rt = []
    _res_green_0_5_allKeys = []
    # keep track of which components have finished
    green0_5Components = [polygon_green_0_5, res_green_0_5]
    for thisComponent in green0_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "green0_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_green_0_5* updates
        
        # if polygon_green_0_5 is starting this frame...
        if polygon_green_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_green_0_5.frameNStart = frameN  # exact frame index
            polygon_green_0_5.tStart = t  # local t and not account for scr refresh
            polygon_green_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_green_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_green_0_5.started')
            # update status
            polygon_green_0_5.status = STARTED
            polygon_green_0_5.setAutoDraw(True)
        
        # if polygon_green_0_5 is active this frame...
        if polygon_green_0_5.status == STARTED:
            # update params
            pass
        
        # *res_green_0_5* updates
        waitOnFlip = False
        
        # if res_green_0_5 is starting this frame...
        if res_green_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_green_0_5.frameNStart = frameN  # exact frame index
            res_green_0_5.tStart = t  # local t and not account for scr refresh
            res_green_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_green_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_green_0_5.started')
            # update status
            res_green_0_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_green_0_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_green_0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_green_0_5.status == STARTED and not waitOnFlip:
            theseKeys = res_green_0_5.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_green_0_5_allKeys.extend(theseKeys)
            if len(_res_green_0_5_allKeys):
                res_green_0_5.keys = _res_green_0_5_allKeys[-1].name  # just the last key pressed
                res_green_0_5.rt = _res_green_0_5_allKeys[-1].rt
                res_green_0_5.duration = _res_green_0_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in green0_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "green0_5" ---
    for thisComponent in green0_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('green0_5.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_green_0_5.keys in ['', [], None]:  # No response was made
        res_green_0_5.keys = None
    thisExp.addData('res_green_0_5.keys',res_green_0_5.keys)
    if res_green_0_5.keys != None:  # we had a response
        thisExp.addData('res_green_0_5.rt', res_green_0_5.rt)
        thisExp.addData('res_green_0_5.duration', res_green_0_5.duration)
    thisExp.nextEntry()
    # the Routine "green0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "green0_625" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('green0_625.started', globalClock.getTime(format='float'))
    res_green_0_625.keys = []
    res_green_0_625.rt = []
    _res_green_0_625_allKeys = []
    # keep track of which components have finished
    green0_625Components = [polygon_green_0_625, res_green_0_625]
    for thisComponent in green0_625Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "green0_625" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_green_0_625* updates
        
        # if polygon_green_0_625 is starting this frame...
        if polygon_green_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_green_0_625.frameNStart = frameN  # exact frame index
            polygon_green_0_625.tStart = t  # local t and not account for scr refresh
            polygon_green_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_green_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_green_0_625.started')
            # update status
            polygon_green_0_625.status = STARTED
            polygon_green_0_625.setAutoDraw(True)
        
        # if polygon_green_0_625 is active this frame...
        if polygon_green_0_625.status == STARTED:
            # update params
            pass
        
        # *res_green_0_625* updates
        waitOnFlip = False
        
        # if res_green_0_625 is starting this frame...
        if res_green_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_green_0_625.frameNStart = frameN  # exact frame index
            res_green_0_625.tStart = t  # local t and not account for scr refresh
            res_green_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_green_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_green_0_625.started')
            # update status
            res_green_0_625.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_green_0_625.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_green_0_625.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_green_0_625.status == STARTED and not waitOnFlip:
            theseKeys = res_green_0_625.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_green_0_625_allKeys.extend(theseKeys)
            if len(_res_green_0_625_allKeys):
                res_green_0_625.keys = _res_green_0_625_allKeys[-1].name  # just the last key pressed
                res_green_0_625.rt = _res_green_0_625_allKeys[-1].rt
                res_green_0_625.duration = _res_green_0_625_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in green0_625Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "green0_625" ---
    for thisComponent in green0_625Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('green0_625.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_green_0_625.keys in ['', [], None]:  # No response was made
        res_green_0_625.keys = None
    thisExp.addData('res_green_0_625.keys',res_green_0_625.keys)
    if res_green_0_625.keys != None:  # we had a response
        thisExp.addData('res_green_0_625.rt', res_green_0_625.rt)
        thisExp.addData('res_green_0_625.duration', res_green_0_625.duration)
    thisExp.nextEntry()
    # the Routine "green0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "purple0_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('purple0_5.started', globalClock.getTime(format='float'))
    res_purple_0_5.keys = []
    res_purple_0_5.rt = []
    _res_purple_0_5_allKeys = []
    # keep track of which components have finished
    purple0_5Components = [polygon_purple_0_5, res_purple_0_5]
    for thisComponent in purple0_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "purple0_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_purple_0_5* updates
        
        # if polygon_purple_0_5 is starting this frame...
        if polygon_purple_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_purple_0_5.frameNStart = frameN  # exact frame index
            polygon_purple_0_5.tStart = t  # local t and not account for scr refresh
            polygon_purple_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_purple_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_purple_0_5.started')
            # update status
            polygon_purple_0_5.status = STARTED
            polygon_purple_0_5.setAutoDraw(True)
        
        # if polygon_purple_0_5 is active this frame...
        if polygon_purple_0_5.status == STARTED:
            # update params
            pass
        
        # *res_purple_0_5* updates
        waitOnFlip = False
        
        # if res_purple_0_5 is starting this frame...
        if res_purple_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_purple_0_5.frameNStart = frameN  # exact frame index
            res_purple_0_5.tStart = t  # local t and not account for scr refresh
            res_purple_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_purple_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_purple_0_5.started')
            # update status
            res_purple_0_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_purple_0_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_purple_0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_purple_0_5.status == STARTED and not waitOnFlip:
            theseKeys = res_purple_0_5.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_purple_0_5_allKeys.extend(theseKeys)
            if len(_res_purple_0_5_allKeys):
                res_purple_0_5.keys = _res_purple_0_5_allKeys[-1].name  # just the last key pressed
                res_purple_0_5.rt = _res_purple_0_5_allKeys[-1].rt
                res_purple_0_5.duration = _res_purple_0_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in purple0_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "purple0_5" ---
    for thisComponent in purple0_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('purple0_5.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_purple_0_5.keys in ['', [], None]:  # No response was made
        res_purple_0_5.keys = None
    thisExp.addData('res_purple_0_5.keys',res_purple_0_5.keys)
    if res_purple_0_5.keys != None:  # we had a response
        thisExp.addData('res_purple_0_5.rt', res_purple_0_5.rt)
        thisExp.addData('res_purple_0_5.duration', res_purple_0_5.duration)
    thisExp.nextEntry()
    # the Routine "purple0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "purple0_625" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('purple0_625.started', globalClock.getTime(format='float'))
    res_purple_0_625.keys = []
    res_purple_0_625.rt = []
    _res_purple_0_625_allKeys = []
    # keep track of which components have finished
    purple0_625Components = [polygon_purple_0_625, res_purple_0_625]
    for thisComponent in purple0_625Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "purple0_625" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_purple_0_625* updates
        
        # if polygon_purple_0_625 is starting this frame...
        if polygon_purple_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_purple_0_625.frameNStart = frameN  # exact frame index
            polygon_purple_0_625.tStart = t  # local t and not account for scr refresh
            polygon_purple_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_purple_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_purple_0_625.started')
            # update status
            polygon_purple_0_625.status = STARTED
            polygon_purple_0_625.setAutoDraw(True)
        
        # if polygon_purple_0_625 is active this frame...
        if polygon_purple_0_625.status == STARTED:
            # update params
            pass
        
        # *res_purple_0_625* updates
        waitOnFlip = False
        
        # if res_purple_0_625 is starting this frame...
        if res_purple_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_purple_0_625.frameNStart = frameN  # exact frame index
            res_purple_0_625.tStart = t  # local t and not account for scr refresh
            res_purple_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_purple_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_purple_0_625.started')
            # update status
            res_purple_0_625.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_purple_0_625.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_purple_0_625.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_purple_0_625.status == STARTED and not waitOnFlip:
            theseKeys = res_purple_0_625.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_purple_0_625_allKeys.extend(theseKeys)
            if len(_res_purple_0_625_allKeys):
                res_purple_0_625.keys = _res_purple_0_625_allKeys[-1].name  # just the last key pressed
                res_purple_0_625.rt = _res_purple_0_625_allKeys[-1].rt
                res_purple_0_625.duration = _res_purple_0_625_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in purple0_625Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "purple0_625" ---
    for thisComponent in purple0_625Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('purple0_625.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_purple_0_625.keys in ['', [], None]:  # No response was made
        res_purple_0_625.keys = None
    thisExp.addData('res_purple_0_625.keys',res_purple_0_625.keys)
    if res_purple_0_625.keys != None:  # we had a response
        thisExp.addData('res_purple_0_625.rt', res_purple_0_625.rt)
        thisExp.addData('res_purple_0_625.duration', res_purple_0_625.duration)
    thisExp.nextEntry()
    # the Routine "purple0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
