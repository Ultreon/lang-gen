from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.input import util
except ImportError:
    util = __import_once__("pyquantum.client.input.util")

import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
try:
    from pyquantum.client.input import key
except ImportError:
    key = __import_once__("pyquantum.client.input.key")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.input.GameInput as __GameInput
__GameInput = __GameInput
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = __import_once__("pygdx.controllers")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
import dev.ultreon.quantum.client.input.DesktopInput as __DesktopInput
__DesktopInput = __DesktopInput
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class DesktopInput(__GameInput, GameInput):
    """dev.ultreon.quantum.client.input.DesktopInput"""
 
    @staticmethod
    def __wrap(java_value: __DesktopInput) -> 'DesktopInput':
        return DesktopInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DesktopInput):
        """
        Dynamic initializer for DesktopInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.DEBUG_KEY
    DEBUG_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.DEBUG_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.THIRD_PERSON_KEY
    THIRD_PERSON_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.THIRD_PERSON_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.HIDE_HUD_KEY
    HIDE_HUD_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.HIDE_HUD_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.DROP_ITEM_KEY
    DROP_ITEM_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.DROP_ITEM_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.INSPECT_KEY
    INSPECT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.INSPECT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.IM_GUI_FOCUS_KEY
    IM_GUI_FOCUS_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.IM_GUI_FOCUS_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.CHAT_KEY
    CHAT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.CHAT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.PAUSE_KEY
    PAUSE_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.PAUSE_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.INVENTORY_KEY
    INVENTORY_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.INVENTORY_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.SCREENSHOT_KEY
    SCREENSHOT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.SCREENSHOT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.IM_GUI_KEY
    IM_GUI_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.IM_GUI_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.COMMAND_KEY
    COMMAND_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.COMMAND_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.FULL_SCREEN_KEY
    FULL_SCREEN_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.FULL_SCREEN_KEY)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonDown(arg0))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2.__wrap(__GameInput.getJoystick(arg0))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__DesktopInput, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def isShiftDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isShiftDown()"""
        return bool.__wrap(__DesktopInput.isShiftDown())

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'Camera'):
        """public dev.ultreon.quantum.client.input.DesktopInput(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.Camera)"""
        val = __DesktopInput(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'.__wrap(super(__GameInput, self).useItem(arg0, arg1, arg2))

    @override
    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.DesktopInput.update(float)"""
        super(__DesktopInput, self).update(__float.valueOf(arg0))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonUp(arg0, __int.valueOf(arg1)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchDragged(int,int,int)"""
        return bool.__wrap(super(__DesktopInput, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isAltDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isAltDown()"""
        return bool.__wrap(__DesktopInput.isAltDown())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isPressingAnyButton() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isPressingAnyButton()"""
        return bool.__wrap(__DesktopInput.isPressingAnyButton())

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
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__DesktopInput, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool.__wrap(super(__GameInput, self).axisMoved(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonJustPressed(arg0))

    @staticmethod
    @overload
    def getMouseDelta() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.DesktopInput.getMouseDelta()"""
        return math.Vector2.__wrap(__DesktopInput.getMouseDelta())

    @staticmethod
    @overload
    def setCursorCaught(arg0: bool):
        """public static void dev.ultreon.quantum.client.input.DesktopInput.setCursorCaught(boolean)"""
        __DesktopInput.setCursorCaught(__boolean.valueOf(arg0))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.mouseMoved(int,int)"""
        return bool.__wrap(super(__DesktopInput, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyUp(int)"""
        return bool.__wrap(super(__DesktopInput, self).keyUp(__int.valueOf(arg0)))

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).disconnected(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.scrolled(float,float)"""
        return bool.__wrap(super(__DesktopInput, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).connected(arg0)

    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool.__wrap(__GameInput.isKeyDown(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def isCtrlDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isCtrlDown()"""
        return bool.__wrap(__DesktopInput.isCtrlDown())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__DesktopInput, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyTyped(char)"""
        return bool.__wrap(super(__DesktopInput, self).keyTyped(__char.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyDown(int)"""
        return bool.__wrap(super(__DesktopInput, self).keyDown(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool.__wrap(__GameInput.startVibration(__int.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool.__wrap(__GameInput.cancelVibration())

    @override
    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool.__wrap(super(GameInput, self).isControllerConnected())

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonDown(arg0, __int.valueOf(arg1)))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.DesktopInput
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.input import util
except ImportError:
    util = __import_once__("pyquantum.client.input.util")

import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
try:
    from pyquantum.client.input import key
except ImportError:
    key = __import_once__("pyquantum.client.input.key")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.input.GameInput as __GameInput
__GameInput = __GameInput
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = __import_once__("pygdx.controllers")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
import dev.ultreon.quantum.client.input.DesktopInput as __DesktopInput
__DesktopInput = __DesktopInput
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class DesktopInput(__GameInput, GameInput):
    """dev.ultreon.quantum.client.input.DesktopInput"""
 
    @staticmethod
    def __wrap(java_value: __DesktopInput) -> 'DesktopInput':
        return DesktopInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DesktopInput):
        """
        Dynamic initializer for DesktopInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.DEBUG_KEY
    DEBUG_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.DEBUG_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.THIRD_PERSON_KEY
    THIRD_PERSON_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.THIRD_PERSON_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.HIDE_HUD_KEY
    HIDE_HUD_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.HIDE_HUD_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.DROP_ITEM_KEY
    DROP_ITEM_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.DROP_ITEM_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.INSPECT_KEY
    INSPECT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.INSPECT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.IM_GUI_FOCUS_KEY
    IM_GUI_FOCUS_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.IM_GUI_FOCUS_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.CHAT_KEY
    CHAT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.CHAT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.PAUSE_KEY
    PAUSE_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.PAUSE_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.INVENTORY_KEY
    INVENTORY_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.INVENTORY_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.SCREENSHOT_KEY
    SCREENSHOT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.SCREENSHOT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.IM_GUI_KEY
    IM_GUI_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.IM_GUI_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.COMMAND_KEY
    COMMAND_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.COMMAND_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.DesktopInput.FULL_SCREEN_KEY
    FULL_SCREEN_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.FULL_SCREEN_KEY)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonDown(arg0))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2.__wrap(__GameInput.getJoystick(arg0))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__DesktopInput, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def isShiftDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isShiftDown()"""
        return bool.__wrap(__DesktopInput.isShiftDown())

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'Camera'):
        """public dev.ultreon.quantum.client.input.DesktopInput(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.Camera)"""
        val = __DesktopInput(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'.__wrap(super(__GameInput, self).useItem(arg0, arg1, arg2))

    @override
    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.DesktopInput.update(float)"""
        super(__DesktopInput, self).update(__float.valueOf(arg0))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonUp(arg0, __int.valueOf(arg1)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchDragged(int,int,int)"""
        return bool.__wrap(super(__DesktopInput, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isAltDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isAltDown()"""
        return bool.__wrap(__DesktopInput.isAltDown())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isPressingAnyButton() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isPressingAnyButton()"""
        return bool.__wrap(__DesktopInput.isPressingAnyButton())

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
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__DesktopInput, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool.__wrap(super(__GameInput, self).axisMoved(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonJustPressed(arg0))

    @staticmethod
    @overload
    def getMouseDelta() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.DesktopInput.getMouseDelta()"""
        return math.Vector2.__wrap(__DesktopInput.getMouseDelta())

    @staticmethod
    @overload
    def setCursorCaught(arg0: bool):
        """public static void dev.ultreon.quantum.client.input.DesktopInput.setCursorCaught(boolean)"""
        __DesktopInput.setCursorCaught(__boolean.valueOf(arg0))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.mouseMoved(int,int)"""
        return bool.__wrap(super(__DesktopInput, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyUp(int)"""
        return bool.__wrap(super(__DesktopInput, self).keyUp(__int.valueOf(arg0)))

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).disconnected(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.scrolled(float,float)"""
        return bool.__wrap(super(__DesktopInput, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).connected(arg0)

    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool.__wrap(__GameInput.isKeyDown(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def isCtrlDown() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.DesktopInput.isCtrlDown()"""
        return bool.__wrap(__DesktopInput.isCtrlDown())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__DesktopInput, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyTyped(char)"""
        return bool.__wrap(super(__DesktopInput, self).keyTyped(__char.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.DesktopInput.keyDown(int)"""
        return bool.__wrap(super(__DesktopInput, self).keyDown(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool.__wrap(__GameInput.startVibration(__int.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool.__wrap(__GameInput.cancelVibration())

    @override
    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool.__wrap(super(GameInput, self).isControllerConnected())

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonDown(arg0, __int.valueOf(arg1)))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.DesktopInput 
 
 
# CLASS: dev.ultreon.quantum.client.input.TouchPoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.input.TouchPoint as __TouchPoint
__TouchPoint = __TouchPoint
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TouchPoint():
    """dev.ultreon.quantum.client.input.TouchPoint"""
 
    @staticmethod
    def __wrap(java_value: __TouchPoint) -> 'TouchPoint':
        return TouchPoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TouchPoint):
        """
        Dynamic initializer for TouchPoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def pointer(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.pointer()"""
        return int.__wrap(super(TouchPoint, self).pointer())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.input.TouchPoint(int,int,int,int)"""
        val = __TouchPoint(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mouseX(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.mouseX()"""
        return int.__wrap(super(TouchPoint, self).mouseX())

    @overload
    def pos(self) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.client.input.TouchPoint.pos()"""
        return 'vector.Vec2i'.__wrap(super(TouchPoint, self).pos())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchPoint.equals(java.lang.Object)"""
        return bool.__wrap(super(__TouchPoint, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def button(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.button()"""
        return int.__wrap(super(TouchPoint, self).button())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.hashCode()"""
        return int.__wrap(super(TouchPoint, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.input.TouchPoint.toString()"""
        return str.__wrap(super(TouchPoint, self).toString())

    @overload
    def mouseY(self) -> int:
        """public int dev.ultreon.quantum.client.input.TouchPoint.mouseY()"""
        return int.__wrap(super(TouchPoint, self).mouseY())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.input.GameCamera
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import dev.ultreon.quantum.client.input.GameCamera as __GameCamera
__GameCamera = __GameCamera
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
from builtins import float
import dev.ultreon.quantum.client.QuantumClient as __QuantumClient
__QuantumClient = __QuantumClient
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import com.badlogic.gdx.graphics.PerspectiveCamera as __PerspectiveCamera
__PerspectiveCamera = __PerspectiveCamera
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
from builtins import int
 
class GameCamera(pygdx.__PerspectiveCamera, graphics.PerspectiveCamera):
    """dev.ultreon.quantum.client.input.GameCamera"""
 
    @staticmethod
    def __wrap(java_value: __GameCamera) -> 'GameCamera':
        return GameCamera(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameCamera):
        """
        Dynamic initializer for GameCamera.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__graphics.Camera, self).project(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.client.input.GameCamera(float,float,float)"""
        val = __GameCamera(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def update(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.PerspectiveCamera.update(boolean)"""
        super(__graphics.PerspectiveCamera, self).update(__boolean.valueOf(arg0))

    @overload
    def getPickRay(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float,float,float,float,float)"""
        return 'collision.Ray'.__wrap(super(__graphics.Camera, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def rotate(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Matrix4)"""
        super(__graphics.Camera, self).rotate(arg0)

    @override
    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(float,float,float,float)"""
        super(__graphics.Camera, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def lookAt(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(float,float,float)"""
        super(__graphics.Camera, self).lookAt(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(__graphics.Camera, self).rotate(arg0, __float.valueOf(arg1))

    @override
    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.translate(com.badlogic.gdx.math.Vector3)"""
        super(__graphics.Camera, self).translate(arg0)

    @override
    @overload
    def normalizeUp(self):
        """public void com.badlogic.gdx.graphics.Camera.normalizeUp()"""
        super(graphics.Camera, self).normalizeUp()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def rotateAround(self, arg0: 'Vector3', arg1: 'Vector3', arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.rotateAround(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        super(__graphics.Camera, self).rotateAround(arg0, arg1, __float.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def update(self, arg0: 'LocalPlayer'):
        """public void dev.ultreon.quantum.client.input.GameCamera.update(dev.ultreon.quantum.client.player.LocalPlayer)"""
        super(__GameCamera, self).update(arg0)

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.PerspectiveCamera.update()"""
        super(graphics.PerspectiveCamera, self).update()

    @override
    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(__graphics.Camera, self).rotate(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__graphics.Camera, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def getFovModifier(self) -> float:
        """public float dev.ultreon.quantum.client.input.GameCamera.getFovModifier()"""
        return float.__wrap(super(GameCamera, self).getFovModifier())

    @overload
    def getCamPos(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.client.input.GameCamera.getCamPos()"""
        return 'vector.Vec3d'.__wrap(super(GameCamera, self).getCamPos())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @property
    def client(self) -> QuantumClient:
        return QuantumClient.__wrap(super(__GameCamera).client())

    @overload
    def unproject(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'.__wrap(super(__graphics.Camera, self).unproject(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @override
    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.transform(com.badlogic.gdx.math.Matrix4)"""
        super(__graphics.Camera, self).transform(arg0)

    @override
    @overload
    def lookAt(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(com.badlogic.gdx.math.Vector3)"""
        super(__graphics.Camera, self).lookAt(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__graphics.Camera, self).unproject(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setFovModifier(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.GameCamera.setFovModifier(float)"""
        super(__GameCamera, self).setFovModifier(__float.valueOf(arg0))

    @overload
    def relative(self, arg0: 'Vec3d', arg1: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.input.GameCamera.relative(dev.ultreon.libs.commons.v0.vector.Vec3d,com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__GameCamera, self).relative(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.translate(float,float,float)"""
        super(__graphics.Camera, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def project(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'.__wrap(super(__graphics.Camera, self).project(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))) 
 
 
# CLASS: dev.ultreon.quantum.client.input.TouchscreenInput
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.input import util
except ImportError:
    util = __import_once__("pyquantum.client.input.util")

import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
try:
    from pyquantum.client.input import key
except ImportError:
    key = __import_once__("pyquantum.client.input.key")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.input.GameInput as __GameInput
__GameInput = __GameInput
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = __import_once__("pygdx.controllers")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.client.input.TouchscreenInput as __TouchscreenInput
__TouchscreenInput = __TouchscreenInput
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class TouchscreenInput(__GameInput, GameInput):
    """dev.ultreon.quantum.client.input.TouchscreenInput"""
 
    @staticmethod
    def __wrap(java_value: __TouchscreenInput) -> 'TouchscreenInput':
        return TouchscreenInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TouchscreenInput):
        """
        Dynamic initializer for TouchscreenInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.PAUSE_KEY
    PAUSE_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.PAUSE_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.HIDE_HUD_KEY
    HIDE_HUD_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.HIDE_HUD_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.THIRD_PERSON_KEY
    THIRD_PERSON_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.THIRD_PERSON_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.IM_GUI_FOCUS_KEY
    IM_GUI_FOCUS_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.IM_GUI_FOCUS_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.INSPECT_KEY
    INSPECT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.INSPECT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.SCREENSHOT_KEY
    SCREENSHOT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.SCREENSHOT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.IM_GUI_KEY
    IM_GUI_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.IM_GUI_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.CHAT_KEY
    CHAT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.CHAT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.FULL_SCREEN_KEY
    FULL_SCREEN_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.FULL_SCREEN_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.DEBUG_KEY
    DEBUG_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.DEBUG_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.INVENTORY_KEY
    INVENTORY_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.INVENTORY_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.TouchscreenInput.COMMAND_KEY
    COMMAND_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.COMMAND_KEY)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonDown(arg0))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.scrolled(float,float)"""
        return bool.__wrap(super(__TouchscreenInput, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.keyDown(int)"""
        return bool.__wrap(super(__TouchscreenInput, self).keyDown(__int.valueOf(arg0)))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.keyTyped(char)"""
        return bool.__wrap(super(__TouchscreenInput, self).keyTyped(__char.valueOf(arg0)))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2.__wrap(__GameInput.getJoystick(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'Camera'):
        """public dev.ultreon.quantum.client.input.TouchscreenInput(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.Camera)"""
        val = __TouchscreenInput(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'.__wrap(super(__GameInput, self).useItem(arg0, arg1, arg2))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonUp(arg0, __int.valueOf(arg1)))

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
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.TouchscreenInput.update(float)"""
        super(__TouchscreenInput, self).update(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool.__wrap(super(__GameInput, self).axisMoved(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonJustPressed(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__TouchscreenInput, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__TouchscreenInput, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.touchDragged(int,int,int)"""
        return bool.__wrap(super(__TouchscreenInput, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).disconnected(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def isPressingAnyButton() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.TouchscreenInput.isPressingAnyButton()"""
        return bool.__wrap(__TouchscreenInput.isPressingAnyButton())

    @staticmethod
    @overload
    def getMouseDelta() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.TouchscreenInput.getMouseDelta()"""
        return math.Vector2.__wrap(__TouchscreenInput.getMouseDelta())

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).connected(arg0)

    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool.__wrap(__GameInput.isKeyDown(__int.valueOf(arg0)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.mouseMoved(int,int)"""
        return bool.__wrap(super(__TouchscreenInput, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def setCursorCaught(arg0: bool):
        """public static void dev.ultreon.quantum.client.input.TouchscreenInput.setCursorCaught(boolean)"""
        __TouchscreenInput.setCursorCaught(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool.__wrap(__GameInput.startVibration(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__TouchscreenInput, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.TouchscreenInput.keyUp(int)"""
        return bool.__wrap(super(__TouchscreenInput, self).keyUp(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool.__wrap(__GameInput.cancelVibration())

    @override
    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool.__wrap(super(GameInput, self).isControllerConnected())

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonDown(arg0, __int.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.quantum.client.input.GameInput
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

try:
    from pyquantum.client.input import util
except ImportError:
    util = __import_once__("pyquantum.client.input.util")

from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.input.GameInput as __GameInput
__GameInput = __GameInput
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
import com.badlogic.gdx.InputProcessor as __InputProcessor
__InputProcessor = __InputProcessor
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = __import_once__("pygdx.controllers")

from builtins import int
 
class GameInput(ABC, pygdx.__InputProcessor, pygdx.InputProcessor, pygdx.__ControllerListener, controllers.ControllerListener, pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.input.GameInput"""
 
    @staticmethod
    def __wrap(java_value: __GameInput) -> 'GameInput':
        return GameInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameInput):
        """
        Dynamic initializer for GameInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @abstractmethod
    def keyTyped(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.InputProcessor.keyTyped(char)"""
        pass

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonDown(arg0))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2.__wrap(__GameInput.getJoystick(arg0))

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

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'.__wrap(super(__GameInput, self).useItem(arg0, arg1, arg2))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonUp(arg0, __int.valueOf(arg1)))

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

    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.GameInput.update(float)"""
        super(__GameInput, self).update(__float.valueOf(arg0))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.keyDown(int)"""
        return bool.__wrap(super(__GameInput, self).keyDown(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool.__wrap(super(__GameInput, self).axisMoved(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonJustPressed(arg0))

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
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).disconnected(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def touchDragged(self, arg0: int, arg1: int, arg2: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchDragged(int,int,int)"""
        pass

    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool.__wrap(super(GameInput, self).isControllerConnected())

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).connected(arg0)

    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool.__wrap(__GameInput.isKeyDown(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.keyUp(int)"""
        return bool.__wrap(super(__GameInput, self).keyUp(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool.__wrap(__GameInput.startVibration(__int.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool.__wrap(__GameInput.cancelVibration())

    @abstractmethod
    def scrolled(self, arg0: float, arg1: float):
        """public abstract boolean com.badlogic.gdx.InputProcessor.scrolled(float,float)"""
        pass

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonDown(arg0, __int.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.quantum.client.input.GyroscopeInput
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.input import util
except ImportError:
    util = __import_once__("pyquantum.client.input.util")

import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
try:
    from pyquantum.client.input import key
except ImportError:
    key = __import_once__("pyquantum.client.input.key")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.input.GameInput as __GameInput
__GameInput = __GameInput
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx import controllers
except ImportError:
    controllers = __import_once__("pygdx.controllers")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.client.input.GyroscopeInput as __GyroscopeInput
__GyroscopeInput = __GyroscopeInput
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class GyroscopeInput(__GameInput, GameInput):
    """dev.ultreon.quantum.client.input.GyroscopeInput"""
 
    @staticmethod
    def __wrap(java_value: __GyroscopeInput) -> 'GyroscopeInput':
        return GyroscopeInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GyroscopeInput):
        """
        Dynamic initializer for GyroscopeInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.SCREENSHOT_KEY
    SCREENSHOT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.SCREENSHOT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.COMMAND_KEY
    COMMAND_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.COMMAND_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.PAUSE_KEY
    PAUSE_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.PAUSE_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.FULL_SCREEN_KEY
    FULL_SCREEN_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.FULL_SCREEN_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.INVENTORY_KEY
    INVENTORY_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.INVENTORY_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.INSPECT_KEY
    INSPECT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.INSPECT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.THIRD_PERSON_KEY
    THIRD_PERSON_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.THIRD_PERSON_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.IM_GUI_FOCUS_KEY
    IM_GUI_FOCUS_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.IM_GUI_FOCUS_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.IM_GUI_KEY
    IM_GUI_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.IM_GUI_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.HIDE_HUD_KEY
    HIDE_HUD_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.HIDE_HUD_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.CHAT_KEY
    CHAT_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.CHAT_KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.GyroscopeInput.DEBUG_KEY
    DEBUG_KEY: 'key.KeyBind' = __wrap(__key.KeyBind.DEBUG_KEY)


    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__GyroscopeInput, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isControllerButtonDown(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonDown(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonDown(arg0))

    @staticmethod
    @overload
    def getJoystick(arg0: 'JoystickType') -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GameInput.getJoystick(dev.ultreon.quantum.client.input.util.JoystickType)"""
        return math.Vector2.__wrap(__GameInput.getJoystick(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.touchDragged(int,int,int)"""
        return bool.__wrap(super(__GyroscopeInput, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def useItem(self, arg0: 'Player', arg1: 'World', arg2: 'HitResult') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.client.input.GameInput.useItem(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.HitResult)"""
        return 'world.UseResult'.__wrap(super(__GameInput, self).useItem(arg0, arg1, arg2))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonUp(arg0, __int.valueOf(arg1)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.scrolled(float,float)"""
        return bool.__wrap(super(__GyroscopeInput, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

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

    @staticmethod
    @overload
    def setCursorCaught(arg0: bool):
        """public static void dev.ultreon.quantum.client.input.GyroscopeInput.setCursorCaught(boolean)"""
        __GyroscopeInput.setCursorCaught(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool.__wrap(super(__GameInput, self).axisMoved(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.keyDown(int)"""
        return bool.__wrap(super(__GyroscopeInput, self).keyDown(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def isControllerButtonJustPressed(arg0: 'ControllerButton') -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isControllerButtonJustPressed(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        return bool.__wrap(__GameInput.isControllerButtonJustPressed(arg0))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__GyroscopeInput, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def update(self, arg0: float):
        """public void dev.ultreon.quantum.client.input.GyroscopeInput.update(float)"""
        super(__GyroscopeInput, self).update(__float.valueOf(arg0))

    @staticmethod
    @overload
    def isPressingAnyButton() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GyroscopeInput.isPressingAnyButton()"""
        return bool.__wrap(__GyroscopeInput.isPressingAnyButton())

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).disconnected(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.keyTyped(char)"""
        return bool.__wrap(super(__GyroscopeInput, self).keyTyped(__char.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'Camera'):
        """public dev.ultreon.quantum.client.input.GyroscopeInput(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.Camera)"""
        val = __GyroscopeInput(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void dev.ultreon.quantum.client.input.GameInput.connected(com.badlogic.gdx.controllers.Controller)"""
        super(__GameInput, self).connected(arg0)

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.mouseMoved(int,int)"""
        return bool.__wrap(super(__GyroscopeInput, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def isKeyDown(arg0: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.isKeyDown(int)"""
        return bool.__wrap(__GameInput.isKeyDown(__int.valueOf(arg0)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__GyroscopeInput, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GyroscopeInput.keyUp(int)"""
        return bool.__wrap(super(__GyroscopeInput, self).keyUp(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def startVibration(arg0: int, arg1: float) -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.startVibration(int,float)"""
        return bool.__wrap(__GameInput.startVibration(__int.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def getMouseDelta() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 dev.ultreon.quantum.client.input.GyroscopeInput.getMouseDelta()"""
        return math.Vector2.__wrap(__GyroscopeInput.getMouseDelta())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def cancelVibration() -> bool:
        """public static boolean dev.ultreon.quantum.client.input.GameInput.cancelVibration()"""
        return bool.__wrap(__GameInput.cancelVibration())

    @override
    @overload
    def isControllerConnected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.isControllerConnected()"""
        return bool.__wrap(super(GameInput, self).isControllerConnected())

    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.client.input.GameInput.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__GameInput, self).buttonDown(arg0, __int.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.quantum.client.input.PlayerInput
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.input.PlayerInput as __PlayerInput
__PlayerInput = __PlayerInput
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PlayerInput():
    """dev.ultreon.quantum.client.input.PlayerInput"""
 
    @staticmethod
    def __wrap(java_value: __PlayerInput) -> 'PlayerInput':
        return PlayerInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerInput):
        """
        Dynamic initializer for PlayerInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.PlayerInput.isWalking()"""
        return bool.__wrap(super(PlayerInput, self).isWalking())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def tick(self, arg0: 'Player', arg1: float):
        """public void dev.ultreon.quantum.client.input.PlayerInput.tick(dev.ultreon.quantum.entity.player.Player,float)"""
        super(__PlayerInput, self).tick(arg0, __float.valueOf(arg1))

    @overload
    def getVelocity(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.input.PlayerInput.getVelocity()"""
        return 'math.Vector3'.__wrap(super(PlayerInput, self).getVelocity())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getVel(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.client.input.PlayerInput.getVel()"""
        return 'vector.Vec3d'.__wrap(super(PlayerInput, self).getVel())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.input.PlayerInput(dev.ultreon.quantum.client.QuantumClient)"""
        val = __PlayerInput(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))