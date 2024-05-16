from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import dev.ultreon.quantum.item.tool.ToolItem as _ToolItem
_ToolItem = _ToolItem
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.item.tool.ShovelItem as _ShovelItem
_ShovelItem = _ShovelItem
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
from builtins import bool
try:
    from pyquantum.item import material
except ImportError:
    material = _import_once("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShovelItem():
    """dev.ultreon.quantum.item.tool.ShovelItem"""
 
    @staticmethod
    def _wrap(java_value: _ShovelItem) -> 'ShovelItem':
        return ShovelItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShovelItem):
        """
        Dynamic initializer for ShovelItem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShovelItem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShovelItem__wrapper":
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
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'._wrap(super(item.Item, self).getTranslation())

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'._wrap(super(_item.Item, self).getDescription(arg0))

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
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.tool.ShovelItem.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float._wrap(super(_ShovelItem, self).getAttackDamage(arg0))

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int._wrap(super(item.Item, self).getMaxStackSize())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.ShovelItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = _ShovelItem(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'._wrap(super(item.Item, self).getId())

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str._wrap(super(item.Item, self).getTranslationId())

    @overload
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'._wrap(super(_item.Item, self).use(arg0))

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

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'._wrap(super(item.Item, self).defaultStack())

    @override
    @overload
    def getToolType(self) -> 'ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ShovelItem.getToolType()"""
        return 'ToolType'._wrap(super(ShovelItem, self).getToolType())

    @override
    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float._wrap(super(ToolItem, self).getEfficiency())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.item.tool.ShovelItem
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import dev.ultreon.quantum.item.tool.ToolItem as _ToolItem
_ToolItem = _ToolItem
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.item.tool.ShovelItem as _ShovelItem
_ShovelItem = _ShovelItem
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
from builtins import bool
try:
    from pyquantum.item import material
except ImportError:
    material = _import_once("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShovelItem():
    """dev.ultreon.quantum.item.tool.ShovelItem"""
 
    @staticmethod
    def _wrap(java_value: _ShovelItem) -> 'ShovelItem':
        return ShovelItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShovelItem):
        """
        Dynamic initializer for ShovelItem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShovelItem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShovelItem__wrapper":
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
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'._wrap(super(item.Item, self).getTranslation())

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'._wrap(super(_item.Item, self).getDescription(arg0))

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
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.tool.ShovelItem.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float._wrap(super(_ShovelItem, self).getAttackDamage(arg0))

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int._wrap(super(item.Item, self).getMaxStackSize())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.ShovelItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = _ShovelItem(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'._wrap(super(item.Item, self).getId())

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str._wrap(super(item.Item, self).getTranslationId())

    @overload
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'._wrap(super(_item.Item, self).use(arg0))

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

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'._wrap(super(item.Item, self).defaultStack())

    @override
    @overload
    def getToolType(self) -> 'ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ShovelItem.getToolType()"""
        return 'ToolType'._wrap(super(ShovelItem, self).getToolType())

    @override
    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float._wrap(super(ToolItem, self).getEfficiency())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.item.tool.ShovelItem 
 
 
# CLASS: dev.ultreon.quantum.item.tool.ToolType
from builtins import str
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
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
 
class ToolType():
    """dev.ultreon.quantum.item.tool.ToolType"""
 
    @staticmethod
    def _wrap(java_value: _ToolType) -> 'ToolType':
        return ToolType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToolType):
        """
        Dynamic initializer for ToolType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToolType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToolType__wrapper":
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
    def valueOf(arg0: str) -> 'ToolType':
        """public static dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ToolType.valueOf(java.lang.String)"""
        return ToolType._wrap(_ToolType.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['ToolType']:
        """public static dev.ultreon.quantum.item.tool.ToolType[] dev.ultreon.quantum.item.tool.ToolType.values()"""
        return List[ToolType]._wrap(_ToolType.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


ToolType.SHOVEL = ToolType._wrap(_SHOVEL.SHOVEL)

ToolType.PICKAXE = ToolType._wrap(_PICKAXE.PICKAXE)

ToolType.AXE = ToolType._wrap(_AXE.AXE) 
 
 
# CLASS: dev.ultreon.quantum.item.tool.PickaxeItem
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import dev.ultreon.quantum.item.tool.ToolItem as _ToolItem
_ToolItem = _ToolItem
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
from builtins import bool
try:
    from pyquantum.item import material
except ImportError:
    material = _import_once("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
import java.lang.Integer as _int
import dev.ultreon.quantum.item.tool.PickaxeItem as _PickaxeItem
_PickaxeItem = _PickaxeItem
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PickaxeItem():
    """dev.ultreon.quantum.item.tool.PickaxeItem"""
 
    @staticmethod
    def _wrap(java_value: _PickaxeItem) -> 'PickaxeItem':
        return PickaxeItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PickaxeItem):
        """
        Dynamic initializer for PickaxeItem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PickaxeItem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PickaxeItem__wrapper":
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
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'._wrap(super(item.Item, self).getTranslation())

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.PickaxeItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = _PickaxeItem(arg0, arg1)
        self.__wrapper = val

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'._wrap(super(_item.Item, self).getDescription(arg0))

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
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int._wrap(super(item.Item, self).getMaxStackSize())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getToolType(self) -> 'ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.PickaxeItem.getToolType()"""
        return 'ToolType'._wrap(super(PickaxeItem, self).getToolType())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'._wrap(super(item.Item, self).getId())

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str._wrap(super(item.Item, self).getTranslationId())

    @overload
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'._wrap(super(_item.Item, self).use(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.tool.PickaxeItem.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float._wrap(super(_PickaxeItem, self).getAttackDamage(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'._wrap(super(item.Item, self).defaultStack())

    @override
    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float._wrap(super(ToolItem, self).getEfficiency())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.item.tool.AxeItem
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import dev.ultreon.quantum.item.tool.ToolItem as _ToolItem
_ToolItem = _ToolItem
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
from builtins import bool
try:
    from pyquantum.item import material
except ImportError:
    material = _import_once("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
import dev.ultreon.quantum.item.tool.AxeItem as _AxeItem
_AxeItem = _AxeItem
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AxeItem():
    """dev.ultreon.quantum.item.tool.AxeItem"""
 
    @staticmethod
    def _wrap(java_value: _AxeItem) -> 'AxeItem':
        return AxeItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AxeItem):
        """
        Dynamic initializer for AxeItem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AxeItem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AxeItem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.AxeItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = _AxeItem(arg0, arg1)
        self.__wrapper = val

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float._wrap(super(_item.Item, self).getAttackDamage(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'._wrap(super(item.Item, self).getTranslation())

    @override
    @overload
    def getToolType(self) -> 'ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.AxeItem.getToolType()"""
        return 'ToolType'._wrap(super(AxeItem, self).getToolType())

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'._wrap(super(_item.Item, self).getDescription(arg0))

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
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int._wrap(super(item.Item, self).getMaxStackSize())

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
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'._wrap(super(item.Item, self).getId())

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str._wrap(super(item.Item, self).getTranslationId())

    @overload
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'._wrap(super(_item.Item, self).use(arg0))

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

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'._wrap(super(item.Item, self).defaultStack())

    @override
    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float._wrap(super(ToolItem, self).getEfficiency())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.item.tool.ToolItem
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import dev.ultreon.quantum.item.tool.ToolItem as _ToolItem
_ToolItem = _ToolItem
import java.lang.Object as _Object
_Object = _Object
from builtins import type
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
from builtins import bool
try:
    from pyquantum.item import material
except ImportError:
    material = _import_once("pyquantum.item.material")

try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ToolItem():
    """dev.ultreon.quantum.item.tool.ToolItem"""
 
    @staticmethod
    def _wrap(java_value: _ToolItem) -> 'ToolItem':
        return ToolItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToolItem):
        """
        Dynamic initializer for ToolItem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToolItem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToolItem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getToolType(self, ):
        """public abstract dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.item.tool.ToolItem.getToolType()"""
        pass

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float._wrap(super(_item.Item, self).getAttackDamage(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'._wrap(super(item.Item, self).getTranslation())

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'._wrap(super(_item.Item, self).getDescription(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'ItemMaterial'):
        """public dev.ultreon.quantum.item.tool.ToolItem(dev.ultreon.quantum.item.Item$Properties,dev.ultreon.quantum.item.material.ItemMaterial)"""
        val = _ToolItem(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int._wrap(super(item.Item, self).getMaxStackSize())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getEfficiency(self) -> float:
        """public float dev.ultreon.quantum.item.tool.ToolItem.getEfficiency()"""
        return float._wrap(super(ToolItem, self).getEfficiency())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'._wrap(super(item.Item, self).getId())

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str._wrap(super(item.Item, self).getTranslationId())

    @overload
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'._wrap(super(_item.Item, self).use(arg0))

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

    @override
    @overload
    def defaultStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'item.ItemStack'._wrap(super(item.Item, self).defaultStack())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())