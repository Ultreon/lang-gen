from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.world.container.ContainerView as __ContainerView
__ContainerView = __ContainerView
 
class ContainerView(ABC):
    """dev.ultreon.quantum.world.container.ContainerView"""
 
    @staticmethod
    def __wrap(java_value: __ContainerView) -> 'ContainerView':
        return ContainerView(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContainerView):
        """
        Dynamic initializer for ContainerView.
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
    def hasPlaceFor(self, arg0: 'ItemStack'):
        """public abstract boolean dev.ultreon.quantum.world.container.ContainerView.hasPlaceFor(dev.ultreon.quantum.item.ItemStack)"""
        pass

    @abstractmethod
    def onItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.world.container.ContainerView.onItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        pass

    @abstractmethod
    def onSlotClick(self, arg0: int, arg1: 'Player', arg2: 'ContainerInteraction'):
        """public abstract void dev.ultreon.quantum.world.container.ContainerView.onSlotClick(int,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.container.ContainerInteraction)"""
        pass

    @abstractmethod
    def onContainerClosed(self, arg0: 'Player'):
        """public abstract void dev.ultreon.quantum.world.container.ContainerView.onContainerClosed(dev.ultreon.quantum.entity.player.Player)"""
        pass

    @abstractmethod
    def moveInto(self, arg0: 'ItemStack'):
        """public abstract dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.world.container.ContainerView.moveInto(dev.ultreon.quantum.item.ItemStack)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.world.container.ContainerView
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.world.container.ContainerView as __ContainerView
__ContainerView = __ContainerView
 
class ContainerView(ABC):
    """dev.ultreon.quantum.world.container.ContainerView"""
 
    @staticmethod
    def __wrap(java_value: __ContainerView) -> 'ContainerView':
        return ContainerView(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContainerView):
        """
        Dynamic initializer for ContainerView.
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
    def hasPlaceFor(self, arg0: 'ItemStack'):
        """public abstract boolean dev.ultreon.quantum.world.container.ContainerView.hasPlaceFor(dev.ultreon.quantum.item.ItemStack)"""
        pass

    @abstractmethod
    def onItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.world.container.ContainerView.onItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        pass

    @abstractmethod
    def onSlotClick(self, arg0: int, arg1: 'Player', arg2: 'ContainerInteraction'):
        """public abstract void dev.ultreon.quantum.world.container.ContainerView.onSlotClick(int,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.container.ContainerInteraction)"""
        pass

    @abstractmethod
    def onContainerClosed(self, arg0: 'Player'):
        """public abstract void dev.ultreon.quantum.world.container.ContainerView.onContainerClosed(dev.ultreon.quantum.entity.player.Player)"""
        pass

    @abstractmethod
    def moveInto(self, arg0: 'ItemStack'):
        """public abstract dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.world.container.ContainerView.moveInto(dev.ultreon.quantum.item.ItemStack)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.world.container.ContainerView 
 
 
# CLASS: dev.ultreon.quantum.world.container.ContainerInteraction
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.world.container.ContainerInteraction as __ContainerInteraction
__ContainerInteraction = __ContainerInteraction
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
from builtins import int
 
class ContainerInteraction():
    """dev.ultreon.quantum.world.container.ContainerInteraction"""
 
    @staticmethod
    def __wrap(java_value: __ContainerInteraction) -> 'ContainerInteraction':
        return ContainerInteraction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContainerInteraction):
        """
        Dynamic initializer for ContainerInteraction.
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
 
    # public static final dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.DROP
    DROP: 'ContainerInteraction' = __wrap(__ContainerInteraction.DROP)

    # public static final dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.PLACE
    PLACE: 'ContainerInteraction' = __wrap(__ContainerInteraction.PLACE)

    # public static final dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.SPLIT
    SPLIT: 'ContainerInteraction' = __wrap(__ContainerInteraction.SPLIT)

    # public static final dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.TAKE
    TAKE: 'ContainerInteraction' = __wrap(__ContainerInteraction.TAKE)

    # public static final dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.PlACE_ONE
    PlACE_ONE: 'ContainerInteraction' = __wrap(__ContainerInteraction.PlACE_ONE)

    # public static final dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.QUICK_MOVE
    QUICK_MOVE: 'ContainerInteraction' = __wrap(__ContainerInteraction.QUICK_MOVE)

    # public static final dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.MERGE
    MERGE: 'ContainerInteraction' = __wrap(__ContainerInteraction.MERGE)


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

    @staticmethod
    @overload
    def values() -> List['ContainerInteraction']:
        """public static dev.ultreon.quantum.world.container.ContainerInteraction[] dev.ultreon.quantum.world.container.ContainerInteraction.values()"""
        return List[ContainerInteraction].__wrap(__ContainerInteraction.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ContainerInteraction':
        """public static dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.valueOf(java.lang.String)"""
        return ContainerInteraction.__wrap(__ContainerInteraction.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.container.Container
from pyquantum_helper import import_once as __import_once__
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
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.container.Container as __Container
__Container = __Container
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

from builtins import int
import java.util.List as List
 
class Container(ABC):
    """dev.ultreon.quantum.world.container.Container"""
 
    @staticmethod
    def __wrap(java_value: __Container) -> 'Container':
        return Container(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Container):
        """
        Dynamic initializer for Container.
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
    def removeWatcher(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.world.container.Container.removeWatcher(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__Container, self).removeWatcher(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onContainerClosed(self, arg0: 'Player'):
        """public final void dev.ultreon.quantum.world.container.Container.onContainerClosed(dev.ultreon.quantum.entity.player.Player)"""
        super(__Container, self).onContainerClosed(arg0)

    @overload
    def addWatcher(self, arg0: 'ServerPlayer', arg1: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.container.Container.addWatcher(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.menu.ContainerMenu)"""
        super(__Container, self).addWatcher(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.world.container.Container.getItem(int)"""
        return 'item.ItemStack'.__wrap(super(__Container, self).getItem(__int.valueOf(arg0)))

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.world.container.Container.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__Container, self).setItem(__int.valueOf(arg0), arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.container.Container(int)"""
        val = __Container(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getContainerSize(self) -> int:
        """public final int dev.ultreon.quantum.world.container.Container.getContainerSize()"""
        return int.__wrap(super(Container, self).getContainerSize())

    @abstractmethod
    def createMenu(self, arg0: 'World', arg1: 'Player', arg2: 'BlockPos'):
        """public abstract dev.ultreon.quantum.menu.ContainerMenu dev.ultreon.quantum.world.container.Container.createMenu(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.BlockPos)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def onSlotClick(self, arg0: int, arg1: 'Player', arg2: 'ContainerInteraction'):
        """public void dev.ultreon.quantum.world.container.Container.onSlotClick(int,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.container.ContainerInteraction)"""
        super(__Container, self).onSlotClick(__int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def onItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.world.container.Container.onItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__Container, self).onItemChanged(__int.valueOf(arg0), arg1)

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
    def hasPlaceFor(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.world.container.Container.hasPlaceFor(dev.ultreon.quantum.item.ItemStack)"""
        return bool.__wrap(super(__Container, self).hasPlaceFor(arg0))

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
    def moveInto(self, arg0: 'Iterable') -> 'List':
        """public java.util.List<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.world.container.Container.moveInto(java.lang.Iterable<dev.ultreon.quantum.item.ItemStack>)"""
        return 'List'.__wrap(super(__Container, self).moveInto(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def moveInto(self, arg0: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.world.container.Container.moveInto(dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'.__wrap(super(__Container, self).moveInto(arg0))