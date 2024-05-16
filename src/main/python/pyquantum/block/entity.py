from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.block.entity.BlockEntityType as __BlockEntityType
__BlockEntityType = __BlockEntityType
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.menu.CrateMenu as __CrateMenu
__CrateMenu = __CrateMenu
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.block.entity.CrateBlockEntity as __CrateBlockEntity
__CrateBlockEntity = __CrateBlockEntity
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

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
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Long as __long
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.block.entity.ContainerBlockEntity as __ContainerBlockEntity
__ContainerBlockEntity = __ContainerBlockEntity
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class CrateBlockEntity(__ContainerBlockEntity, ContainerBlockEntity):
    """dev.ultreon.quantum.block.entity.CrateBlockEntity"""
 
    @staticmethod
    def __wrap(java_value: __CrateBlockEntity) -> 'CrateBlockEntity':
        return CrateBlockEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrateBlockEntity):
        """
        Dynamic initializer for CrateBlockEntity.
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
    def pos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.block.entity.BlockEntity.pos()"""
        return 'world.BlockPos'.__wrap(super(BlockEntity, self).pos())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos'):
        """public dev.ultreon.quantum.block.entity.CrateBlockEntity(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        val = __CrateBlockEntity(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onLostViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onLostViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(__ContainerBlockEntity, self).onLostViewer(arg0, arg1)

    @override
    @overload
    def getType(self) -> 'BlockEntityType':
        """public dev.ultreon.quantum.block.entity.BlockEntityType<?> dev.ultreon.quantum.block.entity.BlockEntity.getType()"""
        return 'BlockEntityType'.__wrap(super(BlockEntity, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMenu(self) -> 'menu.ContainerMenu':
        """public T dev.ultreon.quantum.block.entity.ContainerBlockEntity.getMenu()"""
        return 'menu.ContainerMenu'.__wrap(super(ContainerBlockEntity, self).getMenu())

    @overload
    def remove(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).remove(__int.valueOf(arg0)))

    @overload
    def remove(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int,int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).remove(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.entity.BlockEntity.getBlock()"""
        return 'block.Block'.__wrap(super(BlockEntity, self).getBlock())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.entity.ContainerBlockEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__ContainerBlockEntity, self).save(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: int, arg1: int, arg2: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerBlockEntity, self).set(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.block.entity.BlockEntity.getWorld()"""
        return 'world.World'.__wrap(super(BlockEntity, self).getWorld())

    @overload
    def get(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int,int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def open(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.open(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerBlockEntity, self).open(arg0)

    @override
    @overload
    def set(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerBlockEntity, self).set(__int.valueOf(arg0), arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def createMenu(self, arg0: 'Player') -> 'menu.CrateMenu':
        """public dev.ultreon.quantum.menu.CrateMenu dev.ultreon.quantum.block.entity.CrateBlockEntity.createMenu(dev.ultreon.quantum.entity.player.Player)"""
        return 'menu.CrateMenu'.__wrap(super(__CrateBlockEntity, self).createMenu(arg0))

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(__ContainerBlockEntity, self).load(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onGainedViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onGainedViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(__ContainerBlockEntity, self).onGainedViewer(arg0, arg1)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).get(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def fullyLoad(arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public static dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.block.entity.BlockEntity.fullyLoad(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return BlockEntity.__wrap(__BlockEntity.fullyLoad(arg0, arg1, arg2))

    @override
    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.entity.BlockEntity.getBlockMeta()"""
        return 'state.BlockProperties'.__wrap(super(BlockEntity, self).getBlockMeta())

 
 
 
# CLASS: dev.ultreon.quantum.block.entity.CrateBlockEntity
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.block.entity.BlockEntityType as __BlockEntityType
__BlockEntityType = __BlockEntityType
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.menu.CrateMenu as __CrateMenu
__CrateMenu = __CrateMenu
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.block.entity.CrateBlockEntity as __CrateBlockEntity
__CrateBlockEntity = __CrateBlockEntity
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

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
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Long as __long
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.block.entity.ContainerBlockEntity as __ContainerBlockEntity
__ContainerBlockEntity = __ContainerBlockEntity
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class CrateBlockEntity(__ContainerBlockEntity, ContainerBlockEntity):
    """dev.ultreon.quantum.block.entity.CrateBlockEntity"""
 
    @staticmethod
    def __wrap(java_value: __CrateBlockEntity) -> 'CrateBlockEntity':
        return CrateBlockEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrateBlockEntity):
        """
        Dynamic initializer for CrateBlockEntity.
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
    def pos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.block.entity.BlockEntity.pos()"""
        return 'world.BlockPos'.__wrap(super(BlockEntity, self).pos())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos'):
        """public dev.ultreon.quantum.block.entity.CrateBlockEntity(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        val = __CrateBlockEntity(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onLostViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onLostViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(__ContainerBlockEntity, self).onLostViewer(arg0, arg1)

    @override
    @overload
    def getType(self) -> 'BlockEntityType':
        """public dev.ultreon.quantum.block.entity.BlockEntityType<?> dev.ultreon.quantum.block.entity.BlockEntity.getType()"""
        return 'BlockEntityType'.__wrap(super(BlockEntity, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMenu(self) -> 'menu.ContainerMenu':
        """public T dev.ultreon.quantum.block.entity.ContainerBlockEntity.getMenu()"""
        return 'menu.ContainerMenu'.__wrap(super(ContainerBlockEntity, self).getMenu())

    @overload
    def remove(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).remove(__int.valueOf(arg0)))

    @overload
    def remove(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int,int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).remove(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.entity.BlockEntity.getBlock()"""
        return 'block.Block'.__wrap(super(BlockEntity, self).getBlock())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.entity.ContainerBlockEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__ContainerBlockEntity, self).save(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: int, arg1: int, arg2: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerBlockEntity, self).set(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.block.entity.BlockEntity.getWorld()"""
        return 'world.World'.__wrap(super(BlockEntity, self).getWorld())

    @overload
    def get(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int,int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def open(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.open(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerBlockEntity, self).open(arg0)

    @override
    @overload
    def set(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerBlockEntity, self).set(__int.valueOf(arg0), arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def createMenu(self, arg0: 'Player') -> 'menu.CrateMenu':
        """public dev.ultreon.quantum.menu.CrateMenu dev.ultreon.quantum.block.entity.CrateBlockEntity.createMenu(dev.ultreon.quantum.entity.player.Player)"""
        return 'menu.CrateMenu'.__wrap(super(__CrateBlockEntity, self).createMenu(arg0))

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(__ContainerBlockEntity, self).load(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def onGainedViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onGainedViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(__ContainerBlockEntity, self).onGainedViewer(arg0, arg1)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).get(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def fullyLoad(arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public static dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.block.entity.BlockEntity.fullyLoad(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return BlockEntity.__wrap(__BlockEntity.fullyLoad(arg0, arg1, arg2))

    @override
    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.entity.BlockEntity.getBlockMeta()"""
        return 'state.BlockProperties'.__wrap(super(BlockEntity, self).getBlockMeta())

 
 
 
# CLASS: dev.ultreon.quantum.block.entity.CrateBlockEntity 
 
 
# CLASS: dev.ultreon.quantum.block.entity.ContainerBlockEntity
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.block.entity.BlockEntityType as __BlockEntityType
__BlockEntityType = __BlockEntityType
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
from abc import abstractmethod, ABC
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

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
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Long as __long
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.block.entity.ContainerBlockEntity as __ContainerBlockEntity
__ContainerBlockEntity = __ContainerBlockEntity
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class ContainerBlockEntity(ABC, __BlockEntity, BlockEntity):
    """dev.ultreon.quantum.block.entity.ContainerBlockEntity"""
 
    @staticmethod
    def __wrap(java_value: __ContainerBlockEntity) -> 'ContainerBlockEntity':
        return ContainerBlockEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContainerBlockEntity):
        """
        Dynamic initializer for ContainerBlockEntity.
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
    def pos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.block.entity.BlockEntity.pos()"""
        return 'world.BlockPos'.__wrap(super(BlockEntity, self).pos())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getType(self) -> 'BlockEntityType':
        """public dev.ultreon.quantum.block.entity.BlockEntityType<?> dev.ultreon.quantum.block.entity.BlockEntity.getType()"""
        return 'BlockEntityType'.__wrap(super(BlockEntity, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).remove(__int.valueOf(arg0)))

    @overload
    def remove(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int,int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).remove(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.entity.BlockEntity.getBlock()"""
        return 'block.Block'.__wrap(super(BlockEntity, self).getBlock())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.entity.ContainerBlockEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__ContainerBlockEntity, self).save(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getMenu(self) -> 'menu.ContainerMenu':
        """public T dev.ultreon.quantum.block.entity.ContainerBlockEntity.getMenu()"""
        return 'menu.ContainerMenu'.__wrap(super(ContainerBlockEntity, self).getMenu())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.block.entity.BlockEntity.getWorld()"""
        return 'world.World'.__wrap(super(BlockEntity, self).getWorld())

    @abstractmethod
    def createMenu(self, arg0: 'Player'):
        """public abstract T dev.ultreon.quantum.block.entity.ContainerBlockEntity.createMenu(dev.ultreon.quantum.entity.player.Player)"""
        pass

    @overload
    def get(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int,int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def open(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.open(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerBlockEntity, self).open(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def set(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerBlockEntity, self).set(__int.valueOf(arg0), arg1)

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(__ContainerBlockEntity, self).load(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def onLostViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onLostViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(__ContainerBlockEntity, self).onLostViewer(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int, arg1: int, arg2: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerBlockEntity, self).set(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def __init__(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos', arg3: int):
        """public dev.ultreon.quantum.block.entity.ContainerBlockEntity(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,int)"""
        val = __ContainerBlockEntity(arg0, arg1, arg2, __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerBlockEntity, self).get(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def fullyLoad(arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public static dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.block.entity.BlockEntity.fullyLoad(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return BlockEntity.__wrap(__BlockEntity.fullyLoad(arg0, arg1, arg2))

    @overload
    def onGainedViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onGainedViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(__ContainerBlockEntity, self).onGainedViewer(arg0, arg1)

    @override
    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.entity.BlockEntity.getBlockMeta()"""
        return 'state.BlockProperties'.__wrap(super(BlockEntity, self).getBlockMeta()) 
 
 
# CLASS: dev.ultreon.quantum.block.entity.BlockEntityTypes
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
import dev.ultreon.quantum.block.entity.BlockEntityTypes as __BlockEntityTypes
__BlockEntityTypes = __BlockEntityTypes
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlockEntityTypes():
    """dev.ultreon.quantum.block.entity.BlockEntityTypes"""
 
    @staticmethod
    def __wrap(java_value: __BlockEntityTypes) -> 'BlockEntityTypes':
        return BlockEntityTypes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockEntityTypes):
        """
        Dynamic initializer for BlockEntityTypes.
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
 
    # public static final dev.ultreon.quantum.block.entity.BlockEntityType<dev.ultreon.quantum.block.entity.CrateBlockEntity> dev.ultreon.quantum.block.entity.BlockEntityTypes.CRATE
    CRATE: 'BlockEntityType' = __wrap(__BlockEntityType.CRATE)


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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.entity.BlockEntityTypes()"""
        val = __BlockEntityTypes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.block.entity.BlockEntityTypes.init()"""
            __BlockEntityTypes.init()

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.entity.BlockEntityTypes()"""
        val = __BlockEntityTypes()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.block.entity.BlockEntity
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.block.entity.BlockEntityType as __BlockEntityType
__BlockEntityType = __BlockEntityType
from pyquantum_helper import override
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
import java.lang.Integer as __int
from builtins import bool
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class BlockEntity(ABC):
    """dev.ultreon.quantum.block.entity.BlockEntity"""
 
    @staticmethod
    def __wrap(java_value: __BlockEntity) -> 'BlockEntity':
        return BlockEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockEntity):
        """
        Dynamic initializer for BlockEntity.
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
    def pos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.block.entity.BlockEntity.pos()"""
        return 'world.BlockPos'.__wrap(super(BlockEntity, self).pos())

    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.block.entity.BlockEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(__BlockEntity, self).load(arg0)

    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.entity.BlockEntity.getBlock()"""
        return 'block.Block'.__wrap(super(BlockEntity, self).getBlock())

    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.entity.BlockEntity.getBlockMeta()"""
        return 'state.BlockProperties'.__wrap(super(BlockEntity, self).getBlockMeta())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos'):
        """public dev.ultreon.quantum.block.entity.BlockEntity(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        val = __BlockEntity(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.entity.BlockEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'.__wrap(super(__BlockEntity, self).save(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def fullyLoad(arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public static dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.block.entity.BlockEntity.fullyLoad(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return BlockEntity.__wrap(__BlockEntity.fullyLoad(arg0, arg1, arg2))

    @overload
    def getType(self) -> 'BlockEntityType':
        """public dev.ultreon.quantum.block.entity.BlockEntityType<?> dev.ultreon.quantum.block.entity.BlockEntity.getType()"""
        return 'BlockEntityType'.__wrap(super(BlockEntity, self).getType())

    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.block.entity.BlockEntity.getWorld()"""
        return 'world.World'.__wrap(super(BlockEntity, self).getWorld())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.block.entity.BlockEntityType$BlockEntityFactory
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.block.entity.BlockEntityType as __BlockEntityType_BlockEntityFactory
__BlockEntityFactory = __BlockEntityType_BlockEntityFactory.BlockEntityFactory
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from abc import abstractmethod, ABC
 
class BlockEntityFactory(ABC):
    """dev.ultreon.quantum.block.entity.BlockEntityType.BlockEntityFactory"""
 
    @staticmethod
    def __wrap(java_value: __BlockEntityFactory) -> 'BlockEntityFactory':
        return BlockEntityFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockEntityFactory):
        """
        Dynamic initializer for BlockEntityFactory.
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
    def create(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos'):
        """public abstract T dev.ultreon.quantum.block.entity.BlockEntityType$BlockEntityFactory.create(dev.ultreon.quantum.block.entity.BlockEntityType<T>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.block.entity.BlockEntityType
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.block.entity.BlockEntityType as __BlockEntityType
__BlockEntityType = __BlockEntityType
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
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
 
class BlockEntityType():
    """dev.ultreon.quantum.block.entity.BlockEntityType"""
 
    @staticmethod
    def __wrap(java_value: __BlockEntityType) -> 'BlockEntityType':
        return BlockEntityType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockEntityType):
        """
        Dynamic initializer for BlockEntityType.
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
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.entity.BlockEntityType.getRawId()"""
        return int.__wrap(super(BlockEntityType, self).getRawId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def create(self, arg0: 'World', arg1: 'BlockPos') -> 'BlockEntity':
        """public T dev.ultreon.quantum.block.entity.BlockEntityType.create(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        return 'BlockEntity'.__wrap(super(__BlockEntityType, self).create(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public T dev.ultreon.quantum.block.entity.BlockEntityType.load(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return 'BlockEntity'.__wrap(super(__BlockEntityType, self).load(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'BlockEntityFactory'):
        """public dev.ultreon.quantum.block.entity.BlockEntityType(dev.ultreon.quantum.block.entity.BlockEntityType$BlockEntityFactory<T>)"""
        val = __BlockEntityType(arg0)
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
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.entity.BlockEntityType.getId()"""
        return 'util.Identifier'.__wrap(super(BlockEntityType, self).getId())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))