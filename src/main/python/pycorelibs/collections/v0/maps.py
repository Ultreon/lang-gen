from __future__ import annotations
from overload import overload


 
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import dev.ultreon.libs.collections.v0.maps.OrderedHashMap as __OrderedHashMap
__OrderedHashMap = __OrderedHashMap
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.io.ObjectOutput as ObjectOutput
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.Iterator as Iterator
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class OrderedHashMap(__Map, Map, __Cloneable, Cloneable, __Externalizable, Externalizable):
    """dev.ultreon.libs.collections.v0.maps.OrderedHashMap"""
 
    @staticmethod
    def __wrap(java_value: __OrderedHashMap) -> 'OrderedHashMap':
        return OrderedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedHashMap):
        """
        Dynamic initializer for OrderedHashMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__OrderedHashMap, self).equals(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.keySet()"""
        return 'Set'.__wrap(super(OrderedHashMap, self).keySet())

    @overload
    def getFirst(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirst()"""
        return 'Entry.Map$Entry'.__wrap(super(OrderedHashMap, self).getFirst())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap()"""
        val = __OrderedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.remove(java.lang.Object)"""
        return object.__wrap(super(__OrderedHashMap, self).remove(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.lastIndexOf(K)"""
        return int.__wrap(super(__OrderedHashMap, self).lastIndexOf(arg0))

    @overload
    def getFirstKey(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirstKey()"""
        return object.__wrap(super(OrderedHashMap, self).getFirstKey())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(int,float)"""
        val = __OrderedHashMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__OrderedHashMap, self).containsValue(arg0))

    @overload
    def getFirstValue(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirstValue()"""
        return object.__wrap(super(OrderedHashMap, self).getFirstValue())

    @overload
    def getLastKey(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLastKey()"""
        return object.__wrap(super(OrderedHashMap, self).getLastKey())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.put(K,V)"""
        return object.__wrap(super(__OrderedHashMap, self).put(arg0, arg1))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__OrderedHashMap, self).writeExternal(arg0)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(int)"""
        val = __OrderedHashMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def getValue(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getValue(int)"""
        return object.__wrap(super(__OrderedHashMap, self).getValue(__int.valueOf(arg0)))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def clone(self) -> 'OrderedHashMap':
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.clone() throws java.lang.CloneNotSupportedException"""
        return 'OrderedHashMap'.__wrap(super(OrderedHashMap, self).clone())

    @overload
    def getLast(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLast()"""
        return 'Entry.Map$Entry'.__wrap(super(OrderedHashMap, self).getLast())

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.clear()"""
        super(OrderedHashMap, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.hashCode()"""
        return int.__wrap(super(OrderedHashMap, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def get(self, arg0: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.get(java.lang.Object)"""
        return object.__wrap(super(__OrderedHashMap, self).get(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.size()"""
        return int.__wrap(super(OrderedHashMap, self).size())

    @overload
    def sequence(self) -> 'List':
        """public java.util.List<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.sequence()"""
        return 'List'.__wrap(super(OrderedHashMap, self).sequence())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__OrderedHashMap, self).containsKey(arg0))

    @overload
    def getLastValue(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLastValue()"""
        return object.__wrap(super(OrderedHashMap, self).getLastValue())

    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.iterator()"""
        return 'Iterator'.__wrap(super(OrderedHashMap, self).iterator())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap()"""
        val = __OrderedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.entrySet()"""
        return 'Set'.__wrap(super(OrderedHashMap, self).entrySet())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__OrderedHashMap, self).putAll(arg0)

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.indexOf(K)"""
        return int.__wrap(super(__OrderedHashMap, self).indexOf(arg0))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.readExternal(java.io.ObjectInput) throws java.io.IOException,java.lang.ClassNotFoundException,java.lang.ClassCastException"""
        super(__OrderedHashMap, self).readExternal(arg0)

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.get(int)"""
        return object.__wrap(super(__OrderedHashMap, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.values()"""
        return 'Collection'.__wrap(super(OrderedHashMap, self).values())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.maps.OrderedHashMap.toString()"""
        return str.__wrap(super(OrderedHashMap, self).toString())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.remove(int)"""
        return object.__wrap(super(__OrderedHashMap, self).remove(__int.valueOf(arg0)))

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
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(java.util.Map<K, V>)"""
        val = __OrderedHashMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.isEmpty()"""
        return bool.__wrap(super(OrderedHashMap, self).isEmpty())

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.maps.OrderedHashMap
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import dev.ultreon.libs.collections.v0.maps.OrderedHashMap as __OrderedHashMap
__OrderedHashMap = __OrderedHashMap
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.io.ObjectOutput as ObjectOutput
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.Iterator as Iterator
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class OrderedHashMap(__Map, Map, __Cloneable, Cloneable, __Externalizable, Externalizable):
    """dev.ultreon.libs.collections.v0.maps.OrderedHashMap"""
 
    @staticmethod
    def __wrap(java_value: __OrderedHashMap) -> 'OrderedHashMap':
        return OrderedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedHashMap):
        """
        Dynamic initializer for OrderedHashMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__OrderedHashMap, self).equals(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.keySet()"""
        return 'Set'.__wrap(super(OrderedHashMap, self).keySet())

    @overload
    def getFirst(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirst()"""
        return 'Entry.Map$Entry'.__wrap(super(OrderedHashMap, self).getFirst())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap()"""
        val = __OrderedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.remove(java.lang.Object)"""
        return object.__wrap(super(__OrderedHashMap, self).remove(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.lastIndexOf(K)"""
        return int.__wrap(super(__OrderedHashMap, self).lastIndexOf(arg0))

    @overload
    def getFirstKey(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirstKey()"""
        return object.__wrap(super(OrderedHashMap, self).getFirstKey())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(int,float)"""
        val = __OrderedHashMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__OrderedHashMap, self).containsValue(arg0))

    @overload
    def getFirstValue(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirstValue()"""
        return object.__wrap(super(OrderedHashMap, self).getFirstValue())

    @overload
    def getLastKey(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLastKey()"""
        return object.__wrap(super(OrderedHashMap, self).getLastKey())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.put(K,V)"""
        return object.__wrap(super(__OrderedHashMap, self).put(arg0, arg1))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__OrderedHashMap, self).writeExternal(arg0)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(int)"""
        val = __OrderedHashMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def getValue(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getValue(int)"""
        return object.__wrap(super(__OrderedHashMap, self).getValue(__int.valueOf(arg0)))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def clone(self) -> 'OrderedHashMap':
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.clone() throws java.lang.CloneNotSupportedException"""
        return 'OrderedHashMap'.__wrap(super(OrderedHashMap, self).clone())

    @overload
    def getLast(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLast()"""
        return 'Entry.Map$Entry'.__wrap(super(OrderedHashMap, self).getLast())

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.clear()"""
        super(OrderedHashMap, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.hashCode()"""
        return int.__wrap(super(OrderedHashMap, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def get(self, arg0: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.get(java.lang.Object)"""
        return object.__wrap(super(__OrderedHashMap, self).get(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.size()"""
        return int.__wrap(super(OrderedHashMap, self).size())

    @overload
    def sequence(self) -> 'List':
        """public java.util.List<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.sequence()"""
        return 'List'.__wrap(super(OrderedHashMap, self).sequence())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__OrderedHashMap, self).containsKey(arg0))

    @overload
    def getLastValue(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLastValue()"""
        return object.__wrap(super(OrderedHashMap, self).getLastValue())

    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.iterator()"""
        return 'Iterator'.__wrap(super(OrderedHashMap, self).iterator())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap()"""
        val = __OrderedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.entrySet()"""
        return 'Set'.__wrap(super(OrderedHashMap, self).entrySet())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__OrderedHashMap, self).putAll(arg0)

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.indexOf(K)"""
        return int.__wrap(super(__OrderedHashMap, self).indexOf(arg0))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.readExternal(java.io.ObjectInput) throws java.io.IOException,java.lang.ClassNotFoundException,java.lang.ClassCastException"""
        super(__OrderedHashMap, self).readExternal(arg0)

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.get(int)"""
        return object.__wrap(super(__OrderedHashMap, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.values()"""
        return 'Collection'.__wrap(super(OrderedHashMap, self).values())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.maps.OrderedHashMap.toString()"""
        return str.__wrap(super(OrderedHashMap, self).toString())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.remove(int)"""
        return object.__wrap(super(__OrderedHashMap, self).remove(__int.valueOf(arg0)))

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
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(java.util.Map<K, V>)"""
        val = __OrderedHashMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.isEmpty()"""
        return bool.__wrap(super(OrderedHashMap, self).isEmpty())

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.maps.OrderedHashMap