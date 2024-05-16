from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.input.DesktopInput as _DesktopInput
_DesktopInput = _DesktopInput
try:
    from pyquantum.client.input import util
except ImportError:
    util = _import_once("pyquantum.client.input.util")

import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.client.input import key
except ImportError:
    key = _import_once("pyquantum.client.input.key")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.input.GameInput as _GameInput
_GameInput = _GameInput
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = _import_once("pygdx.controllers")

import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DesktopInput():
    """dev.ultreon.quantum.client.input.DesktopInput"""
 
    @staticmethod
    def _wrap(java_value: _DesktopInput) -> 'DesktopInput':
        return DesktopInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DesktopInput):
        """
        Dynamic initializer for DesktopInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DesktopInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DesktopInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.HIDE_HUD_KEY
    HIDE_HUD_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.HIDE_HUD_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.IM_GUI_FOCUS_KEY
    IM_GUI_FOCUS_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.IM_GUI_FOCUS_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.THIRD_PERSON_KEY
    THIRD_PERSON_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.THIRD_PERSON_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.COMMAND_KEY
    COMMAND_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.COMMAND_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.DEBUG_KEY
    DEBUG_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.DEBUG_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.INVENTORY_KEY
    INVENTORY_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.INVENTORY_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.CHAT_KEY
    CHAT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.CHAT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.INSPECT_KEY
    INSPECT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.INSPECT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.SCREENSHOT_KEY
    SCREENSHOT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.SCREENSHOT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.IM_GUI_KEY
    IM_GUI_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.IM_GUI_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.PAUSE_KEY
    PAUSE_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.PAUSE_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.DROP_ITEM_KEY
    DROP_ITEM_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.DROP_ITEM_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.FULL_SCREEN_KEY
    FULL_SCREEN_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.FULL_SCREEN_KEY)


    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool._wrap(_GameInput.isKeyDown(_int.valueOf(arg0)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.scrolled(float,float)"""
        return bool._wrap(super(_DesktopInput, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.DesktopInput.update(float)"""
        super(_DesktopInput, self).update(_float.valueOf(arg0))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonDown(arg0))

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool._wrap(super(_GameInput, self).axisMoved(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool._wrap(_GameInput.startVibration(_int.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonJustPressed(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.input.GameInput.dispose()"""
        super(GameInput, self).dispose()

    @override
    @overload
    def update(self):
        """public void dev.ultreon.quantum.client.input.GameInput.update()"""
        super(GameInput, self).update()

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).disconnected(arg0)

    @staticmethod
    @overload
    def setCursorCaught(arg0: bool):
        """public static void dev.ultreon.quantum.client.input.DesktopInput.setCursorCaught(boolean)"""
        _DesktopInput.setCursorCaught(_boolean.valueOf(arg0))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonUp(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isPressingAnyButton() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isPressingAnyButton()"""
        return bool._wrap(_DesktopInput.isPressingAnyButton())

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonDown(arg0, _int.valueOf(arg1)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_DesktopInput, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyTyped(char)"""
        return bool._wrap(super(_DesktopInput, self).keyTyped(_char.valueOf(arg0)))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchUp(int,int,int,int)"""
        return bool._wrap(super(_DesktopInput, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchDragged(int,int,int)"""
        return bool._wrap(super(_DesktopInput, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def isCtrlDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isCtrlDown()"""
        return bool._wrap(_DesktopInput.isCtrlDown())

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool._wrap(_GameInput.cancelVibration())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2._wrap(_GameInput.getJoystick(arg0))

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'Camera'):
        """public dev.ultreon.quantum.client.input.DesktopInput(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.Camera)"""
        val = _DesktopInput(arg0, arg1)
        self.__wrapper = val

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchDown(int,int,int,int)"""
        return bool._wrap(super(_DesktopInput, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).connected(arg0)

    @staticmethod
    @overload
    def isShiftDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isShiftDown()"""
        return bool._wrap(_DesktopInput.isShiftDown())

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'._wrap(super(_GameInput, self).useItem(arg0, arg1, arg2))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyDown(int)"""
        return bool._wrap(super(_DesktopInput, self).keyDown(_int.valueOf(arg0)))

    @override
    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool._wrap(super(GameInput, self).isControllerConnected())

    @staticmethod
    @overload
    def isAltDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isAltDown()"""
        return bool._wrap(_DesktopInput.isAltDown())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getMouseDelta() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.DesktopInput.getMouseDelta()"""
        return math.Vector2._wrap(_DesktopInput.getMouseDelta())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.mouseMoved(int,int)"""
        return bool._wrap(super(_DesktopInput, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyUp(int)"""
        return bool._wrap(super(_DesktopInput, self).keyUp(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.input.DesktopInput
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.input.DesktopInput as _DesktopInput
_DesktopInput = _DesktopInput
try:
    from pyquantum.client.input import util
except ImportError:
    util = _import_once("pyquantum.client.input.util")

import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.client.input import key
except ImportError:
    key = _import_once("pyquantum.client.input.key")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.input.GameInput as _GameInput
_GameInput = _GameInput
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = _import_once("pygdx.controllers")

import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DesktopInput():
    """dev.ultreon.quantum.client.input.DesktopInput"""
 
    @staticmethod
    def _wrap(java_value: _DesktopInput) -> 'DesktopInput':
        return DesktopInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DesktopInput):
        """
        Dynamic initializer for DesktopInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DesktopInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DesktopInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.HIDE_HUD_KEY
    HIDE_HUD_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.HIDE_HUD_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.IM_GUI_FOCUS_KEY
    IM_GUI_FOCUS_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.IM_GUI_FOCUS_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.THIRD_PERSON_KEY
    THIRD_PERSON_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.THIRD_PERSON_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.COMMAND_KEY
    COMMAND_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.COMMAND_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.DEBUG_KEY
    DEBUG_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.DEBUG_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.INVENTORY_KEY
    INVENTORY_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.INVENTORY_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.CHAT_KEY
    CHAT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.CHAT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.INSPECT_KEY
    INSPECT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.INSPECT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.SCREENSHOT_KEY
    SCREENSHOT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.SCREENSHOT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.IM_GUI_KEY
    IM_GUI_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.IM_GUI_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.PAUSE_KEY
    PAUSE_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.PAUSE_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.DROP_ITEM_KEY
    DROP_ITEM_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.DROP_ITEM_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.FULL_SCREEN_KEY
    FULL_SCREEN_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.FULL_SCREEN_KEY)


    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool._wrap(_GameInput.isKeyDown(_int.valueOf(arg0)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.scrolled(float,float)"""
        return bool._wrap(super(_DesktopInput, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.DesktopInput.update(float)"""
        super(_DesktopInput, self).update(_float.valueOf(arg0))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonDown(arg0))

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool._wrap(super(_GameInput, self).axisMoved(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool._wrap(_GameInput.startVibration(_int.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonJustPressed(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.input.GameInput.dispose()"""
        super(GameInput, self).dispose()

    @override
    @overload
    def update(self):
        """public void dev.ultreon.quantum.client.input.GameInput.update()"""
        super(GameInput, self).update()

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).disconnected(arg0)

    @staticmethod
    @overload
    def setCursorCaught(arg0: bool):
        """public static void dev.ultreon.quantum.client.input.DesktopInput.setCursorCaught(boolean)"""
        _DesktopInput.setCursorCaught(_boolean.valueOf(arg0))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonUp(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isPressingAnyButton() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isPressingAnyButton()"""
        return bool._wrap(_DesktopInput.isPressingAnyButton())

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonDown(arg0, _int.valueOf(arg1)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_DesktopInput, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyTyped(char)"""
        return bool._wrap(super(_DesktopInput, self).keyTyped(_char.valueOf(arg0)))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchUp(int,int,int,int)"""
        return bool._wrap(super(_DesktopInput, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchDragged(int,int,int)"""
        return bool._wrap(super(_DesktopInput, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def isCtrlDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isCtrlDown()"""
        return bool._wrap(_DesktopInput.isCtrlDown())

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool._wrap(_GameInput.cancelVibration())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2._wrap(_GameInput.getJoystick(arg0))

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'Camera'):
        """public dev.ultreon.quantum.client.input.DesktopInput(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.Camera)"""
        val = _DesktopInput(arg0, arg1)
        self.__wrapper = val

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchDown(int,int,int,int)"""
        return bool._wrap(super(_DesktopInput, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).connected(arg0)

    @staticmethod
    @overload
    def isShiftDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isShiftDown()"""
        return bool._wrap(_DesktopInput.isShiftDown())

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'._wrap(super(_GameInput, self).useItem(arg0, arg1, arg2))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyDown(int)"""
        return bool._wrap(super(_DesktopInput, self).keyDown(_int.valueOf(arg0)))

    @override
    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool._wrap(super(GameInput, self).isControllerConnected())

    @staticmethod
    @overload
    def isAltDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isAltDown()"""
        return bool._wrap(_DesktopInput.isAltDown())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getMouseDelta() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.DesktopInput.getMouseDelta()"""
        return math.Vector2._wrap(_DesktopInput.getMouseDelta())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.mouseMoved(int,int)"""
        return bool._wrap(super(_DesktopInput, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyUp(int)"""
        return bool._wrap(super(_DesktopInput, self).keyUp(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.input.DesktopInput 
 
 
# CLASS: dev.ultreon.quantum.client.input.TouchPoint
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.lang.Integer as _int
from builtins import bool
import dev.ultreon.quantum.client.input.TouchPoint as _TouchPoint
_TouchPoint = _TouchPoint
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TouchPoint():
    """dev.ultreon.quantum.client.input.TouchPoint"""
 
    @staticmethod
    def _wrap(java_value: _TouchPoint) -> 'TouchPoint':
        return TouchPoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TouchPoint):
        """
        Dynamic initializer for TouchPoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TouchPoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TouchPoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def pointer(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.pointer()"""
        return int._wrap(super(TouchPoint, self).pointer())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.hashCode()"""
        return int._wrap(super(TouchPoint, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.input.TouchPoint.toString()"""
        return str._wrap(super(TouchPoint, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseY(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.mouseY()"""
        return int._wrap(super(TouchPoint, self).mouseY())

    @overload
    def pos(self) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.client.input.TouchPoint.pos()"""
        return 'vector.Vec2i'._wrap(super(TouchPoint, self).pos())

    @overload
    def mouseX(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.mouseX()"""
        return int._wrap(super(TouchPoint, self).mouseX())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.input.TouchPoint(int,int,int,int)"""
        val = _TouchPoint(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchPoint.equals(java.lang.Object)"""
        return bool._wrap(super(_TouchPoint, self).equals(arg0))

    @overload
    def button(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.button()"""
        return int._wrap(super(TouchPoint, self).button()) 
 
 
# CLASS: dev.ultreon.quantum.client.input.GameCamera
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.input.GameCamera as _GameCamera
_GameCamera = _GameCamera
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.graphics.PerspectiveCamera as _PerspectiveCamera
_PerspectiveCamera = _PerspectiveCamera
from builtins import float
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.QuantumClient as _QuantumClient
_QuantumClient = _QuantumClient
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameCamera():
    """dev.ultreon.quantum.client.input.GameCamera"""
 
    @staticmethod
    def _wrap(java_value: _GameCamera) -> 'GameCamera':
        return GameCamera(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameCamera):
        """
        Dynamic initializer for GameCamera.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameCamera__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameCamera__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def update(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.PerspectiveCamera.update(boolean)"""
        super(_graphics.PerspectiveCamera, self).update(_boolean.valueOf(arg0))

    @override
    @overload
    def lookAt(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(com.badlogic.gdx.math.Vector3)"""
        super(_graphics.Camera, self).lookAt(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float,float,float,float,float)"""
        return 'collision.Ray'._wrap(super(_graphics.Camera, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_graphics.Camera, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(float,float,float,float)"""
        super(_graphics.Camera, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.transform(com.badlogic.gdx.math.Matrix4)"""
        super(_graphics.Camera, self).transform(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def lookAt(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(float,float,float)"""
        super(_graphics.Camera, self).lookAt(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def project(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'._wrap(super(_graphics.Camera, self).project(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_graphics.Camera, self).unproject(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def relative(self, arg0: 'Vec3d', arg1: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.input.GameCamera.relative(dev.ultreon.libs.commons.v0.vector.Vec3d,com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_GameCamera, self).relative(arg0, arg1))

    @override
    @overload
    def normalizeUp(self):
        """public void com.badlogic.gdx.graphics.Camera.normalizeUp()"""
        super(graphics.Camera, self).normalizeUp()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.PerspectiveCamera.update()"""
        super(graphics.PerspectiveCamera, self).update()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def unproject(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'._wrap(super(_graphics.Camera, self).unproject(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.client.input.GameCamera(float,float,float)"""
        val = _GameCamera(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def rotateAround(self, arg0: 'Vector3', arg1: 'Vector3', arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.rotateAround(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        super(_graphics.Camera, self).rotateAround(arg0, arg1, _float.valueOf(arg2))

    @overload
    def getFovModifier(self) -> float:
        """public float dev.ultreon.quantum.client.input.GameCamera.getFovModifier()"""
        return float._wrap(super(GameCamera, self).getFovModifier())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.translate(float,float,float)"""
        super(_graphics.Camera, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def setFovModifier(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.GameCamera.setFovModifier(float)"""
        super(_GameCamera, self).setFovModifier(_float.valueOf(arg0))

    @override
    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.translate(com.badlogic.gdx.math.Vector3)"""
        super(_graphics.Camera, self).translate(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getCamPos(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.client.input.GameCamera.getCamPos()"""
        return 'vector.Vec3d'._wrap(super(GameCamera, self).getCamPos())

    @override
    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(_graphics.Camera, self).rotate(arg0, _float.valueOf(arg1))

    @override
    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(_graphics.Camera, self).rotate(arg0)

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_graphics.Camera, self).project(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def rotate(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Matrix4)"""
        super(_graphics.Camera, self).rotate(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @property
    def client(self) -> QuantumClient:
        return QuantumClient._wrap(super(_GameCamera).client())

    @overload
    def update(self, arg0: 'LocalPlayer'):
        """public void dev.ultreon.quantum.client.input.GameCamera.update(dev.ultreon.quantum.client.player.LocalPlayer)"""
        super(_GameCamera, self).update(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.input.TouchscreenInput
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.input import util
except ImportError:
    util = _import_once("pyquantum.client.input.util")

import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.client.input import key
except ImportError:
    key = _import_once("pyquantum.client.input.key")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.input.GameInput as _GameInput
_GameInput = _GameInput
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = _import_once("pygdx.controllers")

import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.input.TouchscreenInput as _TouchscreenInput
_TouchscreenInput = _TouchscreenInput
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TouchscreenInput():
    """dev.ultreon.quantum.client.input.TouchscreenInput"""
 
    @staticmethod
    def _wrap(java_value: _TouchscreenInput) -> 'TouchscreenInput':
        return TouchscreenInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TouchscreenInput):
        """
        Dynamic initializer for TouchscreenInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TouchscreenInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TouchscreenInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.SCREENSHOT_KEY
    SCREENSHOT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.SCREENSHOT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.INVENTORY_KEY
    INVENTORY_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.INVENTORY_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.PAUSE_KEY
    PAUSE_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.PAUSE_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.FULL_SCREEN_KEY
    FULL_SCREEN_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.FULL_SCREEN_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.COMMAND_KEY
    COMMAND_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.COMMAND_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.CHAT_KEY
    CHAT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.CHAT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.IM_GUI_KEY
    IM_GUI_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.IM_GUI_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.IM_GUI_FOCUS_KEY
    IM_GUI_FOCUS_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.IM_GUI_FOCUS_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.HIDE_HUD_KEY
    HIDE_HUD_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.HIDE_HUD_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.THIRD_PERSON_KEY
    THIRD_PERSON_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.THIRD_PERSON_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.DEBUG_KEY
    DEBUG_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.DEBUG_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.INSPECT_KEY
    INSPECT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.INSPECT_KEY)


    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool._wrap(_GameInput.isKeyDown(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonDown(arg0))

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool._wrap(super(_GameInput, self).axisMoved(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.touchDown(int,int,int,int)"""
        return bool._wrap(super(_TouchscreenInput, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.touchDragged(int,int,int)"""
        return bool._wrap(super(_TouchscreenInput, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.keyDown(int)"""
        return bool._wrap(super(_TouchscreenInput, self).keyDown(_int.valueOf(arg0)))

    @override
    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.TouchscreenInput.update(float)"""
        super(_TouchscreenInput, self).update(_float.valueOf(arg0))

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool._wrap(_GameInput.startVibration(_int.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonJustPressed(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getMouseDelta() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.TouchscreenInput.getMouseDelta()"""
        return math.Vector2._wrap(_TouchscreenInput.getMouseDelta())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.input.GameInput.dispose()"""
        super(GameInput, self).dispose()

    @override
    @overload
    def update(self):
        """public void dev.ultreon.quantum.client.input.GameInput.update()"""
        super(GameInput, self).update()

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).disconnected(arg0)

    @staticmethod
    @overload
    def setCursorCaught(arg0: bool):
        """public static void dev.ultreon.quantum.client.input.TouchscreenInput.setCursorCaught(boolean)"""
        _TouchscreenInput.setCursorCaught(_boolean.valueOf(arg0))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonUp(arg0, _int.valueOf(arg1)))

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonDown(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'Camera'):
        """public dev.ultreon.quantum.client.input.TouchscreenInput(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.Camera)"""
        val = _TouchscreenInput(arg0, arg1)
        self.__wrapper = val

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.touchUp(int,int,int,int)"""
        return bool._wrap(super(_TouchscreenInput, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool._wrap(_GameInput.cancelVibration())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2._wrap(_GameInput.getJoystick(arg0))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.keyTyped(char)"""
        return bool._wrap(super(_TouchscreenInput, self).keyTyped(_char.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).connected(arg0)

    @staticmethod
    @overload
    def isPressingAnyButton() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.TouchscreenInput.isPressingAnyButton()"""
        return bool._wrap(_TouchscreenInput.isPressingAnyButton())

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'._wrap(super(_GameInput, self).useItem(arg0, arg1, arg2))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.scrolled(float,float)"""
        return bool._wrap(super(_TouchscreenInput, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool._wrap(super(GameInput, self).isControllerConnected())

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_TouchscreenInput, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.keyUp(int)"""
        return bool._wrap(super(_TouchscreenInput, self).keyUp(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.mouseMoved(int,int)"""
        return bool._wrap(super(_TouchscreenInput, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.input.GameInput
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
try:
    from pyquantum.client.input import util
except ImportError:
    util = _import_once("pyquantum.client.input.util")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.input.GameInput as _GameInput
_GameInput = _GameInput
import com.badlogic.gdx.InputProcessor as _InputProcessor
_InputProcessor = _InputProcessor
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pygdx import controllers
except ImportError:
    controllers = _import_once("pygdx.controllers")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameInput():
    """dev.ultreon.quantum.client.input.GameInput"""
 
    @staticmethod
    def _wrap(java_value: _GameInput) -> 'GameInput':
        return GameInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameInput):
        """
        Dynamic initializer for GameInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.GameInput.update(float)"""
        super(_GameInput, self).update(_float.valueOf(arg0))

    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool._wrap(_GameInput.isKeyDown(_int.valueOf(arg0)))

    @abstractmethod
    def keyTyped(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.InputProcessor.keyTyped(char)"""
        pass

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.keyUp(int)"""
        return bool._wrap(super(_GameInput, self).keyUp(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonDown(arg0))

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool._wrap(super(_GameInput, self).axisMoved(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def update(self):
        """public void dev.ultreon.quantum.client.input.GameInput.update()"""
        super(GameInput, self).update()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchDown(int,int,int,int)"""
        pass

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool._wrap(_GameInput.startVibration(_int.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonJustPressed(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.input.GameInput.dispose()"""
        super(GameInput, self).dispose()

    @abstractmethod
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchCancelled(int,int,int,int)"""
        pass

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).disconnected(arg0)

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonUp(arg0, _int.valueOf(arg1)))

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonDown(arg0, _int.valueOf(arg1)))

    @abstractmethod
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchUp(int,int,int,int)"""
        pass

    @abstractmethod
    def mouseMoved(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.mouseMoved(int,int)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool._wrap(super(GameInput, self).isControllerConnected())

    @abstractmethod
    def touchDragged(self, arg0: int, arg1: int, arg2: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchDragged(int,int,int)"""
        pass

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool._wrap(_GameInput.cancelVibration())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2._wrap(_GameInput.getJoystick(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).connected(arg0)

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'._wrap(super(_GameInput, self).useItem(arg0, arg1, arg2))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.keyDown(int)"""
        return bool._wrap(super(_GameInput, self).keyDown(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def scrolled(self, arg0: float, arg1: float):
        """public abstract boolean com.badlogic.gdx.InputProcessor.scrolled(float,float)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.input.GyroscopeInput
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.input import util
except ImportError:
    util = _import_once("pyquantum.client.input.util")

import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.client.input import key
except ImportError:
    key = _import_once("pyquantum.client.input.key")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.input.GameInput as _GameInput
_GameInput = _GameInput
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = _import_once("pygdx.controllers")

import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.input.GyroscopeInput as _GyroscopeInput
_GyroscopeInput = _GyroscopeInput
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GyroscopeInput():
    """dev.ultreon.quantum.client.input.GyroscopeInput"""
 
    @staticmethod
    def _wrap(java_value: _GyroscopeInput) -> 'GyroscopeInput':
        return GyroscopeInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GyroscopeInput):
        """
        Dynamic initializer for GyroscopeInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GyroscopeInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GyroscopeInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.INVENTORY_KEY
    INVENTORY_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.INVENTORY_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.COMMAND_KEY
    COMMAND_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.COMMAND_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.PAUSE_KEY
    PAUSE_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.PAUSE_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.THIRD_PERSON_KEY
    THIRD_PERSON_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.THIRD_PERSON_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.HIDE_HUD_KEY
    HIDE_HUD_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.HIDE_HUD_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.IM_GUI_FOCUS_KEY
    IM_GUI_FOCUS_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.IM_GUI_FOCUS_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.INSPECT_KEY
    INSPECT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.INSPECT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.FULL_SCREEN_KEY
    FULL_SCREEN_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.FULL_SCREEN_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.SCREENSHOT_KEY
    SCREENSHOT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.SCREENSHOT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.IM_GUI_KEY
    IM_GUI_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.IM_GUI_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.DEBUG_KEY
    DEBUG_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.DEBUG_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.CHAT_KEY
    CHAT_KEY: 'key.KeyBind' = _wrap(_key.KeyBind.CHAT_KEY)


    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool._wrap(_GameInput.isKeyDown(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonDown(arg0))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.touchDragged(int,int,int)"""
        return bool._wrap(super(_GyroscopeInput, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool._wrap(super(_GameInput, self).axisMoved(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.GyroscopeInput.update(float)"""
        super(_GyroscopeInput, self).update(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.keyUp(int)"""
        return bool._wrap(super(_GyroscopeInput, self).keyUp(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def getMouseDelta() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GyroscopeInput.getMouseDelta()"""
        return math.Vector2._wrap(_GyroscopeInput.getMouseDelta())

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool._wrap(_GameInput.startVibration(_int.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool._wrap(_GameInput.isControllerButtonJustPressed(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.input.GameInput.dispose()"""
        super(GameInput, self).dispose()

    @override
    @overload
    def update(self):
        """public void dev.ultreon.quantum.client.input.GameInput.update()"""
        super(GameInput, self).update()

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.touchUp(int,int,int,int)"""
        return bool._wrap(super(_GyroscopeInput, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).disconnected(arg0)

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonUp(arg0, _int.valueOf(arg1)))

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_GameInput, self).buttonDown(arg0, _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.keyTyped(char)"""
        return bool._wrap(super(_GyroscopeInput, self).keyTyped(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool._wrap(_GameInput.cancelVibration())

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.touchDown(int,int,int,int)"""
        return bool._wrap(super(_GyroscopeInput, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isPressingAnyButton() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GyroscopeInput.isPressingAnyButton()"""
        return bool._wrap(_GyroscopeInput.isPressingAnyButton())

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2._wrap(_GameInput.getJoystick(arg0))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.scrolled(float,float)"""
        return bool._wrap(super(_GyroscopeInput, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'Camera'):
        """public dev.ultreon.quantum.client.input.GyroscopeInput(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.Camera)"""
        val = _GyroscopeInput(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(_GameInput, self).connected(arg0)

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'._wrap(super(_GameInput, self).useItem(arg0, arg1, arg2))

    @override
    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool._wrap(super(GameInput, self).isControllerConnected())

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.mouseMoved(int,int)"""
        return bool._wrap(super(_GyroscopeInput, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_GyroscopeInput, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.keyDown(int)"""
        return bool._wrap(super(_GyroscopeInput, self).keyDown(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def setCursorCaught(arg0: bool):
        """public static void dev.ultreon.quantum.client.input.GyroscopeInput.setCursorCaught(boolean)"""
        _GyroscopeInput.setCursorCaught(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.input.PlayerInput
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.client.input.PlayerInput as _PlayerInput
_PlayerInput = _PlayerInput
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerInput():
    """dev.ultreon.quantum.client.input.PlayerInput"""
 
    @staticmethod
    def _wrap(java_value: _PlayerInput) -> 'PlayerInput':
        return PlayerInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerInput):
        """
        Dynamic initializer for PlayerInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.input.PlayerInput(dev.ultreon.quantum.client.QuantumClient)"""
        val = _PlayerInput(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def tick(self, arg0: 'Player', arg1: float):
        """public void dev.ultreon.quantum.client.input.PlayerInput.tick(dev.ultreon.quantum.entity.player.Player,float)"""
        super(_PlayerInput, self).tick(arg0, _float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.PlayerInput.isWalking()"""
        return bool._wrap(super(PlayerInput, self).isWalking())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getVelocity(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.input.PlayerInput.getVelocity()"""
        return 'math.Vector3'._wrap(super(PlayerInput, self).getVelocity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getVel(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.client.input.PlayerInput.getVel()"""
        return 'vector.Vec3d'._wrap(super(PlayerInput, self).getVel())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())