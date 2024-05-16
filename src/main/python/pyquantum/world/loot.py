from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.world.loot.RandomLoot as _RandomLoot_LootEntry
_LootEntry = _RandomLoot_LootEntry.LootEntry
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from abc import abstractmethod, ABC
 
class LootEntry():
    """dev.ultreon.quantum.world.loot.RandomLoot.LootEntry"""
 
    @staticmethod
    def _wrap(java_value: _LootEntry) -> 'LootEntry':
        return LootEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LootEntry):
        """
        Dynamic initializer for LootEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LootEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LootEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def data(self, ):
        """public abstract dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.loot.RandomLoot$LootEntry.data()"""
        pass

    @abstractmethod
    def randomCount(self, arg0: 'RNG'):
        """public abstract int dev.ultreon.quantum.world.loot.RandomLoot$LootEntry.randomCount(dev.ultreon.quantum.world.rng.RNG)"""
        pass

    @abstractmethod
    def item(self, ):
        """public abstract dev.ultreon.quantum.item.Item dev.ultreon.quantum.world.loot.RandomLoot$LootEntry.item()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.world.loot.RandomLoot$LootEntry
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.world.loot.RandomLoot as _RandomLoot_LootEntry
_LootEntry = _RandomLoot_LootEntry.LootEntry
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from abc import abstractmethod, ABC
 
class LootEntry():
    """dev.ultreon.quantum.world.loot.RandomLoot.LootEntry"""
 
    @staticmethod
    def _wrap(java_value: _LootEntry) -> 'LootEntry':
        return LootEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LootEntry):
        """
        Dynamic initializer for LootEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LootEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LootEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def data(self, ):
        """public abstract dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.loot.RandomLoot$LootEntry.data()"""
        pass

    @abstractmethod
    def randomCount(self, arg0: 'RNG'):
        """public abstract int dev.ultreon.quantum.world.loot.RandomLoot$LootEntry.randomCount(dev.ultreon.quantum.world.rng.RNG)"""
        pass

    @abstractmethod
    def item(self, ):
        """public abstract dev.ultreon.quantum.item.Item dev.ultreon.quantum.world.loot.RandomLoot$LootEntry.item()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.world.loot.RandomLoot$LootEntry 
 
 
