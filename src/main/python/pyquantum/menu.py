from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.menu.MenuType as _MenuType_MenuBuilder
_MenuBuilder = _MenuType_MenuBuilder.MenuBuilder
from abc import abstractmethod, ABC
 
class MenuBuilder():
    """dev.ultreon.quantum.menu.MenuType.MenuBuilder"""
 
    @staticmethod
    def _wrap(java_value: _MenuBuilder) -> 'MenuBuilder':
        return MenuBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuBuilder):
        """
        Dynamic initializer for MenuBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'BlockPos'):
        """public abstract T dev.ultreon.quantum.menu.MenuType$MenuBuilder.create(dev.ultreon.quantum.menu.MenuType<T>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.menu.MenuType$MenuBuilder
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.menu.MenuType as _MenuType_MenuBuilder
_MenuBuilder = _MenuType_MenuBuilder.MenuBuilder
from abc import abstractmethod, ABC
 
class MenuBuilder():
    """dev.ultreon.quantum.menu.MenuType.MenuBuilder"""
 
    @staticmethod
    def _wrap(java_value: _MenuBuilder) -> 'MenuBuilder':
        return MenuBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuBuilder):
        """
        Dynamic initializer for MenuBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'BlockPos'):
        """public abstract T dev.ultreon.quantum.menu.MenuType$MenuBuilder.create(dev.ultreon.quantum.menu.MenuType<T>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.menu.MenuType$MenuBuilder 
 
 
# CLASS: dev.ultreon.quantum.menu.ItemContainerMenu
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
import dev.ultreon.quantum.menu.ItemContainerMenu as _ItemContainerMenu
_ItemContainerMenu = _ItemContainerMenu
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

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
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.menu.ItemSlot as _ItemSlot
_ItemSlot = _ItemSlot
import dev.ultreon.quantum.menu.EntityContainerMenu as _EntityContainerMenu
_EntityContainerMenu = _EntityContainerMenu
from builtins import bool
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
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.menu.MenuType as _MenuType
_MenuType = _MenuType
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ItemContainerMenu():
    """dev.ultreon.quantum.menu.ItemContainerMenu"""
 
    @staticmethod
    def _wrap(java_value: _ItemContainerMenu) -> 'ItemContainerMenu':
        return ItemContainerMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemContainerMenu):
        """
        Dynamic initializer for ItemContainerMenu.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemContainerMenu__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemContainerMenu__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'._wrap(super(ContainerMenu, self).getWorld())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str._wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getOwner(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.EntityContainerMenu.getOwner()"""
        return 'entity.Entity'._wrap(super(EntityContainerMenu, self).getOwner())

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).addWatcher(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool._wrap(super(ContainerMenu, self).isOnItsOwn())

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool._wrap(super(ContainerMenu, self).hasViewers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'._wrap(super(_ContainerMenu, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).removeWatcher(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).takeItem(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(_ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'._wrap(super(ContainerMenu, self).getType())

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).getItem(_int.valueOf(arg0)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getTitle())

    @overload
    def getHolder(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemContainerMenu.getHolder()"""
        return 'item.ItemStack'._wrap(super(ItemContainerMenu, self).getHolder())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(_ContainerMenu, self).onTakeItem(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2))

    @abstractmethod
    def build(self, ):
        """public abstract void dev.ultreon.quantum.menu.ContainerMenu.build()"""
        pass

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'._wrap(super(ContainerMenu, self).getEntity())

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).setItem(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'._wrap(super(ContainerMenu, self).getPos())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.menu.MenuTypes
import dev.ultreon.quantum.menu.MenuTypes as _MenuTypes
_MenuTypes = _MenuTypes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MenuTypes():
    """dev.ultreon.quantum.menu.MenuTypes"""
 
    @staticmethod
    def _wrap(java_value: _MenuTypes) -> 'MenuTypes':
        return MenuTypes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuTypes):
        """
        Dynamic initializer for MenuTypes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuTypes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuTypes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.menu.MenuType<dev.ultreon.quantum.menu.Inventory> dev.ultreon.quantum.menu.MenuTypes.INVENTORY
    INVENTORY: 'MenuType' = _wrap(_MenuType.INVENTORY)

    # public static final dev.ultreon.quantum.menu.MenuType<dev.ultreon.quantum.menu.CrateMenu> dev.ultreon.quantum.menu.MenuTypes.CRATE
    CRATE: 'MenuType' = _wrap(_MenuType.CRATE)


    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.menu.MenuTypes()"""
        val = _MenuTypes()
        self.__wrapper = val

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.menu.MenuTypes()"""
        val = _MenuTypes()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.menu.BlockContainerMenu
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

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
import dev.ultreon.quantum.block.entity.BlockEntity as _BlockEntity
_BlockEntity = _BlockEntity
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.menu.ItemSlot as _ItemSlot
_ItemSlot = _ItemSlot
from builtins import bool
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
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.menu.BlockContainerMenu as _BlockContainerMenu
_BlockContainerMenu = _BlockContainerMenu
import dev.ultreon.quantum.menu.MenuType as _MenuType
_MenuType = _MenuType
try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockContainerMenu():
    """dev.ultreon.quantum.menu.BlockContainerMenu"""
 
    @staticmethod
    def _wrap(java_value: _BlockContainerMenu) -> 'BlockContainerMenu':
        return BlockContainerMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockContainerMenu):
        """
        Dynamic initializer for BlockContainerMenu.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockContainerMenu__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockContainerMenu__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'._wrap(super(ContainerMenu, self).getWorld())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str._wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).addWatcher(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool._wrap(super(ContainerMenu, self).isOnItsOwn())

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool._wrap(super(ContainerMenu, self).hasViewers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'._wrap(super(_ContainerMenu, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).removeWatcher(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getBlockEntity(self) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.menu.BlockContainerMenu.getBlockEntity()"""
        return 'entity.BlockEntity'._wrap(super(BlockContainerMenu, self).getBlockEntity())

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).takeItem(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(_ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'._wrap(super(ContainerMenu, self).getType())

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).getItem(_int.valueOf(arg0)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(_ContainerMenu, self).onTakeItem(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2))

    @abstractmethod
    def build(self, ):
        """public abstract void dev.ultreon.quantum.menu.ContainerMenu.build()"""
        pass

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'._wrap(super(ContainerMenu, self).getEntity())

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).setItem(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'._wrap(super(ContainerMenu, self).getPos())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.menu.CrateMenu
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.menu.CrateMenu as _CrateMenu
_CrateMenu = _CrateMenu
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.block.entity.CrateBlockEntity as _CrateBlockEntity
_CrateBlockEntity = _CrateBlockEntity
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.menu.ItemSlot as _ItemSlot
_ItemSlot = _ItemSlot
from builtins import bool
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
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.menu.MenuType as _MenuType
_MenuType = _MenuType
try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrateMenu():
    """dev.ultreon.quantum.menu.CrateMenu"""
 
    @staticmethod
    def _wrap(java_value: _CrateMenu) -> 'CrateMenu':
        return CrateMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrateMenu):
        """
        Dynamic initializer for CrateMenu.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrateMenu__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrateMenu__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'._wrap(super(ContainerMenu, self).getWorld())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str._wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).addWatcher(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool._wrap(super(ContainerMenu, self).isOnItsOwn())

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool._wrap(super(ContainerMenu, self).hasViewers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'BlockPos'):
        """public dev.ultreon.quantum.menu.CrateMenu(dev.ultreon.quantum.menu.MenuType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        val = _CrateMenu(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'._wrap(super(_ContainerMenu, self).get(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'CrateBlockEntity', arg4: 'BlockPos'):
        """public dev.ultreon.quantum.menu.CrateMenu(dev.ultreon.quantum.menu.MenuType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.block.entity.CrateBlockEntity,dev.ultreon.quantum.world.BlockPos)"""
        val = _CrateMenu(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).removeWatcher(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).takeItem(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(_ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'._wrap(super(ContainerMenu, self).getType())

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).getItem(_int.valueOf(arg0)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def build(self):
        """public void dev.ultreon.quantum.menu.CrateMenu.build()"""
        super(CrateMenu, self).build()

    @overload
    def setupClient(self, arg0: 'List'):
        """public void dev.ultreon.quantum.menu.CrateMenu.setupClient(java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        super(_CrateMenu, self).setupClient(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(_ContainerMenu, self).onTakeItem(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'._wrap(super(ContainerMenu, self).getEntity())

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).setItem(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getBlockEntity(self) -> 'entity.CrateBlockEntity':
        """public dev.ultreon.quantum.block.entity.CrateBlockEntity dev.ultreon.quantum.menu.CrateMenu.getBlockEntity()"""
        return 'entity.CrateBlockEntity'._wrap(super(CrateMenu, self).getBlockEntity())

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'._wrap(super(ContainerMenu, self).getPos())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.menu.ContainerMenu
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

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
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.menu.ItemSlot as _ItemSlot
_ItemSlot = _ItemSlot
from builtins import bool
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
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.menu.MenuType as _MenuType
_MenuType = _MenuType
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ContainerMenu():
    """dev.ultreon.quantum.menu.ContainerMenu"""
 
    @staticmethod
    def _wrap(java_value: _ContainerMenu) -> 'ContainerMenu':
        return ContainerMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContainerMenu):
        """
        Dynamic initializer for ContainerMenu.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContainerMenu__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContainerMenu__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str._wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool._wrap(super(ContainerMenu, self).isOnItsOwn())

    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool._wrap(super(ContainerMenu, self).hasViewers())

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
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'._wrap(super(_ContainerMenu, self).get(_int.valueOf(arg0)))

    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getCustomTitle())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(_ContainerMenu, self).onTakeItem(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2))

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).takeItem(_int.valueOf(arg0)))

    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).removeWatcher(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).getItem(_int.valueOf(arg0)))

    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getTitle())

    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).addWatcher(arg0)

    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'._wrap(super(ContainerMenu, self).getEntity())

    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'._wrap(super(ContainerMenu, self).getType())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def build(self, ):
        """public abstract void dev.ultreon.quantum.menu.ContainerMenu.build()"""
        pass

    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'._wrap(super(ContainerMenu, self).getWorld())

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).setItem(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(_ContainerMenu, self).setCustomTitle(arg0)

    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'._wrap(super(ContainerMenu, self).getPos())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.menu.MenuType
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.menu.MenuType as _MenuType
_MenuType = _MenuType
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MenuType():
    """dev.ultreon.quantum.menu.MenuType"""
 
    @staticmethod
    def _wrap(java_value: _MenuType) -> 'MenuType':
        return MenuType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuType):
        """
        Dynamic initializer for MenuType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.MenuType.toString()"""
        return str._wrap(super(MenuType, self).toString())

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
    def create(self, arg0: 'World', arg1: 'Entity', arg2: 'BlockPos') -> 'ContainerMenu':
        """public T dev.ultreon.quantum.menu.MenuType.create(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        return 'ContainerMenu'._wrap(super(_MenuType, self).create(arg0, arg1, arg2))

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
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.menu.MenuType.getId()"""
        return 'util.Identifier'._wrap(super(MenuType, self).getId())

    @overload
    def __init__(self, arg0: 'MenuBuilder'):
        """public dev.ultreon.quantum.menu.MenuType(dev.ultreon.quantum.menu.MenuType$MenuBuilder<T>)"""
        val = _MenuType(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.menu.ItemSlot
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.menu.ItemSlot as _ItemSlot
_ItemSlot = _ItemSlot
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ItemSlot():
    """dev.ultreon.quantum.menu.ItemSlot"""
 
    @staticmethod
    def _wrap(java_value: _ItemSlot) -> 'ItemSlot':
        return ItemSlot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemSlot):
        """
        Dynamic initializer for ItemSlot.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemSlot__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemSlot__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def grow(self, arg0: int):
        """public void dev.ultreon.quantum.menu.ItemSlot.grow(int)"""
        super(_ItemSlot, self).grow(_int.valueOf(arg0))

    @overload
    def shrink(self, arg0: int):
        """public void dev.ultreon.quantum.menu.ItemSlot.shrink(int)"""
        super(_ItemSlot, self).shrink(_int.valueOf(arg0))

    @overload
    def getItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.getItem()"""
        return 'item.ItemStack'._wrap(super(ItemSlot, self).getItem())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getContainer(self) -> 'ContainerMenu':
        """public dev.ultreon.quantum.menu.ContainerMenu dev.ultreon.quantum.menu.ItemSlot.getContainer()"""
        return 'ContainerMenu'._wrap(super(ItemSlot, self).getContainer())

    @overload
    def getSlotY(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getSlotY()"""
        return int._wrap(super(ItemSlot, self).getSlotY())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.menu.ItemSlot.isWithinBounds(int,int)"""
        return bool._wrap(super(_ItemSlot, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setItem(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.menu.ItemSlot.setItem(dev.ultreon.quantum.item.ItemStack)"""
        super(_ItemSlot, self).setItem(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ItemSlot.toString()"""
        return str._wrap(super(ItemSlot, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'ContainerMenu', arg2: 'ItemStack', arg3: int, arg4: int):
        """public dev.ultreon.quantum.menu.ItemSlot(int,dev.ultreon.quantum.menu.ContainerMenu,dev.ultreon.quantum.item.ItemStack,int,int)"""
        val = _ItemSlot(_int.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getIndex()"""
        return int._wrap(super(ItemSlot, self).getIndex())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def split(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.split()"""
        return 'item.ItemStack'._wrap(super(ItemSlot, self).split())

    @overload
    def getSlotX(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getSlotX()"""
        return int._wrap(super(ItemSlot, self).getSlotX())

    @overload
    def split(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.split(int)"""
        return 'item.ItemStack'._wrap(super(_ItemSlot, self).split(_int.valueOf(arg0)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ItemSlot.isEmpty()"""
        return bool._wrap(super(ItemSlot, self).isEmpty())

    @overload
    def update(self):
        """public void dev.ultreon.quantum.menu.ItemSlot.update()"""
        super(ItemSlot, self).update()

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
    def setItem(self, arg0: 'ItemStack', arg1: bool) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.setItem(dev.ultreon.quantum.item.ItemStack,boolean)"""
        return 'item.ItemStack'._wrap(super(_ItemSlot, self).setItem(arg0, _boolean.valueOf(arg1)))

    @overload
    def takeItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.takeItem()"""
        return 'item.ItemStack'._wrap(super(ItemSlot, self).takeItem())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.menu.RedirectItemSlot
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.menu.RedirectItemSlot as _RedirectItemSlot
_RedirectItemSlot = _RedirectItemSlot
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.menu.ItemSlot as _ItemSlot
_ItemSlot = _ItemSlot
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RedirectItemSlot():
    """dev.ultreon.quantum.menu.RedirectItemSlot"""
 
    @staticmethod
    def _wrap(java_value: _RedirectItemSlot) -> 'RedirectItemSlot':
        return RedirectItemSlot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RedirectItemSlot):
        """
        Dynamic initializer for RedirectItemSlot.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RedirectItemSlot__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RedirectItemSlot__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.RedirectItemSlot.isEmpty()"""
        return bool._wrap(super(RedirectItemSlot, self).isEmpty())

    @override
    @overload
    def shrink(self, arg0: int):
        """public void dev.ultreon.quantum.menu.RedirectItemSlot.shrink(int)"""
        super(_RedirectItemSlot, self).shrink(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setItem(self, arg0: 'ItemStack', arg1: bool) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.setItem(dev.ultreon.quantum.item.ItemStack,boolean)"""
        return 'item.ItemStack'._wrap(super(_RedirectItemSlot, self).setItem(arg0, _boolean.valueOf(arg1)))

    @overload
    def split(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.split(int)"""
        return 'item.ItemStack'._wrap(super(_RedirectItemSlot, self).split(_int.valueOf(arg0)))

    @override
    @overload
    def takeItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.takeItem()"""
        return 'item.ItemStack'._wrap(super(RedirectItemSlot, self).takeItem())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.menu.ItemSlot.isWithinBounds(int,int)"""
        return bool._wrap(super(_ItemSlot, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getContainer(self) -> 'ContainerMenu':
        """public dev.ultreon.quantum.menu.ContainerMenu dev.ultreon.quantum.menu.RedirectItemSlot.getContainer()"""
        return 'ContainerMenu'._wrap(super(RedirectItemSlot, self).getContainer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def split(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.split()"""
        return 'item.ItemStack'._wrap(super(RedirectItemSlot, self).split())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getIndex()"""
        return int._wrap(super(ItemSlot, self).getIndex())

    @override
    @overload
    def update(self):
        """public void dev.ultreon.quantum.menu.RedirectItemSlot.update()"""
        super(RedirectItemSlot, self).update()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.RedirectItemSlot.toString()"""
        return str._wrap(super(RedirectItemSlot, self).toString())

    @override
    @overload
    def grow(self, arg0: int):
        """public void dev.ultreon.quantum.menu.RedirectItemSlot.grow(int)"""
        super(_RedirectItemSlot, self).grow(_int.valueOf(arg0))

    @override
    @overload
    def getSlotX(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getSlotX()"""
        return int._wrap(super(ItemSlot, self).getSlotX())

    @override
    @overload
    def getSlotY(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getSlotY()"""
        return int._wrap(super(ItemSlot, self).getSlotY())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.getItem()"""
        return 'item.ItemStack'._wrap(super(RedirectItemSlot, self).getItem())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: 'ItemSlot', arg2: int, arg3: int):
        """public dev.ultreon.quantum.menu.RedirectItemSlot(int,dev.ultreon.quantum.menu.ItemSlot,int,int)"""
        val = _RedirectItemSlot(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def setItem(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.menu.RedirectItemSlot.setItem(dev.ultreon.quantum.item.ItemStack)"""
        super(_RedirectItemSlot, self).setItem(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.menu.Inventory
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.menu.Inventory as _Inventory
_Inventory = _Inventory
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.menu.ItemSlot as _ItemSlot
_ItemSlot = _ItemSlot
from builtins import bool
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
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.menu.MenuType as _MenuType
_MenuType = _MenuType
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.entity.player.Player as _Player
_Player = _Player
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Inventory():
    """dev.ultreon.quantum.menu.Inventory"""
 
    @staticmethod
    def _wrap(java_value: _Inventory) -> 'Inventory':
        return Inventory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Inventory):
        """
        Dynamic initializer for Inventory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Inventory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Inventory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getHotbarSlot(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.Inventory.getHotbarSlot(int)"""
        return 'ItemSlot'._wrap(super(_Inventory, self).getHotbarSlot(_int.valueOf(arg0)))

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'._wrap(super(ContainerMenu, self).getWorld())

    @overload
    def addItem(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.menu.Inventory.addItem(dev.ultreon.quantum.item.ItemStack)"""
        return bool._wrap(super(_Inventory, self).addItem(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str._wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addItems(self, arg0: 'Iterable') -> bool:
        """public boolean dev.ultreon.quantum.menu.Inventory.addItems(java.lang.Iterable<dev.ultreon.quantum.item.ItemStack>)"""
        return bool._wrap(super(_Inventory, self).addItems(arg0))

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).addWatcher(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool._wrap(super(ContainerMenu, self).isOnItsOwn())

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool._wrap(super(ContainerMenu, self).hasViewers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'._wrap(super(_ContainerMenu, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).removeWatcher(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'BlockPos'):
        """public dev.ultreon.quantum.menu.Inventory(dev.ultreon.quantum.menu.MenuType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        val = _Inventory(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).takeItem(_int.valueOf(arg0)))

    @overload
    def getHotbarSlots(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.menu.ItemSlot> dev.ultreon.quantum.menu.Inventory.getHotbarSlots()"""
        return 'List'._wrap(super(Inventory, self).getHotbarSlots())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(_ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'._wrap(super(ContainerMenu, self).getType())

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).getItem(_int.valueOf(arg0)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def build(self):
        """public void dev.ultreon.quantum.menu.Inventory.build()"""
        super(Inventory, self).build()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(_ContainerMenu, self).onTakeItem(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'._wrap(super(ContainerMenu, self).getEntity())

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).setItem(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getHolder(self) -> 'player.Player':
        """public dev.ultreon.quantum.entity.player.Player dev.ultreon.quantum.menu.Inventory.getHolder()"""
        return 'player.Player'._wrap(super(Inventory, self).getHolder())

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'._wrap(super(ContainerMenu, self).getPos())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.menu.EntityContainerMenu
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

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
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.menu.ItemSlot as _ItemSlot
_ItemSlot = _ItemSlot
import dev.ultreon.quantum.menu.EntityContainerMenu as _EntityContainerMenu
_EntityContainerMenu = _EntityContainerMenu
from builtins import bool
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
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.menu.ContainerMenu as _ContainerMenu
_ContainerMenu = _ContainerMenu
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.menu.MenuType as _MenuType
_MenuType = _MenuType
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.world.World as _World
_World = _World
import dev.ultreon.quantum.world.BlockPos as _BlockPos
_BlockPos = _BlockPos
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityContainerMenu():
    """dev.ultreon.quantum.menu.EntityContainerMenu"""
 
    @staticmethod
    def _wrap(java_value: _EntityContainerMenu) -> 'EntityContainerMenu':
        return EntityContainerMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityContainerMenu):
        """
        Dynamic initializer for EntityContainerMenu.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityContainerMenu__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityContainerMenu__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'._wrap(super(ContainerMenu, self).getWorld())

    @overload
    def getOwner(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.EntityContainerMenu.getOwner()"""
        return 'entity.Entity'._wrap(super(EntityContainerMenu, self).getOwner())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str._wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).addWatcher(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool._wrap(super(ContainerMenu, self).isOnItsOwn())

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool._wrap(super(ContainerMenu, self).hasViewers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'._wrap(super(_ContainerMenu, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(_ContainerMenu, self).removeWatcher(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).takeItem(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(_ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'._wrap(super(ContainerMenu, self).getType())

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).getItem(_int.valueOf(arg0)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'._wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(_ContainerMenu, self).onTakeItem(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2))

    @abstractmethod
    def build(self, ):
        """public abstract void dev.ultreon.quantum.menu.ContainerMenu.build()"""
        pass

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'._wrap(super(ContainerMenu, self).getEntity())

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'._wrap(super(_ContainerMenu, self).setItem(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'._wrap(super(ContainerMenu, self).getPos())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())