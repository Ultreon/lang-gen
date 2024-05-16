from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

import dev.ultreon.quantum.events.api.Event as _Event
_Event = _Event
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.Mod as _Mod
_Mod = _Mod
import dev.ultreon.quantum.config.crafty.CraftyConfig as _CraftyConfig
_CraftyConfig = _CraftyConfig
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class CraftyConfig():
    """dev.ultreon.quantum.config.crafty.CraftyConfig"""
 
    @staticmethod
    def _wrap(java_value: _CraftyConfig) -> 'CraftyConfig':
        return CraftyConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CraftyConfig):
        """
        Dynamic initializer for CraftyConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CraftyConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CraftyConfig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @property
    def event(self) -> Event:
        return Event._wrap(super(_CraftyConfig).event())

    @overload
    def save(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.save()"""
        super(CraftyConfig, self).save()

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return CraftyConfig._wrap(_CraftyConfig.getConfig(arg0))

    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.config.crafty.CraftyConfig.getMod()"""
        return 'pyquantum.Mod'._wrap(super(CraftyConfig, self).getMod())

    @overload
    def getConfigPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigPath()"""
        return 'Path'._wrap(super(CraftyConfig, self).getConfigPath())

    @staticmethod
    @overload
    def getConfigs() -> 'Collection':
        """public static java.util.Collection<? extends dev.ultreon.quantum.config.crafty.CraftyConfig> dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigs()"""
        return Collection._wrap(_CraftyConfig.getConfigs())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

        @staticmethod
        @overload
        def resetAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.resetAll()"""
            _CraftyConfig.resetAll()

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
    def __init__(self, ):
        """public dev.ultreon.quantum.config.crafty.CraftyConfig()"""
        val = _CraftyConfig()
        self.__wrapper = val

    @overload
    def reset(self, arg0: str):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset(java.lang.String)"""
        super(_CraftyConfig, self).reset(arg0)

    @overload
    def getAll(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getAll()"""
        return 'Map'._wrap(super(CraftyConfig, self).getAll())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.config.crafty.CraftyConfig()"""
        val = _CraftyConfig()
        self.__wrapper = val

        @staticmethod
        @overload
        def update():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.update()"""
            _CraftyConfig.update()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getDefault(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.getDefault(java.lang.String)"""
        return object._wrap(super(_CraftyConfig, self).getDefault(arg0))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.config.crafty.CraftyConfig.contains(java.lang.String)"""
        return bool._wrap(super(_CraftyConfig, self).contains(arg0))

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.get(java.lang.String)"""
        return object._wrap(super(_CraftyConfig, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def reset(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset()"""
        super(CraftyConfig, self).reset()

    @overload
    def getType(self, arg0: str) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.config.crafty.CraftyConfig.getType(java.lang.String)"""
        return 'type.Class'._wrap(super(_CraftyConfig, self).getType(arg0))

    @overload
    def set(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.set(java.lang.String,java.lang.Object)"""
        super(_CraftyConfig, self).set(arg0, arg1)

    @overload
    def getDefaults(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getDefaults()"""
        return 'Map'._wrap(super(CraftyConfig, self).getDefaults())

        @staticmethod
        @overload
        def saveAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.saveAll()"""
            _CraftyConfig.saveAll()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

        @staticmethod
        @overload
        def loadAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.loadAll()"""
            _CraftyConfig.loadAll()

    @overload
    def load(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.load()"""
        super(CraftyConfig, self).load()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFileName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.config.crafty.CraftyConfig.getFileName()"""
        return str._wrap(super(CraftyConfig, self).getFileName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.config.crafty.CraftyConfig
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

import dev.ultreon.quantum.events.api.Event as _Event
_Event = _Event
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.Mod as _Mod
_Mod = _Mod
import dev.ultreon.quantum.config.crafty.CraftyConfig as _CraftyConfig
_CraftyConfig = _CraftyConfig
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class CraftyConfig():
    """dev.ultreon.quantum.config.crafty.CraftyConfig"""
 
    @staticmethod
    def _wrap(java_value: _CraftyConfig) -> 'CraftyConfig':
        return CraftyConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CraftyConfig):
        """
        Dynamic initializer for CraftyConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CraftyConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CraftyConfig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @property
    def event(self) -> Event:
        return Event._wrap(super(_CraftyConfig).event())

    @overload
    def save(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.save()"""
        super(CraftyConfig, self).save()

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return CraftyConfig._wrap(_CraftyConfig.getConfig(arg0))

    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.config.crafty.CraftyConfig.getMod()"""
        return 'pyquantum.Mod'._wrap(super(CraftyConfig, self).getMod())

    @overload
    def getConfigPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigPath()"""
        return 'Path'._wrap(super(CraftyConfig, self).getConfigPath())

    @staticmethod
    @overload
    def getConfigs() -> 'Collection':
        """public static java.util.Collection<? extends dev.ultreon.quantum.config.crafty.CraftyConfig> dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigs()"""
        return Collection._wrap(_CraftyConfig.getConfigs())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

        @staticmethod
        @overload
        def resetAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.resetAll()"""
            _CraftyConfig.resetAll()

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
    def __init__(self, ):
        """public dev.ultreon.quantum.config.crafty.CraftyConfig()"""
        val = _CraftyConfig()
        self.__wrapper = val

    @overload
    def reset(self, arg0: str):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset(java.lang.String)"""
        super(_CraftyConfig, self).reset(arg0)

    @overload
    def getAll(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getAll()"""
        return 'Map'._wrap(super(CraftyConfig, self).getAll())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.config.crafty.CraftyConfig()"""
        val = _CraftyConfig()
        self.__wrapper = val

        @staticmethod
        @overload
        def update():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.update()"""
            _CraftyConfig.update()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getDefault(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.getDefault(java.lang.String)"""
        return object._wrap(super(_CraftyConfig, self).getDefault(arg0))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.config.crafty.CraftyConfig.contains(java.lang.String)"""
        return bool._wrap(super(_CraftyConfig, self).contains(arg0))

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.get(java.lang.String)"""
        return object._wrap(super(_CraftyConfig, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def reset(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset()"""
        super(CraftyConfig, self).reset()

    @overload
    def getType(self, arg0: str) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.config.crafty.CraftyConfig.getType(java.lang.String)"""
        return 'type.Class'._wrap(super(_CraftyConfig, self).getType(arg0))

    @overload
    def set(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.set(java.lang.String,java.lang.Object)"""
        super(_CraftyConfig, self).set(arg0, arg1)

    @overload
    def getDefaults(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getDefaults()"""
        return 'Map'._wrap(super(CraftyConfig, self).getDefaults())

        @staticmethod
        @overload
        def saveAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.saveAll()"""
            _CraftyConfig.saveAll()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

        @staticmethod
        @overload
        def loadAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.loadAll()"""
            _CraftyConfig.loadAll()

    @overload
    def load(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.load()"""
        super(CraftyConfig, self).load()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFileName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.config.crafty.CraftyConfig.getFileName()"""
        return str._wrap(super(CraftyConfig, self).getFileName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.config.crafty.CraftyConfig 
 
 
# CLASS: dev.ultreon.quantum.config.crafty.ConfigEntry
import dev.ultreon.quantum.config.crafty.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class ConfigEntry():
    """dev.ultreon.quantum.config.crafty.ConfigEntry"""
 
    @staticmethod
    def _wrap(java_value: _ConfigEntry) -> 'ConfigEntry':
        return ConfigEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConfigEntry):
        """
        Dynamic initializer for ConfigEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConfigEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConfigEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import dev.ultreon.quantum.config.crafty.RequiresRestart as _RequiresRestart
_RequiresRestart = _RequiresRestart
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class RequiresRestart():
    """dev.ultreon.quantum.config.crafty.RequiresRestart"""
 
    @staticmethod
    def _wrap(java_value: _RequiresRestart) -> 'RequiresRestart':
        return RequiresRestart(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RequiresRestart):
        """
        Dynamic initializer for RequiresRestart.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RequiresRestart__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RequiresRestart__wrapper":
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
 
 
# CLASS: dev.ultreon.quantum.config.crafty.CraftyConfig$LoadConfig
import dev.ultreon.quantum.config.crafty.CraftyConfig as _CraftyConfig_LoadConfig
_LoadConfig = _CraftyConfig_LoadConfig.LoadConfig
from abc import abstractmethod, ABC
 
class LoadConfig():
    """dev.ultreon.quantum.config.crafty.CraftyConfig.LoadConfig"""
 
    @staticmethod
    def _wrap(java_value: _LoadConfig) -> 'LoadConfig':
        return LoadConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadConfig):
        """
        Dynamic initializer for LoadConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadConfig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def load(self, ):
        """public abstract void dev.ultreon.quantum.config.crafty.CraftyConfig$LoadConfig.load() throws java.io.IOException"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.config.crafty.ConfigInfo
import dev.ultreon.quantum.config.crafty.ConfigInfo as _ConfigInfo
_ConfigInfo = _ConfigInfo
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class ConfigInfo():
    """dev.ultreon.quantum.config.crafty.ConfigInfo"""
 
    @staticmethod
    def _wrap(java_value: _ConfigInfo) -> 'ConfigInfo':
        return ConfigInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConfigInfo):
        """
        Dynamic initializer for ConfigInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConfigInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConfigInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import dev.ultreon.quantum.config.crafty.Ranged as _Ranged
_Ranged = _Ranged
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class Ranged():
    """dev.ultreon.quantum.config.crafty.Ranged"""
 
    @staticmethod
    def _wrap(java_value: _Ranged) -> 'Ranged':
        return Ranged(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ranged):
        """
        Dynamic initializer for Ranged.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ranged__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ranged__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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