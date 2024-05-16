from __future__ import annotations
from overload import overload


 
from abc import abstractmethod, ABC
import dev.ultreon.quantum.server.dedicated.DedicatedServerModInit as _DedicatedServerModInit
_DedicatedServerModInit = _DedicatedServerModInit
 
class DedicatedServerModInit():
    """dev.ultreon.quantum.server.dedicated.DedicatedServerModInit"""
 
    @staticmethod
    def _wrap(java_value: _DedicatedServerModInit) -> 'DedicatedServerModInit':
        return DedicatedServerModInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DedicatedServerModInit):
        """
        Dynamic initializer for DedicatedServerModInit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DedicatedServerModInit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DedicatedServerModInit__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onInitialize(self, ):
        """public abstract void dev.ultreon.quantum.server.dedicated.DedicatedServerModInit.onInitialize()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.DedicatedServerModInit
from abc import abstractmethod, ABC
import dev.ultreon.quantum.server.dedicated.DedicatedServerModInit as _DedicatedServerModInit
_DedicatedServerModInit = _DedicatedServerModInit
 
class DedicatedServerModInit():
    """dev.ultreon.quantum.server.dedicated.DedicatedServerModInit"""
 
    @staticmethod
    def _wrap(java_value: _DedicatedServerModInit) -> 'DedicatedServerModInit':
        return DedicatedServerModInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DedicatedServerModInit):
        """
        Dynamic initializer for DedicatedServerModInit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DedicatedServerModInit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DedicatedServerModInit__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onInitialize(self, ):
        """public abstract void dev.ultreon.quantum.server.dedicated.DedicatedServerModInit.onInitialize()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.DedicatedServerModInit 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.ServerConfig
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.api.Event as _Event
_Event = _Event
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
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
import dev.ultreon.quantum.server.dedicated.ServerConfig as _ServerConfig
_ServerConfig = _ServerConfig
import java.nio.file.Path as Path
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.Mod as _Mod
_Mod = _Mod
import dev.ultreon.quantum.config.crafty.CraftyConfig as _CraftyConfig
_CraftyConfig = _CraftyConfig
import java.util.Map as Map
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ServerConfig():
    """dev.ultreon.quantum.server.dedicated.ServerConfig"""
 
    @staticmethod
    def _wrap(java_value: _ServerConfig) -> 'ServerConfig':
        return ServerConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerConfig):
        """
        Dynamic initializer for ServerConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerConfig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @property
    def event(self) -> Event:
        return Event._wrap(super(_CraftyConfig).event())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.dedicated.ServerConfig()"""
        val = _ServerConfig()
        self.__wrapper = val

    @staticmethod
    @overload
    def getConfig(arg0: str) -> 'crafty.CraftyConfig':
        """public static dev.ultreon.quantum.config.crafty.CraftyConfig dev.ultreon.quantum.config.crafty.CraftyConfig.getConfig(java.lang.String)"""
        return crafty.CraftyConfig._wrap(_CraftyConfig.getConfig(arg0))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.dedicated.ServerConfig()"""
        val = _ServerConfig()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.DedicatedServer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

import java.util.UUID as UUID
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

try:
    from pyquantum import recipe
except ImportError:
    recipe = _import_once("pyquantum.recipe")

import java.util.Collection as Collection
try:
    from pyquantum import crash
except ImportError:
    crash = _import_once("pyquantum.crash")

import dev.ultreon.quantum.server.player.ServerPlayer as _ServerPlayer
_ServerPlayer = _ServerPlayer
import java.lang.Boolean as _boolean
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = _import_once("pyquantum.debug.profiler")

import java.util.concurrent.Callable as Callable
import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
try:
    from pyquantum import gamerule
except ImportError:
    gamerule = _import_once("pyquantum.gamerule")

import dev.ultreon.quantum.server.player.CacheablePlayer as _CacheablePlayer
_CacheablePlayer = _CacheablePlayer
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.world.ServerWorld as _ServerWorld
_ServerWorld = _ServerWorld
import java.lang.Object as _object
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
import dev.ultreon.quantum.server.dedicated.DedicatedServer as _DedicatedServer
_DedicatedServer = _DedicatedServer
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import java.util.Collection as _Collection
_Collection = _Collection
import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import java.util.concurrent.CompletableFuture as CompletableFuture
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import dev.ultreon.quantum.util.PollingExecutorService as _PollingExecutorService
_PollingExecutorService = _PollingExecutorService
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.server.PlayerManager as _PlayerManager
_PlayerManager = _PlayerManager
import java.lang.String as _string
import java.lang.Exception as Exception
import dev.ultreon.quantum.network.Networker as _Networker
_Networker = _Networker
import dev.ultreon.quantum.server.player.PermissionMap as _PermissionMap
_PermissionMap = _PermissionMap
import java.util.concurrent.ScheduledFuture as ScheduledFuture
import dev.ultreon.quantum.debug.profiler.Profiler as _Profiler
_Profiler = _Profiler
import dev.ultreon.quantum.recipe.RecipeManager as _RecipeManager
_RecipeManager = _RecipeManager
import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.server.ServerDisposable as _ServerDisposable
_ServerDisposable = _ServerDisposable
try:
    from pyquantum.debug import inspect
except ImportError:
    inspect = _import_once("pyquantum.debug.inspect")

import java.lang.Runnable as Runnable
import dev.ultreon.quantum.gamerule.GameRules as _GameRules
_GameRules = _GameRules
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.resources.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
from builtins import object
import dev.ultreon.quantum.server.player.CachedPlayer as _CachedPlayer
_CachedPlayer = _CachedPlayer
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import java.util.concurrent.ScheduledFuture as _ScheduledFuture
_ScheduledFuture = _ScheduledFuture
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
 
class DedicatedServer():
    """dev.ultreon.quantum.server.dedicated.DedicatedServer"""
 
    @staticmethod
    def _wrap(java_value: _DedicatedServer) -> 'DedicatedServer':
        return DedicatedServer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DedicatedServer):
        """
        Dynamic initializer for DedicatedServer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DedicatedServer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DedicatedServer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.server.QuantumServer.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @override
    @overload
    def getHost(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.QuantumServer.getHost()"""
        return 'UUID'._wrap(super(server.QuantumServer, self).getHost())

    @override
    @overload
    def save(self, arg0: bool):
        """public void dev.ultreon.quantum.server.QuantumServer.save(boolean) throws java.io.IOException"""
        super(_server.QuantumServer, self).save(_boolean.valueOf(arg0))

    @overload
    def getCacheablePlayer(self, arg0: 'UUID') -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.util.UUID)"""
        return 'player.CacheablePlayer'._wrap(super(_server.QuantumServer, self).getCacheablePlayer(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onDisconnected(self, arg0: 'ServerPlayer', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.onDisconnected(dev.ultreon.quantum.server.player.ServerPlayer,java.lang.String)"""
        super(_server.QuantumServer, self).onDisconnected(arg0, arg1)

    @overload
    def disposeOnClose(self, arg0: 'ServerDisposable') -> 'server.ServerDisposable':
        """public <T extends dev.ultreon.quantum.server.ServerDisposable> T dev.ultreon.quantum.server.QuantumServer.disposeOnClose(T)"""
        return 'server.ServerDisposable'._wrap(super(_server.QuantumServer, self).disposeOnClose(arg0))

    @override
    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(util.PollingExecutorService, self).pollAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getGameVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.getGameVersion()"""
        return str._wrap(super(server.QuantumServer, self).getGameVersion())

    @override
    @overload
    def sendChunk(self, arg0: 'ChunkPos', arg1: 'Chunk'):
        """public void dev.ultreon.quantum.server.QuantumServer.sendChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk) throws java.io.IOException"""
        super(_server.QuantumServer, self).sendChunk(arg0, arg1)

    @override
    @overload
    def isIntegrated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isIntegrated()"""
        return bool._wrap(super(server.QuantumServer, self).isIntegrated())

    @override
    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isRunning()"""
        return bool._wrap(super(server.QuantumServer, self).isRunning())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isDedicated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isDedicated()"""
        return bool._wrap(super(server.QuantumServer, self).isDedicated())

    @override
    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(util.PollingExecutorService, self).poll()

    @staticmethod
    @overload
    def get() -> 'server.QuantumServer':
        """public static dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.server.QuantumServer.get()"""
        return server.QuantumServer._wrap(_QuantumServer.get())

    @staticmethod
    @overload
    def minutes2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.minutes2ticks(float)"""
        return int._wrap(_QuantumServer.minutes2ticks(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def hours2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.hours2ticks(float)"""
        return int._wrap(_QuantumServer.hours2ticks(_float.valueOf(arg0)))

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.dedicated.DedicatedServer.isTerminated()"""
        return bool._wrap(super(DedicatedServer, self).isTerminated())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.server.QuantumServer.close()"""
        super(server.QuantumServer, self).close()

    @override
    @overload
    def getConsoleSender(self) -> 'commands.CommandSender':
        """public dev.ultreon.quantum.api.commands.CommandSender dev.ultreon.quantum.server.QuantumServer.getConsoleSender()"""
        return 'commands.CommandSender'._wrap(super(server.QuantumServer, self).getConsoleSender())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Runnable') -> 'CompletableFuture':
        """public static java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.server.QuantumServer.invoke(java.lang.Runnable)"""
        return CompletableFuture._wrap(_QuantumServer.invoke(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Callable') -> 'CompletableFuture':
        """public static <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.server.QuantumServer.invoke(java.util.concurrent.Callable<T>)"""
        return CompletableFuture._wrap(_QuantumServer.invoke(arg0))

    @overload
    def getWorld(self, arg0: 'Identifier') -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld(dev.ultreon.quantum.util.Identifier)"""
        return 'world.ServerWorld'._wrap(super(_server.QuantumServer, self).getWorld(arg0))

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_util.PollingExecutorService, self).awaitTermination(_long.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.toString()"""
        return str._wrap(super(server.QuantumServer, self).toString())

    @property
    def profiler(self) -> Profiler:
        return Profiler._wrap(super(_PollingExecutorService).profiler())

    @overload
    def getPlayer(self, arg0: 'UUID') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.util.UUID)"""
        return 'player.ServerPlayer'._wrap(super(_server.QuantumServer, self).getPlayer(arg0))

    @staticmethod
    @overload
    def seconds2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.seconds2ticks(float)"""
        return int._wrap(_QuantumServer.seconds2ticks(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Callable') -> object:
        """public static <T> T dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.util.concurrent.Callable<T>)"""
        return object._wrap(_QuantumServer.invokeAndWait(arg0))

    @override
    @overload
    def getCurrentTps(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getCurrentTps()"""
        return int._wrap(super(server.QuantumServer, self).getCurrentTps())

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'._wrap(super(_util.PollingExecutorService, self).invokeAll(arg0, _long.valueOf(arg1), arg2))

    @overload
    def hasPlayedBefore(self, arg0: 'CacheablePlayer') -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.hasPlayedBefore(dev.ultreon.quantum.server.player.CacheablePlayer)"""
        return bool._wrap(super(_server.QuantumServer, self).hasPlayedBefore(arg0))

    @override
    @overload
    def crash(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.server.dedicated.DedicatedServer.crash(dev.ultreon.quantum.crash.CrashLog)"""
        super(_DedicatedServer, self).crash(arg0)

    @overload
    def getCachedPlayer(self, arg0: 'UUID') -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.util.UUID)"""
        return 'player.CachedPlayer'._wrap(super(_server.QuantumServer, self).getCachedPlayer(arg0))

    @overload
    def getCacheablePlayer(self, arg0: str) -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.lang.String)"""
        return 'player.CacheablePlayer'._wrap(super(_server.QuantumServer, self).getCacheablePlayer(arg0))

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'._wrap(super(util.PollingExecutorService, self).shutdownNow())

    @overload
    def schedule(self, arg0: 'Runnable', arg1: int, arg2: 'TimeUnit') -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<?> dev.ultreon.quantum.server.QuantumServer.schedule(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        return 'ScheduledFuture'._wrap(super(_server.QuantumServer, self).schedule(arg0, _long.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getNetworker(self) -> 'network.Networker':
        """public dev.ultreon.quantum.network.Networker dev.ultreon.quantum.server.QuantumServer.getNetworker()"""
        return 'network.Networker'._wrap(super(server.QuantumServer, self).getNetworker())

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'._wrap(super(_util.PollingExecutorService, self).invokeAll(arg0))

    @override
    @overload
    def getStorage(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.server.QuantumServer.getStorage()"""
        return 'world.WorldStorage'._wrap(super(server.QuantumServer, self).getStorage())

    @override
    @overload
    def getRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.server.dedicated.DedicatedServer.getRenderDistance()"""
        return int._wrap(super(DedicatedServer, self).getRenderDistance())

    @override
    @overload
    def getPlayerCount(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPlayerCount()"""
        return int._wrap(super(server.QuantumServer, self).getPlayerCount())

    @override
    @overload
    def handleWorldSaveError(self, arg0: 'Exception'):
        """public void dev.ultreon.quantum.server.QuantumServer.handleWorldSaveError(java.lang.Exception)"""
        super(_server.QuantumServer, self).handleWorldSaveError(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.lang.Runnable)"""
        _QuantumServer.invokeAndWait(arg0)

    @override
    @overload
    def isInitialChunksLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isInitialChunksLoaded()"""
        return bool._wrap(super(server.QuantumServer, self).isInitialChunksLoaded())

    @override
    @overload
    def getRecipeManager(self) -> 'recipe.RecipeManager':
        """public dev.ultreon.quantum.recipe.RecipeManager dev.ultreon.quantum.server.QuantumServer.getRecipeManager()"""
        return 'recipe.RecipeManager'._wrap(super(server.QuantumServer, self).getRecipeManager())

    @override
    @overload
    def onInitialChunksLoaded(self):
        """public void dev.ultreon.quantum.server.QuantumServer.onInitialChunksLoaded()"""
        super(server.QuantumServer, self).onInitialChunksLoaded()

    @override
    @overload
    def shutdown(self):
        """public void dev.ultreon.quantum.server.dedicated.DedicatedServer.shutdown()"""
        super(DedicatedServer, self).shutdown()

    @overload
    def getCachedPlayer(self, arg0: str) -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.lang.String)"""
        return 'player.CachedPlayer'._wrap(super(_server.QuantumServer, self).getCachedPlayer(arg0))

    @override
    @overload
    def getPlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayers()"""
        return 'Collection'._wrap(super(server.QuantumServer, self).getPlayers())

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0))

    @overload
    def getEntity(self, arg0: int, *arg1: 'entity.Entity') -> 'entity.Entity':
        """public final <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.server.QuantumServer.getEntity(int,T...)"""
        return 'entity.Entity'._wrap(super(_server.QuantumServer, self).getEntity(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getEntityRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getEntityRenderDistance()"""
        return int._wrap(super(server.QuantumServer, self).getEntityRenderDistance())

    @overload
    def handleTranslation(self, arg0: str, arg1: 'Object') -> str:
        """public java.lang.String dev.ultreon.quantum.server.dedicated.DedicatedServer.handleTranslation(java.lang.String,java.lang.Object[])"""
        return str._wrap(super(_DedicatedServer, self).handleTranslation(arg0, arg1))

    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(_util.PollingExecutorService, self).execute(arg0)

    @overload
    def loadPlayer(self, arg0: str, arg1: 'UUID', arg2: 'IConnection') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.loadPlayer(java.lang.String,java.util.UUID,dev.ultreon.quantum.network.system.IConnection)"""
        return 'player.ServerPlayer'._wrap(super(_server.QuantumServer, self).loadPlayer(arg0, arg1, arg2))

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool._wrap(super(util.PollingExecutorService, self).isShutdown())

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_util.PollingExecutorService, self).invokeAny(arg0))

    @override
    @overload
    def getGameRules(self) -> 'gamerule.GameRules':
        """public dev.ultreon.quantum.gamerule.GameRules dev.ultreon.quantum.server.QuantumServer.getGameRules()"""
        return 'gamerule.GameRules'._wrap(super(server.QuantumServer, self).getGameRules())

    @overload
    def getPlayer(self, arg0: str) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.lang.String)"""
        return 'player.ServerPlayer'._wrap(super(_server.QuantumServer, self).getPlayer(arg0))

    @override
    @overload
    def handleChunkLoadFailure(self, arg0: 'ChunkPos', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.handleChunkLoadFailure(dev.ultreon.quantum.world.ChunkPos,java.lang.String)"""
        super(_server.QuantumServer, self).handleChunkLoadFailure(arg0, arg1)

    @override
    @overload
    def placePlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.placePlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_server.QuantumServer, self).placePlayer(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPlayersInChunk(self, arg0: 'ChunkPos') -> 'Stream':
        """public java.util.stream.Stream<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersInChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Stream'._wrap(super(_server.QuantumServer, self).getPlayersInChunk(arg0))

    @override
    @overload
    def getWorlds(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.world.World> dev.ultreon.quantum.server.QuantumServer.getWorlds()"""
        return 'Collection'._wrap(super(server.QuantumServer, self).getWorlds())

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.server.QuantumServer.load() throws java.io.IOException"""
        super(server.QuantumServer, self).load()

    @override
    @overload
    def getPort(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPort()"""
        return int._wrap(super(server.QuantumServer, self).getPort())

    @override
    @overload
    def crash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.server.QuantumServer.crash(java.lang.Throwable)"""
        super(_server.QuantumServer, self).crash(arg0)

    @override
    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld()"""
        return 'world.ServerWorld'._wrap(super(server.QuantumServer, self).getWorld())

    @staticmethod
    @overload
    def isOnServerThread() -> bool:
        """public static boolean dev.ultreon.quantum.server.QuantumServer.isOnServerThread()"""
        return bool._wrap(_QuantumServer.isOnServerThread())

    @override
    @overload
    def run(self):
        """public void dev.ultreon.quantum.server.QuantumServer.run()"""
        super(server.QuantumServer, self).run()

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0, arg1))

    @override
    @overload
    def addPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.addPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_server.QuantumServer, self).addPlayer(arg0)

    @override
    @overload
    def getCachedPlayers(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.server.player.CachedPlayer> dev.ultreon.quantum.server.QuantumServer.getCachedPlayers()"""
        return 'List'._wrap(super(server.QuantumServer, self).getCachedPlayers())

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_util.PollingExecutorService, self).invokeAny(arg0, _long.valueOf(arg1), arg2))

    @override
    @overload
    def getDefaultPermissions(self) -> 'player.PermissionMap':
        """public dev.ultreon.quantum.server.player.PermissionMap dev.ultreon.quantum.server.QuantumServer.getDefaultPermissions()"""
        return 'player.PermissionMap'._wrap(super(server.QuantumServer, self).getDefaultPermissions())

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getMaxPlayers(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getMaxPlayers()"""
        return int._wrap(super(server.QuantumServer, self).getMaxPlayers())

    @override
    @overload
    def fatalCrash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.server.dedicated.DedicatedServer.fatalCrash(java.lang.Throwable)"""
        super(_DedicatedServer, self).fatalCrash(arg0)

    @overload
    def getEntity(self, arg0: 'UUID') -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.server.QuantumServer.getEntity(java.util.UUID)"""
        return 'entity.Entity'._wrap(super(_server.QuantumServer, self).getEntity(arg0))

    @override
    @overload
    def getOnlineTicks(self) -> int:
        """public long dev.ultreon.quantum.server.QuantumServer.getOnlineTicks()"""
        return int._wrap(super(server.QuantumServer, self).getOnlineTicks())

    @override
    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.server.QuantumServer.getResourceManager()"""
        return 'resources.ResourceManager'._wrap(super(server.QuantumServer, self).getResourceManager())

    @override
    @overload
    def getPlayerManager(self) -> 'server.PlayerManager':
        """public dev.ultreon.quantum.server.PlayerManager dev.ultreon.quantum.server.QuantumServer.getPlayerManager()"""
        return 'server.PlayerManager'._wrap(super(server.QuantumServer, self).getPlayerManager())

    @override
    @overload
    def getPlayersByName(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersByName()"""
        return 'Map'._wrap(super(server.QuantumServer, self).getPlayersByName())

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: 'InspectionRoot'):
        """public dev.ultreon.quantum.server.dedicated.DedicatedServer(java.lang.String,int,dev.ultreon.quantum.debug.inspect.InspectionRoot<dev.ultreon.quantum.server.dedicated.Main>) throws java.io.IOException"""
        val = _DedicatedServer(arg0, _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.server.QuantumServer.start()"""
        super(server.QuantumServer, self).start() 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.Main
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.server.dedicated.Main as _Main
_Main = _Main
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.server.dedicated.DedicatedServer as _DedicatedServer
_DedicatedServer = _DedicatedServer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Main():
    """dev.ultreon.quantum.server.dedicated.Main"""
 
    @staticmethod
    def _wrap(java_value: _Main) -> 'Main':
        return Main(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Main):
        """
        Dynamic initializer for Main.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Main__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Main__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, ):
        """public dev.ultreon.quantum.server.dedicated.Main()"""
        val = _Main()
        self.__wrapper = val

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.server.dedicated.Main.main(java.lang.String[]) throws java.io.IOException,java.lang.InterruptedException"""
        _Main.main(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getServer() -> 'DedicatedServer':
        """public static dev.ultreon.quantum.server.dedicated.DedicatedServer dev.ultreon.quantum.server.dedicated.Main.getServer()"""
        return DedicatedServer._wrap(_Main.getServer())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.dedicated.Main()"""
        val = _Main()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.PreMain
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.server.dedicated.PreMain as _PreMain
_PreMain = _PreMain
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PreMain():
    """dev.ultreon.quantum.server.dedicated.PreMain"""
 
    @staticmethod
    def _wrap(java_value: _PreMain) -> 'PreMain':
        return PreMain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PreMain):
        """
        Dynamic initializer for PreMain.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PreMain__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PreMain__wrapper":
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
        """public dev.ultreon.quantum.server.dedicated.PreMain()"""
        val = _PreMain()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.server.dedicated.PreMain()"""
        val = _PreMain()
        self.__wrapper = val

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.server.dedicated.PreMain.main(java.lang.String[])"""
        _PreMain.main(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.ServerLoader
import dev.ultreon.quantum.server.dedicated.ServerLoader as _ServerLoader
_ServerLoader = _ServerLoader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerLoader():
    """dev.ultreon.quantum.server.dedicated.ServerLoader"""
 
    @staticmethod
    def _wrap(java_value: _ServerLoader) -> 'ServerLoader':
        return ServerLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerLoader):
        """
        Dynamic initializer for ServerLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self):
        """public void dev.ultreon.quantum.server.dedicated.ServerLoader.load()"""
        super(ServerLoader, self).load()

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
    def __init__(self):
        """public dev.ultreon.quantum.server.dedicated.ServerLoader()"""
        val = _ServerLoader()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.dedicated.ServerLoader()"""
        val = _ServerLoader()
        self.__wrapper = val

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