from __future__ import annotations
from overload import overload


 
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.entity.AttributeModifier as __AttributeModifier
__AttributeModifier = __AttributeModifier
import dev.ultreon.quantum.entity.AttributeMap as __AttributeMap
__AttributeMap = __AttributeMap
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AttributeMap():
    """dev.ultreon.quantum.entity.AttributeMap"""
 
    @staticmethod
    def __wrap(java_value: __AttributeMap) -> 'AttributeMap':
        return AttributeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AttributeMap):
        """
        Dynamic initializer for AttributeMap.
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
    def addModifier(self, arg0: 'Attribute', arg1: 'AttributeModifier'):
        """public void dev.ultreon.quantum.entity.AttributeMap.addModifier(dev.ultreon.quantum.entity.Attribute,dev.ultreon.quantum.entity.AttributeModifier)"""
        super(__AttributeMap, self).addModifier(arg0, arg1)

    @overload
    def get(self, arg0: 'Attribute') -> float:
        """public double dev.ultreon.quantum.entity.AttributeMap.get(dev.ultreon.quantum.entity.Attribute)"""
        return float.__wrap(super(__AttributeMap, self).get(arg0))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.AttributeMap()"""
        val = __AttributeMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBase(self, arg0: 'Attribute') -> float:
        """public double dev.ultreon.quantum.entity.AttributeMap.getBase(dev.ultreon.quantum.entity.Attribute)"""
        return float.__wrap(super(__AttributeMap, self).getBase(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.AttributeMap()"""
        val = __AttributeMap()
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def removeModifier(self, arg0: 'Attribute', arg1: 'UUID') -> 'AttributeModifier':
        """public dev.ultreon.quantum.entity.AttributeModifier dev.ultreon.quantum.entity.AttributeMap.removeModifier(dev.ultreon.quantum.entity.Attribute,java.util.UUID)"""
        return 'AttributeModifier'.__wrap(super(__AttributeMap, self).removeModifier(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setBase(self, arg0: 'Attribute', arg1: float):
        """public void dev.ultreon.quantum.entity.AttributeMap.setBase(dev.ultreon.quantum.entity.Attribute,double)"""
        super(__AttributeMap, self).setBase(arg0, __double.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.entity.AttributeMap
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.entity.AttributeModifier as __AttributeModifier
__AttributeModifier = __AttributeModifier
import dev.ultreon.quantum.entity.AttributeMap as __AttributeMap
__AttributeMap = __AttributeMap
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AttributeMap():
    """dev.ultreon.quantum.entity.AttributeMap"""
 
    @staticmethod
    def __wrap(java_value: __AttributeMap) -> 'AttributeMap':
        return AttributeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AttributeMap):
        """
        Dynamic initializer for AttributeMap.
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
    def addModifier(self, arg0: 'Attribute', arg1: 'AttributeModifier'):
        """public void dev.ultreon.quantum.entity.AttributeMap.addModifier(dev.ultreon.quantum.entity.Attribute,dev.ultreon.quantum.entity.AttributeModifier)"""
        super(__AttributeMap, self).addModifier(arg0, arg1)

    @overload
    def get(self, arg0: 'Attribute') -> float:
        """public double dev.ultreon.quantum.entity.AttributeMap.get(dev.ultreon.quantum.entity.Attribute)"""
        return float.__wrap(super(__AttributeMap, self).get(arg0))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.AttributeMap()"""
        val = __AttributeMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBase(self, arg0: 'Attribute') -> float:
        """public double dev.ultreon.quantum.entity.AttributeMap.getBase(dev.ultreon.quantum.entity.Attribute)"""
        return float.__wrap(super(__AttributeMap, self).getBase(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.AttributeMap()"""
        val = __AttributeMap()
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def removeModifier(self, arg0: 'Attribute', arg1: 'UUID') -> 'AttributeModifier':
        """public dev.ultreon.quantum.entity.AttributeModifier dev.ultreon.quantum.entity.AttributeMap.removeModifier(dev.ultreon.quantum.entity.Attribute,java.util.UUID)"""
        return 'AttributeModifier'.__wrap(super(__AttributeMap, self).removeModifier(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setBase(self, arg0: 'Attribute', arg1: float):
        """public void dev.ultreon.quantum.entity.AttributeMap.setBase(dev.ultreon.quantum.entity.Attribute,double)"""
        super(__AttributeMap, self).setBase(arg0, __double.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.entity.AttributeMap 
 
 
# CLASS: dev.ultreon.quantum.entity.AttributeModifier$Operation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from builtins import float
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.entity.AttributeModifier as __AttributeModifier_Operation
__Operation = __AttributeModifier_Operation.Operation
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Operation():
    """dev.ultreon.quantum.entity.AttributeModifier.Operation"""
 
    @staticmethod
    def __wrap(java_value: __Operation) -> 'Operation':
        return Operation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Operation):
        """
        Dynamic initializer for Operation.
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
 
    # public static final dev.ultreon.quantum.entity.AttributeModifier$Operation dev.ultreon.quantum.entity.AttributeModifier$Operation.PLUS
    PLUS: 'Operation' = __wrap(__Operation.PLUS)

    # public static final dev.ultreon.quantum.entity.AttributeModifier$Operation dev.ultreon.quantum.entity.AttributeModifier$Operation.MULTIPLY
    MULTIPLY: 'Operation' = __wrap(__Operation.MULTIPLY)


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

    @overload
    def calculate(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.entity.AttributeModifier$Operation.calculate(double,double)"""
        return float.__wrap(super(__Operation, self).calculate(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Operation':
        """public static dev.ultreon.quantum.entity.AttributeModifier$Operation dev.ultreon.quantum.entity.AttributeModifier$Operation.valueOf(java.lang.String)"""
        return Operation.__wrap(__Operation.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Operation']:
        """public static dev.ultreon.quantum.entity.AttributeModifier$Operation[] dev.ultreon.quantum.entity.AttributeModifier$Operation.values()"""
        return List[Operation].__wrap(__Operation.values()) 
 
 
# CLASS: dev.ultreon.quantum.entity.DroppedItem
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.entity import util
except ImportError:
    util = __import_once__("pyquantum.entity.util")

import java.util.UUID as UUID
import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import java.lang.Boolean as __boolean
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
import dev.ultreon.quantum.entity.AttributeMap as __AttributeMap
__AttributeMap = __AttributeMap
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.entity.EntityType as __EntityType
__EntityType = __EntityType
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import java.lang.Double as __double
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.world.Location as __Location
__Location = __Location
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.entity.DroppedItem as __DroppedItem
__DroppedItem = __DroppedItem
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import dev.ultreon.quantum.world.rng.RNG as __RNG
__RNG = __RNG
 
class DroppedItem():
    """dev.ultreon.quantum.entity.DroppedItem"""
 
    @staticmethod
    def __wrap(java_value: __DroppedItem) -> 'DroppedItem':
        return DroppedItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DroppedItem):
        """
        Dynamic initializer for DroppedItem.
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
    def getStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.entity.DroppedItem.getStack()"""
        return 'item.ItemStack'.__wrap(super(DroppedItem, self).getStack())

    @overload
    def __init__(self, arg0: 'World', arg1: 'ItemStack', arg2: 'Vec3d', arg3: 'Vec3d'):
        """public dev.ultreon.quantum.entity.DroppedItem(dev.ultreon.quantum.world.World,dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = __DroppedItem(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(__Entity, self).teleportDimension(arg0, arg1)

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int.__wrap(super(Entity, self).getId())

    @overload
    def getPickupDelay(self) -> int:
        """public int dev.ultreon.quantum.entity.DroppedItem.getPickupDelay()"""
        return int.__wrap(super(DroppedItem, self).getPickupDelay())

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool.__wrap(super(Entity, self).isInVoid())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.DroppedItem.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__DroppedItem, self).save(arg0))

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(__Entity, self).sendMessage(arg0)

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'.__wrap(super(Entity, self).getUuid())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float.__wrap(super(Entity, self).getYRot())

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.DroppedItem(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.Entity>,dev.ultreon.quantum.world.World)"""
        val = __DroppedItem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.DroppedItem.getAge()"""
        return int.__wrap(super(DroppedItem, self).getAge())

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'.__wrap(super(Entity, self).getSize())

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'.__wrap(super(Entity, self).getWorld())

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(__Entity, self).setZ(__double.valueOf(arg0))

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(__Entity, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(__Entity, self).teleportTo(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(__Entity, self).setGravity(__float.valueOf(arg0))

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity.__wrap(__Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float.__wrap(super(Entity, self).getGravity())

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float.__wrap(super(Entity, self).getZ())

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(__Entity, self).setY(__double.valueOf(arg0))

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(Entity, self).getDisplayName())

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float.__wrap(super(Entity, self).getXRot())

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__Entity, self).hasExplicitPermission(arg0))

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float.__wrap(super(Entity, self).getX())

    @overload
    def setPickupDelay(self, arg0: int):
        """public void dev.ultreon.quantum.entity.DroppedItem.setPickupDelay(int)"""
        super(__DroppedItem, self).setPickupDelay(__int.valueOf(arg0))

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).rotate(arg0)

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'.__wrap(super(__Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(__Entity, self).setX(__double.valueOf(arg0))

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.DroppedItem.tick()"""
        super(DroppedItem, self).tick()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float.__wrap(super(__Entity, self).distanceTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float.__wrap(super(Entity, self).getY())

    @override
    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'.__wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.DroppedItem.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(__DroppedItem, self).onPrepareSpawn(arg0)

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'.__wrap(super(Entity, self).getLocation())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'.__wrap(super(Entity, self).getPipeline())

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float.__wrap(super(__Entity, self).distanceTo(arg0))

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool.__wrap(super(__Entity, self).move(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).loadWithPos(arg0)

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.DroppedItem.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(__DroppedItem, self).onPipeline(arg0)

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(__Entity, self).teleportTo(arg0)

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getLookVector()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getLookVector())

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'.__wrap(super(Entity, self).getBlockPos())

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(__Entity, self).teleportTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(__Entity, self).sendMessage(arg0)

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).teleportTo(arg0)

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(__Entity, self).setYRot(__float.valueOf(arg0))

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(__Entity, self).setXRot(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setStack(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.entity.DroppedItem.setStack(dev.ultreon.quantum.item.ItemStack)"""
        super(__DroppedItem, self).setStack(arg0)

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool.__wrap(super(Entity, self).isAdmin())

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(__Entity, self).setId(__int.valueOf(arg0))

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).setRotation(arg0)

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'.__wrap(super(Entity, self).getRotation())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getPosition())

    @override
    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'.__wrap(super(Entity, self).getType())

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setPosition(arg0)

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.DroppedItem.load(dev.ultreon.ubo.types.MapType)"""
        super(__DroppedItem, self).load(arg0)

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool.__wrap(super(Entity, self).isAffectedByFluid())

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setVelocity(arg0)

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'.__wrap(super(Entity, self).getRng())

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox.__wrap(__Entity.getBoundingBox(arg0, arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str.__wrap(super(Entity, self).getName())

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'.__wrap(super(Entity, self).getBoundingBox())

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(__Entity, self).setUuid(arg0)

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
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool.__wrap(super(Entity, self).isInWater())

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool.__wrap(super(Entity, self).isMarkedForRemoval())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(__Entity, self).setPosition(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str.__wrap(super(Entity, self).getPublicName()) 
 
 
# CLASS: dev.ultreon.quantum.entity.Animal
import dev.ultreon.quantum.entity.Animal as __Animal
__Animal = __Animal
 
class Animal(ABC):
    """dev.ultreon.quantum.entity.Animal"""
 
    @staticmethod
    def __wrap(java_value: __Animal) -> 'Animal':
        return Animal(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Animal):
        """
        Dynamic initializer for Animal.
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
 
 
# CLASS: dev.ultreon.quantum.entity.EntityType
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.entity import util
except ImportError:
    util = __import_once__("pyquantum.entity.util")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import dev.ultreon.quantum.entity.EntityType as __EntityType
__EntityType = __EntityType
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class EntityType(ABC):
    """dev.ultreon.quantum.entity.EntityType"""
 
    @staticmethod
    def __wrap(java_value: __EntityType) -> 'EntityType':
        return EntityType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityType):
        """
        Dynamic initializer for EntityType.
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
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.entity.EntityType.getId()"""
        return 'util.Identifier'.__wrap(super(EntityType, self).getId())

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
    def spawn(self, arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public T dev.ultreon.quantum.entity.EntityType.spawn(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return 'Entity'.__wrap(super(__EntityType, self).spawn(arg0, arg1))

    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.EntityType.getSize()"""
        return 'util.EntitySize'.__wrap(super(EntityType, self).getSize())

    @overload
    def spawn(self, arg0: 'World') -> 'Entity':
        """public T dev.ultreon.quantum.entity.EntityType.spawn(dev.ultreon.quantum.world.World)"""
        return 'Entity'.__wrap(super(__EntityType, self).spawn(arg0))

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

    @abstractmethod
    def create(self, arg0: 'World'):
        """public abstract T dev.ultreon.quantum.entity.EntityType.create(dev.ultreon.quantum.world.World)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.entity.Entity$Pose
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
import dev.ultreon.quantum.entity.Entity as __Entity_Pose
__Pose = __Entity_Pose.Pose
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Pose():
    """dev.ultreon.quantum.entity.Entity.Pose"""
 
    @staticmethod
    def __wrap(java_value: __Pose) -> 'Pose':
        return Pose(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pose):
        """
        Dynamic initializer for Pose.
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
 
    # public static final dev.ultreon.quantum.entity.Entity$Pose dev.ultreon.quantum.entity.Entity$Pose.IDLE
    IDLE: 'Pose' = __wrap(__Pose.IDLE)

    # public static final dev.ultreon.quantum.entity.Entity$Pose dev.ultreon.quantum.entity.Entity$Pose.WALKING
    WALKING: 'Pose' = __wrap(__Pose.WALKING)


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

    @staticmethod
    @overload
    def values() -> List['Pose']:
        """public static dev.ultreon.quantum.entity.Entity$Pose[] dev.ultreon.quantum.entity.Entity$Pose.values()"""
        return List[Pose].__wrap(__Pose.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Pose':
        """public static dev.ultreon.quantum.entity.Entity$Pose dev.ultreon.quantum.entity.Entity$Pose.valueOf(java.lang.String)"""
        return Pose.__wrap(__Pose.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.entity.LivingEntity
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.entity import util
except ImportError:
    util = __import_once__("pyquantum.entity.util")

import java.util.UUID as UUID
import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
import java.lang.Boolean as __boolean
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = __import_once__("pyquantum.item.food")

import dev.ultreon.quantum.entity.AttributeMap as __AttributeMap
__AttributeMap = __AttributeMap
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.entity.EntityType as __EntityType
__EntityType = __EntityType
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.entity.damagesource.DamageSource as __DamageSource
__DamageSource = __DamageSource
import java.lang.Double as __double
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

import dev.ultreon.quantum.entity.LivingEntity as __LivingEntity
__LivingEntity = __LivingEntity
import dev.ultreon.quantum.world.SoundEvent as __SoundEvent
__SoundEvent = __SoundEvent
from builtins import float
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.world.Location as __Location
__Location = __Location
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = __import_once__("pyquantum.entity.damagesource")

import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import dev.ultreon.quantum.world.rng.RNG as __RNG
__RNG = __RNG
 
class LivingEntity():
    """dev.ultreon.quantum.entity.LivingEntity"""
 
    @staticmethod
    def __wrap(java_value: __LivingEntity) -> 'LivingEntity':
        return LivingEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LivingEntity):
        """
        Dynamic initializer for LivingEntity.
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
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(__Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int.__wrap(super(Entity, self).getId())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isWalking()"""
        return bool.__wrap(super(LivingEntity, self).isWalking())

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'.__wrap(super(Entity, self).getUuid())

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float.__wrap(super(Entity, self).getYRot())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(__Entity, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getDeathSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getDeathSound()"""
        return 'world.SoundEvent'.__wrap(super(LivingEntity, self).getDeathSound())

    @overload
    def getHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getHealth()"""
        return float.__wrap(super(LivingEntity, self).getHealth())

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float.__wrap(super(Entity, self).getGravity())

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(__Entity, self).setY(__double.valueOf(arg0))

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float.__wrap(super(Entity, self).getXRot())

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(__LivingEntity, self).onPrepareSpawn(arg0)

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).rotate(arg0)

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'.__wrap(super(__Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(__Entity, self).setX(__double.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float.__wrap(super(__Entity, self).distanceTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'.__wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'.__wrap(super(Entity, self).getPipeline())

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float.__wrap(super(__Entity, self).distanceTo(arg0))

    @overload
    def jump(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.jump()"""
        super(LivingEntity, self).jump()

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(__Entity, self).teleportTo(arg0)

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(__Entity, self).sendMessage(arg0)

    @overload
    def hurt(self, arg0: float, arg1: 'DamageSource'):
        """public final void dev.ultreon.quantum.entity.LivingEntity.hurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).hurt(__float.valueOf(arg0), arg1)

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).teleportTo(arg0)

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(__Entity, self).setYRot(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.LivingEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__LivingEntity, self).save(arg0))

    @overload
    def getLastDamageSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.LivingEntity.getLastDamageSource()"""
        return 'damagesource.DamageSource'.__wrap(super(LivingEntity, self).getLastDamageSource())

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(__LivingEntity, self).load(arg0)

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setPosition(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str.__wrap(super(Entity, self).getName())

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(__Entity, self).setUuid(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def moveTowards(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.moveTowards(double,double,double,double)"""
        super(__LivingEntity, self).moveTowards(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool.__wrap(super(Entity, self).isInWater())

    @overload
    def onDeath(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDeath(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).onDeath(arg0)

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(__Entity, self).setPosition(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @overload
    def isDead(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isDead()"""
        return bool.__wrap(super(LivingEntity, self).isDead())

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str.__wrap(super(Entity, self).getPublicName())

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def getJumpVel(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getJumpVel()"""
        return float.__wrap(super(LivingEntity, self).getJumpVel())

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool.__wrap(super(Entity, self).isInVoid())

    @overload
    def setMaxHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setMaxHealth(float)"""
        super(__LivingEntity, self).setMaxHealth(__float.valueOf(arg0))

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(__Entity, self).sendMessage(arg0)

    @overload
    def setInvincible(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.LivingEntity.setInvincible(boolean)"""
        super(__LivingEntity, self).setInvincible(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).onPipeline(arg0)

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'.__wrap(super(Entity, self).getSize())

    @overload
    def createAiGoals(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.createAiGoals()"""
        super(LivingEntity, self).createAiGoals()

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def getSpeed(self) -> float:
        """public double dev.ultreon.quantum.entity.LivingEntity.getSpeed()"""
        return float.__wrap(super(LivingEntity, self).getSpeed())

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0))

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'.__wrap(super(Entity, self).getWorld())

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(__Entity, self).setZ(__double.valueOf(arg0))

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(__Entity, self).teleportTo(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(__Entity, self).setGravity(__float.valueOf(arg0))

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity.__wrap(__Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getHurtSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getHurtSound()"""
        return 'world.SoundEvent'.__wrap(super(LivingEntity, self).getHurtSound())

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float.__wrap(super(Entity, self).getZ())

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(Entity, self).getDisplayName())

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__Entity, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float.__wrap(super(Entity, self).getX())

    @overload
    def getChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.entity.LivingEntity.getChunkPos()"""
        return 'world.ChunkPos'.__wrap(super(LivingEntity, self).getChunkPos())

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float.__wrap(super(Entity, self).getY())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'.__wrap(super(Entity, self).getLocation())

    @overload
    def kill(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.kill()"""
        super(LivingEntity, self).kill()

    @overload
    def onDropItems(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDropItems(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).onDropItems(arg0)

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool.__wrap(super(__Entity, self).move(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).loadWithPos(arg0)

    @overload
    def setJumpVel(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setJumpVel(float)"""
        super(__LivingEntity, self).setJumpVel(__float.valueOf(arg0))

    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.LivingEntity.getAge()"""
        return int.__wrap(super(LivingEntity, self).getAge())

    @overload
    def getMaxHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getMaxHealth()"""
        return float.__wrap(super(LivingEntity, self).getMaxHealth())

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'.__wrap(super(Entity, self).getBlockPos())

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(__Entity, self).teleportTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.tick()"""
        super(LivingEntity, self).tick()

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(__Entity, self).setXRot(__float.valueOf(arg0))

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool.__wrap(super(Entity, self).isAdmin())

    @overload
    def applyEffect(self, arg0: 'AppliedEffect'):
        """public void dev.ultreon.quantum.entity.LivingEntity.applyEffect(dev.ultreon.quantum.item.food.AppliedEffect)"""
        super(__LivingEntity, self).applyEffect(arg0)

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(__Entity, self).setId(__int.valueOf(arg0))

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).setRotation(arg0)

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'.__wrap(super(Entity, self).getRotation())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getPosition())

    @override
    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'.__wrap(super(Entity, self).getType())

    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isInvincible()"""
        return bool.__wrap(super(LivingEntity, self).isInvincible())

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool.__wrap(super(Entity, self).isAffectedByFluid())

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.LivingEntity.getLookVector()"""
        return 'vector.Vec3d'.__wrap(super(LivingEntity, self).getLookVector())

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setVelocity(arg0)

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'.__wrap(super(Entity, self).getRng())

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox.__wrap(__Entity.getBoundingBox(arg0, arg1))

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'.__wrap(super(Entity, self).getBoundingBox())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setHealth(float)"""
        super(__LivingEntity, self).setHealth(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.LivingEntity(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.LivingEntity>,dev.ultreon.quantum.world.World)"""
        val = __LivingEntity(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def onHurt(self, arg0: float, arg1: 'DamageSource') -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.onHurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        return bool.__wrap(super(__LivingEntity, self).onHurt(__float.valueOf(arg0), arg1))

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool.__wrap(super(Entity, self).isMarkedForRemoval()) 
 
 
# CLASS: dev.ultreon.quantum.entity.EntityTypes
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
import dev.ultreon.quantum.entity.EntityTypes as __EntityTypes
__EntityTypes = __EntityTypes
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntityTypes():
    """dev.ultreon.quantum.entity.EntityTypes"""
 
    @staticmethod
    def __wrap(java_value: __EntityTypes) -> 'EntityTypes':
        return EntityTypes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityTypes):
        """
        Dynamic initializer for EntityTypes.
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
 
    # public static final dev.ultreon.quantum.entity.EntityType<dev.ultreon.quantum.entity.player.Player> dev.ultreon.quantum.entity.EntityTypes.PLAYER
    PLAYER: 'EntityType' = __wrap(__EntityType.PLAYER)

    # public static final dev.ultreon.quantum.entity.EntityType<dev.ultreon.quantum.entity.DroppedItem> dev.ultreon.quantum.entity.EntityTypes.DROPPED_ITEM
    DROPPED_ITEM: 'EntityType' = __wrap(__EntityType.DROPPED_ITEM)

    # public static final dev.ultreon.quantum.entity.EntityType<dev.ultreon.quantum.entity.Something> dev.ultreon.quantum.entity.EntityTypes.SOMETHING
    SOMETHING: 'EntityType' = __wrap(__EntityType.SOMETHING)

    # public static final dev.ultreon.quantum.entity.EntityType<dev.ultreon.quantum.entity.Pig> dev.ultreon.quantum.entity.EntityTypes.PIG
    PIG: 'EntityType' = __wrap(__EntityType.PIG)


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
    def __init__(self):
        """public dev.ultreon.quantum.entity.EntityTypes()"""
        val = __EntityTypes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.EntityTypes()"""
        val = __EntityTypes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.entity.EntityTypes.init()"""
            __EntityTypes.init()

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
 
 
# CLASS: dev.ultreon.quantum.entity.EntityType$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.entity.EntityType as __EntityType_Builder
__Builder = __EntityType_Builder.Builder
import dev.ultreon.quantum.entity.EntityType as __EntityType
__EntityType = __EntityType
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.entity.EntityType.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.EntityType$Builder()"""
        val = __Builder()
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

    @overload
    def size(self, arg0: float, arg1: float) -> 'Builder':
        """public dev.ultreon.quantum.entity.EntityType$Builder<T> dev.ultreon.quantum.entity.EntityType$Builder.size(float,float)"""
        return 'Builder'.__wrap(super(__Builder, self).size(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def build(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<T> dev.ultreon.quantum.entity.EntityType$Builder.build()"""
        return 'EntityType'.__wrap(super(Builder, self).build())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def factory(self, arg0: 'EntityFactory') -> 'Builder':
        """public dev.ultreon.quantum.entity.EntityType$Builder<T> dev.ultreon.quantum.entity.EntityType$Builder.factory(dev.ultreon.quantum.entity.EntityType$EntityFactory<T>)"""
        return 'Builder'.__wrap(super(__Builder, self).factory(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.EntityType$Builder()"""
        val = __Builder()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.entity.Entity
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.entity import util
except ImportError:
    util = __import_once__("pyquantum.entity.util")

import java.util.UUID as UUID
import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import java.lang.Boolean as __boolean
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
import dev.ultreon.quantum.entity.AttributeMap as __AttributeMap
__AttributeMap = __AttributeMap
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.entity.EntityType as __EntityType
__EntityType = __EntityType
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import java.lang.Double as __double
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

from builtins import float
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.world.Location as __Location
__Location = __Location
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import dev.ultreon.quantum.world.rng.RNG as __RNG
__RNG = __RNG
 
class Entity():
    """dev.ultreon.quantum.entity.Entity"""
 
    @staticmethod
    def __wrap(java_value: __Entity) -> 'Entity':
        return Entity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entity):
        """
        Dynamic initializer for Entity.
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
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'.__wrap(super(Entity, self).getPipeline())

    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(__Entity, self).teleportTo(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'.__wrap(super(Entity, self).getSize())

    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(__Entity, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'.__wrap(super(Entity, self).getType())

    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float.__wrap(super(Entity, self).getGravity())

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(__Entity, self).sendMessage(arg0)

    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int.__wrap(super(Entity, self).getId())

    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'.__wrap(super(Entity, self).getBlockPos())

    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'.__wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'.__wrap(super(Entity, self).getUuid())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.load(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).load(arg0)

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(__Entity, self).setXRot(__float.valueOf(arg0))

    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).loadWithPos(arg0)

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float.__wrap(super(Entity, self).getY())

    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float.__wrap(super(Entity, self).getZ())

    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(__Entity, self).teleportTo(arg0)

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool.__wrap(super(Entity, self).isAffectedByFluid())

    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).rotate(arg0)

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity.__wrap(__Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__Entity, self).save(arg0))

    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(Entity, self).getDisplayName())

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(__Entity, self).setPosition(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__Entity, self).hasExplicitPermission(arg0))

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasExplicitPermission(arg0))

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'.__wrap(super(__Entity, self).getBoundingBox(arg0))

    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(__Entity, self).setGravity(__float.valueOf(arg0))

    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(__Entity, self).teleportTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float.__wrap(super(__Entity, self).distanceTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'.__wrap(super(Entity, self).getLocation())

    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(__Entity, self).setUuid(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(__Entity, self).teleportDimension(arg0, arg1)

    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'.__wrap(super(Entity, self).getWorld())

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float.__wrap(super(__Entity, self).distanceTo(arg0))

    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'.__wrap(super(Entity, self).getRotation())

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool.__wrap(super(__Entity, self).move(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(__Entity, self).setX(__double.valueOf(arg0))

    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getPosition())

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(__Entity, self).setZ(__double.valueOf(arg0))

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(__Entity, self).sendMessage(arg0)

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.Entity(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.Entity>,dev.ultreon.quantum.world.World)"""
        val = __Entity(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).teleportTo(arg0)

    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setPosition(arg0)

    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'.__wrap(super(Entity, self).getRng())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool.__wrap(super(Entity, self).isMarkedForRemoval())

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool.__wrap(super(Entity, self).isAdmin())

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.Entity.tick()"""
        super(Entity, self).tick()

    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(__Entity, self).setId(__int.valueOf(arg0))

    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).onPipeline(arg0)

    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool.__wrap(super(Entity, self).isInWater())

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float.__wrap(super(Entity, self).getX())

    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getLookVector()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getLookVector())

    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).setRotation(arg0)

    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).onPrepareSpawn(arg0)

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox.__wrap(__Entity.getBoundingBox(arg0, arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str.__wrap(super(Entity, self).getName())

    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(__Entity, self).setYRot(__float.valueOf(arg0))

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
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float.__wrap(super(Entity, self).getXRot())

    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setVelocity(arg0)

    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool.__wrap(super(Entity, self).isInVoid())

    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'.__wrap(super(Entity, self).getBoundingBox())

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(__Entity, self).setY(__double.valueOf(arg0))

    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float.__wrap(super(Entity, self).getYRot())

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str.__wrap(super(Entity, self).getPublicName()) 
 
 
# CLASS: dev.ultreon.quantum.entity.Attribute
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.entity.Attribute as __Attribute
__Attribute = __Attribute
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Attribute():
    """dev.ultreon.quantum.entity.Attribute"""
 
    @staticmethod
    def __wrap(java_value: __Attribute) -> 'Attribute':
        return Attribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Attribute):
        """
        Dynamic initializer for Attribute.
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
 
    # public static final dev.ultreon.quantum.entity.Attribute dev.ultreon.quantum.entity.Attribute.ENTITY_REACH
    ENTITY_REACH: 'Attribute' = __wrap(__Attribute.ENTITY_REACH)

    # public static final dev.ultreon.quantum.entity.Attribute dev.ultreon.quantum.entity.Attribute.BLOCK_REACH
    BLOCK_REACH: 'Attribute' = __wrap(__Attribute.BLOCK_REACH)

    # public static final dev.ultreon.quantum.entity.Attribute dev.ultreon.quantum.entity.Attribute.SPEED
    SPEED: 'Attribute' = __wrap(__Attribute.SPEED)


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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Attribute.toString()"""
        return str.__wrap(super(Attribute, self).toString())

    @overload
    def key(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Attribute.key()"""
        return str.__wrap(super(Attribute, self).key())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.Attribute.hashCode()"""
        return int.__wrap(super(Attribute, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.entity.Attribute(java.lang.String)"""
        val = __Attribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__Attribute, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.entity.Something
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import dev.ultreon.quantum.entity.AttributeMap as __AttributeMap
__AttributeMap = __AttributeMap
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import java.lang.Double as __double
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

import dev.ultreon.quantum.world.SoundEvent as __SoundEvent
__SoundEvent = __SoundEvent
import dev.ultreon.quantum.entity.LivingEntity as __LivingEntity
__LivingEntity = __LivingEntity
from builtins import float
import dev.ultreon.quantum.world.Location as __Location
__Location = __Location
import java.lang.Float as __float
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = __import_once__("pyquantum.entity.damagesource")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
from builtins import int
import dev.ultreon.quantum.world.rng.RNG as __RNG
__RNG = __RNG
try:
    from pyquantum.entity import util
except ImportError:
    util = __import_once__("pyquantum.entity.util")

import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
import java.lang.Boolean as __boolean
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = __import_once__("pyquantum.item.food")

import dev.ultreon.quantum.entity.EntityType as __EntityType
__EntityType = __EntityType
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import dev.ultreon.quantum.world.World as __World
__World = __World
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.entity.damagesource.DamageSource as __DamageSource
__DamageSource = __DamageSource
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.entity.Something as __Something
__Something = __Something
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

 
class Something():
    """dev.ultreon.quantum.entity.Something"""
 
    @staticmethod
    def __wrap(java_value: __Something) -> 'Something':
        return Something(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Something):
        """
        Dynamic initializer for Something.
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
    def setMaxHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setMaxHealth(float)"""
        super(__LivingEntity, self).setMaxHealth(__float.valueOf(arg0))

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(__Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def getDeathSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getDeathSound()"""
        return 'world.SoundEvent'.__wrap(super(LivingEntity, self).getDeathSound())

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int.__wrap(super(Entity, self).getId())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'.__wrap(super(Entity, self).getUuid())

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float.__wrap(super(Entity, self).getYRot())

    @override
    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.LivingEntity.getAge()"""
        return int.__wrap(super(LivingEntity, self).getAge())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(__Entity, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def isDead(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isDead()"""
        return bool.__wrap(super(LivingEntity, self).isDead())

    @override
    @overload
    def hurt(self, arg0: float, arg1: 'DamageSource'):
        """public final void dev.ultreon.quantum.entity.LivingEntity.hurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).hurt(__float.valueOf(arg0), arg1)

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float.__wrap(super(Entity, self).getGravity())

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(__Entity, self).setY(__double.valueOf(arg0))

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float.__wrap(super(Entity, self).getXRot())

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(__LivingEntity, self).onPrepareSpawn(arg0)

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).rotate(arg0)

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'.__wrap(super(__Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(__Entity, self).setX(__double.valueOf(arg0))

    @override
    @overload
    def getLastDamageSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.LivingEntity.getLastDamageSource()"""
        return 'damagesource.DamageSource'.__wrap(super(LivingEntity, self).getLastDamageSource())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float.__wrap(super(__Entity, self).distanceTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'.__wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isWalking()"""
        return bool.__wrap(super(LivingEntity, self).isWalking())

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'.__wrap(super(Entity, self).getPipeline())

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float.__wrap(super(__Entity, self).distanceTo(arg0))

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.Something(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.Something>,dev.ultreon.quantum.world.World)"""
        val = __Something(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(__Entity, self).teleportTo(arg0)

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(__Entity, self).sendMessage(arg0)

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).teleportTo(arg0)

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(__Entity, self).setYRot(__float.valueOf(arg0))

    @override
    @overload
    def moveTowards(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.moveTowards(double,double,double,double)"""
        super(__LivingEntity, self).moveTowards(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.LivingEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__LivingEntity, self).save(arg0))

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(__LivingEntity, self).load(arg0)

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setPosition(arg0)

    @override
    @overload
    def jump(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.jump()"""
        super(LivingEntity, self).jump()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str.__wrap(super(Entity, self).getName())

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(__Entity, self).setUuid(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isInvincible()"""
        return bool.__wrap(super(LivingEntity, self).isInvincible())

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool.__wrap(super(Entity, self).isInWater())

    @override
    @overload
    def getHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getHealth()"""
        return float.__wrap(super(LivingEntity, self).getHealth())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(__Entity, self).setPosition(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str.__wrap(super(Entity, self).getPublicName())

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def onDropItems(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDropItems(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).onDropItems(arg0)

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool.__wrap(super(Entity, self).isInVoid())

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(__Entity, self).sendMessage(arg0)

    @override
    @overload
    def getSpeed(self) -> float:
        """public double dev.ultreon.quantum.entity.LivingEntity.getSpeed()"""
        return float.__wrap(super(LivingEntity, self).getSpeed())

    @override
    @overload
    def setInvincible(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.LivingEntity.setInvincible(boolean)"""
        super(__LivingEntity, self).setInvincible(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).onPipeline(arg0)

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'.__wrap(super(Entity, self).getSize())

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0))

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'.__wrap(super(Entity, self).getWorld())

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(__Entity, self).setZ(__double.valueOf(arg0))

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(__Entity, self).teleportTo(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(__Entity, self).setGravity(__float.valueOf(arg0))

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity.__wrap(__Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.entity.LivingEntity.getChunkPos()"""
        return 'world.ChunkPos'.__wrap(super(LivingEntity, self).getChunkPos())

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float.__wrap(super(Entity, self).getZ())

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(Entity, self).getDisplayName())

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__Entity, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float.__wrap(super(Entity, self).getX())

    @override
    @overload
    def getMaxHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.Something.getMaxHealth()"""
        return float.__wrap(super(Something, self).getMaxHealth())

    @override
    @overload
    def getHurtSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.Something.getHurtSound()"""
        return 'world.SoundEvent'.__wrap(super(Something, self).getHurtSound())

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float.__wrap(super(Entity, self).getY())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'.__wrap(super(Entity, self).getLocation())

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool.__wrap(super(__Entity, self).move(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).loadWithPos(arg0)

    @override
    @overload
    def onDeath(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDeath(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).onDeath(arg0)

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'.__wrap(super(Entity, self).getBlockPos())

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(__Entity, self).teleportTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.tick()"""
        super(LivingEntity, self).tick()

    @override
    @overload
    def setHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setHealth(float)"""
        super(__LivingEntity, self).setHealth(__float.valueOf(arg0))

    @override
    @overload
    def applyEffect(self, arg0: 'AppliedEffect'):
        """public void dev.ultreon.quantum.entity.LivingEntity.applyEffect(dev.ultreon.quantum.item.food.AppliedEffect)"""
        super(__LivingEntity, self).applyEffect(arg0)

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(__Entity, self).setXRot(__float.valueOf(arg0))

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool.__wrap(super(Entity, self).isAdmin())

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(__Entity, self).setId(__int.valueOf(arg0))

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).setRotation(arg0)

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'.__wrap(super(Entity, self).getRotation())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getPosition())

    @override
    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'.__wrap(super(Entity, self).getType())

    @override
    @overload
    def getJumpVel(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getJumpVel()"""
        return float.__wrap(super(LivingEntity, self).getJumpVel())

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool.__wrap(super(Entity, self).isAffectedByFluid())

    @override
    @overload
    def createAiGoals(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.createAiGoals()"""
        super(LivingEntity, self).createAiGoals()

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.LivingEntity.getLookVector()"""
        return 'vector.Vec3d'.__wrap(super(LivingEntity, self).getLookVector())

    @override
    @overload
    def kill(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.kill()"""
        super(LivingEntity, self).kill()

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setVelocity(arg0)

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'.__wrap(super(Entity, self).getRng())

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox.__wrap(__Entity.getBoundingBox(arg0, arg1))

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'.__wrap(super(Entity, self).getBoundingBox())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setJumpVel(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setJumpVel(float)"""
        super(__LivingEntity, self).setJumpVel(__float.valueOf(arg0))

    @overload
    def onHurt(self, arg0: float, arg1: 'DamageSource') -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.onHurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        return bool.__wrap(super(__LivingEntity, self).onHurt(__float.valueOf(arg0), arg1))

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool.__wrap(super(Entity, self).isMarkedForRemoval()) 
 
 
# CLASS: dev.ultreon.quantum.entity.S2CEntityPipeline
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = __import_once__("pyquantum.network.client")

import dev.ultreon.quantum.entity.S2CEntityPipeline as __S2CEntityPipeline
__S2CEntityPipeline = __S2CEntityPipeline
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
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class S2CEntityPipeline():
    """dev.ultreon.quantum.entity.S2CEntityPipeline"""
 
    @staticmethod
    def __wrap(java_value: __S2CEntityPipeline) -> 'S2CEntityPipeline':
        return S2CEntityPipeline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __S2CEntityPipeline):
        """
        Dynamic initializer for S2CEntityPipeline.
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

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.entity.S2CEntityPipeline(dev.ultreon.quantum.network.PacketIO)"""
        val = __S2CEntityPipeline(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'MapType'):
        """public dev.ultreon.quantum.entity.S2CEntityPipeline(int,dev.ultreon.ubo.types.MapType)"""
        val = __S2CEntityPipeline(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.entity.S2CEntityPipeline.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(__S2CEntityPipeline, self).handle(arg0, arg1)

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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.entity.S2CEntityPipeline.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__S2CEntityPipeline, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.entity.EntityType$EntityFactory
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.entity.EntityType as __EntityType_EntityFactory
__EntityFactory = __EntityType_EntityFactory.EntityFactory
from abc import abstractmethod, ABC
 
class EntityFactory(ABC):
    """dev.ultreon.quantum.entity.EntityType.EntityFactory"""
 
    @staticmethod
    def __wrap(java_value: __EntityFactory) -> 'EntityFactory':
        return EntityFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityFactory):
        """
        Dynamic initializer for EntityFactory.
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
    def create(self, arg0: 'EntityType', arg1: 'World'):
        """public abstract T dev.ultreon.quantum.entity.EntityType$EntityFactory.create(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.world.World)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.entity.AttributeModifier
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.entity.AttributeModifier as __AttributeModifier
__AttributeModifier = __AttributeModifier
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.entity.AttributeModifier as __AttributeModifier_Operation
__Operation = __AttributeModifier_Operation.Operation
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class AttributeModifier():
    """dev.ultreon.quantum.entity.AttributeModifier"""
 
    @staticmethod
    def __wrap(java_value: __AttributeModifier) -> 'AttributeModifier':
        return AttributeModifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AttributeModifier):
        """
        Dynamic initializer for AttributeModifier.
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
        """public java.lang.String dev.ultreon.quantum.entity.AttributeModifier.toString()"""
        return str.__wrap(super(AttributeModifier, self).toString())

    @overload
    def __init__(self, arg0: 'UUID', arg1: 'Operation', arg2: float):
        """public dev.ultreon.quantum.entity.AttributeModifier(java.util.UUID,dev.ultreon.quantum.entity.AttributeModifier$Operation,double)"""
        val = __AttributeModifier(arg0, arg1, __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.AttributeModifier.hashCode()"""
        return int.__wrap(super(AttributeModifier, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def operation(self) -> 'Operation':
        """public dev.ultreon.quantum.entity.AttributeModifier$Operation dev.ultreon.quantum.entity.AttributeModifier.operation()"""
        return 'Operation'.__wrap(super(AttributeModifier, self).operation())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.AttributeModifier.equals(java.lang.Object)"""
        return bool.__wrap(super(__AttributeModifier, self).equals(arg0))

    @overload
    def value(self) -> float:
        """public double dev.ultreon.quantum.entity.AttributeModifier.value()"""
        return float.__wrap(super(AttributeModifier, self).value())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def id(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.AttributeModifier.id()"""
        return 'UUID'.__wrap(super(AttributeModifier, self).id()) 
 
 
# CLASS: dev.ultreon.quantum.entity.Pig
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import dev.ultreon.quantum.entity.AttributeMap as __AttributeMap
__AttributeMap = __AttributeMap
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import dev.ultreon.quantum.entity.Entity as __Entity_Pose
__Pose = __Entity_Pose.Pose
import java.lang.Double as __double
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

import dev.ultreon.quantum.world.SoundEvent as __SoundEvent
__SoundEvent = __SoundEvent
import dev.ultreon.quantum.entity.LivingEntity as __LivingEntity
__LivingEntity = __LivingEntity
from builtins import float
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

import java.lang.Object as __Object
__Object = __Object
from builtins import int
import dev.ultreon.quantum.world.rng.RNG as __RNG
__RNG = __RNG
try:
    from pyquantum.entity import util
except ImportError:
    util = __import_once__("pyquantum.entity.util")

import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
import java.lang.Boolean as __boolean
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = __import_once__("pyquantum.item.food")

import dev.ultreon.quantum.entity.EntityType as __EntityType
__EntityType = __EntityType
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import dev.ultreon.quantum.world.World as __World
__World = __World
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.entity.Pig as __Pig
__Pig = __Pig
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.entity.damagesource.DamageSource as __DamageSource
__DamageSource = __DamageSource
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
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

 
class Pig():
    """dev.ultreon.quantum.entity.Pig"""
 
    @staticmethod
    def __wrap(java_value: __Pig) -> 'Pig':
        return Pig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pig):
        """
        Dynamic initializer for Pig.
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
    def setMaxHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setMaxHealth(float)"""
        super(__LivingEntity, self).setMaxHealth(__float.valueOf(arg0))

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(__Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def getDeathSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getDeathSound()"""
        return 'world.SoundEvent'.__wrap(super(LivingEntity, self).getDeathSound())

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int.__wrap(super(Entity, self).getId())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'.__wrap(super(Entity, self).getUuid())

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float.__wrap(super(Entity, self).getYRot())

    @override
    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.LivingEntity.getAge()"""
        return int.__wrap(super(LivingEntity, self).getAge())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(__Entity, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def isDead(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isDead()"""
        return bool.__wrap(super(LivingEntity, self).isDead())

    @override
    @overload
    def hurt(self, arg0: float, arg1: 'DamageSource'):
        """public final void dev.ultreon.quantum.entity.LivingEntity.hurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).hurt(__float.valueOf(arg0), arg1)

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float.__wrap(super(Entity, self).getGravity())

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(__Entity, self).setY(__double.valueOf(arg0))

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float.__wrap(super(Entity, self).getXRot())

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(__LivingEntity, self).onPrepareSpawn(arg0)

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).rotate(arg0)

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'.__wrap(super(__Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(__Entity, self).setX(__double.valueOf(arg0))

    @override
    @overload
    def getLastDamageSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.LivingEntity.getLastDamageSource()"""
        return 'damagesource.DamageSource'.__wrap(super(LivingEntity, self).getLastDamageSource())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float.__wrap(super(__Entity, self).distanceTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'.__wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isWalking()"""
        return bool.__wrap(super(LivingEntity, self).isWalking())

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'.__wrap(super(Entity, self).getPipeline())

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float.__wrap(super(__Entity, self).distanceTo(arg0))

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(__Entity, self).teleportTo(arg0)

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(__Entity, self).sendMessage(arg0)

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).teleportTo(arg0)

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(__Entity, self).setYRot(__float.valueOf(arg0))

    @override
    @overload
    def moveTowards(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.moveTowards(double,double,double,double)"""
        super(__LivingEntity, self).moveTowards(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getPose(self) -> 'Pose':
        """public dev.ultreon.quantum.entity.Entity$Pose dev.ultreon.quantum.entity.Pig.getPose()"""
        return 'Pose'.__wrap(super(Pig, self).getPose())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.LivingEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__LivingEntity, self).save(arg0))

    @override
    @overload
    def getMaxHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.Pig.getMaxHealth()"""
        return float.__wrap(super(Pig, self).getMaxHealth())

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(__LivingEntity, self).load(arg0)

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setPosition(arg0)

    @override
    @overload
    def jump(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.jump()"""
        super(LivingEntity, self).jump()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str.__wrap(super(Entity, self).getName())

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(__Entity, self).setUuid(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isInvincible()"""
        return bool.__wrap(super(LivingEntity, self).isInvincible())

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool.__wrap(super(Entity, self).isInWater())

    @override
    @overload
    def getHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getHealth()"""
        return float.__wrap(super(LivingEntity, self).getHealth())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(__Entity, self).setPosition(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str.__wrap(super(Entity, self).getPublicName())

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.Pig(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.Pig>,dev.ultreon.quantum.world.World)"""
        val = __Pig(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onDropItems(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDropItems(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).onDropItems(arg0)

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool.__wrap(super(Entity, self).isInVoid())

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(__Entity, self).sendMessage(arg0)

    @override
    @overload
    def getSpeed(self) -> float:
        """public double dev.ultreon.quantum.entity.LivingEntity.getSpeed()"""
        return float.__wrap(super(LivingEntity, self).getSpeed())

    @override
    @overload
    def setInvincible(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.LivingEntity.setInvincible(boolean)"""
        super(__LivingEntity, self).setInvincible(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAnimation(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Pig.getAnimation()"""
        return str.__wrap(super(Pig, self).getAnimation())

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).onPipeline(arg0)

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'.__wrap(super(Entity, self).getSize())

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__commands.CommandSender, self).hasPermission(arg0))

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0))

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'.__wrap(super(Entity, self).getWorld())

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(__Entity, self).setZ(__double.valueOf(arg0))

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(__Entity, self).teleportTo(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(__Entity, self).setGravity(__float.valueOf(arg0))

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity.__wrap(__Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.entity.LivingEntity.getChunkPos()"""
        return 'world.ChunkPos'.__wrap(super(LivingEntity, self).getChunkPos())

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float.__wrap(super(Entity, self).getZ())

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(Entity, self).getDisplayName())

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__Entity, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float.__wrap(super(Entity, self).getX())

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float.__wrap(super(Entity, self).getY())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'.__wrap(super(Entity, self).getLocation())

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool.__wrap(super(__Entity, self).move(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(__Entity, self).loadWithPos(arg0)

    @override
    @overload
    def onDeath(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDeath(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(__LivingEntity, self).onDeath(arg0)

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'.__wrap(super(Entity, self).getBlockPos())

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(__Entity, self).teleportTo(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.tick()"""
        super(LivingEntity, self).tick()

    @override
    @overload
    def setHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setHealth(float)"""
        super(__LivingEntity, self).setHealth(__float.valueOf(arg0))

    @override
    @overload
    def applyEffect(self, arg0: 'AppliedEffect'):
        """public void dev.ultreon.quantum.entity.LivingEntity.applyEffect(dev.ultreon.quantum.item.food.AppliedEffect)"""
        super(__LivingEntity, self).applyEffect(arg0)

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(__Entity, self).setXRot(__float.valueOf(arg0))

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool.__wrap(super(Entity, self).isAdmin())

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(__Entity, self).setId(__int.valueOf(arg0))

    @override
    @overload
    def getHurtSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.Pig.getHurtSound()"""
        return 'world.SoundEvent'.__wrap(super(Pig, self).getHurtSound())

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__Entity, self).setRotation(arg0)

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'.__wrap(super(Entity, self).getRotation())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'.__wrap(super(Entity, self).getPosition())

    @override
    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'.__wrap(super(Entity, self).getType())

    @override
    @overload
    def getJumpVel(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getJumpVel()"""
        return float.__wrap(super(LivingEntity, self).getJumpVel())

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool.__wrap(super(Entity, self).isAffectedByFluid())

    @override
    @overload
    def createAiGoals(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.createAiGoals()"""
        super(LivingEntity, self).createAiGoals()

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.LivingEntity.getLookVector()"""
        return 'vector.Vec3d'.__wrap(super(LivingEntity, self).getLookVector())

    @override
    @overload
    def kill(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.kill()"""
        super(LivingEntity, self).kill()

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__Entity, self).setVelocity(arg0)

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'.__wrap(super(Entity, self).getRng())

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox.__wrap(__Entity.getBoundingBox(arg0, arg1))

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'.__wrap(super(Entity, self).getBoundingBox())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setJumpVel(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setJumpVel(float)"""
        super(__LivingEntity, self).setJumpVel(__float.valueOf(arg0))

    @overload
    def onHurt(self, arg0: float, arg1: 'DamageSource') -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.onHurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        return bool.__wrap(super(__LivingEntity, self).onHurt(__float.valueOf(arg0), arg1))

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool.__wrap(super(Entity, self).isMarkedForRemoval())