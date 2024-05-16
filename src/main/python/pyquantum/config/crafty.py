from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.api.Event as __Event
__Event = __Event
import dev.ultreon.quantum.config.crafty.CraftyConfig as __CraftyConfig
__CraftyConfig = __CraftyConfig
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.file.Path as __Path
__Path = __Path
import java.util.Map as __Map
__Map = __Map
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

import java.util.Collection as Collection
from builtins import object
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.Mod as __Mod
__Mod = __Mod
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class CraftyConfig(ABC):
    """dev.ultreon.quantum.config.crafty.CraftyConfig"""
 
    @staticmethod
    def __wrap(java_value: __CraftyConfig) -> 'CraftyConfig':
        return CraftyConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CraftyConfig):
        """
        Dynamic initializer for CraftyConfig.
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
        def loadAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.loadAll()"""
            __CraftyConfig.loadAll()

    @overload
    def reset(self, arg0: str):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset(java.lang.String)"""
        super(__CraftyConfig, self).reset(arg0)

    @overload
    def save(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.save()"""
        super(CraftyConfig, self).save()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.config.crafty.CraftyConfig()"""
        val = __CraftyConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.config.crafty.CraftyConfig.getMod()"""
        return 'pyquantum.Mod'.__wrap(super(CraftyConfig, self).getMod())

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

        @staticmethod
        @overload
        def update():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.update()"""
            __CraftyConfig.update()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getType(self, arg0: str) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.config.crafty.CraftyConfig.getType(java.lang.String)"""
        return 'type.Class'.__wrap(super(__CraftyConfig, self).getType(arg0))

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return CraftyConfig.__wrap(__CraftyConfig.getConfig(arg0))

    @overload
    def getDefaults(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getDefaults()"""
        return 'Map'.__wrap(super(CraftyConfig, self).getDefaults())

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.config.crafty.CraftyConfig.contains(java.lang.String)"""
        return bool.__wrap(super(__CraftyConfig, self).contains(arg0))

    @staticmethod
    @overload
    def getConfigs() -> 'Collection':
        """public static java.util.Collection<? extends dev.ultreon.quantum.config.crafty.CraftyConfig> dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigs()"""
        return Collection.__wrap(__CraftyConfig.getConfigs())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getFileName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.config.crafty.CraftyConfig.getFileName()"""
        return str.__wrap(super(CraftyConfig, self).getFileName())

    @property
    def event(self) -> Event:
        return Event.__wrap(super(__CraftyConfig).event())

    @overload
    def getConfigPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigPath()"""
        return 'Path'.__wrap(super(CraftyConfig, self).getConfigPath())

    @overload
    def reset(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset()"""
        super(CraftyConfig, self).reset()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getDefault(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.getDefault(java.lang.String)"""
        return object.__wrap(super(__CraftyConfig, self).getDefault(arg0))

    @overload
    def set(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.set(java.lang.String,java.lang.Object)"""
        super(__CraftyConfig, self).set(arg0, arg1)

    @overload
    def getAll(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getAll()"""
        return 'Map'.__wrap(super(CraftyConfig, self).getAll())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.get(java.lang.String)"""
        return object.__wrap(super(__CraftyConfig, self).get(arg0))

        @staticmethod
        @overload
        def saveAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.saveAll()"""
            __CraftyConfig.saveAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.config.crafty.CraftyConfig()"""
        val = __CraftyConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def load(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.load()"""
        super(CraftyConfig, self).load()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

        @staticmethod
        @overload
        def resetAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.resetAll()"""
            __CraftyConfig.resetAll()

 
 
 
# CLASS: dev.ultreon.quantum.config.crafty.CraftyConfig
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.api.Event as __Event
__Event = __Event
import dev.ultreon.quantum.config.crafty.CraftyConfig as __CraftyConfig
__CraftyConfig = __CraftyConfig
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.file.Path as __Path
__Path = __Path
import java.util.Map as __Map
__Map = __Map
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

import java.util.Collection as Collection
from builtins import object
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.Mod as __Mod
__Mod = __Mod
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class CraftyConfig(ABC):
    """dev.ultreon.quantum.config.crafty.CraftyConfig"""
 
    @staticmethod
    def __wrap(java_value: __CraftyConfig) -> 'CraftyConfig':
        return CraftyConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CraftyConfig):
        """
        Dynamic initializer for CraftyConfig.
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
        def loadAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.loadAll()"""
            __CraftyConfig.loadAll()

    @overload
    def reset(self, arg0: str):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset(java.lang.String)"""
        super(__CraftyConfig, self).reset(arg0)

    @overload
    def save(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.save()"""
        super(CraftyConfig, self).save()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.config.crafty.CraftyConfig()"""
        val = __CraftyConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.config.crafty.CraftyConfig.getMod()"""
        return 'pyquantum.Mod'.__wrap(super(CraftyConfig, self).getMod())

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

        @staticmethod
        @overload
        def update():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.update()"""
            __CraftyConfig.update()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getType(self, arg0: str) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.config.crafty.CraftyConfig.getType(java.lang.String)"""
        return 'type.Class'.__wrap(super(__CraftyConfig, self).getType(arg0))

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return CraftyConfig.__wrap(__CraftyConfig.getConfig(arg0))

    @overload
    def getDefaults(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getDefaults()"""
        return 'Map'.__wrap(super(CraftyConfig, self).getDefaults())

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.config.crafty.CraftyConfig.contains(java.lang.String)"""
        return bool.__wrap(super(__CraftyConfig, self).contains(arg0))

    @staticmethod
    @overload
    def getConfigs() -> 'Collection':
        """public static java.util.Collection<? extends dev.ultreon.quantum.config.crafty.CraftyConfig> dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigs()"""
        return Collection.__wrap(__CraftyConfig.getConfigs())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getFileName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.config.crafty.CraftyConfig.getFileName()"""
        return str.__wrap(super(CraftyConfig, self).getFileName())

    @property
    def event(self) -> Event:
        return Event.__wrap(super(__CraftyConfig).event())

    @overload
    def getConfigPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigPath()"""
        return 'Path'.__wrap(super(CraftyConfig, self).getConfigPath())

    @overload
    def reset(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset()"""
        super(CraftyConfig, self).reset()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getDefault(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.getDefault(java.lang.String)"""
        return object.__wrap(super(__CraftyConfig, self).getDefault(arg0))

    @overload
    def set(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.set(java.lang.String,java.lang.Object)"""
        super(__CraftyConfig, self).set(arg0, arg1)

    @overload
    def getAll(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getAll()"""
        return 'Map'.__wrap(super(CraftyConfig, self).getAll())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.get(java.lang.String)"""
        return object.__wrap(super(__CraftyConfig, self).get(arg0))

        @staticmethod
        @overload
        def saveAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.saveAll()"""
            __CraftyConfig.saveAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.config.crafty.CraftyConfig()"""
        val = __CraftyConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def load(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.load()"""
        super(CraftyConfig, self).load()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

        @staticmethod
        @overload
        def resetAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.resetAll()"""
            __CraftyConfig.resetAll()

 
 
 
# CLASS: dev.ultreon.quantum.config.crafty.CraftyConfig 
 
 
# CLASS: dev.ultreon.quantum.config.crafty.ConfigEntry
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.config.crafty.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from abc import abstractmethod, ABC
 
class ConfigEntry(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.config.crafty.ConfigEntry"""
 
    @staticmethod
    def __wrap(java_value: __ConfigEntry) -> 'ConfigEntry':
        return ConfigEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConfigEntry):
        """
        Dynamic initializer for ConfigEntry.
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
    def path(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.config.crafty.ConfigEntry.path()"""
        pass

    @abstractmethod
    def defaulted(self, ):
        """public abstract boolean dev.ultreon.quantum.config.crafty.ConfigEntry.defaulted()"""
        pass

    @abstractmethod
    def comment(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.config.crafty.ConfigEntry.comment()"""
        pass

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
 
 
# CLASS: dev.ultreon.quantum.config.crafty.RequiresRestart
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.config.crafty.RequiresRestart as __RequiresRestart
__RequiresRestart = __RequiresRestart
from abc import abstractmethod, ABC
 
class RequiresRestart(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.config.crafty.RequiresRestart"""
 
    @staticmethod
    def __wrap(java_value: __RequiresRestart) -> 'RequiresRestart':
        return RequiresRestart(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RequiresRestart):
        """
        Dynamic initializer for RequiresRestart.
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
 
 
# CLASS: dev.ultreon.quantum.config.crafty.CraftyConfig$LoadConfig
import dev.ultreon.quantum.config.crafty.CraftyConfig as __CraftyConfig_LoadConfig
__LoadConfig = __CraftyConfig_LoadConfig.LoadConfig
from abc import abstractmethod, ABC
 
class LoadConfig(ABC):
    """dev.ultreon.quantum.config.crafty.CraftyConfig.LoadConfig"""
 
    @staticmethod
    def __wrap(java_value: __LoadConfig) -> 'LoadConfig':
        return LoadConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadConfig):
        """
        Dynamic initializer for LoadConfig.
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
    def load(self, ):
        """public abstract void dev.ultreon.quantum.config.crafty.CraftyConfig$LoadConfig.load() throws java.io.IOException"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.config.crafty.ConfigInfo
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import dev.ultreon.quantum.config.crafty.ConfigInfo as __ConfigInfo
__ConfigInfo = __ConfigInfo
 
class ConfigInfo(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.config.crafty.ConfigInfo"""
 
    @staticmethod
    def __wrap(java_value: __ConfigInfo) -> 'ConfigInfo':
        return ConfigInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConfigInfo):
        """
        Dynamic initializer for ConfigInfo.
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
    def fileName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.config.crafty.ConfigInfo.fileName()"""
        pass

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
 
 
# CLASS: dev.ultreon.quantum.config.crafty.Ranged
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import dev.ultreon.quantum.config.crafty.Ranged as __Ranged
__Ranged = __Ranged
 
class Ranged(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.config.crafty.Ranged"""
 
    @staticmethod
    def __wrap(java_value: __Ranged) -> 'Ranged':
        return Ranged(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ranged):
        """
        Dynamic initializer for Ranged.
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
    def max(self, ):
        """public abstract double dev.ultreon.quantum.config.crafty.Ranged.max()"""
        pass

    @abstractmethod
    def min(self, ):
        """public abstract double dev.ultreon.quantum.config.crafty.Ranged.min()"""
        pass

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