from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.server.dedicated.DedicatedServerModInit as __DedicatedServerModInit
__DedicatedServerModInit = __DedicatedServerModInit
from abc import abstractmethod, ABC
 
class DedicatedServerModInit(ABC):
    """dev.ultreon.quantum.server.dedicated.DedicatedServerModInit"""
 
    @staticmethod
    def __wrap(java_value: __DedicatedServerModInit) -> 'DedicatedServerModInit':
        return DedicatedServerModInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DedicatedServerModInit):
        """
        Dynamic initializer for DedicatedServerModInit.
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
        """public abstract void dev.ultreon.quantum.server.dedicated.DedicatedServerModInit.onInitialize()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.DedicatedServerModInit
import dev.ultreon.quantum.server.dedicated.DedicatedServerModInit as __DedicatedServerModInit
__DedicatedServerModInit = __DedicatedServerModInit
from abc import abstractmethod, ABC
 
class DedicatedServerModInit(ABC):
    """dev.ultreon.quantum.server.dedicated.DedicatedServerModInit"""
 
    @staticmethod
    def __wrap(java_value: __DedicatedServerModInit) -> 'DedicatedServerModInit':
        return DedicatedServerModInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DedicatedServerModInit):
        """
        Dynamic initializer for DedicatedServerModInit.
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
        """public abstract void dev.ultreon.quantum.server.dedicated.DedicatedServerModInit.onInitialize()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.DedicatedServerModInit 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.ServerConfig
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
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.server.dedicated.ServerConfig as __ServerConfig
__ServerConfig = __ServerConfig
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.Mod as __Mod
__Mod = __Mod
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class ServerConfig(config.__CraftyConfig, crafty.CraftyConfig):
    """dev.ultreon.quantum.server.dedicated.ServerConfig"""
 
    @staticmethod
    def __wrap(java_value: __ServerConfig) -> 'ServerConfig':
        return ServerConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerConfig):
        """
        Dynamic initializer for ServerConfig.
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.dedicated.ServerConfig()"""
        val = __ServerConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.dedicated.ServerConfig()"""
        val = __ServerConfig()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.DedicatedServer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import java.util.UUID as UUID
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

try:
    from pyquantum import recipe
except ImportError:
    recipe = __import_once__("pyquantum.recipe")

import java.util.concurrent.ScheduledFuture as __ScheduledFuture
__ScheduledFuture = __ScheduledFuture
import java.util.stream.Stream as __Stream
__Stream = __Stream
import dev.ultreon.quantum.debug.profiler.Profiler as __Profiler
__Profiler = __Profiler
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
import java.util.Collection as Collection
try:
    from pyquantum import crash
except ImportError:
    crash = __import_once__("pyquantum.crash")

import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = __import_once__("pyquantum.debug.profiler")

import java.util.concurrent.Callable as Callable
try:
    from pyquantum import gamerule
except ImportError:
    gamerule = __import_once__("pyquantum.gamerule")

from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.resources.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
import java.util.List as __List
__List = __List
import java.lang.Float as __float
import dev.ultreon.quantum.server.PlayerManager as __PlayerManager
__PlayerManager = __PlayerManager
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.server.dedicated.DedicatedServer as __DedicatedServer
__DedicatedServer = __DedicatedServer
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.server.ServerDisposable as __ServerDisposable
__ServerDisposable = __ServerDisposable
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.util.concurrent.CompletableFuture as CompletableFuture
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
import java.lang.Boolean as __boolean
import dev.ultreon.quantum.server.player.CachedPlayer as __CachedPlayer
__CachedPlayer = __CachedPlayer
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.util.PollingExecutorService as __PollingExecutorService
__PollingExecutorService = __PollingExecutorService
import java.lang.Exception as Exception
import dev.ultreon.quantum.recipe.RecipeManager as __RecipeManager
__RecipeManager = __RecipeManager
import dev.ultreon.quantum.gamerule.GameRules as __GameRules
__GameRules = __GameRules
import java.lang.String as __string
import dev.ultreon.quantum.server.player.CacheablePlayer as __CacheablePlayer
__CacheablePlayer = __CacheablePlayer
import java.util.concurrent.ScheduledFuture as ScheduledFuture
import dev.ultreon.quantum.server.player.PermissionMap as __PermissionMap
__PermissionMap = __PermissionMap
from builtins import str
import dev.ultreon.quantum.world.WorldStorage as __WorldStorage
__WorldStorage = __WorldStorage
from pyquantum_helper import override
try:
    from pyquantum.debug import inspect
except ImportError:
    inspect = __import_once__("pyquantum.debug.inspect")

import java.lang.Object as __object
import java.lang.Runnable as Runnable
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

from builtins import object
import dev.ultreon.quantum.network.Networker as __Networker
__Networker = __Networker
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.Map as Map
import java.util.List as List
 
class DedicatedServer(pyquantum.__QuantumServer, server.QuantumServer):
    """dev.ultreon.quantum.server.dedicated.DedicatedServer"""
 
    @staticmethod
    def __wrap(java_value: __DedicatedServer) -> 'DedicatedServer':
        return DedicatedServer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DedicatedServer):
        """
        Dynamic initializer for DedicatedServer.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.server.QuantumServer.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)


    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(__util.PollingExecutorService, self).execute(arg0)

    @overload
    def getCacheablePlayer(self, arg0: 'UUID') -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.util.UUID)"""
        return 'player.CacheablePlayer'.__wrap(super(__server.QuantumServer, self).getCacheablePlayer(arg0))

    @overload
    def handleTranslation(self, arg0: str, arg1: 'Object') -> str:
        """public java.lang.String dev.ultreon.quantum.server.dedicated.DedicatedServer.handleTranslation(java.lang.String,java.lang.Object[])"""
        return str.__wrap(super(__DedicatedServer, self).handleTranslation(arg0, arg1))

    @overload
    def getCacheablePlayer(self, arg0: str) -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.lang.String)"""
        return 'player.CacheablePlayer'.__wrap(super(__server.QuantumServer, self).getCacheablePlayer(arg0))

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Callable') -> object:
        """public static <T> T dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.util.concurrent.Callable<T>)"""
        return object.__wrap(__QuantumServer.invokeAndWait(arg0))

    @override
    @overload
    def placePlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.placePlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__server.QuantumServer, self).placePlayer(arg0)

    @staticmethod
    @overload
    def get() -> 'server.QuantumServer':
        """public static dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.server.QuantumServer.get()"""
        return server.QuantumServer.__wrap(__QuantumServer.get())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(util.PollingExecutorService, self).pollAll()

    @override
    @overload
    def crash(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.server.dedicated.DedicatedServer.crash(dev.ultreon.quantum.crash.CrashLog)"""
        super(__DedicatedServer, self).crash(arg0)

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def invoke(arg0: 'Callable') -> 'CompletableFuture':
        """public static <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.server.QuantumServer.invoke(java.util.concurrent.Callable<T>)"""
        return CompletableFuture.__wrap(__QuantumServer.invoke(arg0))

    @override
    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld()"""
        return 'world.ServerWorld'.__wrap(super(server.QuantumServer, self).getWorld())

    @override
    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(util.PollingExecutorService, self).poll()

    @override
    @overload
    def getMaxPlayers(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getMaxPlayers()"""
        return int.__wrap(super(server.QuantumServer, self).getMaxPlayers())

    @override
    @overload
    def isDedicated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isDedicated()"""
        return bool.__wrap(super(server.QuantumServer, self).isDedicated())

    @override
    @overload
    def getDefaultPermissions(self) -> 'player.PermissionMap':
        """public dev.ultreon.quantum.server.player.PermissionMap dev.ultreon.quantum.server.QuantumServer.getDefaultPermissions()"""
        return 'player.PermissionMap'.__wrap(super(server.QuantumServer, self).getDefaultPermissions())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.server.QuantumServer.close()"""
        super(server.QuantumServer, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getPlayer(self, arg0: 'UUID') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.util.UUID)"""
        return 'player.ServerPlayer'.__wrap(super(__server.QuantumServer, self).getPlayer(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Runnable') -> 'CompletableFuture':
        """public static java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.server.QuantumServer.invoke(java.lang.Runnable)"""
        return CompletableFuture.__wrap(__QuantumServer.invoke(arg0))

    @override
    @overload
    def getWorlds(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.world.World> dev.ultreon.quantum.server.QuantumServer.getWorlds()"""
        return 'Collection'.__wrap(super(server.QuantumServer, self).getWorlds())

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.dedicated.DedicatedServer.isTerminated()"""
        return bool.__wrap(super(DedicatedServer, self).isTerminated())

    @overload
    def schedule(self, arg0: 'Runnable', arg1: int, arg2: 'TimeUnit') -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<?> dev.ultreon.quantum.server.QuantumServer.schedule(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        return 'ScheduledFuture'.__wrap(super(__server.QuantumServer, self).schedule(arg0, __long.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def isOnServerThread() -> bool:
        """public static boolean dev.ultreon.quantum.server.QuantumServer.isOnServerThread()"""
        return bool.__wrap(__QuantumServer.isOnServerThread())

    @overload
    def getEntity(self, arg0: int, *arg1: 'entity.Entity') -> 'entity.Entity':
        """public final <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.server.QuantumServer.getEntity(int,T...)"""
        return 'entity.Entity'.__wrap(super(__server.QuantumServer, self).getEntity(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getEntityRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getEntityRenderDistance()"""
        return int.__wrap(super(server.QuantumServer, self).getEntityRenderDistance())

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__util.PollingExecutorService, self).invokeAny(arg0, __long.valueOf(arg1), arg2))

    @override
    @overload
    def isInitialChunksLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isInitialChunksLoaded()"""
        return bool.__wrap(super(server.QuantumServer, self).isInitialChunksLoaded())

    @overload
    def getWorld(self, arg0: 'Identifier') -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld(dev.ultreon.quantum.util.Identifier)"""
        return 'world.ServerWorld'.__wrap(super(__server.QuantumServer, self).getWorld(arg0))

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__util.PollingExecutorService, self).invokeAny(arg0))

    @overload
    def disposeOnClose(self, arg0: 'ServerDisposable') -> 'server.ServerDisposable':
        """public <T extends dev.ultreon.quantum.server.ServerDisposable> T dev.ultreon.quantum.server.QuantumServer.disposeOnClose(T)"""
        return 'server.ServerDisposable'.__wrap(super(__server.QuantumServer, self).disposeOnClose(arg0))

    @override
    @overload
    def getGameVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.getGameVersion()"""
        return str.__wrap(super(server.QuantumServer, self).getGameVersion())

    @override
    @overload
    def getHost(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.QuantumServer.getHost()"""
        return 'UUID'.__wrap(super(server.QuantumServer, self).getHost())

    @override
    @overload
    def getStorage(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.server.QuantumServer.getStorage()"""
        return 'world.WorldStorage'.__wrap(super(server.QuantumServer, self).getStorage())

    @override
    @overload
    def getPlayerManager(self) -> 'server.PlayerManager':
        """public dev.ultreon.quantum.server.PlayerManager dev.ultreon.quantum.server.QuantumServer.getPlayerManager()"""
        return 'server.PlayerManager'.__wrap(super(server.QuantumServer, self).getPlayerManager())

    @override
    @overload
    def getRecipeManager(self) -> 'recipe.RecipeManager':
        """public dev.ultreon.quantum.recipe.RecipeManager dev.ultreon.quantum.server.QuantumServer.getRecipeManager()"""
        return 'recipe.RecipeManager'.__wrap(super(server.QuantumServer, self).getRecipeManager())

    @override
    @overload
    def fatalCrash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.server.dedicated.DedicatedServer.fatalCrash(java.lang.Throwable)"""
        super(__DedicatedServer, self).fatalCrash(arg0)

    @override
    @overload
    def save(self, arg0: bool):
        """public void dev.ultreon.quantum.server.QuantumServer.save(boolean) throws java.io.IOException"""
        super(__server.QuantumServer, self).save(__boolean.valueOf(arg0))

    @overload
    def loadPlayer(self, arg0: str, arg1: 'UUID', arg2: 'IConnection') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.loadPlayer(java.lang.String,java.util.UUID,dev.ultreon.quantum.network.system.IConnection)"""
        return 'player.ServerPlayer'.__wrap(super(__server.QuantumServer, self).loadPlayer(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPlayerCount(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPlayerCount()"""
        return int.__wrap(super(server.QuantumServer, self).getPlayerCount())

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0))

    @overload
    def hasPlayedBefore(self, arg0: 'CacheablePlayer') -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.hasPlayedBefore(dev.ultreon.quantum.server.player.CacheablePlayer)"""
        return bool.__wrap(super(__server.QuantumServer, self).hasPlayedBefore(arg0))

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool.__wrap(super(util.PollingExecutorService, self).isShutdown())

    @override
    @overload
    def getPlayersByName(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersByName()"""
        return 'Map'.__wrap(super(server.QuantumServer, self).getPlayersByName())

    @override
    @overload
    def getOnlineTicks(self) -> int:
        """public long dev.ultreon.quantum.server.QuantumServer.getOnlineTicks()"""
        return int.__wrap(super(server.QuantumServer, self).getOnlineTicks())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPlayersInChunk(self, arg0: 'ChunkPos') -> 'Stream':
        """public java.util.stream.Stream<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersInChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Stream'.__wrap(super(__server.QuantumServer, self).getPlayersInChunk(arg0))

    @override
    @overload
    def getPlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayers()"""
        return 'Collection'.__wrap(super(server.QuantumServer, self).getPlayers())

    @override
    @overload
    def crash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.server.QuantumServer.crash(java.lang.Throwable)"""
        super(__server.QuantumServer, self).crash(arg0)

    @override
    @overload
    def onDisconnected(self, arg0: 'ServerPlayer', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.onDisconnected(dev.ultreon.quantum.server.player.ServerPlayer,java.lang.String)"""
        super(__server.QuantumServer, self).onDisconnected(arg0, arg1)

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.lang.Runnable)"""
        __QuantumServer.invokeAndWait(arg0)

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

    @override
    @overload
    def isIntegrated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isIntegrated()"""
        return bool.__wrap(super(server.QuantumServer, self).isIntegrated())

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: 'InspectionRoot'):
        """public dev.ultreon.quantum.server.dedicated.DedicatedServer(java.lang.String,int,dev.ultreon.quantum.debug.inspect.InspectionRoot<dev.ultreon.quantum.server.dedicated.Main>) throws java.io.IOException"""
        val = __DedicatedServer(arg0, __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0))

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'.__wrap(super(__util.PollingExecutorService, self).invokeAll(arg0, __long.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def seconds2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.seconds2ticks(float)"""
        return int.__wrap(__QuantumServer.seconds2ticks(__float.valueOf(arg0)))

    @override
    @overload
    def getNetworker(self) -> 'network.Networker':
        """public dev.ultreon.quantum.network.Networker dev.ultreon.quantum.server.QuantumServer.getNetworker()"""
        return 'network.Networker'.__wrap(super(server.QuantumServer, self).getNetworker())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def minutes2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.minutes2ticks(float)"""
        return int.__wrap(__QuantumServer.minutes2ticks(__float.valueOf(arg0)))

    @property
    def profiler(self) -> Profiler:
        return Profiler.__wrap(super(__PollingExecutorService).profiler())

    @override
    @overload
    def addPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.addPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__server.QuantumServer, self).addPlayer(arg0)

    @override
    @overload
    def getConsoleSender(self) -> 'commands.CommandSender':
        """public dev.ultreon.quantum.api.commands.CommandSender dev.ultreon.quantum.server.QuantumServer.getConsoleSender()"""
        return 'commands.CommandSender'.__wrap(super(server.QuantumServer, self).getConsoleSender())

    @override
    @overload
    def getPort(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPort()"""
        return int.__wrap(super(server.QuantumServer, self).getPort())

    @staticmethod
    @overload
    def hours2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.hours2ticks(float)"""
        return int.__wrap(__QuantumServer.hours2ticks(__float.valueOf(arg0)))

    @override
    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isRunning()"""
        return bool.__wrap(super(server.QuantumServer, self).isRunning())

    @override
    @overload
    def handleChunkLoadFailure(self, arg0: 'ChunkPos', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.handleChunkLoadFailure(dev.ultreon.quantum.world.ChunkPos,java.lang.String)"""
        super(__server.QuantumServer, self).handleChunkLoadFailure(arg0, arg1)

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.server.QuantumServer.load() throws java.io.IOException"""
        super(server.QuantumServer, self).load()

    @override
    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.server.QuantumServer.getResourceManager()"""
        return 'resources.ResourceManager'.__wrap(super(server.QuantumServer, self).getResourceManager())

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'.__wrap(super(util.PollingExecutorService, self).shutdownNow())

    @override
    @overload
    def getCachedPlayers(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.server.player.CachedPlayer> dev.ultreon.quantum.server.QuantumServer.getCachedPlayers()"""
        return 'List'.__wrap(super(server.QuantumServer, self).getCachedPlayers())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.toString()"""
        return str.__wrap(super(server.QuantumServer, self).toString())

    @override
    @overload
    def handleWorldSaveError(self, arg0: 'Exception'):
        """public void dev.ultreon.quantum.server.QuantumServer.handleWorldSaveError(java.lang.Exception)"""
        super(__server.QuantumServer, self).handleWorldSaveError(arg0)

    @overload
    def getEntity(self, arg0: 'UUID') -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.server.QuantumServer.getEntity(java.util.UUID)"""
        return 'entity.Entity'.__wrap(super(__server.QuantumServer, self).getEntity(arg0))

    @override
    @overload
    def getCurrentTps(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getCurrentTps()"""
        return int.__wrap(super(server.QuantumServer, self).getCurrentTps())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def run(self):
        """public void dev.ultreon.quantum.server.QuantumServer.run()"""
        super(server.QuantumServer, self).run()

    @overload
    def getCachedPlayer(self, arg0: str) -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.lang.String)"""
        return 'player.CachedPlayer'.__wrap(super(__server.QuantumServer, self).getCachedPlayer(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getPlayer(self, arg0: str) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.lang.String)"""
        return 'player.ServerPlayer'.__wrap(super(__server.QuantumServer, self).getPlayer(arg0))

    @overload
    def getCachedPlayer(self, arg0: 'UUID') -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.util.UUID)"""
        return 'player.CachedPlayer'.__wrap(super(__server.QuantumServer, self).getCachedPlayer(arg0))

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'.__wrap(super(__util.PollingExecutorService, self).invokeAll(arg0))

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__util.PollingExecutorService, self).awaitTermination(__long.valueOf(arg0), arg1))

    @override
    @overload
    def sendChunk(self, arg0: 'ChunkPos', arg1: 'Chunk'):
        """public void dev.ultreon.quantum.server.QuantumServer.sendChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk) throws java.io.IOException"""
        super(__server.QuantumServer, self).sendChunk(arg0, arg1)

    @override
    @overload
    def getRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.server.dedicated.DedicatedServer.getRenderDistance()"""
        return int.__wrap(super(DedicatedServer, self).getRenderDistance())

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.server.QuantumServer.start()"""
        super(server.QuantumServer, self).start()

    @override
    @overload
    def getGameRules(self) -> 'gamerule.GameRules':
        """public dev.ultreon.quantum.gamerule.GameRules dev.ultreon.quantum.server.QuantumServer.getGameRules()"""
        return 'gamerule.GameRules'.__wrap(super(server.QuantumServer, self).getGameRules()) 
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.Main
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.server.dedicated.Main as __Main
__Main = __Main
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.server.dedicated.DedicatedServer as __DedicatedServer
__DedicatedServer = __DedicatedServer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Main():
    """dev.ultreon.quantum.server.dedicated.Main"""
 
    @staticmethod
    def __wrap(java_value: __Main) -> 'Main':
        return Main(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Main):
        """
        Dynamic initializer for Main.
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
    def getServer() -> 'DedicatedServer':
        """public static dev.ultreon.quantum.server.dedicated.DedicatedServer dev.ultreon.quantum.server.dedicated.Main.getServer()"""
        return DedicatedServer.__wrap(__Main.getServer())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.dedicated.Main()"""
        val = __Main()
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.dedicated.Main()"""
        val = __Main()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.server.dedicated.Main.main(java.lang.String[]) throws java.io.IOException,java.lang.InterruptedException"""
        __Main.main(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.PreMain
from builtins import str
import dev.ultreon.quantum.server.dedicated.PreMain as __PreMain
__PreMain = __PreMain
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
 
class PreMain():
    """dev.ultreon.quantum.server.dedicated.PreMain"""
 
    @staticmethod
    def __wrap(java_value: __PreMain) -> 'PreMain':
        return PreMain(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PreMain):
        """
        Dynamic initializer for PreMain.
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

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.server.dedicated.PreMain.main(java.lang.String[])"""
        __PreMain.main(arg0)

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.dedicated.PreMain()"""
        val = __PreMain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.dedicated.PreMain()"""
        val = __PreMain()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.server.dedicated.ServerLoader
import dev.ultreon.quantum.server.dedicated.ServerLoader as __ServerLoader
__ServerLoader = __ServerLoader
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
 
class ServerLoader():
    """dev.ultreon.quantum.server.dedicated.ServerLoader"""
 
    @staticmethod
    def __wrap(java_value: __ServerLoader) -> 'ServerLoader':
        return ServerLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerLoader):
        """
        Dynamic initializer for ServerLoader.
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
    def load(self):
        """public void dev.ultreon.quantum.server.dedicated.ServerLoader.load()"""
        super(ServerLoader, self).load()

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
        """public dev.ultreon.quantum.server.dedicated.ServerLoader()"""
        val = __ServerLoader()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.dedicated.ServerLoader()"""
        val = __ServerLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val