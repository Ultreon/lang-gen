from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = _import_once("pyquantum.item.food")

from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.entity.player.FoodStatus as _FoodStatus
_FoodStatus = _FoodStatus
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FoodStatus():
    """dev.ultreon.quantum.entity.player.FoodStatus"""
 
    @staticmethod
    def _wrap(java_value: _FoodStatus) -> 'FoodStatus':
        return FoodStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FoodStatus):
        """
        Dynamic initializer for FoodStatus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FoodStatus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FoodStatus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isFull(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.FoodStatus.isFull()"""
        return bool._wrap(super(FoodStatus, self).isFull())

    @overload
    def setSaturationLevel(self, arg0: int):
        """public void dev.ultreon.quantum.entity.player.FoodStatus.setSaturationLevel(int)"""
        super(_FoodStatus, self).setSaturationLevel(_int.valueOf(arg0))

    @overload
    def getFoodLevel(self) -> int:
        """public int dev.ultreon.quantum.entity.player.FoodStatus.getFoodLevel()"""
        return int._wrap(super(FoodStatus, self).getFoodLevel())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Player'):
        """public dev.ultreon.quantum.entity.player.FoodStatus(dev.ultreon.quantum.entity.player.Player)"""
        val = _FoodStatus(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isStarving(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.FoodStatus.isStarving()"""
        return bool._wrap(super(FoodStatus, self).isStarving())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.player.FoodStatus.tick()"""
        super(FoodStatus, self).tick()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setFoodLevel(self, arg0: int):
        """public void dev.ultreon.quantum.entity.player.FoodStatus.setFoodLevel(int)"""
        super(_FoodStatus, self).setFoodLevel(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def exhaust(self, arg0: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.FoodStatus.exhaust(float)"""
        return bool._wrap(super(_FoodStatus, self).exhaust(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Player', arg1: int, arg2: int):
        """public dev.ultreon.quantum.entity.player.FoodStatus(dev.ultreon.quantum.entity.player.Player,int,int)"""
        val = _FoodStatus(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getSaturationLevel(self) -> float:
        """public float dev.ultreon.quantum.entity.player.FoodStatus.getSaturationLevel()"""
        return float._wrap(super(FoodStatus, self).getSaturationLevel())

    @overload
    def isHungry(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.FoodStatus.isHungry()"""
        return bool._wrap(super(FoodStatus, self).isHungry())

    @overload
    def eat(self, arg0: 'FoodData'):
        """public void dev.ultreon.quantum.entity.player.FoodStatus.eat(dev.ultreon.quantum.item.food.FoodData)"""
        super(_FoodStatus, self).eat(arg0)

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

 
 
 
# CLASS: dev.ultreon.quantum.entity.player.FoodStatus
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = _import_once("pyquantum.item.food")

from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.entity.player.FoodStatus as _FoodStatus
_FoodStatus = _FoodStatus
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FoodStatus():
    """dev.ultreon.quantum.entity.player.FoodStatus"""
 
    @staticmethod
    def _wrap(java_value: _FoodStatus) -> 'FoodStatus':
        return FoodStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FoodStatus):
        """
        Dynamic initializer for FoodStatus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FoodStatus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FoodStatus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isFull(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.FoodStatus.isFull()"""
        return bool._wrap(super(FoodStatus, self).isFull())

    @overload
    def setSaturationLevel(self, arg0: int):
        """public void dev.ultreon.quantum.entity.player.FoodStatus.setSaturationLevel(int)"""
        super(_FoodStatus, self).setSaturationLevel(_int.valueOf(arg0))

    @overload
    def getFoodLevel(self) -> int:
        """public int dev.ultreon.quantum.entity.player.FoodStatus.getFoodLevel()"""
        return int._wrap(super(FoodStatus, self).getFoodLevel())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Player'):
        """public dev.ultreon.quantum.entity.player.FoodStatus(dev.ultreon.quantum.entity.player.Player)"""
        val = _FoodStatus(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isStarving(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.FoodStatus.isStarving()"""
        return bool._wrap(super(FoodStatus, self).isStarving())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.player.FoodStatus.tick()"""
        super(FoodStatus, self).tick()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setFoodLevel(self, arg0: int):
        """public void dev.ultreon.quantum.entity.player.FoodStatus.setFoodLevel(int)"""
        super(_FoodStatus, self).setFoodLevel(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def exhaust(self, arg0: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.FoodStatus.exhaust(float)"""
        return bool._wrap(super(_FoodStatus, self).exhaust(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Player', arg1: int, arg2: int):
        """public dev.ultreon.quantum.entity.player.FoodStatus(dev.ultreon.quantum.entity.player.Player,int,int)"""
        val = _FoodStatus(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getSaturationLevel(self) -> float:
        """public float dev.ultreon.quantum.entity.player.FoodStatus.getSaturationLevel()"""
        return float._wrap(super(FoodStatus, self).getSaturationLevel())

    @overload
    def isHungry(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.FoodStatus.isHungry()"""
        return bool._wrap(super(FoodStatus, self).isHungry())

    @overload
    def eat(self, arg0: 'FoodData'):
        """public void dev.ultreon.quantum.entity.player.FoodStatus.eat(dev.ultreon.quantum.item.food.FoodData)"""
        super(_FoodStatus, self).eat(arg0)

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

 
 
 
# CLASS: dev.ultreon.quantum.entity.player.FoodStatus 
 
 
# CLASS: dev.ultreon.quantum.entity.player.Player
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.damagesource.DamageSource as _DamageSource
_DamageSource = _DamageSource
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import java.lang.Object as _object
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.Location as _Location
_Location = _Location
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import dev.ultreon.quantum.entity.util.EntitySize as _EntitySize
_EntitySize = _EntitySize
import java.lang.Float as _float
try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = _import_once("pyquantum.entity.damagesource")

import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
import dev.ultreon.quantum.world.rng.RNG as _RNG
_RNG = _RNG
import dev.ultreon.quantum.entity.player.FoodStatus as _FoodStatus
_FoodStatus = _FoodStatus
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
try:
    from pyquantum.entity import util
except ImportError:
    util = _import_once("pyquantum.entity.util")

import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = _import_once("pyquantum.item.food")

import dev.ultreon.quantum.entity.LivingEntity as _LivingEntity
_LivingEntity = _LivingEntity
import dev.ultreon.quantum.util.HitResult as _HitResult
_HitResult = _HitResult
import dev.ultreon.quantum.entity.EntityType as _EntityType
_EntityType = _EntityType
import java.lang.String as _string
import dev.ultreon.quantum.menu.Inventory as _Inventory
_Inventory = _Inventory
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.entity.player.PlayerAbilities as _PlayerAbilities
_PlayerAbilities = _PlayerAbilities
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.entity.AttributeMap as _AttributeMap
_AttributeMap = _AttributeMap
import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import dev.ultreon.quantum.world.SoundEvent as _SoundEvent
_SoundEvent = _SoundEvent
import java.lang.Integer as _int
import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.entity.player.Player as _Player
_Player = _Player
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import dev.ultreon.quantum.util.GameMode as _GameMode
_GameMode = _GameMode
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class Player():
    """dev.ultreon.quantum.entity.player.Player"""
 
    @staticmethod
    def _wrap(java_value: _Player) -> 'Player':
        return Player(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Player):
        """
        Dynamic initializer for Player.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Player__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Player__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isSurvival(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isSurvival()"""
        return bool._wrap(super(Player, self).isSurvival())

    @overload
    def getSelectedItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.entity.player.Player.getSelectedItem()"""
        return 'item.ItemStack'._wrap(super(Player, self).getSelectedItem())

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool._wrap(super(_entity.Entity, self).move(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(_entity.Entity, self).setPosition(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(_entity.Entity, self).setXRot(_float.valueOf(arg0))

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float._wrap(super(entity.Entity, self).getY())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'._wrap(super(entity.Entity, self).getPosition())

    @property
    def abilities(self) -> PlayerAbilities:
        return PlayerAbilities._wrap(super(_Player).abilities())

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float._wrap(super(entity.Entity, self).getZ())

    @property
    def inventory(self) -> Inventory:
        return Inventory._wrap(super(_Player).inventory())

    @overload
    def isSpectator(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isSpectator()"""
        return bool._wrap(super(Player, self).isSpectator())

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'entity.Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return entity.Entity._wrap(_Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float._wrap(super(entity.Entity, self).getXRot())

    @overload
    def isSpectating(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isSpectating()"""
        return bool._wrap(super(Player, self).isSpectating())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(_entity.Entity, self).sendMessage(arg0)

    @overload
    def nearestEntity(self, arg0: 'Class') -> 'entity.Entity':
        """public <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.entity.player.Player.nearestEntity(java.lang.Class<T>)"""
        return 'entity.Entity'._wrap(super(_Player, self).nearestEntity(arg0))

    @override
    @overload
    def hurt(self, arg0: float, arg1: 'DamageSource'):
        """public final void dev.ultreon.quantum.entity.LivingEntity.hurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_entity.LivingEntity, self).hurt(_float.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isRunning()"""
        return bool._wrap(super(Player, self).isRunning())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'._wrap(super(entity.Entity, self).getLocation())

    @override
    @overload
    def setJumpVel(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setJumpVel(float)"""
        super(_entity.LivingEntity, self).setJumpVel(_float.valueOf(arg0))

    @override
    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isWalking()"""
        return bool._wrap(super(entity.LivingEntity, self).isWalking())

    @overload
    def isAllowFlight(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isAllowFlight()"""
        return bool._wrap(super(Player, self).isAllowFlight())

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'._wrap(super(entity.Entity, self).getUuid())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'._wrap(super(entity.Entity, self).getBlockPos())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def onDropItems(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDropItems(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_entity.LivingEntity, self).onDropItems(arg0)

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str._wrap(super(entity.Entity, self).getPublicName())

    @overload
    def getFoodStatus(self) -> 'FoodStatus':
        """public dev.ultreon.quantum.entity.player.FoodStatus dev.ultreon.quantum.entity.player.Player.getFoodStatus()"""
        return 'FoodStatus'._wrap(super(Player, self).getFoodStatus())

    @override
    @overload
    def getDeathSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getDeathSound()"""
        return 'world.SoundEvent'._wrap(super(entity.LivingEntity, self).getDeathSound())

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(_entity.Entity, self).loadWithPos(arg0)

    @overload
    def closeMenu(self):
        """public void dev.ultreon.quantum.entity.player.Player.closeMenu()"""
        super(Player, self).closeMenu()

    @overload
    def drop(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.entity.player.Player.drop(dev.ultreon.quantum.item.ItemStack)"""
        super(_Player, self).drop(arg0)

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'._wrap(super(entity.Entity, self).getRotation())

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(_entity.Entity, self).setUuid(arg0)

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(_entity.Entity, self).onPipeline(arg0)

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isAffectedByFluid()"""
        return bool._wrap(super(Player, self).isAffectedByFluid())

    @override
    @overload
    def setInvincible(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setInvincible(boolean)"""
        super(_Player, self).setInvincible(_boolean.valueOf(arg0))

    @override
    @overload
    def moveTowards(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.moveTowards(double,double,double,double)"""
        super(_entity.LivingEntity, self).moveTowards(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'._wrap(super(entity.Entity, self).getBoundingBox())

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'._wrap(super(entity.Entity, self).getRng())

    @property
    def inventory(self, value: 'menu.Inventory'):
        super(_Player).inventory(value)

    @override
    @overload
    def jump(self):
        """public void dev.ultreon.quantum.entity.player.Player.jump()"""
        super(Player, self).jump()

    @overload
    def openMenu(self, arg0: 'ContainerMenu'):
        """public void dev.ultreon.quantum.entity.player.Player.openMenu(dev.ultreon.quantum.menu.ContainerMenu)"""
        super(_Player, self).openMenu(arg0)

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(_entity.Entity, self).setX(_double.valueOf(arg0))

    @override
    @overload
    def isDead(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isDead()"""
        return bool._wrap(super(entity.LivingEntity, self).isDead())

    @override
    @overload
    def getSpeed(self) -> float:
        """public double dev.ultreon.quantum.entity.player.Player.getSpeed()"""
        return float._wrap(super(Player, self).getSpeed())

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_entity.Entity, self).setVelocity(arg0)

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool._wrap(super(entity.Entity, self).isInWater())

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(_entity.Entity, self).teleportTo(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(_entity.Entity, self).setGravity(_float.valueOf(arg0))

    @overload
    def isBuilder(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isBuilder()"""
        return bool._wrap(super(Player, self).isBuilder())

    @override
    @overload
    def getHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getHealth()"""
        return float._wrap(super(entity.LivingEntity, self).getHealth())

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_entity.Entity, self).hasExplicitPermission(arg0))

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool._wrap(super(entity.Entity, self).isAdmin())

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float._wrap(super(entity.Entity, self).getX())

    @overload
    def setRunning(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setRunning(boolean)"""
        super(_Player, self).setRunning(_boolean.valueOf(arg0))

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.LivingEntity.getLookVector()"""
        return 'vector.Vec3d'._wrap(super(entity.LivingEntity, self).getLookVector())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setCursor(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.entity.player.Player.setCursor(dev.ultreon.quantum.item.ItemStack)"""
        super(_Player, self).setCursor(arg0)

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox._wrap(_Entity.getBoundingBox(arg0, arg1))

    @overload
    def closeMenu(self, arg0: 'CrateMenu'):
        """public void dev.ultreon.quantum.entity.player.Player.closeMenu(dev.ultreon.quantum.menu.CrateMenu)"""
        super(_Player, self).closeMenu(arg0)

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(_entity.Entity, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def setHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setHealth(float)"""
        super(_entity.LivingEntity, self).setHealth(_float.valueOf(arg0))

    @overload
    def getOpenMenu(self) -> 'menu.ContainerMenu':
        """public dev.ultreon.quantum.menu.ContainerMenu dev.ultreon.quantum.entity.player.Player.getOpenMenu()"""
        return 'menu.ContainerMenu'._wrap(super(Player, self).getOpenMenu())

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(_entity.Entity, self).teleportTo(arg0)

    @overload
    def setCrouching(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setCrouching(boolean)"""
        super(_Player, self).setCrouching(_boolean.valueOf(arg0))

    @overload
    def setSpectating(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setSpectating(boolean)"""
        super(_Player, self).setSpectating(_boolean.valueOf(arg0))

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(_entity.Entity, self).setId(_int.valueOf(arg0))

    @override
    @overload
    def getHurtSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.player.Player.getHurtSound()"""
        return 'world.SoundEvent'._wrap(super(Player, self).getHurtSound())

    @overload
    def getWalkingSpeed(self) -> float:
        """public float dev.ultreon.quantum.entity.player.Player.getWalkingSpeed()"""
        return float._wrap(super(Player, self).getWalkingSpeed())

    @override
    @overload
    def createAiGoals(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.createAiGoals()"""
        super(entity.LivingEntity, self).createAiGoals()

    @overload
    def rayCast(self, arg0: 'Collection') -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.player.Player.rayCast(java.util.Collection<dev.ultreon.quantum.entity.Entity>)"""
        return 'entity.Entity'._wrap(super(_Player, self).rayCast(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(_entity.Entity, self).setZ(_double.valueOf(arg0))

    @override
    @overload
    def applyEffect(self, arg0: 'AppliedEffect'):
        """public void dev.ultreon.quantum.entity.LivingEntity.applyEffect(dev.ultreon.quantum.item.food.AppliedEffect)"""
        super(_entity.LivingEntity, self).applyEffect(arg0)

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_entity.Entity, self).teleportTo(arg0)

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float._wrap(super(_entity.Entity, self).distanceTo(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.player.Player.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Player, self).setPosition(arg0)

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'._wrap(super(entity.Entity, self).getWorld())

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.player.Player.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Player, self).setRotation(arg0)

    @override
    @overload
    def getType(self) -> 'entity.EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'entity.EntityType'._wrap(super(entity.Entity, self).getType())

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.player.Player.getDisplayName()"""
        return 'text.TextObject'._wrap(super(Player, self).getDisplayName())

    @overload
    def isCrouching(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isCrouching()"""
        return bool._wrap(super(Player, self).isCrouching())

    @overload
    def getCursor(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.entity.player.Player.getCursor()"""
        return 'item.ItemStack'._wrap(super(Player, self).getCursor())

    @overload
    def getFlyingSpeed(self) -> float:
        """public float dev.ultreon.quantum.entity.player.Player.getFlyingSpeed()"""
        return float._wrap(super(Player, self).getFlyingSpeed())

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.player.Player.load(dev.ultreon.ubo.types.MapType)"""
        super(_Player, self).load(arg0)

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float._wrap(super(entity.Entity, self).getGravity())

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0))

    @override
    @overload
    def getJumpVel(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getJumpVel()"""
        return float._wrap(super(entity.LivingEntity, self).getJumpVel())

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_entity.Entity, self).rotate(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isSwimming(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isSwimming()"""
        return bool._wrap(super(Player, self).isSwimming())

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(_entity.Entity, self).setY(_double.valueOf(arg0))

    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float):
        """public void dev.ultreon.quantum.entity.player.Player.playSound(dev.ultreon.quantum.world.SoundEvent,float)"""
        super(_Player, self).playSound(arg0, _float.valueOf(arg1))

    @overload
    def rayCast(self) -> 'util.HitResult':
        """public dev.ultreon.quantum.util.HitResult dev.ultreon.quantum.entity.player.Player.rayCast()"""
        return 'util.HitResult'._wrap(super(Player, self).rayCast())

    @override
    @overload
    def getLastDamageSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.LivingEntity.getLastDamageSource()"""
        return 'damagesource.DamageSource'._wrap(super(entity.LivingEntity, self).getLastDamageSource())

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.player.Player.tick()"""
        super(Player, self).tick()

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.player.Player.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_Player, self).save(arg0))

    @overload
    def getEyeHeight(self) -> float:
        """public float dev.ultreon.quantum.entity.player.Player.getEyeHeight()"""
        return float._wrap(super(Player, self).getEyeHeight())

    @overload
    def setAllowFlight(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setAllowFlight(boolean)"""
        super(_Player, self).setAllowFlight(_boolean.valueOf(arg0))

    @overload
    def dropItem(self):
        """public void dev.ultreon.quantum.entity.player.Player.dropItem()"""
        super(Player, self).dropItem()

    @override
    @overload
    def kill(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.kill()"""
        super(entity.LivingEntity, self).kill()

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'._wrap(super(entity.Entity, self).getVelocity())

    @override
    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isInvincible()"""
        return bool._wrap(super(Player, self).isInvincible())

    @overload
    def setGameMode(self, arg0: 'GameMode'):
        """public void dev.ultreon.quantum.entity.player.Player.setGameMode(dev.ultreon.quantum.util.GameMode)"""
        super(_Player, self).setGameMode(arg0)

    @overload
    def setWalkingSpeed(self, arg0: float):
        """public void dev.ultreon.quantum.entity.player.Player.setWalkingSpeed(float)"""
        super(_Player, self).setWalkingSpeed(_float.valueOf(arg0))

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasExplicitPermission(arg0))

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @overload
    def getGamemode(self) -> 'util.GameMode':
        """public dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.entity.player.Player.getGamemode()"""
        return 'util.GameMode'._wrap(super(Player, self).getGamemode())

    @overload
    def nearestEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.player.Player.nearestEntity()"""
        return 'entity.Entity'._wrap(super(Player, self).nearestEntity())

    @override
    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.LivingEntity.getAge()"""
        return int._wrap(super(entity.LivingEntity, self).getAge())

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(entity.Entity, self).sendPipeline()

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float._wrap(super(entity.Entity, self).getYRot())

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'._wrap(super(_entity.Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(entity.Entity, self).markRemoved()

    @overload
    def setFlyingSpeed(self, arg0: float):
        """public void dev.ultreon.quantum.entity.player.Player.setFlyingSpeed(float)"""
        super(_Player, self).setFlyingSpeed(_float.valueOf(arg0))

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool._wrap(super(entity.Entity, self).isInVoid())

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(_entity.Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'._wrap(super(entity.Entity, self).getPipeline())

    @override
    @overload
    def onDeath(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDeath(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_entity.LivingEntity, self).onDeath(arg0)

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(_entity.Entity, self).sendMessage(arg0)

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float._wrap(super(_entity.Entity, self).distanceTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str._wrap(super(entity.Entity, self).getName())

    @overload
    def isFlying(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.player.Player.isFlying()"""
        return bool._wrap(super(Player, self).isFlying())

    @overload
    def onHurt(self, arg0: float, arg1: 'DamageSource') -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.onHurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        return bool._wrap(super(_entity.LivingEntity, self).onHurt(_float.valueOf(arg0), arg1))

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @overload
    def openInventory(self):
        """public void dev.ultreon.quantum.entity.player.Player.openInventory()"""
        super(Player, self).openInventory()

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool._wrap(super(entity.Entity, self).isMarkedForRemoval())

    @overload
    def setFlying(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.player.Player.setFlying(boolean)"""
        super(_Player, self).setFlying(_boolean.valueOf(arg0))

    @override
    @overload
    def getMaxHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getMaxHealth()"""
        return float._wrap(super(entity.LivingEntity, self).getMaxHealth())

    @overload
    def rotateHead(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.player.Player.rotateHead(float,float)"""
        super(_Player, self).rotateHead(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.entity.LivingEntity.getChunkPos()"""
        return 'world.ChunkPos'._wrap(super(entity.LivingEntity, self).getChunkPos())

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'._wrap(super(entity.Entity, self).getSize())

    @override
    @overload
    def getAttributes(self) -> 'entity.AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'entity.AttributeMap'._wrap(super(entity.Entity, self).getAttributes())

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(_entity.Entity, self).teleportTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @overload
    def selectBlock(self, arg0: int):
        """public void dev.ultreon.quantum.entity.player.Player.selectBlock(int)"""
        super(_Player, self).selectBlock(_int.valueOf(arg0))

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(_entity.LivingEntity, self).onPrepareSpawn(arg0)

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int._wrap(super(entity.Entity, self).getId())

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(_entity.Entity, self).setYRot(_float.valueOf(arg0))

    @override
    @overload
    def setMaxHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setMaxHealth(float)"""
        super(_entity.LivingEntity, self).setMaxHealth(_float.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.entity.player.PlayerAbilities
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.entity.player.PlayerAbilities as _PlayerAbilities
_PlayerAbilities = _PlayerAbilities
import java.lang.String as _String
_String = _String
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerAbilities():
    """dev.ultreon.quantum.entity.player.PlayerAbilities"""
 
    @staticmethod
    def _wrap(java_value: _PlayerAbilities) -> 'PlayerAbilities':
        return PlayerAbilities(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerAbilities):
        """
        Dynamic initializer for PlayerAbilities.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerAbilities__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerAbilities__wrapper":
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.player.PlayerAbilities()"""
        val = _PlayerAbilities()
        self.__wrapper = val

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
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.player.PlayerAbilities.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_PlayerAbilities, self).save(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.player.PlayerAbilities()"""
        val = _PlayerAbilities()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.player.PlayerAbilities.load(dev.ultreon.ubo.types.MapType)"""
        super(_PlayerAbilities, self).load(arg0)

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