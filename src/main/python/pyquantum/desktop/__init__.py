from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.desktop.FabricMod as __FabricMod
__FabricMod = __FabricMod
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.ModOrigin as __ModOrigin
__ModOrigin = __ModOrigin
import java.lang.Integer as __int
import net.fabricmc.loader.api.ModContainer as ModContainer
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class FabricMod():
    """dev.ultreon.quantum.desktop.FabricMod"""
 
    @staticmethod
    def __wrap(java_value: __FabricMod) -> 'FabricMod':
        return FabricMod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FabricMod):
        """
        Dynamic initializer for FabricMod.
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
    def getVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getVersion()"""
        return str.__wrap(super(FabricMod, self).getVersion())

    @override
    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getId()"""
        return str.__wrap(super(FabricMod, self).getId())

    @override
    @overload
    def getAuthors(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.quantum.desktop.FabricMod.getAuthors()"""
        return 'Collection'.__wrap(super(FabricMod, self).getAuthors())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getName()"""
        return str.__wrap(super(FabricMod, self).getName())

    @override
    @overload
    def getOrigin(self) -> 'pyquantum.ModOrigin':
        """public dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.desktop.FabricMod.getOrigin()"""
        return 'pyquantum.ModOrigin'.__wrap(super(FabricMod, self).getOrigin())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRootPaths(self) -> 'Iterable':
        """public java.lang.Iterable<java.nio.file.Path> dev.ultreon.quantum.desktop.FabricMod.getRootPaths()"""
        return 'Iterable'.__wrap(super(FabricMod, self).getRootPaths())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ModContainer'):
        """public dev.ultreon.quantum.desktop.FabricMod(net.fabricmc.loader.api.ModContainer)"""
        val = __FabricMod(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getIconPath(self, arg0: int) -> 'Optional':
        """public java.util.Optional<java.lang.String> dev.ultreon.quantum.desktop.FabricMod.getIconPath(int)"""
        return 'Optional'.__wrap(super(__FabricMod, self).getIconPath(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getDescription()"""
        return str.__wrap(super(FabricMod, self).getDescription())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.desktop.FabricMod
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.desktop.FabricMod as __FabricMod
__FabricMod = __FabricMod
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.ModOrigin as __ModOrigin
__ModOrigin = __ModOrigin
import java.lang.Integer as __int
import net.fabricmc.loader.api.ModContainer as ModContainer
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class FabricMod():
    """dev.ultreon.quantum.desktop.FabricMod"""
 
    @staticmethod
    def __wrap(java_value: __FabricMod) -> 'FabricMod':
        return FabricMod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FabricMod):
        """
        Dynamic initializer for FabricMod.
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
    def getVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getVersion()"""
        return str.__wrap(super(FabricMod, self).getVersion())

    @override
    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getId()"""
        return str.__wrap(super(FabricMod, self).getId())

    @override
    @overload
    def getAuthors(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.quantum.desktop.FabricMod.getAuthors()"""
        return 'Collection'.__wrap(super(FabricMod, self).getAuthors())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getName()"""
        return str.__wrap(super(FabricMod, self).getName())

    @override
    @overload
    def getOrigin(self) -> 'pyquantum.ModOrigin':
        """public dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.desktop.FabricMod.getOrigin()"""
        return 'pyquantum.ModOrigin'.__wrap(super(FabricMod, self).getOrigin())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRootPaths(self) -> 'Iterable':
        """public java.lang.Iterable<java.nio.file.Path> dev.ultreon.quantum.desktop.FabricMod.getRootPaths()"""
        return 'Iterable'.__wrap(super(FabricMod, self).getRootPaths())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ModContainer'):
        """public dev.ultreon.quantum.desktop.FabricMod(net.fabricmc.loader.api.ModContainer)"""
        val = __FabricMod(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getIconPath(self, arg0: int) -> 'Optional':
        """public java.util.Optional<java.lang.String> dev.ultreon.quantum.desktop.FabricMod.getIconPath(int)"""
        return 'Optional'.__wrap(super(__FabricMod, self).getIconPath(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getDescription()"""
        return str.__wrap(super(FabricMod, self).getDescription())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.desktop.FabricMod 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopLauncher
