from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.DeviceType as __DeviceType
__DeviceType = __DeviceType
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
 
class DeviceType(__Enum, Enum):
    """dev.ultreon.quantum.DeviceType"""
 
    @staticmethod
    def __wrap(java_value: __DeviceType) -> 'DeviceType':
        return DeviceType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeviceType):
        """
        Dynamic initializer for DeviceType.
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
 
    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.AUTOMOBILE
    AUTOMOBILE: 'DeviceType' = __wrap(__DeviceType.AUTOMOBILE)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.MOBILE
    MOBILE: 'DeviceType' = __wrap(__DeviceType.MOBILE)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.DESKTOP
    DESKTOP: 'DeviceType' = __wrap(__DeviceType.DESKTOP)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.WATCH
    WATCH: 'DeviceType' = __wrap(__DeviceType.WATCH)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.OTHER
    OTHER: 'DeviceType' = __wrap(__DeviceType.OTHER)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.TV
    TV: 'DeviceType' = __wrap(__DeviceType.TV)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.APPLIANCE
    APPLIANCE: 'DeviceType' = __wrap(__DeviceType.APPLIANCE)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.TABLET
    TABLET: 'DeviceType' = __wrap(__DeviceType.TABLET)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.VR_HEADSET
    VR_HEADSET: 'DeviceType' = __wrap(__DeviceType.VR_HEADSET)


    @staticmethod
    @overload
    def values() -> List['DeviceType']:
        """public static dev.ultreon.quantum.DeviceType[] dev.ultreon.quantum.DeviceType.values()"""
        return List[DeviceType].__wrap(__DeviceType.values())

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
    def valueOf(arg0: str) -> 'DeviceType':
        """public static dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.valueOf(java.lang.String)"""
        return DeviceType.__wrap(__DeviceType.valueOf(arg0))

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

 
 
 
# CLASS: dev.ultreon.quantum.DeviceType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.DeviceType as __DeviceType
__DeviceType = __DeviceType
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
 
class DeviceType(__Enum, Enum):
    """dev.ultreon.quantum.DeviceType"""
 
    @staticmethod
    def __wrap(java_value: __DeviceType) -> 'DeviceType':
        return DeviceType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeviceType):
        """
        Dynamic initializer for DeviceType.
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
 
    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.AUTOMOBILE
    AUTOMOBILE: 'DeviceType' = __wrap(__DeviceType.AUTOMOBILE)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.MOBILE
    MOBILE: 'DeviceType' = __wrap(__DeviceType.MOBILE)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.DESKTOP
    DESKTOP: 'DeviceType' = __wrap(__DeviceType.DESKTOP)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.WATCH
    WATCH: 'DeviceType' = __wrap(__DeviceType.WATCH)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.OTHER
    OTHER: 'DeviceType' = __wrap(__DeviceType.OTHER)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.TV
    TV: 'DeviceType' = __wrap(__DeviceType.TV)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.APPLIANCE
    APPLIANCE: 'DeviceType' = __wrap(__DeviceType.APPLIANCE)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.TABLET
    TABLET: 'DeviceType' = __wrap(__DeviceType.TABLET)

    # public static final dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.VR_HEADSET
    VR_HEADSET: 'DeviceType' = __wrap(__DeviceType.VR_HEADSET)


    @staticmethod
    @overload
    def values() -> List['DeviceType']:
        """public static dev.ultreon.quantum.DeviceType[] dev.ultreon.quantum.DeviceType.values()"""
        return List[DeviceType].__wrap(__DeviceType.values())

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
    def valueOf(arg0: str) -> 'DeviceType':
        """public static dev.ultreon.quantum.DeviceType dev.ultreon.quantum.DeviceType.valueOf(java.lang.String)"""
        return DeviceType.__wrap(__DeviceType.valueOf(arg0))

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

 
 
 
# CLASS: dev.ultreon.quantum.DeviceType 
 
 
# CLASS: dev.ultreon.quantum.GamePlatform
from pyquantum_helper import import_once as __import_once__
import org.mozilla.javascript.Context as Context
import java.lang.Boolean as __boolean
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
import dev.ultreon.quantum.GameWindow as __GameWindow
__GameWindow = __GameWindow
import java.lang.Integer as __int
from builtins import int
 
class GamePlatform(ABC):
    """dev.ultreon.quantum.GamePlatform"""
 
    @staticmethod
    def __wrap(java_value: __GamePlatform) -> 'GamePlatform':
        return GamePlatform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GamePlatform):
        """
        Dynamic initializer for GamePlatform.
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
    def launch(self, arg0: 'String'):
        """public void dev.ultreon.quantum.GamePlatform.launch(java.lang.String[])"""
        super(__GamePlatform, self).launch(arg0)

    @overload
    def prepare(self):
        """public void dev.ultreon.quantum.GamePlatform.prepare()"""
        super(GamePlatform, self).prepare()

    @abstractmethod
    def isMouseCaptured(self, ):
        """public abstract boolean dev.ultreon.quantum.GamePlatform.isMouseCaptured()"""
        pass

    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.GamePlatform.setCursorPosition(int,int)"""
        super(__GamePlatform, self).setCursorPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isModLoaded(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isModLoaded(java.lang.String)"""
        return bool.__wrap(super(__GamePlatform, self).isModLoaded(arg0))

    @overload
    def detectDebug(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.detectDebug()"""
        return bool.__wrap(super(GamePlatform, self).detectDebug())

    @abstractmethod
    def setMouseCaptured(self, arg0: bool):
        """public abstract void dev.ultreon.quantum.GamePlatform.setMouseCaptured(boolean)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def createWindow(self) -> 'GameWindow':
        """public dev.ultreon.quantum.GameWindow dev.ultreon.quantum.GamePlatform.createWindow()"""
        return 'GameWindow'.__wrap(super(GamePlatform, self).createWindow())

    @overload
    def locateResources(self):
        """public void dev.ultreon.quantum.GamePlatform.locateResources()"""
        super(GamePlatform, self).locateResources()

    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.GamePlatform.setVisible(boolean)"""
        super(__GamePlatform, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def setupMacOSX(self):
        """public void dev.ultreon.quantum.GamePlatform.setupMacOSX()"""
        super(GamePlatform, self).setupMacOSX()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def getGameDevices(self, ):
        """public abstract java.util.Collection<dev.ultreon.quantum.platform.Device> dev.ultreon.quantum.GamePlatform.getGameDevices()"""
        pass

    @overload
    def requestAttention(self):
        """public void dev.ultreon.quantum.GamePlatform.requestAttention()"""
        super(GamePlatform, self).requestAttention()

    @overload
    def setupImGui(self):
        """public void dev.ultreon.quantum.GamePlatform.setupImGui()"""
        super(GamePlatform, self).setupImGui()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isMobile(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isMobile()"""
        return bool.__wrap(super(GamePlatform, self).isMobile())

    @overload
    def hasCompass(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.hasCompass()"""
        return bool.__wrap(super(GamePlatform, self).hasCompass())

    @overload
    def getEnv(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.GamePlatform.getEnv()"""
        return 'util.Env'.__wrap(super(GamePlatform, self).getEnv())

    @overload
    def getConfigDir(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.GamePlatform.getConfigDir()"""
        return 'Path'.__wrap(super(GamePlatform, self).getConfigDir())

    @overload
    def close(self):
        """public void dev.ultreon.quantum.GamePlatform.close()"""
        super(GamePlatform, self).close()

    @overload
    def isWindows(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isWindows()"""
        return bool.__wrap(super(GamePlatform, self).isWindows())

    @overload
    def areChunkBordersVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.areChunkBordersVisible()"""
        return bool.__wrap(super(GamePlatform, self).areChunkBordersVisible())

    @overload
    def getMod(self, arg0: str) -> 'Optional':
        """public java.util.Optional<dev.ultreon.quantum.Mod> dev.ultreon.quantum.GamePlatform.getMod(java.lang.String)"""
        return 'Optional'.__wrap(super(__GamePlatform, self).getMod(arg0))

    @staticmethod
    @overload
    def get() -> 'GamePlatform':
        """public static dev.ultreon.quantum.GamePlatform dev.ultreon.quantum.GamePlatform.get()"""
        return GamePlatform.__wrap(__GamePlatform.get())

    @overload
    def setShowingImGui(self, arg0: bool):
        """public void dev.ultreon.quantum.GamePlatform.setShowingImGui(boolean)"""
        super(__GamePlatform, self).setShowingImGui(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def getDeviceType(self, ):
        """public abstract dev.ultreon.quantum.DeviceType dev.ultreon.quantum.GamePlatform.getDeviceType()"""
        pass

    @overload
    def preInitImGui(self):
        """public void dev.ultreon.quantum.GamePlatform.preInitImGui()"""
        super(GamePlatform, self).preInitImGui()

    @abstractmethod
    def getMouseDevice(self, ):
        """public abstract dev.ultreon.quantum.platform.MouseDevice dev.ultreon.quantum.GamePlatform.getMouseDevice()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isShowingImGui(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isShowingImGui()"""
        return bool.__wrap(super(GamePlatform, self).isShowingImGui())

    @overload
    def getGameDir(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.GamePlatform.getGameDir()"""
        return 'Path'.__wrap(super(GamePlatform, self).getGameDir())

    @overload
    def isDevEnvironment(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isDevEnvironment()"""
        return bool.__wrap(super(GamePlatform, self).isDevEnvironment())

    @overload
    def isDesktop(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isDesktop()"""
        return bool.__wrap(super(GamePlatform, self).isDesktop())

    @overload
    def enterXeoxContext(self) -> 'Context':
        """public org.mozilla.javascript.Context dev.ultreon.quantum.GamePlatform.enterXeoxContext()"""
        return 'Context'.__wrap(super(GamePlatform, self).enterXeoxContext())

    @overload
    def locateModResources(self):
        """public void dev.ultreon.quantum.GamePlatform.locateModResources()"""
        super(GamePlatform, self).locateModResources()

    @overload
    def getMods(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.Mod> dev.ultreon.quantum.GamePlatform.getMods()"""
        return 'Collection'.__wrap(super(GamePlatform, self).getMods())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isLinux(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isLinux()"""
        return bool.__wrap(super(GamePlatform, self).isLinux())

    @overload
    def onGameDispose(self):
        """public void dev.ultreon.quantum.GamePlatform.onGameDispose()"""
        super(GamePlatform, self).onGameDispose()

    @overload
    def onFirstRender(self):
        """public void dev.ultreon.quantum.GamePlatform.onFirstRender()"""
        super(GamePlatform, self).onFirstRender()

    @overload
    def showRenderPipeline(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.showRenderPipeline()"""
        return bool.__wrap(super(GamePlatform, self).showRenderPipeline())

    @overload
    def isMacOSX(self) -> bool:
        """public boolean dev.ultreon.quantum.GamePlatform.isMacOSX()"""
        return bool.__wrap(super(GamePlatform, self).isMacOSX())

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
    def invokeEntrypoint(self, arg0: str, arg1: 'Class', arg2: 'Consumer'):
        """public <T> void dev.ultreon.quantum.GamePlatform.invokeEntrypoint(java.lang.String,java.lang.Class<T>,java.util.function.Consumer<T>)"""
        super(__GamePlatform, self).invokeEntrypoint(arg0, arg1, arg2)

    @overload
    def renderImGui(self):
        """public void dev.ultreon.quantum.GamePlatform.renderImGui()"""
        super(GamePlatform, self).renderImGui()

    @overload
    def getLogger(self, arg0: str) -> 'log.Logger':
        """public dev.ultreon.quantum.log.Logger dev.ultreon.quantum.GamePlatform.getLogger(java.lang.String)"""
        return 'log.Logger'.__wrap(super(__GamePlatform, self).getLogger(arg0))

    @overload
    def openImportDialog(self) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Boolean> dev.ultreon.quantum.GamePlatform.openImportDialog()"""
        return 'util.Result'.__wrap(super(GamePlatform, self).openImportDialog()) 
 
 
# CLASS: dev.ultreon.quantum.StdoutLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.StdoutLogger as __StdoutLogger
__StdoutLogger = __StdoutLogger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StdoutLogger(pyquantum.__Logger, log.Logger):
    """dev.ultreon.quantum.StdoutLogger"""
 
    @staticmethod
    def __wrap(java_value: __StdoutLogger) -> 'StdoutLogger':
        return StdoutLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StdoutLogger):
        """
        Dynamic initializer for StdoutLogger.
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
    def warn(self, arg0: str):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String)"""
        super(__StdoutLogger, self).warn(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String,java.lang.Object)"""
        super(__StdoutLogger, self).error(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__StdoutLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__StdoutLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__StdoutLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String,java.lang.Object)"""
        super(__StdoutLogger, self).debug(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__StdoutLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String,java.lang.Object)"""
        super(__StdoutLogger, self).warn(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String)"""
        super(__StdoutLogger, self).error(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def info(self, arg0: str):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String)"""
        super(__StdoutLogger, self).info(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__StdoutLogger, self).error(arg0, arg1, arg2)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.StdoutLogger()"""
        val = __StdoutLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__StdoutLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__StdoutLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def debug(self, arg0: str):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String)"""
        super(__StdoutLogger, self).debug(arg0)

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__StdoutLogger, self).debug(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String,java.lang.Object)"""
        super(__StdoutLogger, self).info(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.StdoutLogger()"""
        val = __StdoutLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def warn(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.warn(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__StdoutLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.StdoutLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__StdoutLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__StdoutLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.StdoutLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__StdoutLogger, self).error(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.Mod
import java.util.Optional as __Optional
__Optional = __Optional
import java.util.Optional as Optional
import dev.ultreon.quantum.Mod as __Mod
__Mod = __Mod
from abc import abstractmethod, ABC
import java.lang.Integer as __int
 
class Mod(ABC):
    """dev.ultreon.quantum.Mod"""
 
    @staticmethod
    def __wrap(java_value: __Mod) -> 'Mod':
        return Mod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Mod):
        """
        Dynamic initializer for Mod.
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
    def getAuthors(self, ):
        """public abstract java.util.Collection<java.lang.String> dev.ultreon.quantum.Mod.getAuthors()"""
        pass

    @abstractmethod
    def getRootPaths(self, ):
        """public abstract java.lang.Iterable<java.nio.file.Path> dev.ultreon.quantum.Mod.getRootPaths()"""
        pass

    @overload
    def getIconPath(self, arg0: int) -> 'Optional':
        """public default java.util.Optional<java.lang.String> dev.ultreon.quantum.Mod.getIconPath(int)"""
        return 'Optional'.__wrap(super(__Mod, self).getIconPath(__int.valueOf(arg0)))

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
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.HeadlessGameWindow as __HeadlessGameWindow
__HeadlessGameWindow = __HeadlessGameWindow
import dev.ultreon.quantum.GameWindow as __GameWindow
__GameWindow = __GameWindow
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HeadlessGameWindow(__GameWindow, GameWindow):
    """dev.ultreon.quantum.HeadlessGameWindow"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessGameWindow) -> 'HeadlessGameWindow':
        return HeadlessGameWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessGameWindow):
        """
        Dynamic initializer for HeadlessGameWindow.
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
    def requestAttention(self):
        """public void dev.ultreon.quantum.GameWindow.requestAttention()"""
        super(GameWindow, self).requestAttention()

    @override
    @overload
    def getHandle(self) -> int:
        """public long dev.ultreon.quantum.GameWindow.getHandle()"""
        return int.__wrap(super(GameWindow, self).getHandle())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.HeadlessGameWindow()"""
        val = __HeadlessGameWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def restore(self):
        """public void dev.ultreon.quantum.GameWindow.restore()"""
        super(GameWindow, self).restore()

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setVisible(boolean)"""
        super(__GameWindow, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setResizable(boolean)"""
        super(__GameWindow, self).setResizable(__boolean.valueOf(arg0))

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.GameWindow.close()"""
        super(GameWindow, self).close()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isMinimized(self) -> bool:
        """public boolean dev.ultreon.quantum.HeadlessGameWindow.isMinimized()"""
        return bool.__wrap(super(HeadlessGameWindow, self).isMinimized())

    @override
    @overload
    def minimize(self):
        """public void dev.ultreon.quantum.GameWindow.minimize()"""
        super(GameWindow, self).minimize()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.HeadlessGameWindow.isHovered()"""
        return bool.__wrap(super(HeadlessGameWindow, self).isHovered())

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.HeadlessGameWindow.isFocused()"""
        return bool.__wrap(super(HeadlessGameWindow, self).isFocused())

    @override
    @overload
    def isMaximized(self) -> bool:
        """public boolean dev.ultreon.quantum.HeadlessGameWindow.isMaximized()"""
        return bool.__wrap(super(HeadlessGameWindow, self).isMaximized())

    @override
    @overload
    def isResizable(self) -> bool:
        """public boolean dev.ultreon.quantum.GameWindow.isResizable()"""
        return bool.__wrap(super(GameWindow, self).isResizable())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.HeadlessGameWindow()"""
        val = __HeadlessGameWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def focus(self):
        """public void dev.ultreon.quantum.GameWindow.focus()"""
        super(GameWindow, self).focus()

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
    def setTitle(self, arg0: str):
        """public void dev.ultreon.quantum.GameWindow.setTitle(java.lang.String)"""
        super(__GameWindow, self).setTitle(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.FieldsAreNonnullByDefault
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.FieldsAreNonnullByDefault as __FieldsAreNonnullByDefault
__FieldsAreNonnullByDefault = __FieldsAreNonnullByDefault
from abc import abstractmethod, ABC
 
class FieldsAreNonnullByDefault(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.FieldsAreNonnullByDefault"""
 
    @staticmethod
    def __wrap(java_value: __FieldsAreNonnullByDefault) -> 'FieldsAreNonnullByDefault':
        return FieldsAreNonnullByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FieldsAreNonnullByDefault):
        """
        Dynamic initializer for FieldsAreNonnullByDefault.
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
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.CommonLoader as __CommonLoader
__CommonLoader = __CommonLoader
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CommonLoader():
    """dev.ultreon.quantum.CommonLoader"""
 
    @staticmethod
    def __wrap(java_value: __CommonLoader) -> 'CommonLoader':
        return CommonLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommonLoader):
        """
        Dynamic initializer for CommonLoader.
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.CommonLoader()"""
        val = __CommonLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def initConfigEntrypoints(arg0: 'GamePlatform'):
        """public static void dev.ultreon.quantum.CommonLoader.initConfigEntrypoints(dev.ultreon.quantum.GamePlatform)"""
        __CommonLoader.initConfigEntrypoints(arg0)

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
    def __init__(self):
        """public dev.ultreon.quantum.CommonLoader()"""
        val = __CommonLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.ToolLevels
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.ToolLevels as __ToolLevels
__ToolLevels = __ToolLevels
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class ToolLevels():
    """dev.ultreon.quantum.ToolLevels"""
 
    @staticmethod
    def __wrap(java_value: __ToolLevels) -> 'ToolLevels':
        return ToolLevels(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToolLevels):
        """
        Dynamic initializer for ToolLevels.
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
 
    @staticmethod
    @overload
    def registerBefore(arg0: 'ToolLevel', arg1: int) -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.registerBefore(dev.ultreon.quantum.block.ToolLevel,int)"""
        return block.ToolLevel.__wrap(__ToolLevels.registerBefore(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: 'ToolLevel') -> int:
        """public static int dev.ultreon.quantum.ToolLevels.get(dev.ultreon.quantum.block.ToolLevel)"""
        return int.__wrap(__ToolLevels.get(arg0))

    @staticmethod
    @overload
    def registerAfter(arg0: 'ToolLevel', arg1: int) -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.registerAfter(dev.ultreon.quantum.block.ToolLevel,int)"""
        return block.ToolLevel.__wrap(__ToolLevels.registerAfter(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def registerLast(arg0: 'ToolLevel') -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.registerLast(dev.ultreon.quantum.block.ToolLevel)"""
        return block.ToolLevel.__wrap(__ToolLevels.registerLast(arg0))

    @staticmethod
    @overload
    def get(arg0: int) -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.get(int)"""
        return block.ToolLevel.__wrap(__ToolLevels.get(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.ToolLevels()"""
        val = __ToolLevels()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def register(arg0: 'ToolLevel') -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.register(dev.ultreon.quantum.block.ToolLevel)"""
        return block.ToolLevel.__wrap(__ToolLevels.register(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def registerFirst(arg0: 'ToolLevel') -> 'block.ToolLevel':
        """public static dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.ToolLevels.registerFirst(dev.ultreon.quantum.block.ToolLevel)"""
        return block.ToolLevel.__wrap(__ToolLevels.registerFirst(arg0))

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
    def maxLevel() -> int:
        """public static int dev.ultreon.quantum.ToolLevels.maxLevel()"""
        return int.__wrap(__ToolLevels.maxLevel())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.ToolLevels()"""
        val = __ToolLevels()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def levels() -> 'List':
        """public static java.util.List<dev.ultreon.quantum.block.ToolLevel> dev.ultreon.quantum.ToolLevels.levels()"""
        return List.__wrap(__ToolLevels.levels())

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
 
 
# CLASS: dev.ultreon.quantum.LoadingContext
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.LoadingContext as __LoadingContext
__LoadingContext = __LoadingContext
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoadingContext():
    """dev.ultreon.quantum.LoadingContext"""
 
    @staticmethod
    def __wrap(java_value: __LoadingContext) -> 'LoadingContext':
        return LoadingContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadingContext):
        """
        Dynamic initializer for LoadingContext.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def withinContext(arg0: 'LoadingContext', arg1: 'Runnable'):
        """public static void dev.ultreon.quantum.LoadingContext.withinContext(dev.ultreon.quantum.LoadingContext,java.lang.Runnable)"""
        __LoadingContext.withinContext(arg0, arg1)

    @overload
    def namespace(self) -> str:
        """public java.lang.String dev.ultreon.quantum.LoadingContext.namespace()"""
        return str.__wrap(super(LoadingContext, self).namespace())

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
        """public java.lang.String dev.ultreon.quantum.LoadingContext.toString()"""
        return str.__wrap(super(LoadingContext, self).toString())

    @staticmethod
    @overload
    def get() -> 'LoadingContext':
        """public static dev.ultreon.quantum.LoadingContext dev.ultreon.quantum.LoadingContext.get()"""
        return LoadingContext.__wrap(__LoadingContext.get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.LoadingContext(java.lang.String)"""
        val = __LoadingContext(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.LoadingContext.hashCode()"""
        return int.__wrap(super(LoadingContext, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.LoadingContext.equals(java.lang.Object)"""
        return bool.__wrap(super(__LoadingContext, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.MethodsReturnNonnullByDefault
import dev.ultreon.quantum.MethodsReturnNonnullByDefault as __MethodsReturnNonnullByDefault
__MethodsReturnNonnullByDefault = __MethodsReturnNonnullByDefault
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
 
class MethodsReturnNonnullByDefault(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.MethodsReturnNonnullByDefault"""
 
    @staticmethod
    def __wrap(java_value: __MethodsReturnNonnullByDefault) -> 'MethodsReturnNonnullByDefault':
        return MethodsReturnNonnullByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MethodsReturnNonnullByDefault):
        """
        Dynamic initializer for MethodsReturnNonnullByDefault.
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
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.CommonConstants as __CommonConstants
__CommonConstants = __CommonConstants
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CommonConstants():
    """dev.ultreon.quantum.CommonConstants"""
 
    @staticmethod
    def __wrap(java_value: __CommonConstants) -> 'CommonConstants':
        return CommonConstants(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommonConstants):
        """
        Dynamic initializer for CommonConstants.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.CommonConstants.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)


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

    @staticmethod
    @overload
    def strId(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.CommonConstants.strId(java.lang.String)"""
        return str.__wrap(__CommonConstants.strId(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.ModInit
import dev.ultreon.quantum.ModInit as __ModInit
__ModInit = __ModInit
from abc import abstractmethod, ABC
 
class ModInit(ABC):
    """dev.ultreon.quantum.ModInit"""
 
    @staticmethod
    def __wrap(java_value: __ModInit) -> 'ModInit':
        return ModInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModInit):
        """
        Dynamic initializer for ModInit.
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
    def onInitialize(self, ):
        """public abstract void dev.ultreon.quantum.ModInit.onInitialize()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.FieldsAreNullableByDefault
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.FieldsAreNullableByDefault as __FieldsAreNullableByDefault
__FieldsAreNullableByDefault = __FieldsAreNullableByDefault
from abc import abstractmethod, ABC
 
class FieldsAreNullableByDefault(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.FieldsAreNullableByDefault"""
 
    @staticmethod
    def __wrap(java_value: __FieldsAreNullableByDefault) -> 'FieldsAreNullableByDefault':
        return FieldsAreNullableByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FieldsAreNullableByDefault):
        """
        Dynamic initializer for FieldsAreNullableByDefault.
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
import dev.ultreon.quantum.CommonRegistries as __CommonRegistries
__CommonRegistries = __CommonRegistries
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
 
class CommonRegistries():
    """dev.ultreon.quantum.CommonRegistries"""
 
    @staticmethod
    def __wrap(java_value: __CommonRegistries) -> 'CommonRegistries':
        return CommonRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommonRegistries):
        """
        Dynamic initializer for CommonRegistries.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.CommonRegistries()"""
        val = __CommonRegistries()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.CommonRegistries()"""
        val = __CommonRegistries()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

        @staticmethod
        @overload
        def register():
            """public static void dev.ultreon.quantum.CommonRegistries.register()"""
            __CommonRegistries.register() 
 
 
# CLASS: dev.ultreon.quantum.UnsafeApi
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.UnsafeApi as __UnsafeApi
__UnsafeApi = __UnsafeApi
from abc import abstractmethod, ABC
 
class UnsafeApi(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.UnsafeApi"""
 
    @staticmethod
    def __wrap(java_value: __UnsafeApi) -> 'UnsafeApi':
        return UnsafeApi(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnsafeApi):
        """
        Dynamic initializer for UnsafeApi.
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
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.Consumer as Consumer
try:
    from pyquantum import crash
except ImportError:
    crash = __import_once__("pyquantum.crash")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.CrashHandler as __CrashHandler
__CrashHandler = __CrashHandler
from builtins import int
 
class CrashHandler():
    """dev.ultreon.quantum.CrashHandler"""
 
    @staticmethod
    def __wrap(java_value: __CrashHandler) -> 'CrashHandler':
        return CrashHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrashHandler):
        """
        Dynamic initializer for CrashHandler.
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
    def addHandler(arg0: 'Consumer'):
        """public static void dev.ultreon.quantum.CrashHandler.addHandler(java.util.function.Consumer<dev.ultreon.quantum.crash.CrashLog>)"""
        __CrashHandler.addHandler(arg0)

    @staticmethod
    @overload
    def handleCrash(arg0: 'CrashLog'):
        """public static void dev.ultreon.quantum.CrashHandler.handleCrash(dev.ultreon.quantum.crash.CrashLog)"""
        __CrashHandler.handleCrash(arg0)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.CrashHandler()"""
        val = __CrashHandler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.CrashHandler()"""
        val = __CrashHandler()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.TypeUsesAreNonnullByDefault
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.TypeUsesAreNonnullByDefault as __TypeUsesAreNonnullByDefault
__TypeUsesAreNonnullByDefault = __TypeUsesAreNonnullByDefault
from abc import abstractmethod, ABC
 
class TypeUsesAreNonnullByDefault(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.TypeUsesAreNonnullByDefault"""
 
    @staticmethod
    def __wrap(java_value: __TypeUsesAreNonnullByDefault) -> 'TypeUsesAreNonnullByDefault':
        return TypeUsesAreNonnullByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeUsesAreNonnullByDefault):
        """
        Dynamic initializer for TypeUsesAreNonnullByDefault.
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
import dev.ultreon.quantum.ModOrigin as __ModOrigin
__ModOrigin = __ModOrigin
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class ModOrigin(__Enum, Enum):
    """dev.ultreon.quantum.ModOrigin"""
 
    @staticmethod
    def __wrap(java_value: __ModOrigin) -> 'ModOrigin':
        return ModOrigin(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModOrigin):
        """
        Dynamic initializer for ModOrigin.
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
 
    # public static final dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.ModOrigin.OTHER
    OTHER: 'ModOrigin' = __wrap(__ModOrigin.OTHER)

    # public static final dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.ModOrigin.BUNDLED
    BUNDLED: 'ModOrigin' = __wrap(__ModOrigin.BUNDLED)

    # public static final dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.ModOrigin.ACTUAL_PATH
    ACTUAL_PATH: 'ModOrigin' = __wrap(__ModOrigin.ACTUAL_PATH)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['ModOrigin']:
        """public static dev.ultreon.quantum.ModOrigin[] dev.ultreon.quantum.ModOrigin.values()"""
        return List[ModOrigin].__wrap(__ModOrigin.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ModOrigin':
        """public static dev.ultreon.quantum.ModOrigin dev.ultreon.quantum.ModOrigin.valueOf(java.lang.String)"""
        return ModOrigin.__wrap(__ModOrigin.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.GameWindow
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.GameWindow as __GameWindow
__GameWindow = __GameWindow
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GameWindow(ABC):
    """dev.ultreon.quantum.GameWindow"""
 
    @staticmethod
    def __wrap(java_value: __GameWindow) -> 'GameWindow':
        return GameWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameWindow):
        """
        Dynamic initializer for GameWindow.
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
    def isResizable(self) -> bool:
        """public boolean dev.ultreon.quantum.GameWindow.isResizable()"""
        return bool.__wrap(super(GameWindow, self).isResizable())

    @overload
    def maximize(self):
        """public void dev.ultreon.quantum.GameWindow.maximize()"""
        super(GameWindow, self).maximize()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getHandle(self) -> int:
        """public long dev.ultreon.quantum.GameWindow.getHandle()"""
        return int.__wrap(super(GameWindow, self).getHandle())

    @overload
    def setTitle(self, arg0: str):
        """public void dev.ultreon.quantum.GameWindow.setTitle(java.lang.String)"""
        super(__GameWindow, self).setTitle(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.GameWindow()"""
        val = __GameWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.GameWindow()"""
        val = __GameWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def isHovered(self, ):
        """public abstract boolean dev.ultreon.quantum.GameWindow.isHovered()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def minimize(self):
        """public void dev.ultreon.quantum.GameWindow.minimize()"""
        super(GameWindow, self).minimize()

    @overload
    def restore(self):
        """public void dev.ultreon.quantum.GameWindow.restore()"""
        super(GameWindow, self).restore()

    @overload
    def setResizable(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setResizable(boolean)"""
        super(__GameWindow, self).setResizable(__boolean.valueOf(arg0))

    @abstractmethod
    def isMaximized(self, ):
        """public abstract boolean dev.ultreon.quantum.GameWindow.isMaximized()"""
        pass

    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.GameWindow.setVisible(boolean)"""
        super(__GameWindow, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.TypeParametersAreNonnullByDefault
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.TypeParametersAreNonnullByDefault as __TypeParametersAreNonnullByDefault
__TypeParametersAreNonnullByDefault = __TypeParametersAreNonnullByDefault
from abc import abstractmethod, ABC
 
class TypeParametersAreNonnullByDefault(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.TypeParametersAreNonnullByDefault"""
 
    @staticmethod
    def __wrap(java_value: __TypeParametersAreNonnullByDefault) -> 'TypeParametersAreNonnullByDefault':
        return TypeParametersAreNonnullByDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeParametersAreNonnullByDefault):
        """
        Dynamic initializer for TypeParametersAreNonnullByDefault.
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
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.Modifications as __Modifications
__Modifications = __Modifications
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
 
class Modifications():
    """dev.ultreon.quantum.Modifications"""
 
    @staticmethod
    def __wrap(java_value: __Modifications) -> 'Modifications':
        return Modifications(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Modifications):
        """
        Dynamic initializer for Modifications.
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
 
    # public static final dev.ultreon.quantum.Modifications dev.ultreon.quantum.Modifications.INSTANCE
    INSTANCE: 'Modifications' = __wrap(__Modifications.INSTANCE)


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

    @overload
    def getEnableDomainWarping(self) -> bool:
        """public final boolean dev.ultreon.quantum.Modifications.getEnableDomainWarping()"""
        return bool.__wrap(super(Modifications, self).getEnableDomainWarping())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setEnableDomainWarping(self, arg0: bool):
        """public final void dev.ultreon.quantum.Modifications.setEnableDomainWarping(boolean)"""
        super(__Modifications, self).setEnableDomainWarping(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))