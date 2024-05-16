from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.Preferences as __Preferences
__Preferences = __Preferences
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class Preferences(ABC):
    """com.badlogic.gdx.Preferences"""
 
    @staticmethod
    def __wrap(java_value: __Preferences) -> 'Preferences':
        return Preferences(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Preferences):
        """
        Dynamic initializer for Preferences.
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
 
    @abstractmethod
    def getBoolean(self, arg0: str, arg1: bool):
        """public abstract boolean com.badlogic.gdx.Preferences.getBoolean(java.lang.String,boolean)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void com.badlogic.gdx.Preferences.clear()"""
        pass

    @abstractmethod
    def put(self, arg0: 'Map'):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.put(java.util.Map<java.lang.String, ?>)"""
        pass

    @abstractmethod
    def getFloat(self, arg0: str):
        """public abstract float com.badlogic.gdx.Preferences.getFloat(java.lang.String)"""
        pass

    @abstractmethod
    def putBoolean(self, arg0: str, arg1: bool):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putBoolean(java.lang.String,boolean)"""
        pass

    @abstractmethod
    def getInteger(self, arg0: str):
        """public abstract int com.badlogic.gdx.Preferences.getInteger(java.lang.String)"""
        pass

    @abstractmethod
    def putFloat(self, arg0: str, arg1: float):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putFloat(java.lang.String,float)"""
        pass

    @abstractmethod
    def putString(self, arg0: str, arg1: str):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putString(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def getLong(self, arg0: str):
        """public abstract long com.badlogic.gdx.Preferences.getLong(java.lang.String)"""
        pass

    @abstractmethod
    def getLong(self, arg0: str, arg1: int):
        """public abstract long com.badlogic.gdx.Preferences.getLong(java.lang.String,long)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.Preferences.flush()"""
        pass

    @abstractmethod
    def getFloat(self, arg0: str, arg1: float):
        """public abstract float com.badlogic.gdx.Preferences.getFloat(java.lang.String,float)"""
        pass

    @abstractmethod
    def putInteger(self, arg0: str, arg1: int):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putInteger(java.lang.String,int)"""
        pass

    @abstractmethod
    def getString(self, arg0: str, arg1: str):
        """public abstract java.lang.String com.badlogic.gdx.Preferences.getString(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, arg0: str):
        """public abstract void com.badlogic.gdx.Preferences.remove(java.lang.String)"""
        pass

    @abstractmethod
    def get(self, ):
        """public abstract java.util.Map<java.lang.String, ?> com.badlogic.gdx.Preferences.get()"""
        pass

    @abstractmethod
    def getBoolean(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Preferences.getBoolean(java.lang.String)"""
        pass

    @abstractmethod
    def contains(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Preferences.contains(java.lang.String)"""
        pass

    @abstractmethod
    def getInteger(self, arg0: str, arg1: int):
        """public abstract int com.badlogic.gdx.Preferences.getInteger(java.lang.String,int)"""
        pass

    @abstractmethod
    def putLong(self, arg0: str, arg1: int):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putLong(java.lang.String,long)"""
        pass

    @abstractmethod
    def getString(self, arg0: str):
        """public abstract java.lang.String com.badlogic.gdx.Preferences.getString(java.lang.String)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.Preferences
import com.badlogic.gdx.Preferences as __Preferences
__Preferences = __Preferences
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class Preferences(ABC):
    """com.badlogic.gdx.Preferences"""
 
    @staticmethod
    def __wrap(java_value: __Preferences) -> 'Preferences':
        return Preferences(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Preferences):
        """
        Dynamic initializer for Preferences.
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
 
    @abstractmethod
    def getBoolean(self, arg0: str, arg1: bool):
        """public abstract boolean com.badlogic.gdx.Preferences.getBoolean(java.lang.String,boolean)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void com.badlogic.gdx.Preferences.clear()"""
        pass

    @abstractmethod
    def put(self, arg0: 'Map'):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.put(java.util.Map<java.lang.String, ?>)"""
        pass

    @abstractmethod
    def getFloat(self, arg0: str):
        """public abstract float com.badlogic.gdx.Preferences.getFloat(java.lang.String)"""
        pass

    @abstractmethod
    def putBoolean(self, arg0: str, arg1: bool):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putBoolean(java.lang.String,boolean)"""
        pass

    @abstractmethod
    def getInteger(self, arg0: str):
        """public abstract int com.badlogic.gdx.Preferences.getInteger(java.lang.String)"""
        pass

    @abstractmethod
    def putFloat(self, arg0: str, arg1: float):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putFloat(java.lang.String,float)"""
        pass

    @abstractmethod
    def putString(self, arg0: str, arg1: str):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putString(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def getLong(self, arg0: str):
        """public abstract long com.badlogic.gdx.Preferences.getLong(java.lang.String)"""
        pass

    @abstractmethod
    def getLong(self, arg0: str, arg1: int):
        """public abstract long com.badlogic.gdx.Preferences.getLong(java.lang.String,long)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.Preferences.flush()"""
        pass

    @abstractmethod
    def getFloat(self, arg0: str, arg1: float):
        """public abstract float com.badlogic.gdx.Preferences.getFloat(java.lang.String,float)"""
        pass

    @abstractmethod
    def putInteger(self, arg0: str, arg1: int):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putInteger(java.lang.String,int)"""
        pass

    @abstractmethod
    def getString(self, arg0: str, arg1: str):
        """public abstract java.lang.String com.badlogic.gdx.Preferences.getString(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, arg0: str):
        """public abstract void com.badlogic.gdx.Preferences.remove(java.lang.String)"""
        pass

    @abstractmethod
    def get(self, ):
        """public abstract java.util.Map<java.lang.String, ?> com.badlogic.gdx.Preferences.get()"""
        pass

    @abstractmethod
    def getBoolean(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Preferences.getBoolean(java.lang.String)"""
        pass

    @abstractmethod
    def contains(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Preferences.contains(java.lang.String)"""
        pass

    @abstractmethod
    def getInteger(self, arg0: str, arg1: int):
        """public abstract int com.badlogic.gdx.Preferences.getInteger(java.lang.String,int)"""
        pass

    @abstractmethod
    def putLong(self, arg0: str, arg1: int):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putLong(java.lang.String,long)"""
        pass

    @abstractmethod
    def getString(self, arg0: str):
        """public abstract java.lang.String com.badlogic.gdx.Preferences.getString(java.lang.String)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.Preferences 
 
 
# CLASS: com.badlogic.gdx.Net$HttpMethods
import com.badlogic.gdx.Net as __Net_HttpMethods
__HttpMethods = __Net_HttpMethods.HttpMethods
 
class HttpMethods(ABC):
    """com.badlogic.gdx.Net.HttpMethods"""
 
    @staticmethod
    def __wrap(java_value: __HttpMethods) -> 'HttpMethods':
        return HttpMethods(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpMethods):
        """
        Dynamic initializer for HttpMethods.
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
 
 
# CLASS: com.badlogic.gdx.Input$Orientation
from builtins import str
import com.badlogic.gdx.Input as __Input_Orientation
__Orientation = __Input_Orientation.Orientation
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Orientation():
    """com.badlogic.gdx.Input.Orientation"""
 
    @staticmethod
    def __wrap(java_value: __Orientation) -> 'Orientation':
        return Orientation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Orientation):
        """
        Dynamic initializer for Orientation.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['Orientation']:
        """public static com.badlogic.gdx.Input$Orientation[] com.badlogic.gdx.Input$Orientation.values()"""
        return List[Orientation].__wrap(__Orientation.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Orientation':
        """public static com.badlogic.gdx.Input$Orientation com.badlogic.gdx.Input$Orientation.valueOf(java.lang.String)"""
        return Orientation.__wrap(__Orientation.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.Graphics
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.Graphics as __Graphics
__Graphics = __Graphics
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

 
class Graphics(ABC):
    """com.badlogic.gdx.Graphics"""
 
    @staticmethod
    def __wrap(java_value: __Graphics) -> 'Graphics':
        return Graphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Graphics):
        """
        Dynamic initializer for Graphics.
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
 
    @abstractmethod
    def newCursor(self, arg0: 'Pixmap', arg1: int, arg2: int):
        """public abstract com.badlogic.gdx.graphics.Cursor com.badlogic.gdx.Graphics.newCursor(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        pass

    @abstractmethod
    def getSafeInsetLeft(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetLeft()"""
        pass

    @abstractmethod
    def setVSync(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setVSync(boolean)"""
        pass

    @abstractmethod
    def getSafeInsetTop(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetTop()"""
        pass

    @abstractmethod
    def getMonitor(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.Graphics.getMonitor()"""
        pass

    @abstractmethod
    def getDisplayMode(self, ):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.Graphics.getDisplayMode()"""
        pass

    @abstractmethod
    def getMonitors(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor[] com.badlogic.gdx.Graphics.getMonitors()"""
        pass

    @abstractmethod
    def setGL20(self, arg0: 'GL20'):
        """public abstract void com.badlogic.gdx.Graphics.setGL20(com.badlogic.gdx.graphics.GL20)"""
        pass

    @abstractmethod
    def setGL31(self, arg0: 'GL31'):
        """public abstract void com.badlogic.gdx.Graphics.setGL31(com.badlogic.gdx.graphics.GL31)"""
        pass

    @abstractmethod
    def getPpiX(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpiX()"""
        pass

    @abstractmethod
    def supportsExtension(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Graphics.supportsExtension(java.lang.String)"""
        pass

    @abstractmethod
    def isGL32Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL32Available()"""
        pass

    @abstractmethod
    def getBackBufferHeight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getBackBufferHeight()"""
        pass

    @abstractmethod
    def getPpcY(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpcY()"""
        pass

    @abstractmethod
    def getDisplayMode(self, arg0: 'Monitor'):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.Graphics.getDisplayMode(com.badlogic.gdx.Graphics$Monitor)"""
        pass

    @abstractmethod
    def getFrameId(self, ):
        """public abstract long com.badlogic.gdx.Graphics.getFrameId()"""
        pass

    @abstractmethod
    def getPpcX(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpcX()"""
        pass

    @abstractmethod
    def getSafeInsetBottom(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetBottom()"""
        pass

    @abstractmethod
    def setGL30(self, arg0: 'GL30'):
        """public abstract void com.badlogic.gdx.Graphics.setGL30(com.badlogic.gdx.graphics.GL30)"""
        pass

    @abstractmethod
    def getDisplayModes(self, ):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.Graphics.getDisplayModes()"""
        pass

    @abstractmethod
    def supportsDisplayModeChange(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.supportsDisplayModeChange()"""
        pass

    @abstractmethod
    def setTitle(self, arg0: str):
        """public abstract void com.badlogic.gdx.Graphics.setTitle(java.lang.String)"""
        pass

    @abstractmethod
    def getGL30(self, ):
        """public abstract com.badlogic.gdx.graphics.GL30 com.badlogic.gdx.Graphics.getGL30()"""
        pass

    @abstractmethod
    def setGL32(self, arg0: 'GL32'):
        """public abstract void com.badlogic.gdx.Graphics.setGL32(com.badlogic.gdx.graphics.GL32)"""
        pass

    @abstractmethod
    def setWindowedMode(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.Graphics.setWindowedMode(int,int)"""
        pass

    @abstractmethod
    def isFullscreen(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isFullscreen()"""
        pass

    @abstractmethod
    def getGL32(self, ):
        """public abstract com.badlogic.gdx.graphics.GL32 com.badlogic.gdx.Graphics.getGL32()"""
        pass

    @abstractmethod
    def isGL31Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL31Available()"""
        pass

    @abstractmethod
    def getGLVersion(self, ):
        """public abstract com.badlogic.gdx.graphics.glutils.GLVersion com.badlogic.gdx.Graphics.getGLVersion()"""
        pass

    @abstractmethod
    def getPpiY(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpiY()"""
        pass

    @abstractmethod
    def getBackBufferScale(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getBackBufferScale()"""
        pass

    @abstractmethod
    def getBackBufferWidth(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getBackBufferWidth()"""
        pass

    @abstractmethod
    def getSafeInsetRight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetRight()"""
        pass

    @abstractmethod
    def getDensity(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getDensity()"""
        pass

    @abstractmethod
    def getBufferFormat(self, ):
        """public abstract com.badlogic.gdx.Graphics$BufferFormat com.badlogic.gdx.Graphics.getBufferFormat()"""
        pass

    @abstractmethod
    def isContinuousRendering(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isContinuousRendering()"""
        pass

    @abstractmethod
    def setContinuousRendering(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setContinuousRendering(boolean)"""
        pass

    @abstractmethod
    def getDeltaTime(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getDeltaTime()"""
        pass

    @abstractmethod
    def setFullscreenMode(self, arg0: 'DisplayMode'):
        """public abstract boolean com.badlogic.gdx.Graphics.setFullscreenMode(com.badlogic.gdx.Graphics$DisplayMode)"""
        pass

    @abstractmethod
    def setCursor(self, arg0: 'Cursor'):
        """public abstract void com.badlogic.gdx.Graphics.setCursor(com.badlogic.gdx.graphics.Cursor)"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.Graphics.getType()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getWidth()"""
        pass

    @abstractmethod
    def setResizable(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setResizable(boolean)"""
        pass

    @abstractmethod
    def setForegroundFPS(self, arg0: int):
        """public abstract void com.badlogic.gdx.Graphics.setForegroundFPS(int)"""
        pass

    @abstractmethod
    def requestRendering(self, ):
        """public abstract void com.badlogic.gdx.Graphics.requestRendering()"""
        pass

    @abstractmethod
    def getDisplayModes(self, arg0: 'Monitor'):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.Graphics.getDisplayModes(com.badlogic.gdx.Graphics$Monitor)"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getHeight()"""
        pass

    @abstractmethod
    def getFramesPerSecond(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getFramesPerSecond()"""
        pass

    @abstractmethod
    def isGL30Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL30Available()"""
        pass

    @abstractmethod
    def getGL31(self, ):
        """public abstract com.badlogic.gdx.graphics.GL31 com.badlogic.gdx.Graphics.getGL31()"""
        pass

    @abstractmethod
    def setUndecorated(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setUndecorated(boolean)"""
        pass

    @abstractmethod
    def setSystemCursor(self, arg0: 'SystemCursor'):
        """public abstract void com.badlogic.gdx.Graphics.setSystemCursor(com.badlogic.gdx.graphics.Cursor$SystemCursor)"""
        pass

    @abstractmethod
    def getPrimaryMonitor(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.Graphics.getPrimaryMonitor()"""
        pass

    @abstractmethod
    def getRawDeltaTime(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getRawDeltaTime()"""
        pass

    @abstractmethod
    def getGL20(self, ):
        """public abstract com.badlogic.gdx.graphics.GL20 com.badlogic.gdx.Graphics.getGL20()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ApplicationLogger
import com.badlogic.gdx.ApplicationLogger as __ApplicationLogger
__ApplicationLogger = __ApplicationLogger
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class ApplicationLogger(ABC):
    """com.badlogic.gdx.ApplicationLogger"""
 
    @staticmethod
    def __wrap(java_value: __ApplicationLogger) -> 'ApplicationLogger':
        return ApplicationLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ApplicationLogger):
        """
        Dynamic initializer for ApplicationLogger.
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
 
    @abstractmethod
    def error(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ApplicationLogger.error(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ApplicationLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ApplicationLogger.log(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ApplicationLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ApplicationLogger.debug(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ApplicationLogger.log(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Net$HttpResponse
import com.badlogic.gdx.Net as __Net_HttpResponse
__HttpResponse = __Net_HttpResponse.HttpResponse
from abc import abstractmethod, ABC
 
class HttpResponse(ABC):
    """com.badlogic.gdx.Net.HttpResponse"""
 
    @staticmethod
    def __wrap(java_value: __HttpResponse) -> 'HttpResponse':
        return HttpResponse(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpResponse):
        """
        Dynamic initializer for HttpResponse.
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
 
    @abstractmethod
    def getResult(self, ):
        """public abstract byte[] com.badlogic.gdx.Net$HttpResponse.getResult()"""
        pass

    @abstractmethod
    def getResultAsStream(self, ):
        """public abstract java.io.InputStream com.badlogic.gdx.Net$HttpResponse.getResultAsStream()"""
        pass

    @abstractmethod
    def getHeaders(self, ):
        """public abstract java.util.Map<java.lang.String, java.util.List<java.lang.String>> com.badlogic.gdx.Net$HttpResponse.getHeaders()"""
        pass

    @abstractmethod
    def getHeader(self, arg0: str):
        """public abstract java.lang.String com.badlogic.gdx.Net$HttpResponse.getHeader(java.lang.String)"""
        pass

    @abstractmethod
    def getStatus(self, ):
        """public abstract com.badlogic.gdx.net.HttpStatus com.badlogic.gdx.Net$HttpResponse.getStatus()"""
        pass

    @abstractmethod
    def getResultAsString(self, ):
        """public abstract java.lang.String com.badlogic.gdx.Net$HttpResponse.getResultAsString()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.AbstractGraphics
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.Graphics as __Graphics
__Graphics = __Graphics
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.AbstractGraphics as __AbstractGraphics
__AbstractGraphics = __AbstractGraphics
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class AbstractGraphics(ABC):
    """com.badlogic.gdx.AbstractGraphics"""
 
    @staticmethod
    def __wrap(java_value: __AbstractGraphics) -> 'AbstractGraphics':
        return AbstractGraphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractGraphics):
        """
        Dynamic initializer for AbstractGraphics.
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
 
    @abstractmethod
    def newCursor(self, arg0: 'Pixmap', arg1: int, arg2: int):
        """public abstract com.badlogic.gdx.graphics.Cursor com.badlogic.gdx.Graphics.newCursor(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def getSafeInsetLeft(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetLeft()"""
        pass

    @abstractmethod
    def setVSync(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setVSync(boolean)"""
        pass

    @abstractmethod
    def getSafeInsetTop(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetTop()"""
        pass

    @abstractmethod
    def getMonitor(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.Graphics.getMonitor()"""
        pass

    @abstractmethod
    def getDisplayMode(self, ):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.Graphics.getDisplayMode()"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getMonitors(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor[] com.badlogic.gdx.Graphics.getMonitors()"""
        pass

    @abstractmethod
    def setGL20(self, arg0: 'GL20'):
        """public abstract void com.badlogic.gdx.Graphics.setGL20(com.badlogic.gdx.graphics.GL20)"""
        pass

    @abstractmethod
    def setGL31(self, arg0: 'GL31'):
        """public abstract void com.badlogic.gdx.Graphics.setGL31(com.badlogic.gdx.graphics.GL31)"""
        pass

    @abstractmethod
    def getPpiX(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpiX()"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.AbstractGraphics()"""
        val = __AbstractGraphics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def supportsExtension(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Graphics.supportsExtension(java.lang.String)"""
        pass

    @abstractmethod
    def isGL32Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL32Available()"""
        pass

    @override
    @overload
    def getRawDeltaTime(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getRawDeltaTime()"""
        return float.__wrap(super(AbstractGraphics, self).getRawDeltaTime())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def getBackBufferHeight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getBackBufferHeight()"""
        pass

    @abstractmethod
    def getPpcY(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpcY()"""
        pass

    @abstractmethod
    def getDisplayMode(self, arg0: 'Monitor'):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.Graphics.getDisplayMode(com.badlogic.gdx.Graphics$Monitor)"""
        pass

    @abstractmethod
    def getFrameId(self, ):
        """public abstract long com.badlogic.gdx.Graphics.getFrameId()"""
        pass

    @abstractmethod
    def getPpcX(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpcX()"""
        pass

    @abstractmethod
    def getSafeInsetBottom(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetBottom()"""
        pass

    @abstractmethod
    def setGL30(self, arg0: 'GL30'):
        """public abstract void com.badlogic.gdx.Graphics.setGL30(com.badlogic.gdx.graphics.GL30)"""
        pass

    @abstractmethod
    def getDisplayModes(self, ):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.Graphics.getDisplayModes()"""
        pass

    @abstractmethod
    def supportsDisplayModeChange(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.supportsDisplayModeChange()"""
        pass

    @abstractmethod
    def setTitle(self, arg0: str):
        """public abstract void com.badlogic.gdx.Graphics.setTitle(java.lang.String)"""
        pass

    @abstractmethod
    def getGL30(self, ):
        """public abstract com.badlogic.gdx.graphics.GL30 com.badlogic.gdx.Graphics.getGL30()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getDensity(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getDensity()"""
        return float.__wrap(super(AbstractGraphics, self).getDensity())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @abstractmethod
    def setGL32(self, arg0: 'GL32'):
        """public abstract void com.badlogic.gdx.Graphics.setGL32(com.badlogic.gdx.graphics.GL32)"""
        pass

    @abstractmethod
    def setWindowedMode(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.Graphics.setWindowedMode(int,int)"""
        pass

    @abstractmethod
    def isFullscreen(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isFullscreen()"""
        pass

    @abstractmethod
    def getGL32(self, ):
        """public abstract com.badlogic.gdx.graphics.GL32 com.badlogic.gdx.Graphics.getGL32()"""
        pass

    @abstractmethod
    def isGL31Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL31Available()"""
        pass

    @abstractmethod
    def getGLVersion(self, ):
        """public abstract com.badlogic.gdx.graphics.glutils.GLVersion com.badlogic.gdx.Graphics.getGLVersion()"""
        pass

    @abstractmethod
    def getPpiY(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpiY()"""
        pass

    @abstractmethod
    def getBackBufferWidth(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getBackBufferWidth()"""
        pass

    @abstractmethod
    def getSafeInsetRight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetRight()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def getBufferFormat(self, ):
        """public abstract com.badlogic.gdx.Graphics$BufferFormat com.badlogic.gdx.Graphics.getBufferFormat()"""
        pass

    @abstractmethod
    def isContinuousRendering(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isContinuousRendering()"""
        pass

    @abstractmethod
    def setContinuousRendering(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setContinuousRendering(boolean)"""
        pass

    @abstractmethod
    def getDeltaTime(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getDeltaTime()"""
        pass

    @abstractmethod
    def setFullscreenMode(self, arg0: 'DisplayMode'):
        """public abstract boolean com.badlogic.gdx.Graphics.setFullscreenMode(com.badlogic.gdx.Graphics$DisplayMode)"""
        pass

    @abstractmethod
    def setCursor(self, arg0: 'Cursor'):
        """public abstract void com.badlogic.gdx.Graphics.setCursor(com.badlogic.gdx.graphics.Cursor)"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.Graphics.getType()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getWidth()"""
        pass

    @abstractmethod
    def setResizable(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setResizable(boolean)"""
        pass

    @abstractmethod
    def setForegroundFPS(self, arg0: int):
        """public abstract void com.badlogic.gdx.Graphics.setForegroundFPS(int)"""
        pass

    @abstractmethod
    def requestRendering(self, ):
        """public abstract void com.badlogic.gdx.Graphics.requestRendering()"""
        pass

    @abstractmethod
    def getDisplayModes(self, arg0: 'Monitor'):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.Graphics.getDisplayModes(com.badlogic.gdx.Graphics$Monitor)"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getHeight()"""
        pass

    @abstractmethod
    def getFramesPerSecond(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getFramesPerSecond()"""
        pass

    @override
    @overload
    def getBackBufferScale(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getBackBufferScale()"""
        return float.__wrap(super(AbstractGraphics, self).getBackBufferScale())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def isGL30Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL30Available()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @abstractmethod
    def getGL31(self, ):
        """public abstract com.badlogic.gdx.graphics.GL31 com.badlogic.gdx.Graphics.getGL31()"""
        pass

    @abstractmethod
    def setUndecorated(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setUndecorated(boolean)"""
        pass

    @abstractmethod
    def setSystemCursor(self, arg0: 'SystemCursor'):
        """public abstract void com.badlogic.gdx.Graphics.setSystemCursor(com.badlogic.gdx.graphics.Cursor$SystemCursor)"""
        pass

    @abstractmethod
    def getPrimaryMonitor(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.Graphics.getPrimaryMonitor()"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.AbstractGraphics()"""
        val = __AbstractGraphics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def getGL20(self, ):
        """public abstract com.badlogic.gdx.graphics.GL20 com.badlogic.gdx.Graphics.getGL20()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Graphics$BufferFormat
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.Graphics as __Graphics_BufferFormat
__BufferFormat = __Graphics_BufferFormat.BufferFormat
from builtins import bool
from builtins import int
 
class BufferFormat():
    """com.badlogic.gdx.Graphics.BufferFormat"""
 
    @staticmethod
    def __wrap(java_value: __BufferFormat) -> 'BufferFormat':
        return BufferFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BufferFormat):
        """
        Dynamic initializer for BufferFormat.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.Graphics$BufferFormat.toString()"""
        return str.__wrap(super(BufferFormat, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool):
        """public com.badlogic.gdx.Graphics$BufferFormat(int,int,int,int,int,int,int,boolean)"""
        val = __BufferFormat(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Game
import com.badlogic.gdx.Game as __Game
__Game = __Game
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ApplicationListener as __ApplicationListener
__ApplicationListener = __ApplicationListener
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.Screen as __Screen
__Screen = __Screen
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Game(ABC):
    """com.badlogic.gdx.Game"""
 
    @staticmethod
    def __wrap(java_value: __Game) -> 'Game':
        return Game(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Game):
        """
        Dynamic initializer for Game.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Game()"""
        val = __Game()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.Game.pause()"""
        super(Game, self).pause()

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.Game.resume()"""
        super(Game, self).resume()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.Game.resize(int,int)"""
        super(__Game, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setScreen(self, arg0: 'Screen'):
        """public void com.badlogic.gdx.Game.setScreen(com.badlogic.gdx.Screen)"""
        super(__Game, self).setScreen(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Game()"""
        val = __Game()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getScreen(self) -> 'Screen':
        """public com.badlogic.gdx.Screen com.badlogic.gdx.Game.getScreen()"""
        return 'Screen'.__wrap(super(Game, self).getScreen())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.Game.dispose()"""
        super(Game, self).dispose()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @abstractmethod
    def create(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.create()"""
        pass

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

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.Game.render()"""
        super(Game, self).render()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Input$TextInputListener
from abc import abstractmethod, ABC
import com.badlogic.gdx.Input as __Input_TextInputListener
__TextInputListener = __Input_TextInputListener.TextInputListener
 
class TextInputListener(ABC):
    """com.badlogic.gdx.Input.TextInputListener"""
 
    @staticmethod
    def __wrap(java_value: __TextInputListener) -> 'TextInputListener':
        return TextInputListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextInputListener):
        """
        Dynamic initializer for TextInputListener.
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
 
    @abstractmethod
    def input(self, arg0: str):
        """public abstract void com.badlogic.gdx.Input$TextInputListener.input(java.lang.String)"""
        pass

    @abstractmethod
    def canceled(self, ):
        """public abstract void com.badlogic.gdx.Input$TextInputListener.canceled()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Files$FileType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.Files as __Files_FileType
__FileType = __Files_FileType.FileType
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class FileType():
    """com.badlogic.gdx.Files.FileType"""
 
    @staticmethod
    def __wrap(java_value: __FileType) -> 'FileType':
        return FileType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileType):
        """
        Dynamic initializer for FileType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['FileType']:
        """public static com.badlogic.gdx.Files$FileType[] com.badlogic.gdx.Files$FileType.values()"""
        return List[FileType].__wrap(__FileType.values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FileType':
        """public static com.badlogic.gdx.Files$FileType com.badlogic.gdx.Files$FileType.valueOf(java.lang.String)"""
        return FileType.__wrap(__FileType.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.LifecycleListener
import com.badlogic.gdx.LifecycleListener as __LifecycleListener
__LifecycleListener = __LifecycleListener
from abc import abstractmethod, ABC
 
class LifecycleListener(ABC):
    """com.badlogic.gdx.LifecycleListener"""
 
    @staticmethod
    def __wrap(java_value: __LifecycleListener) -> 'LifecycleListener':
        return LifecycleListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LifecycleListener):
        """
        Dynamic initializer for LifecycleListener.
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
 
    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.LifecycleListener.dispose()"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.LifecycleListener.resume()"""
        pass

    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.LifecycleListener.pause()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.InputProcessor
from abc import abstractmethod, ABC
import com.badlogic.gdx.InputProcessor as __InputProcessor
__InputProcessor = __InputProcessor
 
class InputProcessor(ABC):
    """com.badlogic.gdx.InputProcessor"""
 
    @staticmethod
    def __wrap(java_value: __InputProcessor) -> 'InputProcessor':
        return InputProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InputProcessor):
        """
        Dynamic initializer for InputProcessor.
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
 
    @abstractmethod
    def keyTyped(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.InputProcessor.keyTyped(char)"""
        pass

    @abstractmethod
    def touchDragged(self, arg0: int, arg1: int, arg2: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchDragged(int,int,int)"""
        pass

    @abstractmethod
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchCancelled(int,int,int,int)"""
        pass

    @abstractmethod
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchDown(int,int,int,int)"""
        pass

    @abstractmethod
    def keyDown(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.keyDown(int)"""
        pass

    @abstractmethod
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchUp(int,int,int,int)"""
        pass

    @abstractmethod
    def mouseMoved(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.mouseMoved(int,int)"""
        pass

    @abstractmethod
    def keyUp(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.keyUp(int)"""
        pass

    @abstractmethod
    def scrolled(self, arg0: float, arg1: float):
        """public abstract boolean com.badlogic.gdx.InputProcessor.scrolled(float,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Screen
import com.badlogic.gdx.Screen as __Screen
__Screen = __Screen
from abc import abstractmethod, ABC
 
class Screen(ABC):
    """com.badlogic.gdx.Screen"""
 
    @staticmethod
    def __wrap(java_value: __Screen) -> 'Screen':
        return Screen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Screen):
        """
        Dynamic initializer for Screen.
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
 
    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.Screen.pause()"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.Screen.resume()"""
        pass

    @abstractmethod
    def render(self, arg0: float):
        """public abstract void com.badlogic.gdx.Screen.render(float)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.Screen.dispose()"""
        pass

    @abstractmethod
    def resize(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.Screen.resize(int,int)"""
        pass

    @abstractmethod
    def show(self, ):
        """public abstract void com.badlogic.gdx.Screen.show()"""
        pass

    @abstractmethod
    def hide(self, ):
        """public abstract void com.badlogic.gdx.Screen.hide()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Application
import java.lang.Runnable as Runnable
import java.lang.Throwable as Throwable
import com.badlogic.gdx.Application as __Application
__Application = __Application
from abc import abstractmethod, ABC
 
class Application(ABC):
    """com.badlogic.gdx.Application"""
 
    @staticmethod
    def __wrap(java_value: __Application) -> 'Application':
        return Application(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Application):
        """
        Dynamic initializer for Application.
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
 
    @abstractmethod
    def getNativeHeap(self, ):
        """public abstract long com.badlogic.gdx.Application.getNativeHeap()"""
        pass

    @abstractmethod
    def getJavaHeap(self, ):
        """public abstract long com.badlogic.gdx.Application.getJavaHeap()"""
        pass

    @abstractmethod
    def getInput(self, ):
        """public abstract com.badlogic.gdx.Input com.badlogic.gdx.Application.getInput()"""
        pass

    @abstractmethod
    def setLogLevel(self, arg0: int):
        """public abstract void com.badlogic.gdx.Application.setLogLevel(int)"""
        pass

    @abstractmethod
    def getLogLevel(self, ):
        """public abstract int com.badlogic.gdx.Application.getLogLevel()"""
        pass

    @abstractmethod
    def getPreferences(self, arg0: str):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Application.getPreferences(java.lang.String)"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.Application.log(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.Application.error(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def getVersion(self, ):
        """public abstract int com.badlogic.gdx.Application.getVersion()"""
        pass

    @abstractmethod
    def getApplicationLogger(self, ):
        """public abstract com.badlogic.gdx.ApplicationLogger com.badlogic.gdx.Application.getApplicationLogger()"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.Application.debug(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def getNet(self, ):
        """public abstract com.badlogic.gdx.Net com.badlogic.gdx.Application.getNet()"""
        pass

    @abstractmethod
    def removeLifecycleListener(self, arg0: 'LifecycleListener'):
        """public abstract void com.badlogic.gdx.Application.removeLifecycleListener(com.badlogic.gdx.LifecycleListener)"""
        pass

    @abstractmethod
    def getAudio(self, ):
        """public abstract com.badlogic.gdx.Audio com.badlogic.gdx.Application.getAudio()"""
        pass

    @abstractmethod
    def getApplicationListener(self, ):
        """public abstract com.badlogic.gdx.ApplicationListener com.badlogic.gdx.Application.getApplicationListener()"""
        pass

    @abstractmethod
    def getFiles(self, ):
        """public abstract com.badlogic.gdx.Files com.badlogic.gdx.Application.getFiles()"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.Application.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getClipboard(self, ):
        """public abstract com.badlogic.gdx.utils.Clipboard com.badlogic.gdx.Application.getClipboard()"""
        pass

    @abstractmethod
    def postRunnable(self, arg0: 'Runnable'):
        """public abstract void com.badlogic.gdx.Application.postRunnable(java.lang.Runnable)"""
        pass

    @abstractmethod
    def getGraphics(self, ):
        """public abstract com.badlogic.gdx.Graphics com.badlogic.gdx.Application.getGraphics()"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.Application.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.Application$ApplicationType com.badlogic.gdx.Application.getType()"""
        pass

    @abstractmethod
    def setApplicationLogger(self, arg0: 'ApplicationLogger'):
        """public abstract void com.badlogic.gdx.Application.setApplicationLogger(com.badlogic.gdx.ApplicationLogger)"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.Application.log(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def exit(self, ):
        """public abstract void com.badlogic.gdx.Application.exit()"""
        pass

    @abstractmethod
    def addLifecycleListener(self, arg0: 'LifecycleListener'):
        """public abstract void com.badlogic.gdx.Application.addLifecycleListener(com.badlogic.gdx.LifecycleListener)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Input$VibrationType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.Input as __Input_VibrationType
__VibrationType = __Input_VibrationType.VibrationType
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class VibrationType():
    """com.badlogic.gdx.Input.VibrationType"""
 
    @staticmethod
    def __wrap(java_value: __VibrationType) -> 'VibrationType':
        return VibrationType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VibrationType):
        """
        Dynamic initializer for VibrationType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'VibrationType':
        """public static com.badlogic.gdx.Input$VibrationType com.badlogic.gdx.Input$VibrationType.valueOf(java.lang.String)"""
        return VibrationType.__wrap(__VibrationType.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['VibrationType']:
        """public static com.badlogic.gdx.Input$VibrationType[] com.badlogic.gdx.Input$VibrationType.values()"""
        return List[VibrationType].__wrap(__VibrationType.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.Input$Buttons
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.Input as __Input_Buttons
__Buttons = __Input_Buttons.Buttons
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Buttons():
    """com.badlogic.gdx.Input.Buttons"""
 
    @staticmethod
    def __wrap(java_value: __Buttons) -> 'Buttons':
        return Buttons(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buttons):
        """
        Dynamic initializer for Buttons.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Input$Buttons()"""
        val = __Buttons()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Input$Buttons()"""
        val = __Buttons()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Graphics$DisplayMode
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import com.badlogic.gdx.Graphics as __Graphics_DisplayMode
__DisplayMode = __Graphics_DisplayMode.DisplayMode
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DisplayMode():
    """com.badlogic.gdx.Graphics.DisplayMode"""
 
    @staticmethod
    def __wrap(java_value: __DisplayMode) -> 'DisplayMode':
        return DisplayMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DisplayMode):
        """
        Dynamic initializer for DisplayMode.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.Graphics$DisplayMode.toString()"""
        return str.__wrap(super(DisplayMode, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.Files
import com.badlogic.gdx.Files as __Files
__Files = __Files
from abc import abstractmethod, ABC
 
class Files(ABC):
    """com.badlogic.gdx.Files"""
 
    @staticmethod
    def __wrap(java_value: __Files) -> 'Files':
        return Files(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Files):
        """
        Dynamic initializer for Files.
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
 
    @abstractmethod
    def getLocalStoragePath(self, ):
        """public abstract java.lang.String com.badlogic.gdx.Files.getLocalStoragePath()"""
        pass

    @abstractmethod
    def local(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.local(java.lang.String)"""
        pass

    @abstractmethod
    def getExternalStoragePath(self, ):
        """public abstract java.lang.String com.badlogic.gdx.Files.getExternalStoragePath()"""
        pass

    @abstractmethod
    def external(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.external(java.lang.String)"""
        pass

    @abstractmethod
    def isExternalStorageAvailable(self, ):
        """public abstract boolean com.badlogic.gdx.Files.isExternalStorageAvailable()"""
        pass

    @abstractmethod
    def getFileHandle(self, arg0: str, arg1: 'FileType'):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.getFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        pass

    @abstractmethod
    def isLocalStorageAvailable(self, ):
        """public abstract boolean com.badlogic.gdx.Files.isLocalStorageAvailable()"""
        pass

    @abstractmethod
    def internal(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.internal(java.lang.String)"""
        pass

    @abstractmethod
    def classpath(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.classpath(java.lang.String)"""
        pass

    @abstractmethod
    def absolute(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.absolute(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Graphics$Monitor
from builtins import str
import com.badlogic.gdx.Graphics as __Graphics_Monitor
__Monitor = __Graphics_Monitor.Monitor
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Monitor():
    """com.badlogic.gdx.Graphics.Monitor"""
 
    @staticmethod
    def __wrap(java_value: __Monitor) -> 'Monitor':
        return Monitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Monitor):
        """
        Dynamic initializer for Monitor.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Graphics$GraphicsType
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.Graphics as __Graphics_GraphicsType
__GraphicsType = __Graphics_GraphicsType.GraphicsType
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class GraphicsType():
    """com.badlogic.gdx.Graphics.GraphicsType"""
 
    @staticmethod
    def __wrap(java_value: __GraphicsType) -> 'GraphicsType':
        return GraphicsType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GraphicsType):
        """
        Dynamic initializer for GraphicsType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['GraphicsType']:
        """public static com.badlogic.gdx.Graphics$GraphicsType[] com.badlogic.gdx.Graphics$GraphicsType.values()"""
        return List[GraphicsType].__wrap(__GraphicsType.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GraphicsType':
        """public static com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.Graphics$GraphicsType.valueOf(java.lang.String)"""
        return GraphicsType.__wrap(__GraphicsType.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.AbstractInput
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.AbstractInput as __AbstractInput
__AbstractInput = __AbstractInput
import com.badlogic.gdx.Input as __Input
__Input = __Input
from builtins import float
from abc import abstractmethod, ABC
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
 
class AbstractInput(ABC):
    """com.badlogic.gdx.AbstractInput"""
 
    @staticmethod
    def __wrap(java_value: __AbstractInput) -> 'AbstractInput':
        return AbstractInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractInput):
        """
        Dynamic initializer for AbstractInput.
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
 
    @abstractmethod
    def getRotation(self, ):
        """public abstract int com.badlogic.gdx.Input.getRotation()"""
        pass

    @abstractmethod
    def getNativeOrientation(self, ):
        """public abstract com.badlogic.gdx.Input$Orientation com.badlogic.gdx.Input.getNativeOrientation()"""
        pass

    @override
    @overload
    def isCatchBackKey(self) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isCatchBackKey()"""
        return bool.__wrap(super(AbstractInput, self).isCatchBackKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setCatchKey(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.AbstractInput.setCatchKey(int,boolean)"""
        super(__AbstractInput, self).setCatchKey(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @abstractmethod
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public abstract void com.badlogic.gdx.Input.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        pass

    @overload
    def isKeyPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isKeyPressed(int)"""
        return bool.__wrap(super(__AbstractInput, self).isKeyPressed(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getDeltaY(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getDeltaY(int)"""
        pass

    @abstractmethod
    def getMaxPointers(self, ):
        """public abstract int com.badlogic.gdx.Input.getMaxPointers()"""
        pass

    @abstractmethod
    def isTouched(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isTouched(int)"""
        pass

    @abstractmethod
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public abstract void com.badlogic.gdx.Input.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        pass

    @override
    @overload
    def isCatchMenuKey(self) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isCatchMenuKey()"""
        return bool.__wrap(super(AbstractInput, self).isCatchMenuKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def isButtonJustPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isButtonJustPressed(int)"""
        pass

    @abstractmethod
    def getY(self, ):
        """public abstract int com.badlogic.gdx.Input.getY()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public abstract void com.badlogic.gdx.Input.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        pass

    @abstractmethod
    def getRoll(self, ):
        """public abstract float com.badlogic.gdx.Input.getRoll()"""
        pass

    @abstractmethod
    def getDeltaY(self, ):
        """public abstract int com.badlogic.gdx.Input.getDeltaY()"""
        pass

    @overload
    def isKeyJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isKeyJustPressed(int)"""
        return bool.__wrap(super(__AbstractInput, self).isKeyJustPressed(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.AbstractInput()"""
        val = __AbstractInput()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def getPressure(self, arg0: int):
        """public abstract float com.badlogic.gdx.Input.getPressure(int)"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @abstractmethod
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public abstract void com.badlogic.gdx.Input.vibrate(int,int,boolean)"""
        pass

    @override
    @overload
    def setCatchMenuKey(self, arg0: bool):
        """public void com.badlogic.gdx.AbstractInput.setCatchMenuKey(boolean)"""
        super(__AbstractInput, self).setCatchMenuKey(__boolean.valueOf(arg0))

    @abstractmethod
    def getX(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getX(int)"""
        pass

    @abstractmethod
    def isCursorCatched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isCursorCatched()"""
        pass

    @abstractmethod
    def isPeripheralAvailable(self, arg0: 'Peripheral'):
        """public abstract boolean com.badlogic.gdx.Input.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        pass

    @abstractmethod
    def getRotationMatrix(self, arg0: 'float'):
        """public abstract void com.badlogic.gdx.Input.getRotationMatrix(float[])"""
        pass

    @abstractmethod
    def getGyroscopeY(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeY()"""
        pass

    @abstractmethod
    def getGyroscopeX(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeX()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def vibrate(self, arg0: 'VibrationType'):
        """public abstract void com.badlogic.gdx.Input.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        pass

    @abstractmethod
    def getDeltaX(self, ):
        """public abstract int com.badlogic.gdx.Input.getDeltaX()"""
        pass

    @abstractmethod
    def isTouched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isTouched()"""
        pass

    @abstractmethod
    def getPressure(self, ):
        """public abstract float com.badlogic.gdx.Input.getPressure()"""
        pass

    @abstractmethod
    def getPitch(self, ):
        """public abstract float com.badlogic.gdx.Input.getPitch()"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int, arg1: bool):
        """public abstract void com.badlogic.gdx.Input.vibrate(int,boolean)"""
        pass

    @abstractmethod
    def setCursorCatched(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setCursorCatched(boolean)"""
        pass

    @override
    @overload
    def setCatchBackKey(self, arg0: bool):
        """public void com.badlogic.gdx.AbstractInput.setCatchBackKey(boolean)"""
        super(__AbstractInput, self).setCatchBackKey(__boolean.valueOf(arg0))

    @overload
    def isCatchKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isCatchKey(int)"""
        return bool.__wrap(super(__AbstractInput, self).isCatchKey(__int.valueOf(arg0)))

    @abstractmethod
    def isButtonPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isButtonPressed(int)"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int):
        """public abstract void com.badlogic.gdx.Input.vibrate(int)"""
        pass

    @abstractmethod
    def getAccelerometerX(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerX()"""
        pass

    @abstractmethod
    def getAzimuth(self, ):
        """public abstract float com.badlogic.gdx.Input.getAzimuth()"""
        pass

    @abstractmethod
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public abstract void com.badlogic.gdx.Input.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        pass

    @abstractmethod
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setOnscreenKeyboardVisible(boolean)"""
        pass

    @abstractmethod
    def setCursorPosition(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.Input.setCursorPosition(int,int)"""
        pass

    @abstractmethod
    def getGyroscopeZ(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeZ()"""
        pass

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

    @abstractmethod
    def getY(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getY(int)"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.AbstractInput()"""
        val = __AbstractInput()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def getCurrentEventTime(self, ):
        """public abstract long com.badlogic.gdx.Input.getCurrentEventTime()"""
        pass

    @abstractmethod
    def getAccelerometerZ(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerZ()"""
        pass

    @abstractmethod
    def getDeltaX(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getDeltaX(int)"""
        pass

    @abstractmethod
    def justTouched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.justTouched()"""
        pass

    @abstractmethod
    def getInputProcessor(self, ):
        """public abstract com.badlogic.gdx.InputProcessor com.badlogic.gdx.Input.getInputProcessor()"""
        pass

    @abstractmethod
    def getX(self, ):
        """public abstract int com.badlogic.gdx.Input.getX()"""
        pass

    @abstractmethod
    def getAccelerometerY(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerY()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.InputMultiplexer
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.SnapshotArray as __SnapshotArray
__SnapshotArray = __SnapshotArray
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.InputMultiplexer as __InputMultiplexer
__InputMultiplexer = __InputMultiplexer
from builtins import int
 
class InputMultiplexer():
    """com.badlogic.gdx.InputMultiplexer"""
 
    @staticmethod
    def __wrap(java_value: __InputMultiplexer) -> 'InputMultiplexer':
        return InputMultiplexer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InputMultiplexer):
        """
        Dynamic initializer for InputMultiplexer.
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
    def setProcessors(self, *arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.InputMultiplexer.setProcessors(com.badlogic.gdx.InputProcessor...)"""
        super(__InputMultiplexer, self).setProcessors(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.InputMultiplexer()"""
        val = __InputMultiplexer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, *arg0: 'InputProcessor'):
        """public com.badlogic.gdx.InputMultiplexer(com.badlogic.gdx.InputProcessor...)"""
        val = __InputMultiplexer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.scrolled(float,float)"""
        return bool.__wrap(super(__InputMultiplexer, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.InputMultiplexer.size()"""
        return int.__wrap(super(InputMultiplexer, self).size())

    @overload
    def addProcessor(self, arg0: int, arg1: 'InputProcessor'):
        """public void com.badlogic.gdx.InputMultiplexer.addProcessor(int,com.badlogic.gdx.InputProcessor)"""
        super(__InputMultiplexer, self).addProcessor(__int.valueOf(arg0), arg1)

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__InputMultiplexer, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.InputMultiplexer()"""
        val = __InputMultiplexer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.touchDragged(int,int,int)"""
        return bool.__wrap(super(__InputMultiplexer, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getProcessors(self) -> 'utils.SnapshotArray':
        """public com.badlogic.gdx.utils.SnapshotArray<com.badlogic.gdx.InputProcessor> com.badlogic.gdx.InputMultiplexer.getProcessors()"""
        return 'utils.SnapshotArray'.__wrap(super(InputMultiplexer, self).getProcessors())

    @overload
    def setProcessors(self, arg0: 'Array'):
        """public void com.badlogic.gdx.InputMultiplexer.setProcessors(com.badlogic.gdx.utils.Array<com.badlogic.gdx.InputProcessor>)"""
        super(__InputMultiplexer, self).setProcessors(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.mouseMoved(int,int)"""
        return bool.__wrap(super(__InputMultiplexer, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.keyTyped(char)"""
        return bool.__wrap(super(__InputMultiplexer, self).keyTyped(__char.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.InputMultiplexer.clear()"""
        super(InputMultiplexer, self).clear()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.keyUp(int)"""
        return bool.__wrap(super(__InputMultiplexer, self).keyUp(__int.valueOf(arg0)))

    @overload
    def addProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.InputMultiplexer.addProcessor(com.badlogic.gdx.InputProcessor)"""
        super(__InputMultiplexer, self).addProcessor(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeProcessor(self, arg0: int):
        """public void com.badlogic.gdx.InputMultiplexer.removeProcessor(int)"""
        super(__InputMultiplexer, self).removeProcessor(__int.valueOf(arg0))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.keyDown(int)"""
        return bool.__wrap(super(__InputMultiplexer, self).keyDown(__int.valueOf(arg0)))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__InputMultiplexer, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__InputMultiplexer, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def removeProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.InputMultiplexer.removeProcessor(com.badlogic.gdx.InputProcessor)"""
        super(__InputMultiplexer, self).removeProcessor(arg0) 
 
 
# CLASS: com.badlogic.gdx.Input
import com.badlogic.gdx.Input as __Input
__Input = __Input
from builtins import float
from abc import abstractmethod, ABC
 
class Input(ABC):
    """com.badlogic.gdx.Input"""
 
    @staticmethod
    def __wrap(java_value: __Input) -> 'Input':
        return Input(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Input):
        """
        Dynamic initializer for Input.
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
 
    @abstractmethod
    def getRotation(self, ):
        """public abstract int com.badlogic.gdx.Input.getRotation()"""
        pass

    @abstractmethod
    def setCatchBackKey(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setCatchBackKey(boolean)"""
        pass

    @abstractmethod
    def getNativeOrientation(self, ):
        """public abstract com.badlogic.gdx.Input$Orientation com.badlogic.gdx.Input.getNativeOrientation()"""
        pass

    @abstractmethod
    def isKeyJustPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isKeyJustPressed(int)"""
        pass

    @abstractmethod
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public abstract void com.badlogic.gdx.Input.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        pass

    @abstractmethod
    def isKeyPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isKeyPressed(int)"""
        pass

    @abstractmethod
    def getDeltaY(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getDeltaY(int)"""
        pass

    @abstractmethod
    def getMaxPointers(self, ):
        """public abstract int com.badlogic.gdx.Input.getMaxPointers()"""
        pass

    @abstractmethod
    def isTouched(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isTouched(int)"""
        pass

    @abstractmethod
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public abstract void com.badlogic.gdx.Input.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def isButtonJustPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isButtonJustPressed(int)"""
        pass

    @abstractmethod
    def getY(self, ):
        """public abstract int com.badlogic.gdx.Input.getY()"""
        pass

    @abstractmethod
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public abstract void com.badlogic.gdx.Input.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        pass

    @abstractmethod
    def getRoll(self, ):
        """public abstract float com.badlogic.gdx.Input.getRoll()"""
        pass

    @abstractmethod
    def getDeltaY(self, ):
        """public abstract int com.badlogic.gdx.Input.getDeltaY()"""
        pass

    @abstractmethod
    def isCatchKey(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isCatchKey(int)"""
        pass

    @abstractmethod
    def getPressure(self, arg0: int):
        """public abstract float com.badlogic.gdx.Input.getPressure(int)"""
        pass

    @abstractmethod
    def setCatchKey(self, arg0: int, arg1: bool):
        """public abstract void com.badlogic.gdx.Input.setCatchKey(int,boolean)"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public abstract void com.badlogic.gdx.Input.vibrate(int,int,boolean)"""
        pass

    @abstractmethod
    def getX(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getX(int)"""
        pass

    @abstractmethod
    def isCursorCatched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isCursorCatched()"""
        pass

    @abstractmethod
    def isPeripheralAvailable(self, arg0: 'Peripheral'):
        """public abstract boolean com.badlogic.gdx.Input.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        pass

    @abstractmethod
    def getRotationMatrix(self, arg0: 'float'):
        """public abstract void com.badlogic.gdx.Input.getRotationMatrix(float[])"""
        pass

    @abstractmethod
    def getGyroscopeY(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeY()"""
        pass

    @abstractmethod
    def getGyroscopeX(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeX()"""
        pass

    @abstractmethod
    def vibrate(self, arg0: 'VibrationType'):
        """public abstract void com.badlogic.gdx.Input.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        pass

    @abstractmethod
    def isCatchBackKey(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isCatchBackKey()"""
        pass

    @abstractmethod
    def getDeltaX(self, ):
        """public abstract int com.badlogic.gdx.Input.getDeltaX()"""
        pass

    @abstractmethod
    def isTouched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isTouched()"""
        pass

    @abstractmethod
    def getPressure(self, ):
        """public abstract float com.badlogic.gdx.Input.getPressure()"""
        pass

    @abstractmethod
    def getPitch(self, ):
        """public abstract float com.badlogic.gdx.Input.getPitch()"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int, arg1: bool):
        """public abstract void com.badlogic.gdx.Input.vibrate(int,boolean)"""
        pass

    @abstractmethod
    def setCursorCatched(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setCursorCatched(boolean)"""
        pass

    @abstractmethod
    def isButtonPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isButtonPressed(int)"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int):
        """public abstract void com.badlogic.gdx.Input.vibrate(int)"""
        pass

    @abstractmethod
    def getAccelerometerX(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerX()"""
        pass

    @abstractmethod
    def getAzimuth(self, ):
        """public abstract float com.badlogic.gdx.Input.getAzimuth()"""
        pass

    @abstractmethod
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public abstract void com.badlogic.gdx.Input.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        pass

    @abstractmethod
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setOnscreenKeyboardVisible(boolean)"""
        pass

    @abstractmethod
    def setCursorPosition(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.Input.setCursorPosition(int,int)"""
        pass

    @abstractmethod
    def isCatchMenuKey(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isCatchMenuKey()"""
        pass

    @abstractmethod
    def getGyroscopeZ(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeZ()"""
        pass

    @abstractmethod
    def getY(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getY(int)"""
        pass

    @abstractmethod
    def getCurrentEventTime(self, ):
        """public abstract long com.badlogic.gdx.Input.getCurrentEventTime()"""
        pass

    @abstractmethod
    def getAccelerometerZ(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerZ()"""
        pass

    @abstractmethod
    def getDeltaX(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getDeltaX(int)"""
        pass

    @abstractmethod
    def justTouched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.justTouched()"""
        pass

    @abstractmethod
    def getInputProcessor(self, ):
        """public abstract com.badlogic.gdx.InputProcessor com.badlogic.gdx.Input.getInputProcessor()"""
        pass

    @abstractmethod
    def getX(self, ):
        """public abstract int com.badlogic.gdx.Input.getX()"""
        pass

    @abstractmethod
    def setCatchMenuKey(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setCatchMenuKey(boolean)"""
        pass

    @abstractmethod
    def getAccelerometerY(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerY()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Net$Protocol
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.Net as __Net_Protocol
__Protocol = __Net_Protocol.Protocol
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Protocol():
    """com.badlogic.gdx.Net.Protocol"""
 
    @staticmethod
    def __wrap(java_value: __Protocol) -> 'Protocol':
        return Protocol(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Protocol):
        """
        Dynamic initializer for Protocol.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Protocol':
        """public static com.badlogic.gdx.Net$Protocol com.badlogic.gdx.Net$Protocol.valueOf(java.lang.String)"""
        return Protocol.__wrap(__Protocol.valueOf(arg0))

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['Protocol']:
        """public static com.badlogic.gdx.Net$Protocol[] com.badlogic.gdx.Net$Protocol.values()"""
        return List[Protocol].__wrap(__Protocol.values())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.Input$Peripheral
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.Input as __Input_Peripheral
__Peripheral = __Input_Peripheral.Peripheral
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Peripheral():
    """com.badlogic.gdx.Input.Peripheral"""
 
    @staticmethod
    def __wrap(java_value: __Peripheral) -> 'Peripheral':
        return Peripheral(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Peripheral):
        """
        Dynamic initializer for Peripheral.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Peripheral':
        """public static com.badlogic.gdx.Input$Peripheral com.badlogic.gdx.Input$Peripheral.valueOf(java.lang.String)"""
        return Peripheral.__wrap(__Peripheral.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['Peripheral']:
        """public static com.badlogic.gdx.Input$Peripheral[] com.badlogic.gdx.Input$Peripheral.values()"""
        return List[Peripheral].__wrap(__Peripheral.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.ApplicationListener
import com.badlogic.gdx.ApplicationListener as __ApplicationListener
__ApplicationListener = __ApplicationListener
from abc import abstractmethod, ABC
 
class ApplicationListener(ABC):
    """com.badlogic.gdx.ApplicationListener"""
 
    @staticmethod
    def __wrap(java_value: __ApplicationListener) -> 'ApplicationListener':
        return ApplicationListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ApplicationListener):
        """
        Dynamic initializer for ApplicationListener.
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
 
    @abstractmethod
    def resize(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.ApplicationListener.resize(int,int)"""
        pass

    @abstractmethod
    def create(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.create()"""
        pass

    @abstractmethod
    def render(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.render()"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.resume()"""
        pass

    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.pause()"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Net$HttpResponseListener
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
import com.badlogic.gdx.Net as __Net_HttpResponseListener
__HttpResponseListener = __Net_HttpResponseListener.HttpResponseListener
 
class HttpResponseListener(ABC):
    """com.badlogic.gdx.Net.HttpResponseListener"""
 
    @staticmethod
    def __wrap(java_value: __HttpResponseListener) -> 'HttpResponseListener':
        return HttpResponseListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpResponseListener):
        """
        Dynamic initializer for HttpResponseListener.
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
 
    @abstractmethod
    def cancelled(self, ):
        """public abstract void com.badlogic.gdx.Net$HttpResponseListener.cancelled()"""
        pass

    @abstractmethod
    def failed(self, arg0: 'Throwable'):
        """public abstract void com.badlogic.gdx.Net$HttpResponseListener.failed(java.lang.Throwable)"""
        pass

    @abstractmethod
    def handleHttpResponse(self, arg0: 'HttpResponse'):
        """public abstract void com.badlogic.gdx.Net$HttpResponseListener.handleHttpResponse(com.badlogic.gdx.Net$HttpResponse)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Version
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.Version as __Version
__Version = __Version
from builtins import bool
from builtins import int
 
class Version():
    """com.badlogic.gdx.Version"""
 
    @staticmethod
    def __wrap(java_value: __Version) -> 'Version':
        return Version(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Version):
        """
        Dynamic initializer for Version.
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

    @staticmethod
    @overload
    def isHigherEqual(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.Version.isHigherEqual(int,int,int)"""
        return bool.__wrap(__Version.isHigherEqual(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Version()"""
        val = __Version()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Version()"""
        val = __Version()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @staticmethod
    @overload
    def isHigher(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.Version.isHigher(int,int,int)"""
        return bool.__wrap(__Version.isHigher(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def isLowerEqual(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.Version.isLowerEqual(int,int,int)"""
        return bool.__wrap(__Version.isLowerEqual(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

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

    @staticmethod
    @overload
    def isLower(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.Version.isLower(int,int,int)"""
        return bool.__wrap(__Version.isLower(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Input$Keys
import com.badlogic.gdx.Input as __Input_Keys
__Keys = __Input_Keys.Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Keys():
    """com.badlogic.gdx.Input.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> int:
        """public static int com.badlogic.gdx.Input$Keys.valueOf(java.lang.String)"""
        return int.__wrap(__Keys.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Input$Keys()"""
        val = __Keys()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Input$Keys()"""
        val = __Keys()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toString(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.Input$Keys.toString(int)"""
        return str.__wrap(__Keys.toString(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Audio
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.Audio as __Audio
__Audio = __Audio
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from abc import abstractmethod, ABC
 
class Audio(ABC):
    """com.badlogic.gdx.Audio"""
 
    @staticmethod
    def __wrap(java_value: __Audio) -> 'Audio':
        return Audio(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Audio):
        """
        Dynamic initializer for Audio.
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
 
    @abstractmethod
    def newMusic(self, arg0: 'FileHandle'):
        """public abstract com.badlogic.gdx.audio.Music com.badlogic.gdx.Audio.newMusic(com.badlogic.gdx.files.FileHandle)"""
        pass

    @abstractmethod
    def getAvailableOutputDevices(self, ):
        """public abstract java.lang.String[] com.badlogic.gdx.Audio.getAvailableOutputDevices()"""
        pass

    @abstractmethod
    def newAudioDevice(self, arg0: int, arg1: bool):
        """public abstract com.badlogic.gdx.audio.AudioDevice com.badlogic.gdx.Audio.newAudioDevice(int,boolean)"""
        pass

    @abstractmethod
    def switchOutputDevice(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Audio.switchOutputDevice(java.lang.String)"""
        pass

    @abstractmethod
    def newSound(self, arg0: 'FileHandle'):
        """public abstract com.badlogic.gdx.audio.Sound com.badlogic.gdx.Audio.newSound(com.badlogic.gdx.files.FileHandle)"""
        pass

    @abstractmethod
    def newAudioRecorder(self, arg0: int, arg1: bool):
        """public abstract com.badlogic.gdx.audio.AudioRecorder com.badlogic.gdx.Audio.newAudioRecorder(int,boolean)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ScreenAdapter
import com.badlogic.gdx.ScreenAdapter as __ScreenAdapter
__ScreenAdapter = __ScreenAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScreenAdapter():
    """com.badlogic.gdx.ScreenAdapter"""
 
    @staticmethod
    def __wrap(java_value: __ScreenAdapter) -> 'ScreenAdapter':
        return ScreenAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScreenAdapter):
        """
        Dynamic initializer for ScreenAdapter.
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
    def dispose(self):
        """public void com.badlogic.gdx.ScreenAdapter.dispose()"""
        super(ScreenAdapter, self).dispose()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ScreenAdapter.resize(int,int)"""
        super(__ScreenAdapter, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hide(self):
        """public void com.badlogic.gdx.ScreenAdapter.hide()"""
        super(ScreenAdapter, self).hide()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def show(self):
        """public void com.badlogic.gdx.ScreenAdapter.show()"""
        super(ScreenAdapter, self).show()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.ScreenAdapter.pause()"""
        super(ScreenAdapter, self).pause()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ScreenAdapter()"""
        val = __ScreenAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ScreenAdapter()"""
        val = __ScreenAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def render(self, arg0: float):
        """public void com.badlogic.gdx.ScreenAdapter.render(float)"""
        super(__ScreenAdapter, self).render(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.ScreenAdapter.resume()"""
        super(ScreenAdapter, self).resume()

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Net
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import net
except ImportError:
    net = __import_once__("pygdx.net")

from abc import abstractmethod, ABC
import com.badlogic.gdx.Net as __Net
__Net = __Net
 
class Net(ABC):
    """com.badlogic.gdx.Net"""
 
    @staticmethod
    def __wrap(java_value: __Net) -> 'Net':
        return Net(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Net):
        """
        Dynamic initializer for Net.
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
 
    @abstractmethod
    def cancelHttpRequest(self, arg0: 'HttpRequest'):
        """public abstract void com.badlogic.gdx.Net.cancelHttpRequest(com.badlogic.gdx.Net$HttpRequest)"""
        pass

    @abstractmethod
    def openURI(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Net.openURI(java.lang.String)"""
        pass

    @abstractmethod
    def sendHttpRequest(self, arg0: 'HttpRequest', arg1: 'HttpResponseListener'):
        """public abstract void com.badlogic.gdx.Net.sendHttpRequest(com.badlogic.gdx.Net$HttpRequest,com.badlogic.gdx.Net$HttpResponseListener)"""
        pass

    @abstractmethod
    def newServerSocket(self, arg0: 'Protocol', arg1: int, arg2: 'ServerSocketHints'):
        """public abstract com.badlogic.gdx.net.ServerSocket com.badlogic.gdx.Net.newServerSocket(com.badlogic.gdx.Net$Protocol,int,com.badlogic.gdx.net.ServerSocketHints)"""
        pass

    @abstractmethod
    def newClientSocket(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'SocketHints'):
        """public abstract com.badlogic.gdx.net.Socket com.badlogic.gdx.Net.newClientSocket(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.SocketHints)"""
        pass

    @abstractmethod
    def newServerSocket(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'ServerSocketHints'):
        """public abstract com.badlogic.gdx.net.ServerSocket com.badlogic.gdx.Net.newServerSocket(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.ServerSocketHints)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Gdx
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.Gdx as __Gdx
__Gdx = __Gdx
from builtins import int
 
class Gdx():
    """com.badlogic.gdx.Gdx"""
 
    @staticmethod
    def __wrap(java_value: __Gdx) -> 'Gdx':
        return Gdx(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Gdx):
        """
        Dynamic initializer for Gdx.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Gdx()"""
        val = __Gdx()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Gdx()"""
        val = __Gdx()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ApplicationAdapter
import com.badlogic.gdx.ApplicationAdapter as __ApplicationAdapter
__ApplicationAdapter = __ApplicationAdapter
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ApplicationAdapter(ABC):
    """com.badlogic.gdx.ApplicationAdapter"""
 
    @staticmethod
    def __wrap(java_value: __ApplicationAdapter) -> 'ApplicationAdapter':
        return ApplicationAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ApplicationAdapter):
        """
        Dynamic initializer for ApplicationAdapter.
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
    def resume(self):
        """public void com.badlogic.gdx.ApplicationAdapter.resume()"""
        super(ApplicationAdapter, self).resume()

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.ApplicationAdapter.render()"""
        super(ApplicationAdapter, self).render()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(ApplicationAdapter, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ApplicationAdapter.resize(int,int)"""
        super(__ApplicationAdapter, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ApplicationAdapter()"""
        val = __ApplicationAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def create(self):
        """public void com.badlogic.gdx.ApplicationAdapter.create()"""
        super(ApplicationAdapter, self).create()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ApplicationAdapter()"""
        val = __ApplicationAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.ApplicationAdapter.pause()"""
        super(ApplicationAdapter, self).pause()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Net$HttpRequest
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import com.badlogic.gdx.Net as __Net_HttpRequest
__HttpRequest = __Net_HttpRequest.HttpRequest
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class HttpRequest():
    """com.badlogic.gdx.Net.HttpRequest"""
 
    @staticmethod
    def __wrap(java_value: __HttpRequest) -> 'HttpRequest':
        return HttpRequest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpRequest):
        """
        Dynamic initializer for HttpRequest.
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

    @overload
    def getContent(self) -> str:
        """public java.lang.String com.badlogic.gdx.Net$HttpRequest.getContent()"""
        return str.__wrap(super(HttpRequest, self).getContent())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getContentStream(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.Net$HttpRequest.getContentStream()"""
        return 'InputStream'.__wrap(super(HttpRequest, self).getContentStream())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getIncludeCredentials(self) -> bool:
        """public boolean com.badlogic.gdx.Net$HttpRequest.getIncludeCredentials()"""
        return bool.__wrap(super(HttpRequest, self).getIncludeCredentials())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getUrl(self) -> str:
        """public java.lang.String com.badlogic.gdx.Net$HttpRequest.getUrl()"""
        return str.__wrap(super(HttpRequest, self).getUrl())

    @overload
    def setUrl(self, arg0: str):
        """public void com.badlogic.gdx.Net$HttpRequest.setUrl(java.lang.String)"""
        super(__HttpRequest, self).setUrl(arg0)

    @overload
    def getHeaders(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> com.badlogic.gdx.Net$HttpRequest.getHeaders()"""
        return 'Map'.__wrap(super(HttpRequest, self).getHeaders())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setContent(self, arg0: str):
        """public void com.badlogic.gdx.Net$HttpRequest.setContent(java.lang.String)"""
        super(__HttpRequest, self).setContent(arg0)

    @overload
    def setHeader(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.Net$HttpRequest.setHeader(java.lang.String,java.lang.String)"""
        super(__HttpRequest, self).setHeader(arg0, arg1)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.Net$HttpRequest.reset()"""
        super(HttpRequest, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getFollowRedirects(self) -> bool:
        """public boolean com.badlogic.gdx.Net$HttpRequest.getFollowRedirects()"""
        return bool.__wrap(super(HttpRequest, self).getFollowRedirects())

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.Net$HttpRequest(java.lang.String)"""
        val = __HttpRequest(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setMethod(self, arg0: str):
        """public void com.badlogic.gdx.Net$HttpRequest.setMethod(java.lang.String)"""
        super(__HttpRequest, self).setMethod(arg0)

    @overload
    def setTimeOut(self, arg0: int):
        """public void com.badlogic.gdx.Net$HttpRequest.setTimeOut(int)"""
        super(__HttpRequest, self).setTimeOut(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getTimeOut(self) -> int:
        """public int com.badlogic.gdx.Net$HttpRequest.getTimeOut()"""
        return int.__wrap(super(HttpRequest, self).getTimeOut())

    @overload
    def setContent(self, arg0: 'InputStream', arg1: int):
        """public void com.badlogic.gdx.Net$HttpRequest.setContent(java.io.InputStream,long)"""
        super(__HttpRequest, self).setContent(arg0, __long.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Net$HttpRequest()"""
        val = __HttpRequest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Net$HttpRequest()"""
        val = __HttpRequest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getContentLength(self) -> int:
        """public long com.badlogic.gdx.Net$HttpRequest.getContentLength()"""
        return int.__wrap(super(HttpRequest, self).getContentLength())

    @overload
    def getMethod(self) -> str:
        """public java.lang.String com.badlogic.gdx.Net$HttpRequest.getMethod()"""
        return str.__wrap(super(HttpRequest, self).getMethod())

    @overload
    def setIncludeCredentials(self, arg0: bool):
        """public void com.badlogic.gdx.Net$HttpRequest.setIncludeCredentials(boolean)"""
        super(__HttpRequest, self).setIncludeCredentials(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setFollowRedirects(self, arg0: bool):
        """public void com.badlogic.gdx.Net$HttpRequest.setFollowRedirects(boolean) throws java.lang.IllegalArgumentException"""
        super(__HttpRequest, self).setFollowRedirects(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Application$ApplicationType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.Application as __Application_ApplicationType
__ApplicationType = __Application_ApplicationType.ApplicationType
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class ApplicationType():
    """com.badlogic.gdx.Application.ApplicationType"""
 
    @staticmethod
    def __wrap(java_value: __ApplicationType) -> 'ApplicationType':
        return ApplicationType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ApplicationType):
        """
        Dynamic initializer for ApplicationType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def values() -> List['ApplicationType']:
        """public static com.badlogic.gdx.Application$ApplicationType[] com.badlogic.gdx.Application$ApplicationType.values()"""
        return List[ApplicationType].__wrap(__ApplicationType.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ApplicationType':
        """public static com.badlogic.gdx.Application$ApplicationType com.badlogic.gdx.Application$ApplicationType.valueOf(java.lang.String)"""
        return ApplicationType.__wrap(__ApplicationType.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.InputAdapter
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.InputAdapter as __InputAdapter
__InputAdapter = __InputAdapter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InputAdapter():
    """com.badlogic.gdx.InputAdapter"""
 
    @staticmethod
    def __wrap(java_value: __InputAdapter) -> 'InputAdapter':
        return InputAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InputAdapter):
        """
        Dynamic initializer for InputAdapter.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.InputAdapter()"""
        val = __InputAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyDown(int)"""
        return bool.__wrap(super(__InputAdapter, self).keyDown(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.scrolled(float,float)"""
        return bool.__wrap(super(__InputAdapter, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__InputAdapter, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool.__wrap(super(__InputAdapter, self).keyTyped(__char.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__InputAdapter, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchDragged(int,int,int)"""
        return bool.__wrap(super(__InputAdapter, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool.__wrap(super(__InputAdapter, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyUp(int)"""
        return bool.__wrap(super(__InputAdapter, self).keyUp(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.InputAdapter()"""
        val = __InputAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__InputAdapter, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Input$OnscreenKeyboardType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.Input as __Input_OnscreenKeyboardType
__OnscreenKeyboardType = __Input_OnscreenKeyboardType.OnscreenKeyboardType
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class OnscreenKeyboardType():
    """com.badlogic.gdx.Input.OnscreenKeyboardType"""
 
    @staticmethod
    def __wrap(java_value: __OnscreenKeyboardType) -> 'OnscreenKeyboardType':
        return OnscreenKeyboardType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OnscreenKeyboardType):
        """
        Dynamic initializer for OnscreenKeyboardType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def values() -> List['OnscreenKeyboardType']:
        """public static com.badlogic.gdx.Input$OnscreenKeyboardType[] com.badlogic.gdx.Input$OnscreenKeyboardType.values()"""
        return List[OnscreenKeyboardType].__wrap(__OnscreenKeyboardType.values())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'OnscreenKeyboardType':
        """public static com.badlogic.gdx.Input$OnscreenKeyboardType com.badlogic.gdx.Input$OnscreenKeyboardType.valueOf(java.lang.String)"""
        return OnscreenKeyboardType.__wrap(__OnscreenKeyboardType.valueOf(arg0))

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.InputEventQueue
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.InputEventQueue as __InputEventQueue
__InputEventQueue = __InputEventQueue
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InputEventQueue():
    """com.badlogic.gdx.InputEventQueue"""
 
    @staticmethod
    def __wrap(java_value: __InputEventQueue) -> 'InputEventQueue':
        return InputEventQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InputEventQueue):
        """
        Dynamic initializer for InputEventQueue.
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

    @overload
    def keyTyped(self, arg0: str, arg1: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.keyTyped(char,long)"""
        return bool.__wrap(super(__InputEventQueue, self).keyTyped(__char.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.touchDragged(int,int,int,long)"""
        return bool.__wrap(super(__InputEventQueue, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.mouseMoved(int,int,long)"""
        return bool.__wrap(super(__InputEventQueue, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def keyDown(self, arg0: int, arg1: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.keyDown(int,long)"""
        return bool.__wrap(super(__InputEventQueue, self).keyDown(__int.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.InputEventQueue()"""
        val = __InputEventQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def drain(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.InputEventQueue.drain(com.badlogic.gdx.InputProcessor)"""
        super(__InputEventQueue, self).drain(arg0)

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.touchUp(int,int,int,int,long)"""
        return bool.__wrap(super(__InputEventQueue, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.touchDown(int,int,int,int,long)"""
        return bool.__wrap(super(__InputEventQueue, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @overload
    def scrolled(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.scrolled(float,float,long)"""
        return bool.__wrap(super(__InputEventQueue, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.InputEventQueue()"""
        val = __InputEventQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getCurrentEventTime(self) -> int:
        """public long com.badlogic.gdx.InputEventQueue.getCurrentEventTime()"""
        return int.__wrap(super(InputEventQueue, self).getCurrentEventTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def keyUp(self, arg0: int, arg1: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.keyUp(int,long)"""
        return bool.__wrap(super(__InputEventQueue, self).keyUp(__int.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))