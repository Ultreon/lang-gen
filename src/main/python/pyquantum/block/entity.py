from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.menu.CrateMenu as _CrateMenu
_CrateMenu = _CrateMenu
import dev.ultreon.quantum.block.entity.CrateBlockEntity as _CrateBlockEntity
_CrateBlockEntity = _CrateBlockEntity
import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

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
import dev.ultreon.quantum.block.entity.ContainerBlockEntity as _ContainerBlockEntity
_ContainerBlockEntity = _ContainerBlockEntity
import dev.ultreon.quantum.block.entity.BlockEntityType as _BlockEntityType
_BlockEntityType = _BlockEntityType
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrateBlockEntity():
    """dev.ultreon.quantum.block.entity.CrateBlockEntity"""
 
    @staticmethod
    def _wrap(java_value: _CrateBlockEntity) -> 'CrateBlockEntity':
        return CrateBlockEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrateBlockEntity):
        """
        Dynamic initializer for CrateBlockEntity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrateBlockEntity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrateBlockEntity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.block.entity.BlockEntity.getWorld()"""
        return 'world.World'._wrap(super(BlockEntity, self).getWorld())

    @override
    @overload
    def getMenu(self) -> 'menu.ContainerMenu':
        """public T dev.ultreon.quantum.block.entity.ContainerBlockEntity.getMenu()"""
        return 'menu.ContainerMenu'._wrap(super(ContainerBlockEntity, self).getMenu())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def onGainedViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onGainedViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(_ContainerBlockEntity, self).onGainedViewer(arg0, arg1)

    @overload
    def remove(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int,int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).remove(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getType(self) -> 'BlockEntityType':
        """public dev.ultreon.quantum.block.entity.BlockEntityType<?> dev.ultreon.quantum.block.entity.BlockEntity.getType()"""
        return 'BlockEntityType'._wrap(super(BlockEntity, self).getType())

    @override
    @overload
    def open(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.open(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerBlockEntity, self).open(arg0)

    @override
    @overload
    def pos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.block.entity.BlockEntity.pos()"""
        return 'world.BlockPos'._wrap(super(BlockEntity, self).pos())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.entity.ContainerBlockEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_ContainerBlockEntity, self).save(arg0))

    @override
    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.entity.BlockEntity.getBlockMeta()"""
        return 'state.BlockProperties'._wrap(super(BlockEntity, self).getBlockMeta())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def onLostViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onLostViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(_ContainerBlockEntity, self).onLostViewer(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,dev.ultreon.quantum.item.ItemStack)"""
        super(_ContainerBlockEntity, self).set(_int.valueOf(arg0), arg1)

    @overload
    def remove(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def get(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int,int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos'):
        """public dev.ultreon.quantum.block.entity.CrateBlockEntity(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        val = _CrateBlockEntity(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def set(self, arg0: int, arg1: int, arg2: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,int,dev.ultreon.quantum.item.ItemStack)"""
        super(_ContainerBlockEntity, self).set(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.entity.BlockEntity.getBlock()"""
        return 'block.Block'._wrap(super(BlockEntity, self).getBlock())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def fullyLoad(arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public static dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.block.entity.BlockEntity.fullyLoad(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return BlockEntity._wrap(_BlockEntity.fullyLoad(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createMenu(self, arg0: 'Player') -> 'menu.CrateMenu':
        """public dev.ultreon.quantum.menu.CrateMenu dev.ultreon.quantum.block.entity.CrateBlockEntity.createMenu(dev.ultreon.quantum.entity.player.Player)"""
        return 'menu.CrateMenu'._wrap(super(_CrateBlockEntity, self).createMenu(arg0))

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(_ContainerBlockEntity, self).load(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.block.entity.CrateBlockEntity
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.menu.CrateMenu as _CrateMenu
_CrateMenu = _CrateMenu
import dev.ultreon.quantum.block.entity.CrateBlockEntity as _CrateBlockEntity
_CrateBlockEntity = _CrateBlockEntity
import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

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
import dev.ultreon.quantum.block.entity.ContainerBlockEntity as _ContainerBlockEntity
_ContainerBlockEntity = _ContainerBlockEntity
import dev.ultreon.quantum.block.entity.BlockEntityType as _BlockEntityType
_BlockEntityType = _BlockEntityType
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrateBlockEntity():
    """dev.ultreon.quantum.block.entity.CrateBlockEntity"""
 
    @staticmethod
    def _wrap(java_value: _CrateBlockEntity) -> 'CrateBlockEntity':
        return CrateBlockEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrateBlockEntity):
        """
        Dynamic initializer for CrateBlockEntity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrateBlockEntity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrateBlockEntity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.block.entity.BlockEntity.getWorld()"""
        return 'world.World'._wrap(super(BlockEntity, self).getWorld())

    @override
    @overload
    def getMenu(self) -> 'menu.ContainerMenu':
        """public T dev.ultreon.quantum.block.entity.ContainerBlockEntity.getMenu()"""
        return 'menu.ContainerMenu'._wrap(super(ContainerBlockEntity, self).getMenu())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def onGainedViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onGainedViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(_ContainerBlockEntity, self).onGainedViewer(arg0, arg1)

    @overload
    def remove(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int,int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).remove(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getType(self) -> 'BlockEntityType':
        """public dev.ultreon.quantum.block.entity.BlockEntityType<?> dev.ultreon.quantum.block.entity.BlockEntity.getType()"""
        return 'BlockEntityType'._wrap(super(BlockEntity, self).getType())

    @override
    @overload
    def open(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.open(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerBlockEntity, self).open(arg0)

    @override
    @overload
    def pos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.block.entity.BlockEntity.pos()"""
        return 'world.BlockPos'._wrap(super(BlockEntity, self).pos())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.entity.ContainerBlockEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_ContainerBlockEntity, self).save(arg0))

    @override
    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.entity.BlockEntity.getBlockMeta()"""
        return 'state.BlockProperties'._wrap(super(BlockEntity, self).getBlockMeta())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def onLostViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onLostViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(_ContainerBlockEntity, self).onLostViewer(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,dev.ultreon.quantum.item.ItemStack)"""
        super(_ContainerBlockEntity, self).set(_int.valueOf(arg0), arg1)

    @overload
    def remove(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def get(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int,int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos'):
        """public dev.ultreon.quantum.block.entity.CrateBlockEntity(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        val = _CrateBlockEntity(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def set(self, arg0: int, arg1: int, arg2: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,int,dev.ultreon.quantum.item.ItemStack)"""
        super(_ContainerBlockEntity, self).set(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.entity.BlockEntity.getBlock()"""
        return 'block.Block'._wrap(super(BlockEntity, self).getBlock())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def fullyLoad(arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public static dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.block.entity.BlockEntity.fullyLoad(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return BlockEntity._wrap(_BlockEntity.fullyLoad(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createMenu(self, arg0: 'Player') -> 'menu.CrateMenu':
        """public dev.ultreon.quantum.menu.CrateMenu dev.ultreon.quantum.block.entity.CrateBlockEntity.createMenu(dev.ultreon.quantum.entity.player.Player)"""
        return 'menu.CrateMenu'._wrap(super(_CrateBlockEntity, self).createMenu(arg0))

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(_ContainerBlockEntity, self).load(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.block.entity.CrateBlockEntity 
 
 
# CLASS: dev.ultreon.quantum.block.entity.ContainerBlockEntity
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
from abc import abstractmethod, ABC
import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

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
import dev.ultreon.quantum.block.entity.ContainerBlockEntity as _ContainerBlockEntity
_ContainerBlockEntity = _ContainerBlockEntity
import dev.ultreon.quantum.block.entity.BlockEntityType as _BlockEntityType
_BlockEntityType = _BlockEntityType
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ContainerBlockEntity():
    """dev.ultreon.quantum.block.entity.ContainerBlockEntity"""
 
    @staticmethod
    def _wrap(java_value: _ContainerBlockEntity) -> 'ContainerBlockEntity':
        return ContainerBlockEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContainerBlockEntity):
        """
        Dynamic initializer for ContainerBlockEntity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContainerBlockEntity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContainerBlockEntity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getMenu(self) -> 'menu.ContainerMenu':
        """public T dev.ultreon.quantum.block.entity.ContainerBlockEntity.getMenu()"""
        return 'menu.ContainerMenu'._wrap(super(ContainerBlockEntity, self).getMenu())

    @overload
    def get(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.block.entity.BlockEntity.getWorld()"""
        return 'world.World'._wrap(super(BlockEntity, self).getWorld())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def remove(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int,int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).remove(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getType(self) -> 'BlockEntityType':
        """public dev.ultreon.quantum.block.entity.BlockEntityType<?> dev.ultreon.quantum.block.entity.BlockEntity.getType()"""
        return 'BlockEntityType'._wrap(super(BlockEntity, self).getType())

    @override
    @overload
    def pos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.block.entity.BlockEntity.pos()"""
        return 'world.BlockPos'._wrap(super(BlockEntity, self).pos())

    @overload
    def __init__(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos', arg3: int):
        """public dev.ultreon.quantum.block.entity.ContainerBlockEntity(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,int)"""
        val = _ContainerBlockEntity(arg0, arg1, arg2, _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.entity.ContainerBlockEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_ContainerBlockEntity, self).save(arg0))

    @abstractmethod
    def createMenu(self, arg0: 'Player'):
        """public abstract T dev.ultreon.quantum.block.entity.ContainerBlockEntity.createMenu(dev.ultreon.quantum.entity.player.Player)"""
        pass

    @overload
    def onLostViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onLostViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(_ContainerBlockEntity, self).onLostViewer(arg0, arg1)

    @override
    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.entity.BlockEntity.getBlockMeta()"""
        return 'state.BlockProperties'._wrap(super(BlockEntity, self).getBlockMeta())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.remove(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).remove(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,int,dev.ultreon.quantum.item.ItemStack)"""
        super(_ContainerBlockEntity, self).set(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def get(self, arg0: int, arg1: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.block.entity.ContainerBlockEntity.get(int,int)"""
        return 'item.ItemStack'._wrap(super(_ContainerBlockEntity, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.entity.BlockEntity.getBlock()"""
        return 'block.Block'._wrap(super(BlockEntity, self).getBlock())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def open(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.open(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerBlockEntity, self).open(arg0)

    @overload
    def onGainedViewer(self, arg0: 'Player', arg1: 'CrateMenu'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.onGainedViewer(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.menu.CrateMenu)"""
        super(_ContainerBlockEntity, self).onGainedViewer(arg0, arg1)

    @staticmethod
    @overload
    def fullyLoad(arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public static dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.block.entity.BlockEntity.fullyLoad(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return BlockEntity._wrap(_BlockEntity.fullyLoad(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(_ContainerBlockEntity, self).load(arg0)

    @overload
    def set(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.block.entity.ContainerBlockEntity.set(int,dev.ultreon.quantum.item.ItemStack)"""
        super(_ContainerBlockEntity, self).set(_int.valueOf(arg0), arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.block.entity.BlockEntityTypes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.block.entity.BlockEntityTypes as _BlockEntityTypes
_BlockEntityTypes = _BlockEntityTypes
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockEntityTypes():
    """dev.ultreon.quantum.block.entity.BlockEntityTypes"""
 
    @staticmethod
    def _wrap(java_value: _BlockEntityTypes) -> 'BlockEntityTypes':
        return BlockEntityTypes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockEntityTypes):
        """
        Dynamic initializer for BlockEntityTypes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockEntityTypes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockEntityTypes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.block.entity.BlockEntityType<dev.ultreon.quantum.block.entity.CrateBlockEntity> dev.ultreon.quantum.block.entity.BlockEntityTypes.CRATE
    CRATE: 'BlockEntityType' = _wrap(_BlockEntityType.CRATE)


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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.entity.BlockEntityTypes()"""
        val = _BlockEntityTypes()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.entity.BlockEntityTypes()"""
        val = _BlockEntityTypes()
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.block.entity.BlockEntityTypes.init()"""
            _BlockEntityTypes.init()

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
 
 
# CLASS: dev.ultreon.quantum.block.entity.BlockEntity
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.block.entity.BlockEntityType as _BlockEntityType
_BlockEntityType = _BlockEntityType
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
import java.lang.String as _String
_String = _String
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
from builtins import bool
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockEntity():
    """dev.ultreon.quantum.block.entity.BlockEntity"""
 
    @staticmethod
    def _wrap(java_value: _BlockEntity) -> 'BlockEntity':
        return BlockEntity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockEntity):
        """
        Dynamic initializer for BlockEntity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockEntity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockEntity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getType(self) -> 'BlockEntityType':
        """public dev.ultreon.quantum.block.entity.BlockEntityType<?> dev.ultreon.quantum.block.entity.BlockEntity.getType()"""
        return 'BlockEntityType'._wrap(super(BlockEntity, self).getType())

    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.entity.BlockEntity.getBlockMeta()"""
        return 'state.BlockProperties'._wrap(super(BlockEntity, self).getBlockMeta())

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
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.block.entity.BlockEntity.getWorld()"""
        return 'world.World'._wrap(super(BlockEntity, self).getWorld())

    @overload
    def save(self, arg0: 'MapType') -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.entity.BlockEntity.save(dev.ultreon.ubo.types.MapType)"""
        return 'types.MapType'._wrap(super(_BlockEntity, self).save(arg0))

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
    def pos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.block.entity.BlockEntity.pos()"""
        return 'world.BlockPos'._wrap(super(BlockEntity, self).pos())

    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.entity.BlockEntity.getBlock()"""
        return 'block.Block'._wrap(super(BlockEntity, self).getBlock())

    @staticmethod
    @overload
    def fullyLoad(arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public static dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.block.entity.BlockEntity.fullyLoad(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return BlockEntity._wrap(_BlockEntity.fullyLoad(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos'):
        """public dev.ultreon.quantum.block.entity.BlockEntity(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        val = _BlockEntity(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def load(self, arg0: 'MapType'):
        """public void dev.ultreon.quantum.block.entity.BlockEntity.load(dev.ultreon.ubo.types.MapType)"""
        super(_BlockEntity, self).load(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.block.entity.BlockEntityType$BlockEntityFactory
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.entity.BlockEntityType as _BlockEntityType_BlockEntityFactory
_BlockEntityFactory = _BlockEntityType_BlockEntityFactory.BlockEntityFactory
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from abc import abstractmethod, ABC
 
class BlockEntityFactory():
    """dev.ultreon.quantum.block.entity.BlockEntityType.BlockEntityFactory"""
 
    @staticmethod
    def _wrap(java_value: _BlockEntityFactory) -> 'BlockEntityFactory':
        return BlockEntityFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockEntityFactory):
        """
        Dynamic initializer for BlockEntityFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockEntityFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockEntityFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, arg0: 'BlockEntityType', arg1: 'World', arg2: 'BlockPos'):
        """public abstract T dev.ultreon.quantum.block.entity.BlockEntityType$BlockEntityFactory.create(dev.ultreon.quantum.block.entity.BlockEntityType<T>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.block.entity.BlockEntityType
from pyquantum_helper import import_once as _import_once
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
import dev.ultreon.quantum.block.entity.BlockEntityType as _BlockEntityType
_BlockEntityType = _BlockEntityType
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
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
 
class BlockEntityType():
    """dev.ultreon.quantum.block.entity.BlockEntityType"""
 
    @staticmethod
    def _wrap(java_value: _BlockEntityType) -> 'BlockEntityType':
        return BlockEntityType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockEntityType):
        """
        Dynamic initializer for BlockEntityType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockEntityType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockEntityType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def create(self, arg0: 'World', arg1: 'BlockPos') -> 'BlockEntity':
        """public T dev.ultreon.quantum.block.entity.BlockEntityType.create(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos)"""
        return 'BlockEntity'._wrap(super(_BlockEntityType, self).create(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.entity.BlockEntityType.getId()"""
        return 'util.Identifier'._wrap(super(BlockEntityType, self).getId())

    @overload
    def load(self, arg0: 'World', arg1: 'BlockPos', arg2: 'MapType') -> 'BlockEntity':
        """public T dev.ultreon.quantum.block.entity.BlockEntityType.load(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.ubo.types.MapType)"""
        return 'BlockEntity'._wrap(super(_BlockEntityType, self).load(arg0, arg1, arg2))

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
    def __init__(self, arg0: 'BlockEntityFactory'):
        """public dev.ultreon.quantum.block.entity.BlockEntityType(dev.ultreon.quantum.block.entity.BlockEntityType$BlockEntityFactory<T>)"""
        val = _BlockEntityType(arg0)
        self.__wrapper = val

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
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.entity.BlockEntityType.getRawId()"""
        return int._wrap(super(BlockEntityType, self).getRawId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())