from builtins import str
import dev.ultreon.quantum.desktop.DesktopLauncher as __DesktopLauncher
__DesktopLauncher = __DesktopLauncher
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.desktop.DesktopPlatform as __DesktopPlatform
__DesktopPlatform = __DesktopPlatform
from builtins import type
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
 
class DesktopLauncher():
    """dev.ultreon.quantum.desktop.DesktopLauncher"""
 
    @staticmethod
    def __wrap(java_value: __DesktopLauncher) -> 'DesktopLauncher':
        return DesktopLauncher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DesktopLauncher):
        """
        Dynamic initializer for DesktopLauncher.
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
    def getPlatform() -> 'DesktopPlatform':
        """public static dev.ultreon.quantum.desktop.DesktopPlatform dev.ultreon.quantum.desktop.DesktopLauncher.getPlatform()"""
        return DesktopPlatform.__wrap(__DesktopLauncher.getPlatform())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.desktop.DesktopLauncher.main(java.lang.String[])"""
        __DesktopLauncher.main(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.DesktopLauncher()"""
        val = __DesktopLauncher()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.DesktopLauncher()"""
        val = __DesktopLauncher()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopPlatform
from pyquantum_helper import import_once as __import_once__
import org.mozilla.javascript.Context as Context
import java.lang.Boolean as __boolean
import dev.ultreon.quantum.desktop.DesktopPlatform as __DesktopPlatform
__DesktopPlatform = __DesktopPlatform
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import dev.ultreon.quantum.GamePlatform as __GamePlatform
__GamePlatform = __GamePlatform
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import org.mozilla.javascript.Context as __Context
__Context = __Context
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
import java.util.Optional as __Optional
__Optional = __Optional
import java.nio.file.Path as Path
import dev.ultreon.quantum.util.Env as __Env
__Env = __Env
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

import dev.ultreon.quantum.DeviceType as __DeviceType
__DeviceType = __DeviceType
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.log.Logger as __Logger
__Logger = __Logger
import java.lang.Integer as __int
from builtins import int
 
class DesktopPlatform(ABC):
    """dev.ultreon.quantum.desktop.DesktopPlatform"""
 
    @staticmethod
    def __wrap(java_value: __DesktopPlatform) -> 'DesktopPlatform':
        return DesktopPlatform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DesktopPlatform):
        """
        Dynamic initializer for DesktopPlatform.
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
    def invokeEntrypoint(self, arg0: str, arg1: 'Class', arg2: 'Consumer'):
        """public <T> void dev.ultreon.quantum.desktop.DesktopPlatform.invokeEntrypoint(java.lang.String,java.lang.Class<T>,java.util.function.Consumer<T>)"""
        super(__DesktopPlatform, self).invokeEntrypoint(arg0, arg1, arg2)

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.close()"""
        super(DesktopPlatform, self).close()

    @override
    @overload
    def isWindows(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isWindows()"""
        return bool.__wrap(super(DesktopPlatform, self).isWindows())

    @override
    @overload
    def locateResources(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.locateResources()"""
        super(DesktopPlatform, self).locateResources()

    @override
    @overload
    def locateModResources(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.locateModResources()"""
        super(DesktopPlatform, self).locateModResources()

    @override
    @overload
    def setupImGui(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setupImGui()"""
        super(DesktopPlatform, self).setupImGui()

    @override
    @overload
    def getDeviceType(self) -> 'pyquantum.DeviceType':
        """public dev.ultreon.quantum.DeviceType dev.ultreon.quantum.desktop.DesktopPlatform.getDeviceType()"""
        return 'pyquantum.DeviceType'.__wrap(super(DesktopPlatform, self).getDeviceType())

    @override
    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setCursorPosition(int,int)"""
        super(__DesktopPlatform, self).setCursorPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hasCompass(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.hasCompass()"""
        return bool.__wrap(super(pyquantum.GamePlatform, self).hasCompass())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onFirstRender(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.onFirstRender()"""
        super(DesktopPlatform, self).onFirstRender()

    @override
    @overload
    def showRenderPipeline(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.showRenderPipeline()"""
        return bool.__wrap(super(DesktopPlatform, self).showRenderPipeline())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setVisible(boolean)"""
        super(__DesktopPlatform, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def areChunkBordersVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.areChunkBordersVisible()"""
        return bool.__wrap(super(DesktopPlatform, self).areChunkBordersVisible())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def getGameDevices(self, ):
        """public abstract java.util.Collection<dev.ultreon.quantum.platform.Device> dev.ultreon.quantum.GamePlatform.getGameDevices()"""
        pass

    @staticmethod
    @overload
    def get() -> 'pyquantum.GamePlatform':
        """public static dev.ultreon.quantum.GamePlatform dev.ultreon.quantum.GamePlatform.get()"""
        return pyquantum.GamePlatform.__wrap(__GamePlatform.get())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getMod(self, arg0: str) -> 'Optional':
        """public java.util.Optional<dev.ultreon.quantum.Mod> dev.ultreon.quantum.desktop.DesktopPlatform.getMod(java.lang.String)"""
        return 'Optional'.__wrap(super(__DesktopPlatform, self).getMod(arg0))

    @override
    @overload
    def isMouseCaptured(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isMouseCaptured()"""
        return bool.__wrap(super(DesktopPlatform, self).isMouseCaptured())

    @override
    @overload
    def requestAttention(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.requestAttention()"""
        super(DesktopPlatform, self).requestAttention()

    @overload
    def getLogger(self, arg0: str) -> 'log.Logger':
        """public dev.ultreon.quantum.log.Logger dev.ultreon.quantum.desktop.DesktopPlatform.getLogger(java.lang.String)"""
        return 'log.Logger'.__wrap(super(__DesktopPlatform, self).getLogger(arg0))

    @override
    @overload
    def isMobile(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isMobile()"""
        return bool.__wrap(super(pyquantum.GamePlatform, self).isMobile())

    @overload
    def isModLoaded(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isModLoaded(java.lang.String)"""
        return bool.__wrap(super(__DesktopPlatform, self).isModLoaded(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMods(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.Mod> dev.ultreon.quantum.desktop.DesktopPlatform.getMods()"""
        return 'Collection'.__wrap(super(DesktopPlatform, self).getMods())

    @override
    @overload
    def setShowingImGui(self, arg0: bool):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setShowingImGui(boolean)"""
        super(__DesktopPlatform, self).setShowingImGui(__boolean.valueOf(arg0))

    @abstractmethod
    def createWindow(self, ):
        """public abstract dev.ultreon.quantum.GameWindow dev.ultreon.quantum.desktop.DesktopPlatform.createWindow()"""
        pass

    @abstractmethod
    def getMouseDevice(self, ):
        """public abstract dev.ultreon.quantum.platform.MouseDevice dev.ultreon.quantum.GamePlatform.getMouseDevice()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def enterXeoxContext(self) -> 'Context':
        """public org.mozilla.javascript.Context dev.ultreon.quantum.GamePlatform.enterXeoxContext()"""
        return 'Context'.__wrap(super(pyquantum.GamePlatform, self).enterXeoxContext())

    @override
    @overload
    def isLinux(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isLinux()"""
        return bool.__wrap(super(DesktopPlatform, self).isLinux())

    @override
    @overload
    def isMacOSX(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isMacOSX()"""
        return bool.__wrap(super(DesktopPlatform, self).isMacOSX())

    @override
    @overload
    def preInitImGui(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.preInitImGui()"""
        super(DesktopPlatform, self).preInitImGui()

    @override
    @overload
    def isDevEnvironment(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isDevEnvironment()"""
        return bool.__wrap(super(DesktopPlatform, self).isDevEnvironment())

    @override
    @overload
    def isDesktop(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isDesktop()"""
        return bool.__wrap(super(DesktopPlatform, self).isDesktop())

    @override
    @overload
    def getConfigDir(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.desktop.DesktopPlatform.getConfigDir()"""
        return 'Path'.__wrap(super(DesktopPlatform, self).getConfigDir())

    @override
    @overload
    def getEnv(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.desktop.DesktopPlatform.getEnv()"""
        return 'util.Env'.__wrap(super(DesktopPlatform, self).getEnv())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def onGameDispose(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.onGameDispose()"""
        super(DesktopPlatform, self).onGameDispose()

    @override
    @overload
    def openImportDialog(self) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Boolean> dev.ultreon.quantum.desktop.DesktopPlatform.openImportDialog()"""
        return 'util.Result'.__wrap(super(DesktopPlatform, self).openImportDialog())

    @override
    @overload
    def detectDebug(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.detectDebug()"""
        return bool.__wrap(super(DesktopPlatform, self).detectDebug())

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
    def launch(self, arg0: 'String'):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.launch(java.lang.String[])"""
        super(__DesktopPlatform, self).launch(arg0)

    @override
    @overload
    def setupMacOSX(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setupMacOSX()"""
        super(DesktopPlatform, self).setupMacOSX()

    @override
    @overload
    def prepare(self):
        """public void dev.ultreon.quantum.GamePlatform.prepare()"""
        super(pyquantum.GamePlatform, self).prepare()

    @override
    @overload
    def isShowingImGui(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isShowingImGui()"""
        return bool.__wrap(super(DesktopPlatform, self).isShowingImGui())

    @override
    @overload
    def setMouseCaptured(self, arg0: bool):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setMouseCaptured(boolean)"""
        super(__DesktopPlatform, self).setMouseCaptured(__boolean.valueOf(arg0))

    @override
    @overload
    def renderImGui(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.renderImGui()"""
        super(DesktopPlatform, self).renderImGui()

    @override
    @overload
    def getGameDir(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.desktop.DesktopPlatform.getGameDir()"""
        return 'Path'.__wrap(super(DesktopPlatform, self).getGameDir()) 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopWindow
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.backends import lwjgl3
except ImportError:
    lwjgl3 = __import_once__("pygdx.backends.lwjgl3")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.desktop.DesktopWindow as __DesktopWindow
__DesktopWindow = __DesktopWindow
import dev.ultreon.quantum.GameWindow as __GameWindow
__GameWindow = __GameWindow
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DesktopWindow():
    """dev.ultreon.quantum.desktop.DesktopWindow"""
 
    @staticmethod
    def __wrap(java_value: __DesktopWindow) -> 'DesktopWindow':
        return DesktopWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DesktopWindow):
        """
        Dynamic initializer for DesktopWindow.
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
    def isMaximized(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopWindow.isMaximized()"""
        return bool.__wrap(super(DesktopWindow, self).isMaximized())

    @override
    @overload
    def restore(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.restore()"""
        super(DesktopWindow, self).restore()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setVisible(boolean)"""
        super(__pyquantum.GameWindow, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.close()"""
        super(DesktopWindow, self).close()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isMinimized(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopWindow.isMinimized()"""
        return bool.__wrap(super(DesktopWindow, self).isMinimized())

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void dev.ultreon.quantum.GameWindow.setTitle(java.lang.String)"""
        super(__pyquantum.GameWindow, self).setTitle(arg0)

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
    def focus(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.focus()"""
        super(DesktopWindow, self).focus()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def minimize(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.minimize()"""
        super(DesktopWindow, self).minimize()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def maximize(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.maximize()"""
        super(DesktopWindow, self).maximize()

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.setResizable(boolean)"""
        super(__DesktopWindow, self).setResizable(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Lwjgl3Window'):
        """public dev.ultreon.quantum.desktop.DesktopWindow(com.badlogic.gdx.backends.lwjgl3.Lwjgl3Window)"""
        val = __DesktopWindow(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getHandle(self) -> int:
        """public long dev.ultreon.quantum.desktop.DesktopWindow.getHandle()"""
        return int.__wrap(super(DesktopWindow, self).getHandle())

    @override
    @overload
    def requestAttention(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.requestAttention()"""
        super(DesktopWindow, self).requestAttention()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopWindow.isHovered()"""
        return bool.__wrap(super(DesktopWindow, self).isHovered())

    @override
    @overload
    def isResizable(self) -> bool:
        """public boolean dev.ultreon.quantum.GameWindow.isResizable()"""
        return bool.__wrap(super(pyquantum.GameWindow, self).isResizable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopWindow.isFocused()"""
        return bool.__wrap(super(DesktopWindow, self).isFocused())