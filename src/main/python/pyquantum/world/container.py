from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import dev.ultreon.quantum.world.container.ContainerView as _ContainerView
_ContainerView = _ContainerView
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

from abc import abstractmethod, ABC
 
class ContainerView():
    """dev.ultreon.quantum.world.container.ContainerView"""
 
    @staticmethod
    def _wrap(java_value: _ContainerView) -> 'ContainerView':
        return ContainerView(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContainerView):
        """
        Dynamic initializer for ContainerView.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContainerView__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContainerView__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import dev.ultreon.quantum.world.container.ContainerView as _ContainerView
_ContainerView = _ContainerView
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

from abc import abstractmethod, ABC
 
class ContainerView():
    """dev.ultreon.quantum.world.container.ContainerView"""
 
    @staticmethod
    def _wrap(java_value: _ContainerView) -> 'ContainerView':
        return ContainerView(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContainerView):
        """
        Dynamic initializer for ContainerView.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContainerView__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContainerView__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import dev.ultreon.quantum.world.container.ContainerInteraction as _ContainerInteraction
_ContainerInteraction = _ContainerInteraction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ContainerInteraction():
    """dev.ultreon.quantum.world.container.ContainerInteraction"""
 
    @staticmethod
    def _wrap(java_value: _ContainerInteraction) -> 'ContainerInteraction':
        return ContainerInteraction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContainerInteraction):
        """
        Dynamic initializer for ContainerInteraction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContainerInteraction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContainerInteraction__wrapper":
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
    def valueOf(arg0: str) -> 'ContainerInteraction':
        """public static dev.ultreon.quantum.world.container.ContainerInteraction dev.ultreon.quantum.world.container.ContainerInteraction.valueOf(java.lang.String)"""
        return ContainerInteraction._wrap(_ContainerInteraction.valueOf(arg0))

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

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['ContainerInteraction']:
        """public static dev.ultreon.quantum.world.container.ContainerInteraction[] dev.ultreon.quantum.world.container.ContainerInteraction.values()"""
        return List[ContainerInteraction]._wrap(_ContainerInteraction.values())


ContainerInteraction.DROP = ContainerInteraction._wrap(_DROP.DROP)

ContainerInteraction.TAKE = ContainerInteraction._wrap(_TAKE.TAKE)

ContainerInteraction.PLACE = ContainerInteraction._wrap(_PLACE.PLACE)

ContainerInteraction.QUICK_MOVE = ContainerInteraction._wrap(_QUICK_MOVE.QUICK_MOVE)

ContainerInteraction.PlACE_ONE = ContainerInteraction._wrap(_PlACE_ONE.PlACE_ONE)

ContainerInteraction.MERGE = ContainerInteraction._wrap(_MERGE.MERGE)

ContainerInteraction.SPLIT = ContainerInteraction._wrap(_SPLIT.SPLIT) 
 
 
# CLASS: dev.ultreon.quantum.world.container.Container
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
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.world.container.Container as _Container
_Container = _Container
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

from builtins import bool
import java.lang.Long as _long
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Container():
    """dev.ultreon.quantum.world.container.Container"""
 
    @staticmethod
    def _wrap(java_value: _Container) -> 'Container':
        return Container(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Container):
        """
        Dynamic initializer for Container.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Container__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Container__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def onItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.world.container.Container.onItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(_Container, self).onItemChanged(_int.valueOf(arg0), arg1)

    @override
    @overload
    def onContainerClosed(self, arg0: 'Player'):
        """public final void dev.ultreon.quantum.world.container.Container.onContainerClosed(dev.ultreon.quantum.entity.player.Player)"""
        super(_Container, self).onContainerClosed(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getContainerSize(self) -> int:
        """public final int dev.ultreon.quantum.world.container.Container.getContainerSize()"""
        return int._wrap(super(Container, self).getContainerSize())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def moveInto(self, arg0: 'ItemStack') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.world.container.Container.moveInto(dev.ultreon.quantum.item.ItemStack)"""
        return 'item.ItemStack'._wrap(super(_Container, self).moveInto(arg0))

    @override
    @overload
    def onSlotClick(self, arg0: int, arg1: 'Player', arg2: 'ContainerInteraction'):
        """public void dev.ultreon.quantum.world.container.Container.onSlotClick(int,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.container.ContainerInteraction)"""
        super(_Container, self).onSlotClick(_int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def createMenu(self, arg0: 'World', arg1: 'Player', arg2: 'BlockPos'):
        """public abstract dev.ultreon.quantum.menu.ContainerMenu dev.ultreon.quantum.world.container.Container.createMenu(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.world.BlockPos)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.container.Container(int)"""
        val = _Container(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def hasPlaceFor(self, arg0: 'ItemStack') -> bool:
        """public boolean dev.ultreon.quantum.world.container.Container.hasPlaceFor(dev.ultreon.quantum.item.ItemStack)"""
        return bool._wrap(super(_Container, self).hasPlaceFor(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getItem(self, arg0: int) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.world.container.Container.getItem(int)"""
        return 'item.ItemStack'._wrap(super(_Container, self).getItem(_int.valueOf(arg0)))

    @overload
    def removeWatcher(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.world.container.Container.removeWatcher(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_Container, self).removeWatcher(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def moveInto(self, arg0: 'Iterable') -> 'List':
        """public java.util.List<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.world.container.Container.moveInto(java.lang.Iterable<dev.ultreon.quantum.item.ItemStack>)"""
        return 'List'._wrap(super(_Container, self).moveInto(arg0))

    @overload
    def addWatcher(self, arg0: 'ServerPlayer', arg1: 'ContainerMenu'):
        """public void dev.ultreon.quantum.world.container.Container.addWatcher(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.menu.ContainerMenu)"""
        super(_Container, self).addWatcher(arg0, arg1)

    @overload
    def setItem(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.world.container.Container.setItem(int,dev.ultreon.quantum.item.ItemStack)"""
        super(_Container, self).setItem(_int.valueOf(arg0), arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())