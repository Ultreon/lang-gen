from __future__ import annotations
from overload import overload


 
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.Map.Entry as Entry
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _object
import java.io.ObjectOutput as ObjectOutput
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.function.BiFunction as BiFunction
import java.util.Iterator as Iterator
import java.lang.Float as _float
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import dev.ultreon.libs.collections.v0.maps.OrderedHashMap as _OrderedHashMap
_OrderedHashMap = _OrderedHashMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class OrderedHashMap():
    """dev.ultreon.libs.collections.v0.maps.OrderedHashMap"""
 
    @staticmethod
    def _wrap(java_value: _OrderedHashMap) -> 'OrderedHashMap':
        return OrderedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrderedHashMap):
        """
        Dynamic initializer for OrderedHashMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrderedHashMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrderedHashMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sequence(self) -> 'List':
        """public java.util.List<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.sequence()"""
        return 'List'._wrap(super(OrderedHashMap, self).sequence())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.put(K,V)"""
        return object._wrap(super(_OrderedHashMap, self).put(arg0, arg1))

    @overload
    def getFirstKey(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirstKey()"""
        return object._wrap(super(OrderedHashMap, self).getFirstKey())

    @overload
    def getValue(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getValue(int)"""
        return object._wrap(super(_OrderedHashMap, self).getValue(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap()"""
        val = _OrderedHashMap()
        self.__wrapper = val

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_OrderedHashMap, self).putAll(arg0)

    @override
    @overload
    def size(self) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.size()"""
        return int._wrap(super(OrderedHashMap, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.isEmpty()"""
        return bool._wrap(super(OrderedHashMap, self).isEmpty())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.remove(java.lang.Object)"""
        return object._wrap(super(_OrderedHashMap, self).remove(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(int)"""
        val = _OrderedHashMap(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(java.util.Map<K, V>)"""
        val = _OrderedHashMap(arg0)
        self.__wrapper = val

    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.iterator()"""
        return 'Iterator'._wrap(super(OrderedHashMap, self).iterator())

    @overload
    def getFirstValue(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirstValue()"""
        return object._wrap(super(OrderedHashMap, self).getFirstValue())

    @overload
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.get(int)"""
        return object._wrap(super(_OrderedHashMap, self).get(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.get(java.lang.Object)"""
        return object._wrap(super(_OrderedHashMap, self).get(arg0))

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.clear()"""
        super(OrderedHashMap, self).clear()

    @overload
    def getLast(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLast()"""
        return 'Entry.Map$Entry'._wrap(super(OrderedHashMap, self).getLast())

    @overload
    def getFirst(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirst()"""
        return 'Entry.Map$Entry'._wrap(super(OrderedHashMap, self).getFirst())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clone(self) -> 'OrderedHashMap':
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.clone() throws java.lang.CloneNotSupportedException"""
        return 'OrderedHashMap'._wrap(super(OrderedHashMap, self).clone())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_OrderedHashMap, self).containsKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_OrderedHashMap, self).containsValue(arg0))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.entrySet()"""
        return 'Set'._wrap(super(OrderedHashMap, self).entrySet())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.keySet()"""
        return 'Set'._wrap(super(OrderedHashMap, self).keySet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.hashCode()"""
        return int._wrap(super(OrderedHashMap, self).hashCode())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.readExternal(java.io.ObjectInput) throws java.io.IOException,java.lang.ClassNotFoundException,java.lang.ClassCastException"""
        super(_OrderedHashMap, self).readExternal(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.maps.OrderedHashMap.toString()"""
        return str._wrap(super(OrderedHashMap, self).toString())

    @overload
    def getLastValue(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLastValue()"""
        return object._wrap(super(OrderedHashMap, self).getLastValue())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.values()"""
        return 'Collection'._wrap(super(OrderedHashMap, self).values())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.indexOf(K)"""
        return int._wrap(super(_OrderedHashMap, self).indexOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap()"""
        val = _OrderedHashMap()
        self.__wrapper = val

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def remove(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.remove(int)"""
        return object._wrap(super(_OrderedHashMap, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_OrderedHashMap, self).writeExternal(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def getLastKey(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLastKey()"""
        return object._wrap(super(OrderedHashMap, self).getLastKey())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.lastIndexOf(K)"""
        return int._wrap(super(_OrderedHashMap, self).lastIndexOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(int,float)"""
        val = _OrderedHashMap(_int.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.equals(java.lang.Object)"""
        return bool._wrap(super(_OrderedHashMap, self).equals(arg0))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.maps.OrderedHashMap
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.Map.Entry as Entry
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _object
import java.io.ObjectOutput as ObjectOutput
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.function.BiFunction as BiFunction
import java.util.Iterator as Iterator
import java.lang.Float as _float
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import dev.ultreon.libs.collections.v0.maps.OrderedHashMap as _OrderedHashMap
_OrderedHashMap = _OrderedHashMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class OrderedHashMap():
    """dev.ultreon.libs.collections.v0.maps.OrderedHashMap"""
 
    @staticmethod
    def _wrap(java_value: _OrderedHashMap) -> 'OrderedHashMap':
        return OrderedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrderedHashMap):
        """
        Dynamic initializer for OrderedHashMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrderedHashMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrderedHashMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sequence(self) -> 'List':
        """public java.util.List<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.sequence()"""
        return 'List'._wrap(super(OrderedHashMap, self).sequence())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.put(K,V)"""
        return object._wrap(super(_OrderedHashMap, self).put(arg0, arg1))

    @overload
    def getFirstKey(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirstKey()"""
        return object._wrap(super(OrderedHashMap, self).getFirstKey())

    @overload
    def getValue(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getValue(int)"""
        return object._wrap(super(_OrderedHashMap, self).getValue(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap()"""
        val = _OrderedHashMap()
        self.__wrapper = val

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_OrderedHashMap, self).putAll(arg0)

    @override
    @overload
    def size(self) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.size()"""
        return int._wrap(super(OrderedHashMap, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.isEmpty()"""
        return bool._wrap(super(OrderedHashMap, self).isEmpty())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.remove(java.lang.Object)"""
        return object._wrap(super(_OrderedHashMap, self).remove(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(int)"""
        val = _OrderedHashMap(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(java.util.Map<K, V>)"""
        val = _OrderedHashMap(arg0)
        self.__wrapper = val

    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.iterator()"""
        return 'Iterator'._wrap(super(OrderedHashMap, self).iterator())

    @overload
    def getFirstValue(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirstValue()"""
        return object._wrap(super(OrderedHashMap, self).getFirstValue())

    @overload
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.get(int)"""
        return object._wrap(super(_OrderedHashMap, self).get(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: object) -> object:
        """public V dev.ultreon.libs.collections.v0.maps.OrderedHashMap.get(java.lang.Object)"""
        return object._wrap(super(_OrderedHashMap, self).get(arg0))

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.clear()"""
        super(OrderedHashMap, self).clear()

    @overload
    def getLast(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLast()"""
        return 'Entry.Map$Entry'._wrap(super(OrderedHashMap, self).getLast())

    @overload
    def getFirst(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getFirst()"""
        return 'Entry.Map$Entry'._wrap(super(OrderedHashMap, self).getFirst())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clone(self) -> 'OrderedHashMap':
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap<K, V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.clone() throws java.lang.CloneNotSupportedException"""
        return 'OrderedHashMap'._wrap(super(OrderedHashMap, self).clone())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_OrderedHashMap, self).containsKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_OrderedHashMap, self).containsValue(arg0))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.entrySet()"""
        return 'Set'._wrap(super(OrderedHashMap, self).entrySet())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.keySet()"""
        return 'Set'._wrap(super(OrderedHashMap, self).keySet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.hashCode()"""
        return int._wrap(super(OrderedHashMap, self).hashCode())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.readExternal(java.io.ObjectInput) throws java.io.IOException,java.lang.ClassNotFoundException,java.lang.ClassCastException"""
        super(_OrderedHashMap, self).readExternal(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.maps.OrderedHashMap.toString()"""
        return str._wrap(super(OrderedHashMap, self).toString())

    @overload
    def getLastValue(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLastValue()"""
        return object._wrap(super(OrderedHashMap, self).getLastValue())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.libs.collections.v0.maps.OrderedHashMap.values()"""
        return 'Collection'._wrap(super(OrderedHashMap, self).values())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.indexOf(K)"""
        return int._wrap(super(_OrderedHashMap, self).indexOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap()"""
        val = _OrderedHashMap()
        self.__wrapper = val

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def remove(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.remove(int)"""
        return object._wrap(super(_OrderedHashMap, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.collections.v0.maps.OrderedHashMap.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_OrderedHashMap, self).writeExternal(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def getLastKey(self) -> object:
        """public java.lang.Object dev.ultreon.libs.collections.v0.maps.OrderedHashMap.getLastKey()"""
        return object._wrap(super(OrderedHashMap, self).getLastKey())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int dev.ultreon.libs.collections.v0.maps.OrderedHashMap.lastIndexOf(K)"""
        return int._wrap(super(_OrderedHashMap, self).lastIndexOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public dev.ultreon.libs.collections.v0.maps.OrderedHashMap(int,float)"""
        val = _OrderedHashMap(_int.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.maps.OrderedHashMap.equals(java.lang.Object)"""
        return bool._wrap(super(_OrderedHashMap, self).equals(arg0))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.maps.OrderedHashMap