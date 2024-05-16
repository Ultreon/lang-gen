from __future__ import annotations
from overload import overload


 
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.AttributeModifier as _AttributeModifier
_AttributeModifier = _AttributeModifier
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import dev.ultreon.quantum.entity.AttributeMap as _AttributeMap
_AttributeMap = _AttributeMap
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AttributeMap():
    """dev.ultreon.quantum.entity.AttributeMap"""
 
    @staticmethod
    def _wrap(java_value: _AttributeMap) -> 'AttributeMap':
        return AttributeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AttributeMap):
        """
        Dynamic initializer for AttributeMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AttributeMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AttributeMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: 'Attribute') -> float:
        """public double dev.ultreon.quantum.entity.AttributeMap.get(dev.ultreon.quantum.entity.Attribute)"""
        return float._wrap(super(_AttributeMap, self).get(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.AttributeMap()"""
        val = _AttributeMap()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def addModifier(self, arg0: 'Attribute', arg1: 'AttributeModifier'):
        """public void dev.ultreon.quantum.entity.AttributeMap.addModifier(dev.ultreon.quantum.entity.Attribute,dev.ultreon.quantum.entity.AttributeModifier)"""
        super(_AttributeMap, self).addModifier(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getBase(self, arg0: 'Attribute') -> float:
        """public double dev.ultreon.quantum.entity.AttributeMap.getBase(dev.ultreon.quantum.entity.Attribute)"""
        return float._wrap(super(_AttributeMap, self).getBase(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.AttributeMap()"""
        val = _AttributeMap()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def removeModifier(self, arg0: 'Attribute', arg1: 'UUID') -> 'AttributeModifier':
        """public dev.ultreon.quantum.entity.AttributeModifier dev.ultreon.quantum.entity.AttributeMap.removeModifier(dev.ultreon.quantum.entity.Attribute,java.util.UUID)"""
        return 'AttributeModifier'._wrap(super(_AttributeMap, self).removeModifier(arg0, arg1))

    @overload
    def setBase(self, arg0: 'Attribute', arg1: float):
        """public void dev.ultreon.quantum.entity.AttributeMap.setBase(dev.ultreon.quantum.entity.Attribute,double)"""
        super(_AttributeMap, self).setBase(arg0, _double.valueOf(arg1))

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

 
 
 
# CLASS: dev.ultreon.quantum.entity.AttributeMap
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.AttributeModifier as _AttributeModifier
_AttributeModifier = _AttributeModifier
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import dev.ultreon.quantum.entity.AttributeMap as _AttributeMap
_AttributeMap = _AttributeMap
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AttributeMap():
    """dev.ultreon.quantum.entity.AttributeMap"""
 
    @staticmethod
    def _wrap(java_value: _AttributeMap) -> 'AttributeMap':
        return AttributeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AttributeMap):
        """
        Dynamic initializer for AttributeMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AttributeMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AttributeMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: 'Attribute') -> float:
        """public double dev.ultreon.quantum.entity.AttributeMap.get(dev.ultreon.quantum.entity.Attribute)"""
        return float._wrap(super(_AttributeMap, self).get(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.AttributeMap()"""
        val = _AttributeMap()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def addModifier(self, arg0: 'Attribute', arg1: 'AttributeModifier'):
        """public void dev.ultreon.quantum.entity.AttributeMap.addModifier(dev.ultreon.quantum.entity.Attribute,dev.ultreon.quantum.entity.AttributeModifier)"""
        super(_AttributeMap, self).addModifier(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getBase(self, arg0: 'Attribute') -> float:
        """public double dev.ultreon.quantum.entity.AttributeMap.getBase(dev.ultreon.quantum.entity.Attribute)"""
        return float._wrap(super(_AttributeMap, self).getBase(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.AttributeMap()"""
        val = _AttributeMap()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def removeModifier(self, arg0: 'Attribute', arg1: 'UUID') -> 'AttributeModifier':
        """public dev.ultreon.quantum.entity.AttributeModifier dev.ultreon.quantum.entity.AttributeMap.removeModifier(dev.ultreon.quantum.entity.Attribute,java.util.UUID)"""
        return 'AttributeModifier'._wrap(super(_AttributeMap, self).removeModifier(arg0, arg1))

    @overload
    def setBase(self, arg0: 'Attribute', arg1: float):
        """public void dev.ultreon.quantum.entity.AttributeMap.setBase(dev.ultreon.quantum.entity.Attribute,double)"""
        super(_AttributeMap, self).setBase(arg0, _double.valueOf(arg1))

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

 
 
 
# CLASS: dev.ultreon.quantum.entity.AttributeMap 
 
 
# CLASS: dev.ultreon.quantum.entity.AttributeModifier$Operation
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.entity.AttributeModifier as _AttributeModifier_Operation
_Operation = _AttributeModifier_Operation.Operation
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Operation():
    """dev.ultreon.quantum.entity.AttributeModifier.Operation"""
 
    @staticmethod
    def _wrap(java_value: _Operation) -> 'Operation':
        return Operation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Operation):
        """
        Dynamic initializer for Operation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Operation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Operation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['Operation']:
        """public static dev.ultreon.quantum.entity.AttributeModifier$Operation[] dev.ultreon.quantum.entity.AttributeModifier$Operation.values()"""
        return List[Operation]._wrap(_Operation.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Operation':
        """public static dev.ultreon.quantum.entity.AttributeModifier$Operation dev.ultreon.quantum.entity.AttributeModifier$Operation.valueOf(java.lang.String)"""
        return Operation._wrap(_Operation.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def calculate(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.entity.AttributeModifier$Operation.calculate(double,double)"""
        return float._wrap(super(_Operation, self).calculate(_double.valueOf(arg0), _double.valueOf(arg1)))


Operation.MULTIPLY = Operation._wrap(_MULTIPLY.MULTIPLY)

Operation.PLUS = Operation._wrap(_PLUS.PLUS) 
 
 
# CLASS: dev.ultreon.quantum.entity.DroppedItem
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.entity import util
except ImportError:
    util = _import_once("pyquantum.entity.util")

import java.util.UUID as UUID
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.entity.DroppedItem as _DroppedItem
_DroppedItem = _DroppedItem
import dev.ultreon.quantum.entity.EntityType as _EntityType
_EntityType = _EntityType
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import java.lang.Boolean as _boolean
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.entity.AttributeMap as _AttributeMap
_AttributeMap = _AttributeMap
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
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.rng.RNG as _RNG
_RNG = _RNG
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class DroppedItem():
    """dev.ultreon.quantum.entity.DroppedItem"""
 
    @staticmethod
    def _wrap(java_value: _DroppedItem) -> 'DroppedItem':
        return DroppedItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DroppedItem):
        """
        Dynamic initializer for DroppedItem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DroppedItem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DroppedItem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getLookVector()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getLookVector())

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(_Entity, self).setGravity(_float.valueOf(arg0))

    @override
    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'._wrap(super(Entity, self).getType())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'._wrap(super(Entity, self).getLocation())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'._wrap(super(Entity, self).getWorld())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(_Entity, self).setY(_double.valueOf(arg0))

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(_Entity, self).setUuid(arg0)

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'._wrap(super(_Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(_Entity, self).teleportTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'._wrap(super(Entity, self).getPipeline())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'._wrap(super(Entity, self).getBlockPos())

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str._wrap(super(Entity, self).getPublicName())

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(_Entity, self).teleportTo(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'._wrap(super(Entity, self).getUuid())

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float._wrap(super(Entity, self).getXRot())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(_Entity, self).sendMessage(arg0)

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0))

    @overload
    def getPickupDelay(self) -> int:
        """public int dev.ultreon.quantum.entity.DroppedItem.getPickupDelay()"""
        return int._wrap(super(DroppedItem, self).getPickupDelay())

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(_Entity, self).setX(_double.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'World', arg1: 'ItemStack', arg2: 'Vec3d', arg3: 'Vec3d'):
        """public dev.ultreon.quantum.entity.DroppedItem(dev.ultreon.quantum.world.World,dev.ultreon.quantum.item.ItemStack,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _DroppedItem(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).rotate(arg0)

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'._wrap(super(Entity, self).getSize())

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.DroppedItem.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(_DroppedItem, self).onPipeline(arg0)

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.DroppedItem.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(_DroppedItem, self).onPrepareSpawn(arg0)

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.DroppedItem.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_DroppedItem, self).save(arg0))

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'._wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'._wrap(super(Entity, self).getBoundingBox())

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setVelocity(arg0)

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float._wrap(super(_Entity, self).distanceTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int._wrap(super(Entity, self).getId())

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.DroppedItem.tick()"""
        super(DroppedItem, self).tick()

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.DroppedItem(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.Entity>,dev.ultreon.quantum.world.World)"""
        val = _DroppedItem(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool._wrap(super(Entity, self).isInVoid())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float._wrap(super(Entity, self).getX())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool._wrap(super(Entity, self).isAdmin())

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_Entity, self).hasExplicitPermission(arg0))

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str._wrap(super(Entity, self).getName())

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float._wrap(super(Entity, self).getY())

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'._wrap(super(Entity, self).getRng())

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).setRotation(arg0)

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float._wrap(super(Entity, self).getZ())

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(_Entity, self).setYRot(_float.valueOf(arg0))

    @overload
    def getStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.entity.DroppedItem.getStack()"""
        return 'item.ItemStack'._wrap(super(DroppedItem, self).getStack())

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float._wrap(super(Entity, self).getYRot())

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'._wrap(super(Entity, self).getRotation())

    @overload
    def setStack(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.entity.DroppedItem.setStack(dev.ultreon.quantum.item.ItemStack)"""
        super(_DroppedItem, self).setStack(arg0)

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(_Entity, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float._wrap(super(Entity, self).getGravity())

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(_Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'._wrap(super(Entity, self).getDisplayName())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(_Entity, self).setPosition(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(_Entity, self).setXRot(_float.valueOf(arg0))

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool._wrap(super(_Entity, self).move(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(_Entity, self).setId(_int.valueOf(arg0))

    @overload
    def setPickupDelay(self, arg0: int):
        """public void dev.ultreon.quantum.entity.DroppedItem.setPickupDelay(int)"""
        super(_DroppedItem, self).setPickupDelay(_int.valueOf(arg0))

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(_Entity, self).sendMessage(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.DroppedItem.getAge()"""
        return int._wrap(super(DroppedItem, self).getAge())

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity._wrap(_Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool._wrap(super(Entity, self).isInWater())

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setPosition(arg0)

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getPosition())

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.DroppedItem.load(dev.ultreon.ubo.types.MapType)"""
        super(_DroppedItem, self).load(arg0)

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(_Entity, self).setZ(_double.valueOf(arg0))

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox._wrap(_Entity.getBoundingBox(arg0, arg1))

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).loadWithPos(arg0)

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float._wrap(super(_Entity, self).distanceTo(arg0))

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool._wrap(super(Entity, self).isAffectedByFluid())

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool._wrap(super(Entity, self).isMarkedForRemoval())

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0, _boolean.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.quantum.entity.Animal
import dev.ultreon.quantum.entity.Animal as _Animal
_Animal = _Animal
 
class Animal():
    """dev.ultreon.quantum.entity.Animal"""
 
    @staticmethod
    def _wrap(java_value: _Animal) -> 'Animal':
        return Animal(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Animal):
        """
        Dynamic initializer for Animal.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Animal__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Animal__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: dev.ultreon.quantum.entity.EntityType
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.entity import util
except ImportError:
    util = _import_once("pyquantum.entity.util")

try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.entity.EntityType as _EntityType
_EntityType = _EntityType
import dev.ultreon.quantum.entity.util.EntitySize as _EntitySize
_EntitySize = _EntitySize
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityType():
    """dev.ultreon.quantum.entity.EntityType"""
 
    @staticmethod
    def _wrap(java_value: _EntityType) -> 'EntityType':
        return EntityType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityType):
        """
        Dynamic initializer for EntityType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.entity.EntityType.getId()"""
        return 'util.Identifier'._wrap(super(EntityType, self).getId())

    @overload
    def spawn(self, arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public T dev.ultreon.quantum.entity.EntityType.spawn(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return 'Entity'._wrap(super(_EntityType, self).spawn(arg0, arg1))

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
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.EntityType.getSize()"""
        return 'util.EntitySize'._wrap(super(EntityType, self).getSize())

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
    def spawn(self, arg0: 'World') -> 'Entity':
        """public T dev.ultreon.quantum.entity.EntityType.spawn(dev.ultreon.quantum.world.World)"""
        return 'Entity'._wrap(super(_EntityType, self).spawn(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.entity.Entity$Pose
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.entity.Entity as _Entity_Pose
_Pose = _Entity_Pose.Pose
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pose():
    """dev.ultreon.quantum.entity.Entity.Pose"""
 
    @staticmethod
    def _wrap(java_value: _Pose) -> 'Pose':
        return Pose(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pose):
        """
        Dynamic initializer for Pose.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pose__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pose__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['Pose']:
        """public static dev.ultreon.quantum.entity.Entity$Pose[] dev.ultreon.quantum.entity.Entity$Pose.values()"""
        return List[Pose]._wrap(_Pose.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Pose':
        """public static dev.ultreon.quantum.entity.Entity$Pose dev.ultreon.quantum.entity.Entity$Pose.valueOf(java.lang.String)"""
        return Pose._wrap(_Pose.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Pose.IDLE = Pose._wrap(_IDLE.IDLE)

Pose.WALKING = Pose._wrap(_WALKING.WALKING) 
 
 
# CLASS: dev.ultreon.quantum.entity.LivingEntity
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.entity import util
except ImportError:
    util = _import_once("pyquantum.entity.util")

import java.util.UUID as UUID
import java.lang.Double as _double
import dev.ultreon.quantum.entity.damagesource.DamageSource as _DamageSource
_DamageSource = _DamageSource
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = _import_once("pyquantum.item.food")

import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
import dev.ultreon.quantum.entity.LivingEntity as _LivingEntity
_LivingEntity = _LivingEntity
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.entity.EntityType as _EntityType
_EntityType = _EntityType
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
from builtins import float
import dev.ultreon.quantum.entity.AttributeMap as _AttributeMap
_AttributeMap = _AttributeMap
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
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import dev.ultreon.quantum.world.SoundEvent as _SoundEvent
_SoundEvent = _SoundEvent
import java.lang.Integer as _int
try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = _import_once("pyquantum.entity.damagesource")

import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.rng.RNG as _RNG
_RNG = _RNG
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class LivingEntity():
    """dev.ultreon.quantum.entity.LivingEntity"""
 
    @staticmethod
    def _wrap(java_value: _LivingEntity) -> 'LivingEntity':
        return LivingEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LivingEntity):
        """
        Dynamic initializer for LivingEntity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LivingEntity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LivingEntity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(_Entity, self).setGravity(_float.valueOf(arg0))

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'._wrap(super(Entity, self).getLocation())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMaxHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getMaxHealth()"""
        return float._wrap(super(LivingEntity, self).getMaxHealth())

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(_Entity, self).setY(_double.valueOf(arg0))

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'._wrap(super(_Entity, self).getBoundingBox(arg0))

    @overload
    def setMaxHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setMaxHealth(float)"""
        super(_LivingEntity, self).setMaxHealth(_float.valueOf(arg0))

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(_Entity, self).teleportTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'._wrap(super(Entity, self).getPipeline())

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'._wrap(super(Entity, self).getBlockPos())

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(_Entity, self).teleportTo(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.LivingEntity.getAge()"""
        return int._wrap(super(LivingEntity, self).getAge())

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'._wrap(super(Entity, self).getUuid())

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float._wrap(super(Entity, self).getXRot())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(_Entity, self).sendMessage(arg0)

    @overload
    def getJumpVel(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getJumpVel()"""
        return float._wrap(super(LivingEntity, self).getJumpVel())

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).rotate(arg0)

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'._wrap(super(Entity, self).getSize())

    @overload
    def applyEffect(self, arg0: 'AppliedEffect'):
        """public void dev.ultreon.quantum.entity.LivingEntity.applyEffect(dev.ultreon.quantum.item.food.AppliedEffect)"""
        super(_LivingEntity, self).applyEffect(arg0)

    @overload
    def getLastDamageSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.LivingEntity.getLastDamageSource()"""
        return 'damagesource.DamageSource'._wrap(super(LivingEntity, self).getLastDamageSource())

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'._wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setVelocity(arg0)

    @overload
    def onDropItems(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDropItems(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).onDropItems(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def moveTowards(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.moveTowards(double,double,double,double)"""
        super(_LivingEntity, self).moveTowards(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float._wrap(super(Entity, self).getX())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool._wrap(super(Entity, self).isAdmin())

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float._wrap(super(Entity, self).getY())

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'._wrap(super(Entity, self).getRng())

    @overload
    def jump(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.jump()"""
        super(LivingEntity, self).jump()

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).setRotation(arg0)

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float._wrap(super(Entity, self).getZ())

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(_Entity, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float._wrap(super(Entity, self).getGravity())

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool._wrap(super(_Entity, self).move(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(_Entity, self).setId(_int.valueOf(arg0))

    @overload
    def getChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.entity.LivingEntity.getChunkPos()"""
        return 'world.ChunkPos'._wrap(super(LivingEntity, self).getChunkPos())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getHealth()"""
        return float._wrap(super(LivingEntity, self).getHealth())

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.LivingEntity(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.LivingEntity>,dev.ultreon.quantum.world.World)"""
        val = _LivingEntity(arg0, arg1)
        self.__wrapper = val

    @overload
    def hurt(self, arg0: float, arg1: 'DamageSource'):
        """public final void dev.ultreon.quantum.entity.LivingEntity.hurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).hurt(_float.valueOf(arg0), arg1)

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool._wrap(super(Entity, self).isInWater())

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setPosition(arg0)

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).onPipeline(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onDeath(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDeath(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).onDeath(arg0)

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox._wrap(_Entity.getBoundingBox(arg0, arg1))

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float._wrap(super(_Entity, self).distanceTo(arg0))

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool._wrap(super(Entity, self).isAffectedByFluid())

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool._wrap(super(Entity, self).isMarkedForRemoval())

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @override
    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'._wrap(super(Entity, self).getType())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'._wrap(super(Entity, self).getWorld())

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(_Entity, self).setUuid(arg0)

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(_LivingEntity, self).onPrepareSpawn(arg0)

    @overload
    def onHurt(self, arg0: float, arg1: 'DamageSource') -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.onHurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        return bool._wrap(super(_LivingEntity, self).onHurt(_float.valueOf(arg0), arg1))

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
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str._wrap(super(Entity, self).getPublicName())

    @overload
    def getDeathSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getDeathSound()"""
        return 'world.SoundEvent'._wrap(super(LivingEntity, self).getDeathSound())

    @overload
    def createAiGoals(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.createAiGoals()"""
        super(LivingEntity, self).createAiGoals()

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0))

    @overload
    def setJumpVel(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setJumpVel(float)"""
        super(_LivingEntity, self).setJumpVel(_float.valueOf(arg0))

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(_Entity, self).setX(_double.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'._wrap(super(Entity, self).getBoundingBox())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.LivingEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_LivingEntity, self).save(arg0))

    @overload
    def isDead(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isDead()"""
        return bool._wrap(super(LivingEntity, self).isDead())

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float._wrap(super(_Entity, self).distanceTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int._wrap(super(Entity, self).getId())

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool._wrap(super(Entity, self).isInVoid())

    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isInvincible()"""
        return bool._wrap(super(LivingEntity, self).isInvincible())

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasExplicitPermission(arg0))

    @overload
    def kill(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.kill()"""
        super(LivingEntity, self).kill()

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_Entity, self).hasExplicitPermission(arg0))

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str._wrap(super(Entity, self).getName())

    @overload
    def getSpeed(self) -> float:
        """public double dev.ultreon.quantum.entity.LivingEntity.getSpeed()"""
        return float._wrap(super(LivingEntity, self).getSpeed())

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(_Entity, self).setYRot(_float.valueOf(arg0))

    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isWalking()"""
        return bool._wrap(super(LivingEntity, self).isWalking())

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float._wrap(super(Entity, self).getYRot())

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'._wrap(super(Entity, self).getRotation())

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.LivingEntity.getLookVector()"""
        return 'vector.Vec3d'._wrap(super(LivingEntity, self).getLookVector())

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.tick()"""
        super(LivingEntity, self).tick()

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(_Entity, self).teleportDimension(arg0, arg1)

    @overload
    def setInvincible(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.LivingEntity.setInvincible(boolean)"""
        super(_LivingEntity, self).setInvincible(_boolean.valueOf(arg0))

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'._wrap(super(Entity, self).getDisplayName())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(_Entity, self).setPosition(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(_Entity, self).setXRot(_float.valueOf(arg0))

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(_Entity, self).sendMessage(arg0)

    @overload
    def getHurtSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getHurtSound()"""
        return 'world.SoundEvent'._wrap(super(LivingEntity, self).getHurtSound())

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity._wrap(_Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(_LivingEntity, self).load(arg0)

    @overload
    def setHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setHealth(float)"""
        super(_LivingEntity, self).setHealth(_float.valueOf(arg0))

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getPosition())

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(_Entity, self).setZ(_double.valueOf(arg0))

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).loadWithPos(arg0) 
 
 
# CLASS: dev.ultreon.quantum.entity.EntityTypes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.entity.EntityTypes as _EntityTypes
_EntityTypes = _EntityTypes
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityTypes():
    """dev.ultreon.quantum.entity.EntityTypes"""
 
    @staticmethod
    def _wrap(java_value: _EntityTypes) -> 'EntityTypes':
        return EntityTypes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityTypes):
        """
        Dynamic initializer for EntityTypes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityTypes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityTypes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.entity.EntityType<dev.ultreon.quantum.entity.player.Player> dev.ultreon.quantum.entity.EntityTypes.PLAYER
    PLAYER: 'EntityType' = _wrap(_EntityType.PLAYER)

    # public static final dev.ultreon.quantum.entity.EntityType<dev.ultreon.quantum.entity.Something> dev.ultreon.quantum.entity.EntityTypes.SOMETHING
    SOMETHING: 'EntityType' = _wrap(_EntityType.SOMETHING)

    # public static final dev.ultreon.quantum.entity.EntityType<dev.ultreon.quantum.entity.DroppedItem> dev.ultreon.quantum.entity.EntityTypes.DROPPED_ITEM
    DROPPED_ITEM: 'EntityType' = _wrap(_EntityType.DROPPED_ITEM)

    # public static final dev.ultreon.quantum.entity.EntityType<dev.ultreon.quantum.entity.Pig> dev.ultreon.quantum.entity.EntityTypes.PIG
    PIG: 'EntityType' = _wrap(_EntityType.PIG)


    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.EntityTypes()"""
        val = _EntityTypes()
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.entity.EntityTypes.init()"""
            _EntityTypes.init()

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.EntityTypes()"""
        val = _EntityTypes()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.entity.EntityType$Builder
import dev.ultreon.quantum.entity.EntityType as _EntityType_Builder
_Builder = _EntityType_Builder.Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.entity.EntityType as _EntityType
_EntityType = _EntityType
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.entity.EntityType.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.entity.EntityType$Builder()"""
        val = _Builder()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def factory(self, arg0: 'EntityFactory') -> 'Builder':
        """public dev.ultreon.quantum.entity.EntityType$Builder<T> dev.ultreon.quantum.entity.EntityType$Builder.factory(dev.ultreon.quantum.entity.EntityType$EntityFactory<T>)"""
        return 'Builder'._wrap(super(_Builder, self).factory(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def build(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<T> dev.ultreon.quantum.entity.EntityType$Builder.build()"""
        return 'EntityType'._wrap(super(Builder, self).build())

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
    def size(self, arg0: float, arg1: float) -> 'Builder':
        """public dev.ultreon.quantum.entity.EntityType$Builder<T> dev.ultreon.quantum.entity.EntityType$Builder.size(float,float)"""
        return 'Builder'._wrap(super(_Builder, self).size(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.entity.EntityType$Builder()"""
        val = _Builder()
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
 
 
# CLASS: dev.ultreon.quantum.entity.Entity
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.entity import util
except ImportError:
    util = _import_once("pyquantum.entity.util")

import java.util.UUID as UUID
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.entity.EntityType as _EntityType
_EntityType = _EntityType
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import java.lang.Boolean as _boolean
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
from builtins import float
import dev.ultreon.quantum.entity.AttributeMap as _AttributeMap
_AttributeMap = _AttributeMap
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
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.rng.RNG as _RNG
_RNG = _RNG
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class Entity():
    """dev.ultreon.quantum.entity.Entity"""
 
    @staticmethod
    def _wrap(java_value: _Entity) -> 'Entity':
        return Entity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Entity):
        """
        Dynamic initializer for Entity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Entity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Entity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(_Entity, self).setGravity(_float.valueOf(arg0))

    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'._wrap(super(Entity, self).getSize())

    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'._wrap(super(Entity, self).getLocation())

    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).rotate(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(_Entity, self).teleportTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getPosition())

    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool._wrap(super(Entity, self).isAffectedByFluid())

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'._wrap(super(_Entity, self).getBoundingBox(arg0))

    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(_Entity, self).setYRot(_float.valueOf(arg0))

    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(_Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_Entity, self).save(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str._wrap(super(Entity, self).getPublicName())

    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(_Entity, self).setUuid(arg0)

    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'._wrap(super(Entity, self).getUuid())

    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).onPipeline(arg0)

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(_Entity, self).sendMessage(arg0)

    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float._wrap(super(Entity, self).getGravity())

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0))

    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool._wrap(super(Entity, self).isInWater())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(_Entity, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'._wrap(super(Entity, self).getWorld())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setVelocity(arg0)

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(_Entity, self).setZ(_double.valueOf(arg0))

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float._wrap(super(_Entity, self).distanceTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).setRotation(arg0)

    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).onPrepareSpawn(arg0)

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
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'._wrap(super(Entity, self).getRng())

    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(_Entity, self).setXRot(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool._wrap(super(Entity, self).isAdmin())

    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'._wrap(super(Entity, self).getType())

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_Entity, self).hasExplicitPermission(arg0))

    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).loadWithPos(arg0)

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str._wrap(super(Entity, self).getName())

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(_Entity, self).setY(_double.valueOf(arg0))

    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'._wrap(super(Entity, self).getBoundingBox())

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.Entity(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.Entity>,dev.ultreon.quantum.world.World)"""
        val = _Entity(arg0, arg1)
        self.__wrapper = val

    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool._wrap(super(Entity, self).isInVoid())

    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.load(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).load(arg0)

    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getVelocity())

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float._wrap(super(Entity, self).getX())

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(_Entity, self).setPosition(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'._wrap(super(Entity, self).getRotation())

    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float._wrap(super(Entity, self).getY())

    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(_Entity, self).teleportTo(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.Entity.tick()"""
        super(Entity, self).tick()

    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getLookVector()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getLookVector())

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(_Entity, self).setX(_double.valueOf(arg0))

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'._wrap(super(Entity, self).getDisplayName())

    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(_Entity, self).setId(_int.valueOf(arg0))

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'._wrap(super(Entity, self).getAttributes())

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool._wrap(super(_Entity, self).move(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float._wrap(super(Entity, self).getYRot())

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(_Entity, self).sendMessage(arg0)

    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float._wrap(super(Entity, self).getZ())

    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool._wrap(super(Entity, self).isMarkedForRemoval())

    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int._wrap(super(Entity, self).getId())

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity._wrap(_Entity.loadFrom(arg0, arg1))

    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float._wrap(super(Entity, self).getXRot())

    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'._wrap(super(Entity, self).getBlockPos())

    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setPosition(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox._wrap(_Entity.getBoundingBox(arg0, arg1))

    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'._wrap(super(Entity, self).getPipeline())

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float._wrap(super(_Entity, self).distanceTo(arg0))

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0, _boolean.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.quantum.entity.Attribute
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import dev.ultreon.quantum.entity.Attribute as _Attribute
_Attribute = _Attribute
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Attribute():
    """dev.ultreon.quantum.entity.Attribute"""
 
    @staticmethod
    def _wrap(java_value: _Attribute) -> 'Attribute':
        return Attribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Attribute):
        """
        Dynamic initializer for Attribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Attribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Attribute__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Attribute.toString()"""
        return str._wrap(super(Attribute, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_Attribute, self).equals(arg0))

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

    @overload
    def key(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Attribute.key()"""
        return str._wrap(super(Attribute, self).key())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.Attribute.hashCode()"""
        return int._wrap(super(Attribute, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.entity.Attribute(java.lang.String)"""
        val = _Attribute(arg0)
        self.__wrapper = val


Attribute.SPEED = Attribute._wrap(_SPEED.SPEED)

Attribute.BLOCK_REACH = Attribute._wrap(_BLOCK_REACH.BLOCK_REACH)

Attribute.ENTITY_REACH = Attribute._wrap(_ENTITY_REACH.ENTITY_REACH) 
 
 
# CLASS: dev.ultreon.quantum.entity.Something
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.damagesource.DamageSource as _DamageSource
_DamageSource = _DamageSource
import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

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
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
try:
    from pyquantum.entity import util
except ImportError:
    util = _import_once("pyquantum.entity.util")

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
import dev.ultreon.quantum.entity.EntityType as _EntityType
_EntityType = _EntityType
import dev.ultreon.quantum.entity.Something as _Something
_Something = _Something
import java.lang.String as _string
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.entity.AttributeMap as _AttributeMap
_AttributeMap = _AttributeMap
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
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class Something():
    """dev.ultreon.quantum.entity.Something"""
 
    @staticmethod
    def _wrap(java_value: _Something) -> 'Something':
        return Something(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Something):
        """
        Dynamic initializer for Something.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Something__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Something__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(_Entity, self).setGravity(_float.valueOf(arg0))

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'._wrap(super(Entity, self).getLocation())

    @override
    @overload
    def setMaxHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setMaxHealth(float)"""
        super(_LivingEntity, self).setMaxHealth(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.LivingEntity.getAge()"""
        return int._wrap(super(LivingEntity, self).getAge())

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(_Entity, self).setY(_double.valueOf(arg0))

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'._wrap(super(_Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(_Entity, self).teleportTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def getHurtSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.Something.getHurtSound()"""
        return 'world.SoundEvent'._wrap(super(Something, self).getHurtSound())

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'._wrap(super(Entity, self).getPipeline())

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'._wrap(super(Entity, self).getBlockPos())

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(_Entity, self).teleportTo(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'._wrap(super(Entity, self).getUuid())

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float._wrap(super(Entity, self).getXRot())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(_Entity, self).sendMessage(arg0)

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.Something(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.Something>,dev.ultreon.quantum.world.World)"""
        val = _Something(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def applyEffect(self, arg0: 'AppliedEffect'):
        """public void dev.ultreon.quantum.entity.LivingEntity.applyEffect(dev.ultreon.quantum.item.food.AppliedEffect)"""
        super(_LivingEntity, self).applyEffect(arg0)

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).rotate(arg0)

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'._wrap(super(Entity, self).getSize())

    @override
    @overload
    def onDropItems(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDropItems(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).onDropItems(arg0)

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'._wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setVelocity(arg0)

    @override
    @overload
    def hurt(self, arg0: float, arg1: 'DamageSource'):
        """public final void dev.ultreon.quantum.entity.LivingEntity.hurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).hurt(_float.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float._wrap(super(Entity, self).getX())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool._wrap(super(Entity, self).isAdmin())

    @override
    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isInvincible()"""
        return bool._wrap(super(LivingEntity, self).isInvincible())

    @override
    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isWalking()"""
        return bool._wrap(super(LivingEntity, self).isWalking())

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float._wrap(super(Entity, self).getY())

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'._wrap(super(Entity, self).getRng())

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).setRotation(arg0)

    @override
    @overload
    def moveTowards(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.moveTowards(double,double,double,double)"""
        super(_LivingEntity, self).moveTowards(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float._wrap(super(Entity, self).getZ())

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(_Entity, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float._wrap(super(Entity, self).getGravity())

    @override
    @overload
    def setInvincible(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.LivingEntity.setInvincible(boolean)"""
        super(_LivingEntity, self).setInvincible(_boolean.valueOf(arg0))

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool._wrap(super(_Entity, self).move(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(_Entity, self).setId(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def jump(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.jump()"""
        super(LivingEntity, self).jump()

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool._wrap(super(Entity, self).isInWater())

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setPosition(arg0)

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).onPipeline(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox._wrap(_Entity.getBoundingBox(arg0, arg1))

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float._wrap(super(_Entity, self).distanceTo(arg0))

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool._wrap(super(Entity, self).isAffectedByFluid())

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool._wrap(super(Entity, self).isMarkedForRemoval())

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @override
    @overload
    def getDeathSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getDeathSound()"""
        return 'world.SoundEvent'._wrap(super(LivingEntity, self).getDeathSound())

    @override
    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'._wrap(super(Entity, self).getType())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'._wrap(super(Entity, self).getWorld())

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(_Entity, self).setUuid(arg0)

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(_LivingEntity, self).onPrepareSpawn(arg0)

    @overload
    def onHurt(self, arg0: float, arg1: 'DamageSource') -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.onHurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        return bool._wrap(super(_LivingEntity, self).onHurt(_float.valueOf(arg0), arg1))

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
    def getHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getHealth()"""
        return float._wrap(super(LivingEntity, self).getHealth())

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str._wrap(super(Entity, self).getPublicName())

    @override
    @overload
    def setHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setHealth(float)"""
        super(_LivingEntity, self).setHealth(_float.valueOf(arg0))

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0))

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(_Entity, self).setX(_double.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def onDeath(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDeath(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).onDeath(arg0)

    @override
    @overload
    def getMaxHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.Something.getMaxHealth()"""
        return float._wrap(super(Something, self).getMaxHealth())

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'._wrap(super(Entity, self).getBoundingBox())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.LivingEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_LivingEntity, self).save(arg0))

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float._wrap(super(_Entity, self).distanceTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int._wrap(super(Entity, self).getId())

    @override
    @overload
    def getSpeed(self) -> float:
        """public double dev.ultreon.quantum.entity.LivingEntity.getSpeed()"""
        return float._wrap(super(LivingEntity, self).getSpeed())

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool._wrap(super(Entity, self).isInVoid())

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasExplicitPermission(arg0))

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_Entity, self).hasExplicitPermission(arg0))

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str._wrap(super(Entity, self).getName())

    @override
    @overload
    def setJumpVel(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setJumpVel(float)"""
        super(_LivingEntity, self).setJumpVel(_float.valueOf(arg0))

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(_Entity, self).setYRot(_float.valueOf(arg0))

    @override
    @overload
    def getJumpVel(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getJumpVel()"""
        return float._wrap(super(LivingEntity, self).getJumpVel())

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float._wrap(super(Entity, self).getYRot())

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'._wrap(super(Entity, self).getRotation())

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.LivingEntity.getLookVector()"""
        return 'vector.Vec3d'._wrap(super(LivingEntity, self).getLookVector())

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.tick()"""
        super(LivingEntity, self).tick()

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(_Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'._wrap(super(Entity, self).getDisplayName())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(_Entity, self).setPosition(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def getChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.entity.LivingEntity.getChunkPos()"""
        return 'world.ChunkPos'._wrap(super(LivingEntity, self).getChunkPos())

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(_Entity, self).setXRot(_float.valueOf(arg0))

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(_Entity, self).sendMessage(arg0)

    @override
    @overload
    def createAiGoals(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.createAiGoals()"""
        super(LivingEntity, self).createAiGoals()

    @override
    @overload
    def getLastDamageSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.LivingEntity.getLastDamageSource()"""
        return 'damagesource.DamageSource'._wrap(super(LivingEntity, self).getLastDamageSource())

    @override
    @overload
    def kill(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.kill()"""
        super(LivingEntity, self).kill()

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity._wrap(_Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(_LivingEntity, self).load(arg0)

    @override
    @overload
    def isDead(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isDead()"""
        return bool._wrap(super(LivingEntity, self).isDead())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getPosition())

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(_Entity, self).setZ(_double.valueOf(arg0))

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).loadWithPos(arg0) 
 
 
# CLASS: dev.ultreon.quantum.entity.S2CEntityPipeline
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.entity.S2CEntityPipeline as _S2CEntityPipeline
_S2CEntityPipeline = _S2CEntityPipeline
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class S2CEntityPipeline():
    """dev.ultreon.quantum.entity.S2CEntityPipeline"""
 
    @staticmethod
    def _wrap(java_value: _S2CEntityPipeline) -> 'S2CEntityPipeline':
        return S2CEntityPipeline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CEntityPipeline):
        """
        Dynamic initializer for S2CEntityPipeline.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CEntityPipeline__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CEntityPipeline__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.entity.S2CEntityPipeline.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CEntityPipeline, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.entity.S2CEntityPipeline.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CEntityPipeline, self).handle(arg0, arg1)

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

    @overload
    def __init__(self, arg0: int, arg1: 'MapType'):
        """public dev.ultreon.quantum.entity.S2CEntityPipeline(int,dev.ultreon.ubo.types.MapType)"""
        val = _S2CEntityPipeline(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.entity.S2CEntityPipeline(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CEntityPipeline(arg0)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.entity.EntityType$EntityFactory
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.entity.EntityType as _EntityType_EntityFactory
_EntityFactory = _EntityType_EntityFactory.EntityFactory
from abc import abstractmethod, ABC
 
class EntityFactory():
    """dev.ultreon.quantum.entity.EntityType.EntityFactory"""
 
    @staticmethod
    def _wrap(java_value: _EntityFactory) -> 'EntityFactory':
        return EntityFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityFactory):
        """
        Dynamic initializer for EntityFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, arg0: 'EntityType', arg1: 'World'):
        """public abstract T dev.ultreon.quantum.entity.EntityType$EntityFactory.create(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.world.World)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.entity.AttributeModifier
import dev.ultreon.quantum.entity.AttributeModifier as _AttributeModifier
_AttributeModifier = _AttributeModifier
from builtins import str
import java.util.UUID as UUID
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.entity.AttributeModifier as _AttributeModifier_Operation
_Operation = _AttributeModifier_Operation.Operation
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class AttributeModifier():
    """dev.ultreon.quantum.entity.AttributeModifier"""
 
    @staticmethod
    def _wrap(java_value: _AttributeModifier) -> 'AttributeModifier':
        return AttributeModifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AttributeModifier):
        """
        Dynamic initializer for AttributeModifier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AttributeModifier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AttributeModifier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.AttributeModifier.hashCode()"""
        return int._wrap(super(AttributeModifier, self).hashCode())

    @overload
    def id(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.AttributeModifier.id()"""
        return 'UUID'._wrap(super(AttributeModifier, self).id())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.AttributeModifier.equals(java.lang.Object)"""
        return bool._wrap(super(_AttributeModifier, self).equals(arg0))

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
    def operation(self) -> 'Operation':
        """public dev.ultreon.quantum.entity.AttributeModifier$Operation dev.ultreon.quantum.entity.AttributeModifier.operation()"""
        return 'Operation'._wrap(super(AttributeModifier, self).operation())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'UUID', arg1: 'Operation', arg2: float):
        """public dev.ultreon.quantum.entity.AttributeModifier(java.util.UUID,dev.ultreon.quantum.entity.AttributeModifier$Operation,double)"""
        val = _AttributeModifier(arg0, arg1, _double.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def value(self) -> float:
        """public double dev.ultreon.quantum.entity.AttributeModifier.value()"""
        return float._wrap(super(AttributeModifier, self).value())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.AttributeModifier.toString()"""
        return str._wrap(super(AttributeModifier, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.entity.Pig
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.damagesource.DamageSource as _DamageSource
_DamageSource = _DamageSource
import dev.ultreon.quantum.world.ChunkPos as _ChunkPos
_ChunkPos = _ChunkPos
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

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
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
try:
    from pyquantum.entity import util
except ImportError:
    util = _import_once("pyquantum.entity.util")

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
import dev.ultreon.quantum.entity.Pig as _Pig
_Pig = _Pig
import dev.ultreon.quantum.entity.EntityType as _EntityType
_EntityType = _EntityType
import java.lang.String as _string
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.entity.Entity as _Entity_Pose
_Pose = _Entity_Pose.Pose
import dev.ultreon.quantum.entity.AttributeMap as _AttributeMap
_AttributeMap = _AttributeMap
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
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class Pig():
    """dev.ultreon.quantum.entity.Pig"""
 
    @staticmethod
    def _wrap(java_value: _Pig) -> 'Pig':
        return Pig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pig):
        """
        Dynamic initializer for Pig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setGravity(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setGravity(float)"""
        super(_Entity, self).setGravity(_float.valueOf(arg0))

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.entity.Entity.getLocation()"""
        return 'world.Location'._wrap(super(Entity, self).getLocation())

    @override
    @overload
    def setMaxHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setMaxHealth(float)"""
        super(_LivingEntity, self).setMaxHealth(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getAge(self) -> int:
        """public int dev.ultreon.quantum.entity.LivingEntity.getAge()"""
        return int._wrap(super(LivingEntity, self).getAge())

    @override
    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setY(double)"""
        super(_Entity, self).setY(_double.valueOf(arg0))

    @overload
    def getBoundingBox(self, arg0: 'EntitySize') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.quantum.entity.util.EntitySize)"""
        return 'util.BoundingBox'._wrap(super(_Entity, self).getBoundingBox(arg0))

    @override
    @overload
    def teleportTo(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(double,double,double)"""
        super(_Entity, self).teleportTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def getPipeline(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.Entity.getPipeline()"""
        return 'types.MapType'._wrap(super(Entity, self).getPipeline())

    @override
    @overload
    def getBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.entity.Entity.getBlockPos()"""
        return 'world.BlockPos'._wrap(super(Entity, self).getBlockPos())

    @override
    @overload
    def teleportTo(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(int,int,int)"""
        super(_Entity, self).teleportTo(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.entity.Entity.getUuid()"""
        return 'UUID'._wrap(super(Entity, self).getUuid())

    @override
    @overload
    def getXRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getXRot()"""
        return float._wrap(super(Entity, self).getXRot())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(_Entity, self).sendMessage(arg0)

    @override
    @overload
    def applyEffect(self, arg0: 'AppliedEffect'):
        """public void dev.ultreon.quantum.entity.LivingEntity.applyEffect(dev.ultreon.quantum.item.food.AppliedEffect)"""
        super(_LivingEntity, self).applyEffect(arg0)

    @override
    @overload
    def rotate(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.rotate(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).rotate(arg0)

    @override
    @overload
    def getSize(self) -> 'util.EntitySize':
        """public dev.ultreon.quantum.entity.util.EntitySize dev.ultreon.quantum.entity.Entity.getSize()"""
        return 'util.EntitySize'._wrap(super(Entity, self).getSize())

    @overload
    def getPose(self) -> 'Pose':
        """public dev.ultreon.quantum.entity.Entity$Pose dev.ultreon.quantum.entity.Pig.getPose()"""
        return 'Pose'._wrap(super(Pig, self).getPose())

    @override
    @overload
    def onDropItems(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDropItems(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).onDropItems(arg0)

    @override
    @overload
    def getVelocity(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getVelocity()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getVelocity())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getAnimation(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Pig.getAnimation()"""
        return str._wrap(super(Pig, self).getAnimation())

    @override
    @overload
    def getAttributes(self) -> 'AttributeMap':
        """public dev.ultreon.quantum.entity.AttributeMap dev.ultreon.quantum.entity.Entity.getAttributes()"""
        return 'AttributeMap'._wrap(super(Entity, self).getAttributes())

    @override
    @overload
    def setVelocity(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setVelocity(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setVelocity(arg0)

    @override
    @overload
    def hurt(self, arg0: float, arg1: 'DamageSource'):
        """public final void dev.ultreon.quantum.entity.LivingEntity.hurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).hurt(_float.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getX(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getX()"""
        return float._wrap(super(Entity, self).getX())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAdmin()"""
        return bool._wrap(super(Entity, self).isAdmin())

    @override
    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isInvincible()"""
        return bool._wrap(super(LivingEntity, self).isInvincible())

    @override
    @overload
    def isWalking(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isWalking()"""
        return bool._wrap(super(LivingEntity, self).isWalking())

    @override
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getY()"""
        return float._wrap(super(Entity, self).getY())

    @override
    @overload
    def getRng(self) -> 'rng.RNG':
        """public dev.ultreon.quantum.world.rng.RNG dev.ultreon.quantum.entity.Entity.getRng()"""
        return 'rng.RNG'._wrap(super(Entity, self).getRng())

    @override
    @overload
    def setRotation(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.entity.Entity.setRotation(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_Entity, self).setRotation(arg0)

    @override
    @overload
    def moveTowards(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.moveTowards(double,double,double,double)"""
        super(_LivingEntity, self).moveTowards(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))

    @override
    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.quantum.entity.Entity.getZ()"""
        return float._wrap(super(Entity, self).getZ())

    @override
    @overload
    def rotate(self, arg0: float, arg1: float):
        """public void dev.ultreon.quantum.entity.Entity.rotate(float,float)"""
        super(_Entity, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getGravity(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getGravity()"""
        return float._wrap(super(Entity, self).getGravity())

    @override
    @overload
    def setInvincible(self, arg0: bool):
        """public void dev.ultreon.quantum.entity.LivingEntity.setInvincible(boolean)"""
        super(_LivingEntity, self).setInvincible(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'EntityType', arg1: 'World'):
        """public dev.ultreon.quantum.entity.Pig(dev.ultreon.quantum.entity.EntityType<? extends dev.ultreon.quantum.entity.Pig>,dev.ultreon.quantum.world.World)"""
        val = _Pig(arg0, arg1)
        self.__wrapper = val

    @overload
    def move(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.move(double,double,double)"""
        return bool._wrap(super(_Entity, self).move(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def setId(self, arg0: int):
        """public void dev.ultreon.quantum.entity.Entity.setId(int)"""
        super(_Entity, self).setId(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def jump(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.jump()"""
        super(LivingEntity, self).jump()

    @override
    @overload
    def isInWater(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInWater()"""
        return bool._wrap(super(Entity, self).isInWater())

    @override
    @overload
    def setPosition(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).setPosition(arg0)

    @override
    @overload
    def sendPipeline(self):
        """public void dev.ultreon.quantum.entity.Entity.sendPipeline()"""
        super(Entity, self).sendPipeline()

    @override
    @overload
    def onPipeline(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.onPipeline(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).onPipeline(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getBoundingBox(arg0: 'Vec3d', arg1: 'EntitySize') -> 'util.BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.entity.util.EntitySize)"""
        return util.BoundingBox._wrap(_Entity.getBoundingBox(arg0, arg1))

    @overload
    def distanceTo(self, arg0: 'Entity') -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(dev.ultreon.quantum.entity.Entity)"""
        return float._wrap(super(_Entity, self).distanceTo(arg0))

    @override
    @overload
    def isAffectedByFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isAffectedByFluid()"""
        return bool._wrap(super(Entity, self).isAffectedByFluid())

    @override
    @overload
    def isMarkedForRemoval(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isMarkedForRemoval()"""
        return bool._wrap(super(Entity, self).isMarkedForRemoval())

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def markRemoved(self):
        """public void dev.ultreon.quantum.entity.Entity.markRemoved()"""
        super(Entity, self).markRemoved()

    @override
    @overload
    def getDeathSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.LivingEntity.getDeathSound()"""
        return 'world.SoundEvent'._wrap(super(LivingEntity, self).getDeathSound())

    @override
    @overload
    def getType(self) -> 'EntityType':
        """public dev.ultreon.quantum.entity.EntityType<?> dev.ultreon.quantum.entity.Entity.getType()"""
        return 'EntityType'._wrap(super(Entity, self).getType())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.entity.Entity.getWorld()"""
        return 'world.World'._wrap(super(Entity, self).getWorld())

    @override
    @overload
    def teleportTo(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.quantum.entity.Entity)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def setUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.entity.Entity.setUuid(java.util.UUID)"""
        super(_Entity, self).setUuid(arg0)

    @override
    @overload
    def onPrepareSpawn(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onPrepareSpawn(dev.ultreon.ubo.types.MapType)"""
        super(_LivingEntity, self).onPrepareSpawn(arg0)

    @overload
    def onHurt(self, arg0: float, arg1: 'DamageSource') -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.onHurt(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        return bool._wrap(super(_LivingEntity, self).onHurt(_float.valueOf(arg0), arg1))

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
    def getHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getHealth()"""
        return float._wrap(super(LivingEntity, self).getHealth())

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getPublicName()"""
        return str._wrap(super(Entity, self).getPublicName())

    @override
    @overload
    def setHealth(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setHealth(float)"""
        super(_LivingEntity, self).setHealth(_float.valueOf(arg0))

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0))

    @override
    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setX(double)"""
        super(_Entity, self).setX(_double.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def onDeath(self, arg0: 'DamageSource'):
        """public void dev.ultreon.quantum.entity.LivingEntity.onDeath(dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        super(_LivingEntity, self).onDeath(arg0)

    @override
    @overload
    def getBoundingBox(self) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.entity.Entity.getBoundingBox()"""
        return 'util.BoundingBox'._wrap(super(Entity, self).getBoundingBox())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.entity.LivingEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_LivingEntity, self).save(arg0))

    @overload
    def distanceTo(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.entity.Entity.distanceTo(double,double,double)"""
        return float._wrap(super(_Entity, self).distanceTo(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getMaxHealth(self) -> float:
        """public float dev.ultreon.quantum.entity.Pig.getMaxHealth()"""
        return float._wrap(super(Pig, self).getMaxHealth())

    @override
    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.entity.Entity.getId()"""
        return int._wrap(super(Entity, self).getId())

    @override
    @overload
    def getSpeed(self) -> float:
        """public double dev.ultreon.quantum.entity.LivingEntity.getSpeed()"""
        return float._wrap(super(LivingEntity, self).getSpeed())

    @override
    @overload
    def getHurtSound(self) -> 'world.SoundEvent':
        """public dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.entity.Pig.getHurtSound()"""
        return 'world.SoundEvent'._wrap(super(Pig, self).getHurtSound())

    @override
    @overload
    def isInVoid(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.isInVoid()"""
        return bool._wrap(super(Entity, self).isInVoid())

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasExplicitPermission(arg0))

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.entity.Entity.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_Entity, self).hasExplicitPermission(arg0))

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.Entity.getName()"""
        return str._wrap(super(Entity, self).getName())

    @override
    @overload
    def setJumpVel(self, arg0: float):
        """public void dev.ultreon.quantum.entity.LivingEntity.setJumpVel(float)"""
        super(_LivingEntity, self).setJumpVel(_float.valueOf(arg0))

    @override
    @overload
    def setYRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setYRot(float)"""
        super(_Entity, self).setYRot(_float.valueOf(arg0))

    @override
    @overload
    def getJumpVel(self) -> float:
        """public float dev.ultreon.quantum.entity.LivingEntity.getJumpVel()"""
        return float._wrap(super(LivingEntity, self).getJumpVel())

    @override
    @overload
    def teleportTo(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.entity.Entity.teleportTo(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(_Entity, self).teleportTo(arg0)

    @override
    @overload
    def getYRot(self) -> float:
        """public float dev.ultreon.quantum.entity.Entity.getYRot()"""
        return float._wrap(super(Entity, self).getYRot())

    @override
    @overload
    def getRotation(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.entity.Entity.getRotation()"""
        return 'vector.Vec2f'._wrap(super(Entity, self).getRotation())

    @override
    @overload
    def getLookVector(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.LivingEntity.getLookVector()"""
        return 'vector.Vec3d'._wrap(super(LivingEntity, self).getLookVector())

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.tick()"""
        super(LivingEntity, self).tick()

    @override
    @overload
    def teleportDimension(self, arg0: 'Vec3d', arg1: 'ServerWorld'):
        """public void dev.ultreon.quantum.entity.Entity.teleportDimension(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        super(_Entity, self).teleportDimension(arg0, arg1)

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.entity.Entity.getDisplayName()"""
        return 'text.TextObject'._wrap(super(Entity, self).getDisplayName())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.entity.Entity.setPosition(double,double,double)"""
        super(_Entity, self).setPosition(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def getChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.entity.LivingEntity.getChunkPos()"""
        return 'world.ChunkPos'._wrap(super(LivingEntity, self).getChunkPos())

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_commands.CommandSender, self).hasPermission(arg0))

    @override
    @overload
    def setXRot(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setXRot(float)"""
        super(_Entity, self).setXRot(_float.valueOf(arg0))

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.entity.Entity.sendMessage(java.lang.String)"""
        super(_Entity, self).sendMessage(arg0)

    @override
    @overload
    def createAiGoals(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.createAiGoals()"""
        super(LivingEntity, self).createAiGoals()

    @override
    @overload
    def getLastDamageSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.entity.LivingEntity.getLastDamageSource()"""
        return 'damagesource.DamageSource'._wrap(super(LivingEntity, self).getLastDamageSource())

    @override
    @overload
    def kill(self):
        """public void dev.ultreon.quantum.entity.LivingEntity.kill()"""
        super(LivingEntity, self).kill()

    @staticmethod
    @overload
    def loadFrom(arg0: 'World', arg1: 'MapType') -> 'Entity':
        """public static dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.entity.Entity.loadFrom(dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.MapType)"""
        return Entity._wrap(_Entity.loadFrom(arg0, arg1))

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.LivingEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(_LivingEntity, self).load(arg0)

    @override
    @overload
    def isDead(self) -> bool:
        """public boolean dev.ultreon.quantum.entity.LivingEntity.isDead()"""
        return bool._wrap(super(LivingEntity, self).isDead())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.entity.Entity.getPosition()"""
        return 'vector.Vec3d'._wrap(super(Entity, self).getPosition())

    @override
    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.quantum.entity.Entity.setZ(double)"""
        super(_Entity, self).setZ(_double.valueOf(arg0))

    @override
    @overload
    def loadWithPos(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.entity.Entity.loadWithPos(dev.ultreon.ubo.types.MapType)"""
        super(_Entity, self).loadWithPos(arg0)