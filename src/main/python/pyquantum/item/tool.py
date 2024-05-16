from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.tool.ToolItem as __ToolItem
__ToolItem = __ToolItem
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
from builtins import bool
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum.item import material
except ImportError:
    material = __import_once__("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.item.tool.ShovelItem as __ShovelItem
__ShovelItem = __ShovelItem
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class ShovelItem(__ToolItem, ToolItem):
    """dev.ultreon.quantum.item.tool.ShovelItem"""
 
    @staticmethod
    def __wrap(java_value: __ShovelItem) -> 'ShovelItem':
        return ShovelItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShovelItem):
        """
        Dynamic initializer for ShovelItem.
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
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'.__wrap(super(__item.Item, self).getDescription(arg0))

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int.__wrap(super(item.Item, self).getMaxStackSize())

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
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'.__wrap(super(item.Item, self).getTranslation())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.ShovelItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = __ShovelItem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getToolType(self) -> 'ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ShovelItem.getToolType()"""
        return 'ToolType'.__wrap(super(ShovelItem, self).getToolType())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'.__wrap(super(__item.Item, self).use(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'.__wrap(super(item.Item, self).defaultStack())

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.tool.ShovelItem.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float.__wrap(super(__ShovelItem, self).getAttackDamage(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float.__wrap(super(ToolItem, self).getEfficiency())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'.__wrap(super(item.Item, self).getId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str.__wrap(super(item.Item, self).getTranslationId())

 
 
 
# CLASS: dev.ultreon.quantum.item.tool.ShovelItem
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.tool.ToolItem as __ToolItem
__ToolItem = __ToolItem
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
from builtins import bool
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum.item import material
except ImportError:
    material = __import_once__("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.item.tool.ShovelItem as __ShovelItem
__ShovelItem = __ShovelItem
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class ShovelItem(__ToolItem, ToolItem):
    """dev.ultreon.quantum.item.tool.ShovelItem"""
 
    @staticmethod
    def __wrap(java_value: __ShovelItem) -> 'ShovelItem':
        return ShovelItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShovelItem):
        """
        Dynamic initializer for ShovelItem.
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
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'.__wrap(super(__item.Item, self).getDescription(arg0))

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int.__wrap(super(item.Item, self).getMaxStackSize())

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
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'.__wrap(super(item.Item, self).getTranslation())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.ShovelItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = __ShovelItem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getToolType(self) -> 'ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ShovelItem.getToolType()"""
        return 'ToolType'.__wrap(super(ShovelItem, self).getToolType())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'.__wrap(super(__item.Item, self).use(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'.__wrap(super(item.Item, self).defaultStack())

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.tool.ShovelItem.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float.__wrap(super(__ShovelItem, self).getAttackDamage(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float.__wrap(super(ToolItem, self).getEfficiency())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'.__wrap(super(item.Item, self).getId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str.__wrap(super(item.Item, self).getTranslationId())

 
 
 
# CLASS: dev.ultreon.quantum.item.tool.ShovelItem 
 
 
# CLASS: dev.ultreon.quantum.item.tool.ToolType
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
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
from builtins import int
 
class ToolType(__Enum, Enum):
    """dev.ultreon.quantum.item.tool.ToolType"""
 
    @staticmethod
    def __wrap(java_value: __ToolType) -> 'ToolType':
        return ToolType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToolType):
        """
        Dynamic initializer for ToolType.
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
 
    # public static final dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ToolType.PICKAXE
    PICKAXE: 'ToolType' = __wrap(__ToolType.PICKAXE)

    # public static final dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ToolType.SHOVEL
    SHOVEL: 'ToolType' = __wrap(__ToolType.SHOVEL)

    # public static final dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ToolType.AXE
    AXE: 'ToolType' = __wrap(__ToolType.AXE)


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

    @staticmethod
    @overload
    def values() -> List['ToolType']:
        """public static dev.ultreon.quantum.item.tool.ToolType[] dev.ultreon.quantum.item.tool.ToolType.values()"""
        return List[ToolType].__wrap(__ToolType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ToolType':
        """public static dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ToolType.valueOf(java.lang.String)"""
        return ToolType.__wrap(__ToolType.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.item.tool.PickaxeItem
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.tool.ToolItem as __ToolItem
__ToolItem = __ToolItem
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
from builtins import bool
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum.item import material
except ImportError:
    material = __import_once__("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.item.tool.PickaxeItem as __PickaxeItem
__PickaxeItem = __PickaxeItem
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class PickaxeItem(__ToolItem, ToolItem):
    """dev.ultreon.quantum.item.tool.PickaxeItem"""
 
    @staticmethod
    def __wrap(java_value: __PickaxeItem) -> 'PickaxeItem':
        return PickaxeItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PickaxeItem):
        """
        Dynamic initializer for PickaxeItem.
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
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'.__wrap(super(__item.Item, self).getDescription(arg0))

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int.__wrap(super(item.Item, self).getMaxStackSize())

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
    def getToolType(self) -> 'ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.PickaxeItem.getToolType()"""
        return 'ToolType'.__wrap(super(PickaxeItem, self).getToolType())

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.tool.PickaxeItem.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float.__wrap(super(__PickaxeItem, self).getAttackDamage(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'.__wrap(super(item.Item, self).getTranslation())

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
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'.__wrap(super(__item.Item, self).use(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'.__wrap(super(item.Item, self).defaultStack())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.PickaxeItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = __PickaxeItem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float.__wrap(super(ToolItem, self).getEfficiency())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'.__wrap(super(item.Item, self).getId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str.__wrap(super(item.Item, self).getTranslationId()) 
 
 
# CLASS: dev.ultreon.quantum.item.tool.AxeItem
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.tool.ToolItem as __ToolItem
__ToolItem = __ToolItem
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
from builtins import bool
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum.item import material
except ImportError:
    material = __import_once__("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.item.tool.AxeItem as __AxeItem
__AxeItem = __AxeItem
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class AxeItem(__ToolItem, ToolItem):
    """dev.ultreon.quantum.item.tool.AxeItem"""
 
    @staticmethod
    def __wrap(java_value: __AxeItem) -> 'AxeItem':
        return AxeItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AxeItem):
        """
        Dynamic initializer for AxeItem.
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
    def getToolType(self) -> 'ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.AxeItem.getToolType()"""
        return 'ToolType'.__wrap(super(AxeItem, self).getToolType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'.__wrap(super(__item.Item, self).getDescription(arg0))

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int.__wrap(super(item.Item, self).getMaxStackSize())

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
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'.__wrap(super(item.Item, self).getTranslation())

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
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'.__wrap(super(__item.Item, self).use(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'.__wrap(super(item.Item, self).defaultStack())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.AxeItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = __AxeItem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float.__wrap(super(__item.Item, self).getAttackDamage(arg0))

    @override
    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float.__wrap(super(ToolItem, self).getEfficiency())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'.__wrap(super(item.Item, self).getId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str.__wrap(super(item.Item, self).getTranslationId()) 
 
 
# CLASS: dev.ultreon.quantum.item.tool.ToolItem
from pyquantum_helper import import_once as __import_once__
from builtins import type
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.tool.ToolItem as __ToolItem
__ToolItem = __ToolItem
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
from builtins import bool
try:
    from pyquantum.item import material
except ImportError:
    material = __import_once__("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class ToolItem(ABC, pyquantum.__Item, item.Item):
    """dev.ultreon.quantum.item.tool.ToolItem"""
 
    @staticmethod
    def __wrap(java_value: __ToolItem) -> 'ToolItem':
        return ToolItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToolItem):
        """
        Dynamic initializer for ToolItem.
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
    def getToolType(self, ):
        """public abstract dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ToolItem.getToolType()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'.__wrap(super(__item.Item, self).getDescription(arg0))

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int.__wrap(super(item.Item, self).getMaxStackSize())

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
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.ToolItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = __ToolItem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float.__wrap(super(ToolItem, self).getEfficiency())

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'.__wrap(super(item.Item, self).getTranslation())

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
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'.__wrap(super(__item.Item, self).use(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'.__wrap(super(item.Item, self).defaultStack())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float.__wrap(super(__item.Item, self).getAttackDamage(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'.__wrap(super(item.Item, self).getId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str.__wrap(super(item.Item, self).getTranslationId())