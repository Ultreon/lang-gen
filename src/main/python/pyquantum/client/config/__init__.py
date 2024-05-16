from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.api.Event as __Event
__Event = __Event
from builtins import type
import java.nio.file.Path as __Path
__Path = __Path
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum.config import crafty
except ImportError:
    crafty = __import_once__("pyquantum.config.crafty")

from builtins import bool
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

import dev.ultreon.quantum.config.crafty.CraftyConfig as __CraftyConfig
__CraftyConfig = __CraftyConfig
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.Mod as __Mod
__Mod = __Mod
import java.lang.Integer as __int
import dev.ultreon.quantum.client.config.ClientConfig as __ClientConfig
__ClientConfig = __ClientConfig
import java.util.Map as Map
from builtins import int
 
class ClientConfig():
    """dev.ultreon.quantum.client.config.ClientConfig"""
 
    @staticmethod
    def __wrap(java_value: __ClientConfig) -> 'ClientConfig':
        return ClientConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientConfig):
        """
        Dynamic initializer for ClientConfig.
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

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'crafty.CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return crafty.CraftyConfig.__wrap(__CraftyConfig.getConfig(arg0))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.config.crafty.CraftyConfig.contains(java.lang.String)"""
        return bool.__wrap(super(__crafty.CraftyConfig, self).contains(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.config.ClientConfig()"""
        val = __ClientConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.config.ClientConfig()"""
        val = __ClientConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @property
    def language_(value: 'util.Identifier'):
        """
        Setter for the language property.
     
        :param value: Value to set for the language property.
        """
     
        super('util.Identifier').language(value)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self, arg0: str):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset(java.lang.String)"""
        super(__crafty.CraftyConfig, self).reset(arg0)

    @overload
    def getDefault(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.getDefault(java.lang.String)"""
        return object.__wrap(super(__crafty.CraftyConfig, self).getDefault(arg0))

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
    def reset(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset()"""
        super(crafty.CraftyConfig, self).reset()

    @overload
    def getType(self, arg0: str) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.config.crafty.CraftyConfig.getType(java.lang.String)"""
        return 'type.Class'.__wrap(super(__crafty.CraftyConfig, self).getType(arg0))

        @staticmethod
        @overload
        def update():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.update()"""
            __CraftyConfig.update()

    @override
    @overload
    def getConfigPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigPath()"""
        return 'Path'.__wrap(super(crafty.CraftyConfig, self).getConfigPath())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.config.crafty.CraftyConfig.getMod()"""
        return 'pyquantum.Mod'.__wrap(super(crafty.CraftyConfig, self).getMod())

    @override
    @overload
    def set(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.set(java.lang.String,java.lang.Object)"""
        super(__crafty.CraftyConfig, self).set(arg0, arg1)

    @override
    @overload
    def getAll(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getAll()"""
        return 'Map'.__wrap(super(crafty.CraftyConfig, self).getAll())

    @override
    @overload
    def getFileName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.config.crafty.CraftyConfig.getFileName()"""
        return str.__wrap(super(crafty.CraftyConfig, self).getFileName())

    @staticmethod
    @overload
    def getConfigs() -> 'Collection':
        """public static java.util.Collection<? extends dev.ultreon.quantum.config.crafty.CraftyConfig> dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigs()"""
        return Collection.__wrap(__CraftyConfig.getConfigs())

    @override
    @overload
    def getDefaults(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getDefaults()"""
        return 'Map'.__wrap(super(crafty.CraftyConfig, self).getDefaults())

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.get(java.lang.String)"""
        return object.__wrap(super(__crafty.CraftyConfig, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @property
    def event(self) -> Event:
        return Event.__wrap(super(__CraftyConfig).event())

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
    def load(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.load()"""
        super(crafty.CraftyConfig, self).load()

        @staticmethod
        @overload
        def saveAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.saveAll()"""
            __CraftyConfig.saveAll()

    @staticmethod
    @property
    def language_() -> Identifier:
        """
        Getter for the language property.
     
        :return: Value of language
        """
     
        return super(Identifier).language()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def save(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.save()"""
        super(crafty.CraftyConfig, self).save()

        @staticmethod
        @overload
        def resetAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.resetAll()"""
            __CraftyConfig.resetAll()

 
 
 
# CLASS: dev.ultreon.quantum.client.config.ClientConfig
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.api.Event as __Event
__Event = __Event
from builtins import type
import java.nio.file.Path as __Path
__Path = __Path
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum.config import crafty
except ImportError:
    crafty = __import_once__("pyquantum.config.crafty")

from builtins import bool
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

import dev.ultreon.quantum.config.crafty.CraftyConfig as __CraftyConfig
__CraftyConfig = __CraftyConfig
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.Mod as __Mod
__Mod = __Mod
import java.lang.Integer as __int
import dev.ultreon.quantum.client.config.ClientConfig as __ClientConfig
__ClientConfig = __ClientConfig
import java.util.Map as Map
from builtins import int
 
class ClientConfig():
    """dev.ultreon.quantum.client.config.ClientConfig"""
 
    @staticmethod
    def __wrap(java_value: __ClientConfig) -> 'ClientConfig':
        return ClientConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientConfig):
        """
        Dynamic initializer for ClientConfig.
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

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'crafty.CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return crafty.CraftyConfig.__wrap(__CraftyConfig.getConfig(arg0))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.config.crafty.CraftyConfig.contains(java.lang.String)"""
        return bool.__wrap(super(__crafty.CraftyConfig, self).contains(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.config.ClientConfig()"""
        val = __ClientConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.config.ClientConfig()"""
        val = __ClientConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @property
    def language_(value: 'util.Identifier'):
        """
        Setter for the language property.
     
        :param value: Value to set for the language property.
        """
     
        super('util.Identifier').language(value)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self, arg0: str):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset(java.lang.String)"""
        super(__crafty.CraftyConfig, self).reset(arg0)

    @overload
    def getDefault(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.getDefault(java.lang.String)"""
        return object.__wrap(super(__crafty.CraftyConfig, self).getDefault(arg0))

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
    def reset(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset()"""
        super(crafty.CraftyConfig, self).reset()

    @overload
    def getType(self, arg0: str) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.config.crafty.CraftyConfig.getType(java.lang.String)"""
        return 'type.Class'.__wrap(super(__crafty.CraftyConfig, self).getType(arg0))

        @staticmethod
        @overload
        def update():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.update()"""
            __CraftyConfig.update()

    @override
    @overload
    def getConfigPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigPath()"""
        return 'Path'.__wrap(super(crafty.CraftyConfig, self).getConfigPath())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.config.crafty.CraftyConfig.getMod()"""
        return 'pyquantum.Mod'.__wrap(super(crafty.CraftyConfig, self).getMod())

    @override
    @overload
    def set(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.set(java.lang.String,java.lang.Object)"""
        super(__crafty.CraftyConfig, self).set(arg0, arg1)

    @override
    @overload
    def getAll(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getAll()"""
        return 'Map'.__wrap(super(crafty.CraftyConfig, self).getAll())

    @override
    @overload
    def getFileName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.config.crafty.CraftyConfig.getFileName()"""
        return str.__wrap(super(crafty.CraftyConfig, self).getFileName())

    @staticmethod
    @overload
    def getConfigs() -> 'Collection':
        """public static java.util.Collection<? extends dev.ultreon.quantum.config.crafty.CraftyConfig> dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigs()"""
        return Collection.__wrap(__CraftyConfig.getConfigs())

    @override
    @overload
    def getDefaults(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getDefaults()"""
        return 'Map'.__wrap(super(crafty.CraftyConfig, self).getDefaults())

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.get(java.lang.String)"""
        return object.__wrap(super(__crafty.CraftyConfig, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @property
    def event(self) -> Event:
        return Event.__wrap(super(__CraftyConfig).event())

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
    def load(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.load()"""
        super(crafty.CraftyConfig, self).load()

        @staticmethod
        @overload
        def saveAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.saveAll()"""
            __CraftyConfig.saveAll()

    @staticmethod
    @property
    def language_() -> Identifier:
        """
        Getter for the language property.
     
        :return: Value of language
        """
     
        return super(Identifier).language()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def save(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.save()"""
        super(crafty.CraftyConfig, self).save()

        @staticmethod
        @overload
        def resetAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.resetAll()"""
            __CraftyConfig.resetAll()

 
 
 
# CLASS: dev.ultreon.quantum.client.config.ClientConfig 
 
 
# CLASS: dev.ultreon.quantum.client.config.GameSettings
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

import dev.ultreon.quantum.client.config.GameSettings as __GameSettings
__GameSettings = __GameSettings
import dev.ultreon.quantum.client.config.Configuration as __Configuration
__Configuration = __Configuration
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from builtins import int
 
class GameSettings():
    """dev.ultreon.quantum.client.config.GameSettings"""
 
    @staticmethod
    def __wrap(java_value: __GameSettings) -> 'GameSettings':
        return GameSettings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameSettings):
        """
        Dynamic initializer for GameSettings.
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
    def save(self):
        """public void dev.ultreon.quantum.client.config.GameSettings.save()"""
        super(GameSettings, self).save()

    @property
    def hidePlayerWhenThirdPerson(self) -> ConfigEntry:
        return ConfigEntry.__wrap(super(__GameSettings).hidePlayerWhenThirdPerson())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.config.GameSettings()"""
        val = __GameSettings()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def values(self) -> List['gui.ConfigEntry']:
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<?>[] dev.ultreon.quantum.client.config.Configuration.values()"""
        return List['gui.ConfigEntry'].__wrap(super(Configuration, self).values())

    @property
    def fullscreen(self) -> ConfigEntry:
        return ConfigEntry.__wrap(super(__GameSettings).fullscreen())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'Configuration':
        """public static dev.ultreon.quantum.client.config.Configuration dev.ultreon.quantum.client.config.Configuration.getConfig(java.lang.String)"""
        return Configuration.__wrap(__Configuration.getConfig(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.config.GameSettings()"""
        val = __GameSettings()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @property
    def width(self) -> ConfigEntry:
        return ConfigEntry.__wrap(super(__GameSettings).width())

    @property
    def renderDistance(self) -> ConfigEntry:
        return ConfigEntry.__wrap(super(__GameSettings).renderDistance())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @property
    def guiScale(self) -> ConfigEntry:
        return ConfigEntry.__wrap(super(__GameSettings).guiScale())

    @overload
    def onChanged(self):
        """public void dev.ultreon.quantum.client.config.GameSettings.onChanged()"""
        super(GameSettings, self).onChanged()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @property
    def craftingShowOnlyCraftable(self) -> ConfigEntry:
        return ConfigEntry.__wrap(super(__GameSettings).craftingShowOnlyCraftable())

    @override
    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.Configuration.getId()"""
        return str.__wrap(super(Configuration, self).getId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @property
    def height(self) -> ConfigEntry:
        return ConfigEntry.__wrap(super(__GameSettings).height())

    @override
    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.config.Configuration.reload()"""
        super(Configuration, self).reload()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getHandle(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.config.Configuration.getHandle()"""
        return 'files.FileHandle'.__wrap(super(Configuration, self).getHandle())

    @property
    def language(self) -> ConfigEntry:
        return ConfigEntry.__wrap(super(__GameSettings).language()) 
 
 
# CLASS: dev.ultreon.quantum.client.config.Configuration
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

import dev.ultreon.quantum.client.config.Configuration as __Configuration
__Configuration = __Configuration
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from builtins import int
 
class Configuration():
    """dev.ultreon.quantum.client.config.Configuration"""
 
    @staticmethod
    def __wrap(java_value: __Configuration) -> 'Configuration':
        return Configuration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Configuration):
        """
        Dynamic initializer for Configuration.
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
    def values(self) -> List['gui.ConfigEntry']:
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<?>[] dev.ultreon.quantum.client.config.Configuration.values()"""
        return List['gui.ConfigEntry'].__wrap(super(Configuration, self).values())

    @overload
    def getHandle(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.config.Configuration.getHandle()"""
        return 'files.FileHandle'.__wrap(super(Configuration, self).getHandle())

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

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'Configuration':
        """public static dev.ultreon.quantum.client.config.Configuration dev.ultreon.quantum.client.config.Configuration.getConfig(java.lang.String)"""
        return Configuration.__wrap(__Configuration.getConfig(arg0))

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
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.Configuration.getId()"""
        return str.__wrap(super(Configuration, self).getId())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.config.Configuration.reload()"""
        super(Configuration, self).reload()

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
    def save(self):
        """public void dev.ultreon.quantum.client.config.Configuration.save()"""
        super(Configuration, self).save()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.config.Configuration(java.lang.String)"""
        val = __Configuration(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.config.ConfigScreenFactory
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.config.ConfigScreenFactory as __ConfigScreenFactory
__ConfigScreenFactory = __ConfigScreenFactory
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class ConfigScreenFactory(ABC):
    """dev.ultreon.quantum.client.config.ConfigScreenFactory"""
 
    @staticmethod
    def __wrap(java_value: __ConfigScreenFactory) -> 'ConfigScreenFactory':
        return ConfigScreenFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConfigScreenFactory):
        """
        Dynamic initializer for ConfigScreenFactory.
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
    def create(self, arg0: 'Screen'):
        """public abstract dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.config.ConfigScreenFactory.create(dev.ultreon.quantum.client.gui.Screen)"""
        pass