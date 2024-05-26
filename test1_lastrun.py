#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.1),
    on May 26, 2024, at 12:36
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
        originPath='E:\\桌面\\CrestAwardProg\\test1_lastrun.py',
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
    if deviceManager.getDevice('res_intro') is None:
        # initialise res_intro
        res_intro = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_intro',
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
    if deviceManager.getDevice('res_red_0_75') is None:
        # initialise res_red_0_75
        res_red_0_75 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_red_0_75',
        )
    if deviceManager.getDevice('res_red_0_875') is None:
        # initialise res_red_0_875
        res_red_0_875 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_red_0_875',
        )
    if deviceManager.getDevice('res_red_1') is None:
        # initialise res_red_1
        res_red_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_red_1',
        )
    if deviceManager.getDevice('res_yellow_0_5') is None:
        # initialise res_yellow_0_5
        res_yellow_0_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_yellow_0_5',
        )
    if deviceManager.getDevice('res_yellow_0_625') is None:
        # initialise res_yellow_0_625
        res_yellow_0_625 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_yellow_0_625',
        )
    if deviceManager.getDevice('res_yellow_0_75') is None:
        # initialise res_yellow_0_75
        res_yellow_0_75 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_yellow_0_75',
        )
    if deviceManager.getDevice('res_yellow_0_875') is None:
        # initialise res_yellow_0_875
        res_yellow_0_875 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_yellow_0_875',
        )
    if deviceManager.getDevice('res_yellow_1') is None:
        # initialise res_yellow_1
        res_yellow_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_yellow_1',
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
    if deviceManager.getDevice('res_blue_0_75') is None:
        # initialise res_blue_0_75
        res_blue_0_75 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_blue_0_75',
        )
    if deviceManager.getDevice('res_blue_0_875') is None:
        # initialise res_blue_0_875
        res_blue_0_875 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_blue_0_875',
        )
    if deviceManager.getDevice('res_blue_1') is None:
        # initialise res_blue_1
        res_blue_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_blue_1',
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
    if deviceManager.getDevice('res_green_0_75') is None:
        # initialise res_green_0_75
        res_green_0_75 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_green_0_75',
        )
    if deviceManager.getDevice('res_green_0_875') is None:
        # initialise res_green_0_875
        res_green_0_875 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_green_0_875',
        )
    if deviceManager.getDevice('res_green_1') is None:
        # initialise res_green_1
        res_green_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_green_1',
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
    if deviceManager.getDevice('res_purple_0_75') is None:
        # initialise res_purple_0_75
        res_purple_0_75 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_purple_0_75',
        )
    if deviceManager.getDevice('res_purple_0_875') is None:
        # initialise res_purple_0_875
        res_purple_0_875 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_purple_0_875',
        )
    if deviceManager.getDevice('res_purple_1') is None:
        # initialise res_purple_1
        res_purple_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_purple_1',
        )
    if deviceManager.getDevice('res_orange_0_5') is None:
        # initialise res_orange_0_5
        res_orange_0_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_orange_0_5',
        )
    if deviceManager.getDevice('res_orange_0_625') is None:
        # initialise res_orange_0_625
        res_orange_0_625 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_orange_0_625',
        )
    if deviceManager.getDevice('res_orange_0_75') is None:
        # initialise res_orange_0_75
        res_orange_0_75 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_orange_0_75',
        )
    if deviceManager.getDevice('res_orange_0_875') is None:
        # initialise res_orange_0_875
        res_orange_0_875 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_orange_0_875',
        )
    if deviceManager.getDevice('res_orange_1') is None:
        # initialise res_orange_1
        res_orange_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_orange_1',
        )
    if deviceManager.getDevice('audiointro_res') is None:
        # initialise audiointro_res
        audiointro_res = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='audiointro_res',
        )
    # create speaker 'sound_testrun'
    deviceManager.addDevice(
        deviceName='sound_testrun',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_audio_testrun') is None:
        # initialise res_audio_testrun
        res_audio_testrun = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_audio_testrun',
        )
    if deviceManager.getDevice('res_testpassed') is None:
        # initialise res_testpassed
        res_testpassed = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_testpassed',
        )
    # create speaker 'sound_500Hz_0_25'
    deviceManager.addDevice(
        deviceName='sound_500Hz_0_25',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_500Hz_0_25') is None:
        # initialise res_500Hz_0_25
        res_500Hz_0_25 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_500Hz_0_25',
        )
    # create speaker 'sound_500Hz_0_5'
    deviceManager.addDevice(
        deviceName='sound_500Hz_0_5',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_500Hz_0_5') is None:
        # initialise res_500Hz_0_5
        res_500Hz_0_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_500Hz_0_5',
        )
    # create speaker 'sound_500Hz_0_75'
    deviceManager.addDevice(
        deviceName='sound_500Hz_0_75',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_500Hz_0_75') is None:
        # initialise res_500Hz_0_75
        res_500Hz_0_75 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_500Hz_0_75',
        )
    # create speaker 'sound_500Hz'
    deviceManager.addDevice(
        deviceName='sound_500Hz',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_500Hz') is None:
        # initialise res_500Hz
        res_500Hz = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_500Hz',
        )
    # create speaker 'sound_2500Hz_0_25'
    deviceManager.addDevice(
        deviceName='sound_2500Hz_0_25',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_2500Hz_0_25') is None:
        # initialise res_2500Hz_0_25
        res_2500Hz_0_25 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_2500Hz_0_25',
        )
    # create speaker 'sound_2500Hz'
    deviceManager.addDevice(
        deviceName='sound_2500Hz',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_2500Hz') is None:
        # initialise res_2500Hz
        res_2500Hz = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_2500Hz',
        )
    # create speaker 'sound_5000Hz'
    deviceManager.addDevice(
        deviceName='sound_5000Hz',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_5000Hz') is None:
        # initialise res_5000Hz
        res_5000Hz = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_5000Hz',
        )
    # create speaker 'sound_7500Hz'
    deviceManager.addDevice(
        deviceName='sound_7500Hz',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_7500Hz') is None:
        # initialise res_7500Hz
        res_7500Hz = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_7500Hz',
        )
    # create speaker 'sound_10000Hz'
    deviceManager.addDevice(
        deviceName='sound_10000Hz',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_10000Hz') is None:
        # initialise res_10000Hz
        res_10000Hz = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_10000Hz',
        )
    # create speaker 'sound_12500'
    deviceManager.addDevice(
        deviceName='sound_12500',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_12500') is None:
        # initialise res_12500
        res_12500 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_12500',
        )
    # create speaker 'sound_15000'
    deviceManager.addDevice(
        deviceName='sound_15000',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('res_15000Hz') is None:
        # initialise res_15000Hz
        res_15000Hz = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='res_15000Hz',
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
        text='Hello\n\nWelcome to the PsychoPy script developed by Eli, for testing average reaction time depending on different colours. I really appreciate your participation as every piece of data contributes to the final conclusion\n\nPress the space bar when you have finished reading',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    res_intro = keyboard.Keyboard(deviceName='res_intro')
    
    # --- Initialize components for Routine "howitworks" ---
    text_howitworks = visual.TextStim(win=win, name='text_howitworks',
        text='This test is made of two parts\nVisual and Auditory\n\nThis test aims to test your reaction time. When you hear the sound being played or the image being shown, press the space bar on the keyboard as soon as you can. Do not try to predict the time that the stimulus will start as all stimuli are generated at random timings\n\nPlease move the mouse cursor to the edge of the screen or off screen to reduce interference. If the computer stops working during the test, please tell me\n\nThe first one will be the test run for you familiarise with this test\n\nPress the space bar when you have finished reading\n',
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
    
    # --- Initialize components for Routine "red0_75" ---
    polygon_red_0_75 = visual.ShapeStim(
        win=win, name='polygon_red_0_75',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.5000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_red_0_75 = keyboard.Keyboard(deviceName='res_red_0_75')
    
    # --- Initialize components for Routine "red0_875" ---
    polygon_red_0_875 = visual.ShapeStim(
        win=win, name='polygon_red_0_875',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.7500, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_red_0_875 = keyboard.Keyboard(deviceName='res_red_0_875')
    
    # --- Initialize components for Routine "red1" ---
    polygon_red_1 = visual.ShapeStim(
        win=win, name='polygon_red_1',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_red_1 = keyboard.Keyboard(deviceName='res_red_1')
    
    # --- Initialize components for Routine "yellow0_5" ---
    polygon_0_5 = visual.ShapeStim(
        win=win, name='polygon_0_5',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_yellow_0_5 = keyboard.Keyboard(deviceName='res_yellow_0_5')
    
    # --- Initialize components for Routine "yellow0_625" ---
    polygon_yellow_0_625 = visual.ShapeStim(
        win=win, name='polygon_yellow_0_625',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2500, 0.2500, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_yellow_0_625 = keyboard.Keyboard(deviceName='res_yellow_0_625')
    
    # --- Initialize components for Routine "yellow0_75" ---
    polygon_yellow_0_75 = visual.ShapeStim(
        win=win, name='polygon_yellow_0_75',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.5000, 0.5000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_yellow_0_75 = keyboard.Keyboard(deviceName='res_yellow_0_75')
    
    # --- Initialize components for Routine "yellow0_875" ---
    polygon_yellow_0_875 = visual.ShapeStim(
        win=win, name='polygon_yellow_0_875',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.7500, 0.7500, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_yellow_0_875 = keyboard.Keyboard(deviceName='res_yellow_0_875')
    
    # --- Initialize components for Routine "yellow1" ---
    polygon_yellow_1 = visual.ShapeStim(
        win=win, name='polygon_yellow_1',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, 1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_yellow_1 = keyboard.Keyboard(deviceName='res_yellow_1')
    
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
    
    # --- Initialize components for Routine "blue0_75" ---
    polygon_blue_0_75 = visual.ShapeStim(
        win=win, name='polygon_blue_0_75',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -0.0000, 0.5000],
        opacity=None, depth=0.0, interpolate=True)
    res_blue_0_75 = keyboard.Keyboard(deviceName='res_blue_0_75')
    
    # --- Initialize components for Routine "blue0_875" ---
    polygon_blue_0_875 = visual.ShapeStim(
        win=win, name='polygon_blue_0_875',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, 0.1667, 0.7500],
        opacity=None, depth=0.0, interpolate=True)
    res_blue_0_875 = keyboard.Keyboard(deviceName='res_blue_0_875')
    
    # --- Initialize components for Routine "blue1" ---
    polygon_blue_1 = visual.ShapeStim(
        win=win, name='polygon_blue_1',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, 0.3333, 1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_blue_1 = keyboard.Keyboard(deviceName='res_blue_1')
    
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
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-0.5833, 0.2500, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_green_0_625 = keyboard.Keyboard(deviceName='res_green_0_625')
    
    # --- Initialize components for Routine "green0_75" ---
    polygon_green_0_75 = visual.ShapeStim(
        win=win, name='polygon_green_0_75',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-0.5000, 0.5000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_green_0_75 = keyboard.Keyboard(deviceName='res_green_0_75')
    
    # --- Initialize components for Routine "green0_875" ---
    polygon_green_0_875 = visual.ShapeStim(
        win=win, name='polygon_green_0_875',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-0.4167, 0.7500, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_green_0_875 = keyboard.Keyboard(deviceName='res_green_0_875')
    
    # --- Initialize components for Routine "green1" ---
    polygon_green_1 = visual.ShapeStim(
        win=win, name='polygon_green_1',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-0.3333, 1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_green_1 = keyboard.Keyboard(deviceName='res_green_1')
    
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
    
    # --- Initialize components for Routine "purple0_75" ---
    polygon_purple_0_75 = visual.ShapeStim(
        win=win, name='polygon_purple_0_75',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.5000, -1.0000, 0.5000],
        opacity=None, depth=0.0, interpolate=True)
    res_purple_0_75 = keyboard.Keyboard(deviceName='res_purple_0_75')
    
    # --- Initialize components for Routine "purple0_875" ---
    polygon_purple_0_875 = visual.ShapeStim(
        win=win, name='polygon_purple_0_875',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.7500, -1.0000, 0.7500],
        opacity=None, depth=0.0, interpolate=True)
    res_purple_0_875 = keyboard.Keyboard(deviceName='res_purple_0_875')
    
    # --- Initialize components for Routine "purple1" ---
    polygon_purple_1 = visual.ShapeStim(
        win=win, name='polygon_purple_1',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_purple_1 = keyboard.Keyboard(deviceName='res_purple_1')
    
    # --- Initialize components for Routine "orange0_5" ---
    polygon_orange_0_5 = visual.ShapeStim(
        win=win, name='polygon_orange_0_5',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, -0.4167, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_orange_0_5 = keyboard.Keyboard(deviceName='res_orange_0_5')
    
    # --- Initialize components for Routine "orange0_625" ---
    polygon_orange_0_625 = visual.ShapeStim(
        win=win, name='polygon_orange_0_625',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2500, -0.2708, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_orange_0_625 = keyboard.Keyboard(deviceName='res_orange_0_625')
    
    # --- Initialize components for Routine "orange0_75" ---
    polygon_orange_0_75 = visual.ShapeStim(
        win=win, name='polygon_orange_0_75',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.5000, -0.1250, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_orange_0_75 = keyboard.Keyboard(deviceName='res_orange_0_75')
    
    # --- Initialize components for Routine "orange0_875" ---
    polygon_res_0_875 = visual.ShapeStim(
        win=win, name='polygon_res_0_875',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.7500, 0.0208, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_orange_0_875 = keyboard.Keyboard(deviceName='res_orange_0_875')
    
    # --- Initialize components for Routine "orange1" ---
    polygon_orange_1 = visual.ShapeStim(
        win=win, name='polygon_orange_1',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, 0.1667, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    res_orange_1 = keyboard.Keyboard(deviceName='res_orange_1')
    
    # --- Initialize components for Routine "audiointro" ---
    audiotext = visual.TextStim(win=win, name='audiotext',
        text='You have now finished all visual stimuli \n\nThe next part is made of a series of sound stimuli with different frequencies. As you did for the visual stimuli, press the space bar when you hear the sound. \n\nThe first stimulus is your test run for you to familiarise with the test\n\nPress space bar when you have finished reading\n\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    audiointro_res = keyboard.Keyboard(deviceName='audiointro_res')
    
    # --- Initialize components for Routine "audiotest" ---
    sound_testrun = sound.Sound(
        'audio files/2500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_testrun',    name='sound_testrun'
    )
    sound_testrun.setVolume(1.0)
    res_audio_testrun = keyboard.Keyboard(deviceName='res_audio_testrun')
    
    # --- Initialize components for Routine "audiotestpassed" ---
    autest_passed = visual.TextStim(win=win, name='autest_passed',
        text='You have done the testrun\n\n\n\nPress the space bar when you have finished reading',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    res_testpassed = keyboard.Keyboard(deviceName='res_testpassed')
    
    # --- Initialize components for Routine "audio_500Hz_0_25" ---
    sound_500Hz_0_25 = sound.Sound(
        'audio files/500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_500Hz_0_25',    name='sound_500Hz_0_25'
    )
    sound_500Hz_0_25.setVolume(0.25)
    res_500Hz_0_25 = keyboard.Keyboard(deviceName='res_500Hz_0_25')
    
    # --- Initialize components for Routine "audio_500Hz_0_5" ---
    sound_500Hz_0_5 = sound.Sound(
        'audio files/500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_500Hz_0_5',    name='sound_500Hz_0_5'
    )
    sound_500Hz_0_5.setVolume(0.5)
    res_500Hz_0_5 = keyboard.Keyboard(deviceName='res_500Hz_0_5')
    
    # --- Initialize components for Routine "audio_500Hz_0_75" ---
    sound_500Hz_0_75 = sound.Sound(
        'audio files/500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_500Hz_0_75',    name='sound_500Hz_0_75'
    )
    sound_500Hz_0_75.setVolume(0.75)
    res_500Hz_0_75 = keyboard.Keyboard(deviceName='res_500Hz_0_75')
    
    # --- Initialize components for Routine "audio_500Hz_1" ---
    sound_500Hz = sound.Sound(
        'audio files/500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_500Hz',    name='sound_500Hz'
    )
    sound_500Hz.setVolume(1.0)
    res_500Hz = keyboard.Keyboard(deviceName='res_500Hz')
    
    # --- Initialize components for Routine "audio_2500Hz_0_25" ---
    sound_2500Hz_0_25 = sound.Sound(
        'audio files/2500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_2500Hz_0_25',    name='sound_2500Hz_0_25'
    )
    sound_2500Hz_0_25.setVolume(0.25)
    res_2500Hz_0_25 = keyboard.Keyboard(deviceName='res_2500Hz_0_25')
    
    # --- Initialize components for Routine "audio_2500Hz" ---
    sound_2500Hz = sound.Sound(
        'audio files/2500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_2500Hz',    name='sound_2500Hz'
    )
    sound_2500Hz.setVolume(1.0)
    res_2500Hz = keyboard.Keyboard(deviceName='res_2500Hz')
    
    # --- Initialize components for Routine "audio_5000Hz" ---
    sound_5000Hz = sound.Sound(
        'audio files/5000.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_5000Hz',    name='sound_5000Hz'
    )
    sound_5000Hz.setVolume(1.0)
    res_5000Hz = keyboard.Keyboard(deviceName='res_5000Hz')
    
    # --- Initialize components for Routine "audio_7500Hz" ---
    sound_7500Hz = sound.Sound(
        'audio files/7500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_7500Hz',    name='sound_7500Hz'
    )
    sound_7500Hz.setVolume(1.0)
    res_7500Hz = keyboard.Keyboard(deviceName='res_7500Hz')
    
    # --- Initialize components for Routine "audio_10000Hz" ---
    sound_10000Hz = sound.Sound(
        'audio files/10000.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_10000Hz',    name='sound_10000Hz'
    )
    sound_10000Hz.setVolume(1.0)
    res_10000Hz = keyboard.Keyboard(deviceName='res_10000Hz')
    
    # --- Initialize components for Routine "audio_12500Hz" ---
    sound_12500 = sound.Sound(
        'audio files/12500.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_12500',    name='sound_12500'
    )
    sound_12500.setVolume(1.0)
    res_12500 = keyboard.Keyboard(deviceName='res_12500')
    
    # --- Initialize components for Routine "audio_15000Hz" ---
    sound_15000 = sound.Sound(
        'audio files/15000.wav', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_15000',    name='sound_15000'
    )
    sound_15000.setVolume(1.0)
    res_15000Hz = keyboard.Keyboard(deviceName='res_15000Hz')
    
    # --- Initialize components for Routine "outro" ---
    text_outro = visual.TextStim(win=win, name='text_outro',
        text='You have now finished the whole test\n\nThank you to your participation in the experiment\n\nPlease do not forget to apply hand sanitiser on the way out\n\nYou may press Esc to end the test',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
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
    res_intro.keys = []
    res_intro.rt = []
    _res_intro_allKeys = []
    # keep track of which components have finished
    introComponents = [text, res_intro]
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
        
        # *res_intro* updates
        waitOnFlip = False
        
        # if res_intro is starting this frame...
        if res_intro.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            res_intro.frameNStart = frameN  # exact frame index
            res_intro.tStart = t  # local t and not account for scr refresh
            res_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_intro.started')
            # update status
            res_intro.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_intro.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_intro.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_intro.status == STARTED and not waitOnFlip:
            theseKeys = res_intro.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_intro_allKeys.extend(theseKeys)
            if len(_res_intro_allKeys):
                res_intro.keys = _res_intro_allKeys[-1].name  # just the last key pressed
                res_intro.rt = _res_intro_allKeys[-1].rt
                res_intro.duration = _res_intro_allKeys[-1].duration
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
    if res_intro.keys in ['', [], None]:  # No response was made
        res_intro.keys = None
    thisExp.addData('res_intro.keys',res_intro.keys)
    if res_intro.keys != None:  # we had a response
        thisExp.addData('res_intro.rt', res_intro.rt)
        thisExp.addData('res_intro.duration', res_intro.duration)
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
    howitworksComponents = [text_howitworks, endhowitworks]
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
        
        # *text_howitworks* updates
        
        # if text_howitworks is starting this frame...
        if text_howitworks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_howitworks.frameNStart = frameN  # exact frame index
            text_howitworks.tStart = t  # local t and not account for scr refresh
            text_howitworks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_howitworks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_howitworks.started')
            # update status
            text_howitworks.status = STARTED
            text_howitworks.setAutoDraw(True)
        
        # if text_howitworks is active this frame...
        if text_howitworks.status == STARTED:
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
    
    # set up handler to look after randomisation of conditions etc
    redloop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='redloop')
    thisExp.addLoop(redloop)  # add the loop to the experiment
    thisRedloop = redloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRedloop.rgb)
    if thisRedloop != None:
        for paramName in thisRedloop:
            globals()[paramName] = thisRedloop[paramName]
    
    for thisRedloop in redloop:
        currentLoop = redloop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRedloop.rgb)
        if thisRedloop != None:
            for paramName in thisRedloop:
                globals()[paramName] = thisRedloop[paramName]
        
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
        redloop.addData('res_red_0_5.keys',res_red_0_5.keys)
        if res_red_0_5.keys != None:  # we had a response
            redloop.addData('res_red_0_5.rt', res_red_0_5.rt)
            redloop.addData('res_red_0_5.duration', res_red_0_5.duration)
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
        redloop.addData('res_red_0_625.keys',res_red_0_625.keys)
        if res_red_0_625.keys != None:  # we had a response
            redloop.addData('res_red_0_625.rt', res_red_0_625.rt)
            redloop.addData('res_red_0_625.duration', res_red_0_625.duration)
        # the Routine "red0_625" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "red0_75" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('red0_75.started', globalClock.getTime(format='float'))
        res_red_0_75.keys = []
        res_red_0_75.rt = []
        _res_red_0_75_allKeys = []
        # keep track of which components have finished
        red0_75Components = [polygon_red_0_75, res_red_0_75]
        for thisComponent in red0_75Components:
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
        
        # --- Run Routine "red0_75" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_red_0_75* updates
            
            # if polygon_red_0_75 is starting this frame...
            if polygon_red_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                polygon_red_0_75.frameNStart = frameN  # exact frame index
                polygon_red_0_75.tStart = t  # local t and not account for scr refresh
                polygon_red_0_75.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_red_0_75, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_red_0_75.started')
                # update status
                polygon_red_0_75.status = STARTED
                polygon_red_0_75.setAutoDraw(True)
            
            # if polygon_red_0_75 is active this frame...
            if polygon_red_0_75.status == STARTED:
                # update params
                pass
            
            # *res_red_0_75* updates
            waitOnFlip = False
            
            # if res_red_0_75 is starting this frame...
            if res_red_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                res_red_0_75.frameNStart = frameN  # exact frame index
                res_red_0_75.tStart = t  # local t and not account for scr refresh
                res_red_0_75.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(res_red_0_75, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'res_red_0_75.started')
                # update status
                res_red_0_75.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(res_red_0_75.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(res_red_0_75.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if res_red_0_75.status == STARTED and not waitOnFlip:
                theseKeys = res_red_0_75.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
                _res_red_0_75_allKeys.extend(theseKeys)
                if len(_res_red_0_75_allKeys):
                    res_red_0_75.keys = _res_red_0_75_allKeys[-1].name  # just the last key pressed
                    res_red_0_75.rt = _res_red_0_75_allKeys[-1].rt
                    res_red_0_75.duration = _res_red_0_75_allKeys[-1].duration
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
            for thisComponent in red0_75Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "red0_75" ---
        for thisComponent in red0_75Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('red0_75.stopped', globalClock.getTime(format='float'))
        # check responses
        if res_red_0_75.keys in ['', [], None]:  # No response was made
            res_red_0_75.keys = None
        redloop.addData('res_red_0_75.keys',res_red_0_75.keys)
        if res_red_0_75.keys != None:  # we had a response
            redloop.addData('res_red_0_75.rt', res_red_0_75.rt)
            redloop.addData('res_red_0_75.duration', res_red_0_75.duration)
        # the Routine "red0_75" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "red0_875" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('red0_875.started', globalClock.getTime(format='float'))
        res_red_0_875.keys = []
        res_red_0_875.rt = []
        _res_red_0_875_allKeys = []
        # keep track of which components have finished
        red0_875Components = [polygon_red_0_875, res_red_0_875]
        for thisComponent in red0_875Components:
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
        
        # --- Run Routine "red0_875" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_red_0_875* updates
            
            # if polygon_red_0_875 is starting this frame...
            if polygon_red_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                polygon_red_0_875.frameNStart = frameN  # exact frame index
                polygon_red_0_875.tStart = t  # local t and not account for scr refresh
                polygon_red_0_875.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_red_0_875, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_red_0_875.started')
                # update status
                polygon_red_0_875.status = STARTED
                polygon_red_0_875.setAutoDraw(True)
            
            # if polygon_red_0_875 is active this frame...
            if polygon_red_0_875.status == STARTED:
                # update params
                pass
            
            # *res_red_0_875* updates
            waitOnFlip = False
            
            # if res_red_0_875 is starting this frame...
            if res_red_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                res_red_0_875.frameNStart = frameN  # exact frame index
                res_red_0_875.tStart = t  # local t and not account for scr refresh
                res_red_0_875.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(res_red_0_875, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'res_red_0_875.started')
                # update status
                res_red_0_875.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(res_red_0_875.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(res_red_0_875.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if res_red_0_875.status == STARTED and not waitOnFlip:
                theseKeys = res_red_0_875.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
                _res_red_0_875_allKeys.extend(theseKeys)
                if len(_res_red_0_875_allKeys):
                    res_red_0_875.keys = _res_red_0_875_allKeys[-1].name  # just the last key pressed
                    res_red_0_875.rt = _res_red_0_875_allKeys[-1].rt
                    res_red_0_875.duration = _res_red_0_875_allKeys[-1].duration
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
            for thisComponent in red0_875Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "red0_875" ---
        for thisComponent in red0_875Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('red0_875.stopped', globalClock.getTime(format='float'))
        # check responses
        if res_red_0_875.keys in ['', [], None]:  # No response was made
            res_red_0_875.keys = None
        redloop.addData('res_red_0_875.keys',res_red_0_875.keys)
        if res_red_0_875.keys != None:  # we had a response
            redloop.addData('res_red_0_875.rt', res_red_0_875.rt)
            redloop.addData('res_red_0_875.duration', res_red_0_875.duration)
        # the Routine "red0_875" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "red1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('red1.started', globalClock.getTime(format='float'))
        res_red_1.keys = []
        res_red_1.rt = []
        _res_red_1_allKeys = []
        # keep track of which components have finished
        red1Components = [polygon_red_1, res_red_1]
        for thisComponent in red1Components:
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
        
        # --- Run Routine "red1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_red_1* updates
            
            # if polygon_red_1 is starting this frame...
            if polygon_red_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                polygon_red_1.frameNStart = frameN  # exact frame index
                polygon_red_1.tStart = t  # local t and not account for scr refresh
                polygon_red_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_red_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_red_1.started')
                # update status
                polygon_red_1.status = STARTED
                polygon_red_1.setAutoDraw(True)
            
            # if polygon_red_1 is active this frame...
            if polygon_red_1.status == STARTED:
                # update params
                pass
            
            # *res_red_1* updates
            waitOnFlip = False
            
            # if res_red_1 is starting this frame...
            if res_red_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                res_red_1.frameNStart = frameN  # exact frame index
                res_red_1.tStart = t  # local t and not account for scr refresh
                res_red_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(res_red_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'res_red_1.started')
                # update status
                res_red_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(res_red_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(res_red_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if res_red_1.status == STARTED and not waitOnFlip:
                theseKeys = res_red_1.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
                _res_red_1_allKeys.extend(theseKeys)
                if len(_res_red_1_allKeys):
                    res_red_1.keys = _res_red_1_allKeys[-1].name  # just the last key pressed
                    res_red_1.rt = _res_red_1_allKeys[-1].rt
                    res_red_1.duration = _res_red_1_allKeys[-1].duration
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
            for thisComponent in red1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "red1" ---
        for thisComponent in red1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('red1.stopped', globalClock.getTime(format='float'))
        # check responses
        if res_red_1.keys in ['', [], None]:  # No response was made
            res_red_1.keys = None
        redloop.addData('res_red_1.keys',res_red_1.keys)
        if res_red_1.keys != None:  # we had a response
            redloop.addData('res_red_1.rt', res_red_1.rt)
            redloop.addData('res_red_1.duration', res_red_1.duration)
        # the Routine "red1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 3.0 repeats of 'redloop'
    
    
    # --- Prepare to start Routine "yellow0_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('yellow0_5.started', globalClock.getTime(format='float'))
    res_yellow_0_5.keys = []
    res_yellow_0_5.rt = []
    _res_yellow_0_5_allKeys = []
    # keep track of which components have finished
    yellow0_5Components = [polygon_0_5, res_yellow_0_5]
    for thisComponent in yellow0_5Components:
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
    
    # --- Run Routine "yellow0_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_0_5* updates
        
        # if polygon_0_5 is starting this frame...
        if polygon_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_0_5.frameNStart = frameN  # exact frame index
            polygon_0_5.tStart = t  # local t and not account for scr refresh
            polygon_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_0_5.started')
            # update status
            polygon_0_5.status = STARTED
            polygon_0_5.setAutoDraw(True)
        
        # if polygon_0_5 is active this frame...
        if polygon_0_5.status == STARTED:
            # update params
            pass
        
        # *res_yellow_0_5* updates
        waitOnFlip = False
        
        # if res_yellow_0_5 is starting this frame...
        if res_yellow_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_yellow_0_5.frameNStart = frameN  # exact frame index
            res_yellow_0_5.tStart = t  # local t and not account for scr refresh
            res_yellow_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_yellow_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_yellow_0_5.started')
            # update status
            res_yellow_0_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_yellow_0_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_yellow_0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_yellow_0_5.status == STARTED and not waitOnFlip:
            theseKeys = res_yellow_0_5.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_yellow_0_5_allKeys.extend(theseKeys)
            if len(_res_yellow_0_5_allKeys):
                res_yellow_0_5.keys = _res_yellow_0_5_allKeys[-1].name  # just the last key pressed
                res_yellow_0_5.rt = _res_yellow_0_5_allKeys[-1].rt
                res_yellow_0_5.duration = _res_yellow_0_5_allKeys[-1].duration
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
        for thisComponent in yellow0_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "yellow0_5" ---
    for thisComponent in yellow0_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('yellow0_5.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_yellow_0_5.keys in ['', [], None]:  # No response was made
        res_yellow_0_5.keys = None
    thisExp.addData('res_yellow_0_5.keys',res_yellow_0_5.keys)
    if res_yellow_0_5.keys != None:  # we had a response
        thisExp.addData('res_yellow_0_5.rt', res_yellow_0_5.rt)
        thisExp.addData('res_yellow_0_5.duration', res_yellow_0_5.duration)
    thisExp.nextEntry()
    # the Routine "yellow0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "yellow0_625" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('yellow0_625.started', globalClock.getTime(format='float'))
    res_yellow_0_625.keys = []
    res_yellow_0_625.rt = []
    _res_yellow_0_625_allKeys = []
    # keep track of which components have finished
    yellow0_625Components = [polygon_yellow_0_625, res_yellow_0_625]
    for thisComponent in yellow0_625Components:
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
    
    # --- Run Routine "yellow0_625" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_yellow_0_625* updates
        
        # if polygon_yellow_0_625 is starting this frame...
        if polygon_yellow_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_yellow_0_625.frameNStart = frameN  # exact frame index
            polygon_yellow_0_625.tStart = t  # local t and not account for scr refresh
            polygon_yellow_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_yellow_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_yellow_0_625.started')
            # update status
            polygon_yellow_0_625.status = STARTED
            polygon_yellow_0_625.setAutoDraw(True)
        
        # if polygon_yellow_0_625 is active this frame...
        if polygon_yellow_0_625.status == STARTED:
            # update params
            pass
        
        # *res_yellow_0_625* updates
        waitOnFlip = False
        
        # if res_yellow_0_625 is starting this frame...
        if res_yellow_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_yellow_0_625.frameNStart = frameN  # exact frame index
            res_yellow_0_625.tStart = t  # local t and not account for scr refresh
            res_yellow_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_yellow_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_yellow_0_625.started')
            # update status
            res_yellow_0_625.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_yellow_0_625.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_yellow_0_625.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_yellow_0_625.status == STARTED and not waitOnFlip:
            theseKeys = res_yellow_0_625.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_yellow_0_625_allKeys.extend(theseKeys)
            if len(_res_yellow_0_625_allKeys):
                res_yellow_0_625.keys = _res_yellow_0_625_allKeys[-1].name  # just the last key pressed
                res_yellow_0_625.rt = _res_yellow_0_625_allKeys[-1].rt
                res_yellow_0_625.duration = _res_yellow_0_625_allKeys[-1].duration
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
        for thisComponent in yellow0_625Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "yellow0_625" ---
    for thisComponent in yellow0_625Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('yellow0_625.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_yellow_0_625.keys in ['', [], None]:  # No response was made
        res_yellow_0_625.keys = None
    thisExp.addData('res_yellow_0_625.keys',res_yellow_0_625.keys)
    if res_yellow_0_625.keys != None:  # we had a response
        thisExp.addData('res_yellow_0_625.rt', res_yellow_0_625.rt)
        thisExp.addData('res_yellow_0_625.duration', res_yellow_0_625.duration)
    thisExp.nextEntry()
    # the Routine "yellow0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "yellow0_75" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('yellow0_75.started', globalClock.getTime(format='float'))
    res_yellow_0_75.keys = []
    res_yellow_0_75.rt = []
    _res_yellow_0_75_allKeys = []
    # keep track of which components have finished
    yellow0_75Components = [polygon_yellow_0_75, res_yellow_0_75]
    for thisComponent in yellow0_75Components:
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
    
    # --- Run Routine "yellow0_75" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_yellow_0_75* updates
        
        # if polygon_yellow_0_75 is starting this frame...
        if polygon_yellow_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_yellow_0_75.frameNStart = frameN  # exact frame index
            polygon_yellow_0_75.tStart = t  # local t and not account for scr refresh
            polygon_yellow_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_yellow_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_yellow_0_75.started')
            # update status
            polygon_yellow_0_75.status = STARTED
            polygon_yellow_0_75.setAutoDraw(True)
        
        # if polygon_yellow_0_75 is active this frame...
        if polygon_yellow_0_75.status == STARTED:
            # update params
            pass
        
        # *res_yellow_0_75* updates
        waitOnFlip = False
        
        # if res_yellow_0_75 is starting this frame...
        if res_yellow_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_yellow_0_75.frameNStart = frameN  # exact frame index
            res_yellow_0_75.tStart = t  # local t and not account for scr refresh
            res_yellow_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_yellow_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_yellow_0_75.started')
            # update status
            res_yellow_0_75.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_yellow_0_75.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_yellow_0_75.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_yellow_0_75.status == STARTED and not waitOnFlip:
            theseKeys = res_yellow_0_75.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_yellow_0_75_allKeys.extend(theseKeys)
            if len(_res_yellow_0_75_allKeys):
                res_yellow_0_75.keys = _res_yellow_0_75_allKeys[-1].name  # just the last key pressed
                res_yellow_0_75.rt = _res_yellow_0_75_allKeys[-1].rt
                res_yellow_0_75.duration = _res_yellow_0_75_allKeys[-1].duration
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
        for thisComponent in yellow0_75Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "yellow0_75" ---
    for thisComponent in yellow0_75Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('yellow0_75.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_yellow_0_75.keys in ['', [], None]:  # No response was made
        res_yellow_0_75.keys = None
    thisExp.addData('res_yellow_0_75.keys',res_yellow_0_75.keys)
    if res_yellow_0_75.keys != None:  # we had a response
        thisExp.addData('res_yellow_0_75.rt', res_yellow_0_75.rt)
        thisExp.addData('res_yellow_0_75.duration', res_yellow_0_75.duration)
    thisExp.nextEntry()
    # the Routine "yellow0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "yellow0_875" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('yellow0_875.started', globalClock.getTime(format='float'))
    res_yellow_0_875.keys = []
    res_yellow_0_875.rt = []
    _res_yellow_0_875_allKeys = []
    # keep track of which components have finished
    yellow0_875Components = [polygon_yellow_0_875, res_yellow_0_875]
    for thisComponent in yellow0_875Components:
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
    
    # --- Run Routine "yellow0_875" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_yellow_0_875* updates
        
        # if polygon_yellow_0_875 is starting this frame...
        if polygon_yellow_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_yellow_0_875.frameNStart = frameN  # exact frame index
            polygon_yellow_0_875.tStart = t  # local t and not account for scr refresh
            polygon_yellow_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_yellow_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_yellow_0_875.started')
            # update status
            polygon_yellow_0_875.status = STARTED
            polygon_yellow_0_875.setAutoDraw(True)
        
        # if polygon_yellow_0_875 is active this frame...
        if polygon_yellow_0_875.status == STARTED:
            # update params
            pass
        
        # *res_yellow_0_875* updates
        waitOnFlip = False
        
        # if res_yellow_0_875 is starting this frame...
        if res_yellow_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_yellow_0_875.frameNStart = frameN  # exact frame index
            res_yellow_0_875.tStart = t  # local t and not account for scr refresh
            res_yellow_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_yellow_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_yellow_0_875.started')
            # update status
            res_yellow_0_875.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_yellow_0_875.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_yellow_0_875.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_yellow_0_875.status == STARTED and not waitOnFlip:
            theseKeys = res_yellow_0_875.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_yellow_0_875_allKeys.extend(theseKeys)
            if len(_res_yellow_0_875_allKeys):
                res_yellow_0_875.keys = _res_yellow_0_875_allKeys[-1].name  # just the last key pressed
                res_yellow_0_875.rt = _res_yellow_0_875_allKeys[-1].rt
                res_yellow_0_875.duration = _res_yellow_0_875_allKeys[-1].duration
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
        for thisComponent in yellow0_875Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "yellow0_875" ---
    for thisComponent in yellow0_875Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('yellow0_875.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_yellow_0_875.keys in ['', [], None]:  # No response was made
        res_yellow_0_875.keys = None
    thisExp.addData('res_yellow_0_875.keys',res_yellow_0_875.keys)
    if res_yellow_0_875.keys != None:  # we had a response
        thisExp.addData('res_yellow_0_875.rt', res_yellow_0_875.rt)
        thisExp.addData('res_yellow_0_875.duration', res_yellow_0_875.duration)
    thisExp.nextEntry()
    # the Routine "yellow0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "yellow1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('yellow1.started', globalClock.getTime(format='float'))
    res_yellow_1.keys = []
    res_yellow_1.rt = []
    _res_yellow_1_allKeys = []
    # keep track of which components have finished
    yellow1Components = [polygon_yellow_1, res_yellow_1]
    for thisComponent in yellow1Components:
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
    
    # --- Run Routine "yellow1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_yellow_1* updates
        
        # if polygon_yellow_1 is starting this frame...
        if polygon_yellow_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_yellow_1.frameNStart = frameN  # exact frame index
            polygon_yellow_1.tStart = t  # local t and not account for scr refresh
            polygon_yellow_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_yellow_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_yellow_1.started')
            # update status
            polygon_yellow_1.status = STARTED
            polygon_yellow_1.setAutoDraw(True)
        
        # if polygon_yellow_1 is active this frame...
        if polygon_yellow_1.status == STARTED:
            # update params
            pass
        
        # *res_yellow_1* updates
        waitOnFlip = False
        
        # if res_yellow_1 is starting this frame...
        if res_yellow_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_yellow_1.frameNStart = frameN  # exact frame index
            res_yellow_1.tStart = t  # local t and not account for scr refresh
            res_yellow_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_yellow_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_yellow_1.started')
            # update status
            res_yellow_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_yellow_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_yellow_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_yellow_1.status == STARTED and not waitOnFlip:
            theseKeys = res_yellow_1.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_yellow_1_allKeys.extend(theseKeys)
            if len(_res_yellow_1_allKeys):
                res_yellow_1.keys = _res_yellow_1_allKeys[-1].name  # just the last key pressed
                res_yellow_1.rt = _res_yellow_1_allKeys[-1].rt
                res_yellow_1.duration = _res_yellow_1_allKeys[-1].duration
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
        for thisComponent in yellow1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "yellow1" ---
    for thisComponent in yellow1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('yellow1.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_yellow_1.keys in ['', [], None]:  # No response was made
        res_yellow_1.keys = None
    thisExp.addData('res_yellow_1.keys',res_yellow_1.keys)
    if res_yellow_1.keys != None:  # we had a response
        thisExp.addData('res_yellow_1.rt', res_yellow_1.rt)
        thisExp.addData('res_yellow_1.duration', res_yellow_1.duration)
    thisExp.nextEntry()
    # the Routine "yellow1" was not non-slip safe, so reset the non-slip timer
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
    
    # --- Prepare to start Routine "blue0_75" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blue0_75.started', globalClock.getTime(format='float'))
    res_blue_0_75.keys = []
    res_blue_0_75.rt = []
    _res_blue_0_75_allKeys = []
    # keep track of which components have finished
    blue0_75Components = [polygon_blue_0_75, res_blue_0_75]
    for thisComponent in blue0_75Components:
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
    
    # --- Run Routine "blue0_75" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_blue_0_75* updates
        
        # if polygon_blue_0_75 is starting this frame...
        if polygon_blue_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_blue_0_75.frameNStart = frameN  # exact frame index
            polygon_blue_0_75.tStart = t  # local t and not account for scr refresh
            polygon_blue_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_blue_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_blue_0_75.started')
            # update status
            polygon_blue_0_75.status = STARTED
            polygon_blue_0_75.setAutoDraw(True)
        
        # if polygon_blue_0_75 is active this frame...
        if polygon_blue_0_75.status == STARTED:
            # update params
            pass
        
        # *res_blue_0_75* updates
        waitOnFlip = False
        
        # if res_blue_0_75 is starting this frame...
        if res_blue_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_blue_0_75.frameNStart = frameN  # exact frame index
            res_blue_0_75.tStart = t  # local t and not account for scr refresh
            res_blue_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_blue_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_blue_0_75.started')
            # update status
            res_blue_0_75.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_blue_0_75.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_blue_0_75.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_blue_0_75.status == STARTED and not waitOnFlip:
            theseKeys = res_blue_0_75.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_blue_0_75_allKeys.extend(theseKeys)
            if len(_res_blue_0_75_allKeys):
                res_blue_0_75.keys = _res_blue_0_75_allKeys[-1].name  # just the last key pressed
                res_blue_0_75.rt = _res_blue_0_75_allKeys[-1].rt
                res_blue_0_75.duration = _res_blue_0_75_allKeys[-1].duration
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
        for thisComponent in blue0_75Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blue0_75" ---
    for thisComponent in blue0_75Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blue0_75.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_blue_0_75.keys in ['', [], None]:  # No response was made
        res_blue_0_75.keys = None
    thisExp.addData('res_blue_0_75.keys',res_blue_0_75.keys)
    if res_blue_0_75.keys != None:  # we had a response
        thisExp.addData('res_blue_0_75.rt', res_blue_0_75.rt)
        thisExp.addData('res_blue_0_75.duration', res_blue_0_75.duration)
    thisExp.nextEntry()
    # the Routine "blue0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blue0_875" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blue0_875.started', globalClock.getTime(format='float'))
    res_blue_0_875.keys = []
    res_blue_0_875.rt = []
    _res_blue_0_875_allKeys = []
    # keep track of which components have finished
    blue0_875Components = [polygon_blue_0_875, res_blue_0_875]
    for thisComponent in blue0_875Components:
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
    
    # --- Run Routine "blue0_875" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_blue_0_875* updates
        
        # if polygon_blue_0_875 is starting this frame...
        if polygon_blue_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_blue_0_875.frameNStart = frameN  # exact frame index
            polygon_blue_0_875.tStart = t  # local t and not account for scr refresh
            polygon_blue_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_blue_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_blue_0_875.started')
            # update status
            polygon_blue_0_875.status = STARTED
            polygon_blue_0_875.setAutoDraw(True)
        
        # if polygon_blue_0_875 is active this frame...
        if polygon_blue_0_875.status == STARTED:
            # update params
            pass
        
        # *res_blue_0_875* updates
        waitOnFlip = False
        
        # if res_blue_0_875 is starting this frame...
        if res_blue_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_blue_0_875.frameNStart = frameN  # exact frame index
            res_blue_0_875.tStart = t  # local t and not account for scr refresh
            res_blue_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_blue_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_blue_0_875.started')
            # update status
            res_blue_0_875.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_blue_0_875.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_blue_0_875.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_blue_0_875.status == STARTED and not waitOnFlip:
            theseKeys = res_blue_0_875.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_blue_0_875_allKeys.extend(theseKeys)
            if len(_res_blue_0_875_allKeys):
                res_blue_0_875.keys = _res_blue_0_875_allKeys[-1].name  # just the last key pressed
                res_blue_0_875.rt = _res_blue_0_875_allKeys[-1].rt
                res_blue_0_875.duration = _res_blue_0_875_allKeys[-1].duration
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
        for thisComponent in blue0_875Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blue0_875" ---
    for thisComponent in blue0_875Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blue0_875.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_blue_0_875.keys in ['', [], None]:  # No response was made
        res_blue_0_875.keys = None
    thisExp.addData('res_blue_0_875.keys',res_blue_0_875.keys)
    if res_blue_0_875.keys != None:  # we had a response
        thisExp.addData('res_blue_0_875.rt', res_blue_0_875.rt)
        thisExp.addData('res_blue_0_875.duration', res_blue_0_875.duration)
    thisExp.nextEntry()
    # the Routine "blue0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blue1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blue1.started', globalClock.getTime(format='float'))
    res_blue_1.keys = []
    res_blue_1.rt = []
    _res_blue_1_allKeys = []
    # keep track of which components have finished
    blue1Components = [polygon_blue_1, res_blue_1]
    for thisComponent in blue1Components:
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
    
    # --- Run Routine "blue1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_blue_1* updates
        
        # if polygon_blue_1 is starting this frame...
        if polygon_blue_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_blue_1.frameNStart = frameN  # exact frame index
            polygon_blue_1.tStart = t  # local t and not account for scr refresh
            polygon_blue_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_blue_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_blue_1.started')
            # update status
            polygon_blue_1.status = STARTED
            polygon_blue_1.setAutoDraw(True)
        
        # if polygon_blue_1 is active this frame...
        if polygon_blue_1.status == STARTED:
            # update params
            pass
        
        # *res_blue_1* updates
        waitOnFlip = False
        
        # if res_blue_1 is starting this frame...
        if res_blue_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_blue_1.frameNStart = frameN  # exact frame index
            res_blue_1.tStart = t  # local t and not account for scr refresh
            res_blue_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_blue_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_blue_1.started')
            # update status
            res_blue_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_blue_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_blue_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_blue_1.status == STARTED and not waitOnFlip:
            theseKeys = res_blue_1.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_blue_1_allKeys.extend(theseKeys)
            if len(_res_blue_1_allKeys):
                res_blue_1.keys = _res_blue_1_allKeys[-1].name  # just the last key pressed
                res_blue_1.rt = _res_blue_1_allKeys[-1].rt
                res_blue_1.duration = _res_blue_1_allKeys[-1].duration
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
        for thisComponent in blue1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blue1" ---
    for thisComponent in blue1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blue1.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_blue_1.keys in ['', [], None]:  # No response was made
        res_blue_1.keys = None
    thisExp.addData('res_blue_1.keys',res_blue_1.keys)
    if res_blue_1.keys != None:  # we had a response
        thisExp.addData('res_blue_1.rt', res_blue_1.rt)
        thisExp.addData('res_blue_1.duration', res_blue_1.duration)
    thisExp.nextEntry()
    # the Routine "blue1" was not non-slip safe, so reset the non-slip timer
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
    
    # --- Prepare to start Routine "green0_75" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('green0_75.started', globalClock.getTime(format='float'))
    res_green_0_75.keys = []
    res_green_0_75.rt = []
    _res_green_0_75_allKeys = []
    # keep track of which components have finished
    green0_75Components = [polygon_green_0_75, res_green_0_75]
    for thisComponent in green0_75Components:
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
    
    # --- Run Routine "green0_75" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_green_0_75* updates
        
        # if polygon_green_0_75 is starting this frame...
        if polygon_green_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_green_0_75.frameNStart = frameN  # exact frame index
            polygon_green_0_75.tStart = t  # local t and not account for scr refresh
            polygon_green_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_green_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_green_0_75.started')
            # update status
            polygon_green_0_75.status = STARTED
            polygon_green_0_75.setAutoDraw(True)
        
        # if polygon_green_0_75 is active this frame...
        if polygon_green_0_75.status == STARTED:
            # update params
            pass
        
        # *res_green_0_75* updates
        waitOnFlip = False
        
        # if res_green_0_75 is starting this frame...
        if res_green_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_green_0_75.frameNStart = frameN  # exact frame index
            res_green_0_75.tStart = t  # local t and not account for scr refresh
            res_green_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_green_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_green_0_75.started')
            # update status
            res_green_0_75.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_green_0_75.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_green_0_75.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_green_0_75.status == STARTED and not waitOnFlip:
            theseKeys = res_green_0_75.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_green_0_75_allKeys.extend(theseKeys)
            if len(_res_green_0_75_allKeys):
                res_green_0_75.keys = _res_green_0_75_allKeys[-1].name  # just the last key pressed
                res_green_0_75.rt = _res_green_0_75_allKeys[-1].rt
                res_green_0_75.duration = _res_green_0_75_allKeys[-1].duration
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
        for thisComponent in green0_75Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "green0_75" ---
    for thisComponent in green0_75Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('green0_75.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_green_0_75.keys in ['', [], None]:  # No response was made
        res_green_0_75.keys = None
    thisExp.addData('res_green_0_75.keys',res_green_0_75.keys)
    if res_green_0_75.keys != None:  # we had a response
        thisExp.addData('res_green_0_75.rt', res_green_0_75.rt)
        thisExp.addData('res_green_0_75.duration', res_green_0_75.duration)
    thisExp.nextEntry()
    # the Routine "green0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "green0_875" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('green0_875.started', globalClock.getTime(format='float'))
    res_green_0_875.keys = []
    res_green_0_875.rt = []
    _res_green_0_875_allKeys = []
    # keep track of which components have finished
    green0_875Components = [polygon_green_0_875, res_green_0_875]
    for thisComponent in green0_875Components:
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
    
    # --- Run Routine "green0_875" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_green_0_875* updates
        
        # if polygon_green_0_875 is starting this frame...
        if polygon_green_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_green_0_875.frameNStart = frameN  # exact frame index
            polygon_green_0_875.tStart = t  # local t and not account for scr refresh
            polygon_green_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_green_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_green_0_875.started')
            # update status
            polygon_green_0_875.status = STARTED
            polygon_green_0_875.setAutoDraw(True)
        
        # if polygon_green_0_875 is active this frame...
        if polygon_green_0_875.status == STARTED:
            # update params
            pass
        
        # *res_green_0_875* updates
        waitOnFlip = False
        
        # if res_green_0_875 is starting this frame...
        if res_green_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_green_0_875.frameNStart = frameN  # exact frame index
            res_green_0_875.tStart = t  # local t and not account for scr refresh
            res_green_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_green_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_green_0_875.started')
            # update status
            res_green_0_875.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_green_0_875.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_green_0_875.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_green_0_875.status == STARTED and not waitOnFlip:
            theseKeys = res_green_0_875.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_green_0_875_allKeys.extend(theseKeys)
            if len(_res_green_0_875_allKeys):
                res_green_0_875.keys = _res_green_0_875_allKeys[-1].name  # just the last key pressed
                res_green_0_875.rt = _res_green_0_875_allKeys[-1].rt
                res_green_0_875.duration = _res_green_0_875_allKeys[-1].duration
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
        for thisComponent in green0_875Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "green0_875" ---
    for thisComponent in green0_875Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('green0_875.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_green_0_875.keys in ['', [], None]:  # No response was made
        res_green_0_875.keys = None
    thisExp.addData('res_green_0_875.keys',res_green_0_875.keys)
    if res_green_0_875.keys != None:  # we had a response
        thisExp.addData('res_green_0_875.rt', res_green_0_875.rt)
        thisExp.addData('res_green_0_875.duration', res_green_0_875.duration)
    thisExp.nextEntry()
    # the Routine "green0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "green1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('green1.started', globalClock.getTime(format='float'))
    res_green_1.keys = []
    res_green_1.rt = []
    _res_green_1_allKeys = []
    # keep track of which components have finished
    green1Components = [polygon_green_1, res_green_1]
    for thisComponent in green1Components:
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
    
    # --- Run Routine "green1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_green_1* updates
        
        # if polygon_green_1 is starting this frame...
        if polygon_green_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_green_1.frameNStart = frameN  # exact frame index
            polygon_green_1.tStart = t  # local t and not account for scr refresh
            polygon_green_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_green_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_green_1.started')
            # update status
            polygon_green_1.status = STARTED
            polygon_green_1.setAutoDraw(True)
        
        # if polygon_green_1 is active this frame...
        if polygon_green_1.status == STARTED:
            # update params
            pass
        
        # *res_green_1* updates
        waitOnFlip = False
        
        # if res_green_1 is starting this frame...
        if res_green_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_green_1.frameNStart = frameN  # exact frame index
            res_green_1.tStart = t  # local t and not account for scr refresh
            res_green_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_green_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_green_1.started')
            # update status
            res_green_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_green_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_green_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_green_1.status == STARTED and not waitOnFlip:
            theseKeys = res_green_1.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_green_1_allKeys.extend(theseKeys)
            if len(_res_green_1_allKeys):
                res_green_1.keys = _res_green_1_allKeys[-1].name  # just the last key pressed
                res_green_1.rt = _res_green_1_allKeys[-1].rt
                res_green_1.duration = _res_green_1_allKeys[-1].duration
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
        for thisComponent in green1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "green1" ---
    for thisComponent in green1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('green1.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_green_1.keys in ['', [], None]:  # No response was made
        res_green_1.keys = None
    thisExp.addData('res_green_1.keys',res_green_1.keys)
    if res_green_1.keys != None:  # we had a response
        thisExp.addData('res_green_1.rt', res_green_1.rt)
        thisExp.addData('res_green_1.duration', res_green_1.duration)
    thisExp.nextEntry()
    # the Routine "green1" was not non-slip safe, so reset the non-slip timer
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
    
    # --- Prepare to start Routine "purple0_75" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('purple0_75.started', globalClock.getTime(format='float'))
    res_purple_0_75.keys = []
    res_purple_0_75.rt = []
    _res_purple_0_75_allKeys = []
    # keep track of which components have finished
    purple0_75Components = [polygon_purple_0_75, res_purple_0_75]
    for thisComponent in purple0_75Components:
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
    
    # --- Run Routine "purple0_75" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_purple_0_75* updates
        
        # if polygon_purple_0_75 is starting this frame...
        if polygon_purple_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_purple_0_75.frameNStart = frameN  # exact frame index
            polygon_purple_0_75.tStart = t  # local t and not account for scr refresh
            polygon_purple_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_purple_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_purple_0_75.started')
            # update status
            polygon_purple_0_75.status = STARTED
            polygon_purple_0_75.setAutoDraw(True)
        
        # if polygon_purple_0_75 is active this frame...
        if polygon_purple_0_75.status == STARTED:
            # update params
            pass
        
        # *res_purple_0_75* updates
        waitOnFlip = False
        
        # if res_purple_0_75 is starting this frame...
        if res_purple_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_purple_0_75.frameNStart = frameN  # exact frame index
            res_purple_0_75.tStart = t  # local t and not account for scr refresh
            res_purple_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_purple_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_purple_0_75.started')
            # update status
            res_purple_0_75.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_purple_0_75.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_purple_0_75.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_purple_0_75.status == STARTED and not waitOnFlip:
            theseKeys = res_purple_0_75.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_purple_0_75_allKeys.extend(theseKeys)
            if len(_res_purple_0_75_allKeys):
                res_purple_0_75.keys = _res_purple_0_75_allKeys[-1].name  # just the last key pressed
                res_purple_0_75.rt = _res_purple_0_75_allKeys[-1].rt
                res_purple_0_75.duration = _res_purple_0_75_allKeys[-1].duration
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
        for thisComponent in purple0_75Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "purple0_75" ---
    for thisComponent in purple0_75Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('purple0_75.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_purple_0_75.keys in ['', [], None]:  # No response was made
        res_purple_0_75.keys = None
    thisExp.addData('res_purple_0_75.keys',res_purple_0_75.keys)
    if res_purple_0_75.keys != None:  # we had a response
        thisExp.addData('res_purple_0_75.rt', res_purple_0_75.rt)
        thisExp.addData('res_purple_0_75.duration', res_purple_0_75.duration)
    thisExp.nextEntry()
    # the Routine "purple0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "purple0_875" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('purple0_875.started', globalClock.getTime(format='float'))
    res_purple_0_875.keys = []
    res_purple_0_875.rt = []
    _res_purple_0_875_allKeys = []
    # keep track of which components have finished
    purple0_875Components = [polygon_purple_0_875, res_purple_0_875]
    for thisComponent in purple0_875Components:
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
    
    # --- Run Routine "purple0_875" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_purple_0_875* updates
        
        # if polygon_purple_0_875 is starting this frame...
        if polygon_purple_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_purple_0_875.frameNStart = frameN  # exact frame index
            polygon_purple_0_875.tStart = t  # local t and not account for scr refresh
            polygon_purple_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_purple_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_purple_0_875.started')
            # update status
            polygon_purple_0_875.status = STARTED
            polygon_purple_0_875.setAutoDraw(True)
        
        # if polygon_purple_0_875 is active this frame...
        if polygon_purple_0_875.status == STARTED:
            # update params
            pass
        
        # *res_purple_0_875* updates
        waitOnFlip = False
        
        # if res_purple_0_875 is starting this frame...
        if res_purple_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_purple_0_875.frameNStart = frameN  # exact frame index
            res_purple_0_875.tStart = t  # local t and not account for scr refresh
            res_purple_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_purple_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_purple_0_875.started')
            # update status
            res_purple_0_875.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_purple_0_875.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_purple_0_875.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_purple_0_875.status == STARTED and not waitOnFlip:
            theseKeys = res_purple_0_875.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_purple_0_875_allKeys.extend(theseKeys)
            if len(_res_purple_0_875_allKeys):
                res_purple_0_875.keys = _res_purple_0_875_allKeys[-1].name  # just the last key pressed
                res_purple_0_875.rt = _res_purple_0_875_allKeys[-1].rt
                res_purple_0_875.duration = _res_purple_0_875_allKeys[-1].duration
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
        for thisComponent in purple0_875Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "purple0_875" ---
    for thisComponent in purple0_875Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('purple0_875.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_purple_0_875.keys in ['', [], None]:  # No response was made
        res_purple_0_875.keys = None
    thisExp.addData('res_purple_0_875.keys',res_purple_0_875.keys)
    if res_purple_0_875.keys != None:  # we had a response
        thisExp.addData('res_purple_0_875.rt', res_purple_0_875.rt)
        thisExp.addData('res_purple_0_875.duration', res_purple_0_875.duration)
    thisExp.nextEntry()
    # the Routine "purple0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "purple1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('purple1.started', globalClock.getTime(format='float'))
    res_purple_1.keys = []
    res_purple_1.rt = []
    _res_purple_1_allKeys = []
    # keep track of which components have finished
    purple1Components = [polygon_purple_1, res_purple_1]
    for thisComponent in purple1Components:
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
    
    # --- Run Routine "purple1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_purple_1* updates
        
        # if polygon_purple_1 is starting this frame...
        if polygon_purple_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_purple_1.frameNStart = frameN  # exact frame index
            polygon_purple_1.tStart = t  # local t and not account for scr refresh
            polygon_purple_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_purple_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_purple_1.started')
            # update status
            polygon_purple_1.status = STARTED
            polygon_purple_1.setAutoDraw(True)
        
        # if polygon_purple_1 is active this frame...
        if polygon_purple_1.status == STARTED:
            # update params
            pass
        
        # *res_purple_1* updates
        waitOnFlip = False
        
        # if res_purple_1 is starting this frame...
        if res_purple_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_purple_1.frameNStart = frameN  # exact frame index
            res_purple_1.tStart = t  # local t and not account for scr refresh
            res_purple_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_purple_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_purple_1.started')
            # update status
            res_purple_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_purple_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_purple_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_purple_1.status == STARTED and not waitOnFlip:
            theseKeys = res_purple_1.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_purple_1_allKeys.extend(theseKeys)
            if len(_res_purple_1_allKeys):
                res_purple_1.keys = _res_purple_1_allKeys[-1].name  # just the last key pressed
                res_purple_1.rt = _res_purple_1_allKeys[-1].rt
                res_purple_1.duration = _res_purple_1_allKeys[-1].duration
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
        for thisComponent in purple1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "purple1" ---
    for thisComponent in purple1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('purple1.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_purple_1.keys in ['', [], None]:  # No response was made
        res_purple_1.keys = None
    thisExp.addData('res_purple_1.keys',res_purple_1.keys)
    if res_purple_1.keys != None:  # we had a response
        thisExp.addData('res_purple_1.rt', res_purple_1.rt)
        thisExp.addData('res_purple_1.duration', res_purple_1.duration)
    thisExp.nextEntry()
    # the Routine "purple1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "orange0_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('orange0_5.started', globalClock.getTime(format='float'))
    res_orange_0_5.keys = []
    res_orange_0_5.rt = []
    _res_orange_0_5_allKeys = []
    # keep track of which components have finished
    orange0_5Components = [polygon_orange_0_5, res_orange_0_5]
    for thisComponent in orange0_5Components:
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
    
    # --- Run Routine "orange0_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_orange_0_5* updates
        
        # if polygon_orange_0_5 is starting this frame...
        if polygon_orange_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_orange_0_5.frameNStart = frameN  # exact frame index
            polygon_orange_0_5.tStart = t  # local t and not account for scr refresh
            polygon_orange_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_orange_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_orange_0_5.started')
            # update status
            polygon_orange_0_5.status = STARTED
            polygon_orange_0_5.setAutoDraw(True)
        
        # if polygon_orange_0_5 is active this frame...
        if polygon_orange_0_5.status == STARTED:
            # update params
            pass
        
        # *res_orange_0_5* updates
        waitOnFlip = False
        
        # if res_orange_0_5 is starting this frame...
        if res_orange_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_orange_0_5.frameNStart = frameN  # exact frame index
            res_orange_0_5.tStart = t  # local t and not account for scr refresh
            res_orange_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_orange_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_orange_0_5.started')
            # update status
            res_orange_0_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_orange_0_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_orange_0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_orange_0_5.status == STARTED and not waitOnFlip:
            theseKeys = res_orange_0_5.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_orange_0_5_allKeys.extend(theseKeys)
            if len(_res_orange_0_5_allKeys):
                res_orange_0_5.keys = _res_orange_0_5_allKeys[-1].name  # just the last key pressed
                res_orange_0_5.rt = _res_orange_0_5_allKeys[-1].rt
                res_orange_0_5.duration = _res_orange_0_5_allKeys[-1].duration
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
        for thisComponent in orange0_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "orange0_5" ---
    for thisComponent in orange0_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('orange0_5.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_orange_0_5.keys in ['', [], None]:  # No response was made
        res_orange_0_5.keys = None
    thisExp.addData('res_orange_0_5.keys',res_orange_0_5.keys)
    if res_orange_0_5.keys != None:  # we had a response
        thisExp.addData('res_orange_0_5.rt', res_orange_0_5.rt)
        thisExp.addData('res_orange_0_5.duration', res_orange_0_5.duration)
    thisExp.nextEntry()
    # the Routine "orange0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "orange0_625" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('orange0_625.started', globalClock.getTime(format='float'))
    res_orange_0_625.keys = []
    res_orange_0_625.rt = []
    _res_orange_0_625_allKeys = []
    # keep track of which components have finished
    orange0_625Components = [polygon_orange_0_625, res_orange_0_625]
    for thisComponent in orange0_625Components:
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
    
    # --- Run Routine "orange0_625" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_orange_0_625* updates
        
        # if polygon_orange_0_625 is starting this frame...
        if polygon_orange_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_orange_0_625.frameNStart = frameN  # exact frame index
            polygon_orange_0_625.tStart = t  # local t and not account for scr refresh
            polygon_orange_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_orange_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_orange_0_625.started')
            # update status
            polygon_orange_0_625.status = STARTED
            polygon_orange_0_625.setAutoDraw(True)
        
        # if polygon_orange_0_625 is active this frame...
        if polygon_orange_0_625.status == STARTED:
            # update params
            pass
        
        # *res_orange_0_625* updates
        waitOnFlip = False
        
        # if res_orange_0_625 is starting this frame...
        if res_orange_0_625.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_orange_0_625.frameNStart = frameN  # exact frame index
            res_orange_0_625.tStart = t  # local t and not account for scr refresh
            res_orange_0_625.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_orange_0_625, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_orange_0_625.started')
            # update status
            res_orange_0_625.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_orange_0_625.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_orange_0_625.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_orange_0_625.status == STARTED and not waitOnFlip:
            theseKeys = res_orange_0_625.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_orange_0_625_allKeys.extend(theseKeys)
            if len(_res_orange_0_625_allKeys):
                res_orange_0_625.keys = _res_orange_0_625_allKeys[-1].name  # just the last key pressed
                res_orange_0_625.rt = _res_orange_0_625_allKeys[-1].rt
                res_orange_0_625.duration = _res_orange_0_625_allKeys[-1].duration
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
        for thisComponent in orange0_625Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "orange0_625" ---
    for thisComponent in orange0_625Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('orange0_625.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_orange_0_625.keys in ['', [], None]:  # No response was made
        res_orange_0_625.keys = None
    thisExp.addData('res_orange_0_625.keys',res_orange_0_625.keys)
    if res_orange_0_625.keys != None:  # we had a response
        thisExp.addData('res_orange_0_625.rt', res_orange_0_625.rt)
        thisExp.addData('res_orange_0_625.duration', res_orange_0_625.duration)
    thisExp.nextEntry()
    # the Routine "orange0_625" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "orange0_75" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('orange0_75.started', globalClock.getTime(format='float'))
    res_orange_0_75.keys = []
    res_orange_0_75.rt = []
    _res_orange_0_75_allKeys = []
    # keep track of which components have finished
    orange0_75Components = [polygon_orange_0_75, res_orange_0_75]
    for thisComponent in orange0_75Components:
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
    
    # --- Run Routine "orange0_75" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_orange_0_75* updates
        
        # if polygon_orange_0_75 is starting this frame...
        if polygon_orange_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_orange_0_75.frameNStart = frameN  # exact frame index
            polygon_orange_0_75.tStart = t  # local t and not account for scr refresh
            polygon_orange_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_orange_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_orange_0_75.started')
            # update status
            polygon_orange_0_75.status = STARTED
            polygon_orange_0_75.setAutoDraw(True)
        
        # if polygon_orange_0_75 is active this frame...
        if polygon_orange_0_75.status == STARTED:
            # update params
            pass
        
        # *res_orange_0_75* updates
        waitOnFlip = False
        
        # if res_orange_0_75 is starting this frame...
        if res_orange_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_orange_0_75.frameNStart = frameN  # exact frame index
            res_orange_0_75.tStart = t  # local t and not account for scr refresh
            res_orange_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_orange_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_orange_0_75.started')
            # update status
            res_orange_0_75.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_orange_0_75.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_orange_0_75.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_orange_0_75.status == STARTED and not waitOnFlip:
            theseKeys = res_orange_0_75.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_orange_0_75_allKeys.extend(theseKeys)
            if len(_res_orange_0_75_allKeys):
                res_orange_0_75.keys = _res_orange_0_75_allKeys[-1].name  # just the last key pressed
                res_orange_0_75.rt = _res_orange_0_75_allKeys[-1].rt
                res_orange_0_75.duration = _res_orange_0_75_allKeys[-1].duration
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
        for thisComponent in orange0_75Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "orange0_75" ---
    for thisComponent in orange0_75Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('orange0_75.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_orange_0_75.keys in ['', [], None]:  # No response was made
        res_orange_0_75.keys = None
    thisExp.addData('res_orange_0_75.keys',res_orange_0_75.keys)
    if res_orange_0_75.keys != None:  # we had a response
        thisExp.addData('res_orange_0_75.rt', res_orange_0_75.rt)
        thisExp.addData('res_orange_0_75.duration', res_orange_0_75.duration)
    thisExp.nextEntry()
    # the Routine "orange0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "orange0_875" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('orange0_875.started', globalClock.getTime(format='float'))
    res_orange_0_875.keys = []
    res_orange_0_875.rt = []
    _res_orange_0_875_allKeys = []
    # keep track of which components have finished
    orange0_875Components = [polygon_res_0_875, res_orange_0_875]
    for thisComponent in orange0_875Components:
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
    
    # --- Run Routine "orange0_875" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_res_0_875* updates
        
        # if polygon_res_0_875 is starting this frame...
        if polygon_res_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_res_0_875.frameNStart = frameN  # exact frame index
            polygon_res_0_875.tStart = t  # local t and not account for scr refresh
            polygon_res_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_res_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_res_0_875.started')
            # update status
            polygon_res_0_875.status = STARTED
            polygon_res_0_875.setAutoDraw(True)
        
        # if polygon_res_0_875 is active this frame...
        if polygon_res_0_875.status == STARTED:
            # update params
            pass
        
        # *res_orange_0_875* updates
        waitOnFlip = False
        
        # if res_orange_0_875 is starting this frame...
        if res_orange_0_875.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_orange_0_875.frameNStart = frameN  # exact frame index
            res_orange_0_875.tStart = t  # local t and not account for scr refresh
            res_orange_0_875.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_orange_0_875, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_orange_0_875.started')
            # update status
            res_orange_0_875.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_orange_0_875.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_orange_0_875.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_orange_0_875.status == STARTED and not waitOnFlip:
            theseKeys = res_orange_0_875.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_orange_0_875_allKeys.extend(theseKeys)
            if len(_res_orange_0_875_allKeys):
                res_orange_0_875.keys = _res_orange_0_875_allKeys[-1].name  # just the last key pressed
                res_orange_0_875.rt = _res_orange_0_875_allKeys[-1].rt
                res_orange_0_875.duration = _res_orange_0_875_allKeys[-1].duration
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
        for thisComponent in orange0_875Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "orange0_875" ---
    for thisComponent in orange0_875Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('orange0_875.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_orange_0_875.keys in ['', [], None]:  # No response was made
        res_orange_0_875.keys = None
    thisExp.addData('res_orange_0_875.keys',res_orange_0_875.keys)
    if res_orange_0_875.keys != None:  # we had a response
        thisExp.addData('res_orange_0_875.rt', res_orange_0_875.rt)
        thisExp.addData('res_orange_0_875.duration', res_orange_0_875.duration)
    thisExp.nextEntry()
    # the Routine "orange0_875" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "orange1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('orange1.started', globalClock.getTime(format='float'))
    res_orange_1.keys = []
    res_orange_1.rt = []
    _res_orange_1_allKeys = []
    # keep track of which components have finished
    orange1Components = [polygon_orange_1, res_orange_1]
    for thisComponent in orange1Components:
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
    
    # --- Run Routine "orange1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_orange_1* updates
        
        # if polygon_orange_1 is starting this frame...
        if polygon_orange_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            polygon_orange_1.frameNStart = frameN  # exact frame index
            polygon_orange_1.tStart = t  # local t and not account for scr refresh
            polygon_orange_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_orange_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_orange_1.started')
            # update status
            polygon_orange_1.status = STARTED
            polygon_orange_1.setAutoDraw(True)
        
        # if polygon_orange_1 is active this frame...
        if polygon_orange_1.status == STARTED:
            # update params
            pass
        
        # *res_orange_1* updates
        waitOnFlip = False
        
        # if res_orange_1 is starting this frame...
        if res_orange_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_orange_1.frameNStart = frameN  # exact frame index
            res_orange_1.tStart = t  # local t and not account for scr refresh
            res_orange_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_orange_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_orange_1.started')
            # update status
            res_orange_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_orange_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_orange_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_orange_1.status == STARTED and not waitOnFlip:
            theseKeys = res_orange_1.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_orange_1_allKeys.extend(theseKeys)
            if len(_res_orange_1_allKeys):
                res_orange_1.keys = _res_orange_1_allKeys[-1].name  # just the last key pressed
                res_orange_1.rt = _res_orange_1_allKeys[-1].rt
                res_orange_1.duration = _res_orange_1_allKeys[-1].duration
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
        for thisComponent in orange1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "orange1" ---
    for thisComponent in orange1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('orange1.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_orange_1.keys in ['', [], None]:  # No response was made
        res_orange_1.keys = None
    thisExp.addData('res_orange_1.keys',res_orange_1.keys)
    if res_orange_1.keys != None:  # we had a response
        thisExp.addData('res_orange_1.rt', res_orange_1.rt)
        thisExp.addData('res_orange_1.duration', res_orange_1.duration)
    thisExp.nextEntry()
    # the Routine "orange1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audiointro" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audiointro.started', globalClock.getTime(format='float'))
    audiointro_res.keys = []
    audiointro_res.rt = []
    _audiointro_res_allKeys = []
    # keep track of which components have finished
    audiointroComponents = [audiotext, audiointro_res]
    for thisComponent in audiointroComponents:
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
    
    # --- Run Routine "audiointro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *audiotext* updates
        
        # if audiotext is starting this frame...
        if audiotext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            audiotext.frameNStart = frameN  # exact frame index
            audiotext.tStart = t  # local t and not account for scr refresh
            audiotext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(audiotext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'audiotext.started')
            # update status
            audiotext.status = STARTED
            audiotext.setAutoDraw(True)
        
        # if audiotext is active this frame...
        if audiotext.status == STARTED:
            # update params
            pass
        
        # *audiointro_res* updates
        waitOnFlip = False
        
        # if audiointro_res is starting this frame...
        if audiointro_res.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            audiointro_res.frameNStart = frameN  # exact frame index
            audiointro_res.tStart = t  # local t and not account for scr refresh
            audiointro_res.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(audiointro_res, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'audiointro_res.started')
            # update status
            audiointro_res.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(audiointro_res.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(audiointro_res.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if audiointro_res.status == STARTED and not waitOnFlip:
            theseKeys = audiointro_res.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _audiointro_res_allKeys.extend(theseKeys)
            if len(_audiointro_res_allKeys):
                audiointro_res.keys = _audiointro_res_allKeys[-1].name  # just the last key pressed
                audiointro_res.rt = _audiointro_res_allKeys[-1].rt
                audiointro_res.duration = _audiointro_res_allKeys[-1].duration
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
        for thisComponent in audiointroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audiointro" ---
    for thisComponent in audiointroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audiointro.stopped', globalClock.getTime(format='float'))
    # check responses
    if audiointro_res.keys in ['', [], None]:  # No response was made
        audiointro_res.keys = None
    thisExp.addData('audiointro_res.keys',audiointro_res.keys)
    if audiointro_res.keys != None:  # we had a response
        thisExp.addData('audiointro_res.rt', audiointro_res.rt)
        thisExp.addData('audiointro_res.duration', audiointro_res.duration)
    thisExp.nextEntry()
    # the Routine "audiointro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audiotest" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audiotest.started', globalClock.getTime(format='float'))
    sound_testrun.setSound('audio files/2500.wav', hamming=True)
    sound_testrun.setVolume(1.0, log=False)
    sound_testrun.seek(0)
    res_audio_testrun.keys = []
    res_audio_testrun.rt = []
    _res_audio_testrun_allKeys = []
    # keep track of which components have finished
    audiotestComponents = [sound_testrun, res_audio_testrun]
    for thisComponent in audiotestComponents:
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
    
    # --- Run Routine "audiotest" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_testrun is starting this frame...
        if sound_testrun.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_testrun.frameNStart = frameN  # exact frame index
            sound_testrun.tStart = t  # local t and not account for scr refresh
            sound_testrun.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_testrun.started', tThisFlipGlobal)
            # update status
            sound_testrun.status = STARTED
            sound_testrun.play(when=win)  # sync with win flip
        # update sound_testrun status according to whether it's playing
        if sound_testrun.isPlaying:
            sound_testrun.status = STARTED
        elif sound_testrun.isFinished:
            sound_testrun.status = FINISHED
        
        # *res_audio_testrun* updates
        waitOnFlip = False
        
        # if res_audio_testrun is starting this frame...
        if res_audio_testrun.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_audio_testrun.frameNStart = frameN  # exact frame index
            res_audio_testrun.tStart = t  # local t and not account for scr refresh
            res_audio_testrun.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_audio_testrun, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_audio_testrun.started')
            # update status
            res_audio_testrun.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_audio_testrun.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_audio_testrun.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_audio_testrun.status == STARTED and not waitOnFlip:
            theseKeys = res_audio_testrun.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_audio_testrun_allKeys.extend(theseKeys)
            if len(_res_audio_testrun_allKeys):
                res_audio_testrun.keys = _res_audio_testrun_allKeys[-1].name  # just the last key pressed
                res_audio_testrun.rt = _res_audio_testrun_allKeys[-1].rt
                res_audio_testrun.duration = _res_audio_testrun_allKeys[-1].duration
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
        for thisComponent in audiotestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audiotest" ---
    for thisComponent in audiotestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audiotest.stopped', globalClock.getTime(format='float'))
    sound_testrun.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_audio_testrun.keys in ['', [], None]:  # No response was made
        res_audio_testrun.keys = None
    thisExp.addData('res_audio_testrun.keys',res_audio_testrun.keys)
    if res_audio_testrun.keys != None:  # we had a response
        thisExp.addData('res_audio_testrun.rt', res_audio_testrun.rt)
        thisExp.addData('res_audio_testrun.duration', res_audio_testrun.duration)
    thisExp.nextEntry()
    # the Routine "audiotest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audiotestpassed" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audiotestpassed.started', globalClock.getTime(format='float'))
    res_testpassed.keys = []
    res_testpassed.rt = []
    _res_testpassed_allKeys = []
    # keep track of which components have finished
    audiotestpassedComponents = [autest_passed, res_testpassed]
    for thisComponent in audiotestpassedComponents:
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
    
    # --- Run Routine "audiotestpassed" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *autest_passed* updates
        
        # if autest_passed is starting this frame...
        if autest_passed.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            autest_passed.frameNStart = frameN  # exact frame index
            autest_passed.tStart = t  # local t and not account for scr refresh
            autest_passed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(autest_passed, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'autest_passed.started')
            # update status
            autest_passed.status = STARTED
            autest_passed.setAutoDraw(True)
        
        # if autest_passed is active this frame...
        if autest_passed.status == STARTED:
            # update params
            pass
        
        # *res_testpassed* updates
        waitOnFlip = False
        
        # if res_testpassed is starting this frame...
        if res_testpassed.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_testpassed.frameNStart = frameN  # exact frame index
            res_testpassed.tStart = t  # local t and not account for scr refresh
            res_testpassed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_testpassed, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_testpassed.started')
            # update status
            res_testpassed.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_testpassed.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_testpassed.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_testpassed.status == STARTED and not waitOnFlip:
            theseKeys = res_testpassed.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_testpassed_allKeys.extend(theseKeys)
            if len(_res_testpassed_allKeys):
                res_testpassed.keys = _res_testpassed_allKeys[-1].name  # just the last key pressed
                res_testpassed.rt = _res_testpassed_allKeys[-1].rt
                res_testpassed.duration = _res_testpassed_allKeys[-1].duration
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
        for thisComponent in audiotestpassedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audiotestpassed" ---
    for thisComponent in audiotestpassedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audiotestpassed.stopped', globalClock.getTime(format='float'))
    # check responses
    if res_testpassed.keys in ['', [], None]:  # No response was made
        res_testpassed.keys = None
    thisExp.addData('res_testpassed.keys',res_testpassed.keys)
    if res_testpassed.keys != None:  # we had a response
        thisExp.addData('res_testpassed.rt', res_testpassed.rt)
        thisExp.addData('res_testpassed.duration', res_testpassed.duration)
    thisExp.nextEntry()
    # the Routine "audiotestpassed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_500Hz_0_25" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_500Hz_0_25.started', globalClock.getTime(format='float'))
    sound_500Hz_0_25.setSound('audio files/500.wav', hamming=True)
    sound_500Hz_0_25.setVolume(0.25, log=False)
    sound_500Hz_0_25.seek(0)
    res_500Hz_0_25.keys = []
    res_500Hz_0_25.rt = []
    _res_500Hz_0_25_allKeys = []
    # keep track of which components have finished
    audio_500Hz_0_25Components = [sound_500Hz_0_25, res_500Hz_0_25]
    for thisComponent in audio_500Hz_0_25Components:
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
    
    # --- Run Routine "audio_500Hz_0_25" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_500Hz_0_25 is starting this frame...
        if sound_500Hz_0_25.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_500Hz_0_25.frameNStart = frameN  # exact frame index
            sound_500Hz_0_25.tStart = t  # local t and not account for scr refresh
            sound_500Hz_0_25.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_500Hz_0_25.started', tThisFlipGlobal)
            # update status
            sound_500Hz_0_25.status = STARTED
            sound_500Hz_0_25.play(when=win)  # sync with win flip
        # update sound_500Hz_0_25 status according to whether it's playing
        if sound_500Hz_0_25.isPlaying:
            sound_500Hz_0_25.status = STARTED
        elif sound_500Hz_0_25.isFinished:
            sound_500Hz_0_25.status = FINISHED
        
        # *res_500Hz_0_25* updates
        waitOnFlip = False
        
        # if res_500Hz_0_25 is starting this frame...
        if res_500Hz_0_25.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_500Hz_0_25.frameNStart = frameN  # exact frame index
            res_500Hz_0_25.tStart = t  # local t and not account for scr refresh
            res_500Hz_0_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_500Hz_0_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_500Hz_0_25.started')
            # update status
            res_500Hz_0_25.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_500Hz_0_25.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_500Hz_0_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_500Hz_0_25.status == STARTED and not waitOnFlip:
            theseKeys = res_500Hz_0_25.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_500Hz_0_25_allKeys.extend(theseKeys)
            if len(_res_500Hz_0_25_allKeys):
                res_500Hz_0_25.keys = _res_500Hz_0_25_allKeys[-1].name  # just the last key pressed
                res_500Hz_0_25.rt = _res_500Hz_0_25_allKeys[-1].rt
                res_500Hz_0_25.duration = _res_500Hz_0_25_allKeys[-1].duration
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
        for thisComponent in audio_500Hz_0_25Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_500Hz_0_25" ---
    for thisComponent in audio_500Hz_0_25Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_500Hz_0_25.stopped', globalClock.getTime(format='float'))
    sound_500Hz_0_25.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_500Hz_0_25.keys in ['', [], None]:  # No response was made
        res_500Hz_0_25.keys = None
    thisExp.addData('res_500Hz_0_25.keys',res_500Hz_0_25.keys)
    if res_500Hz_0_25.keys != None:  # we had a response
        thisExp.addData('res_500Hz_0_25.rt', res_500Hz_0_25.rt)
        thisExp.addData('res_500Hz_0_25.duration', res_500Hz_0_25.duration)
    thisExp.nextEntry()
    # the Routine "audio_500Hz_0_25" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_500Hz_0_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_500Hz_0_5.started', globalClock.getTime(format='float'))
    sound_500Hz_0_5.setSound('audio files/500.wav', hamming=True)
    sound_500Hz_0_5.setVolume(0.5, log=False)
    sound_500Hz_0_5.seek(0)
    res_500Hz_0_5.keys = []
    res_500Hz_0_5.rt = []
    _res_500Hz_0_5_allKeys = []
    # keep track of which components have finished
    audio_500Hz_0_5Components = [sound_500Hz_0_5, res_500Hz_0_5]
    for thisComponent in audio_500Hz_0_5Components:
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
    
    # --- Run Routine "audio_500Hz_0_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_500Hz_0_5 is starting this frame...
        if sound_500Hz_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_500Hz_0_5.frameNStart = frameN  # exact frame index
            sound_500Hz_0_5.tStart = t  # local t and not account for scr refresh
            sound_500Hz_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_500Hz_0_5.started', tThisFlipGlobal)
            # update status
            sound_500Hz_0_5.status = STARTED
            sound_500Hz_0_5.play(when=win)  # sync with win flip
        # update sound_500Hz_0_5 status according to whether it's playing
        if sound_500Hz_0_5.isPlaying:
            sound_500Hz_0_5.status = STARTED
        elif sound_500Hz_0_5.isFinished:
            sound_500Hz_0_5.status = FINISHED
        
        # *res_500Hz_0_5* updates
        waitOnFlip = False
        
        # if res_500Hz_0_5 is starting this frame...
        if res_500Hz_0_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_500Hz_0_5.frameNStart = frameN  # exact frame index
            res_500Hz_0_5.tStart = t  # local t and not account for scr refresh
            res_500Hz_0_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_500Hz_0_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_500Hz_0_5.started')
            # update status
            res_500Hz_0_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_500Hz_0_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_500Hz_0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_500Hz_0_5.status == STARTED and not waitOnFlip:
            theseKeys = res_500Hz_0_5.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_500Hz_0_5_allKeys.extend(theseKeys)
            if len(_res_500Hz_0_5_allKeys):
                res_500Hz_0_5.keys = _res_500Hz_0_5_allKeys[-1].name  # just the last key pressed
                res_500Hz_0_5.rt = _res_500Hz_0_5_allKeys[-1].rt
                res_500Hz_0_5.duration = _res_500Hz_0_5_allKeys[-1].duration
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
        for thisComponent in audio_500Hz_0_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_500Hz_0_5" ---
    for thisComponent in audio_500Hz_0_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_500Hz_0_5.stopped', globalClock.getTime(format='float'))
    sound_500Hz_0_5.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_500Hz_0_5.keys in ['', [], None]:  # No response was made
        res_500Hz_0_5.keys = None
    thisExp.addData('res_500Hz_0_5.keys',res_500Hz_0_5.keys)
    if res_500Hz_0_5.keys != None:  # we had a response
        thisExp.addData('res_500Hz_0_5.rt', res_500Hz_0_5.rt)
        thisExp.addData('res_500Hz_0_5.duration', res_500Hz_0_5.duration)
    thisExp.nextEntry()
    # the Routine "audio_500Hz_0_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_500Hz_0_75" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_500Hz_0_75.started', globalClock.getTime(format='float'))
    sound_500Hz_0_75.setSound('audio files/500.wav', hamming=True)
    sound_500Hz_0_75.setVolume(0.75, log=False)
    sound_500Hz_0_75.seek(0)
    res_500Hz_0_75.keys = []
    res_500Hz_0_75.rt = []
    _res_500Hz_0_75_allKeys = []
    # keep track of which components have finished
    audio_500Hz_0_75Components = [sound_500Hz_0_75, res_500Hz_0_75]
    for thisComponent in audio_500Hz_0_75Components:
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
    
    # --- Run Routine "audio_500Hz_0_75" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_500Hz_0_75 is starting this frame...
        if sound_500Hz_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_500Hz_0_75.frameNStart = frameN  # exact frame index
            sound_500Hz_0_75.tStart = t  # local t and not account for scr refresh
            sound_500Hz_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_500Hz_0_75.started', tThisFlipGlobal)
            # update status
            sound_500Hz_0_75.status = STARTED
            sound_500Hz_0_75.play(when=win)  # sync with win flip
        # update sound_500Hz_0_75 status according to whether it's playing
        if sound_500Hz_0_75.isPlaying:
            sound_500Hz_0_75.status = STARTED
        elif sound_500Hz_0_75.isFinished:
            sound_500Hz_0_75.status = FINISHED
        
        # *res_500Hz_0_75* updates
        waitOnFlip = False
        
        # if res_500Hz_0_75 is starting this frame...
        if res_500Hz_0_75.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_500Hz_0_75.frameNStart = frameN  # exact frame index
            res_500Hz_0_75.tStart = t  # local t and not account for scr refresh
            res_500Hz_0_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_500Hz_0_75, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_500Hz_0_75.started')
            # update status
            res_500Hz_0_75.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_500Hz_0_75.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_500Hz_0_75.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_500Hz_0_75.status == STARTED and not waitOnFlip:
            theseKeys = res_500Hz_0_75.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_500Hz_0_75_allKeys.extend(theseKeys)
            if len(_res_500Hz_0_75_allKeys):
                res_500Hz_0_75.keys = _res_500Hz_0_75_allKeys[-1].name  # just the last key pressed
                res_500Hz_0_75.rt = _res_500Hz_0_75_allKeys[-1].rt
                res_500Hz_0_75.duration = _res_500Hz_0_75_allKeys[-1].duration
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
        for thisComponent in audio_500Hz_0_75Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_500Hz_0_75" ---
    for thisComponent in audio_500Hz_0_75Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_500Hz_0_75.stopped', globalClock.getTime(format='float'))
    sound_500Hz_0_75.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_500Hz_0_75.keys in ['', [], None]:  # No response was made
        res_500Hz_0_75.keys = None
    thisExp.addData('res_500Hz_0_75.keys',res_500Hz_0_75.keys)
    if res_500Hz_0_75.keys != None:  # we had a response
        thisExp.addData('res_500Hz_0_75.rt', res_500Hz_0_75.rt)
        thisExp.addData('res_500Hz_0_75.duration', res_500Hz_0_75.duration)
    thisExp.nextEntry()
    # the Routine "audio_500Hz_0_75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_500Hz_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_500Hz_1.started', globalClock.getTime(format='float'))
    sound_500Hz.setSound('audio files/500.wav', hamming=True)
    sound_500Hz.setVolume(1.0, log=False)
    sound_500Hz.seek(0)
    res_500Hz.keys = []
    res_500Hz.rt = []
    _res_500Hz_allKeys = []
    # keep track of which components have finished
    audio_500Hz_1Components = [sound_500Hz, res_500Hz]
    for thisComponent in audio_500Hz_1Components:
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
    
    # --- Run Routine "audio_500Hz_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_500Hz is starting this frame...
        if sound_500Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_500Hz.frameNStart = frameN  # exact frame index
            sound_500Hz.tStart = t  # local t and not account for scr refresh
            sound_500Hz.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_500Hz.started', tThisFlipGlobal)
            # update status
            sound_500Hz.status = STARTED
            sound_500Hz.play(when=win)  # sync with win flip
        # update sound_500Hz status according to whether it's playing
        if sound_500Hz.isPlaying:
            sound_500Hz.status = STARTED
        elif sound_500Hz.isFinished:
            sound_500Hz.status = FINISHED
        
        # *res_500Hz* updates
        waitOnFlip = False
        
        # if res_500Hz is starting this frame...
        if res_500Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_500Hz.frameNStart = frameN  # exact frame index
            res_500Hz.tStart = t  # local t and not account for scr refresh
            res_500Hz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_500Hz, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_500Hz.started')
            # update status
            res_500Hz.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_500Hz.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_500Hz.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_500Hz.status == STARTED and not waitOnFlip:
            theseKeys = res_500Hz.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_500Hz_allKeys.extend(theseKeys)
            if len(_res_500Hz_allKeys):
                res_500Hz.keys = _res_500Hz_allKeys[-1].name  # just the last key pressed
                res_500Hz.rt = _res_500Hz_allKeys[-1].rt
                res_500Hz.duration = _res_500Hz_allKeys[-1].duration
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
        for thisComponent in audio_500Hz_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_500Hz_1" ---
    for thisComponent in audio_500Hz_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_500Hz_1.stopped', globalClock.getTime(format='float'))
    sound_500Hz.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_500Hz.keys in ['', [], None]:  # No response was made
        res_500Hz.keys = None
    thisExp.addData('res_500Hz.keys',res_500Hz.keys)
    if res_500Hz.keys != None:  # we had a response
        thisExp.addData('res_500Hz.rt', res_500Hz.rt)
        thisExp.addData('res_500Hz.duration', res_500Hz.duration)
    thisExp.nextEntry()
    # the Routine "audio_500Hz_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_2500Hz_0_25" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_2500Hz_0_25.started', globalClock.getTime(format='float'))
    sound_2500Hz_0_25.setSound('audio files/2500.wav', hamming=True)
    sound_2500Hz_0_25.setVolume(0.25, log=False)
    sound_2500Hz_0_25.seek(0)
    res_2500Hz_0_25.keys = []
    res_2500Hz_0_25.rt = []
    _res_2500Hz_0_25_allKeys = []
    # keep track of which components have finished
    audio_2500Hz_0_25Components = [sound_2500Hz_0_25, res_2500Hz_0_25]
    for thisComponent in audio_2500Hz_0_25Components:
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
    
    # --- Run Routine "audio_2500Hz_0_25" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_2500Hz_0_25 is starting this frame...
        if sound_2500Hz_0_25.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_2500Hz_0_25.frameNStart = frameN  # exact frame index
            sound_2500Hz_0_25.tStart = t  # local t and not account for scr refresh
            sound_2500Hz_0_25.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_2500Hz_0_25.started', tThisFlipGlobal)
            # update status
            sound_2500Hz_0_25.status = STARTED
            sound_2500Hz_0_25.play(when=win)  # sync with win flip
        # update sound_2500Hz_0_25 status according to whether it's playing
        if sound_2500Hz_0_25.isPlaying:
            sound_2500Hz_0_25.status = STARTED
        elif sound_2500Hz_0_25.isFinished:
            sound_2500Hz_0_25.status = FINISHED
        
        # *res_2500Hz_0_25* updates
        waitOnFlip = False
        
        # if res_2500Hz_0_25 is starting this frame...
        if res_2500Hz_0_25.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_2500Hz_0_25.frameNStart = frameN  # exact frame index
            res_2500Hz_0_25.tStart = t  # local t and not account for scr refresh
            res_2500Hz_0_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_2500Hz_0_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_2500Hz_0_25.started')
            # update status
            res_2500Hz_0_25.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_2500Hz_0_25.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_2500Hz_0_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_2500Hz_0_25.status == STARTED and not waitOnFlip:
            theseKeys = res_2500Hz_0_25.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_2500Hz_0_25_allKeys.extend(theseKeys)
            if len(_res_2500Hz_0_25_allKeys):
                res_2500Hz_0_25.keys = _res_2500Hz_0_25_allKeys[-1].name  # just the last key pressed
                res_2500Hz_0_25.rt = _res_2500Hz_0_25_allKeys[-1].rt
                res_2500Hz_0_25.duration = _res_2500Hz_0_25_allKeys[-1].duration
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
        for thisComponent in audio_2500Hz_0_25Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_2500Hz_0_25" ---
    for thisComponent in audio_2500Hz_0_25Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_2500Hz_0_25.stopped', globalClock.getTime(format='float'))
    sound_2500Hz_0_25.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_2500Hz_0_25.keys in ['', [], None]:  # No response was made
        res_2500Hz_0_25.keys = None
    thisExp.addData('res_2500Hz_0_25.keys',res_2500Hz_0_25.keys)
    if res_2500Hz_0_25.keys != None:  # we had a response
        thisExp.addData('res_2500Hz_0_25.rt', res_2500Hz_0_25.rt)
        thisExp.addData('res_2500Hz_0_25.duration', res_2500Hz_0_25.duration)
    thisExp.nextEntry()
    # the Routine "audio_2500Hz_0_25" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_2500Hz" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_2500Hz.started', globalClock.getTime(format='float'))
    sound_2500Hz.setSound('audio files/2500.wav', hamming=True)
    sound_2500Hz.setVolume(1.0, log=False)
    sound_2500Hz.seek(0)
    res_2500Hz.keys = []
    res_2500Hz.rt = []
    _res_2500Hz_allKeys = []
    # keep track of which components have finished
    audio_2500HzComponents = [sound_2500Hz, res_2500Hz]
    for thisComponent in audio_2500HzComponents:
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
    
    # --- Run Routine "audio_2500Hz" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_2500Hz is starting this frame...
        if sound_2500Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_2500Hz.frameNStart = frameN  # exact frame index
            sound_2500Hz.tStart = t  # local t and not account for scr refresh
            sound_2500Hz.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_2500Hz.started', tThisFlipGlobal)
            # update status
            sound_2500Hz.status = STARTED
            sound_2500Hz.play(when=win)  # sync with win flip
        # update sound_2500Hz status according to whether it's playing
        if sound_2500Hz.isPlaying:
            sound_2500Hz.status = STARTED
        elif sound_2500Hz.isFinished:
            sound_2500Hz.status = FINISHED
        
        # *res_2500Hz* updates
        waitOnFlip = False
        
        # if res_2500Hz is starting this frame...
        if res_2500Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_2500Hz.frameNStart = frameN  # exact frame index
            res_2500Hz.tStart = t  # local t and not account for scr refresh
            res_2500Hz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_2500Hz, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_2500Hz.started')
            # update status
            res_2500Hz.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_2500Hz.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_2500Hz.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_2500Hz.status == STARTED and not waitOnFlip:
            theseKeys = res_2500Hz.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_2500Hz_allKeys.extend(theseKeys)
            if len(_res_2500Hz_allKeys):
                res_2500Hz.keys = _res_2500Hz_allKeys[-1].name  # just the last key pressed
                res_2500Hz.rt = _res_2500Hz_allKeys[-1].rt
                res_2500Hz.duration = _res_2500Hz_allKeys[-1].duration
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
        for thisComponent in audio_2500HzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_2500Hz" ---
    for thisComponent in audio_2500HzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_2500Hz.stopped', globalClock.getTime(format='float'))
    sound_2500Hz.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_2500Hz.keys in ['', [], None]:  # No response was made
        res_2500Hz.keys = None
    thisExp.addData('res_2500Hz.keys',res_2500Hz.keys)
    if res_2500Hz.keys != None:  # we had a response
        thisExp.addData('res_2500Hz.rt', res_2500Hz.rt)
        thisExp.addData('res_2500Hz.duration', res_2500Hz.duration)
    thisExp.nextEntry()
    # the Routine "audio_2500Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_5000Hz" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_5000Hz.started', globalClock.getTime(format='float'))
    sound_5000Hz.setSound('audio files/5000.wav', hamming=True)
    sound_5000Hz.setVolume(1.0, log=False)
    sound_5000Hz.seek(0)
    res_5000Hz.keys = []
    res_5000Hz.rt = []
    _res_5000Hz_allKeys = []
    # keep track of which components have finished
    audio_5000HzComponents = [sound_5000Hz, res_5000Hz]
    for thisComponent in audio_5000HzComponents:
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
    
    # --- Run Routine "audio_5000Hz" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_5000Hz is starting this frame...
        if sound_5000Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_5000Hz.frameNStart = frameN  # exact frame index
            sound_5000Hz.tStart = t  # local t and not account for scr refresh
            sound_5000Hz.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_5000Hz.started', tThisFlipGlobal)
            # update status
            sound_5000Hz.status = STARTED
            sound_5000Hz.play(when=win)  # sync with win flip
        # update sound_5000Hz status according to whether it's playing
        if sound_5000Hz.isPlaying:
            sound_5000Hz.status = STARTED
        elif sound_5000Hz.isFinished:
            sound_5000Hz.status = FINISHED
        
        # *res_5000Hz* updates
        waitOnFlip = False
        
        # if res_5000Hz is starting this frame...
        if res_5000Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_5000Hz.frameNStart = frameN  # exact frame index
            res_5000Hz.tStart = t  # local t and not account for scr refresh
            res_5000Hz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_5000Hz, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_5000Hz.started')
            # update status
            res_5000Hz.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_5000Hz.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_5000Hz.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_5000Hz.status == STARTED and not waitOnFlip:
            theseKeys = res_5000Hz.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_5000Hz_allKeys.extend(theseKeys)
            if len(_res_5000Hz_allKeys):
                res_5000Hz.keys = _res_5000Hz_allKeys[-1].name  # just the last key pressed
                res_5000Hz.rt = _res_5000Hz_allKeys[-1].rt
                res_5000Hz.duration = _res_5000Hz_allKeys[-1].duration
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
        for thisComponent in audio_5000HzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_5000Hz" ---
    for thisComponent in audio_5000HzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_5000Hz.stopped', globalClock.getTime(format='float'))
    sound_5000Hz.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_5000Hz.keys in ['', [], None]:  # No response was made
        res_5000Hz.keys = None
    thisExp.addData('res_5000Hz.keys',res_5000Hz.keys)
    if res_5000Hz.keys != None:  # we had a response
        thisExp.addData('res_5000Hz.rt', res_5000Hz.rt)
        thisExp.addData('res_5000Hz.duration', res_5000Hz.duration)
    thisExp.nextEntry()
    # the Routine "audio_5000Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_7500Hz" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_7500Hz.started', globalClock.getTime(format='float'))
    sound_7500Hz.setSound('audio files/7500.wav', hamming=True)
    sound_7500Hz.setVolume(1.0, log=False)
    sound_7500Hz.seek(0)
    res_7500Hz.keys = []
    res_7500Hz.rt = []
    _res_7500Hz_allKeys = []
    # keep track of which components have finished
    audio_7500HzComponents = [sound_7500Hz, res_7500Hz]
    for thisComponent in audio_7500HzComponents:
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
    
    # --- Run Routine "audio_7500Hz" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_7500Hz is starting this frame...
        if sound_7500Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_7500Hz.frameNStart = frameN  # exact frame index
            sound_7500Hz.tStart = t  # local t and not account for scr refresh
            sound_7500Hz.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_7500Hz.started', tThisFlipGlobal)
            # update status
            sound_7500Hz.status = STARTED
            sound_7500Hz.play(when=win)  # sync with win flip
        # update sound_7500Hz status according to whether it's playing
        if sound_7500Hz.isPlaying:
            sound_7500Hz.status = STARTED
        elif sound_7500Hz.isFinished:
            sound_7500Hz.status = FINISHED
        
        # *res_7500Hz* updates
        waitOnFlip = False
        
        # if res_7500Hz is starting this frame...
        if res_7500Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_7500Hz.frameNStart = frameN  # exact frame index
            res_7500Hz.tStart = t  # local t and not account for scr refresh
            res_7500Hz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_7500Hz, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_7500Hz.started')
            # update status
            res_7500Hz.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_7500Hz.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_7500Hz.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_7500Hz.status == STARTED and not waitOnFlip:
            theseKeys = res_7500Hz.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_7500Hz_allKeys.extend(theseKeys)
            if len(_res_7500Hz_allKeys):
                res_7500Hz.keys = _res_7500Hz_allKeys[-1].name  # just the last key pressed
                res_7500Hz.rt = _res_7500Hz_allKeys[-1].rt
                res_7500Hz.duration = _res_7500Hz_allKeys[-1].duration
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
        for thisComponent in audio_7500HzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_7500Hz" ---
    for thisComponent in audio_7500HzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_7500Hz.stopped', globalClock.getTime(format='float'))
    sound_7500Hz.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_7500Hz.keys in ['', [], None]:  # No response was made
        res_7500Hz.keys = None
    thisExp.addData('res_7500Hz.keys',res_7500Hz.keys)
    if res_7500Hz.keys != None:  # we had a response
        thisExp.addData('res_7500Hz.rt', res_7500Hz.rt)
        thisExp.addData('res_7500Hz.duration', res_7500Hz.duration)
    thisExp.nextEntry()
    # the Routine "audio_7500Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_10000Hz" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_10000Hz.started', globalClock.getTime(format='float'))
    sound_10000Hz.setSound('audio files/10000.wav', hamming=True)
    sound_10000Hz.setVolume(1.0, log=False)
    sound_10000Hz.seek(0)
    res_10000Hz.keys = []
    res_10000Hz.rt = []
    _res_10000Hz_allKeys = []
    # keep track of which components have finished
    audio_10000HzComponents = [sound_10000Hz, res_10000Hz]
    for thisComponent in audio_10000HzComponents:
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
    
    # --- Run Routine "audio_10000Hz" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_10000Hz is starting this frame...
        if sound_10000Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_10000Hz.frameNStart = frameN  # exact frame index
            sound_10000Hz.tStart = t  # local t and not account for scr refresh
            sound_10000Hz.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_10000Hz.started', tThisFlipGlobal)
            # update status
            sound_10000Hz.status = STARTED
            sound_10000Hz.play(when=win)  # sync with win flip
        # update sound_10000Hz status according to whether it's playing
        if sound_10000Hz.isPlaying:
            sound_10000Hz.status = STARTED
        elif sound_10000Hz.isFinished:
            sound_10000Hz.status = FINISHED
        
        # *res_10000Hz* updates
        waitOnFlip = False
        
        # if res_10000Hz is starting this frame...
        if res_10000Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_10000Hz.frameNStart = frameN  # exact frame index
            res_10000Hz.tStart = t  # local t and not account for scr refresh
            res_10000Hz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_10000Hz, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_10000Hz.started')
            # update status
            res_10000Hz.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_10000Hz.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_10000Hz.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_10000Hz.status == STARTED and not waitOnFlip:
            theseKeys = res_10000Hz.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_10000Hz_allKeys.extend(theseKeys)
            if len(_res_10000Hz_allKeys):
                res_10000Hz.keys = _res_10000Hz_allKeys[-1].name  # just the last key pressed
                res_10000Hz.rt = _res_10000Hz_allKeys[-1].rt
                res_10000Hz.duration = _res_10000Hz_allKeys[-1].duration
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
        for thisComponent in audio_10000HzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_10000Hz" ---
    for thisComponent in audio_10000HzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_10000Hz.stopped', globalClock.getTime(format='float'))
    sound_10000Hz.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_10000Hz.keys in ['', [], None]:  # No response was made
        res_10000Hz.keys = None
    thisExp.addData('res_10000Hz.keys',res_10000Hz.keys)
    if res_10000Hz.keys != None:  # we had a response
        thisExp.addData('res_10000Hz.rt', res_10000Hz.rt)
        thisExp.addData('res_10000Hz.duration', res_10000Hz.duration)
    thisExp.nextEntry()
    # the Routine "audio_10000Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_12500Hz" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_12500Hz.started', globalClock.getTime(format='float'))
    sound_12500.setSound('audio files/12500.wav', hamming=True)
    sound_12500.setVolume(1.0, log=False)
    sound_12500.seek(0)
    res_12500.keys = []
    res_12500.rt = []
    _res_12500_allKeys = []
    # keep track of which components have finished
    audio_12500HzComponents = [sound_12500, res_12500]
    for thisComponent in audio_12500HzComponents:
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
    
    # --- Run Routine "audio_12500Hz" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_12500 is starting this frame...
        if sound_12500.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_12500.frameNStart = frameN  # exact frame index
            sound_12500.tStart = t  # local t and not account for scr refresh
            sound_12500.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_12500.started', tThisFlipGlobal)
            # update status
            sound_12500.status = STARTED
            sound_12500.play(when=win)  # sync with win flip
        # update sound_12500 status according to whether it's playing
        if sound_12500.isPlaying:
            sound_12500.status = STARTED
        elif sound_12500.isFinished:
            sound_12500.status = FINISHED
        
        # *res_12500* updates
        waitOnFlip = False
        
        # if res_12500 is starting this frame...
        if res_12500.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_12500.frameNStart = frameN  # exact frame index
            res_12500.tStart = t  # local t and not account for scr refresh
            res_12500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_12500, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_12500.started')
            # update status
            res_12500.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_12500.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_12500.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_12500.status == STARTED and not waitOnFlip:
            theseKeys = res_12500.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_12500_allKeys.extend(theseKeys)
            if len(_res_12500_allKeys):
                res_12500.keys = _res_12500_allKeys[-1].name  # just the last key pressed
                res_12500.rt = _res_12500_allKeys[-1].rt
                res_12500.duration = _res_12500_allKeys[-1].duration
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
        for thisComponent in audio_12500HzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_12500Hz" ---
    for thisComponent in audio_12500HzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_12500Hz.stopped', globalClock.getTime(format='float'))
    sound_12500.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_12500.keys in ['', [], None]:  # No response was made
        res_12500.keys = None
    thisExp.addData('res_12500.keys',res_12500.keys)
    if res_12500.keys != None:  # we had a response
        thisExp.addData('res_12500.rt', res_12500.rt)
        thisExp.addData('res_12500.duration', res_12500.duration)
    thisExp.nextEntry()
    # the Routine "audio_12500Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "audio_15000Hz" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('audio_15000Hz.started', globalClock.getTime(format='float'))
    sound_15000.setSound('audio files/15000.wav', hamming=True)
    sound_15000.setVolume(1.0, log=False)
    sound_15000.seek(0)
    res_15000Hz.keys = []
    res_15000Hz.rt = []
    _res_15000Hz_allKeys = []
    # keep track of which components have finished
    audio_15000HzComponents = [sound_15000, res_15000Hz]
    for thisComponent in audio_15000HzComponents:
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
    
    # --- Run Routine "audio_15000Hz" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sound_15000 is starting this frame...
        if sound_15000.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_15000.frameNStart = frameN  # exact frame index
            sound_15000.tStart = t  # local t and not account for scr refresh
            sound_15000.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_15000.started', tThisFlipGlobal)
            # update status
            sound_15000.status = STARTED
            sound_15000.play(when=win)  # sync with win flip
        # update sound_15000 status according to whether it's playing
        if sound_15000.isPlaying:
            sound_15000.status = STARTED
        elif sound_15000.isFinished:
            sound_15000.status = FINISHED
        
        # *res_15000Hz* updates
        waitOnFlip = False
        
        # if res_15000Hz is starting this frame...
        if res_15000Hz.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            res_15000Hz.frameNStart = frameN  # exact frame index
            res_15000Hz.tStart = t  # local t and not account for scr refresh
            res_15000Hz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(res_15000Hz, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'res_15000Hz.started')
            # update status
            res_15000Hz.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(res_15000Hz.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(res_15000Hz.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if res_15000Hz.status == STARTED and not waitOnFlip:
            theseKeys = res_15000Hz.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _res_15000Hz_allKeys.extend(theseKeys)
            if len(_res_15000Hz_allKeys):
                res_15000Hz.keys = _res_15000Hz_allKeys[-1].name  # just the last key pressed
                res_15000Hz.rt = _res_15000Hz_allKeys[-1].rt
                res_15000Hz.duration = _res_15000Hz_allKeys[-1].duration
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
        for thisComponent in audio_15000HzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "audio_15000Hz" ---
    for thisComponent in audio_15000HzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audio_15000Hz.stopped', globalClock.getTime(format='float'))
    sound_15000.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if res_15000Hz.keys in ['', [], None]:  # No response was made
        res_15000Hz.keys = None
    thisExp.addData('res_15000Hz.keys',res_15000Hz.keys)
    if res_15000Hz.keys != None:  # we had a response
        thisExp.addData('res_15000Hz.rt', res_15000Hz.rt)
        thisExp.addData('res_15000Hz.duration', res_15000Hz.duration)
    thisExp.nextEntry()
    # the Routine "audio_15000Hz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "outro" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('outro.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    outroComponents = [text_outro]
    for thisComponent in outroComponents:
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
    
    # --- Run Routine "outro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_outro* updates
        
        # if text_outro is starting this frame...
        if text_outro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_outro.frameNStart = frameN  # exact frame index
            text_outro.tStart = t  # local t and not account for scr refresh
            text_outro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_outro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_outro.started')
            # update status
            text_outro.status = STARTED
            text_outro.setAutoDraw(True)
        
        # if text_outro is active this frame...
        if text_outro.status == STARTED:
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
        for thisComponent in outroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "outro" ---
    for thisComponent in outroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('outro.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "outro" was not non-slip safe, so reset the non-slip timer
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
