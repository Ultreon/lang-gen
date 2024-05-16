from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
from builtins import object
import java.lang.Enum as Enum
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.block.state.BlockDataEntry as __BlockDataEntry
__BlockDataEntry = __BlockDataEntry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import de.marhali.json5.Json5Object as Json5Object
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class BlockDataEntry(ABC):
    """dev.ultreon.quantum.block.state.BlockDataEntry"""
 
    @staticmethod
    def __wrap(java_value: __BlockDataEntry) -> 'BlockDataEntry':
        return BlockDataEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockDataEntry):
        """
        Dynamic initializer for BlockDataEntry.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.block.state.BlockDataEntry.hashCode()"""
        return int.__wrap(super(BlockDataEntry, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockDataEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__BlockDataEntry, self).equals(arg0))

    @staticmethod
    @overload
    def of(arg0: bool) -> 'BlockDataEntry':
        """public static dev.ultreon.quantum.block.state.BlockDataEntry<java.lang.Boolean> dev.ultreon.quantum.block.state.BlockDataEntry.of(boolean)"""
        return BlockDataEntry.__wrap(__BlockDataEntry.of(__boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.block.state.BlockDataEntry.getValue()"""
        return object.__wrap(super(BlockDataEntry, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.state.BlockDataEntry.toString()"""
        return str.__wrap(super(BlockDataEntry, self).toString())

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int) -> 'BlockDataEntry':
        """public static dev.ultreon.quantum.block.state.BlockDataEntry<java.lang.Integer> dev.ultreon.quantum.block.state.BlockDataEntry.of(int,int,int)"""
        return BlockDataEntry.__wrap(__BlockDataEntry.of(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @abstractmethod
    def with(self, arg0: object):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.with(T)"""
        pass

    @staticmethod
    @overload
    def ofEnum(arg0: 'Enum') -> 'BlockDataEntry':
        """public static <T extends java.lang.Enum<T>> dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.ofEnum(T)"""
        return BlockDataEntry.__wrap(__BlockDataEntry.ofEnum(arg0))

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
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.block.state.BlockDataEntry(T)"""
        val = __BlockDataEntry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def load(self, arg0: 'DataType'):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockDataEntry.load(dev.ultreon.ubo.types.DataType<?>)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def map(self, arg0: 'Function') -> 'BlockDataEntry':
        """public dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.map(java.util.function.Function<T, T>)"""
        return 'BlockDataEntry'.__wrap(super(__BlockDataEntry, self).map(arg0))

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
    def cast(self, arg0: 'Class') -> 'BlockDataEntry':
        """public <R> dev.ultreon.quantum.block.state.BlockDataEntry<R> dev.ultreon.quantum.block.state.BlockDataEntry.cast(java.lang.Class<R>)"""
        return 'BlockDataEntry'.__wrap(super(__BlockDataEntry, self).cast(arg0))

    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.copy()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.block.state.BlockDataEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
from builtins import object
import java.lang.Enum as Enum
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.block.state.BlockDataEntry as __BlockDataEntry
__BlockDataEntry = __BlockDataEntry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import de.marhali.json5.Json5Object as Json5Object
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class BlockDataEntry(ABC):
    """dev.ultreon.quantum.block.state.BlockDataEntry"""
 
    @staticmethod
    def __wrap(java_value: __BlockDataEntry) -> 'BlockDataEntry':
        return BlockDataEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockDataEntry):
        """
        Dynamic initializer for BlockDataEntry.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.block.state.BlockDataEntry.hashCode()"""
        return int.__wrap(super(BlockDataEntry, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockDataEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__BlockDataEntry, self).equals(arg0))

    @staticmethod
    @overload
    def of(arg0: bool) -> 'BlockDataEntry':
        """public static dev.ultreon.quantum.block.state.BlockDataEntry<java.lang.Boolean> dev.ultreon.quantum.block.state.BlockDataEntry.of(boolean)"""
        return BlockDataEntry.__wrap(__BlockDataEntry.of(__boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.block.state.BlockDataEntry.getValue()"""
        return object.__wrap(super(BlockDataEntry, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.state.BlockDataEntry.toString()"""
        return str.__wrap(super(BlockDataEntry, self).toString())

    @staticmethod
    @overload
    def of(arg0: int, arg1: int, arg2: int) -> 'BlockDataEntry':
        """public static dev.ultreon.quantum.block.state.BlockDataEntry<java.lang.Integer> dev.ultreon.quantum.block.state.BlockDataEntry.of(int,int,int)"""
        return BlockDataEntry.__wrap(__BlockDataEntry.of(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @abstractmethod
    def with(self, arg0: object):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.with(T)"""
        pass

    @staticmethod
    @overload
    def ofEnum(arg0: 'Enum') -> 'BlockDataEntry':
        """public static <T extends java.lang.Enum<T>> dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.ofEnum(T)"""
        return BlockDataEntry.__wrap(__BlockDataEntry.ofEnum(arg0))

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
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.block.state.BlockDataEntry(T)"""
        val = __BlockDataEntry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def load(self, arg0: 'DataType'):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockDataEntry.load(dev.ultreon.ubo.types.DataType<?>)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def map(self, arg0: 'Function') -> 'BlockDataEntry':
        """public dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.map(java.util.function.Function<T, T>)"""
        return 'BlockDataEntry'.__wrap(super(__BlockDataEntry, self).map(arg0))

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
    def cast(self, arg0: 'Class') -> 'BlockDataEntry':
        """public <R> dev.ultreon.quantum.block.state.BlockDataEntry<R> dev.ultreon.quantum.block.state.BlockDataEntry.cast(java.lang.Class<R>)"""
        return 'BlockDataEntry'.__wrap(super(__BlockDataEntry, self).cast(arg0))

    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockDataEntry.copy()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.block.state.BlockDataEntry 
 
 
# CLASS: dev.ultreon.quantum.block.state.BlockProperties
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import dev.ultreon.quantum.block.state.BlockDataEntry as __BlockDataEntry
__BlockDataEntry = __BlockDataEntry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class BlockProperties():
    """dev.ultreon.quantum.block.state.BlockProperties"""
 
    @staticmethod
    def __wrap(java_value: __BlockProperties) -> 'BlockProperties':
        return BlockProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockProperties):
        """
        Dynamic initializer for BlockProperties.
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
 
    # public static final dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.AIR
    AIR: 'BlockProperties' = __wrap(__BlockProperties.AIR)


    @overload
    def onPlace(self, arg0: 'ServerWorld', arg1: 'BlockPos'):
        """public void dev.ultreon.quantum.block.state.BlockProperties.onPlace(dev.ultreon.quantum.world.ServerWorld,dev.ultreon.quantum.world.BlockPos)"""
        super(__BlockProperties, self).onPlace(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def withEntry(self, arg0: str, arg1: object) -> 'BlockProperties':
        """public <T> dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.withEntry(java.lang.String,T)"""
        return 'BlockProperties'.__wrap(super(__BlockProperties, self).withEntry(arg0, arg1))

    @overload
    def get(self, arg0: str, *arg1: object) -> object:
        """public final <T> T dev.ultreon.quantum.block.state.BlockProperties.get(java.lang.String,T...)"""
        return object.__wrap(super(__BlockProperties, self).get(arg0, arg1))

    @overload
    def is(self, arg0: 'Block') -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.is(dev.ultreon.quantum.block.Block)"""
        return bool.__wrap(super(__BlockProperties, self).is(arg0))

    @overload
    def setEntry(self, arg0: str, arg1: 'BlockDataEntry'):
        """public void dev.ultreon.quantum.block.state.BlockProperties.setEntry(java.lang.String,dev.ultreon.quantum.block.state.BlockDataEntry<?>)"""
        super(__BlockProperties, self).setEntry(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Block', arg1: 'Map'):
        """public dev.ultreon.quantum.block.state.BlockProperties(dev.ultreon.quantum.block.Block,java.util.Map<java.lang.String, dev.ultreon.quantum.block.state.BlockDataEntry<?>>)"""
        val = __BlockProperties(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.block.state.BlockProperties.hashCode()"""
        return int.__wrap(super(BlockProperties, self).hashCode())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int) -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.state.BlockProperties.getBoundingBox(int,int,int)"""
        return 'util.BoundingBox'.__wrap(super(__BlockProperties, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isTransparent()"""
        return bool.__wrap(super(BlockProperties, self).isTransparent())

    @overload
    def hasEntry(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.hasEntry(java.lang.String)"""
        return bool.__wrap(super(__BlockProperties, self).hasEntry(arg0))

    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.state.BlockProperties.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(BlockProperties, self).getEffectiveTool())

    @overload
    def getLootGen(self) -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.state.BlockProperties.getLootGen()"""
        return 'loot.LootGenerator'.__wrap(super(BlockProperties, self).getLootGen())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.state.BlockProperties.toString()"""
        return str.__wrap(super(BlockProperties, self).toString())

    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.state.BlockProperties.save()"""
        return 'types.MapType'.__wrap(super(BlockProperties, self).save())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext') -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext)"""
        return bool.__wrap(super(__BlockProperties, self).canBeReplacedBy(arg0))

    @overload
    def withEntry(self, arg0: str, arg1: 'BlockDataEntry') -> 'BlockProperties':
        """public <T> dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.withEntry(java.lang.String,dev.ultreon.quantum.block.state.BlockDataEntry<T>)"""
        return 'BlockProperties'.__wrap(super(__BlockProperties, self).withEntry(arg0, arg1))

    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.state.BlockProperties.getHardness()"""
        return float.__wrap(super(BlockProperties, self).getHardness())

    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isFluid()"""
        return bool.__wrap(super(BlockProperties, self).isFluid())

    @overload
    def getEntryUnsafe(self, arg0: str) -> 'BlockDataEntry':
        """public final dev.ultreon.quantum.block.state.BlockDataEntry<?> dev.ultreon.quantum.block.state.BlockProperties.getEntryUnsafe(java.lang.String)"""
        return 'BlockDataEntry'.__wrap(super(__BlockProperties, self).getEntryUnsafe(arg0))

    @overload
    def with(self, arg0: str, arg1: object) -> 'BlockDataEntry':
        """public final <T> dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockProperties.with(java.lang.String,T)"""
        return 'BlockDataEntry'.__wrap(super(__BlockProperties, self).with(arg0, arg1))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.load(dev.ultreon.ubo.types.MapType)"""
        return BlockProperties.__wrap(__BlockProperties.load(arg0))

    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isAir()"""
        return bool.__wrap(super(BlockProperties, self).isAir())

    @overload
    def isWater(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isWater()"""
        return bool.__wrap(super(BlockProperties, self).isWater())

    @overload
    def write(self, arg0: 'PacketIO') -> int:
        """public int dev.ultreon.quantum.block.state.BlockProperties.write(dev.ultreon.quantum.network.PacketIO)"""
        return int.__wrap(super(__BlockProperties, self).write(arg0))

    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isReplaceable()"""
        return bool.__wrap(super(BlockProperties, self).isReplaceable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos'):
        """public void dev.ultreon.quantum.block.state.BlockProperties.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        super(__BlockProperties, self).update(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.equals(java.lang.Object)"""
        return bool.__wrap(super(__BlockProperties, self).equals(arg0))

    @overload
    def getEntries(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.block.state.BlockDataEntry<?>> dev.ultreon.quantum.block.state.BlockProperties.getEntries()"""
        return 'Map'.__wrap(super(BlockProperties, self).getEntries())

    @overload
    def getProperty(self, arg0: str, *arg1: object) -> 'BlockDataEntry':
        """public final <T> dev.ultreon.quantum.block.state.BlockDataEntry<T> dev.ultreon.quantum.block.state.BlockProperties.getProperty(java.lang.String,T...)"""
        return 'BlockDataEntry'.__wrap(super(__BlockProperties, self).getProperty(arg0, arg1))

    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.state.BlockProperties.getBlock()"""
        return 'block.Block'.__wrap(super(BlockProperties, self).getBlock())

    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player'):
        """public void dev.ultreon.quantum.block.state.BlockProperties.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player)"""
        super(__BlockProperties, self).onDestroy(arg0, arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def read(arg0: 'PacketIO') -> 'BlockProperties':
        """public static dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.state.BlockProperties.read(dev.ultreon.quantum.network.PacketIO)"""
        return BlockProperties.__wrap(__BlockProperties.read(arg0))

    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.isToolRequired()"""
        return bool.__wrap(super(BlockProperties, self).isToolRequired())

    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.state.BlockProperties.hasCollider()"""
        return bool.__wrap(super(BlockProperties, self).hasCollider())