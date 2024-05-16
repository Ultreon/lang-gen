from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class Item():
    """dev.ultreon.quantum.item.Item"""
 
    @staticmethod
    def __wrap(java_value: __Item) -> 'Item':
        return Item(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Item):
        """
        Dynamic initializer for Item.
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
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'.__wrap(super(Item, self).getId())

    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int.__wrap(super(Item, self).getMaxStackSize())

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
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str.__wrap(super(Item, self).getTranslationId())

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float.__wrap(super(__Item, self).getAttackDamage(arg0))

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
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'.__wrap(super(__Item, self).use(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.item.Item(dev.ultreon.quantum.item.Item$Properties)"""
        val = __Item(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Item, self).getTranslation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'.__wrap(super(__Item, self).getDescription(arg0))

    @overload
    def defaultStack(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'ItemStack'.__wrap(super(Item, self).defaultStack())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.item.Item
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class Item():
    """dev.ultreon.quantum.item.Item"""
 
    @staticmethod
    def __wrap(java_value: __Item) -> 'Item':
        return Item(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Item):
        """
        Dynamic initializer for Item.
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
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'.__wrap(super(Item, self).getId())

    @overload
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int.__wrap(super(Item, self).getMaxStackSize())

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
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.Item.getTranslationId()"""
        return str.__wrap(super(Item, self).getTranslationId())

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float.__wrap(super(__Item, self).getAttackDamage(arg0))

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
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.Item.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'.__wrap(super(__Item, self).use(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.item.Item(dev.ultreon.quantum.item.Item$Properties)"""
        val = __Item(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.Item.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Item, self).getTranslation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'.__wrap(super(__Item, self).getDescription(arg0))

    @overload
    def defaultStack(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'ItemStack'.__wrap(super(Item, self).defaultStack())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.item.Item 
 
 
# CLASS: dev.ultreon.quantum.item.ItemStack
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import de.marhali.json5.Json5Object as Json5Object
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
import java.lang.Integer as __int
from builtins import bool
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.util.List as List
 
class ItemStack():
    """dev.ultreon.quantum.item.ItemStack"""
 
    @staticmethod
    def __wrap(java_value: __ItemStack) -> 'ItemStack':
        return ItemStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemStack):
        """
        Dynamic initializer for ItemStack.
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
        """public java.lang.String dev.ultreon.quantum.item.ItemStack.toString()"""
        return str.__wrap(super(ItemStack, self).toString())

    @overload
    def getItem(self) -> 'Item':
        """public dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.ItemStack.getItem()"""
        return 'Item'.__wrap(super(ItemStack, self).getItem())

    @overload
    def getAttackDamage(self) -> float:
        """public float dev.ultreon.quantum.item.ItemStack.getAttackDamage()"""
        return float.__wrap(super(ItemStack, self).getAttackDamage())

    @staticmethod
    @overload
    def deserialize(arg0: 'Json5Object') -> 'ItemStack':
        """public static dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.deserialize(de.marhali.json5.Json5Object)"""
        return ItemStack.__wrap(__ItemStack.deserialize(arg0))

    @overload
    def __init__(self, arg0: 'Item'):
        """public dev.ultreon.quantum.item.ItemStack(dev.ultreon.quantum.item.Item)"""
        val = __ItemStack(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def shrink(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.item.ItemStack.shrink(int)"""
        return int.__wrap(super(__ItemStack, self).shrink(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.item.ItemStack()"""
        val = __ItemStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'ItemStack':
        """public static dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.load(dev.ultreon.ubo.types.MapType)"""
        return ItemStack.__wrap(__ItemStack.load(arg0))

    @staticmethod
    @overload
    def empty() -> 'ItemStack':
        """public static dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.empty()"""
        return ItemStack.__wrap(__ItemStack.empty())

    @overload
    def getData(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.item.ItemStack.getData()"""
        return 'types.MapType'.__wrap(super(ItemStack, self).getData())

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.item.ItemStack.isEmpty()"""
        return bool.__wrap(super(ItemStack, self).isEmpty())

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
    def transferTo(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.item.ItemStack.transferTo(dev.ultreon.quantum.item.ItemStack)"""
        return bool.__wrap(super(__ItemStack, self).transferTo(arg0))

    @overload
    def sameItemSameData(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.item.ItemStack.sameItemSameData(dev.ultreon.quantum.item.ItemStack)"""
        return bool.__wrap(super(__ItemStack, self).sameItemSameData(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.item.ItemStack()"""
        val = __ItemStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getDescription(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.ItemStack.getDescription()"""
        return 'List'.__wrap(super(ItemStack, self).getDescription())

    @overload
    def setCount(self, arg0: int):
        """public void dev.ultreon.quantum.item.ItemStack.setCount(int)"""
        super(__ItemStack, self).setCount(__int.valueOf(arg0))

    @overload
    def setData(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.item.ItemStack.setData(dev.ultreon.ubo.types.MapType)"""
        super(__ItemStack, self).setData(arg0)

    @overload
    def merge(self, arg0: 'ItemStack') -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.merge(dev.ultreon.quantum.item.ItemStack)"""
        return 'ItemStack'.__wrap(super(__ItemStack, self).merge(arg0))

    @overload
    def split(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.split()"""
        return 'ItemStack'.__wrap(super(ItemStack, self).split())

    @overload
    def copy(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.copy()"""
        return 'ItemStack'.__wrap(super(ItemStack, self).copy())

    @overload
    def grow(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.item.ItemStack.grow(int)"""
        return int.__wrap(super(__ItemStack, self).grow(__int.valueOf(arg0)))

    @overload
    def isSameItem(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.item.ItemStack.isSameItem(dev.ultreon.quantum.item.ItemStack)"""
        return bool.__wrap(super(__ItemStack, self).isSameItem(arg0))

    @overload
    def split(self, arg0: int) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.ItemStack.split(int)"""
        return 'ItemStack'.__wrap(super(__ItemStack, self).split(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Item', arg1: int, arg2: 'MapType'):
        """public dev.ultreon.quantum.item.ItemStack(dev.ultreon.quantum.item.Item,int,dev.ultreon.ubo.types.MapType)"""
        val = __ItemStack(arg0, __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.item.ItemStack.save()"""
        return 'types.MapType'.__wrap(super(ItemStack, self).save())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def transferTo(self, arg0: 'ItemStack', arg1: int) -> int:
        """public int dev.ultreon.quantum.item.ItemStack.transferTo(dev.ultreon.quantum.item.ItemStack,int)"""
        return int.__wrap(super(__ItemStack, self).transferTo(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Item', arg1: int):
        """public dev.ultreon.quantum.item.ItemStack(dev.ultreon.quantum.item.Item,int)"""
        val = __ItemStack(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCount(self) -> int:
        """public int dev.ultreon.quantum.item.ItemStack.getCount()"""
        return int.__wrap(super(ItemStack, self).getCount()) 
 
 
# CLASS: dev.ultreon.quantum.item.BlockItem
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.item.BlockItem as __BlockItem
__BlockItem = __BlockItem
from builtins import float
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
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class BlockItem():
    """dev.ultreon.quantum.item.BlockItem"""
 
    @staticmethod
    def __wrap(java_value: __BlockItem) -> 'BlockItem':
        return BlockItem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockItem):
        """
        Dynamic initializer for BlockItem.
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
    def getMaxStackSize(self) -> int:
        """public int dev.ultreon.quantum.item.Item.getMaxStackSize()"""
        return int.__wrap(super(Item, self).getMaxStackSize())

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
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.item.BlockItem.getTranslation()"""
        return 'text.TextObject'.__wrap(super(BlockItem, self).getTranslation())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.item.BlockItem.getBlock()"""
        return 'block.Block'.__wrap(super(BlockItem, self).getBlock())

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.item.Item.getId()"""
        return 'util.Identifier'.__wrap(super(Item, self).getId())

    @overload
    def getAttackDamage(self, arg0: 'ItemStack') -> float:
        """public float dev.ultreon.quantum.item.Item.getAttackDamage(dev.ultreon.quantum.item.ItemStack)"""
        return float.__wrap(super(__Item, self).getAttackDamage(arg0))

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
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.BlockItem.getTranslationId()"""
        return str.__wrap(super(BlockItem, self).getTranslationId())

    @override
    @overload
    def defaultStack(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.Item.defaultStack()"""
        return 'ItemStack'.__wrap(super(Item, self).defaultStack())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def use(self, arg0: 'UseItemContext') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.item.BlockItem.use(dev.ultreon.quantum.item.UseItemContext)"""
        return 'world.UseResult'.__wrap(super(__BlockItem, self).use(arg0))

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
    def createBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.item.BlockItem.createBlockMeta()"""
        return 'state.BlockProperties'.__wrap(super(BlockItem, self).createBlockMeta())

    @overload
    def getDescription(self, arg0: 'ItemStack') -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.item.Item.getDescription(dev.ultreon.quantum.item.ItemStack)"""
        return 'List'.__wrap(super(__Item, self).getDescription(arg0))

    @overload
    def __init__(self, arg0: 'Properties', arg1: 'Supplier'):
        """public dev.ultreon.quantum.item.BlockItem(dev.ultreon.quantum.item.Item$Properties,java.util.function.Supplier<dev.ultreon.quantum.block.Block>)"""
        val = __BlockItem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.item.UseItemContext
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.item.UseItemContext as __UseItemContext
__UseItemContext = __UseItemContext
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
import dev.ultreon.quantum.entity.player.Player as __Player
__Player = __Player
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.util.HitResult as __HitResult
__HitResult = __HitResult
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UseItemContext():
    """dev.ultreon.quantum.item.UseItemContext"""
 
    @staticmethod
    def __wrap(java_value: __UseItemContext) -> 'UseItemContext':
        return UseItemContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UseItemContext):
        """
        Dynamic initializer for UseItemContext.
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
        """public java.lang.String dev.ultreon.quantum.item.UseItemContext.toString()"""
        return str.__wrap(super(UseItemContext, self).toString())

    @overload
    def world(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.item.UseItemContext.world()"""
        return 'world.World'.__wrap(super(UseItemContext, self).world())

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
    def __init__(self, arg0: 'World', arg1: 'Player', arg2: 'HitResult', arg3: 'ItemStack'):
        """public dev.ultreon.quantum.item.UseItemContext(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.util.HitResult,dev.ultreon.quantum.item.ItemStack)"""
        val = __UseItemContext(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.item.UseItemContext.equals(java.lang.Object)"""
        return bool.__wrap(super(__UseItemContext, self).equals(arg0))

    @overload
    def result(self) -> 'util.HitResult':
        """public dev.ultreon.quantum.util.HitResult dev.ultreon.quantum.item.UseItemContext.result()"""
        return 'util.HitResult'.__wrap(super(UseItemContext, self).result())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.item.UseItemContext.hashCode()"""
        return int.__wrap(super(UseItemContext, self).hashCode())

    @overload
    def stack(self) -> 'ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.item.UseItemContext.stack()"""
        return 'ItemStack'.__wrap(super(UseItemContext, self).stack())

    @overload
    def player(self) -> 'player.Player':
        """public dev.ultreon.quantum.entity.player.Player dev.ultreon.quantum.item.UseItemContext.player()"""
        return 'player.Player'.__wrap(super(UseItemContext, self).player()) 
 
 
# CLASS: dev.ultreon.quantum.item.Item$Properties
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.item import food
except ImportError:
    food = __import_once__("pyquantum.item.food")

import dev.ultreon.quantum.item.Item as __Item_Properties
__Properties = __Item_Properties.Properties
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Properties():
    """dev.ultreon.quantum.item.Item.Properties"""
 
    @staticmethod
    def __wrap(java_value: __Properties) -> 'Properties':
        return Properties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Properties):
        """
        Dynamic initializer for Properties.
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
    def food(self, arg0: 'FoodData') -> 'Properties':
        """public dev.ultreon.quantum.item.Item$Properties dev.ultreon.quantum.item.Item$Properties.food(dev.ultreon.quantum.item.food.FoodData)"""
        return 'Properties'.__wrap(super(__Properties, self).food(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.item.Item$Properties()"""
        val = __Properties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.item.Item$Properties()"""
        val = __Properties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def rarity(self, arg0: 'ItemRarity') -> 'Properties':
        """public dev.ultreon.quantum.item.Item$Properties dev.ultreon.quantum.item.Item$Properties.rarity(dev.ultreon.quantum.item.ItemRarity)"""
        return 'Properties'.__wrap(super(__Properties, self).rarity(arg0))

    @overload
    def stackSize(self, arg0: int) -> 'Properties':
        """public dev.ultreon.quantum.item.Item$Properties dev.ultreon.quantum.item.Item$Properties.stackSize(int)"""
        return 'Properties'.__wrap(super(__Properties, self).stackSize(__int.valueOf(arg0)))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.item.ItemRarity
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.item.ItemRarity as __ItemRarity
__ItemRarity = __ItemRarity
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
 
class ItemRarity():
    """dev.ultreon.quantum.item.ItemRarity"""
 
    @staticmethod
    def __wrap(java_value: __ItemRarity) -> 'ItemRarity':
        return ItemRarity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemRarity):
        """
        Dynamic initializer for ItemRarity.
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
 
    # public static final dev.ultreon.quantum.item.ItemRarity dev.ultreon.quantum.item.ItemRarity.EPIC
    EPIC: 'ItemRarity' = __wrap(__ItemRarity.EPIC)

    # public static final dev.ultreon.quantum.item.ItemRarity dev.ultreon.quantum.item.ItemRarity.RARE
    RARE: 'ItemRarity' = __wrap(__ItemRarity.RARE)

    # public static final dev.ultreon.quantum.item.ItemRarity dev.ultreon.quantum.item.ItemRarity.LEGENDARY
    LEGENDARY: 'ItemRarity' = __wrap(__ItemRarity.LEGENDARY)

    # public static final dev.ultreon.quantum.item.ItemRarity dev.ultreon.quantum.item.ItemRarity.COMMON
    COMMON: 'ItemRarity' = __wrap(__ItemRarity.COMMON)

    # public static final dev.ultreon.quantum.item.ItemRarity dev.ultreon.quantum.item.ItemRarity.MYTHIC
    MYTHIC: 'ItemRarity' = __wrap(__ItemRarity.MYTHIC)

    # public static final dev.ultreon.quantum.item.ItemRarity dev.ultreon.quantum.item.ItemRarity.UNCOMMON
    UNCOMMON: 'ItemRarity' = __wrap(__ItemRarity.UNCOMMON)

    # public static final dev.ultreon.quantum.item.ItemRarity dev.ultreon.quantum.item.ItemRarity.GODLIKE
    GODLIKE: 'ItemRarity' = __wrap(__ItemRarity.GODLIKE)


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
    def __init__(self, arg0: 'ColorCode', arg1: str):
        """public dev.ultreon.quantum.item.ItemRarity(dev.ultreon.quantum.text.ColorCode,java.lang.String)"""
        val = __ItemRarity(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.item.ItemRarity.getName()"""
        return str.__wrap(super(ItemRarity, self).getName())

    @overload
    def applyStyle(self, arg0: 'TextStyle'):
        """public void dev.ultreon.quantum.item.ItemRarity.applyStyle(dev.ultreon.quantum.text.TextStyle)"""
        super(__ItemRarity, self).applyStyle(arg0)

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
    def __init__(self, arg0: 'RgbColor', arg1: 'Identifier'):
        """public dev.ultreon.quantum.item.ItemRarity(dev.ultreon.quantum.util.RgbColor,dev.ultreon.quantum.util.Identifier)"""
        val = __ItemRarity(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'ColorCode', arg1: 'Identifier'):
        """public dev.ultreon.quantum.item.ItemRarity(dev.ultreon.quantum.text.ColorCode,dev.ultreon.quantum.util.Identifier)"""
        val = __ItemRarity(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.item.Items
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.item.Items as __Items
__Items = __Items
import java.lang.String as __String
__String = __String
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Items():
    """dev.ultreon.quantum.item.Items"""
 
    @staticmethod
    def __wrap(java_value: __Items) -> 'Items':
        return Items(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Items):
        """
        Dynamic initializer for Items.
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
 
    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.PLANKS_SLAB
    PLANKS_SLAB: 'BlockItem' = __wrap(__BlockItem.PLANKS_SLAB)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.PLANKS
    PLANKS: 'BlockItem' = __wrap(__BlockItem.PLANKS)

    # public static final dev.ultreon.quantum.item.tool.AxeItem dev.ultreon.quantum.item.Items.WOODEN_AXE
    WOODEN_AXE: 'tool.AxeItem' = __wrap(__tool.AxeItem.WOODEN_AXE)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.PLANK
    PLANK: 'Item' = __wrap(__Item.PLANK)

    # public static final dev.ultreon.quantum.item.tool.ShovelItem dev.ultreon.quantum.item.Items.STONE_SHOVEL
    STONE_SHOVEL: 'tool.ShovelItem' = __wrap(__tool.ShovelItem.STONE_SHOVEL)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.RAW_BACON
    RAW_BACON: 'Item' = __wrap(__Item.RAW_BACON)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.GRASS_FIBRE
    GRASS_FIBRE: 'Item' = __wrap(__Item.GRASS_FIBRE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.SAND
    SAND: 'BlockItem' = __wrap(__BlockItem.SAND)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.META_SWITCH_TEST
    META_SWITCH_TEST: 'BlockItem' = __wrap(__BlockItem.META_SWITCH_TEST)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.IRON_ORE
    IRON_ORE: 'BlockItem' = __wrap(__BlockItem.IRON_ORE)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.AIR
    AIR: 'Item' = __wrap(__Item.AIR)

    # public static final dev.ultreon.quantum.item.tool.ShovelItem dev.ultreon.quantum.item.Items.WOODEN_SHOVEL
    WOODEN_SHOVEL: 'tool.ShovelItem' = __wrap(__tool.ShovelItem.WOODEN_SHOVEL)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.IRON_INGOT
    IRON_INGOT: 'Item' = __wrap(__Item.IRON_INGOT)

    # public static final dev.ultreon.quantum.item.tool.PickaxeItem dev.ultreon.quantum.item.Items.WOODEN_PICKAXE
    WOODEN_PICKAXE: 'tool.PickaxeItem' = __wrap(__tool.PickaxeItem.WOODEN_PICKAXE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.STONE
    STONE: 'BlockItem' = __wrap(__BlockItem.STONE)

    # public static final dev.ultreon.quantum.item.tool.AxeItem dev.ultreon.quantum.item.Items.STONE_AXE
    STONE_AXE: 'tool.AxeItem' = __wrap(__tool.AxeItem.STONE_AXE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.COBBLESTONE
    COBBLESTONE: 'BlockItem' = __wrap(__BlockItem.COBBLESTONE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.SANDSTONE
    SANDSTONE: 'BlockItem' = __wrap(__BlockItem.SANDSTONE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.CRAFTING_BENCH
    CRAFTING_BENCH: 'BlockItem' = __wrap(__BlockItem.CRAFTING_BENCH)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.DIRT
    DIRT: 'BlockItem' = __wrap(__BlockItem.DIRT)

    # public static final dev.ultreon.quantum.item.tool.PickaxeItem dev.ultreon.quantum.item.Items.STONE_PICKAXE
    STONE_PICKAXE: 'tool.PickaxeItem' = __wrap(__tool.PickaxeItem.STONE_PICKAXE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.GRASS_BLOCK
    GRASS_BLOCK: 'BlockItem' = __wrap(__BlockItem.GRASS_BLOCK)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.ROCK
    ROCK: 'Item' = __wrap(__Item.ROCK)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.BLAST_FURNACE
    BLAST_FURNACE: 'BlockItem' = __wrap(__BlockItem.BLAST_FURNACE)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.GRAVEL
    GRAVEL: 'BlockItem' = __wrap(__BlockItem.GRAVEL)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.LOG
    LOG: 'BlockItem' = __wrap(__BlockItem.LOG)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.WATER
    WATER: 'BlockItem' = __wrap(__BlockItem.WATER)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.CACTUS
    CACTUS: 'BlockItem' = __wrap(__BlockItem.CACTUS)

    # public static final dev.ultreon.quantum.item.BlockItem dev.ultreon.quantum.item.Items.CRATE
    CRATE: 'BlockItem' = __wrap(__BlockItem.CRATE)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.RAW_IRON
    RAW_IRON: 'Item' = __wrap(__Item.RAW_IRON)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.BACON
    BACON: 'Item' = __wrap(__Item.BACON)

    # public static final dev.ultreon.quantum.item.Item dev.ultreon.quantum.item.Items.STICK
    STICK: 'Item' = __wrap(__Item.STICK)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.item.Items()"""
        val = __Items()
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
    def __init__(self):
        """public dev.ultreon.quantum.item.Items()"""
        val = __Items()
        self.__dict__ = val.__dict__
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.item.Items.init()"""
            __Items.init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))