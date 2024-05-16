from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.menu.MenuType as __MenuType_MenuBuilder
__MenuBuilder = __MenuType_MenuBuilder.MenuBuilder
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from abc import abstractmethod, ABC
 
class MenuBuilder(ABC):
    """dev.ultreon.quantum.menu.MenuType.MenuBuilder"""
 
    @staticmethod
    def __wrap(java_value: __MenuBuilder) -> 'MenuBuilder':
        return MenuBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuBuilder):
        """
        Dynamic initializer for MenuBuilder.
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
    def create(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'BlockPos'):
        """public abstract T dev.ultreon.quantum.menu.MenuType$MenuBuilder.create(dev.ultreon.quantum.menu.MenuType<T>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.menu.MenuType$MenuBuilder
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.menu.MenuType as __MenuType_MenuBuilder
__MenuBuilder = __MenuType_MenuBuilder.MenuBuilder
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from abc import abstractmethod, ABC
 
class MenuBuilder(ABC):
    """dev.ultreon.quantum.menu.MenuType.MenuBuilder"""
 
    @staticmethod
    def __wrap(java_value: __MenuBuilder) -> 'MenuBuilder':
        return MenuBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuBuilder):
        """
        Dynamic initializer for MenuBuilder.
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
    def create(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'BlockPos'):
        """public abstract T dev.ultreon.quantum.menu.MenuType$MenuBuilder.create(dev.ultreon.quantum.menu.MenuType<T>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.menu.MenuType$MenuBuilder 
 
 
# CLASS: dev.ultreon.quantum.menu.ItemContainerMenu
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
from builtins import bool
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

import dev.ultreon.quantum.menu.ItemContainerMenu as __ItemContainerMenu
__ItemContainerMenu = __ItemContainerMenu
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.menu.EntityContainerMenu as __EntityContainerMenu
__EntityContainerMenu = __EntityContainerMenu
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
import dev.ultreon.quantum.menu.MenuType as __MenuType
__MenuType = __MenuType
from builtins import int
 
class ItemContainerMenu(ABC, __EntityContainerMenu, EntityContainerMenu):
    """dev.ultreon.quantum.menu.ItemContainerMenu"""
 
    @staticmethod
    def __wrap(java_value: __ItemContainerMenu) -> 'ItemContainerMenu':
        return ItemContainerMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemContainerMenu):
        """
        Dynamic initializer for ItemContainerMenu.
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
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(__ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).setItem(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool.__wrap(super(ContainerMenu, self).hasViewers())

    @overload
    def getHolder(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemContainerMenu.getHolder()"""
        return 'item.ItemStack'.__wrap(super(ItemContainerMenu, self).getHolder())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str.__wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'.__wrap(super(ContainerMenu, self).getWorld())

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool.__wrap(super(ContainerMenu, self).isOnItsOwn())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).addWatcher(arg0)

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).takeItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).removeWatcher(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'.__wrap(super(__ContainerMenu, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'.__wrap(super(ContainerMenu, self).getType())

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'.__wrap(super(ContainerMenu, self).getEntity())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(__ContainerMenu, self).onTakeItem(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def getOwner(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.EntityContainerMenu.getOwner()"""
        return 'entity.Entity'.__wrap(super(EntityContainerMenu, self).getOwner())

    @abstractmethod
    def build(self, ):
        """public abstract void dev.ultreon.quantum.menu.ContainerMenu.build()"""
        pass

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).getItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'.__wrap(super(ContainerMenu, self).getPos()) 
 
 
# CLASS: dev.ultreon.quantum.menu.MenuTypes
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.menu.MenuTypes as __MenuTypes
__MenuTypes = __MenuTypes
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MenuTypes():
    """dev.ultreon.quantum.menu.MenuTypes"""
 
    @staticmethod
    def __wrap(java_value: __MenuTypes) -> 'MenuTypes':
        return MenuTypes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuTypes):
        """
        Dynamic initializer for MenuTypes.
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
 
    # public static final dev.ultreon.quantum.menu.MenuType<dev.ultreon.quantum.menu.Inventory> dev.ultreon.quantum.menu.MenuTypes.INVENTORY
    INVENTORY: 'MenuType' = __wrap(__MenuType.INVENTORY)

    # public static final dev.ultreon.quantum.menu.MenuType<dev.ultreon.quantum.menu.CrateMenu> dev.ultreon.quantum.menu.MenuTypes.CRATE
    CRATE: 'MenuType' = __wrap(__MenuType.CRATE)


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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.menu.MenuTypes()"""
        val = __MenuTypes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.menu.MenuTypes()"""
        val = __MenuTypes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.menu.BlockContainerMenu
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
import dev.ultreon.quantum.block.entity.BlockEntity as __BlockEntity
__BlockEntity = __BlockEntity
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
from builtins import bool
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
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.menu.BlockContainerMenu as __BlockContainerMenu
__BlockContainerMenu = __BlockContainerMenu
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
import dev.ultreon.quantum.menu.MenuType as __MenuType
__MenuType = __MenuType
from builtins import int
 
class BlockContainerMenu(ABC, __ContainerMenu, ContainerMenu):
    """dev.ultreon.quantum.menu.BlockContainerMenu"""
 
    @staticmethod
    def __wrap(java_value: __BlockContainerMenu) -> 'BlockContainerMenu':
        return BlockContainerMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockContainerMenu):
        """
        Dynamic initializer for BlockContainerMenu.
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
    def getBlockEntity(self) -> 'entity.BlockEntity':
        """public dev.ultreon.quantum.block.entity.BlockEntity dev.ultreon.quantum.menu.BlockContainerMenu.getBlockEntity()"""
        return 'entity.BlockEntity'.__wrap(super(BlockContainerMenu, self).getBlockEntity())

    @override
    @overload
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(__ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).setItem(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool.__wrap(super(ContainerMenu, self).hasViewers())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str.__wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'.__wrap(super(ContainerMenu, self).getWorld())

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool.__wrap(super(ContainerMenu, self).isOnItsOwn())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).addWatcher(arg0)

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).takeItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).removeWatcher(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'.__wrap(super(__ContainerMenu, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'.__wrap(super(ContainerMenu, self).getType())

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'.__wrap(super(ContainerMenu, self).getEntity())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(__ContainerMenu, self).onTakeItem(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))

    @abstractmethod
    def build(self, ):
        """public abstract void dev.ultreon.quantum.menu.ContainerMenu.build()"""
        pass

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).getItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'.__wrap(super(ContainerMenu, self).getPos()) 
 
 
# CLASS: dev.ultreon.quantum.menu.CrateMenu
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
import dev.ultreon.quantum.menu.CrateMenu as __CrateMenu
__CrateMenu = __CrateMenu
import dev.ultreon.quantum.block.entity.CrateBlockEntity as __CrateBlockEntity
__CrateBlockEntity = __CrateBlockEntity
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
from builtins import bool
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
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
import dev.ultreon.quantum.menu.MenuType as __MenuType
__MenuType = __MenuType
import java.util.List as List
from builtins import int
 
