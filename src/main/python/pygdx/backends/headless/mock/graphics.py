from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.GL31 as _GL31
_GL31 = _GL31
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.GL30 as _GL30
_GL30 = _GL30
from builtins import type
import com.badlogic.gdx.graphics.Cursor as _Cursor
_Cursor = _Cursor
import com.badlogic.gdx.Graphics as _Graphics_GraphicsType
_GraphicsType = _Graphics_GraphicsType.GraphicsType
import com.badlogic.gdx.graphics.GL32 as _GL32
_GL32 = _GL32
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.Graphics as _Graphics_Monitor
_Monitor = _Graphics_Monitor.Monitor
from builtins import bool
import com.badlogic.gdx.graphics.GL20 as _GL20
_GL20 = _GL20
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import com.badlogic.gdx.Graphics as _Graphics_DisplayMode
_DisplayMode = _Graphics_DisplayMode.DisplayMode
from builtins import str
import com.badlogic.gdx.AbstractGraphics as _AbstractGraphics
_AbstractGraphics = _AbstractGraphics
from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics as _MockGraphics
_MockGraphics = _MockGraphics
from builtins import float
import com.badlogic.gdx.graphics.glutils.GLVersion as _GLVersion
_GLVersion = _GLVersion
import java.lang.String as _String
_String = _String
from typing import List
import com.badlogic.gdx.Graphics as _Graphics_BufferFormat
_BufferFormat = _Graphics_BufferFormat.BufferFormat
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockGraphics():
    """com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics"""
 
    @staticmethod
    def _wrap(java_value: _MockGraphics) -> 'MockGraphics':
        return MockGraphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockGraphics):
        """
        Dynamic initializer for MockGraphics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockGraphics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockGraphics__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isFullscreen(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isFullscreen()"""
        return bool._wrap(super(MockGraphics, self).isFullscreen())

    @override
    @overload
    def supportsDisplayModeChange(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.supportsDisplayModeChange()"""
        return bool._wrap(super(MockGraphics, self).supportsDisplayModeChange())

    @override
    @overload
    def setGL20(self, arg0: 'GL20'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL20(com.badlogic.gdx.graphics.GL20)"""
        super(_MockGraphics, self).setGL20(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setCursor(self, arg0: 'Cursor'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setCursor(com.badlogic.gdx.graphics.Cursor)"""
        super(_MockGraphics, self).setCursor(arg0)

    @override
    @overload
    def getGL20(self) -> 'graphics.GL20':
        """public com.badlogic.gdx.graphics.GL20 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL20()"""
        return 'graphics.GL20'._wrap(super(MockGraphics, self).getGL20())

    @override
    @overload
    def getGL31(self) -> 'graphics.GL31':
        """public com.badlogic.gdx.graphics.GL31 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL31()"""
        return 'graphics.GL31'._wrap(super(MockGraphics, self).getGL31())

    @override
    @overload
    def getSafeInsetBottom(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetBottom()"""
        return int._wrap(super(MockGraphics, self).getSafeInsetBottom())

    @override
    @overload
    def getBackBufferWidth(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBackBufferWidth()"""
        return int._wrap(super(MockGraphics, self).getBackBufferWidth())

    @override
    @overload
    def getSafeInsetRight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetRight()"""
        return int._wrap(super(MockGraphics, self).getSafeInsetRight())

    @override
    @overload
    def getBufferFormat(self) -> 'pygdx.Graphics$BufferFormat':
        """public com.badlogic.gdx.Graphics$BufferFormat com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBufferFormat()"""
        return 'pygdx.Graphics$BufferFormat'._wrap(super(MockGraphics, self).getBufferFormat())

    @override
    @overload
    def getDeltaTime(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDeltaTime()"""
        return float._wrap(super(MockGraphics, self).getDeltaTime())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getFramesPerSecond(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getFramesPerSecond()"""
        return int._wrap(super(MockGraphics, self).getFramesPerSecond())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setTitle(java.lang.String)"""
        super(_MockGraphics, self).setTitle(arg0)

    @override
    @overload
    def getPpcY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpcY()"""
        return float._wrap(super(MockGraphics, self).getPpcY())

    @override
    @overload
    def isGL31Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL31Available()"""
        return bool._wrap(super(MockGraphics, self).isGL31Available())

    @override
    @overload
    def setGL32(self, arg0: 'GL32'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL32(com.badlogic.gdx.graphics.GL32)"""
        super(_MockGraphics, self).setGL32(arg0)

    @override
    @overload
    def getGL30(self) -> 'graphics.GL30':
        """public com.badlogic.gdx.graphics.GL30 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL30()"""
        return 'graphics.GL30'._wrap(super(MockGraphics, self).getGL30())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setFullscreenMode(self, arg0: 'DisplayMode') -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setFullscreenMode(com.badlogic.gdx.Graphics$DisplayMode)"""
        return bool._wrap(super(_MockGraphics, self).setFullscreenMode(arg0))

    @override
    @overload
    def getBackBufferHeight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBackBufferHeight()"""
        return int._wrap(super(MockGraphics, self).getBackBufferHeight())

    @override
    @overload
    def getPrimaryMonitor(self) -> 'pygdx.Graphics$Monitor':
        """public com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPrimaryMonitor()"""
        return 'pygdx.Graphics$Monitor'._wrap(super(MockGraphics, self).getPrimaryMonitor())

    @override
    @overload
    def getBackBufferScale(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getBackBufferScale()"""
        return float._wrap(super(pygdx.AbstractGraphics, self).getBackBufferScale())

    @override
    @overload
    def getPpiY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpiY()"""
        return float._wrap(super(MockGraphics, self).getPpiY())

    @overload
    def getDisplayModes(self, arg0: 'Monitor') -> List['pygdx.Graphics$DisplayMode']:
        """public com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayModes(com.badlogic.gdx.Graphics$Monitor)"""
        return List['pygdx.Graphics$DisplayMode']._wrap(super(_MockGraphics, self).getDisplayModes(arg0))

    @override
    @overload
    def setSystemCursor(self, arg0: 'SystemCursor'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setSystemCursor(com.badlogic.gdx.graphics.Cursor$SystemCursor)"""
        super(_MockGraphics, self).setSystemCursor(arg0)

    @override
    @overload
    def requestRendering(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.requestRendering()"""
        super(MockGraphics, self).requestRendering()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics()"""
        val = _MockGraphics()
        self.__wrapper = val

    @overload
    def setWindowedMode(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setWindowedMode(int,int)"""
        return bool._wrap(super(_MockGraphics, self).setWindowedMode(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getDisplayMode(self) -> 'pygdx.Graphics$DisplayMode':
        """public com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayMode()"""
        return 'pygdx.Graphics$DisplayMode'._wrap(super(MockGraphics, self).getDisplayMode())

    @override
    @overload
    def setVSync(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setVSync(boolean)"""
        super(_MockGraphics, self).setVSync(_boolean.valueOf(arg0))

    @override
    @overload
    def isGL30Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL30Available()"""
        return bool._wrap(super(MockGraphics, self).isGL30Available())

    @override
    @overload
    def getDisplayModes(self) -> List['pygdx.Graphics$DisplayMode']:
        """public com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayModes()"""
        return List['pygdx.Graphics$DisplayMode']._wrap(super(MockGraphics, self).getDisplayModes())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setGL31(self, arg0: 'GL31'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL31(com.badlogic.gdx.graphics.GL31)"""
        super(_MockGraphics, self).setGL31(arg0)

    @overload
    def getDisplayMode(self, arg0: 'Monitor') -> 'pygdx.Graphics$DisplayMode':
        """public com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayMode(com.badlogic.gdx.Graphics$Monitor)"""
        return 'pygdx.Graphics$DisplayMode'._wrap(super(_MockGraphics, self).getDisplayMode(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isContinuousRendering(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isContinuousRendering()"""
        return bool._wrap(super(MockGraphics, self).isContinuousRendering())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getWidth()"""
        return int._wrap(super(MockGraphics, self).getWidth())

    @override
    @overload
    def getSafeInsetLeft(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetLeft()"""
        return int._wrap(super(MockGraphics, self).getSafeInsetLeft())

    @overload
    def newCursor(self, arg0: 'Pixmap', arg1: int, arg2: int) -> 'graphics.Cursor':
        """public com.badlogic.gdx.graphics.Cursor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.newCursor(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        return 'graphics.Cursor'._wrap(super(_MockGraphics, self).newCursor(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def incrementFrameId(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.incrementFrameId()"""
        super(MockGraphics, self).incrementFrameId()

    @override
    @overload
    def isGL32Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL32Available()"""
        return bool._wrap(super(MockGraphics, self).isGL32Available())

    @override
    @overload
    def getPpcX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpcX()"""
        return float._wrap(super(MockGraphics, self).getPpcX())

    @override
    @overload
    def getMonitors(self) -> List['pygdx.Graphics$Monitor']:
        """public com.badlogic.gdx.Graphics$Monitor[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getMonitors()"""
        return List['pygdx.Graphics$Monitor']._wrap(super(MockGraphics, self).getMonitors())

    @override
    @overload
    def setGL30(self, arg0: 'GL30'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL30(com.badlogic.gdx.graphics.GL30)"""
        super(_MockGraphics, self).setGL30(arg0)

    @override
    @overload
    def getSafeInsetTop(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetTop()"""
        return int._wrap(super(MockGraphics, self).getSafeInsetTop())

    @override
    @overload
    def getGLVersion(self) -> 'glutils.GLVersion':
        """public com.badlogic.gdx.graphics.glutils.GLVersion com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGLVersion()"""
        return 'glutils.GLVersion'._wrap(super(MockGraphics, self).getGLVersion())

    @overload
    def supportsExtension(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.supportsExtension(java.lang.String)"""
        return bool._wrap(super(_MockGraphics, self).supportsExtension(arg0))

    @override
    @overload
    def getDensity(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getDensity()"""
        return float._wrap(super(pygdx.AbstractGraphics, self).getDensity())

    @overload
    def getTargetRenderInterval(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getTargetRenderInterval()"""
        return int._wrap(super(MockGraphics, self).getTargetRenderInterval())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setForegroundFPS(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setForegroundFPS(int)"""
        super(_MockGraphics, self).setForegroundFPS(_int.valueOf(arg0))

    @override
    @overload
    def getFrameId(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getFrameId()"""
        return int._wrap(super(MockGraphics, self).getFrameId())

    @override
    @overload
    def getType(self) -> 'pygdx.Graphics$GraphicsType':
        """public com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getType()"""
        return 'pygdx.Graphics$GraphicsType'._wrap(super(MockGraphics, self).getType())

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setResizable(boolean)"""
        super(_MockGraphics, self).setResizable(_boolean.valueOf(arg0))

    @override
    @overload
    def getMonitor(self) -> 'pygdx.Graphics$Monitor':
        """public com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getMonitor()"""
        return 'pygdx.Graphics$Monitor'._wrap(super(MockGraphics, self).getMonitor())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getHeight()"""
        return int._wrap(super(MockGraphics, self).getHeight())

    @overload
    def updateTime(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.updateTime()"""
        super(MockGraphics, self).updateTime()

    @override
    @overload
    def setUndecorated(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setUndecorated(boolean)"""
        super(_MockGraphics, self).setUndecorated(_boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setContinuousRendering(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setContinuousRendering(boolean)"""
        super(_MockGraphics, self).setContinuousRendering(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics()"""
        val = _MockGraphics()
        self.__wrapper = val

    @override
    @overload
    def getPpiX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpiX()"""
        return float._wrap(super(MockGraphics, self).getPpiX())

    @override
    @overload
    def getGL32(self) -> 'graphics.GL32':
        """public com.badlogic.gdx.graphics.GL32 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL32()"""
        return 'graphics.GL32'._wrap(super(MockGraphics, self).getGL32())

    @override
    @overload
    def getRawDeltaTime(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getRawDeltaTime()"""
        return float._wrap(super(pygdx.AbstractGraphics, self).getRawDeltaTime())

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.GL31 as _GL31
_GL31 = _GL31
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.GL30 as _GL30
_GL30 = _GL30
from builtins import type
import com.badlogic.gdx.graphics.Cursor as _Cursor
_Cursor = _Cursor
import com.badlogic.gdx.Graphics as _Graphics_GraphicsType
_GraphicsType = _Graphics_GraphicsType.GraphicsType
import com.badlogic.gdx.graphics.GL32 as _GL32
_GL32 = _GL32
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.Graphics as _Graphics_Monitor
_Monitor = _Graphics_Monitor.Monitor
from builtins import bool
import com.badlogic.gdx.graphics.GL20 as _GL20
_GL20 = _GL20
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import com.badlogic.gdx.Graphics as _Graphics_DisplayMode
_DisplayMode = _Graphics_DisplayMode.DisplayMode
from builtins import str
import com.badlogic.gdx.AbstractGraphics as _AbstractGraphics
_AbstractGraphics = _AbstractGraphics
from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics as _MockGraphics
_MockGraphics = _MockGraphics
from builtins import float
import com.badlogic.gdx.graphics.glutils.GLVersion as _GLVersion
_GLVersion = _GLVersion
import java.lang.String as _String
_String = _String
from typing import List
import com.badlogic.gdx.Graphics as _Graphics_BufferFormat
_BufferFormat = _Graphics_BufferFormat.BufferFormat
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockGraphics():
    """com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics"""
 
    @staticmethod
    def _wrap(java_value: _MockGraphics) -> 'MockGraphics':
        return MockGraphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockGraphics):
        """
        Dynamic initializer for MockGraphics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockGraphics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockGraphics__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isFullscreen(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isFullscreen()"""
        return bool._wrap(super(MockGraphics, self).isFullscreen())

    @override
    @overload
    def supportsDisplayModeChange(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.supportsDisplayModeChange()"""
        return bool._wrap(super(MockGraphics, self).supportsDisplayModeChange())

    @override
    @overload
    def setGL20(self, arg0: 'GL20'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL20(com.badlogic.gdx.graphics.GL20)"""
        super(_MockGraphics, self).setGL20(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setCursor(self, arg0: 'Cursor'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setCursor(com.badlogic.gdx.graphics.Cursor)"""
        super(_MockGraphics, self).setCursor(arg0)

    @override
    @overload
    def getGL20(self) -> 'graphics.GL20':
        """public com.badlogic.gdx.graphics.GL20 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL20()"""
        return 'graphics.GL20'._wrap(super(MockGraphics, self).getGL20())

    @override
    @overload
    def getGL31(self) -> 'graphics.GL31':
        """public com.badlogic.gdx.graphics.GL31 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL31()"""
        return 'graphics.GL31'._wrap(super(MockGraphics, self).getGL31())

    @override
    @overload
    def getSafeInsetBottom(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetBottom()"""
        return int._wrap(super(MockGraphics, self).getSafeInsetBottom())

    @override
    @overload
    def getBackBufferWidth(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBackBufferWidth()"""
        return int._wrap(super(MockGraphics, self).getBackBufferWidth())

    @override
    @overload
    def getSafeInsetRight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetRight()"""
        return int._wrap(super(MockGraphics, self).getSafeInsetRight())

    @override
    @overload
    def getBufferFormat(self) -> 'pygdx.Graphics$BufferFormat':
        """public com.badlogic.gdx.Graphics$BufferFormat com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBufferFormat()"""
        return 'pygdx.Graphics$BufferFormat'._wrap(super(MockGraphics, self).getBufferFormat())

    @override
    @overload
    def getDeltaTime(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDeltaTime()"""
        return float._wrap(super(MockGraphics, self).getDeltaTime())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getFramesPerSecond(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getFramesPerSecond()"""
        return int._wrap(super(MockGraphics, self).getFramesPerSecond())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setTitle(java.lang.String)"""
        super(_MockGraphics, self).setTitle(arg0)

    @override
    @overload
    def getPpcY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpcY()"""
        return float._wrap(super(MockGraphics, self).getPpcY())

    @override
    @overload
    def isGL31Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL31Available()"""
        return bool._wrap(super(MockGraphics, self).isGL31Available())

    @override
    @overload
    def setGL32(self, arg0: 'GL32'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL32(com.badlogic.gdx.graphics.GL32)"""
        super(_MockGraphics, self).setGL32(arg0)

    @override
    @overload
    def getGL30(self) -> 'graphics.GL30':
        """public com.badlogic.gdx.graphics.GL30 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL30()"""
        return 'graphics.GL30'._wrap(super(MockGraphics, self).getGL30())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setFullscreenMode(self, arg0: 'DisplayMode') -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setFullscreenMode(com.badlogic.gdx.Graphics$DisplayMode)"""
        return bool._wrap(super(_MockGraphics, self).setFullscreenMode(arg0))

    @override
    @overload
    def getBackBufferHeight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBackBufferHeight()"""
        return int._wrap(super(MockGraphics, self).getBackBufferHeight())

    @override
    @overload
    def getPrimaryMonitor(self) -> 'pygdx.Graphics$Monitor':
        """public com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPrimaryMonitor()"""
        return 'pygdx.Graphics$Monitor'._wrap(super(MockGraphics, self).getPrimaryMonitor())

    @override
    @overload
    def getBackBufferScale(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getBackBufferScale()"""
        return float._wrap(super(pygdx.AbstractGraphics, self).getBackBufferScale())

    @override
    @overload
    def getPpiY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpiY()"""
        return float._wrap(super(MockGraphics, self).getPpiY())

    @overload
    def getDisplayModes(self, arg0: 'Monitor') -> List['pygdx.Graphics$DisplayMode']:
        """public com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayModes(com.badlogic.gdx.Graphics$Monitor)"""
        return List['pygdx.Graphics$DisplayMode']._wrap(super(_MockGraphics, self).getDisplayModes(arg0))

    @override
    @overload
    def setSystemCursor(self, arg0: 'SystemCursor'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setSystemCursor(com.badlogic.gdx.graphics.Cursor$SystemCursor)"""
        super(_MockGraphics, self).setSystemCursor(arg0)

    @override
    @overload
    def requestRendering(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.requestRendering()"""
        super(MockGraphics, self).requestRendering()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics()"""
        val = _MockGraphics()
        self.__wrapper = val

    @overload
    def setWindowedMode(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setWindowedMode(int,int)"""
        return bool._wrap(super(_MockGraphics, self).setWindowedMode(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getDisplayMode(self) -> 'pygdx.Graphics$DisplayMode':
        """public com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayMode()"""
        return 'pygdx.Graphics$DisplayMode'._wrap(super(MockGraphics, self).getDisplayMode())

    @override
    @overload
    def setVSync(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setVSync(boolean)"""
        super(_MockGraphics, self).setVSync(_boolean.valueOf(arg0))

    @override
    @overload
    def isGL30Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL30Available()"""
        return bool._wrap(super(MockGraphics, self).isGL30Available())

    @override
    @overload
    def getDisplayModes(self) -> List['pygdx.Graphics$DisplayMode']:
        """public com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayModes()"""
        return List['pygdx.Graphics$DisplayMode']._wrap(super(MockGraphics, self).getDisplayModes())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setGL31(self, arg0: 'GL31'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL31(com.badlogic.gdx.graphics.GL31)"""
        super(_MockGraphics, self).setGL31(arg0)

    @overload
    def getDisplayMode(self, arg0: 'Monitor') -> 'pygdx.Graphics$DisplayMode':
        """public com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayMode(com.badlogic.gdx.Graphics$Monitor)"""
        return 'pygdx.Graphics$DisplayMode'._wrap(super(_MockGraphics, self).getDisplayMode(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isContinuousRendering(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isContinuousRendering()"""
        return bool._wrap(super(MockGraphics, self).isContinuousRendering())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getWidth()"""
        return int._wrap(super(MockGraphics, self).getWidth())

    @override
    @overload
    def getSafeInsetLeft(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetLeft()"""
        return int._wrap(super(MockGraphics, self).getSafeInsetLeft())

    @overload
    def newCursor(self, arg0: 'Pixmap', arg1: int, arg2: int) -> 'graphics.Cursor':
        """public com.badlogic.gdx.graphics.Cursor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.newCursor(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        return 'graphics.Cursor'._wrap(super(_MockGraphics, self).newCursor(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def incrementFrameId(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.incrementFrameId()"""
        super(MockGraphics, self).incrementFrameId()

    @override
    @overload
    def isGL32Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL32Available()"""
        return bool._wrap(super(MockGraphics, self).isGL32Available())

    @override
    @overload
    def getPpcX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpcX()"""
        return float._wrap(super(MockGraphics, self).getPpcX())

    @override
    @overload
    def getMonitors(self) -> List['pygdx.Graphics$Monitor']:
        """public com.badlogic.gdx.Graphics$Monitor[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getMonitors()"""
        return List['pygdx.Graphics$Monitor']._wrap(super(MockGraphics, self).getMonitors())

    @override
    @overload
    def setGL30(self, arg0: 'GL30'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL30(com.badlogic.gdx.graphics.GL30)"""
        super(_MockGraphics, self).setGL30(arg0)

    @override
    @overload
    def getSafeInsetTop(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetTop()"""
        return int._wrap(super(MockGraphics, self).getSafeInsetTop())

    @override
    @overload
    def getGLVersion(self) -> 'glutils.GLVersion':
        """public com.badlogic.gdx.graphics.glutils.GLVersion com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGLVersion()"""
        return 'glutils.GLVersion'._wrap(super(MockGraphics, self).getGLVersion())

    @overload
    def supportsExtension(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.supportsExtension(java.lang.String)"""
        return bool._wrap(super(_MockGraphics, self).supportsExtension(arg0))

    @override
    @overload
    def getDensity(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getDensity()"""
        return float._wrap(super(pygdx.AbstractGraphics, self).getDensity())

    @overload
    def getTargetRenderInterval(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getTargetRenderInterval()"""
        return int._wrap(super(MockGraphics, self).getTargetRenderInterval())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setForegroundFPS(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setForegroundFPS(int)"""
        super(_MockGraphics, self).setForegroundFPS(_int.valueOf(arg0))

    @override
    @overload
    def getFrameId(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getFrameId()"""
        return int._wrap(super(MockGraphics, self).getFrameId())

    @override
    @overload
    def getType(self) -> 'pygdx.Graphics$GraphicsType':
        """public com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getType()"""
        return 'pygdx.Graphics$GraphicsType'._wrap(super(MockGraphics, self).getType())

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setResizable(boolean)"""
        super(_MockGraphics, self).setResizable(_boolean.valueOf(arg0))

    @override
    @overload
    def getMonitor(self) -> 'pygdx.Graphics$Monitor':
        """public com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getMonitor()"""
        return 'pygdx.Graphics$Monitor'._wrap(super(MockGraphics, self).getMonitor())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getHeight()"""
        return int._wrap(super(MockGraphics, self).getHeight())

    @overload
    def updateTime(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.updateTime()"""
        super(MockGraphics, self).updateTime()

    @override
    @overload
    def setUndecorated(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setUndecorated(boolean)"""
        super(_MockGraphics, self).setUndecorated(_boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setContinuousRendering(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setContinuousRendering(boolean)"""
        super(_MockGraphics, self).setContinuousRendering(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics()"""
        val = _MockGraphics()
        self.__wrapper = val

    @override
    @overload
    def getPpiX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpiX()"""
        return float._wrap(super(MockGraphics, self).getPpiX())

    @override
    @overload
    def getGL32(self) -> 'graphics.GL32':
        """public com.badlogic.gdx.graphics.GL32 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL32()"""
        return 'graphics.GL32'._wrap(super(MockGraphics, self).getGL32())

    @override
    @overload
    def getRawDeltaTime(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getRawDeltaTime()"""
        return float._wrap(super(pygdx.AbstractGraphics, self).getRawDeltaTime())

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics