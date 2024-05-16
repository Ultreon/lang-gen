from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.GL30 as __GL30
__GL30 = __GL30
import com.badlogic.gdx.Graphics as __Graphics_GraphicsType
__GraphicsType = __Graphics_GraphicsType.GraphicsType
import com.badlogic.gdx.graphics.GL32 as __GL32
__GL32 = __GL32
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLVersion as __GLVersion
__GLVersion = __GLVersion
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.badlogic.gdx.Graphics as __Graphics_DisplayMode
__DisplayMode = __Graphics_DisplayMode.DisplayMode
from builtins import bool
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import com.badlogic.gdx.graphics.Cursor as __Cursor
__Cursor = __Cursor
from builtins import str
import com.badlogic.gdx.graphics.GL31 as __GL31
__GL31 = __GL31
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics as __MockGraphics
__MockGraphics = __MockGraphics
from builtins import float
from typing import List
import com.badlogic.gdx.Graphics as __Graphics_Monitor
__Monitor = __Graphics_Monitor.Monitor
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.GL20 as __GL20
__GL20 = __GL20
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.AbstractGraphics as __AbstractGraphics
__AbstractGraphics = __AbstractGraphics
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.Graphics as __Graphics_BufferFormat
__BufferFormat = __Graphics_BufferFormat.BufferFormat
from builtins import int
 
