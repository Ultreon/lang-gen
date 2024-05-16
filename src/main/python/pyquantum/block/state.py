from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from builtins import object
import dev.ultreon.quantum.block.state.BlockDataEntry as _BlockDataEntry
_BlockDataEntry = _BlockDataEntry
import java.lang.Enum as Enum
import java.lang.Boolean as _boolean
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import de.marhali.json5.Json5Object as Json5Object
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class BlockDataEntry():
    """dev.ultreon.quantum.block.state.BlockDataEntry"""
 
    @staticmethod
    def _wrap(java_value: _BlockDataEntry) -> 'BlockDataEntry':
        return BlockDataEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockDataEntry):
        """
        Dynamic initializer for BlockDataEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockDataEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockDataEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ofEnum(arg0: 'Enum') -> 'BlockDataEntry':
        """public static <T extends java.lang.Enum<T>> dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.ofEnum(T)"""
        return BlockDataEntry._wrap(_BlockDataEntry.ofEnum(arg0))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int) -> 'BlockDataEntry':
        """public static dev.ultreon.quantum.block.state.BlockDataEntry<java.lang.Integer> dev.ultreon.quantum.block.state.BlockDataEntry.of(int,int,int)"""
        return BlockDataEntry._wrap(_BlockDataEntry.of(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @abstractmethod
    def read(self, arg0: 'PacketIO'):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockDataEntry.read(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @abstractmethod
    def write(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.block.state.BlockDataEntry.write(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @abstractmethod
    def parse(self, arg0: 'Json5Object'):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockDataEntry.parse(de.marhali.json5.Json5Object)"""
        pass

    @overload
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.block.state.BlockDataEntry(T)"""
        val = _BlockDataEntry(arg0)
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

    @abstractmethod
    def with(self, arg0: object):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.with(T)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.state.BlockDataEntry.toString()"""
        return str._wrap(super(BlockDataEntry, self).toString())

    @abstractmethod
    def load(self, arg0: 'DataType'):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockDataEntry.load(dev.ultreon.ubo.types.DataType<?>)"""
        pass

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
    def of(arg0: bool) -> 'BlockDataEntry':
        """public static dev.ultreon.quantum.block.state.BlockDataEntry<java.lang.Boolean> dev.ultreon.quantum.block.state.BlockDataEntry.of(boolean)"""
        return BlockDataEntry._wrap(_BlockDataEntry.of(_boolean.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.block.state.BlockDataEntry.hashCode()"""
        return int._wrap(super(BlockDataEntry, self).hashCode())

    @overload
    def cast(self, arg0: 'Class') -> 'BlockDataEntry':
        """public <R> dev.ultreon.quantum.block.state.BlockDataEntry<R> dev.ultreon.quantum.block.state.BlockDataEntry.cast(java.lang.Class<R>)"""
        return 'BlockDataEntry'._wrap(super(_BlockDataEntry, self).cast(arg0))

    @abstractmethod
    def save(self, ):
        """public abstract dev.ultreon.ubo.types.DataType<?> dev.ultreon.quantum.block.state.BlockDataEntry.save()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def map(self, arg0: 'Function') -> 'BlockDataEntry':
        """public dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.map(java.util.function.Function<T, T>)"""
        return 'BlockDataEntry'._wrap(super(_BlockDataEntry, self).map(arg0))

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.block.state.BlockDataEntry.getValue()"""
        return object._wrap(super(BlockDataEntry, self).getValue())

    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockDataEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_BlockDataEntry, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.block.state.BlockDataEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from builtins import object
