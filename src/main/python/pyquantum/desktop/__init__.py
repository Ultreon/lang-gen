from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.ModOrigin as _ModOrigin
_ModOrigin = _ModOrigin
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.desktop.FabricMod as _FabricMod
_FabricMod = _FabricMod
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import net.fabricmc.loader.api.ModContainer as ModContainer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FabricMod():
    """dev.ultreon.quantum.desktop.FabricMod"""
 
    @staticmethod
    def _wrap(java_value: _FabricMod) -> 'FabricMod':
        return FabricMod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FabricMod):
        """
        Dynamic initializer for FabricMod.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FabricMod__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FabricMod__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getDescription()"""
        return str._wrap(super(FabricMod, self).getDescription())

    @override
    @overload
    def getAuthors(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.quantum.desktop.FabricMod.getAuthors()"""
        return 'Collection'._wrap(super(FabricMod, self).getAuthors())

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

    @override
    @overload
    def getVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getVersion()"""
        return str._wrap(super(FabricMod, self).getVersion())

    @overload
    def getIconPath(self, arg0: int) -> 'Optional':
        """public java.util.Optional<java.lang.String> dev.ultreon.quantum.desktop.FabricMod.getIconPath(int)"""
        return 'Optional'._wrap(super(_FabricMod, self).getIconPath(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getId()"""
        return str._wrap(super(FabricMod, self).getId())

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

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getName()"""
        return str._wrap(super(FabricMod, self).getName())

    @override
    @overload
    def getRootPaths(self) -> 'Iterable':
        """public java.lang.Iterable<java.nio.file.Path> dev.ultreon.quantum.desktop.FabricMod.getRootPaths()"""
        return 'Iterable'._wrap(super(FabricMod, self).getRootPaths())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ModContainer'):
        """public dev.ultreon.quantum.desktop.FabricMod(net.fabricmc.loader.api.ModContainer)"""
        val = _FabricMod(arg0)
        self.__wrapper = val

    @override
    @overload
    def getOrigin(self) -> 'pyquantum.ModOrigin':
        """public dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.desktop.FabricMod.getOrigin()"""
        return 'pyquantum.ModOrigin'._wrap(super(FabricMod, self).getOrigin())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.desktop.FabricMod
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.ModOrigin as _ModOrigin
_ModOrigin = _ModOrigin
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.desktop.FabricMod as _FabricMod
_FabricMod = _FabricMod
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import net.fabricmc.loader.api.ModContainer as ModContainer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FabricMod():
    """dev.ultreon.quantum.desktop.FabricMod"""
 
    @staticmethod
    def _wrap(java_value: _FabricMod) -> 'FabricMod':
        return FabricMod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FabricMod):
        """
        Dynamic initializer for FabricMod.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FabricMod__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FabricMod__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getDescription()"""
        return str._wrap(super(FabricMod, self).getDescription())

    @override
    @overload
    def getAuthors(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.quantum.desktop.FabricMod.getAuthors()"""
        return 'Collection'._wrap(super(FabricMod, self).getAuthors())

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

    @override
    @overload
    def getVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getVersion()"""
        return str._wrap(super(FabricMod, self).getVersion())

    @overload
    def getIconPath(self, arg0: int) -> 'Optional':
        """public java.util.Optional<java.lang.String> dev.ultreon.quantum.desktop.FabricMod.getIconPath(int)"""
        return 'Optional'._wrap(super(_FabricMod, self).getIconPath(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getId()"""
        return str._wrap(super(FabricMod, self).getId())

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

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.desktop.FabricMod.getName()"""
        return str._wrap(super(FabricMod, self).getName())

    @override
    @overload
    def getRootPaths(self) -> 'Iterable':
        """public java.lang.Iterable<java.nio.file.Path> dev.ultreon.quantum.desktop.FabricMod.getRootPaths()"""
        return 'Iterable'._wrap(super(FabricMod, self).getRootPaths())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ModContainer'):
        """public dev.ultreon.quantum.desktop.FabricMod(net.fabricmc.loader.api.ModContainer)"""
        val = _FabricMod(arg0)
        self.__wrapper = val

    @override
    @overload
    def getOrigin(self) -> 'pyquantum.ModOrigin':
        """public dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.desktop.FabricMod.getOrigin()"""
        return 'pyquantum.ModOrigin'._wrap(super(FabricMod, self).getOrigin())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.desktop.FabricMod 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopLauncher
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.desktop.DesktopLauncher as _DesktopLauncher
_DesktopLauncher = _DesktopLauncher
import dev.ultreon.quantum.desktop.DesktopPlatform as _DesktopPlatform
_DesktopPlatform = _DesktopPlatform
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DesktopLauncher():
    """dev.ultreon.quantum.desktop.DesktopLauncher"""
 
    @staticmethod
    def _wrap(java_value: _DesktopLauncher) -> 'DesktopLauncher':
        return DesktopLauncher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DesktopLauncher):
        """
        Dynamic initializer for DesktopLauncher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DesktopLauncher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DesktopLauncher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.DesktopLauncher()"""
        val = _DesktopLauncher()
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

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.desktop.DesktopLauncher.main(java.lang.String[])"""
        _DesktopLauncher.main(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.DesktopLauncher()"""
        val = _DesktopLauncher()
        self.__wrapper = val

    @staticmethod
    @overload
    def getPlatform() -> 'DesktopPlatform':
        """public static dev.ultreon.quantum.desktop.DesktopPlatform dev.ultreon.quantum.desktop.DesktopLauncher.getPlatform()"""
        return DesktopPlatform._wrap(_DesktopLauncher.getPlatform())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopPlatform
from pyquantum_helper import import_once as _import_once
import org.mozilla.javascript.Context as Context
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import dev.ultreon.quantum.desktop.DesktopPlatform as _DesktopPlatform
_DesktopPlatform = _DesktopPlatform
from abc import abstractmethod, ABC
import dev.ultreon.quantum.util.Env as _Env
_Env = _Env
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.DeviceType as _DeviceType
_DeviceType = _DeviceType
import java.util.Optional as _Optional
_Optional = _Optional
from builtins import bool
import dev.ultreon.quantum.GamePlatform as _GamePlatform
_GamePlatform = _GamePlatform
from builtins import str
import org.mozilla.javascript.Context as _Context
_Context = _Context
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.lang.Integer as _int
import java.util.Optional as Optional
import java.lang.Long as _long
import dev.ultreon.quantum.log.Logger as _Logger
_Logger = _Logger
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DesktopPlatform():
    """dev.ultreon.quantum.desktop.DesktopPlatform"""
 
    @staticmethod
    def _wrap(java_value: _DesktopPlatform) -> 'DesktopPlatform':
        return DesktopPlatform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DesktopPlatform):
        """
        Dynamic initializer for DesktopPlatform.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DesktopPlatform__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DesktopPlatform__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.close()"""
        super(DesktopPlatform, self).close()

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
    def invokeEntrypoint(self, arg0: str, arg1: 'Class', arg2: 'Consumer'):
        """public <T> void dev.ultreon.quantum.desktop.DesktopPlatform.invokeEntrypoint(java.lang.String,java.lang.Class<T>,java.util.function.Consumer<T>)"""
        super(_DesktopPlatform, self).invokeEntrypoint(arg0, arg1, arg2)

    @override
    @overload
    def isMouseCaptured(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isMouseCaptured()"""
        return bool._wrap(super(DesktopPlatform, self).isMouseCaptured())

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
    def enterXeoxContext(self) -> 'Context':
        """public org.mozilla.javascript.Context dev.ultreon.quantum.GamePlatform.enterXeoxContext()"""
        return 'Context'._wrap(super(pyquantum.GamePlatform, self).enterXeoxContext())

    @override
    @overload
    def isLinux(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isLinux()"""
        return bool._wrap(super(DesktopPlatform, self).isLinux())

    @override
    @overload
    def isWindows(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isWindows()"""
        return bool._wrap(super(DesktopPlatform, self).isWindows())

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
    def isDevEnvironment(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isDevEnvironment()"""
        return bool._wrap(super(DesktopPlatform, self).isDevEnvironment())

    @override
    @overload
    def isMacOSX(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isMacOSX()"""
        return bool._wrap(super(DesktopPlatform, self).isMacOSX())

    @abstractmethod
    def getGameDevices(self, ):
        """public abstract java.util.Collection<dev.ultreon.quantum.platform.Device> dev.ultreon.quantum.GamePlatform.getGameDevices()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def get() -> 'pyquantum.GamePlatform':
        """public static dev.ultreon.quantum.GamePlatform dev.ultreon.quantum.GamePlatform.get()"""
        return pyquantum.GamePlatform._wrap(_GamePlatform.get())

    @override
    @overload
    def setMouseCaptured(self, arg0: bool):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setMouseCaptured(boolean)"""
        super(_DesktopPlatform, self).setMouseCaptured(_boolean.valueOf(arg0))

    @override
    @overload
    def showRenderPipeline(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.showRenderPipeline()"""
        return bool._wrap(super(DesktopPlatform, self).showRenderPipeline())

    @override
    @overload
    def requestAttention(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.requestAttention()"""
        super(DesktopPlatform, self).requestAttention()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getConfigDir(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.desktop.DesktopPlatform.getConfigDir()"""
        return 'Path'._wrap(super(DesktopPlatform, self).getConfigDir())

    @override
    @overload
    def setShowingImGui(self, arg0: bool):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setShowingImGui(boolean)"""
        super(_DesktopPlatform, self).setShowingImGui(_boolean.valueOf(arg0))

    @override
    @overload
    def areChunkBordersVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.areChunkBordersVisible()"""
        return bool._wrap(super(DesktopPlatform, self).areChunkBordersVisible())

    @override
    @overload
    def openImportDialog(self) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Boolean> dev.ultreon.quantum.desktop.DesktopPlatform.openImportDialog()"""
        return 'util.Result'._wrap(super(DesktopPlatform, self).openImportDialog())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isDesktop(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isDesktop()"""
        return bool._wrap(super(DesktopPlatform, self).isDesktop())

    @override
    @overload
    def isMobile(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isMobile()"""
        return bool._wrap(super(pyquantum.GamePlatform, self).isMobile())

    @overload
    def isModLoaded(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isModLoaded(java.lang.String)"""
        return bool._wrap(super(_DesktopPlatform, self).isModLoaded(arg0))

    @abstractmethod
    def createWindow(self, ):
        """public abstract dev.ultreon.quantum.GameWindow dev.ultreon.quantum.desktop.DesktopPlatform.createWindow()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @abstractmethod
    def getMouseDevice(self, ):
        """public abstract dev.ultreon.quantum.platform.MouseDevice dev.ultreon.quantum.GamePlatform.getMouseDevice()"""
        pass

    @override
    @overload
    def preInitImGui(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.preInitImGui()"""
        super(DesktopPlatform, self).preInitImGui()

    @override
    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setCursorPosition(int,int)"""
        super(_DesktopPlatform, self).setCursorPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getMods(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.Mod> dev.ultreon.quantum.desktop.DesktopPlatform.getMods()"""
        return 'Collection'._wrap(super(DesktopPlatform, self).getMods())

    @override
    @overload
    def hasCompass(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.hasCompass()"""
        return bool._wrap(super(pyquantum.GamePlatform, self).hasCompass())

    @overload
    def getMod(self, arg0: str) -> 'Optional':
        """public java.util.Optional<dev.ultreon.quantum.Mod> dev.ultreon.quantum.desktop.DesktopPlatform.getMod(java.lang.String)"""
        return 'Optional'._wrap(super(_DesktopPlatform, self).getMod(arg0))

    @override
    @overload
    def launch(self, arg0: 'String'):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.launch(java.lang.String[])"""
        super(_DesktopPlatform, self).launch(arg0)

    @override
    @overload
    def onGameDispose(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.onGameDispose()"""
        super(DesktopPlatform, self).onGameDispose()

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.setVisible(boolean)"""
        super(_DesktopPlatform, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getEnv(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.desktop.DesktopPlatform.getEnv()"""
        return 'util.Env'._wrap(super(DesktopPlatform, self).getEnv())

    @override
    @overload
    def getDeviceType(self) -> 'pyquantum.DeviceType':
        """public dev.ultreon.quantum.DeviceType dev.ultreon.quantum.desktop.DesktopPlatform.getDeviceType()"""
        return 'pyquantum.DeviceType'._wrap(super(DesktopPlatform, self).getDeviceType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isShowingImGui(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.isShowingImGui()"""
        return bool._wrap(super(DesktopPlatform, self).isShowingImGui())

    @overload
    def getLogger(self, arg0: str) -> 'log.Logger':
        """public dev.ultreon.quantum.log.Logger dev.ultreon.quantum.desktop.DesktopPlatform.getLogger(java.lang.String)"""
        return 'log.Logger'._wrap(super(_DesktopPlatform, self).getLogger(arg0))

    @override
    @overload
    def detectDebug(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopPlatform.detectDebug()"""
        return bool._wrap(super(DesktopPlatform, self).detectDebug())

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
    def renderImGui(self):
        """public void dev.ultreon.quantum.desktop.DesktopPlatform.renderImGui()"""
        super(DesktopPlatform, self).renderImGui()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getGameDir(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.desktop.DesktopPlatform.getGameDir()"""
        return 'Path'._wrap(super(DesktopPlatform, self).getGameDir()) 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopWindow
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
    from pygdx.backends import lwjgl3
except ImportError:
    lwjgl3 = _import_once("pygdx.backends.lwjgl3")

import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.GameWindow as _GameWindow
_GameWindow = _GameWindow
import dev.ultreon.quantum.desktop.DesktopWindow as _DesktopWindow
_DesktopWindow = _DesktopWindow
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DesktopWindow():
    """dev.ultreon.quantum.desktop.DesktopWindow"""
 
    @staticmethod
    def _wrap(java_value: _DesktopWindow) -> 'DesktopWindow':
        return DesktopWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DesktopWindow):
        """
        Dynamic initializer for DesktopWindow.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DesktopWindow__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DesktopWindow__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def restore(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.restore()"""
        super(DesktopWindow, self).restore()

    @override
    @overload
    def isMaximized(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopWindow.isMaximized()"""
        return bool._wrap(super(DesktopWindow, self).isMaximized())

    @overload
    def __init__(self, arg0: 'Lwjgl3Window'):
        """public dev.ultreon.quantum.desktop.DesktopWindow(com.badlogic.gdx.backends.lwjgl3.Lwjgl3Window)"""
        val = _DesktopWindow(arg0)
        self.__wrapper = val

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
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopWindow.isFocused()"""
        return bool._wrap(super(DesktopWindow, self).isFocused())

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
    def focus(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.focus()"""
        super(DesktopWindow, self).focus()

    @override
    @overload
    def isMinimized(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopWindow.isMinimized()"""
        return bool._wrap(super(DesktopWindow, self).isMinimized())

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.desktop.DesktopWindow.isHovered()"""
        return bool._wrap(super(DesktopWindow, self).isHovered())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def minimize(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.minimize()"""
        super(DesktopWindow, self).minimize()

    @override
    @overload
    def maximize(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.maximize()"""
        super(DesktopWindow, self).maximize()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getHandle(self) -> int:
        """public long dev.ultreon.quantum.desktop.DesktopWindow.getHandle()"""
        return int._wrap(super(DesktopWindow, self).getHandle())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isResizable(self) -> bool:
        """public boolean dev.ultreon.quantum.GameWindow.isResizable()"""
        return bool._wrap(super(pyquantum.GameWindow, self).isResizable())

    @override
    @overload
    def requestAttention(self):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.requestAttention()"""
        super(DesktopWindow, self).requestAttention()

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void dev.ultreon.quantum.desktop.DesktopWindow.setResizable(boolean)"""
        super(_DesktopWindow, self).setResizable(_boolean.valueOf(arg0))

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

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void dev.ultreon.quantum.GameWindow.setTitle(java.lang.String)"""
        super(_pyquantum.GameWindow, self).setTitle(arg0)

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setVisible(boolean)"""
        super(_pyquantum.GameWindow, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())