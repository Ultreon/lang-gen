from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import dev.ultreon.quantum.DeviceType as _DeviceType
_DeviceType = _DeviceType
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeviceType():
    """dev.ultreon.quantum.DeviceType"""
 
    @staticmethod
    def _wrap(java_value: _DeviceType) -> 'DeviceType':
        return DeviceType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeviceType):
        """
        Dynamic initializer for DeviceType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeviceType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeviceType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['DeviceType']:
        """public static dev.ultreon.quantum.DeviceType[] dev.ultreon.quantum.DeviceType.values()"""
        return List[DeviceType]._wrap(_DeviceType.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DeviceType':
        """public static dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.valueOf(java.lang.String)"""
        return DeviceType._wrap(_DeviceType.valueOf(arg0))


DeviceType.AUTOMOBILE = DeviceType._wrap(_AUTOMOBILE.AUTOMOBILE)

DeviceType.VR_HEADSET = DeviceType._wrap(_VR_HEADSET.VR_HEADSET)

DeviceType.APPLIANCE = DeviceType._wrap(_APPLIANCE.APPLIANCE)

DeviceType.TV = DeviceType._wrap(_TV.TV)

DeviceType.WATCH = DeviceType._wrap(_WATCH.WATCH)

DeviceType.DESKTOP = DeviceType._wrap(_DESKTOP.DESKTOP)

DeviceType.MOBILE = DeviceType._wrap(_MOBILE.MOBILE)

DeviceType.TABLET = DeviceType._wrap(_TABLET.TABLET)

DeviceType.OTHER = DeviceType._wrap(_OTHER.OTHER)

 
 
 
# CLASS: dev.ultreon.quantum.DeviceType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import dev.ultreon.quantum.DeviceType as _DeviceType
_DeviceType = _DeviceType
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeviceType():
    """dev.ultreon.quantum.DeviceType"""
 
    @staticmethod
    def _wrap(java_value: _DeviceType) -> 'DeviceType':
        return DeviceType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeviceType):
        """
        Dynamic initializer for DeviceType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeviceType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeviceType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['DeviceType']:
        """public static dev.ultreon.quantum.DeviceType[] dev.ultreon.quantum.DeviceType.values()"""
        return List[DeviceType]._wrap(_DeviceType.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DeviceType':
        """public static dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.valueOf(java.lang.String)"""
        return DeviceType._wrap(_DeviceType.valueOf(arg0))


DeviceType.AUTOMOBILE = DeviceType._wrap(_AUTOMOBILE.AUTOMOBILE)

DeviceType.VR_HEADSET = DeviceType._wrap(_VR_HEADSET.VR_HEADSET)

DeviceType.APPLIANCE = DeviceType._wrap(_APPLIANCE.APPLIANCE)

DeviceType.TV = DeviceType._wrap(_TV.TV)

DeviceType.WATCH = DeviceType._wrap(_WATCH.WATCH)

DeviceType.DESKTOP = DeviceType._wrap(_DESKTOP.DESKTOP)

DeviceType.MOBILE = DeviceType._wrap(_MOBILE.MOBILE)

DeviceType.TABLET = DeviceType._wrap(_TABLET.TABLET)

DeviceType.OTHER = DeviceType._wrap(_OTHER.OTHER)

 
 
 
# CLASS: dev.ultreon.quantum.DeviceType 
 
 
# CLASS: dev.ultreon.quantum.GamePlatform
from pyquantum_helper import import_once as _import_once
import org.mozilla.javascript.Context as Context
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import dev.ultreon.quantum.util.Env as _Env
_Env = _Env
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.GameWindow as _GameWindow
_GameWindow = _GameWindow
import java.util.Optional as _Optional
_Optional = _Optional
import dev.ultreon.quantum.GamePlatform as _GamePlatform
_GamePlatform = _GamePlatform
from builtins import bool
from builtins import str
import org.mozilla.javascript.Context as _Context
_Context = _Context
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
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
 
class GamePlatform():
    """dev.ultreon.quantum.GamePlatform"""
 
    @staticmethod
    def _wrap(java_value: _GamePlatform) -> 'GamePlatform':
        return GamePlatform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GamePlatform):
        """
        Dynamic initializer for GamePlatform.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GamePlatform__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GamePlatform__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isLinux(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isLinux()"""
        return bool._wrap(super(GamePlatform, self).isLinux())

    @overload
    def areChunkBordersVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.areChunkBordersVisible()"""
        return bool._wrap(super(GamePlatform, self).areChunkBordersVisible())

    @overload
    def isWindows(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isWindows()"""
        return bool._wrap(super(GamePlatform, self).isWindows())

    @overload
    def prepare(self):
        """public void dev.ultreon.quantum.GamePlatform.prepare()"""
        super(GamePlatform, self).prepare()

    @overload
    def enterXeoxContext(self) -> 'Context':
        """public org.mozilla.javascript.Context dev.ultreon.quantum.GamePlatform.enterXeoxContext()"""
        return 'Context'._wrap(super(GamePlatform, self).enterXeoxContext())

    @abstractmethod
    def isMouseCaptured(self, ):
        """public abstract boolean dev.ultreon.quantum.GamePlatform.isMouseCaptured()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def hasCompass(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.hasCompass()"""
        return bool._wrap(super(GamePlatform, self).hasCompass())

    @abstractmethod
    def setMouseCaptured(self, arg0: bool):
        """public abstract void dev.ultreon.quantum.GamePlatform.setMouseCaptured(boolean)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getLogger(self, arg0: str) -> 'log.Logger':
        """public dev.ultreon.quantum.log.Logger dev.ultreon.quantum.GamePlatform.getLogger(java.lang.String)"""
        return 'log.Logger'._wrap(super(_GamePlatform, self).getLogger(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def locateResources(self):
        """public void dev.ultreon.quantum.GamePlatform.locateResources()"""
        super(GamePlatform, self).locateResources()

    @overload
    def setShowingImGui(self, arg0: bool):
        """public void dev.ultreon.quantum.GamePlatform.setShowingImGui(boolean)"""
        super(_GamePlatform, self).setShowingImGui(_boolean.valueOf(arg0))

    @overload
    def setupMacOSX(self):
        """public void dev.ultreon.quantum.GamePlatform.setupMacOSX()"""
        super(GamePlatform, self).setupMacOSX()

    @abstractmethod
    def getGameDevices(self, ):
        """public abstract java.util.Collection<dev.ultreon.quantum.platform.Device> dev.ultreon.quantum.GamePlatform.getGameDevices()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def requestAttention(self):
        """public void dev.ultreon.quantum.GamePlatform.requestAttention()"""
        super(GamePlatform, self).requestAttention()

    @overload
    def getMods(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.Mod> dev.ultreon.quantum.GamePlatform.getMods()"""
        return 'Collection'._wrap(super(GamePlatform, self).getMods())

    @overload
    def getMod(self, arg0: str) -> 'Optional':
        """public java.util.Optional<dev.ultreon.quantum.Mod> dev.ultreon.quantum.GamePlatform.getMod(java.lang.String)"""
        return 'Optional'._wrap(super(_GamePlatform, self).getMod(arg0))

    @overload
    def setupImGui(self):
        """public void dev.ultreon.quantum.GamePlatform.setupImGui()"""
        super(GamePlatform, self).setupImGui()

    @overload
    def launch(self, arg0: 'String'):
        """public void dev.ultreon.quantum.GamePlatform.launch(java.lang.String[])"""
        super(_GamePlatform, self).launch(arg0)

    @overload
    def createWindow(self) -> 'GameWindow':
        """public dev.ultreon.quantum.GameWindow dev.ultreon.quantum.GamePlatform.createWindow()"""
        return 'GameWindow'._wrap(super(GamePlatform, self).createWindow())

    @overload
    def invokeEntrypoint(self, arg0: str, arg1: 'Class', arg2: 'Consumer'):
        """public <T> void dev.ultreon.quantum.GamePlatform.invokeEntrypoint(java.lang.String,java.lang.Class<T>,java.util.function.Consumer<T>)"""
        super(_GamePlatform, self).invokeEntrypoint(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.GamePlatform.setCursorPosition(int,int)"""
        super(_GamePlatform, self).setCursorPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def close(self):
        """public void dev.ultreon.quantum.GamePlatform.close()"""
        super(GamePlatform, self).close()

    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.GamePlatform.setVisible(boolean)"""
        super(_GamePlatform, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isMobile(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isMobile()"""
        return bool._wrap(super(GamePlatform, self).isMobile())

    @abstractmethod
    def getDeviceType(self, ):
        """public abstract dev.ultreon.quantum.DeviceType dev.ultreon.quantum.GamePlatform.getDeviceType()"""
        pass

    @overload
    def preInitImGui(self):
        """public void dev.ultreon.quantum.GamePlatform.preInitImGui()"""
        super(GamePlatform, self).preInitImGui()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @abstractmethod
    def getMouseDevice(self, ):
        """public abstract dev.ultreon.quantum.platform.MouseDevice dev.ultreon.quantum.GamePlatform.getMouseDevice()"""
        pass

    @overload
    def isMacOSX(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isMacOSX()"""
        return bool._wrap(super(GamePlatform, self).isMacOSX())

    @overload
    def openImportDialog(self) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Boolean> dev.ultreon.quantum.GamePlatform.openImportDialog()"""
        return 'util.Result'._wrap(super(GamePlatform, self).openImportDialog())

    @overload
    def getGameDir(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.GamePlatform.getGameDir()"""
        return 'Path'._wrap(super(GamePlatform, self).getGameDir())

    @overload
    def locateModResources(self):
        """public void dev.ultreon.quantum.GamePlatform.locateModResources()"""
        super(GamePlatform, self).locateModResources()

    @overload
    def getEnv(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.GamePlatform.getEnv()"""
        return 'util.Env'._wrap(super(GamePlatform, self).getEnv())

    @staticmethod
    @overload
    def get() -> 'GamePlatform':
        """public static dev.ultreon.quantum.GamePlatform dev.ultreon.quantum.GamePlatform.get()"""
        return GamePlatform._wrap(_GamePlatform.get())

    @overload
    def getConfigDir(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.GamePlatform.getConfigDir()"""
        return 'Path'._wrap(super(GamePlatform, self).getConfigDir())

    @overload
    def onGameDispose(self):
        """public void dev.ultreon.quantum.GamePlatform.onGameDispose()"""
        super(GamePlatform, self).onGameDispose()

    @overload
    def onFirstRender(self):
        """public void dev.ultreon.quantum.GamePlatform.onFirstRender()"""
        super(GamePlatform, self).onFirstRender()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isDevEnvironment(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isDevEnvironment()"""
        return bool._wrap(super(GamePlatform, self).isDevEnvironment())

    @overload
    def isModLoaded(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isModLoaded(java.lang.String)"""
        return bool._wrap(super(_GamePlatform, self).isModLoaded(arg0))

    @overload
    def isDesktop(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isDesktop()"""
        return bool._wrap(super(GamePlatform, self).isDesktop())

    @overload
    def isShowingImGui(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isShowingImGui()"""
        return bool._wrap(super(GamePlatform, self).isShowingImGui())

    @overload
    def renderImGui(self):
        """public void dev.ultreon.quantum.GamePlatform.renderImGui()"""
        super(GamePlatform, self).renderImGui()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def detectDebug(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.detectDebug()"""
        return bool._wrap(super(GamePlatform, self).detectDebug())

    @overload
    def showRenderPipeline(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.showRenderPipeline()"""
        return bool._wrap(super(GamePlatform, self).showRenderPipeline()) 
 
 
# CLASS: dev.ultreon.quantum.StdoutLogger
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.StdoutLogger as _StdoutLogger
_StdoutLogger = _StdoutLogger
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StdoutLogger():
    """dev.ultreon.quantum.StdoutLogger"""
 
    @staticmethod
    def _wrap(java_value: _StdoutLogger) -> 'StdoutLogger':
        return StdoutLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StdoutLogger):
        """
        Dynamic initializer for StdoutLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StdoutLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StdoutLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.StdoutLogger()"""
        val = _StdoutLogger()
        self.__wrapper = val

    @override
    @overload
    def warn(self, arg0: str):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String)"""
        super(_StdoutLogger, self).warn(arg0)

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_StdoutLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_StdoutLogger, self).error(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_StdoutLogger, self).debug(arg0, arg1)

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
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_StdoutLogger, self).error(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_StdoutLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String,java.lang.Object)"""
        super(_StdoutLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_StdoutLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_StdoutLogger, self).warn(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_StdoutLogger, self).info(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String,java.lang.Object)"""
        super(_StdoutLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_StdoutLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: str):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String)"""
        super(_StdoutLogger, self).info(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String,java.lang.Object)"""
        super(_StdoutLogger, self).warn(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String)"""
        super(_StdoutLogger, self).error(arg0)

    @override
    @overload
    def debug(self, arg0: str):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String)"""
        super(_StdoutLogger, self).debug(arg0)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_StdoutLogger, self).debug(arg0, arg1, arg2)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.StdoutLogger()"""
        val = _StdoutLogger()
        self.__wrapper = val

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_StdoutLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String,java.lang.Object)"""
        super(_StdoutLogger, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_StdoutLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.Mod
import java.lang.Integer as _int
import dev.ultreon.quantum.Mod as _Mod
_Mod = _Mod
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from abc import abstractmethod, ABC
 
class Mod():
    """dev.ultreon.quantum.Mod"""
 
    @staticmethod
    def _wrap(java_value: _Mod) -> 'Mod':
        return Mod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Mod):
        """
        Dynamic initializer for Mod.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Mod__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Mod__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getAuthors(self, ):
        """public abstract java.util.Collection<java.lang.String> dev.ultreon.quantum.Mod.getAuthors()"""
        pass

    @abstractmethod
    def getRootPaths(self, ):
        """public abstract java.lang.Iterable<java.nio.file.Path> dev.ultreon.quantum.Mod.getRootPaths()"""
        pass

    @abstractmethod
    def getId(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.Mod.getId()"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.Mod.getName()"""
        pass

    @abstractmethod
    def getVersion(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.Mod.getVersion()"""
        pass

    @overload
    def getIconPath(self, arg0: int) -> 'Optional':
        """public default java.util.Optional<java.lang.String> dev.ultreon.quantum.Mod.getIconPath(int)"""
        return 'Optional'._wrap(super(_Mod, self).getIconPath(_int.valueOf(arg0)))

    @abstractmethod
    def getDescription(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.Mod.getDescription()"""
        pass

    @abstractmethod
    def getOrigin(self, ):
        """public abstract dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.Mod.getOrigin()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.HeadlessGameWindow
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.HeadlessGameWindow as _HeadlessGameWindow
_HeadlessGameWindow = _HeadlessGameWindow
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.GameWindow as _GameWindow
_GameWindow = _GameWindow
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessGameWindow():
    """dev.ultreon.quantum.HeadlessGameWindow"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessGameWindow) -> 'HeadlessGameWindow':
        return HeadlessGameWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessGameWindow):
        """
        Dynamic initializer for HeadlessGameWindow.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessGameWindow__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessGameWindow__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.HeadlessGameWindow.isHovered()"""
        return bool._wrap(super(HeadlessGameWindow, self).isHovered())

    @override
    @overload
    def requestAttention(self):
        """public void dev.ultreon.quantum.GameWindow.requestAttention()"""
        super(GameWindow, self).requestAttention()

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setResizable(boolean)"""
        super(_GameWindow, self).setResizable(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isMinimized(self) -> bool:
        """public boolean dev.ultreon.quantum.HeadlessGameWindow.isMinimized()"""
        return bool._wrap(super(HeadlessGameWindow, self).isMinimized())

    @override
    @overload
    def restore(self):
        """public void dev.ultreon.quantum.GameWindow.restore()"""
        super(GameWindow, self).restore()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.GameWindow.close()"""
        super(GameWindow, self).close()

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void dev.ultreon.quantum.GameWindow.setTitle(java.lang.String)"""
        super(_GameWindow, self).setTitle(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isMaximized(self) -> bool:
        """public boolean dev.ultreon.quantum.HeadlessGameWindow.isMaximized()"""
        return bool._wrap(super(HeadlessGameWindow, self).isMaximized())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getHandle(self) -> int:
        """public long dev.ultreon.quantum.GameWindow.getHandle()"""
        return int._wrap(super(GameWindow, self).getHandle())

    @override
    @overload
    def minimize(self):
        """public void dev.ultreon.quantum.GameWindow.minimize()"""
        super(GameWindow, self).minimize()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isResizable(self) -> bool:
        """public boolean dev.ultreon.quantum.GameWindow.isResizable()"""
        return bool._wrap(super(GameWindow, self).isResizable())

    @override
    @overload
    def focus(self):
        """public void dev.ultreon.quantum.GameWindow.focus()"""
        super(GameWindow, self).focus()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.HeadlessGameWindow.isFocused()"""
        return bool._wrap(super(HeadlessGameWindow, self).isFocused())

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
    def maximize(self):
        """public void dev.ultreon.quantum.GameWindow.maximize()"""
        super(GameWindow, self).maximize()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.HeadlessGameWindow()"""
        val = _HeadlessGameWindow()
        self.__wrapper = val

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setVisible(boolean)"""
        super(_GameWindow, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.HeadlessGameWindow()"""
        val = _HeadlessGameWindow()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.FieldsAreNonnullByDefault
import dev.ultreon.quantum.FieldsAreNonnullByDefault as _FieldsAreNonnullByDefault
_FieldsAreNonnullByDefault = _FieldsAreNonnullByDefault
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class FieldsAreNonnullByDefault():
    """dev.ultreon.quantum.FieldsAreNonnullByDefault"""
 
    @staticmethod
    def _wrap(java_value: _FieldsAreNonnullByDefault) -> 'FieldsAreNonnullByDefault':
        return FieldsAreNonnullByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FieldsAreNonnullByDefault):
        """
        Dynamic initializer for FieldsAreNonnullByDefault.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FieldsAreNonnullByDefault__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FieldsAreNonnullByDefault__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.CommonLoader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.CommonLoader as _CommonLoader
_CommonLoader = _CommonLoader
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommonLoader():
    """dev.ultreon.quantum.CommonLoader"""
 
    @staticmethod
    def _wrap(java_value: _CommonLoader) -> 'CommonLoader':
        return CommonLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommonLoader):
        """
        Dynamic initializer for CommonLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommonLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommonLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self):
        """public dev.ultreon.quantum.CommonLoader()"""
        val = _CommonLoader()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.CommonLoader()"""
        val = _CommonLoader()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def initConfigEntrypoints(arg0: 'GamePlatform'):
        """public static void dev.ultreon.quantum.CommonLoader.initConfigEntrypoints(dev.ultreon.quantum.GamePlatform)"""
        _CommonLoader.initConfigEntrypoints(arg0)

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.ToolLevels
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.ToolLevels as _ToolLevels
_ToolLevels = _ToolLevels
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
import java.util.List as _List
_List = _List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ToolLevels():
    """dev.ultreon.quantum.ToolLevels"""
 
    @staticmethod
    def _wrap(java_value: _ToolLevels) -> 'ToolLevels':
        return ToolLevels(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToolLevels):
        """
        Dynamic initializer for ToolLevels.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToolLevels__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToolLevels__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.ToolLevels()"""
        val = _ToolLevels()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.ToolLevels()"""
        val = _ToolLevels()
        self.__wrapper = val

    @staticmethod
    @overload
    def maxLevel() -> int:
        """public static int dev.ultreon.quantum.ToolLevels.maxLevel()"""
        return int._wrap(_ToolLevels.maxLevel())

    @staticmethod
    @overload
    def registerBefore(arg0: 'ToolLevel', arg1: int) -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.registerBefore(dev.ultreon.quantum.block.ToolLevel,int)"""
        return block.ToolLevel._wrap(_ToolLevels.registerBefore(arg0, _int.valueOf(arg1)))

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
    def register(arg0: 'ToolLevel') -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.register(dev.ultreon.quantum.block.ToolLevel)"""
        return block.ToolLevel._wrap(_ToolLevels.register(arg0))

    @staticmethod
    @overload
    def levels() -> 'List':
        """public static java.util.List<dev.ultreon.quantum.block.ToolLevel> dev.ultreon.quantum.ToolLevels.levels()"""
        return List._wrap(_ToolLevels.levels())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def registerLast(arg0: 'ToolLevel') -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.registerLast(dev.ultreon.quantum.block.ToolLevel)"""
        return block.ToolLevel._wrap(_ToolLevels.registerLast(arg0))

    @staticmethod
    @overload
    def registerFirst(arg0: 'ToolLevel') -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.registerFirst(dev.ultreon.quantum.block.ToolLevel)"""
        return block.ToolLevel._wrap(_ToolLevels.registerFirst(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def get(arg0: 'ToolLevel') -> int:
        """public static int dev.ultreon.quantum.ToolLevels.get(dev.ultreon.quantum.block.ToolLevel)"""
        return int._wrap(_ToolLevels.get(arg0))

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

    @staticmethod
    @overload
    def get(arg0: int) -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.get(int)"""
        return block.ToolLevel._wrap(_ToolLevels.get(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def registerAfter(arg0: 'ToolLevel', arg1: int) -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.registerAfter(dev.ultreon.quantum.block.ToolLevel,int)"""
        return block.ToolLevel._wrap(_ToolLevels.registerAfter(arg0, _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.LoadingContext
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.LoadingContext as _LoadingContext
_LoadingContext = _LoadingContext
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoadingContext():
    """dev.ultreon.quantum.LoadingContext"""
 
    @staticmethod
    def _wrap(java_value: _LoadingContext) -> 'LoadingContext':
        return LoadingContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadingContext):
        """
        Dynamic initializer for LoadingContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadingContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadingContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.LoadingContext.hashCode()"""
        return int._wrap(super(LoadingContext, self).hashCode())

    @staticmethod
    @overload
    def withinContext(arg0: 'LoadingContext', arg1: 'Runnable'):
        """public static void dev.ultreon.quantum.LoadingContext.withinContext(dev.ultreon.quantum.LoadingContext,java.lang.Runnable)"""
        _LoadingContext.withinContext(arg0, arg1)

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.LoadingContext(java.lang.String)"""
        val = _LoadingContext(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.LoadingContext.equals(java.lang.Object)"""
        return bool._wrap(super(_LoadingContext, self).equals(arg0))

    @overload
    def namespace(self) -> str:
        """public java.lang.String dev.ultreon.quantum.LoadingContext.namespace()"""
        return str._wrap(super(LoadingContext, self).namespace())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def get() -> 'LoadingContext':
        """public static dev.ultreon.quantum.LoadingContext dev.ultreon.quantum.LoadingContext.get()"""
        return LoadingContext._wrap(_LoadingContext.get())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.LoadingContext.toString()"""
        return str._wrap(super(LoadingContext, self).toString())

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
 
 
# CLASS: dev.ultreon.quantum.MethodsReturnNonnullByDefault
from abc import abstractmethod, ABC
import dev.ultreon.quantum.MethodsReturnNonnullByDefault as _MethodsReturnNonnullByDefault
_MethodsReturnNonnullByDefault = _MethodsReturnNonnullByDefault
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class MethodsReturnNonnullByDefault():
    """dev.ultreon.quantum.MethodsReturnNonnullByDefault"""
 
    @staticmethod
    def _wrap(java_value: _MethodsReturnNonnullByDefault) -> 'MethodsReturnNonnullByDefault':
        return MethodsReturnNonnullByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MethodsReturnNonnullByDefault):
        """
        Dynamic initializer for MethodsReturnNonnullByDefault.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MethodsReturnNonnullByDefault__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MethodsReturnNonnullByDefault__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.CommonConstants
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
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.CommonConstants as _CommonConstants
_CommonConstants = _CommonConstants
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommonConstants():
    """dev.ultreon.quantum.CommonConstants"""
 
    @staticmethod
    def _wrap(java_value: _CommonConstants) -> 'CommonConstants':
        return CommonConstants(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommonConstants):
        """
        Dynamic initializer for CommonConstants.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommonConstants__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommonConstants__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.CommonConstants.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def strId(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.CommonConstants.strId(java.lang.String)"""
        return str._wrap(_CommonConstants.strId(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.ModInit
import dev.ultreon.quantum.ModInit as _ModInit
_ModInit = _ModInit
from abc import abstractmethod, ABC
 
class ModInit():
    """dev.ultreon.quantum.ModInit"""
 
    @staticmethod
    def _wrap(java_value: _ModInit) -> 'ModInit':
        return ModInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModInit):
        """
        Dynamic initializer for ModInit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModInit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModInit__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onInitialize(self, ):
        """public abstract void dev.ultreon.quantum.ModInit.onInitialize()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.FieldsAreNullableByDefault
import dev.ultreon.quantum.FieldsAreNullableByDefault as _FieldsAreNullableByDefault
_FieldsAreNullableByDefault = _FieldsAreNullableByDefault
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class FieldsAreNullableByDefault():
    """dev.ultreon.quantum.FieldsAreNullableByDefault"""
 
    @staticmethod
    def _wrap(java_value: _FieldsAreNullableByDefault) -> 'FieldsAreNullableByDefault':
        return FieldsAreNullableByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FieldsAreNullableByDefault):
        """
        Dynamic initializer for FieldsAreNullableByDefault.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FieldsAreNullableByDefault__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FieldsAreNullableByDefault__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.CommonRegistries
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.CommonRegistries as _CommonRegistries
_CommonRegistries = _CommonRegistries
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommonRegistries():
    """dev.ultreon.quantum.CommonRegistries"""
 
    @staticmethod
    def _wrap(java_value: _CommonRegistries) -> 'CommonRegistries':
        return CommonRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommonRegistries):
        """
        Dynamic initializer for CommonRegistries.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommonRegistries__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommonRegistries__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.CommonRegistries()"""
        val = _CommonRegistries()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def register():
            """public static void dev.ultreon.quantum.CommonRegistries.register()"""
            _CommonRegistries.register()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.CommonRegistries()"""
        val = _CommonRegistries()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.UnsafeApi
from abc import abstractmethod, ABC
import dev.ultreon.quantum.UnsafeApi as _UnsafeApi
_UnsafeApi = _UnsafeApi
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class UnsafeApi():
    """dev.ultreon.quantum.UnsafeApi"""
 
    @staticmethod
    def _wrap(java_value: _UnsafeApi) -> 'UnsafeApi':
        return UnsafeApi(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnsafeApi):
        """
        Dynamic initializer for UnsafeApi.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnsafeApi__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnsafeApi__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.CrashHandler
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.CrashHandler as _CrashHandler
_CrashHandler = _CrashHandler
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyquantum import crash
except ImportError:
    crash = _import_once("pyquantum.crash")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrashHandler():
    """dev.ultreon.quantum.CrashHandler"""
 
    @staticmethod
    def _wrap(java_value: _CrashHandler) -> 'CrashHandler':
        return CrashHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrashHandler):
        """
        Dynamic initializer for CrashHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrashHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrashHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.CrashHandler()"""
        val = _CrashHandler()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.CrashHandler()"""
        val = _CrashHandler()
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
    def handleCrash(arg0: 'CrashLog'):
        """public static void dev.ultreon.quantum.CrashHandler.handleCrash(dev.ultreon.quantum.crash.CrashLog)"""
        _CrashHandler.handleCrash(arg0)

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

    @staticmethod
    @overload
    def addHandler(arg0: 'Consumer'):
        """public static void dev.ultreon.quantum.CrashHandler.addHandler(java.util.function.Consumer<dev.ultreon.quantum.crash.CrashLog>)"""
        _CrashHandler.addHandler(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.TypeUsesAreNonnullByDefault
import dev.ultreon.quantum.TypeUsesAreNonnullByDefault as _TypeUsesAreNonnullByDefault
_TypeUsesAreNonnullByDefault = _TypeUsesAreNonnullByDefault
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class TypeUsesAreNonnullByDefault():
    """dev.ultreon.quantum.TypeUsesAreNonnullByDefault"""
 
    @staticmethod
    def _wrap(java_value: _TypeUsesAreNonnullByDefault) -> 'TypeUsesAreNonnullByDefault':
        return TypeUsesAreNonnullByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeUsesAreNonnullByDefault):
        """
        Dynamic initializer for TypeUsesAreNonnullByDefault.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeUsesAreNonnullByDefault__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeUsesAreNonnullByDefault__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.ModOrigin
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.ModOrigin as _ModOrigin
_ModOrigin = _ModOrigin
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModOrigin():
    """dev.ultreon.quantum.ModOrigin"""
 
    @staticmethod
    def _wrap(java_value: _ModOrigin) -> 'ModOrigin':
        return ModOrigin(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModOrigin):
        """
        Dynamic initializer for ModOrigin.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModOrigin__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModOrigin__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ModOrigin':
        """public static dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.ModOrigin.valueOf(java.lang.String)"""
        return ModOrigin._wrap(_ModOrigin.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['ModOrigin']:
        """public static dev.ultreon.quantum.ModOrigin[] dev.ultreon.quantum.ModOrigin.values()"""
        return List[ModOrigin]._wrap(_ModOrigin.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


ModOrigin.BUNDLED = ModOrigin._wrap(_BUNDLED.BUNDLED)

ModOrigin.ACTUAL_PATH = ModOrigin._wrap(_ACTUAL_PATH.ACTUAL_PATH)

ModOrigin.OTHER = ModOrigin._wrap(_OTHER.OTHER) 
 
 
# CLASS: dev.ultreon.quantum.GameWindow
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.GameWindow as _GameWindow
_GameWindow = _GameWindow
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameWindow():
    """dev.ultreon.quantum.GameWindow"""
 
    @staticmethod
    def _wrap(java_value: _GameWindow) -> 'GameWindow':
        return GameWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameWindow):
        """
        Dynamic initializer for GameWindow.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameWindow__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameWindow__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def maximize(self):
        """public void dev.ultreon.quantum.GameWindow.maximize()"""
        super(GameWindow, self).maximize()

    @overload
    def isResizable(self) -> bool:
        """public boolean dev.ultreon.quantum.GameWindow.isResizable()"""
        return bool._wrap(super(GameWindow, self).isResizable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def isMinimized(self, ):
        """public abstract boolean dev.ultreon.quantum.GameWindow.isMinimized()"""
        pass

    @overload
    def focus(self):
        """public void dev.ultreon.quantum.GameWindow.focus()"""
        super(GameWindow, self).focus()

    @overload
    def requestAttention(self):
        """public void dev.ultreon.quantum.GameWindow.requestAttention()"""
        super(GameWindow, self).requestAttention()

    @overload
    def setResizable(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setResizable(boolean)"""
        super(_GameWindow, self).setResizable(_boolean.valueOf(arg0))

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
    def getHandle(self) -> int:
        """public long dev.ultreon.quantum.GameWindow.getHandle()"""
        return int._wrap(super(GameWindow, self).getHandle())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def close(self):
        """public void dev.ultreon.quantum.GameWindow.close()"""
        super(GameWindow, self).close()

    @abstractmethod
    def isFocused(self, ):
        """public abstract boolean dev.ultreon.quantum.GameWindow.isFocused()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setVisible(boolean)"""
        super(_GameWindow, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.GameWindow()"""
        val = _GameWindow()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setTitle(self, arg0: str):
        """public void dev.ultreon.quantum.GameWindow.setTitle(java.lang.String)"""
        super(_GameWindow, self).setTitle(arg0)

    @abstractmethod
    def isHovered(self, ):
        """public abstract boolean dev.ultreon.quantum.GameWindow.isHovered()"""
        pass

    @overload
    def minimize(self):
        """public void dev.ultreon.quantum.GameWindow.minimize()"""
        super(GameWindow, self).minimize()

    @overload
    def restore(self):
        """public void dev.ultreon.quantum.GameWindow.restore()"""
        super(GameWindow, self).restore()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def isMaximized(self, ):
        """public abstract boolean dev.ultreon.quantum.GameWindow.isMaximized()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.GameWindow()"""
        val = _GameWindow()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.TypeParametersAreNonnullByDefault
from abc import abstractmethod, ABC
import dev.ultreon.quantum.TypeParametersAreNonnullByDefault as _TypeParametersAreNonnullByDefault
_TypeParametersAreNonnullByDefault = _TypeParametersAreNonnullByDefault
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class TypeParametersAreNonnullByDefault():
    """dev.ultreon.quantum.TypeParametersAreNonnullByDefault"""
 
    @staticmethod
    def _wrap(java_value: _TypeParametersAreNonnullByDefault) -> 'TypeParametersAreNonnullByDefault':
        return TypeParametersAreNonnullByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeParametersAreNonnullByDefault):
        """
        Dynamic initializer for TypeParametersAreNonnullByDefault.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeParametersAreNonnullByDefault__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeParametersAreNonnullByDefault__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.Modifications
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.Modifications as _Modifications
_Modifications = _Modifications
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Modifications():
    """dev.ultreon.quantum.Modifications"""
 
    @staticmethod
    def _wrap(java_value: _Modifications) -> 'Modifications':
        return Modifications(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Modifications):
        """
        Dynamic initializer for Modifications.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Modifications__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Modifications__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getEnableDomainWarping(self) -> bool:
        """public final boolean dev.ultreon.quantum.Modifications.getEnableDomainWarping()"""
        return bool._wrap(super(Modifications, self).getEnableDomainWarping())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setEnableDomainWarping(self, arg0: bool):
        """public final void dev.ultreon.quantum.Modifications.setEnableDomainWarping(boolean)"""
        super(_Modifications, self).setEnableDomainWarping(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


Modifications.INSTANCE = Modifications._wrap(_INSTANCE.INSTANCE)