import dev.ultreon.quantum.block.state.BlockDataEntry as _BlockDataEntry
_BlockDataEntry = _BlockDataEntry
import java.lang.Enum as Enum
import java.lang.Boolean as _boolean
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import de.marhali.json5.Json5Object as Json5Object
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class BlockDataEntry():
    """dev.ultreon.quantum.block.state.BlockDataEntry"""
 
    @staticmethod
    def _wrap(java_value: _BlockDataEntry) -> 'BlockDataEntry':
        return BlockDataEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockDataEntry):
        """
        Dynamic initializer for BlockDataEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockDataEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockDataEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ofEnum(arg0: 'Enum') -> 'BlockDataEntry':
        """public static <T extends java.lang.Enum<T>> dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.ofEnum(T)"""
        return BlockDataEntry._wrap(_BlockDataEntry.ofEnum(arg0))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int) -> 'BlockDataEntry':
        """public static dev.ultreon.quantum.block.state.BlockDataEntry<java.lang.Integer> dev.ultreon.quantum.block.state.BlockDataEntry.of(int,int,int)"""
        return BlockDataEntry._wrap(_BlockDataEntry.of(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @abstractmethod
    def read(self, arg0: 'PacketIO'):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockDataEntry.read(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @abstractmethod
    def write(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.block.state.BlockDataEntry.write(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @abstractmethod
    def parse(self, arg0: 'Json5Object'):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockDataEntry.parse(de.marhali.json5.Json5Object)"""
        pass

    @overload
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.block.state.BlockDataEntry(T)"""
        val = _BlockDataEntry(arg0)
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

    @abstractmethod
    def with(self, arg0: object):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.with(T)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.state.BlockDataEntry.toString()"""
        return str._wrap(super(BlockDataEntry, self).toString())

    @abstractmethod
    def load(self, arg0: 'DataType'):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockDataEntry.load(dev.ultreon.ubo.types.DataType<?>)"""
        pass

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
    def of(arg0: bool) -> 'BlockDataEntry':
        """public static dev.ultreon.quantum.block.state.BlockDataEntry<java.lang.Boolean> dev.ultreon.quantum.block.state.BlockDataEntry.of(boolean)"""
        return BlockDataEntry._wrap(_BlockDataEntry.of(_boolean.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.block.state.BlockDataEntry.hashCode()"""
        return int._wrap(super(BlockDataEntry, self).hashCode())

    @overload
    def cast(self, arg0: 'Class') -> 'BlockDataEntry':
        """public <R> dev.ultreon.quantum.block.state.BlockDataEntry<R> dev.ultreon.quantum.block.state.BlockDataEntry.cast(java.lang.Class<R>)"""
        return 'BlockDataEntry'._wrap(super(_BlockDataEntry, self).cast(arg0))

    @abstractmethod
    def save(self, ):
        """public abstract dev.ultreon.ubo.types.DataType<?> dev.ultreon.quantum.block.state.BlockDataEntry.save()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def map(self, arg0: 'Function') -> 'BlockDataEntry':
        """public dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.map(java.util.function.Function<T, T>)"""
        return 'BlockDataEntry'._wrap(super(_BlockDataEntry, self).map(arg0))

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.block.state.BlockDataEntry.getValue()"""
        return object._wrap(super(BlockDataEntry, self).getValue())

    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockDataEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_BlockDataEntry, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.block.state.BlockDataEntry 
 
 