class MockGraphics():
    """com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics"""
 
    @staticmethod
    def __wrap(java_value: __MockGraphics) -> 'MockGraphics':
        return MockGraphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockGraphics):
        """
        Dynamic initializer for MockGraphics.
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
    def isFullscreen(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isFullscreen()"""
        return bool.__wrap(super(MockGraphics, self).isFullscreen())

    @override
    @overload
    def getType(self) -> 'pygdx.Graphics$GraphicsType':
        """public com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getType()"""
        return 'pygdx.Graphics$GraphicsType'.__wrap(super(MockGraphics, self).getType())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getHeight()"""
        return int.__wrap(super(MockGraphics, self).getHeight())

    @override
    @overload
    def setUndecorated(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setUndecorated(boolean)"""
        super(__MockGraphics, self).setUndecorated(__boolean.valueOf(arg0))

    @override
    @overload
    def getRawDeltaTime(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getRawDeltaTime()"""
        return float.__wrap(super(pygdx.AbstractGraphics, self).getRawDeltaTime())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDisplayModes(self, arg0: 'Monitor') -> List['pygdx.Graphics$DisplayMode']:
        """public com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayModes(com.badlogic.gdx.Graphics$Monitor)"""
        return List['pygdx.Graphics$DisplayMode'].__wrap(super(__MockGraphics, self).getDisplayModes(arg0))

    @override
    @overload
    def getPpcX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpcX()"""
        return float.__wrap(super(MockGraphics, self).getPpcX())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getWidth()"""
        return int.__wrap(super(MockGraphics, self).getWidth())

    @override
    @overload
    def setSystemCursor(self, arg0: 'SystemCursor'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setSystemCursor(com.badlogic.gdx.graphics.Cursor$SystemCursor)"""
        super(__MockGraphics, self).setSystemCursor(arg0)

    @override
    @overload
    def getBackBufferHeight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBackBufferHeight()"""
        return int.__wrap(super(MockGraphics, self).getBackBufferHeight())

    @override
    @overload
    def getSafeInsetBottom(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetBottom()"""
        return int.__wrap(super(MockGraphics, self).getSafeInsetBottom())

    @override
    @overload
    def isGL32Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL32Available()"""
        return bool.__wrap(super(MockGraphics, self).isGL32Available())

    @override
    @overload
    def setGL20(self, arg0: 'GL20'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL20(com.badlogic.gdx.graphics.GL20)"""
        super(__MockGraphics, self).setGL20(arg0)

    @override
    @overload
    def setGL30(self, arg0: 'GL30'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL30(com.badlogic.gdx.graphics.GL30)"""
        super(__MockGraphics, self).setGL30(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setGL31(self, arg0: 'GL31'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL31(com.badlogic.gdx.graphics.GL31)"""
        super(__MockGraphics, self).setGL31(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics()"""
        val = __MockGraphics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setResizable(boolean)"""
        super(__MockGraphics, self).setResizable(__boolean.valueOf(arg0))

    @override
    @overload
    def getGL31(self) -> 'graphics.GL31':
        """public com.badlogic.gdx.graphics.GL31 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL31()"""
        return 'graphics.GL31'.__wrap(super(MockGraphics, self).getGL31())

    @override
    @overload
    def isGL31Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL31Available()"""
        return bool.__wrap(super(MockGraphics, self).isGL31Available())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getGL20(self) -> 'graphics.GL20':
        """public com.badlogic.gdx.graphics.GL20 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL20()"""
        return 'graphics.GL20'.__wrap(super(MockGraphics, self).getGL20())

    @override
    @overload
    def isContinuousRendering(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isContinuousRendering()"""
        return bool.__wrap(super(MockGraphics, self).isContinuousRendering())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getSafeInsetTop(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetTop()"""
        return int.__wrap(super(MockGraphics, self).getSafeInsetTop())

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setTitle(java.lang.String)"""
        super(__MockGraphics, self).setTitle(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics()"""
        val = __MockGraphics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def supportsExtension(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.supportsExtension(java.lang.String)"""
        return bool.__wrap(super(__MockGraphics, self).supportsExtension(arg0))

    @override
    @overload
    def getDensity(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getDensity()"""
        return float.__wrap(super(pygdx.AbstractGraphics, self).getDensity())

    @overload
    def setWindowedMode(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setWindowedMode(int,int)"""
        return bool.__wrap(super(__MockGraphics, self).setWindowedMode(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setCursor(self, arg0: 'Cursor'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setCursor(com.badlogic.gdx.graphics.Cursor)"""
        super(__MockGraphics, self).setCursor(arg0)

    @override
    @overload
    def getBufferFormat(self) -> 'pygdx.Graphics$BufferFormat':
        """public com.badlogic.gdx.Graphics$BufferFormat com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBufferFormat()"""
        return 'pygdx.Graphics$BufferFormat'.__wrap(super(MockGraphics, self).getBufferFormat())

    @override
    @overload
    def requestRendering(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.requestRendering()"""
        super(MockGraphics, self).requestRendering()

    @override
    @overload
    def setGL32(self, arg0: 'GL32'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL32(com.badlogic.gdx.graphics.GL32)"""
        super(__MockGraphics, self).setGL32(arg0)

    @override
    @overload
    def setVSync(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setVSync(boolean)"""
        super(__MockGraphics, self).setVSync(__boolean.valueOf(arg0))

    @override
    @overload
    def getGL32(self) -> 'graphics.GL32':
        """public com.badlogic.gdx.graphics.GL32 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL32()"""
        return 'graphics.GL32'.__wrap(super(MockGraphics, self).getGL32())

    @override
    @overload
    def getSafeInsetLeft(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetLeft()"""
        return int.__wrap(super(MockGraphics, self).getSafeInsetLeft())

    @override
    @overload
    def supportsDisplayModeChange(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.supportsDisplayModeChange()"""
        return bool.__wrap(super(MockGraphics, self).supportsDisplayModeChange())

    @override
    @overload
    def getDisplayMode(self) -> 'pygdx.Graphics$DisplayMode':
        """public com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayMode()"""
        return 'pygdx.Graphics$DisplayMode'.__wrap(super(MockGraphics, self).getDisplayMode())

    @override
    @overload
    def getPrimaryMonitor(self) -> 'pygdx.Graphics$Monitor':
        """public com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPrimaryMonitor()"""
        return 'pygdx.Graphics$Monitor'.__wrap(super(MockGraphics, self).getPrimaryMonitor())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPpiX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpiX()"""
        return float.__wrap(super(MockGraphics, self).getPpiX())

    @override
    @overload
    def getMonitor(self) -> 'pygdx.Graphics$Monitor':
        """public com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getMonitor()"""
        return 'pygdx.Graphics$Monitor'.__wrap(super(MockGraphics, self).getMonitor())

    @override
    @overload
    def getDisplayModes(self) -> List['pygdx.Graphics$DisplayMode']:
        """public com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayModes()"""
        return List['pygdx.Graphics$DisplayMode'].__wrap(super(MockGraphics, self).getDisplayModes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def incrementFrameId(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.incrementFrameId()"""
        super(MockGraphics, self).incrementFrameId()

    @overload
    def setFullscreenMode(self, arg0: 'DisplayMode') -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setFullscreenMode(com.badlogic.gdx.Graphics$DisplayMode)"""
        return bool.__wrap(super(__MockGraphics, self).setFullscreenMode(arg0))

    @override
    @overload
    def getSafeInsetRight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetRight()"""
        return int.__wrap(super(MockGraphics, self).getSafeInsetRight())

    @override
    @overload
    def getPpcY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpcY()"""
        return float.__wrap(super(MockGraphics, self).getPpcY())

    @override
    @overload
    def getDeltaTime(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDeltaTime()"""
        return float.__wrap(super(MockGraphics, self).getDeltaTime())

    @overload
    def newCursor(self, arg0: 'Pixmap', arg1: int, arg2: int) -> 'graphics.Cursor':
        """public com.badlogic.gdx.graphics.Cursor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.newCursor(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        return 'graphics.Cursor'.__wrap(super(__MockGraphics, self).newCursor(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getBackBufferScale(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getBackBufferScale()"""
        return float.__wrap(super(pygdx.AbstractGraphics, self).getBackBufferScale())

    @override
    @overload
    def getFrameId(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getFrameId()"""
        return int.__wrap(super(MockGraphics, self).getFrameId())

    @overload
    def getDisplayMode(self, arg0: 'Monitor') -> 'pygdx.Graphics$DisplayMode':
        """public com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayMode(com.badlogic.gdx.Graphics$Monitor)"""
        return 'pygdx.Graphics$DisplayMode'.__wrap(super(__MockGraphics, self).getDisplayMode(arg0))

    @override
    @overload
    def setForegroundFPS(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setForegroundFPS(int)"""
        super(__MockGraphics, self).setForegroundFPS(__int.valueOf(arg0))

    @override
    @overload
    def getGL30(self) -> 'graphics.GL30':
        """public com.badlogic.gdx.graphics.GL30 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL30()"""
        return 'graphics.GL30'.__wrap(super(MockGraphics, self).getGL30())

    @override
    @overload
    def getFramesPerSecond(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getFramesPerSecond()"""
        return int.__wrap(super(MockGraphics, self).getFramesPerSecond())

    @override
    @overload
    def getGLVersion(self) -> 'glutils.GLVersion':
        """public com.badlogic.gdx.graphics.glutils.GLVersion com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGLVersion()"""
        return 'glutils.GLVersion'.__wrap(super(MockGraphics, self).getGLVersion())

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
    def setContinuousRendering(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setContinuousRendering(boolean)"""
        super(__MockGraphics, self).setContinuousRendering(__boolean.valueOf(arg0))

    @override
    @overload
    def isGL30Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL30Available()"""
        return bool.__wrap(super(MockGraphics, self).isGL30Available())

    @overload
    def updateTime(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.updateTime()"""
        super(MockGraphics, self).updateTime()

    @override
    @overload
    def getBackBufferWidth(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBackBufferWidth()"""
        return int.__wrap(super(MockGraphics, self).getBackBufferWidth())

    @override
    @overload
    def getPpiY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpiY()"""
        return float.__wrap(super(MockGraphics, self).getPpiY())

    @override
    @overload
    def getMonitors(self) -> List['pygdx.Graphics$Monitor']:
        """public com.badlogic.gdx.Graphics$Monitor[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getMonitors()"""
        return List['pygdx.Graphics$Monitor'].__wrap(super(MockGraphics, self).getMonitors())

    @overload
    def getTargetRenderInterval(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getTargetRenderInterval()"""
        return int.__wrap(super(MockGraphics, self).getTargetRenderInterval())

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.GL30 as __GL30
__GL30 = __GL30
import com.badlogic.gdx.Graphics as __Graphics_GraphicsType
__GraphicsType = __Graphics_GraphicsType.GraphicsType
import com.badlogic.gdx.graphics.GL32 as __GL32
__GL32 = __GL32
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLVersion as __GLVersion
__GLVersion = __GLVersion
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.badlogic.gdx.Graphics as __Graphics_DisplayMode
__DisplayMode = __Graphics_DisplayMode.DisplayMode
from builtins import bool
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import com.badlogic.gdx.graphics.Cursor as __Cursor
__Cursor = __Cursor
from builtins import str
import com.badlogic.gdx.graphics.GL31 as __GL31
__GL31 = __GL31
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics as __MockGraphics
__MockGraphics = __MockGraphics
from builtins import float
from typing import List
import com.badlogic.gdx.Graphics as __Graphics_Monitor
__Monitor = __Graphics_Monitor.Monitor
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.GL20 as __GL20
__GL20 = __GL20
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.AbstractGraphics as __AbstractGraphics
__AbstractGraphics = __AbstractGraphics
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.Graphics as __Graphics_BufferFormat
__BufferFormat = __Graphics_BufferFormat.BufferFormat
from builtins import int
 
class MockGraphics():
    """com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics"""
 
    @staticmethod
    def __wrap(java_value: __MockGraphics) -> 'MockGraphics':
        return MockGraphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockGraphics):
        """
        Dynamic initializer for MockGraphics.
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
    def isFullscreen(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isFullscreen()"""
        return bool.__wrap(super(MockGraphics, self).isFullscreen())

    @override
    @overload
    def getType(self) -> 'pygdx.Graphics$GraphicsType':
        """public com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getType()"""
        return 'pygdx.Graphics$GraphicsType'.__wrap(super(MockGraphics, self).getType())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getHeight()"""
        return int.__wrap(super(MockGraphics, self).getHeight())

    @override
    @overload
    def setUndecorated(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setUndecorated(boolean)"""
        super(__MockGraphics, self).setUndecorated(__boolean.valueOf(arg0))

    @override
    @overload
    def getRawDeltaTime(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getRawDeltaTime()"""
        return float.__wrap(super(pygdx.AbstractGraphics, self).getRawDeltaTime())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDisplayModes(self, arg0: 'Monitor') -> List['pygdx.Graphics$DisplayMode']:
        """public com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayModes(com.badlogic.gdx.Graphics$Monitor)"""
        return List['pygdx.Graphics$DisplayMode'].__wrap(super(__MockGraphics, self).getDisplayModes(arg0))

    @override
    @overload
    def getPpcX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpcX()"""
        return float.__wrap(super(MockGraphics, self).getPpcX())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getWidth()"""
        return int.__wrap(super(MockGraphics, self).getWidth())

    @override
    @overload
    def setSystemCursor(self, arg0: 'SystemCursor'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setSystemCursor(com.badlogic.gdx.graphics.Cursor$SystemCursor)"""
        super(__MockGraphics, self).setSystemCursor(arg0)

    @override
    @overload
    def getBackBufferHeight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBackBufferHeight()"""
        return int.__wrap(super(MockGraphics, self).getBackBufferHeight())

    @override
    @overload
    def getSafeInsetBottom(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetBottom()"""
        return int.__wrap(super(MockGraphics, self).getSafeInsetBottom())

    @override
    @overload
    def isGL32Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL32Available()"""
        return bool.__wrap(super(MockGraphics, self).isGL32Available())

    @override
    @overload
    def setGL20(self, arg0: 'GL20'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL20(com.badlogic.gdx.graphics.GL20)"""
        super(__MockGraphics, self).setGL20(arg0)

    @override
    @overload
    def setGL30(self, arg0: 'GL30'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL30(com.badlogic.gdx.graphics.GL30)"""
        super(__MockGraphics, self).setGL30(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setGL31(self, arg0: 'GL31'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL31(com.badlogic.gdx.graphics.GL31)"""
        super(__MockGraphics, self).setGL31(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics()"""
        val = __MockGraphics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setResizable(boolean)"""
        super(__MockGraphics, self).setResizable(__boolean.valueOf(arg0))

    @override
    @overload
    def getGL31(self) -> 'graphics.GL31':
        """public com.badlogic.gdx.graphics.GL31 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL31()"""
        return 'graphics.GL31'.__wrap(super(MockGraphics, self).getGL31())

    @override
    @overload
    def isGL31Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL31Available()"""
        return bool.__wrap(super(MockGraphics, self).isGL31Available())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getGL20(self) -> 'graphics.GL20':
        """public com.badlogic.gdx.graphics.GL20 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL20()"""
        return 'graphics.GL20'.__wrap(super(MockGraphics, self).getGL20())

    @override
    @overload
    def isContinuousRendering(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isContinuousRendering()"""
        return bool.__wrap(super(MockGraphics, self).isContinuousRendering())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getSafeInsetTop(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetTop()"""
        return int.__wrap(super(MockGraphics, self).getSafeInsetTop())

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setTitle(java.lang.String)"""
        super(__MockGraphics, self).setTitle(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics()"""
        val = __MockGraphics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def supportsExtension(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.supportsExtension(java.lang.String)"""
        return bool.__wrap(super(__MockGraphics, self).supportsExtension(arg0))

    @override
    @overload
    def getDensity(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getDensity()"""
        return float.__wrap(super(pygdx.AbstractGraphics, self).getDensity())

    @overload
    def setWindowedMode(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setWindowedMode(int,int)"""
        return bool.__wrap(super(__MockGraphics, self).setWindowedMode(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setCursor(self, arg0: 'Cursor'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setCursor(com.badlogic.gdx.graphics.Cursor)"""
        super(__MockGraphics, self).setCursor(arg0)

    @override
    @overload
    def getBufferFormat(self) -> 'pygdx.Graphics$BufferFormat':
        """public com.badlogic.gdx.Graphics$BufferFormat com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBufferFormat()"""
        return 'pygdx.Graphics$BufferFormat'.__wrap(super(MockGraphics, self).getBufferFormat())

    @override
    @overload
    def requestRendering(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.requestRendering()"""
        super(MockGraphics, self).requestRendering()

    @override
    @overload
    def setGL32(self, arg0: 'GL32'):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setGL32(com.badlogic.gdx.graphics.GL32)"""
        super(__MockGraphics, self).setGL32(arg0)

    @override
    @overload
    def setVSync(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setVSync(boolean)"""
        super(__MockGraphics, self).setVSync(__boolean.valueOf(arg0))

    @override
    @overload
    def getGL32(self) -> 'graphics.GL32':
        """public com.badlogic.gdx.graphics.GL32 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL32()"""
        return 'graphics.GL32'.__wrap(super(MockGraphics, self).getGL32())

    @override
    @overload
    def getSafeInsetLeft(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetLeft()"""
        return int.__wrap(super(MockGraphics, self).getSafeInsetLeft())

    @override
    @overload
    def supportsDisplayModeChange(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.supportsDisplayModeChange()"""
        return bool.__wrap(super(MockGraphics, self).supportsDisplayModeChange())

    @override
    @overload
    def getDisplayMode(self) -> 'pygdx.Graphics$DisplayMode':
        """public com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayMode()"""
        return 'pygdx.Graphics$DisplayMode'.__wrap(super(MockGraphics, self).getDisplayMode())

    @override
    @overload
    def getPrimaryMonitor(self) -> 'pygdx.Graphics$Monitor':
        """public com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPrimaryMonitor()"""
        return 'pygdx.Graphics$Monitor'.__wrap(super(MockGraphics, self).getPrimaryMonitor())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPpiX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpiX()"""
        return float.__wrap(super(MockGraphics, self).getPpiX())

    @override
    @overload
    def getMonitor(self) -> 'pygdx.Graphics$Monitor':
        """public com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getMonitor()"""
        return 'pygdx.Graphics$Monitor'.__wrap(super(MockGraphics, self).getMonitor())

    @override
    @overload
    def getDisplayModes(self) -> List['pygdx.Graphics$DisplayMode']:
        """public com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayModes()"""
        return List['pygdx.Graphics$DisplayMode'].__wrap(super(MockGraphics, self).getDisplayModes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def incrementFrameId(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.incrementFrameId()"""
        super(MockGraphics, self).incrementFrameId()

    @overload
    def setFullscreenMode(self, arg0: 'DisplayMode') -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setFullscreenMode(com.badlogic.gdx.Graphics$DisplayMode)"""
        return bool.__wrap(super(__MockGraphics, self).setFullscreenMode(arg0))

    @override
    @overload
    def getSafeInsetRight(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getSafeInsetRight()"""
        return int.__wrap(super(MockGraphics, self).getSafeInsetRight())

    @override
    @overload
    def getPpcY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpcY()"""
        return float.__wrap(super(MockGraphics, self).getPpcY())

    @override
    @overload
    def getDeltaTime(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDeltaTime()"""
        return float.__wrap(super(MockGraphics, self).getDeltaTime())

    @overload
    def newCursor(self, arg0: 'Pixmap', arg1: int, arg2: int) -> 'graphics.Cursor':
        """public com.badlogic.gdx.graphics.Cursor com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.newCursor(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        return 'graphics.Cursor'.__wrap(super(__MockGraphics, self).newCursor(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getBackBufferScale(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getBackBufferScale()"""
        return float.__wrap(super(pygdx.AbstractGraphics, self).getBackBufferScale())

    @override
    @overload
    def getFrameId(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getFrameId()"""
        return int.__wrap(super(MockGraphics, self).getFrameId())

    @overload
    def getDisplayMode(self, arg0: 'Monitor') -> 'pygdx.Graphics$DisplayMode':
        """public com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getDisplayMode(com.badlogic.gdx.Graphics$Monitor)"""
        return 'pygdx.Graphics$DisplayMode'.__wrap(super(__MockGraphics, self).getDisplayMode(arg0))

    @override
    @overload
    def setForegroundFPS(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setForegroundFPS(int)"""
        super(__MockGraphics, self).setForegroundFPS(__int.valueOf(arg0))

    @override
    @overload
    def getGL30(self) -> 'graphics.GL30':
        """public com.badlogic.gdx.graphics.GL30 com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGL30()"""
        return 'graphics.GL30'.__wrap(super(MockGraphics, self).getGL30())

    @override
    @overload
    def getFramesPerSecond(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getFramesPerSecond()"""
        return int.__wrap(super(MockGraphics, self).getFramesPerSecond())

    @override
    @overload
    def getGLVersion(self) -> 'glutils.GLVersion':
        """public com.badlogic.gdx.graphics.glutils.GLVersion com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getGLVersion()"""
        return 'glutils.GLVersion'.__wrap(super(MockGraphics, self).getGLVersion())

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
    def setContinuousRendering(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.setContinuousRendering(boolean)"""
        super(__MockGraphics, self).setContinuousRendering(__boolean.valueOf(arg0))

    @override
    @overload
    def isGL30Available(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.isGL30Available()"""
        return bool.__wrap(super(MockGraphics, self).isGL30Available())

    @overload
    def updateTime(self):
        """public void com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.updateTime()"""
        super(MockGraphics, self).updateTime()

    @override
    @overload
    def getBackBufferWidth(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getBackBufferWidth()"""
        return int.__wrap(super(MockGraphics, self).getBackBufferWidth())

    @override
    @overload
    def getPpiY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getPpiY()"""
        return float.__wrap(super(MockGraphics, self).getPpiY())

    @override
    @overload
    def getMonitors(self) -> List['pygdx.Graphics$Monitor']:
        """public com.badlogic.gdx.Graphics$Monitor[] com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getMonitors()"""
        return List['pygdx.Graphics$Monitor'].__wrap(super(MockGraphics, self).getMonitors())

    @overload
    def getTargetRenderInterval(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics.getTargetRenderInterval()"""
        return int.__wrap(super(MockGraphics, self).getTargetRenderInterval())

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics