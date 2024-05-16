from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.List as _List
_List = _List
import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Item():
    """dev.ultreon.quantum.item.Item"""
 
    @staticmethod
    def _wrap(java_value: _Item) -> 'Item':
        return Item(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Item):
        """
        Dynamic initializer for Item.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Item__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Item__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'._wrap(super(Item, self).getId())

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'._wrap(super(_Item, self).getDescription(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float._wrap(super(_Item, self).getAttackDamage(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.item.Item(dev.ultreon.quantum.item.Item$Properties)"""
        val = _Item(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str._wrap(super(Item, self).getTranslationId())

    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int._wrap(super(Item, self).getMaxStackSize())

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
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'._wrap(super(_Item, self).use(arg0))

    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'._wrap(super(Item, self).getTranslation())

    @overload
    def defaultStack(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'ItemStack'._wrap(super(Item, self).defaultStack())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.item.Item
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.List as _List
_List = _List
import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Item():
    """dev.ultreon.quantum.item.Item"""
 
    @staticmethod
    def _wrap(java_value: _Item) -> 'Item':
        return Item(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Item):
        """
        Dynamic initializer for Item.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Item__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Item__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'._wrap(super(Item, self).getId())

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'._wrap(super(_Item, self).getDescription(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float._wrap(super(_Item, self).getAttackDamage(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.item.Item(dev.ultreon.quantum.item.Item$Properties)"""
        val = _Item(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str._wrap(super(Item, self).getTranslationId())

    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int._wrap(super(Item, self).getMaxStackSize())

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
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'._wrap(super(_Item, self).use(arg0))

    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'._wrap(super(Item, self).getTranslation())

    @overload
    def defaultStack(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'ItemStack'._wrap(super(Item, self).defaultStack())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.item.Item 
 
 
# CLASS: dev.ultreon.quantum.item.ItemStack
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
import de.marhali.json5.Json5Object as Json5Object
from builtins import bool
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ItemStack():
    """dev.ultreon.quantum.item.ItemStack"""
 
    @staticmethod
    def _wrap(java_value: _ItemStack) -> 'ItemStack':
        return ItemStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemStack):
        """
        Dynamic initializer for ItemStack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemStack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemStack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def transferTo(self, arg0: 'ItemStack', arg1: int) -> int:
        """public int dev.ultreon.quantum.item.ItemStack.transferTo(dev.ultreon.quantum.item.ItemStack,int)"""
        return int._wrap(super(_ItemStack, self).transferTo(arg0, _int.valueOf(arg1)))

    @overload
    def getAttackDamage(self) -> float:
        """public float dev.ultreon.quantum.item.ItemStack.getAttackDamage()"""
        return float._wrap(super(ItemStack, self).getAttackDamage())

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.item.ItemStack.save()"""
        return 'types.MapType'._wrap(super(ItemStack, self).save())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.item.ItemStack()"""
        val = _ItemStack()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.ItemStack.toString()"""
        return str._wrap(super(ItemStack, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def sameItemSameData(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.item.ItemStack.sameItemSameData(dev.ultreon.quantum.item.ItemStack)"""
        return bool._wrap(super(_ItemStack, self).sameItemSameData(arg0))

    @overload
    def setData(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.item.ItemStack.setData(dev.ultreon.ubo.types.MapType)"""
        super(_ItemStack, self).setData(arg0)

    @overload
    def split(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.split()"""
        return 'ItemStack'._wrap(super(ItemStack, self).split())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def split(self, arg0: int) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.split(int)"""
        return 'ItemStack'._wrap(super(_ItemStack, self).split(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def merge(self, arg0: 'ItemStack') -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.merge(dev.ultreon.quantum.item.ItemStack)"""
        return 'ItemStack'._wrap(super(_ItemStack, self).merge(arg0))

    @overload
    def copy(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.copy()"""
        return 'ItemStack'._wrap(super(ItemStack, self).copy())

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'ItemStack':
        """public static dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.load(dev.ultreon.ubo.types.MapType)"""
        return ItemStack._wrap(_ItemStack.load(arg0))

    @overload
    def __init__(self, arg0: 'Item', arg1: int):
        """public dev.ultreon.quantum.item.ItemStack(dev.ultreon.quantum.item.Item,int)"""
        val = _ItemStack(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @staticmethod
    @overload
    def empty() -> 'ItemStack':
        """public static dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.empty()"""
        return ItemStack._wrap(_ItemStack.empty())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def shrink(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.item.ItemStack.shrink(int)"""
        return int._wrap(super(_ItemStack, self).shrink(_int.valueOf(arg0)))

    @overload
    def getDescription(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.ItemStack.getDescription()"""
        return 'List'._wrap(super(ItemStack, self).getDescription())

    @overload
    def __init__(self, arg0: 'Item', arg1: int, arg2: 'MapType'):
        """public dev.ultreon.quantum.item.ItemStack(dev.ultreon.quantum.item.Item,int,dev.ultreon.ubo.types.MapType)"""
        val = _ItemStack(arg0, _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.item.ItemStack()"""
        val = _ItemStack()
        self.__wrapper = val

    @overload
    def getItem(self) -> 'Item':
        """public dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.ItemStack.getItem()"""
        return 'Item'._wrap(super(ItemStack, self).getItem())

    @overload
    def __init__(self, arg0: 'Item'):
        """public dev.ultreon.quantum.item.ItemStack(dev.ultreon.quantum.item.Item)"""
        val = _ItemStack(arg0)
        self.__wrapper = val

    @overload
    def transferTo(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.item.ItemStack.transferTo(dev.ultreon.quantum.item.ItemStack)"""
        return bool._wrap(super(_ItemStack, self).transferTo(arg0))

    @overload
    def isSameItem(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.item.ItemStack.isSameItem(dev.ultreon.quantum.item.ItemStack)"""
        return bool._wrap(super(_ItemStack, self).isSameItem(arg0))

    @overload
    def getCount(self) -> int:
        """public int dev.ultreon.quantum.item.ItemStack.getCount()"""
        return int._wrap(super(ItemStack, self).getCount())

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.item.ItemStack.isEmpty()"""
        return bool._wrap(super(ItemStack, self).isEmpty())

    @overload
    def getData(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.item.ItemStack.getData()"""
        return 'types.MapType'._wrap(super(ItemStack, self).getData())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def grow(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.item.ItemStack.grow(int)"""
        return int._wrap(super(_ItemStack, self).grow(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def deserialize(arg0: 'Json5Object') -> 'ItemStack':
        """public static dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.deserialize(de.marhali.json5.Json5Object)"""
        return ItemStack._wrap(_ItemStack.deserialize(arg0))

    @overload
    def setCount(self, arg0: int):
        """public void dev.ultreon.quantum.item.ItemStack.setCount(int)"""
        super(_ItemStack, self).setCount(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.item.BlockItem
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

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
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
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
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.item.BlockItem as _BlockItem
_BlockItem = _BlockItem
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockItem():
    """dev.ultreon.quantum.item.BlockItem"""
 
    @staticmethod
    def _wrap(java_value: _BlockItem) -> 'BlockItem':
        return BlockItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockItem):
        """
        Dynamic initializer for BlockItem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockItem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockItem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'._wrap(super(_Item, self).getDescription(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.BlockItem.getTranslationId()"""
        return str._wrap(super(BlockItem, self).getTranslationId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'Supplier'):
        """public dev.ultreon.quantum.item.BlockItem(dev.ultreon.quantum.item.Item$Properties,java.util.function.Supplier<dev.ultreon.quantum.block.Block>)"""
        val = _BlockItem(arg0, arg1)
        self.__wrapper = val

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float._wrap(super(_Item, self).getAttackDamage(arg0))

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
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.BlockItem.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'._wrap(super(_BlockItem, self).use(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.BlockItem.getTranslation()"""
        return 'text.TextObject'._wrap(super(BlockItem, self).getTranslation())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int._wrap(super(Item, self).getMaxStackSize())

    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.item.BlockItem.getBlock()"""
        return 'block.Block'._wrap(super(BlockItem, self).getBlock())

    @override
    @overload
    def defaultStack(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'ItemStack'._wrap(super(Item, self).defaultStack())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.item.BlockItem.createBlockMeta()"""
        return 'state.BlockProperties'._wrap(super(BlockItem, self).createBlockMeta())

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'._wrap(super(Item, self).getId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.item.UseItemContext
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.item.UseItemContext as _UseItemContext
_UseItemContext = _UseItemContext
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.util.HitResult as _HitResult
_HitResult = _HitResult
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.world.World as _World
_World = _World
from builtins import bool
import dev.ultreon.quantum.entity.player.Player as _Player
_Player = _Player
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UseItemContext():
    """dev.ultreon.quantum.item.UseItemContext"""
 
    @staticmethod
    def _wrap(java_value: _UseItemContext) -> 'UseItemContext':
        return UseItemContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UseItemContext):
        """
        Dynamic initializer for UseItemContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UseItemContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UseItemContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def stack(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.UseItemContext.stack()"""
        return 'ItemStack'._wrap(super(UseItemContext, self).stack())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.item.UseItemContext.equals(java.lang.Object)"""
        return bool._wrap(super(_UseItemContext, self).equals(arg0))

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
        """public java.lang.String dev.ultreon.quantum.item.UseItemContext.toString()"""
        return str._wrap(super(UseItemContext, self).toString())

    @overload
    def player(self) -> 'player.Player':
        """public dev.ultreon.quantum.entity.player.Player dev.ultreon.quantum.item.UseItemContext.player()"""
        return 'player.Player'._wrap(super(UseItemContext, self).player())

    @overload
    def __init__(self, arg0: 'World', arg1: 'Player', arg2: 'HitResult', arg3: 'ItemStack'):
        """public dev.ultreon.quantum.item.UseItemContext(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.util.HitResult,dev.ultreon.quantum.item.ItemStack)"""
        val = _UseItemContext(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def result(self) -> 'util.HitResult':
        """public dev.ultreon.quantum.util.HitResult dev.ultreon.quantum.item.UseItemContext.result()"""
        return 'util.HitResult'._wrap(super(UseItemContext, self).result())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.item.UseItemContext.hashCode()"""
        return int._wrap(super(UseItemContext, self).hashCode())

    @overload
    def world(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.item.UseItemContext.world()"""
        return 'world.World'._wrap(super(UseItemContext, self).world())

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
 
 
# CLASS: dev.ultreon.quantum.item.Item$Properties
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.item.Item as _Item_Properties
_Properties = _Item_Properties.Properties
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = _import_once("pyquantum.item.food")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Properties():
    """dev.ultreon.quantum.item.Item.Properties"""
 
    @staticmethod
    def _wrap(java_value: _Properties) -> 'Properties':
        return Properties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Properties):
        """
        Dynamic initializer for Properties.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Properties__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Properties__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def food(self, arg0: 'FoodData') -> 'Properties':
        """public dev.ultreon.quantum.item.Item$Properties dev.ultreon.quantum.item.Item$Properties.food(dev.ultreon.quantum.item.food.FoodData)"""
        return 'Properties'._wrap(super(_Properties, self).food(arg0))

    @overload
    def stackSize(self, arg0: int) -> 'Properties':
        """public dev.ultreon.quantum.item.Item$Properties dev.ultreon.quantum.item.Item$Properties.stackSize(int)"""
        return 'Properties'._wrap(super(_Properties, self).stackSize(_int.valueOf(arg0)))

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
    def rarity(self, arg0: 'ItemRarity') -> 'Properties':
        """public dev.ultreon.quantum.item.Item$Properties dev.ultreon.quantum.item.Item$Properties.rarity(dev.ultreon.quantum.item.ItemRarity)"""
        return 'Properties'._wrap(super(_Properties, self).rarity(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.item.Item$Properties()"""
        val = _Properties()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.item.Item$Properties()"""
        val = _Properties()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.item.ItemRarity
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.item.ItemRarity as _ItemRarity
_ItemRarity = _ItemRarity
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ItemRarity():
    """dev.ultreon.quantum.item.ItemRarity"""
 
    @staticmethod
    def _wrap(java_value: _ItemRarity) -> 'ItemRarity':
        return ItemRarity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemRarity):
        """
        Dynamic initializer for ItemRarity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemRarity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemRarity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def applyStyle(self, arg0: 'TextStyle'):
        """public void dev.ultreon.quantum.item.ItemRarity.applyStyle(dev.ultreon.quantum.text.TextStyle)"""
        super(_ItemRarity, self).applyStyle(arg0)

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
    def __init__(self, arg0: 'RgbColor', arg1: 'Identifier'):
        """public dev.ultreon.quantum.item.ItemRarity(dev.ultreon.quantum.util.RgbColor,dev.ultreon.quantum.util.Identifier)"""
        val = _ItemRarity(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'ColorCode', arg1: 'Identifier'):
        """public dev.ultreon.quantum.item.ItemRarity(dev.ultreon.quantum.text.ColorCode,dev.ultreon.quantum.util.Identifier)"""
        val = _ItemRarity(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ColorCode', arg1: str):
        """public dev.ultreon.quantum.item.ItemRarity(dev.ultreon.quantum.text.ColorCode,java.lang.String)"""
        val = _ItemRarity(arg0, arg1)
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.ItemRarity.getName()"""
        return str._wrap(super(ItemRarity, self).getName())

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


ItemRarity.EPIC = ItemRarity._wrap(_EPIC.EPIC)

ItemRarity.RARE = ItemRarity._wrap(_RARE.RARE)

ItemRarity.MYTHIC = ItemRarity._wrap(_MYTHIC.MYTHIC)

ItemRarity.GODLIKE = ItemRarity._wrap(_GODLIKE.GODLIKE)

ItemRarity.COMMON = ItemRarity._wrap(_COMMON.COMMON)

ItemRarity.LEGENDARY = ItemRarity._wrap(_LEGENDARY.LEGENDARY)

ItemRarity.UNCOMMON = ItemRarity._wrap(_UNCOMMON.UNCOMMON) 
 
 
# CLASS: dev.ultreon.quantum.item.Items
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

import dev.ultreon.quantum.item.Items as _Items
_Items = _Items
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Items():
    """dev.ultreon.quantum.item.Items"""
 
    @staticmethod
    def _wrap(java_value: _Items) -> 'Items':
        return Items(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Items):
        """
        Dynamic initializer for Items.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Items__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Items__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.META_SWITCH_TEST
    META_SWITCH_TEST: 'BlockItem' = _wrap(_BlockItem.META_SWITCH_TEST)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.SANDSTONE
    SANDSTONE: 'BlockItem' = _wrap(_BlockItem.SANDSTONE)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.BACON
    BACON: 'Item' = _wrap(_Item.BACON)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.PLANKS_SLAB
    PLANKS_SLAB: 'BlockItem' = _wrap(_BlockItem.PLANKS_SLAB)

    # public static final dev.ultreon.quantum.item.tool.AxeItem dev.ultreon.quantum.item.Items.WOODEN_AXE
    WOODEN_AXE: 'tool.AxeItem' = _wrap(_tool.AxeItem.WOODEN_AXE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.COBBLESTONE
    COBBLESTONE: 'BlockItem' = _wrap(_BlockItem.COBBLESTONE)

    # public static final dev.ultreon.quantum.item.tool.AxeItem dev.ultreon.quantum.item.Items.STONE_AXE
    STONE_AXE: 'tool.AxeItem' = _wrap(_tool.AxeItem.STONE_AXE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.GRAVEL
    GRAVEL: 'BlockItem' = _wrap(_BlockItem.GRAVEL)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.PLANK
    PLANK: 'Item' = _wrap(_Item.PLANK)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.CACTUS
    CACTUS: 'BlockItem' = _wrap(_BlockItem.CACTUS)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.WATER
    WATER: 'BlockItem' = _wrap(_BlockItem.WATER)

    # public static final dev.ultreon.quantum.item.tool.ShovelItem dev.ultreon.quantum.item.Items.STONE_SHOVEL
    STONE_SHOVEL: 'tool.ShovelItem' = _wrap(_tool.ShovelItem.STONE_SHOVEL)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.IRON_INGOT
    IRON_INGOT: 'Item' = _wrap(_Item.IRON_INGOT)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.RAW_IRON
    RAW_IRON: 'Item' = _wrap(_Item.RAW_IRON)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.LOG
    LOG: 'BlockItem' = _wrap(_BlockItem.LOG)

    # public static final dev.ultreon.quantum.item.tool.ShovelItem dev.ultreon.quantum.item.Items.WOODEN_SHOVEL
    WOODEN_SHOVEL: 'tool.ShovelItem' = _wrap(_tool.ShovelItem.WOODEN_SHOVEL)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.DIRT
    DIRT: 'BlockItem' = _wrap(_BlockItem.DIRT)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.SAND
    SAND: 'BlockItem' = _wrap(_BlockItem.SAND)

    # public static final dev.ultreon.quantum.item.tool.PickaxeItem dev.ultreon.quantum.item.Items.WOODEN_PICKAXE
    WOODEN_PICKAXE: 'tool.PickaxeItem' = _wrap(_tool.PickaxeItem.WOODEN_PICKAXE)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.AIR
    AIR: 'Item' = _wrap(_Item.AIR)

    # public static final dev.ultreon.quantum.item.tool.PickaxeItem dev.ultreon.quantum.item.Items.STONE_PICKAXE
    STONE_PICKAXE: 'tool.PickaxeItem' = _wrap(_tool.PickaxeItem.STONE_PICKAXE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.IRON_ORE
    IRON_ORE: 'BlockItem' = _wrap(_BlockItem.IRON_ORE)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.RAW_BACON
    RAW_BACON: 'Item' = _wrap(_Item.RAW_BACON)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.GRASS_BLOCK
    GRASS_BLOCK: 'BlockItem' = _wrap(_BlockItem.GRASS_BLOCK)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.ROCK
    ROCK: 'Item' = _wrap(_Item.ROCK)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.BLAST_FURNACE
    BLAST_FURNACE: 'BlockItem' = _wrap(_BlockItem.BLAST_FURNACE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.PLANKS
    PLANKS: 'BlockItem' = _wrap(_BlockItem.PLANKS)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.CRATE
    CRATE: 'BlockItem' = _wrap(_BlockItem.CRATE)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.GRASS_FIBRE
    GRASS_FIBRE: 'Item' = _wrap(_Item.GRASS_FIBRE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.STONE
    STONE: 'BlockItem' = _wrap(_BlockItem.STONE)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.STICK
    STICK: 'Item' = _wrap(_Item.STICK)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.CRAFTING_BENCH
    CRAFTING_BENCH: 'BlockItem' = _wrap(_BlockItem.CRAFTING_BENCH)


    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.item.Items.init()"""
            _Items.init()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.item.Items()"""
        val = _Items()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.item.Items()"""
        val = _Items()
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