# CLASS: dev.ultreon.quantum.world.loot.ConstantLoot
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.loot.ConstantLoot as _ConstantLoot
_ConstantLoot = _ConstantLoot
import java.lang.Iterable as Iterable
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class ConstantLoot():
    """dev.ultreon.quantum.world.loot.ConstantLoot"""
 
    @staticmethod
    def _wrap(java_value: _ConstantLoot) -> 'ConstantLoot':
        return ConstantLoot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantLoot):
        """
        Dynamic initializer for ConstantLoot.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantLoot__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantLoot__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.world.loot.ConstantLoot.EMPTY
    EMPTY: 'LootGenerator' = _wrap(_LootGenerator.EMPTY)


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
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.world.loot.ConstantLoot(java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        val = _ConstantLoot(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def generate(self, arg0: 'RNG') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.world.loot.ConstantLoot.generate(dev.ultreon.quantum.world.rng.RNG)"""
        return 'Iterable'._wrap(super(_ConstantLoot, self).generate(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, *arg0: 'item.ItemStack'):
        """public dev.ultreon.quantum.world.loot.ConstantLoot(dev.ultreon.quantum.item.ItemStack...)"""
        val = _ConstantLoot(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.world.loot.RandomLoot as _RandomLoot_CountLootEntry
_CountLootEntry = _RandomLoot_CountLootEntry.CountLootEntry
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
try:
    from pyapache import lang3
except ImportError:
    lang3 = _import_once("pyapache.lang3")

import org.apache.commons.lang3.IntegerRange as _IntegerRange
_IntegerRange = _IntegerRange
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class CountLootEntry():
    """dev.ultreon.quantum.world.loot.RandomLoot.CountLootEntry"""
 
    @staticmethod
    def _wrap(java_value: _CountLootEntry) -> 'CountLootEntry':
        return CountLootEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CountLootEntry):
        """
        Dynamic initializer for CountLootEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CountLootEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CountLootEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def range(self) -> 'lang3.IntegerRange':
        """public org.apache.commons.lang3.IntegerRange dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.range()"""
        return 'lang3.IntegerRange'._wrap(super(CountLootEntry, self).range())

    @overload
    def __init__(self, arg0: 'IntegerRange', arg1: 'Item'):
        """public dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry(org.apache.commons.lang3.IntegerRange,dev.ultreon.quantum.item.Item)"""
        val = _CountLootEntry(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def item(self) -> 'item.Item':
        """public dev.ultreon.quantum.item.Item dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.item()"""
        return 'item.Item'._wrap(super(CountLootEntry, self).item())

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
        """public java.lang.String dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.toString()"""
        return str._wrap(super(CountLootEntry, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'IntegerRange', arg1: 'Item', arg2: 'MapType'):
        """public dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry(org.apache.commons.lang3.IntegerRange,dev.ultreon.quantum.item.Item,dev.ultreon.ubo.types.MapType)"""
        val = _CountLootEntry(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.hashCode()"""
        return int._wrap(super(CountLootEntry, self).hashCode())

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
    def data(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.data()"""
        return 'types.MapType'._wrap(super(CountLootEntry, self).data())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def randomCount(self, arg0: 'RNG') -> int:
        """public int dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.randomCount(dev.ultreon.quantum.world.rng.RNG)"""
        return int._wrap(super(_CountLootEntry, self).randomCount(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_CountLootEntry, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.loot.LootGenerator
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
from abc import abstractmethod, ABC
 
class LootGenerator():
    """dev.ultreon.quantum.world.loot.LootGenerator"""
 
    @staticmethod
    def _wrap(java_value: _LootGenerator) -> 'LootGenerator':
        return LootGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LootGenerator):
        """
        Dynamic initializer for LootGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LootGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LootGenerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def generate(self, arg0: 'RNG'):
        """public abstract java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.world.loot.LootGenerator.generate(dev.ultreon.quantum.world.rng.RNG)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.loot.RandomLoot as _RandomLoot_ChanceLootEntry
_ChanceLootEntry = _RandomLoot_ChanceLootEntry.ChanceLootEntry
import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
import java.lang.Float as _float
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class ChanceLootEntry():
    """dev.ultreon.quantum.world.loot.RandomLoot.ChanceLootEntry"""
 
    @staticmethod
    def _wrap(java_value: _ChanceLootEntry) -> 'ChanceLootEntry':
        return ChanceLootEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChanceLootEntry):
        """
        Dynamic initializer for ChanceLootEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChanceLootEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChanceLootEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float, arg1: 'Item', arg2: 'MapType'):
        """public dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry(float,dev.ultreon.quantum.item.Item,dev.ultreon.ubo.types.MapType)"""
        val = _ChanceLootEntry(_float.valueOf(arg0), arg1, arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_ChanceLootEntry, self).equals(arg0))

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
    def item(self) -> 'item.Item':
        """public dev.ultreon.quantum.item.Item dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.item()"""
        return 'item.Item'._wrap(super(ChanceLootEntry, self).item())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.hashCode()"""
        return int._wrap(super(ChanceLootEntry, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.toString()"""
        return str._wrap(super(ChanceLootEntry, self).toString())

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
    def randomCount(self, arg0: 'RNG') -> int:
        """public int dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.randomCount(dev.ultreon.quantum.world.rng.RNG)"""
        return int._wrap(super(_ChanceLootEntry, self).randomCount(arg0))

    @overload
    def chance(self) -> float:
        """public float dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.chance()"""
        return float._wrap(super(ChanceLootEntry, self).chance())

    @override
    @overload
    def data(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.data()"""
        return 'types.MapType'._wrap(super(ChanceLootEntry, self).data())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: 'Item'):
        """public dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry(float,dev.ultreon.quantum.item.Item)"""
        val = _ChanceLootEntry(_float.valueOf(arg0), arg1)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.world.loot.RandomLoot
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.world.loot.RandomLoot as _RandomLoot
_RandomLoot = _RandomLoot
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pyquantum.world import rng
except ImportError:
    rng = _import_once("pyquantum.world.rng")

from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RandomLoot():
    """dev.ultreon.quantum.world.loot.RandomLoot"""
 
    @staticmethod
    def _wrap(java_value: _RandomLoot) -> 'RandomLoot':
        return RandomLoot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RandomLoot):
        """
        Dynamic initializer for RandomLoot.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RandomLoot__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RandomLoot__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def getEntries(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.world.loot.RandomLoot$LootEntry> dev.ultreon.quantum.world.loot.RandomLoot.getEntries()"""
        return 'List'._wrap(super(RandomLoot, self).getEntries())

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
    def generate(self, arg0: 'RNG') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.world.loot.RandomLoot.generate(dev.ultreon.quantum.world.rng.RNG)"""
        return 'Iterable'._wrap(super(_RandomLoot, self).generate(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, *arg0: 'LootEntry'):
        """public dev.ultreon.quantum.world.loot.RandomLoot(dev.ultreon.quantum.world.loot.RandomLoot$LootEntry...)"""
        val = _RandomLoot(arg0)
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