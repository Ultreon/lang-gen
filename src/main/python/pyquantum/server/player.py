from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.server.player.PermissionMap as __PermissionMap
__PermissionMap = __PermissionMap
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PermissionMap():
    """dev.ultreon.quantum.server.player.PermissionMap"""
 
    @staticmethod
    def __wrap(java_value: __PermissionMap) -> 'PermissionMap':
        return PermissionMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PermissionMap):
        """
        Dynamic initializer for PermissionMap.
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
    def __init__(self, ):
        """public dev.ultreon.quantum.server.player.PermissionMap()"""
        val = __PermissionMap()
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
    def has(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.player.PermissionMap.has(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__PermissionMap, self).has(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.player.PermissionMap()"""
        val = __PermissionMap()
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

 
 
 
# CLASS: dev.ultreon.quantum.server.player.PermissionMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.server.player.PermissionMap as __PermissionMap
__PermissionMap = __PermissionMap
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PermissionMap():
    """dev.ultreon.quantum.server.player.PermissionMap"""
 
    @staticmethod
    def __wrap(java_value: __PermissionMap) -> 'PermissionMap':
        return PermissionMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PermissionMap):
        """
        Dynamic initializer for PermissionMap.
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
    def __init__(self, ):
        """public dev.ultreon.quantum.server.player.PermissionMap()"""
        val = __PermissionMap()
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
    def has(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.player.PermissionMap.has(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__PermissionMap, self).has(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.player.PermissionMap()"""
        val = __PermissionMap()
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

 
 
 
# CLASS: dev.ultreon.quantum.server.player.PermissionMap 
 
 
# CLASS: dev.ultreon.quantum.server.player.CachedPlayer
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.server.player.CachedPlayer as __CachedPlayer
__CachedPlayer = __CachedPlayer
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CachedPlayer():
    """dev.ultreon.quantum.server.player.CachedPlayer"""
 
    @staticmethod
    def __wrap(java_value: __CachedPlayer) -> 'CachedPlayer':
        return CachedPlayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CachedPlayer):
        """
        Dynamic initializer for CachedPlayer.
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
    def __init__(self, arg0: 'UUID', arg1: str):
        """public dev.ultreon.quantum.server.player.CachedPlayer(java.util.UUID,java.lang.String)"""
        val = __CachedPlayer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isOnline(self) -> bool:
        """public boolean dev.ultreon.quantum.server.player.CachedPlayer.isOnline()"""
        return bool.__wrap(super(CachedPlayer, self).isOnline())

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

    @override
    @overload
    def isCache(self) -> bool:
        """public boolean dev.ultreon.quantum.server.player.CachedPlayer.isCache()"""
        return bool.__wrap(super(CachedPlayer, self).isCache())

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
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.player.CachedPlayer.getUuid()"""
        return 'UUID'.__wrap(super(CachedPlayer, self).getUuid())

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

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.player.CachedPlayer.getName()"""
        return str.__wrap(super(CachedPlayer, self).getName()) 
 
 
# CLASS: dev.ultreon.quantum.server.player.MutablePermissionMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.server.player.MutablePermissionMap as __MutablePermissionMap
__MutablePermissionMap = __MutablePermissionMap
import java.lang.Long as __long
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.server.player.PermissionMap as __PermissionMap
__PermissionMap = __PermissionMap
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MutablePermissionMap():
    """dev.ultreon.quantum.server.player.MutablePermissionMap"""
 
    @staticmethod
    def __wrap(java_value: __MutablePermissionMap) -> 'MutablePermissionMap':
        return MutablePermissionMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutablePermissionMap):
        """
        Dynamic initializer for MutablePermissionMap.
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
    def __init__(self):
        """public dev.ultreon.quantum.server.player.MutablePermissionMap()"""
        val = __MutablePermissionMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def has(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.player.PermissionMap.has(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__PermissionMap, self).has(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.player.MutablePermissionMap()"""
        val = __MutablePermissionMap()
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
 
 
# CLASS: dev.ultreon.quantum.server.player.CacheablePlayer
import dev.ultreon.quantum.server.player.CacheablePlayer as __CacheablePlayer
__CacheablePlayer = __CacheablePlayer
from abc import abstractmethod, ABC
 
class CacheablePlayer(ABC):
    """dev.ultreon.quantum.server.player.CacheablePlayer"""
 
    @staticmethod
    def __wrap(java_value: __CacheablePlayer) -> 'CacheablePlayer':
        return CacheablePlayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CacheablePlayer):
        """
        Dynamic initializer for CacheablePlayer.
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
    def getName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.server.player.CacheablePlayer.getName()"""
        pass

    @abstractmethod
    def isOnline(self, ):
        """public abstract boolean dev.ultreon.quantum.server.player.CacheablePlayer.isOnline()"""
        pass

    @abstractmethod
    def getUuid(self, ):
        """public abstract java.util.UUID dev.ultreon.quantum.server.player.CacheablePlayer.getUuid()"""
        pass

    @abstractmethod
    def isCache(self, ):
        """public abstract boolean dev.ultreon.quantum.server.player.CacheablePlayer.isCache()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.player.ServerPlayer
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import dev.ultreon.quantum.entity.player.Player as __Player
__Player = __Player
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
import dev.ultreon.quantum.entity.AttributeMap as __AttributeMap
__AttributeMap = __AttributeMap
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import dev.ultreon.quantum.util.HitResult as __HitResult
__HitResult = __HitResult
import java.lang.Double as __double
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.entity.player.FoodStatus as __FoodStatus
__FoodStatus = __FoodStatus
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

import dev.ultreon.quantum.world.SoundEvent as __SoundEvent
__SoundEvent = __SoundEvent
import dev.ultreon.quantum.entity.LivingEntity as __LivingEntity
__LivingEntity = __LivingEntity
from builtins import float
try:
    from pyapache.collections4 import set
except ImportError:
    set = __import_once__("pyapache.collections4.set")

import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
import dev.ultreon.quantum.world.Location as __Location
__Location = __Location
import java.lang.Float as __float
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
import java.lang.String as __String
__String = __String
try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = __import_once__("pyquantum.entity.damagesource")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
import dev.ultreon.quantum.world.rng.RNG as __RNG
__RNG = __RNG
try:
    from pyquantum.entity import util
except ImportError:
    util = __import_once__("pyquantum.entity.util")

import dev.ultreon.quantum.util.GameMode as __GameMode
__GameMode = __GameMode
import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
import java.lang.Boolean as __boolean
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
try:
    from pyquantum.item import food
except ImportError:
    food = __import_once__("pyquantum.item.food")

import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
import dev.ultreon.quantum.entity.EntityType as __EntityType
__EntityType = __EntityType
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.entity.damagesource.DamageSource as __DamageSource
__DamageSource = __DamageSource
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.menu.Inventory as __Inventory
__Inventory = __Inventory
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.entity.player.PlayerAbilities as __PlayerAbilities
__PlayerAbilities = __PlayerAbilities
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class ServerPlayer():
    """dev.ultreon.quantum.server.player.ServerPlayer"""
 
    @staticmethod
    def __wrap(java_value: __ServerPlayer) -> 'ServerPlayer':
        return ServerPlayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerPlayer):
        """
        Dynamic initializer for ServerPlayer.
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
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.server.player.ServerPlayer.getLocation()"""
        return 'world.Location'.__wrap(super(ServerPlayer, self).getLocation())

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(__entity.Entity, self).setX(__double.valueOf(arg0))

    @override
    @overload
    def isSpectator(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isSpectator()"""
        return bool.__wrap(super(player.Player, self).isSpectator())

    @override
    @overload
    def setSpectating(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setSpectating(boolean)"""
        super(__player.Player, self).setSpectating(__boolean.valueOf(arg0))

    @override
    @overload
    def getMaxHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getMaxHealth()"""
        return float.__wrap(super(entity.LivingEntity, self).getMaxHealth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setCursor(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.setCursor(dev.ultreon.quantum.item.ItemStack)"""
        super(__ServerPlayer, self).setCursor(arg0)

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float.__wrap(super(entity.Entity, self).getX())

    @override
    @overload
    def isSurvival(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isSurvival()"""
        return bool.__wrap(super(player.Player, self).isSurvival())

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'.__wrap(super(entity.Entity, self).getBoundingBox())

    @override
    @overload
    def isCrouching(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isCrouching()"""
        return bool.__wrap(super(player.Player, self).isCrouching())

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.player.Player.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__player.Player, self).setPosition(arg0)

    @override
    @overload
    def getAttributes(self) -> 'entity.AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'entity.AttributeMap'.__wrap(super(entity.Entity, self).getAttributes())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(__ServerPlayer, self).sendMessage(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool.__wrap(super(entity.Entity, self).isInWater())

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'.__wrap(super(__entity.Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__entity.Entity, self).rotate(arg0)

    @override
    @overload
    def hurt(self, arg0: float, arg1: 'DamageSource'):
        """public final void dev.ultreon.quantum.entity.LivingEntity.hurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__entity.LivingEntity, self).hurt(__float.valueOf(arg0), arg1)

    @overload
    def isSpawned(self) -> bool:
        """public boolean dev.ultreon.quantum.server.player.ServerPlayer.isSpawned()"""
        return bool.__wrap(super(ServerPlayer, self).isSpawned())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'.__wrap(super(entity.Entity, self).getPosition())

    @override
    @overload
    def getHurtSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.player.Player.getHurtSound()"""
        return 'world.SoundEvent'.__wrap(super(player.Player, self).getHurtSound())

    @override
    @overload
    def moveTowards(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.moveTowards(double,double,double,double)"""
        super(__entity.LivingEntity, self).moveTowards(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))

    @override
    @overload
    def rotateHead(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.player.Player.rotateHead(float,float)"""
        super(__player.Player, self).rotateHead(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setFlyingSpeed(self, arg0: float):
        """public void dev.ultreon.quantum.entity.player.Player.setFlyingSpeed(float)"""
        super(__player.Player, self).setFlyingSpeed(__float.valueOf(arg0))

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(__entity.Entity, self).onPipeline(arg0)

    @overload
    def markSpawned(self):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.markSpawned()"""
        super(ServerPlayer, self).markSpawned()

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.player.Player.load(dev.ultreon.ubo.types.MapType)"""
        super(__player.Player, self).load(arg0)

    @overload
    def placeBlock(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.placeBlock(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__ServerPlayer, self).placeBlock(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def setGameMode(self, arg0: 'GameMode'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.setGameMode(dev.ultreon.quantum.util.GameMode)"""
        super(__ServerPlayer, self).setGameMode(arg0)

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def nearestEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.player.Player.nearestEntity()"""
        return 'entity.Entity'.__wrap(super(player.Player, self).nearestEntity())

    @overload
    def hasPlayedBefore(self) -> bool:
        """public boolean dev.ultreon.quantum.server.player.ServerPlayer.hasPlayedBefore()"""
        return bool.__wrap(super(ServerPlayer, self).hasPlayedBefore())

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float.__wrap(super(entity.Entity, self).getXRot())

    @override
    @overload
    def setWalkingSpeed(self, arg0: float):
        """public void dev.ultreon.quantum.entity.player.Player.setWalkingSpeed(float)"""
        super(__player.Player, self).setWalkingSpeed(__float.valueOf(arg0))

    @override
    @overload
    def getDeathSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getDeathSound()"""
        return 'world.SoundEvent'.__wrap(super(entity.LivingEntity, self).getDeathSound())

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(__entity.Entity, self).setId(__int.valueOf(arg0))

    @override
    @overload
    def onDeath(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDeath(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__entity.LivingEntity, self).onDeath(arg0)

    @overload
    def spawn(self, arg0: 'Vec3d', arg1: 'IConnection'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.spawn(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.server.ServerPacketHandler, dev.ultreon.quantum.network.client.ClientPacketHandler>)"""
        super(__ServerPlayer, self).spawn(arg0, arg1)

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'.__wrap(super(entity.Entity, self).getPipeline())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def openMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.openMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(__ServerPlayer, self).openMenu(arg0)

    @override
    @overload
    def getHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getHealth()"""
        return float.__wrap(super(entity.LivingEntity, self).getHealth())

    @overload
    def kick(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.kick(dev.ultreon.quantum.text.TextObject)"""
        super(__ServerPlayer, self).kick(arg0)

    @override
    @overload
    def setInvincible(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setInvincible(boolean)"""
        super(__player.Player, self).setInvincible(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @property
    def inventory(self) -> Inventory:
        return Inventory.__wrap(super(__Player).inventory())

    @override
    @overload
    def dropItem(self):
        """public void dev.ultreon.quantum.entity.player.Player.dropItem()"""
        super(player.Player, self).dropItem()

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(__entity.Entity, self).setY(__double.valueOf(arg0))

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float.__wrap(super(entity.Entity, self).getGravity())

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(__entity.Entity, self).setUuid(arg0)

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str.__wrap(super(entity.Entity, self).getPublicName())

    @property
    def abilities(self) -> PlayerAbilities:
        return PlayerAbilities.__wrap(super(__Player).abilities())

    @override
    @overload
    def jump(self):
        """public void dev.ultreon.quantum.entity.player.Player.jump()"""
        super(player.Player, self).jump()

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.sendMessage(java.lang.String)"""
        super(__ServerPlayer, self).sendMessage(arg0)

    @overload
    def onAttack(self, arg0: int):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.onAttack(int)"""
        super(__ServerPlayer, self).onAttack(__int.valueOf(arg0))

    @overload
    def onHurt(self, arg0: float, arg1: 'DamageSource') -> bool:
        """public boolean dev.ultreon.quantum.server.player.ServerPlayer.onHurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        return bool.__wrap(super(__ServerPlayer, self).onHurt(__float.valueOf(arg0), arg1))

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.teleportTo(int,int,int)"""
        super(__ServerPlayer, self).teleportTo(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def tabComplete(self, arg0: str):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.tabComplete(java.lang.String)"""
        super(__ServerPlayer, self).tabComplete(arg0)

    @override
    @overload
    def setFlying(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setFlying(boolean)"""
        super(__player.Player, self).setFlying(__boolean.valueOf(arg0))

    @override
    @overload
    def getGamemode(self) -> 'util.GameMode':
        """public dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.entity.player.Player.getGamemode()"""
        return 'util.GameMode'.__wrap(super(player.Player, self).getGamemode())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getCursor(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.entity.player.Player.getCursor()"""
        return 'item.ItemStack'.__wrap(super(player.Player, self).getCursor())

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'ServerWorld', arg2: 'UUID', arg3: str, arg4: 'IConnection'):
        """public dev.ultreon.quantum.server.player.ServerPlayer(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.player.Player>,dev.ultreon.quantum.world.ServerWorld,java.util.UUID,java.lang.String,dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.server.ServerPacketHandler, dev.ultreon.quantum.network.client.ClientPacketHandler>)"""
        val = __ServerPlayer(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.player.ServerPlayer.getWorld()"""
        return 'world.ServerWorld'.__wrap(super(ServerPlayer, self).getWorld())

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(__entity.LivingEntity, self).onPrepareSpawn(arg0)

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(__entity.Entity, self).setXRot(__float.valueOf(arg0))

    @overload
    def makeAdmin(self):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.makeAdmin()"""
        super(ServerPlayer, self).makeAdmin()

    @override
    @overload
    def isFlying(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isFlying()"""
        return bool.__wrap(super(player.Player, self).isFlying())

    @overload
    def refreshChunks(self, arg0: 'ChunkRefresher'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.refreshChunks(dev.ultreon.quantum.world.ChunkRefresher)"""
        super(__ServerPlayer, self).refreshChunks(arg0)

    @override
    @overload
    def getChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.entity.LivingEntity.getChunkPos()"""
        return 'world.ChunkPos'.__wrap(super(entity.LivingEntity, self).getChunkPos())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.player.Player.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__player.Player, self).save(arg0))

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float.__wrap(super(entity.Entity, self).getY())

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__entity.Entity, self).teleportTo(arg0)

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(__entity.Entity, self).setYRot(__float.valueOf(arg0))

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.tick()"""
        super(ServerPlayer, self).tick()

    @override
    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isWalking()"""
        return bool.__wrap(super(entity.LivingEntity, self).isWalking())

    @property
    def connection(self) -> IConnection:
        return IConnection.__wrap(super(__ServerPlayer).connection())

    @override
    @overload
    def isSpectating(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isSpectating()"""
        return bool.__wrap(super(player.Player, self).isSpectating())

    @property
    def inventory(self, value: 'menu.Inventory'):
        super(__Player).inventory(value)

    @override
    @overload
    def openInventory(self):
        """public void dev.ultreon.quantum.entity.player.Player.openInventory()"""
        super(player.Player, self).openInventory()

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.LivingEntity.getLookVector()"""
        return 'vector.Vec3d'.__wrap(super(entity.LivingEntity, self).getLookVector())

    @override
    @overload
    def selectBlock(self, arg0: int):
        """public void dev.ultreon.quantum.entity.player.Player.selectBlock(int)"""
        super(__player.Player, self).selectBlock(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def isSwimming(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isSwimming()"""
        return bool.__wrap(super(player.Player, self).isSwimming())

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.player.ServerPlayer.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__ServerPlayer, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'.__wrap(super(entity.Entity, self).getVelocity())

    @overload
    def getChunkVec(self) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.server.player.ServerPlayer.getChunkVec()"""
        return 'vector.Vec2i'.__wrap(super(ServerPlayer, self).getChunkVec())

    @override
    @overload
    def getSpeed(self) -> float:
        """public double dev.ultreon.quantum.entity.player.Player.getSpeed()"""
        return float.__wrap(super(player.Player, self).getSpeed())

    @override
    @overload
    def isBuilder(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isBuilder()"""
        return bool.__wrap(super(player.Player, self).isBuilder())

    @override
    @overload
    def setJumpVel(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setJumpVel(float)"""
        super(__entity.LivingEntity, self).setJumpVel(__float.valueOf(arg0))

    @override
    @overload
    def isOnline(self) -> bool:
        """public boolean dev.ultreon.quantum.server.player.ServerPlayer.isOnline()"""
        return bool.__wrap(super(ServerPlayer, self).isOnline())

    @overload
    def getAttackDamage(self) -> float:
        """public float dev.ultreon.quantum.server.player.ServerPlayer.getAttackDamage()"""
        return float.__wrap(super(ServerPlayer, self).getAttackDamage())

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(__entity.Entity, self).loadWithPos(arg0)

    @override
    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.LivingEntity.getAge()"""
        return int.__wrap(super(entity.LivingEntity, self).getAge())

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def sendChunk(self, arg0: 'ChunkPos', arg1: 'Chunk'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.sendChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk)"""
        super(__ServerPlayer, self).sendChunk(arg0, arg1)

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'.__wrap(super(entity.Entity, self).getSize())

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__entity.Entity, self).setVelocity(arg0)

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(__entity.Entity, self).setZ(__double.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(__entity.Entity, self).setPosition(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.teleportTo(double,double,double)"""
        super(__ServerPlayer, self).teleportTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def setRunning(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setRunning(boolean)"""
        super(__player.Player, self).setRunning(__boolean.valueOf(arg0))

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool.__wrap(super(__entity.Entity, self).move(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def createAiGoals(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.createAiGoals()"""
        super(entity.LivingEntity, self).createAiGoals()

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float.__wrap(super(entity.Entity, self).getYRot())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool.__wrap(super(entity.Entity, self).isMarkedForRemoval())

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0))

    @property
    def connection(self, value: 'system.IConnection'):
        super(__ServerPlayer).connection(value)

    @override
    @overload
    def drop(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.entity.player.Player.drop(dev.ultreon.quantum.item.ItemStack)"""
        super(__player.Player, self).drop(arg0)

    @override
    @overload
    def setCrouching(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setCrouching(boolean)"""
        super(__player.Player, self).setCrouching(__boolean.valueOf(arg0))

    @overload
    def markPlayedBefore(self):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.markPlayedBefore()"""
        super(ServerPlayer, self).markPlayedBefore()

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.player.Player.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(player.Player, self).getDisplayName())

    @override
    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isInvincible()"""
        return bool.__wrap(super(player.Player, self).isInvincible())

    @override
    @overload
    def setHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setHealth(float)"""
        super(__entity.LivingEntity, self).setHealth(__float.valueOf(arg0))

    @override
    @overload
    def getJumpVel(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getJumpVel()"""
        return float.__wrap(super(entity.LivingEntity, self).getJumpVel())

    @override
    @overload
    def closeMenu(self, arg0: 'CrateMenu'):
        """public void dev.ultreon.quantum.entity.player.Player.closeMenu(dev.ultreon.quantum.menu.CrateMenu)"""
        super(__player.Player, self).closeMenu(arg0)

    @override
    @overload
    def getSelectedItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.entity.player.Player.getSelectedItem()"""
        return 'item.ItemStack'.__wrap(super(player.Player, self).getSelectedItem())

    @override
    @overload
    def getWalkingSpeed(self) -> float:
        """public float dev.ultreon.quantum.entity.player.Player.getWalkingSpeed()"""
        return float.__wrap(super(player.Player, self).getWalkingSpeed())

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(__entity.Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def kill(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.kill()"""
        super(entity.LivingEntity, self).kill()

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int.__wrap(super(entity.Entity, self).getId())

    @override
    @overload
    def isAllowFlight(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isAllowFlight()"""
        return bool.__wrap(super(player.Player, self).isAllowFlight())

    @override
    @overload
    def setMaxHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setMaxHealth(float)"""
        super(__entity.LivingEntity, self).setMaxHealth(__float.valueOf(arg0))

    @override
    @overload
    def closeMenu(self):
        """public void dev.ultreon.quantum.entity.player.Player.closeMenu()"""
        super(player.Player, self).closeMenu()

    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(__entity.Entity, self).setGravity(__float.valueOf(arg0))

    @override
    @overload
    def getFoodStatus(self) -> 'player.FoodStatus':
        """public dev.ultreon.quantum.entity.player.FoodStatus dev.ultreon.quantum.entity.player.Player.getFoodStatus()"""
        return 'player.FoodStatus'.__wrap(super(player.Player, self).getFoodStatus())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.player.ServerPlayer.getName()"""
        return str.__wrap(super(ServerPlayer, self).getName())

    @overload
    def isChunkActive(self, arg0: 'ChunkPos') -> bool:
        """public boolean dev.ultreon.quantum.server.player.ServerPlayer.isChunkActive(dev.ultreon.quantum.world.ChunkPos)"""
        return bool.__wrap(super(__ServerPlayer, self).isChunkActive(arg0))

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(__entity.Entity, self).teleportTo(arg0)

    @override
    @overload
    def applyEffect(self, arg0: 'AppliedEffect'):
        """public void dev.ultreon.quantum.entity.LivingEntity.applyEffect(dev.ultreon.quantum.item.food.AppliedEffect)"""
        super(__entity.LivingEntity, self).applyEffect(arg0)

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'entity.Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return entity.Entity.__wrap(__Entity.loadFrom(arg0, arg1))

    @overload
    def onChunkPending(self, arg0: 'ChunkPos'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.onChunkPending(dev.ultreon.quantum.world.ChunkPos)"""
        super(__ServerPlayer, self).onChunkPending(arg0)

    @override
    @overload
    def getEyeHeight(self) -> float:
        """public float dev.ultreon.quantum.entity.player.Player.getEyeHeight()"""
        return float.__wrap(super(player.Player, self).getEyeHeight())

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float.__wrap(super(__entity.Entity, self).distanceTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def isCache(self) -> bool:
        """public boolean dev.ultreon.quantum.server.player.ServerPlayer.isCache()"""
        return bool.__wrap(super(ServerPlayer, self).isCache())

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float.__wrap(super(entity.Entity, self).getZ())

    @override
    @overload
    def rayCast(self) -> 'util.HitResult':
        """public dev.ultreon.quantum.util.HitResult dev.ultreon.quantum.entity.player.Player.rayCast()"""
        return 'util.HitResult'.__wrap(super(player.Player, self).rayCast())

    @override
    @overload
    def getLastDamageSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.LivingEntity.getLastDamageSource()"""
        return 'damagesource.DamageSource'.__wrap(super(entity.LivingEntity, self).getLastDamageSource())

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(entity.Entity, self).sendPipeline()

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(__entity.Entity, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.player.Player.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__player.Player, self).setRotation(arg0)

    @override
    @overload
    def onDropItems(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDropItems(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__entity.LivingEntity, self).onDropItems(arg0)

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(entity.Entity, self).markRemoved()

    @overload
    def onMessageSent(self, arg0: str):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.onMessageSent(java.lang.String)"""
        super(__ServerPlayer, self).onMessageSent(arg0)

    @overload
    def respawn(self):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.respawn()"""
        super(ServerPlayer, self).respawn()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.player.ServerPlayer.toString()"""
        return str.__wrap(super(ServerPlayer, self).toString())

    @override
    @overload
    def setAllowFlight(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setAllowFlight(boolean)"""
        super(__player.Player, self).setAllowFlight(__boolean.valueOf(arg0))

    @override
    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.playSound(dev.ultreon.quantum.world.SoundEvent,float)"""
        super(__ServerPlayer, self).playSound(arg0, __float.valueOf(arg1))

    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.onDisconnect(java.lang.String)"""
        super(__ServerPlayer, self).onDisconnect(arg0)

    @overload
    def onChunkStatus(self, arg0: 'ChunkPos', arg1: 'Status'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.onChunkStatus(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk$Status)"""
        super(__ServerPlayer, self).onChunkStatus(arg0, arg1)

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'.__wrap(super(entity.Entity, self).getRng())

    @overload
    def useItem(self, arg0: 'BlockHitResult', arg1: 'ItemStack', arg2: 'ItemSlot') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.server.player.ServerPlayer.useItem(dev.ultreon.quantum.util.BlockHitResult,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.menu.ItemSlot)"""
        return 'world.UseResult'.__wrap(super(__ServerPlayer, self).useItem(arg0, arg1, arg2))

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isAffectedByFluid()"""
        return bool.__wrap(super(player.Player, self).isAffectedByFluid())

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'.__wrap(super(entity.Entity, self).getRotation())

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.player.ServerPlayer.getUuid()"""
        return 'UUID'.__wrap(super(ServerPlayer, self).getUuid())

    @override
    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isRunning()"""
        return bool.__wrap(super(player.Player, self).isRunning())

    @overload
    def onAbilities(self, arg0: 'AbilitiesPacket'):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.onAbilities(dev.ultreon.quantum.network.packets.AbilitiesPacket)"""
        super(__ServerPlayer, self).onAbilities(arg0)

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.server.player.ServerPlayer.isAdmin()"""
        return bool.__wrap(super(ServerPlayer, self).isAdmin())

    @staticmethod
    @overload
    def refreshChunks(arg0: 'ChunkRefresher', arg1: 'QuantumServer', arg2: 'ServerWorld', arg3: 'ChunkPos', arg4: 'ListOrderedSet', arg5: 'ListOrderedSet'):
        """public static void dev.ultreon.quantum.server.player.ServerPlayer.refreshChunks(dev.ultreon.quantum.world.ChunkRefresher,dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.ChunkPos,org.apache.commons.collections4.set.ListOrderedSet<dev.ultreon.quantum.world.ChunkPos>,org.apache.commons.collections4.set.ListOrderedSet<dev.ultreon.quantum.world.ChunkPos>)"""
        __ServerPlayer.refreshChunks(arg0, arg1, arg2, arg3, arg4, arg5)

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'.__wrap(super(entity.Entity, self).getBlockPos())

    @overload
    def rayCast(self, arg0: 'Collection') -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.player.Player.rayCast(java.util.Collection<dev.ultreon.quantum.entity.Entity>)"""
        return 'entity.Entity'.__wrap(super(__player.Player, self).rayCast(arg0))

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool.__wrap(super(entity.Entity, self).isInVoid())

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox.__wrap(__Entity.getBoundingBox(arg0, arg1))

    @override
    @overload
    def getOpenMenu(self) -> 'menu.ContainerMenu':
        """public dev.ultreon.quantum.menu.ContainerMenu dev.ultreon.quantum.entity.player.Player.getOpenMenu()"""
        return 'menu.ContainerMenu'.__wrap(super(player.Player, self).getOpenMenu())

    @override
    @overload
    def isDead(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isDead()"""
        return bool.__wrap(super(entity.LivingEntity, self).isDead())

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float.__wrap(super(__entity.Entity, self).distanceTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def handlePlayerMove(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.handlePlayerMove(double,double,double)"""
        super(__ServerPlayer, self).handlePlayerMove(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @overload
    def nearestEntity(self, arg0: 'Class') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.entity.player.Player.nearestEntity(java.lang.Class<T>)"""
        return 'entity.Entity'.__wrap(super(__player.Player, self).nearestEntity(arg0))

    @overload
    def kick(self, arg0: str):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.kick(java.lang.String)"""
        super(__ServerPlayer, self).kick(arg0)

    @overload
    def setInitialItems(self):
        """public void dev.ultreon.quantum.server.player.ServerPlayer.setInitialItems()"""
        super(ServerPlayer, self).setInitialItems()

    @override
    @overload
    def getType(self) -> 'entity.EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'entity.EntityType'.__wrap(super(entity.Entity, self).getType())

    @override
    @overload
    def getFlyingSpeed(self) -> float:
        """public float dev.ultreon.quantum.entity.player.Player.getFlyingSpeed()"""
        return float.__wrap(super(player.Player, self).getFlyingSpeed()) 
 
 
# CLASS: dev.ultreon.quantum.server.player.S2CPlayerAttackPacket
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import dev.ultreon.quantum.server.player.S2CPlayerAttackPacket as __S2CPlayerAttackPacket
__S2CPlayerAttackPacket = __S2CPlayerAttackPacket
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = __import_once__("pyquantum.network.client")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class S2CPlayerAttackPacket():
    """dev.ultreon.quantum.server.player.S2CPlayerAttackPacket"""
 
    @staticmethod
    def __wrap(java_value: __S2CPlayerAttackPacket) -> 'S2CPlayerAttackPacket':
        return S2CPlayerAttackPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __S2CPlayerAttackPacket):
        """
        Dynamic initializer for S2CPlayerAttackPacket.
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

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.server.player.S2CPlayerAttackPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __S2CPlayerAttackPacket(arg0)
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
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.server.player.S2CPlayerAttackPacket(int,int)"""
        val = __S2CPlayerAttackPacket(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'ServerPlayer', arg1: 'Entity'):
        """public dev.ultreon.quantum.server.player.S2CPlayerAttackPacket(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.entity.Entity)"""
        val = __S2CPlayerAttackPacket(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.server.player.S2CPlayerAttackPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__S2CPlayerAttackPacket, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.server.player.S2CPlayerAttackPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(__S2CPlayerAttackPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))