class CrateMenu(__BlockContainerMenu, BlockContainerMenu):
    """dev.ultreon.quantum.menu.CrateMenu"""
 
    @staticmethod
    def __wrap(java_value: __CrateMenu) -> 'CrateMenu':
        return CrateMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrateMenu):
        """
        Dynamic initializer for CrateMenu.
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
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(__ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).setItem(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'CrateBlockEntity', arg4: 'BlockPos'):
        """public dev.ultreon.quantum.menu.CrateMenu(dev.ultreon.quantum.menu.MenuType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.block.entity.CrateBlockEntity,dev.ultreon.quantum.world.BlockPos)"""
        val = __CrateMenu(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool.__wrap(super(ContainerMenu, self).hasViewers())

    @override
    @overload
    def getBlockEntity(self) -> 'entity.CrateBlockEntity':
        """public dev.ultreon.quantum.block.entity.CrateBlockEntity dev.ultreon.quantum.menu.CrateMenu.getBlockEntity()"""
        return 'entity.CrateBlockEntity'.__wrap(super(CrateMenu, self).getBlockEntity())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'BlockPos'):
        """public dev.ultreon.quantum.menu.CrateMenu(dev.ultreon.quantum.menu.MenuType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        val = __CrateMenu(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str.__wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'.__wrap(super(ContainerMenu, self).getWorld())

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool.__wrap(super(ContainerMenu, self).isOnItsOwn())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setupClient(self, arg0: 'List'):
        """public void dev.ultreon.quantum.menu.CrateMenu.setupClient(java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        super(__CrateMenu, self).setupClient(arg0)

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).addWatcher(arg0)

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).takeItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).removeWatcher(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'.__wrap(super(__ContainerMenu, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'.__wrap(super(ContainerMenu, self).getType())

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'.__wrap(super(ContainerMenu, self).getEntity())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(__ContainerMenu, self).onTakeItem(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def build(self):
        """public void dev.ultreon.quantum.menu.CrateMenu.build()"""
        super(CrateMenu, self).build()

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).getItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'.__wrap(super(ContainerMenu, self).getPos()) 
 
 
# CLASS: dev.ultreon.quantum.menu.ContainerMenu
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
from builtins import bool
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
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.MenuType as __MenuType
__MenuType = __MenuType
from builtins import int
 
class ContainerMenu(ABC):
    """dev.ultreon.quantum.menu.ContainerMenu"""
 
    @staticmethod
    def __wrap(java_value: __ContainerMenu) -> 'ContainerMenu':
        return ContainerMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContainerMenu):
        """
        Dynamic initializer for ContainerMenu.
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
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool.__wrap(super(ContainerMenu, self).isOnItsOwn())

    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'.__wrap(super(ContainerMenu, self).getPos())

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).setItem(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'.__wrap(super(ContainerMenu, self).getEntity())

    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getCustomTitle())

    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).addWatcher(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str.__wrap(super(ContainerMenu, self).toString())

    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(__ContainerMenu, self).onTakeItem(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'.__wrap(super(ContainerMenu, self).getType())

    @overload
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(__ContainerMenu, self).setCustomTitle(arg0)

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).takeItem(__int.valueOf(arg0)))

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
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'.__wrap(super(__ContainerMenu, self).get(__int.valueOf(arg0)))

    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).removeWatcher(arg0)

    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool.__wrap(super(ContainerMenu, self).hasViewers())

    @abstractmethod
    def build(self, ):
        """public abstract void dev.ultreon.quantum.menu.ContainerMenu.build()"""
        pass

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).getItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'.__wrap(super(ContainerMenu, self).getWorld()) 
 
 
# CLASS: dev.ultreon.quantum.menu.MenuType
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
from builtins import type
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
import dev.ultreon.quantum.menu.MenuType as __MenuType
__MenuType = __MenuType
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MenuType():
    """dev.ultreon.quantum.menu.MenuType"""
 
    @staticmethod
    def __wrap(java_value: __MenuType) -> 'MenuType':
        return MenuType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuType):
        """
        Dynamic initializer for MenuType.
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

    @overload
    def create(self, arg0: 'World', arg1: 'Entity', arg2: 'BlockPos') -> 'ContainerMenu':
        """public T dev.ultreon.quantum.menu.MenuType.create(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        return 'ContainerMenu'.__wrap(super(__MenuType, self).create(arg0, arg1, arg2))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.MenuType.toString()"""
        return str.__wrap(super(MenuType, self).toString())

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
    def __init__(self, arg0: 'MenuBuilder'):
        """public dev.ultreon.quantum.menu.MenuType(dev.ultreon.quantum.menu.MenuType$MenuBuilder<T>)"""
        val = __MenuType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.menu.MenuType.getId()"""
        return 'util.Identifier'.__wrap(super(MenuType, self).getId()) 
 
 
# CLASS: dev.ultreon.quantum.menu.ItemSlot
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
from builtins import bool
from builtins import int
 
class ItemSlot():
    """dev.ultreon.quantum.menu.ItemSlot"""
 
    @staticmethod
    def __wrap(java_value: __ItemSlot) -> 'ItemSlot':
        return ItemSlot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemSlot):
        """
        Dynamic initializer for ItemSlot.
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
    def __init__(self, arg0: int, arg1: 'ContainerMenu', arg2: 'ItemStack', arg3: int, arg4: int):
        """public dev.ultreon.quantum.menu.ItemSlot(int,dev.ultreon.quantum.menu.ContainerMenu,dev.ultreon.quantum.item.ItemStack,int,int)"""
        val = __ItemSlot(__int.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setItem(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.menu.ItemSlot.setItem(dev.ultreon.quantum.item.ItemStack)"""
        super(__ItemSlot, self).setItem(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def takeItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.takeItem()"""
        return 'item.ItemStack'.__wrap(super(ItemSlot, self).takeItem())

    @overload
    def getSlotY(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getSlotY()"""
        return int.__wrap(super(ItemSlot, self).getSlotY())

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
    def split(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.split(int)"""
        return 'item.ItemStack'.__wrap(super(__ItemSlot, self).split(__int.valueOf(arg0)))

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getIndex()"""
        return int.__wrap(super(ItemSlot, self).getIndex())

    @overload
    def getItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.getItem()"""
        return 'item.ItemStack'.__wrap(super(ItemSlot, self).getItem())

    @overload
    def setItem(self, arg0: 'ItemStack', arg1: bool) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.setItem(dev.ultreon.quantum.item.ItemStack,boolean)"""
        return 'item.ItemStack'.__wrap(super(__ItemSlot, self).setItem(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ItemSlot.toString()"""
        return str.__wrap(super(ItemSlot, self).toString())

    @overload
    def getContainer(self) -> 'ContainerMenu':
        """public dev.ultreon.quantum.menu.ContainerMenu dev.ultreon.quantum.menu.ItemSlot.getContainer()"""
        return 'ContainerMenu'.__wrap(super(ItemSlot, self).getContainer())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.menu.ItemSlot.isWithinBounds(int,int)"""
        return bool.__wrap(super(__ItemSlot, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def shrink(self, arg0: int):
        """public void dev.ultreon.quantum.menu.ItemSlot.shrink(int)"""
        super(__ItemSlot, self).shrink(__int.valueOf(arg0))

    @overload
    def grow(self, arg0: int):
        """public void dev.ultreon.quantum.menu.ItemSlot.grow(int)"""
        super(__ItemSlot, self).grow(__int.valueOf(arg0))

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
    def update(self):
        """public void dev.ultreon.quantum.menu.ItemSlot.update()"""
        super(ItemSlot, self).update()

    @overload
    def split(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ItemSlot.split()"""
        return 'item.ItemStack'.__wrap(super(ItemSlot, self).split())

    @overload
    def getSlotX(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getSlotX()"""
        return int.__wrap(super(ItemSlot, self).getSlotX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ItemSlot.isEmpty()"""
        return bool.__wrap(super(ItemSlot, self).isEmpty()) 
 
 
# CLASS: dev.ultreon.quantum.menu.RedirectItemSlot
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.menu.RedirectItemSlot as __RedirectItemSlot
__RedirectItemSlot = __RedirectItemSlot
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
from builtins import bool
from builtins import int
 
class RedirectItemSlot(__ItemSlot, ItemSlot):
    """dev.ultreon.quantum.menu.RedirectItemSlot"""
 
    @staticmethod
    def __wrap(java_value: __RedirectItemSlot) -> 'RedirectItemSlot':
        return RedirectItemSlot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RedirectItemSlot):
        """
        Dynamic initializer for RedirectItemSlot.
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
    def getItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.getItem()"""
        return 'item.ItemStack'.__wrap(super(RedirectItemSlot, self).getItem())

    @overload
    def split(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.split(int)"""
        return 'item.ItemStack'.__wrap(super(__RedirectItemSlot, self).split(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: 'ItemSlot', arg2: int, arg3: int):
        """public dev.ultreon.quantum.menu.RedirectItemSlot(int,dev.ultreon.quantum.menu.ItemSlot,int,int)"""
        val = __RedirectItemSlot(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getSlotY(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getSlotY()"""
        return int.__wrap(super(ItemSlot, self).getSlotY())

    @override
    @overload
    def setItem(self, arg0: 'ItemStack'):
        """public void dev.ultreon.quantum.menu.RedirectItemSlot.setItem(dev.ultreon.quantum.item.ItemStack)"""
        super(__RedirectItemSlot, self).setItem(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.RedirectItemSlot.toString()"""
        return str.__wrap(super(RedirectItemSlot, self).toString())

    @override
    @overload
    def takeItem(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.takeItem()"""
        return 'item.ItemStack'.__wrap(super(RedirectItemSlot, self).takeItem())

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
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public boolean dev.ultreon.quantum.menu.ItemSlot.isWithinBounds(int,int)"""
        return bool.__wrap(super(__ItemSlot, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def update(self):
        """public void dev.ultreon.quantum.menu.RedirectItemSlot.update()"""
        super(RedirectItemSlot, self).update()

    @overload
    def setItem(self, arg0: 'ItemStack', arg1: bool) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.setItem(dev.ultreon.quantum.item.ItemStack,boolean)"""
        return 'item.ItemStack'.__wrap(super(__RedirectItemSlot, self).setItem(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.RedirectItemSlot.isEmpty()"""
        return bool.__wrap(super(RedirectItemSlot, self).isEmpty())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getIndex()"""
        return int.__wrap(super(ItemSlot, self).getIndex())

    @override
    @overload
    def getSlotX(self) -> int:
        """public int dev.ultreon.quantum.menu.ItemSlot.getSlotX()"""
        return int.__wrap(super(ItemSlot, self).getSlotX())

    @override
    @overload
    def shrink(self, arg0: int):
        """public void dev.ultreon.quantum.menu.RedirectItemSlot.shrink(int)"""
        super(__RedirectItemSlot, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def split(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.RedirectItemSlot.split()"""
        return 'item.ItemStack'.__wrap(super(RedirectItemSlot, self).split())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getContainer(self) -> 'ContainerMenu':
        """public dev.ultreon.quantum.menu.ContainerMenu dev.ultreon.quantum.menu.RedirectItemSlot.getContainer()"""
        return 'ContainerMenu'.__wrap(super(RedirectItemSlot, self).getContainer())

    @override
    @overload
    def grow(self, arg0: int):
        """public void dev.ultreon.quantum.menu.RedirectItemSlot.grow(int)"""
        super(__RedirectItemSlot, self).grow(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.menu.Inventory
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import dev.ultreon.quantum.entity.player.Player as __Player
__Player = __Player
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
from builtins import bool
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
import dev.ultreon.quantum.menu.Inventory as __Inventory
__Inventory = __Inventory
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
import dev.ultreon.quantum.menu.MenuType as __MenuType
__MenuType = __MenuType
import java.util.List as List
from builtins import int
 
class Inventory(__ContainerMenu, ContainerMenu):
    """dev.ultreon.quantum.menu.Inventory"""
 
    @staticmethod
    def __wrap(java_value: __Inventory) -> 'Inventory':
        return Inventory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Inventory):
        """
        Dynamic initializer for Inventory.
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
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(__ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getHotbarSlot(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.Inventory.getHotbarSlot(int)"""
        return 'ItemSlot'.__wrap(super(__Inventory, self).getHotbarSlot(__int.valueOf(arg0)))

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).setItem(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool.__wrap(super(ContainerMenu, self).hasViewers())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str.__wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'.__wrap(super(ContainerMenu, self).getWorld())

    @overload
    def getHotbarSlots(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.menu.ItemSlot> dev.ultreon.quantum.menu.Inventory.getHotbarSlots()"""
        return 'List'.__wrap(super(Inventory, self).getHotbarSlots())

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool.__wrap(super(ContainerMenu, self).isOnItsOwn())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addItem(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.menu.Inventory.addItem(dev.ultreon.quantum.item.ItemStack)"""
        return bool.__wrap(super(__Inventory, self).addItem(arg0))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).addWatcher(arg0)

    @overload
    def getHolder(self) -> 'player.Player':
        """public dev.ultreon.quantum.entity.player.Player dev.ultreon.quantum.menu.Inventory.getHolder()"""
        return 'player.Player'.__wrap(super(Inventory, self).getHolder())

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).takeItem(__int.valueOf(arg0)))

    @overload
    def addItems(self, arg0: 'Iterable') -> bool:
        """public boolean dev.ultreon.quantum.menu.Inventory.addItems(java.lang.Iterable<dev.ultreon.quantum.item.ItemStack>)"""
        return bool.__wrap(super(__Inventory, self).addItems(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'MenuType', arg1: 'World', arg2: 'Entity', arg3: 'BlockPos'):
        """public dev.ultreon.quantum.menu.Inventory(dev.ultreon.quantum.menu.MenuType<?>,dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.world.BlockPos)"""
        val = __Inventory(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def build(self):
        """public void dev.ultreon.quantum.menu.Inventory.build()"""
        super(Inventory, self).build()

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).removeWatcher(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'.__wrap(super(__ContainerMenu, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'.__wrap(super(ContainerMenu, self).getType())

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'.__wrap(super(ContainerMenu, self).getEntity())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(__ContainerMenu, self).onTakeItem(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).getItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'.__wrap(super(ContainerMenu, self).getPos()) 
 
 
# CLASS: dev.ultreon.quantum.menu.EntityContainerMenu
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.World as __World
__World = __World
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
from builtins import bool
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
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.menu.EntityContainerMenu as __EntityContainerMenu
__EntityContainerMenu = __EntityContainerMenu
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.menu.ContainerMenu as __ContainerMenu
__ContainerMenu = __ContainerMenu
import dev.ultreon.quantum.menu.MenuType as __MenuType
__MenuType = __MenuType
from builtins import int
 
class EntityContainerMenu(ABC, __ContainerMenu, ContainerMenu):
    """dev.ultreon.quantum.menu.EntityContainerMenu"""
 
    @staticmethod
    def __wrap(java_value: __EntityContainerMenu) -> 'EntityContainerMenu':
        return EntityContainerMenu(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityContainerMenu):
        """
        Dynamic initializer for EntityContainerMenu.
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
    def setCustomTitle(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.setCustomTitle(dev.ultreon.quantum.text.TextObject)"""
        super(__ContainerMenu, self).setCustomTitle(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).setItem(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasViewers(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.hasViewers()"""
        return bool.__wrap(super(ContainerMenu, self).hasViewers())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.menu.ContainerMenu.toString()"""
        return str.__wrap(super(ContainerMenu, self).toString())

    @override
    @overload
    def getWorld(self) -> 'world.World':
        """public dev.ultreon.quantum.world.World dev.ultreon.quantum.menu.ContainerMenu.getWorld()"""
        return 'world.World'.__wrap(super(ContainerMenu, self).getWorld())

    @override
    @overload
    def isOnItsOwn(self) -> bool:
        """public boolean dev.ultreon.quantum.menu.ContainerMenu.isOnItsOwn()"""
        return bool.__wrap(super(ContainerMenu, self).isOnItsOwn())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getTitle())

    @override
    @overload
    def addWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.addWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).addWatcher(arg0)

    @overload
    def getOwner(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.EntityContainerMenu.getOwner()"""
        return 'entity.Entity'.__wrap(super(EntityContainerMenu, self).getOwner())

    @overload
    def takeItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.takeItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).takeItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def removeWatcher(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.menu.ContainerMenu.removeWatcher(dev.ultreon.quantum.entity.player.Player)"""
        super(__ContainerMenu, self).removeWatcher(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: int) -> 'ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.menu.ContainerMenu.get(int)"""
        return 'ItemSlot'.__wrap(super(__ContainerMenu, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def getType(self) -> 'MenuType':
        """public dev.ultreon.quantum.menu.MenuType<?> dev.ultreon.quantum.menu.ContainerMenu.getType()"""
        return 'MenuType'.__wrap(super(ContainerMenu, self).getType())

    @override
    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.menu.ContainerMenu.getEntity()"""
        return 'entity.Entity'.__wrap(super(ContainerMenu, self).getEntity())

    @override
    @overload
    def onTakeItem(self, arg0: 'ServerPlayer', arg1: int, arg2: bool):
        """public void dev.ultreon.quantum.menu.ContainerMenu.onTakeItem(dev.ultreon.quantum.server.player.ServerPlayer,int,boolean)"""
        super(__ContainerMenu, self).onTakeItem(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))

    @abstractmethod
    def build(self, ):
        """public abstract void dev.ultreon.quantum.menu.ContainerMenu.build()"""
        pass

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.menu.ContainerMenu.getItem(int)"""
        return 'item.ItemStack'.__wrap(super(__ContainerMenu, self).getItem(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCustomTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.menu.ContainerMenu.getCustomTitle()"""
        return 'text.TextObject'.__wrap(super(ContainerMenu, self).getCustomTitle())

    @override
    @overload
    def getPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.menu.ContainerMenu.getPos()"""
        return 'world.BlockPos'.__wrap(super(ContainerMenu, self).getPos())