# CLASS: dev.ultreon.quantum.block.state.BlockProperties
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _string
try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.state.BlockDataEntry as _BlockDataEntry
_BlockDataEntry = _BlockDataEntry
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class BlockProperties():
    """dev.ultreon.quantum.block.state.BlockProperties"""
 
    @staticmethod
    def _wrap(java_value: _BlockProperties) -> 'BlockProperties':
        return BlockProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockProperties):
        """
        Dynamic initializer for BlockProperties.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockProperties__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockProperties__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player'):
        """public void dev.ultreon.quantum.block.state.BlockProperties.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(_BlockProperties, self).onDestroy(arg0, arg1, arg2)

    @overload
    def getProperty(self, arg0: str, *arg1: object) -> 'BlockDataEntry':
        """public final <T> dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockProperties.getProperty(java.lang.String,T...)"""
        return 'BlockDataEntry'._wrap(super(_BlockProperties, self).getProperty(arg0, arg1))

    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isAir()"""
        return bool._wrap(super(BlockProperties, self).isAir())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.block.state.BlockProperties.hashCode()"""
        return int._wrap(super(BlockProperties, self).hashCode())

    @overload
    def setEntry(self, arg0: str, arg1: 'BlockDataEntry'):
        """public void dev.ultreon.quantum.block.state.BlockProperties.setEntry(java.lang.String,dev.ultreon.quantum.block.state.BlockDataEntry<?>)"""
        super(_BlockProperties, self).setEntry(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.state.BlockProperties.save()"""
        return 'types.MapType'._wrap(super(BlockProperties, self).save())

    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isReplaceable()"""
        return bool._wrap(super(BlockProperties, self).isReplaceable())

    @overload
    def get(self, arg0: str, *arg1: object) -> object:
        """public final <T> T dev.ultreon.quantum.block.state.BlockProperties.get(java.lang.String,T...)"""
        return object._wrap(super(_BlockProperties, self).get(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def withEntry(self, arg0: str, arg1: object) -> 'BlockProperties':
        """public <T> dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.withEntry(java.lang.String,T)"""
        return 'BlockProperties'._wrap(super(_BlockProperties, self).withEntry(arg0, arg1))

    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isFluid()"""
        return bool._wrap(super(BlockProperties, self).isFluid())

    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isToolRequired()"""
        return bool._wrap(super(BlockProperties, self).isToolRequired())

    @overload
    def is(self, arg0: 'Block') -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.is(dev.ultreon.quantum.block.Block)"""
        return bool._wrap(super(_BlockProperties, self).is(arg0))

    @overload
    def hasEntry(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.hasEntry(java.lang.String)"""
        return bool._wrap(super(_BlockProperties, self).hasEntry(arg0))

    @overload
    def write(self, arg0: 'PacketIO') -> int:
        """public int dev.ultreon.quantum.block.state.BlockProperties.write(dev.ultreon.quantum.network.PacketIO)"""
        return int._wrap(super(_BlockProperties, self).write(arg0))

    @overload
    def withEntry(self, arg0: str, arg1: 'BlockDataEntry') -> 'BlockProperties':
        """public <T> dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.withEntry(java.lang.String,dev.ultreon.quantum.block.state.BlockDataEntry<T>)"""
        return 'BlockProperties'._wrap(super(_BlockProperties, self).withEntry(arg0, arg1))

    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.state.BlockProperties.getBlock()"""
        return 'block.Block'._wrap(super(BlockProperties, self).getBlock())

    @overload
    def onPlace(self, arg0: 'ServerWorld', arg1: 'BlockPos'):
        """public void dev.ultreon.quantum.block.state.BlockProperties.onPlace(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.BlockPos)"""
        super(_BlockProperties, self).onPlace(arg0, arg1)

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.load(dev.ultreon.ubo.types.MapType)"""
        return BlockProperties._wrap(_BlockProperties.load(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.state.BlockProperties.toString()"""
        return str._wrap(super(BlockProperties, self).toString())

    @overload
    def __init__(self, arg0: 'Block', arg1: 'Map'):
        """public dev.ultreon.quantum.block.state.BlockProperties(dev.ultreon.quantum.block.Block,java.util.Map<java.lang.String, dev.ultreon.quantum.block.state.BlockDataEntry<?>>)"""
        val = _BlockProperties(arg0, arg1)
        self.__wrapper = val

    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.hasCollider()"""
        return bool._wrap(super(BlockProperties, self).hasCollider())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.state.BlockProperties.getBoundingBox(int,int,int)"""
        return 'util.BoundingBox'._wrap(super(_BlockProperties, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.state.BlockProperties.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(BlockProperties, self).getEffectiveTool())

    @overload
    def getEntryUnsafe(self, arg0: str) -> 'BlockDataEntry':
        """public final dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockProperties.getEntryUnsafe(java.lang.String)"""
        return 'BlockDataEntry'._wrap(super(_BlockProperties, self).getEntryUnsafe(arg0))

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext') -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext)"""
        return bool._wrap(super(_BlockProperties, self).canBeReplacedBy(arg0))

    @staticmethod
    @overload
    def read(arg0: 'PacketIO') -> 'BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.read(dev.ultreon.quantum.network.PacketIO)"""
        return BlockProperties._wrap(_BlockProperties.read(arg0))

    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isTransparent()"""
        return bool._wrap(super(BlockProperties, self).isTransparent())

    @overload
    def getEntries(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.block.state.BlockDataEntry<?>> dev.ultreon.quantum.block.state.BlockProperties.getEntries()"""
        return 'Map'._wrap(super(BlockProperties, self).getEntries())

    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos'):
        """public void dev.ultreon.quantum.block.state.BlockProperties.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        super(_BlockProperties, self).update(arg0, arg1)

    @overload
    def isWater(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isWater()"""
        return bool._wrap(super(BlockProperties, self).isWater())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getLootGen(self) -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.state.BlockProperties.getLootGen()"""
        return 'loot.LootGenerator'._wrap(super(BlockProperties, self).getLootGen())

    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.state.BlockProperties.getHardness()"""
        return float._wrap(super(BlockProperties, self).getHardness())

    @overload
    def with(self, arg0: str, arg1: object) -> 'BlockDataEntry':
        """public final <T> dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockProperties.with(java.lang.String,T)"""
        return 'BlockDataEntry'._wrap(super(_BlockProperties, self).with(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.equals(java.lang.Object)"""
        return bool._wrap(super(_BlockProperties, self).equals(arg0))


BlockProperties.AIR = BlockProperties._wrap(_AIR.AIR)