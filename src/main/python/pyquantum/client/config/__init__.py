from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.api.Event as _Event
_Event = _Event
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.client.config.ClientConfig as _ClientConfig
_ClientConfig = _ClientConfig
import java.util.Collection as Collection
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
try:
    from pyquantum.config import crafty
except ImportError:
    crafty = _import_once("pyquantum.config.crafty")

from builtins import bool
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.Mod as _Mod
_Mod = _Mod
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.config.crafty.CraftyConfig as _CraftyConfig
_CraftyConfig = _CraftyConfig
import java.util.Map as Map
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ClientConfig():
    """dev.ultreon.quantum.client.config.ClientConfig"""
 
    @staticmethod
    def _wrap(java_value: _ClientConfig) -> 'ClientConfig':
        return ClientConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientConfig):
        """
        Dynamic initializer for ClientConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientConfig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @property
    def event(self) -> Event:
        return Event._wrap(super(_CraftyConfig).event())

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'crafty.CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return crafty.CraftyConfig._wrap(_CraftyConfig.getConfig(arg0))

    @staticmethod
    @property
    def language_(value: 'util.Identifier'):
        """
        Setter for the language property.
     
        :param value: Value to set for the language property.
        """
     
        super('util.Identifier').language(value)

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

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.config.crafty.CraftyConfig.contains(java.lang.String)"""
        return bool._wrap(super(_crafty.CraftyConfig, self).contains(arg0))

        @staticmethod
        @overload
        def resetAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.resetAll()"""
            _CraftyConfig.resetAll()

    @override
    @overload
    def reset(self, arg0: str):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset(java.lang.String)"""
        super(_crafty.CraftyConfig, self).reset(arg0)

    @overload
    def getDefault(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.getDefault(java.lang.String)"""
        return object._wrap(super(_crafty.CraftyConfig, self).getDefault(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.config.ClientConfig()"""
        val = _ClientConfig()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.get(java.lang.String)"""
        return object._wrap(super(_crafty.CraftyConfig, self).get(arg0))

    @override
    @overload
    def reset(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset()"""
        super(crafty.CraftyConfig, self).reset()

    @override
    @overload
    def getConfigPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigPath()"""
        return 'Path'._wrap(super(crafty.CraftyConfig, self).getConfigPath())

    @override
    @overload
    def getDefaults(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getDefaults()"""
        return 'Map'._wrap(super(crafty.CraftyConfig, self).getDefaults())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.config.ClientConfig()"""
        val = _ClientConfig()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getFileName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.config.crafty.CraftyConfig.getFileName()"""
        return str._wrap(super(crafty.CraftyConfig, self).getFileName())

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.load()"""
        super(crafty.CraftyConfig, self).load()

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

    @override
    @overload
    def getAll(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getAll()"""
        return 'Map'._wrap(super(crafty.CraftyConfig, self).getAll())

    @override
    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.config.crafty.CraftyConfig.getMod()"""
        return 'pyquantum.Mod'._wrap(super(crafty.CraftyConfig, self).getMod())

        @staticmethod
        @overload
        def loadAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.loadAll()"""
            _CraftyConfig.loadAll()

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
    def set(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.set(java.lang.String,java.lang.Object)"""
        super(_crafty.CraftyConfig, self).set(arg0, arg1)

    @override
    @overload
    def save(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.save()"""
        super(crafty.CraftyConfig, self).save()

    @overload
    def getType(self, arg0: str) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.config.crafty.CraftyConfig.getType(java.lang.String)"""
        return 'type.Class'._wrap(super(_crafty.CraftyConfig, self).getType(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.config.ClientConfig
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.api.Event as _Event
_Event = _Event
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.client.config.ClientConfig as _ClientConfig
_ClientConfig = _ClientConfig
import java.util.Collection as Collection
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
try:
    from pyquantum.config import crafty
except ImportError:
    crafty = _import_once("pyquantum.config.crafty")

from builtins import bool
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.Mod as _Mod
_Mod = _Mod
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.config.crafty.CraftyConfig as _CraftyConfig
_CraftyConfig = _CraftyConfig
import java.util.Map as Map
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ClientConfig():
    """dev.ultreon.quantum.client.config.ClientConfig"""
 
    @staticmethod
    def _wrap(java_value: _ClientConfig) -> 'ClientConfig':
        return ClientConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientConfig):
        """
        Dynamic initializer for ClientConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientConfig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @property
    def event(self) -> Event:
        return Event._wrap(super(_CraftyConfig).event())

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'crafty.CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return crafty.CraftyConfig._wrap(_CraftyConfig.getConfig(arg0))

    @staticmethod
    @property
    def language_(value: 'util.Identifier'):
        """
        Setter for the language property.
     
        :param value: Value to set for the language property.
        """
     
        super('util.Identifier').language(value)

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

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.config.crafty.CraftyConfig.contains(java.lang.String)"""
        return bool._wrap(super(_crafty.CraftyConfig, self).contains(arg0))

        @staticmethod
        @overload
        def resetAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.resetAll()"""
            _CraftyConfig.resetAll()

    @override
    @overload
    def reset(self, arg0: str):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset(java.lang.String)"""
        super(_crafty.CraftyConfig, self).reset(arg0)

    @overload
    def getDefault(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.getDefault(java.lang.String)"""
        return object._wrap(super(_crafty.CraftyConfig, self).getDefault(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.config.ClientConfig()"""
        val = _ClientConfig()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.config.crafty.CraftyConfig.get(java.lang.String)"""
        return object._wrap(super(_crafty.CraftyConfig, self).get(arg0))

    @override
    @overload
    def reset(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.reset()"""
        super(crafty.CraftyConfig, self).reset()

    @override
    @overload
    def getConfigPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.config.crafty.CraftyConfig.getConfigPath()"""
        return 'Path'._wrap(super(crafty.CraftyConfig, self).getConfigPath())

    @override
    @overload
    def getDefaults(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getDefaults()"""
        return 'Map'._wrap(super(crafty.CraftyConfig, self).getDefaults())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.config.ClientConfig()"""
        val = _ClientConfig()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getFileName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.config.crafty.CraftyConfig.getFileName()"""
        return str._wrap(super(crafty.CraftyConfig, self).getFileName())

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.load()"""
        super(crafty.CraftyConfig, self).load()

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

    @override
    @overload
    def getAll(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Object> dev.ultreon.quantum.config.crafty.CraftyConfig.getAll()"""
        return 'Map'._wrap(super(crafty.CraftyConfig, self).getAll())

    @override
    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.config.crafty.CraftyConfig.getMod()"""
        return 'pyquantum.Mod'._wrap(super(crafty.CraftyConfig, self).getMod())

        @staticmethod
        @overload
        def loadAll():
            """public static void dev.ultreon.quantum.config.crafty.CraftyConfig.loadAll()"""
            _CraftyConfig.loadAll()

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
    def set(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.set(java.lang.String,java.lang.Object)"""
        super(_crafty.CraftyConfig, self).set(arg0, arg1)

    @override
    @overload
    def save(self):
        """public void dev.ultreon.quantum.config.crafty.CraftyConfig.save()"""
        super(crafty.CraftyConfig, self).save()

    @overload
    def getType(self, arg0: str) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.config.crafty.CraftyConfig.getType(java.lang.String)"""
        return 'type.Class'._wrap(super(_crafty.CraftyConfig, self).getType(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.config.ClientConfig 
 
 
# CLASS: dev.ultreon.quantum.client.config.GameSettings
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.config.GameSettings as _GameSettings
_GameSettings = _GameSettings
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
from typing import List
import java.lang.String as _string
import dev.ultreon.quantum.client.config.Configuration as _Configuration
_Configuration = _Configuration
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameSettings():
    """dev.ultreon.quantum.client.config.GameSettings"""
 
    @staticmethod
    def _wrap(java_value: _GameSettings) -> 'GameSettings':
        return GameSettings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameSettings):
        """
        Dynamic initializer for GameSettings.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameSettings__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameSettings__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def save(self):
        """public void dev.ultreon.quantum.client.config.GameSettings.save()"""
        super(GameSettings, self).save()

    @override
    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.Configuration.getId()"""
        return str._wrap(super(Configuration, self).getId())

    @property
    def width(self) -> ConfigEntry:
        return ConfigEntry._wrap(super(_GameSettings).width())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
        """public dev.ultreon.quantum.client.config.GameSettings()"""
        val = _GameSettings()
        self.__wrapper = val

    @overload
    def onChanged(self):
        """public void dev.ultreon.quantum.client.config.GameSettings.onChanged()"""
        super(GameSettings, self).onChanged()

    @property
    def height(self) -> ConfigEntry:
        return ConfigEntry._wrap(super(_GameSettings).height())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'Configuration':
        """public static dev.ultreon.quantum.client.config.Configuration dev.ultreon.quantum.client.config.Configuration.getConfig(java.lang.String)"""
        return Configuration._wrap(_Configuration.getConfig(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.config.GameSettings()"""
        val = _GameSettings()
        self.__wrapper = val

    @override
    @overload
    def values(self) -> List['gui.ConfigEntry']:
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<?>[] dev.ultreon.quantum.client.config.Configuration.values()"""
        return List['gui.ConfigEntry']._wrap(super(Configuration, self).values())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @property
    def fullscreen(self) -> ConfigEntry:
        return ConfigEntry._wrap(super(_GameSettings).fullscreen())

    @property
    def language(self) -> ConfigEntry:
        return ConfigEntry._wrap(super(_GameSettings).language())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @property
    def renderDistance(self) -> ConfigEntry:
        return ConfigEntry._wrap(super(_GameSettings).renderDistance())

    @override
    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.config.Configuration.reload()"""
        super(Configuration, self).reload()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @property
    def guiScale(self) -> ConfigEntry:
        return ConfigEntry._wrap(super(_GameSettings).guiScale())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @property
    def craftingShowOnlyCraftable(self) -> ConfigEntry:
        return ConfigEntry._wrap(super(_GameSettings).craftingShowOnlyCraftable())

    @property
    def hidePlayerWhenThirdPerson(self) -> ConfigEntry:
        return ConfigEntry._wrap(super(_GameSettings).hidePlayerWhenThirdPerson())

    @override
    @overload
    def getHandle(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.config.Configuration.getHandle()"""
        return 'files.FileHandle'._wrap(super(Configuration, self).getHandle())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.config.Configuration
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
from typing import List
import java.lang.String as _string
import dev.ultreon.quantum.client.config.Configuration as _Configuration
_Configuration = _Configuration
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Configuration():
    """dev.ultreon.quantum.client.config.Configuration"""
 
    @staticmethod
    def _wrap(java_value: _Configuration) -> 'Configuration':
        return Configuration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Configuration):
        """
        Dynamic initializer for Configuration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Configuration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Configuration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'Configuration':
        """public static dev.ultreon.quantum.client.config.Configuration dev.ultreon.quantum.client.config.Configuration.getConfig(java.lang.String)"""
        return Configuration._wrap(_Configuration.getConfig(arg0))

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

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.config.Configuration.reload()"""
        super(Configuration, self).reload()

    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.Configuration.getId()"""
        return str._wrap(super(Configuration, self).getId())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def values(self) -> List['gui.ConfigEntry']:
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<?>[] dev.ultreon.quantum.client.config.Configuration.values()"""
        return List['gui.ConfigEntry']._wrap(super(Configuration, self).values())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.config.Configuration(java.lang.String)"""
        val = _Configuration(arg0)
        self.__wrapper = val

    @overload
    def save(self):
        """public void dev.ultreon.quantum.client.config.Configuration.save()"""
        super(Configuration, self).save()

    @overload
    def getHandle(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.config.Configuration.getHandle()"""
        return 'files.FileHandle'._wrap(super(Configuration, self).getHandle())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.config.ConfigScreenFactory
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.config.ConfigScreenFactory as _ConfigScreenFactory
_ConfigScreenFactory = _ConfigScreenFactory
 
class ConfigScreenFactory():
    """dev.ultreon.quantum.client.config.ConfigScreenFactory"""
 
    @staticmethod
    def _wrap(java_value: _ConfigScreenFactory) -> 'ConfigScreenFactory':
        return ConfigScreenFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConfigScreenFactory):
        """
        Dynamic initializer for ConfigScreenFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConfigScreenFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConfigScreenFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, arg0: 'Screen'):
        """public abstract dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.config.ConfigScreenFactory.create(dev.ultreon.quantum.client.gui.Screen)"""
        pass