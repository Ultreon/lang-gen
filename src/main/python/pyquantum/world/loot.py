from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import dev.ultreon.quantum.world.loot.RandomLoot as __RandomLoot_LootEntry
__LootEntry = __RandomLoot_LootEntry.LootEntry
from abc import abstractmethod, ABC
 
class LootEntry(ABC):
    """dev.ultreon.quantum.world.loot.RandomLoot.LootEntry"""
 
    @staticmethod
    def __wrap(java_value: __LootEntry) -> 'LootEntry':
        return LootEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LootEntry):
        """
        Dynamic initializer for LootEntry.
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
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import dev.ultreon.quantum.world.loot.RandomLoot as __RandomLoot_LootEntry
__LootEntry = __RandomLoot_LootEntry.LootEntry
from abc import abstractmethod, ABC
 
class LootEntry(ABC):
    """dev.ultreon.quantum.world.loot.RandomLoot.LootEntry"""
 
    @staticmethod
    def __wrap(java_value: __LootEntry) -> 'LootEntry':
        return LootEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LootEntry):
        """
        Dynamic initializer for LootEntry.
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
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.world.loot.ConstantLoot as __ConstantLoot
__ConstantLoot = __ConstantLoot
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
import java.util.List as List
 
class ConstantLoot(__LootGenerator, LootGenerator):
    """dev.ultreon.quantum.world.loot.ConstantLoot"""
 
    @staticmethod
    def __wrap(java_value: __ConstantLoot) -> 'ConstantLoot':
        return ConstantLoot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantLoot):
        """
        Dynamic initializer for ConstantLoot.
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
 
    # public static final dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.world.loot.ConstantLoot.EMPTY
    EMPTY: 'LootGenerator' = __wrap(__LootGenerator.EMPTY)


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
    def __init__(self, *arg0: 'item.ItemStack'):
        """public dev.ultreon.quantum.world.loot.ConstantLoot(dev.ultreon.quantum.item.ItemStack...)"""
        val = __ConstantLoot(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.world.loot.ConstantLoot(java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        val = __ConstantLoot(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def generate(self, arg0: 'RNG') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.world.loot.ConstantLoot.generate(dev.ultreon.quantum.world.rng.RNG)"""
        return 'Iterable'.__wrap(super(__ConstantLoot, self).generate(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.world.loot.RandomLoot as __RandomLoot_CountLootEntry
__CountLootEntry = __RandomLoot_CountLootEntry.CountLootEntry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyapache import lang3
except ImportError:
    lang3 = __import_once__("pyapache.lang3")

try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
import org.apache.commons.lang3.IntegerRange as __IntegerRange
__IntegerRange = __IntegerRange
import java.lang.Integer as __int
from builtins import bool
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class CountLootEntry(__LootEntry, LootEntry):
    """dev.ultreon.quantum.world.loot.RandomLoot.CountLootEntry"""
 
    @staticmethod
    def __wrap(java_value: __CountLootEntry) -> 'CountLootEntry':
        return CountLootEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CountLootEntry):
        """
        Dynamic initializer for CountLootEntry.
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
    def range(self) -> 'lang3.IntegerRange':
        """public org.apache.commons.lang3.IntegerRange dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.range()"""
        return 'lang3.IntegerRange'.__wrap(super(CountLootEntry, self).range())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__CountLootEntry, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.toString()"""
        return str.__wrap(super(CountLootEntry, self).toString())

    @overload
    def __init__(self, arg0: 'IntegerRange', arg1: 'Item'):
        """public dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry(org.apache.commons.lang3.IntegerRange,dev.ultreon.quantum.item.Item)"""
        val = __CountLootEntry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.data()"""
        return 'types.MapType'.__wrap(super(CountLootEntry, self).data())

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
    def __init__(self, arg0: 'IntegerRange', arg1: 'Item', arg2: 'MapType'):
        """public dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry(org.apache.commons.lang3.IntegerRange,dev.ultreon.quantum.item.Item,dev.ultreon.ubo.types.MapType)"""
        val = __CountLootEntry(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def randomCount(self, arg0: 'RNG') -> int:
        """public int dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.randomCount(dev.ultreon.quantum.world.rng.RNG)"""
        return int.__wrap(super(__CountLootEntry, self).randomCount(arg0))

    @override
    @overload
    def item(self) -> 'item.Item':
        """public dev.ultreon.quantum.item.Item dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.item()"""
        return 'item.Item'.__wrap(super(CountLootEntry, self).item())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.loot.RandomLoot$CountLootEntry.hashCode()"""
        return int.__wrap(super(CountLootEntry, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.loot.LootGenerator
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

from abc import abstractmethod, ABC
 
class LootGenerator(ABC):
    """dev.ultreon.quantum.world.loot.LootGenerator"""
 
    @staticmethod
    def __wrap(java_value: __LootGenerator) -> 'LootGenerator':
        return LootGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LootGenerator):
        """
        Dynamic initializer for LootGenerator.
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
    def generate(self, arg0: 'RNG'):
        """public abstract java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.world.loot.LootGenerator.generate(dev.ultreon.quantum.world.rng.RNG)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
import dev.ultreon.quantum.world.loot.RandomLoot as __RandomLoot_ChanceLootEntry
__ChanceLootEntry = __RandomLoot_ChanceLootEntry.ChanceLootEntry
from builtins import type
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.item.Item as __Item
__Item = __Item
import java.lang.Integer as __int
from builtins import bool
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class ChanceLootEntry(__LootEntry, LootEntry):
    """dev.ultreon.quantum.world.loot.RandomLoot.ChanceLootEntry"""
 
    @staticmethod
    def __wrap(java_value: __ChanceLootEntry) -> 'ChanceLootEntry':
        return ChanceLootEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChanceLootEntry):
        """
        Dynamic initializer for ChanceLootEntry.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__ChanceLootEntry, self).equals(arg0))

    @overload
    def randomCount(self, arg0: 'RNG') -> int:
        """public int dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.randomCount(dev.ultreon.quantum.world.rng.RNG)"""
        return int.__wrap(super(__ChanceLootEntry, self).randomCount(arg0))

    @overload
    def __init__(self, arg0: float, arg1: 'Item'):
        """public dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry(float,dev.ultreon.quantum.item.Item)"""
        val = __ChanceLootEntry(__float.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def data(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.data()"""
        return 'types.MapType'.__wrap(super(ChanceLootEntry, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.hashCode()"""
        return int.__wrap(super(ChanceLootEntry, self).hashCode())

    @override
    @overload
    def item(self) -> 'item.Item':
        """public dev.ultreon.quantum.item.Item dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.item()"""
        return 'item.Item'.__wrap(super(ChanceLootEntry, self).item())

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: 'Item', arg2: 'MapType'):
        """public dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry(float,dev.ultreon.quantum.item.Item,dev.ultreon.ubo.types.MapType)"""
        val = __ChanceLootEntry(__float.valueOf(arg0), arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def chance(self) -> float:
        """public float dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.chance()"""
        return float.__wrap(super(ChanceLootEntry, self).chance())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.loot.RandomLoot$ChanceLootEntry.toString()"""
        return str.__wrap(super(ChanceLootEntry, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.world.loot.RandomLoot
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.world import rng
except ImportError:
    rng = __import_once__("pyquantum.world.rng")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.world.loot.RandomLoot as __RandomLoot
__RandomLoot = __RandomLoot
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class RandomLoot(__LootGenerator, LootGenerator):
    """dev.ultreon.quantum.world.loot.RandomLoot"""
 
    @staticmethod
    def __wrap(java_value: __RandomLoot) -> 'RandomLoot':
        return RandomLoot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RandomLoot):
        """
        Dynamic initializer for RandomLoot.
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

    @overload
    def __init__(self, *arg0: 'LootEntry'):
        """public dev.ultreon.quantum.world.loot.RandomLoot(dev.ultreon.quantum.world.loot.RandomLoot$LootEntry...)"""
        val = __RandomLoot(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getEntries(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.world.loot.RandomLoot$LootEntry> dev.ultreon.quantum.world.loot.RandomLoot.getEntries()"""
        return 'List'.__wrap(super(RandomLoot, self).getEntries())

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
    def generate(self, arg0: 'RNG') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.world.loot.RandomLoot.generate(dev.ultreon.quantum.world.rng.RNG)"""
        return 'Iterable'.__wrap(super(__RandomLoot, self).generate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))