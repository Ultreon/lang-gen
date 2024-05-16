from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.Map.Entry as Entry
import org.apache.commons.collections4.map.SingletonMap as _SingletonMap
_SingletonMap = _SingletonMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SingletonMap():
    """org.apache.commons.collections4.map.SingletonMap"""
 
    @staticmethod
    def _wrap(java_value: _SingletonMap) -> 'SingletonMap':
        return SingletonMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SingletonMap):
        """
        Dynamic initializer for SingletonMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SingletonMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SingletonMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.hashCode()"""
        return int._wrap(super(SingletonMap, self).hashCode())

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.map.SingletonMap(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = _SingletonMap(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.map.SingletonMap(org.apache.commons.collections4.KeyValue<K, V>)"""
        val = _SingletonMap(arg0)
        self.__wrapper = val

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.isFull()"""
        return bool._wrap(super(SingletonMap, self).isFull())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_SingletonMap, self).containsValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.getKey()"""
        return object._wrap(super(SingletonMap, self).getKey())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.SingletonMap.clear()"""
        super(SingletonMap, self).clear()

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.SingletonMap(java.util.Map<? extends K, ? extends V>)"""
        val = _SingletonMap(arg0)
        self.__wrapper = val

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.SingletonMap()"""
        val = _SingletonMap()
        self.__wrapper = val

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.nextKey(K)"""
        return object._wrap(super(_SingletonMap, self).nextKey(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.get(java.lang.Object)"""
        return object._wrap(super(_SingletonMap, self).get(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.SingletonMap.keySet()"""
        return 'Set'._wrap(super(SingletonMap, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.SingletonMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(SingletonMap, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.lastKey()"""
        return object._wrap(super(SingletonMap, self).lastKey())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.SingletonMap()"""
        val = _SingletonMap()
        self.__wrapper = val

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.maxSize()"""
        return int._wrap(super(SingletonMap, self).maxSize())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def clone(self) -> 'SingletonMap':
        """public org.apache.commons.collections4.map.SingletonMap<K, V> org.apache.commons.collections4.map.SingletonMap.clone()"""
        return 'SingletonMap'._wrap(super(SingletonMap, self).clone())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.put(K,V)"""
        return object._wrap(super(_SingletonMap, self).put(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.SingletonMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_SingletonMap, self).putAll(arg0)

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.previousKey(K)"""
        return object._wrap(super(_SingletonMap, self).previousKey(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.setValue(V)"""
        return object._wrap(super(_SingletonMap, self).setValue(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.remove(java.lang.Object)"""
        return object._wrap(super(_SingletonMap, self).remove(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.SingletonMap.values()"""
        return 'Collection'._wrap(super(SingletonMap, self).values())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.firstKey()"""
        return object._wrap(super(SingletonMap, self).firstKey())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.SingletonMap.toString()"""
        return str._wrap(super(SingletonMap, self).toString())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.SingletonMap.entrySet()"""
        return 'Set'._wrap(super(SingletonMap, self).entrySet())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_SingletonMap, self).containsKey(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.size()"""
        return int._wrap(super(SingletonMap, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.equals(java.lang.Object)"""
        return bool._wrap(super(_SingletonMap, self).equals(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.getValue()"""
        return object._wrap(super(SingletonMap, self).getValue())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.isEmpty()"""
        return bool._wrap(super(SingletonMap, self).isEmpty())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.map.SingletonMap(K,V)"""
        val = _SingletonMap(arg0, arg1)
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.collections4.map.SingletonMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.Map.Entry as Entry
import org.apache.commons.collections4.map.SingletonMap as _SingletonMap
_SingletonMap = _SingletonMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SingletonMap():
    """org.apache.commons.collections4.map.SingletonMap"""
 
    @staticmethod
    def _wrap(java_value: _SingletonMap) -> 'SingletonMap':
        return SingletonMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SingletonMap):
        """
        Dynamic initializer for SingletonMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SingletonMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SingletonMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.hashCode()"""
        return int._wrap(super(SingletonMap, self).hashCode())

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.map.SingletonMap(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = _SingletonMap(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.map.SingletonMap(org.apache.commons.collections4.KeyValue<K, V>)"""
        val = _SingletonMap(arg0)
        self.__wrapper = val

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.isFull()"""
        return bool._wrap(super(SingletonMap, self).isFull())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_SingletonMap, self).containsValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.getKey()"""
        return object._wrap(super(SingletonMap, self).getKey())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.SingletonMap.clear()"""
        super(SingletonMap, self).clear()

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.SingletonMap(java.util.Map<? extends K, ? extends V>)"""
        val = _SingletonMap(arg0)
        self.__wrapper = val

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.SingletonMap()"""
        val = _SingletonMap()
        self.__wrapper = val

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.nextKey(K)"""
        return object._wrap(super(_SingletonMap, self).nextKey(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.get(java.lang.Object)"""
        return object._wrap(super(_SingletonMap, self).get(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.SingletonMap.keySet()"""
        return 'Set'._wrap(super(SingletonMap, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.SingletonMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(SingletonMap, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.lastKey()"""
        return object._wrap(super(SingletonMap, self).lastKey())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.SingletonMap()"""
        val = _SingletonMap()
        self.__wrapper = val

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.maxSize()"""
        return int._wrap(super(SingletonMap, self).maxSize())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def clone(self) -> 'SingletonMap':
        """public org.apache.commons.collections4.map.SingletonMap<K, V> org.apache.commons.collections4.map.SingletonMap.clone()"""
        return 'SingletonMap'._wrap(super(SingletonMap, self).clone())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.put(K,V)"""
        return object._wrap(super(_SingletonMap, self).put(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.SingletonMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_SingletonMap, self).putAll(arg0)

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.previousKey(K)"""
        return object._wrap(super(_SingletonMap, self).previousKey(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.setValue(V)"""
        return object._wrap(super(_SingletonMap, self).setValue(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.remove(java.lang.Object)"""
        return object._wrap(super(_SingletonMap, self).remove(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.SingletonMap.values()"""
        return 'Collection'._wrap(super(SingletonMap, self).values())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.firstKey()"""
        return object._wrap(super(SingletonMap, self).firstKey())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.SingletonMap.toString()"""
        return str._wrap(super(SingletonMap, self).toString())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.SingletonMap.entrySet()"""
        return 'Set'._wrap(super(SingletonMap, self).entrySet())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_SingletonMap, self).containsKey(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.size()"""
        return int._wrap(super(SingletonMap, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.equals(java.lang.Object)"""
        return bool._wrap(super(_SingletonMap, self).equals(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.getValue()"""
        return object._wrap(super(SingletonMap, self).getValue())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.isEmpty()"""
        return bool._wrap(super(SingletonMap, self).isEmpty())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.map.SingletonMap(K,V)"""
        val = _SingletonMap(arg0, arg1)
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.collections4.map.SingletonMap 
 
 
# CLASS: org.apache.commons.collections4.map.DefaultedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.map.DefaultedMap as _DefaultedMap
_DefaultedMap = _DefaultedMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultedMap():
    """org.apache.commons.collections4.map.DefaultedMap"""
 
    @staticmethod
    def _wrap(java_value: _DefaultedMap) -> 'DefaultedMap':
        return DefaultedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultedMap):
        """
        Dynamic initializer for DefaultedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def defaultedMap(arg0: 'Map', arg1: object) -> 'DefaultedMap':
        """public static <K,V> org.apache.commons.collections4.map.DefaultedMap<K, V> org.apache.commons.collections4.map.DefaultedMap.defaultedMap(java.util.Map<K, V>,V)"""
        return DefaultedMap._wrap(_DefaultedMap.defaultedMap(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.DefaultedMap.get(java.lang.Object)"""
        return object._wrap(super(_DefaultedMap, self).get(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.map.DefaultedMap(org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        val = _DefaultedMap(arg0)
        self.__wrapper = val

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMapDecorator, self).putAll(arg0)

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @staticmethod
    @overload
    def defaultedMap(arg0: 'Map', arg1: 'Factory') -> 'DefaultedMap':
        """public static <K,V> org.apache.commons.collections4.map.DefaultedMap<K, V> org.apache.commons.collections4.map.DefaultedMap.defaultedMap(java.util.Map<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return DefaultedMap._wrap(_DefaultedMap.defaultedMap(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @staticmethod
    @overload
    def defaultedMap(arg0: 'Map', arg1: 'Transformer') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.map.DefaultedMap.defaultedMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return Map._wrap(_DefaultedMap.defaultedMap(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.map.DefaultedMap(V)"""
        val = _DefaultedMap(arg0)
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$KeySetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashIterator
_HashIterator = _AbstractHashedMap_HashIterator.HashIterator
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_KeySetIterator
_KeySetIterator = _AbstractHashedMap_KeySetIterator.KeySetIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeySetIterator():
    """org.apache.commons.collections4.map.AbstractHashedMap.KeySetIterator"""
 
    @staticmethod
    def _wrap(java_value: _KeySetIterator) -> 'KeySetIterator':
        return KeySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeySetIterator):
        """
        Dynamic initializer for KeySetIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeySetIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeySetIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str._wrap(super(HashIterator, self).toString())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$KeySetIterator.next()"""
        return object._wrap(super(KeySetIterator, self).next())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool._wrap(super(HashIterator, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashMapIterator
_HashMapIterator = _AbstractHashedMap_HashMapIterator.HashMapIterator
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashIterator
_HashIterator = _AbstractHashedMap_HashIterator.HashIterator
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashMapIterator():
    """org.apache.commons.collections4.map.AbstractHashedMap.HashMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _HashMapIterator) -> 'HashMapIterator':
        return HashMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashMapIterator):
        """
        Dynamic initializer for HashMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator.getValue()"""
        return object._wrap(super(HashMapIterator, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str._wrap(super(HashIterator, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator.next()"""
        return object._wrap(super(HashMapIterator, self).next())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator.setValue(V)"""
        return object._wrap(super(_HashMapIterator, self).setValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator.getKey()"""
        return object._wrap(super(HashMapIterator, self).getKey())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool._wrap(super(HashIterator, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.TransformedSortedMap
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.map.TransformedMap as _TransformedMap
_TransformedMap = _TransformedMap
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.util.SequencedCollection as SequencedCollection
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
import java.util.Map.Entry as Entry
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import java.util.SortedMap as SortedMap
import java.util.SequencedSet as SequencedSet
from builtins import bool
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.TransformedSortedMap as _TransformedSortedMap
_TransformedSortedMap = _TransformedSortedMap
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedSortedMap():
    """org.apache.commons.collections4.map.TransformedSortedMap"""
 
    @staticmethod
    def _wrap(java_value: _TransformedSortedMap) -> 'TransformedSortedMap':
        return TransformedSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedSortedMap):
        """
        Dynamic initializer for TransformedSortedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedSortedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedSortedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_TransformedSortedMap, self).subMap(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.TransformedSortedMap.firstKey()"""
        return object._wrap(super(TransformedSortedMap, self).firstKey())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @staticmethod
    @overload
    def transformedMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedMap<K, V> org.apache.commons.collections4.map.TransformedMap.transformedMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMap._wrap(_TransformedMap.transformedMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def transformingMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedMap<K, V> org.apache.commons.collections4.map.TransformedMap.transformingMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMap._wrap(_TransformedMap.transformingMap(arg0, arg1, arg2))

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @staticmethod
    @overload
    def transformingSortedMap(arg0: 'SortedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedSortedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedSortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.transformingSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedSortedMap._wrap(_TransformedSortedMap.transformingSortedMap(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.TransformedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_TransformedMap, self).putAll(arg0)

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @staticmethod
    @overload
    def transformedSortedMap(arg0: 'SortedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedSortedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedSortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.transformedSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedSortedMap._wrap(_TransformedSortedMap.transformedSortedMap(arg0, arg1, arg2))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.TransformedSortedMap.comparator()"""
        return 'Comparator'._wrap(super(TransformedSortedMap, self).comparator())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_TransformedSortedMap, self).tailMap(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.TransformedSortedMap.lastKey()"""
        return object._wrap(super(TransformedSortedMap, self).lastKey())

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_TransformedSortedMap, self).headMap(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.TransformedMap.put(K,V)"""
        return object._wrap(super(_TransformedMap, self).put(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.LazySortedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.util.SequencedCollection as SequencedCollection
import org.apache.commons.collections4.map.LazyMap as _LazyMap
_LazyMap = _LazyMap
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
import java.util.Map.Entry as Entry
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import java.util.SortedMap as SortedMap
import java.util.SequencedSet as SequencedSet
from builtins import bool
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from builtins import str
from pyquantum_helper import override
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
import org.apache.commons.collections4.map.LazySortedMap as _LazySortedMap
_LazySortedMap = _LazySortedMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LazySortedMap():
    """org.apache.commons.collections4.map.LazySortedMap"""
 
    @staticmethod
    def _wrap(java_value: _LazySortedMap) -> 'LazySortedMap':
        return LazySortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LazySortedMap):
        """
        Dynamic initializer for LazySortedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LazySortedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LazySortedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Transformer') -> 'LazyMap':
        """public static <V,K> org.apache.commons.collections4.map.LazyMap<K, V> org.apache.commons.collections4.map.LazyMap.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return LazyMap._wrap(_LazyMap.lazyMap(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_LazySortedMap, self).tailMap(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMapDecorator, self).putAll(arg0)

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @staticmethod
    @overload
    def lazySortedMap(arg0: 'SortedMap', arg1: 'Factory') -> 'LazySortedMap':
        """public static <K,V> org.apache.commons.collections4.map.LazySortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.lazySortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return LazySortedMap._wrap(_LazySortedMap.lazySortedMap(arg0, arg1))

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_AbstractMapDecorator, self).put(arg0, arg1))

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Factory') -> 'LazyMap':
        """public static <K,V> org.apache.commons.collections4.map.LazyMap<K, V> org.apache.commons.collections4.map.LazyMap.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return LazyMap._wrap(_LazyMap.lazyMap(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_LazySortedMap, self).headMap(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.LazySortedMap.lastKey()"""
        return object._wrap(super(LazySortedMap, self).lastKey())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.LazySortedMap.comparator()"""
        return 'Comparator'._wrap(super(LazySortedMap, self).comparator())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @staticmethod
    @overload
    def lazySortedMap(arg0: 'SortedMap', arg1: 'Transformer') -> 'LazySortedMap':
        """public static <K,V> org.apache.commons.collections4.map.LazySortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.lazySortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return LazySortedMap._wrap(_LazySortedMap.lazySortedMap(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.LazyMap.get(java.lang.Object)"""
        return object._wrap(super(_LazyMap, self).get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_LazySortedMap, self).subMap(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.LazySortedMap.firstKey()"""
        return object._wrap(super(LazySortedMap, self).firstKey())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter as _EntrySetToMapIteratorAdapter
_EntrySetToMapIteratorAdapter = _EntrySetToMapIteratorAdapter
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.util.Set as Set
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntrySetToMapIteratorAdapter():
    """org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter"""
 
    @staticmethod
    def _wrap(java_value: _EntrySetToMapIteratorAdapter) -> 'EntrySetToMapIteratorAdapter':
        return EntrySetToMapIteratorAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntrySetToMapIteratorAdapter):
        """
        Dynamic initializer for EntrySetToMapIteratorAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntrySetToMapIteratorAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntrySetToMapIteratorAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.hasNext()"""
        return bool._wrap(super(EntrySetToMapIteratorAdapter, self).hasNext())

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
    def reset(self):
        """public synchronized void org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.reset()"""
        super(EntrySetToMapIteratorAdapter, self).reset()

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.next()"""
        return object._wrap(super(EntrySetToMapIteratorAdapter, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.remove()"""
        super(EntrySetToMapIteratorAdapter, self).remove()

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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.getKey()"""
        return object._wrap(super(EntrySetToMapIteratorAdapter, self).getKey())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.getValue()"""
        return object._wrap(super(EntrySetToMapIteratorAdapter, self).getValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.setValue(V)"""
        return object._wrap(super(_EntrySetToMapIteratorAdapter, self).setValue(arg0))

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Set'):
        """public org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter(java.util.Set<java.util.Map$Entry<K, V>>)"""
        val = _EntrySetToMapIteratorAdapter(arg0)
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
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$Values
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_Values
_Values = _AbstractHashedMap_Values.Values
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Values():
    """org.apache.commons.collections4.map.AbstractHashedMap.Values"""
 
    @staticmethod
    def _wrap(java_value: _Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Values):
        """
        Dynamic initializer for Values.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Values__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Values__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object]._wrap(super(AbstractCollection, self).toArray())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<V> org.apache.commons.collections4.map.AbstractHashedMap$Values.iterator()"""
        return 'Iterator'._wrap(super(Values, self).iterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$Values.contains(java.lang.Object)"""
        return bool._wrap(super(_Values, self).contains(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$Values.clear()"""
        super(Values, self).clear()

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool._wrap(super(_AbstractCollection, self).add(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$Values.size()"""
        return int._wrap(super(Values, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).removeAll(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_AbstractCollection, self).remove(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$KeySet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_KeySet
_KeySet = _AbstractHashedMap_KeySet.KeySet
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.AbstractSet as _AbstractSet
_AbstractSet = _AbstractSet
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeySet():
    """org.apache.commons.collections4.map.AbstractHashedMap.KeySet"""
 
    @staticmethod
    def _wrap(java_value: _KeySet) -> 'KeySet':
        return KeySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeySet):
        """
        Dynamic initializer for KeySet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeySet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeySet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int._wrap(super(AbstractSet, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object]._wrap(super(AbstractCollection, self).toArray())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractSet, self).removeAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSet, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$KeySet.clear()"""
        super(KeySet, self).clear()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$KeySet.remove(java.lang.Object)"""
        return bool._wrap(super(_KeySet, self).remove(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$KeySet.size()"""
        return int._wrap(super(KeySet, self).size())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool._wrap(super(_AbstractCollection, self).add(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$KeySet.contains(java.lang.Object)"""
        return bool._wrap(super(_KeySet, self).contains(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> org.apache.commons.collections4.map.AbstractHashedMap$KeySet.iterator()"""
        return 'Iterator'._wrap(super(KeySet, self).iterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty()) 
 
 
# CLASS: org.apache.commons.collections4.map.StaticBucketMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import org.apache.commons.collections4.map.StaticBucketMap as _StaticBucketMap
_StaticBucketMap = _StaticBucketMap
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StaticBucketMap():
    """org.apache.commons.collections4.map.StaticBucketMap"""
 
    @staticmethod
    def _wrap(java_value: _StaticBucketMap) -> 'StaticBucketMap':
        return StaticBucketMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StaticBucketMap):
        """
        Dynamic initializer for StaticBucketMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StaticBucketMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StaticBucketMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.StaticBucketMap.hashCode()"""
        return int._wrap(super(StaticBucketMap, self).hashCode())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.StaticBucketMap.entrySet()"""
        return 'Set'._wrap(super(StaticBucketMap, self).entrySet())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.StaticBucketMap()"""
        val = _StaticBucketMap()
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.StaticBucketMap.put(K,V)"""
        return object._wrap(super(_StaticBucketMap, self).put(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.StaticBucketMap.clear()"""
        super(StaticBucketMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.StaticBucketMap.size()"""
        return int._wrap(super(StaticBucketMap, self).size())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.StaticBucketMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_StaticBucketMap, self).putAll(arg0)

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
    def __init__(self, ):
        """public org.apache.commons.collections4.map.StaticBucketMap()"""
        val = _StaticBucketMap()
        self.__wrapper = val

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.StaticBucketMap.get(java.lang.Object)"""
        return object._wrap(super(_StaticBucketMap, self).get(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.StaticBucketMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_StaticBucketMap, self).containsValue(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.StaticBucketMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_StaticBucketMap, self).containsKey(arg0))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def atomic(self, arg0: 'Runnable'):
        """public void org.apache.commons.collections4.map.StaticBucketMap.atomic(java.lang.Runnable)"""
        super(_StaticBucketMap, self).atomic(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.StaticBucketMap.remove(java.lang.Object)"""
        return object._wrap(super(_StaticBucketMap, self).remove(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.StaticBucketMap.equals(java.lang.Object)"""
        return bool._wrap(super(_StaticBucketMap, self).equals(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.StaticBucketMap.isEmpty()"""
        return bool._wrap(super(StaticBucketMap, self).isEmpty())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.StaticBucketMap.keySet()"""
        return 'Set'._wrap(super(StaticBucketMap, self).keySet())

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
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.StaticBucketMap.values()"""
        return 'Collection'._wrap(super(StaticBucketMap, self).values())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.StaticBucketMap(int)"""
        val = _StaticBucketMap(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$EntrySet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.AbstractSet as _AbstractSet
_AbstractSet = _AbstractSet
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_EntrySet
_EntrySet = _AbstractHashedMap_EntrySet.EntrySet
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntrySet():
    """org.apache.commons.collections4.map.AbstractHashedMap.EntrySet"""
 
    @staticmethod
    def _wrap(java_value: _EntrySet) -> 'EntrySet':
        return EntrySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntrySet):
        """
        Dynamic initializer for EntrySet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntrySet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntrySet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int._wrap(super(AbstractSet, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object]._wrap(super(AbstractCollection, self).toArray())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.clear()"""
        super(EntrySet, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractSet, self).removeAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSet, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool._wrap(super(_AbstractCollection, self).add(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.iterator()"""
        return 'Iterator'._wrap(super(EntrySet, self).iterator())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object]._wrap(super(_AbstractCollection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.remove(java.lang.Object)"""
        return bool._wrap(super(_EntrySet, self).remove(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.size()"""
        return int._wrap(super(EntrySet, self).size())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.contains(java.lang.Object)"""
        return bool._wrap(super(_EntrySet, self).contains(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool._wrap(super(AbstractCollection, self).isEmpty()) 
 
 
# CLASS: org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.map.PassiveExpiringMap as _PassiveExpiringMap_ConstantTimeToLiveExpirationPolicy
_ConstantTimeToLiveExpirationPolicy = _PassiveExpiringMap_ConstantTimeToLiveExpirationPolicy.ConstantTimeToLiveExpirationPolicy
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstantTimeToLiveExpirationPolicy():
    """org.apache.commons.collections4.map.PassiveExpiringMap.ConstantTimeToLiveExpirationPolicy"""
 
    @staticmethod
    def _wrap(java_value: _ConstantTimeToLiveExpirationPolicy) -> 'ConstantTimeToLiveExpirationPolicy':
        return ConstantTimeToLiveExpirationPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantTimeToLiveExpirationPolicy):
        """
        Dynamic initializer for ConstantTimeToLiveExpirationPolicy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantTimeToLiveExpirationPolicy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantTimeToLiveExpirationPolicy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: 'TimeUnit'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy(long,java.util.concurrent.TimeUnit)"""
        val = _ConstantTimeToLiveExpirationPolicy(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy(long)"""
        val = _ConstantTimeToLiveExpirationPolicy(_long.valueOf(arg0))
        self.__wrapper = val

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
        """public org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy()"""
        val = _ConstantTimeToLiveExpirationPolicy()
        self.__wrapper = val

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
    def expirationTime(self, arg0: object, arg1: object) -> int:
        """public long org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy.expirationTime(K,V)"""
        return int._wrap(super(_ConstantTimeToLiveExpirationPolicy, self).expirationTime(arg0, arg1))

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
    def __init__(self, ):
        """public org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy()"""
        val = _ConstantTimeToLiveExpirationPolicy()
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
 
 
# CLASS: org.apache.commons.collections4.map.ReferenceIdentityMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.ReferenceIdentityMap as _ReferenceIdentityMap
_ReferenceIdentityMap = _ReferenceIdentityMap
import java.lang.Boolean as _boolean
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Float as _float
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.map.AbstractReferenceMap as _AbstractReferenceMap
_AbstractReferenceMap = _AbstractReferenceMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReferenceIdentityMap():
    """org.apache.commons.collections4.map.ReferenceIdentityMap"""
 
    @staticmethod
    def _wrap(java_value: _ReferenceIdentityMap) -> 'ReferenceIdentityMap':
        return ReferenceIdentityMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReferenceIdentityMap):
        """
        Dynamic initializer for ReferenceIdentityMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReferenceIdentityMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReferenceIdentityMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractReferenceMap.entrySet()"""
        return 'Set'._wrap(super(AbstractReferenceMap, self).entrySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractReferenceMap, self).remove(arg0))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength'):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength)"""
        val = _ReferenceIdentityMap(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractReferenceMap.size()"""
        return int._wrap(super(AbstractReferenceMap, self).size())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.isEmpty()"""
        return bool._wrap(super(AbstractReferenceMap, self).isEmpty())

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
    def __init__(self, ):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap()"""
        val = _ReferenceIdentityMap()
        self.__wrapper = val

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractReferenceMap.keySet()"""
        return 'Set'._wrap(super(AbstractReferenceMap, self).keySet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractReferenceMap, self).get(arg0))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: bool):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,boolean)"""
        val = _ReferenceIdentityMap(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractReferenceMap, self).containsValue(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap()"""
        val = _ReferenceIdentityMap()
        self.__wrapper = val

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: int, arg3: float):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,int,float)"""
        val = _ReferenceIdentityMap(arg0, arg1, _int.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractReferenceMap, self).containsKey(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractReferenceMap.values()"""
        return 'Collection'._wrap(super(AbstractReferenceMap, self).values())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractReferenceMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractReferenceMap, self).mapIterator())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.put(K,V)"""
        return object._wrap(super(_AbstractReferenceMap, self).put(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractReferenceMap.clear()"""
        super(AbstractReferenceMap, self).clear()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: int, arg3: float, arg4: bool):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,int,float,boolean)"""
        val = _ReferenceIdentityMap(arg0, arg1, _int.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.PredicatedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
import org.apache.commons.collections4.map.PredicatedMap as _PredicatedMap
_PredicatedMap = _PredicatedMap
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedMap():
    """org.apache.commons.collections4.map.PredicatedMap"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedMap) -> 'PredicatedMap':
        return PredicatedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedMap):
        """
        Dynamic initializer for PredicatedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.PredicatedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_PredicatedMap, self).putAll(arg0)

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.PredicatedMap.put(K,V)"""
        return object._wrap(super(_PredicatedMap, self).put(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def predicatedMap(arg0: 'Map', arg1: 'Predicate', arg2: 'Predicate') -> 'PredicatedMap':
        """public static <K,V> org.apache.commons.collections4.map.PredicatedMap<K, V> org.apache.commons.collections4.map.PredicatedMap.predicatedMap(java.util.Map<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return PredicatedMap._wrap(_PredicatedMap.predicatedMap(arg0, arg1, arg2))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.TransformedMap
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.map.TransformedMap as _TransformedMap
_TransformedMap = _TransformedMap
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedMap():
    """org.apache.commons.collections4.map.TransformedMap"""
 
    @staticmethod
    def _wrap(java_value: _TransformedMap) -> 'TransformedMap':
        return TransformedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedMap):
        """
        Dynamic initializer for TransformedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.TransformedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_TransformedMap, self).putAll(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def transformedMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedMap<K, V> org.apache.commons.collections4.map.TransformedMap.transformedMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMap._wrap(_TransformedMap.transformedMap(arg0, arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @staticmethod
    @overload
    def transformingMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedMap<K, V> org.apache.commons.collections4.map.TransformedMap.transformingMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMap._wrap(_TransformedMap.transformingMap(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.TransformedMap.put(K,V)"""
        return object._wrap(super(_TransformedMap, self).put(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.LinkedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap
_AbstractLinkedMap = _AbstractLinkedMap
import org.apache.commons.collections4.map.LinkedMap as _LinkedMap
_LinkedMap = _LinkedMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.lang.Float as _float
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class LinkedMap():
    """org.apache.commons.collections4.map.LinkedMap"""
 
    @staticmethod
    def _wrap(java_value: _LinkedMap) -> 'LinkedMap':
        return LinkedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinkedMap):
        """
        Dynamic initializer for LinkedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinkedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinkedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.LinkedMap()"""
        val = _LinkedMap()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.LinkedMap()"""
        val = _LinkedMap()
        self.__wrapper = val

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.lastKey()"""
        return object._wrap(super(AbstractLinkedMap, self).lastKey())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool._wrap(super(AbstractHashedMap, self).isEmpty())

    @overload
    def clone(self) -> 'LinkedMap':
        """public org.apache.commons.collections4.map.LinkedMap<K, V> org.apache.commons.collections4.map.LinkedMap.clone()"""
        return 'LinkedMap'._wrap(super(LinkedMap, self).clone())

    @overload
    def remove(self, arg0: int) -> object:
        """public V org.apache.commons.collections4.map.LinkedMap.remove(int)"""
        return object._wrap(super(_LinkedMap, self).remove(_int.valueOf(arg0)))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.previousKey(java.lang.Object)"""
        return object._wrap(super(_AbstractLinkedMap, self).previousKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int._wrap(super(AbstractHashedMap, self).size())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'._wrap(super(AbstractHashedMap, self).values())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public org.apache.commons.collections4.map.LinkedMap(int,float)"""
        val = _LinkedMap(_int.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.map.LinkedMap.indexOf(java.lang.Object)"""
        return int._wrap(super(_LinkedMap, self).indexOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @overload
    def getValue(self, arg0: int) -> object:
        """public V org.apache.commons.collections4.map.LinkedMap.getValue(int)"""
        return object._wrap(super(_LinkedMap, self).getValue(_int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap.clear()"""
        super(AbstractLinkedMap, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedMap, self).containsValue(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public K org.apache.commons.collections4.map.LinkedMap.get(int)"""
        return object._wrap(super(_LinkedMap, self).get(_int.valueOf(arg0)))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.LinkedMap(java.util.Map<? extends K, ? extends V>)"""
        val = _LinkedMap(arg0)
        self.__wrapper = val

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractLinkedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractLinkedMap, self).mapIterator())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.nextKey(java.lang.Object)"""
        return object._wrap(super(_AbstractLinkedMap, self).nextKey(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).get(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.firstKey()"""
        return object._wrap(super(AbstractLinkedMap, self).firstKey())

    @overload
    def asList(self) -> 'List':
        """public java.util.List<K> org.apache.commons.collections4.map.LinkedMap.asList()"""
        return 'List'._wrap(super(LinkedMap, self).asList())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object._wrap(super(_AbstractHashedMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.LinkedMap(int)"""
        val = _LinkedMap(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap
_AbstractLinkedMap = _AbstractLinkedMap
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractLinkedMap():
    """org.apache.commons.collections4.map.AbstractLinkedMap"""
 
    @staticmethod
    def _wrap(java_value: _AbstractLinkedMap) -> 'AbstractLinkedMap':
        return AbstractLinkedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractLinkedMap):
        """
        Dynamic initializer for AbstractLinkedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractLinkedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractLinkedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.lastKey()"""
        return object._wrap(super(AbstractLinkedMap, self).lastKey())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool._wrap(super(AbstractHashedMap, self).isEmpty())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.previousKey(java.lang.Object)"""
        return object._wrap(super(_AbstractLinkedMap, self).previousKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int._wrap(super(AbstractHashedMap, self).size())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'._wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap.clear()"""
        super(AbstractLinkedMap, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedMap, self).containsValue(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractLinkedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractLinkedMap, self).mapIterator())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.nextKey(java.lang.Object)"""
        return object._wrap(super(_AbstractLinkedMap, self).nextKey(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).get(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.firstKey()"""
        return object._wrap(super(AbstractLinkedMap, self).firstKey())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object._wrap(super(_AbstractHashedMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_LinkIterator
_LinkIterator = _AbstractLinkedMap_LinkIterator.LinkIterator
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinkIterator():
    """org.apache.commons.collections4.map.AbstractLinkedMap.LinkIterator"""
 
    @staticmethod
    def _wrap(java_value: _LinkIterator) -> 'LinkIterator':
        return LinkIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinkIterator):
        """
        Dynamic initializer for LinkIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinkIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinkIterator__wrapper":
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool._wrap(super(LinkIterator, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool._wrap(super(LinkIterator, self).hasPrevious())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str._wrap(super(LinkIterator, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$HashIterator
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashIterator
_HashIterator = _AbstractHashedMap_HashIterator.HashIterator
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
 
class HashIterator():
    """org.apache.commons.collections4.map.AbstractHashedMap.HashIterator"""
 
    @staticmethod
    def _wrap(java_value: _HashIterator) -> 'HashIterator':
        return HashIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashIterator):
        """
        Dynamic initializer for HashIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

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
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str._wrap(super(HashIterator, self).toString())

    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool._wrap(super(HashIterator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.Flat3Map
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.map.Flat3Map as _Flat3Map
_Flat3Map = _Flat3Map
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Flat3Map():
    """org.apache.commons.collections4.map.Flat3Map"""
 
    @staticmethod
    def _wrap(java_value: _Flat3Map) -> 'Flat3Map':
        return Flat3Map(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Flat3Map):
        """
        Dynamic initializer for Flat3Map.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Flat3Map__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Flat3Map__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.Flat3Map.get(java.lang.Object)"""
        return object._wrap(super(_Flat3Map, self).get(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.Flat3Map.keySet()"""
        return 'Set'._wrap(super(Flat3Map, self).keySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def clone(self) -> 'Flat3Map':
        """public org.apache.commons.collections4.map.Flat3Map<K, V> org.apache.commons.collections4.map.Flat3Map.clone()"""
        return 'Flat3Map'._wrap(super(Flat3Map, self).clone())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.Flat3Map.containsKey(java.lang.Object)"""
        return bool._wrap(super(_Flat3Map, self).containsKey(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.Flat3Map.hashCode()"""
        return int._wrap(super(Flat3Map, self).hashCode())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.Flat3Map.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(Flat3Map, self).mapIterator())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.Flat3Map.put(K,V)"""
        return object._wrap(super(_Flat3Map, self).put(arg0, arg1))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.Flat3Map.equals(java.lang.Object)"""
        return bool._wrap(super(_Flat3Map, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.Flat3Map.remove(java.lang.Object)"""
        return object._wrap(super(_Flat3Map, self).remove(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.Flat3Map.clear()"""
        super(Flat3Map, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.Flat3Map.entrySet()"""
        return 'Set'._wrap(super(Flat3Map, self).entrySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.Flat3Map.values()"""
        return 'Collection'._wrap(super(Flat3Map, self).values())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.Flat3Map.size()"""
        return int._wrap(super(Flat3Map, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.Flat3Map.toString()"""
        return str._wrap(super(Flat3Map, self).toString())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.Flat3Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_Flat3Map, self).putAll(arg0)

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.Flat3Map()"""
        val = _Flat3Map()
        self.__wrapper = val

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.Flat3Map.containsValue(java.lang.Object)"""
        return bool._wrap(super(_Flat3Map, self).containsValue(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.Flat3Map()"""
        val = _Flat3Map()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.Flat3Map(java.util.Map<? extends K, ? extends V>)"""
        val = _Flat3Map(arg0)
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.Flat3Map.isEmpty()"""
        return bool._wrap(super(Flat3Map, self).isEmpty())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractSortedMapDecorator$SortedMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter as _EntrySetToMapIteratorAdapter
_EntrySetToMapIteratorAdapter = _EntrySetToMapIteratorAdapter
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as _AbstractSortedMapDecorator_SortedMapIterator
_SortedMapIterator = _AbstractSortedMapDecorator_SortedMapIterator.SortedMapIterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SortedMapIterator():
    """org.apache.commons.collections4.map.AbstractSortedMapDecorator.SortedMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _SortedMapIterator) -> 'SortedMapIterator':
        return SortedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SortedMapIterator):
        """
        Dynamic initializer for SortedMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SortedMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SortedMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.hasNext()"""
        return bool._wrap(super(EntrySetToMapIteratorAdapter, self).hasNext())

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator$SortedMapIterator.previous()"""
        return object._wrap(super(SortedMapIterator, self).previous())

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
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractSortedMapDecorator$SortedMapIterator.hasPrevious()"""
        return bool._wrap(super(SortedMapIterator, self).hasPrevious())

    @override
    @overload
    def reset(self):
        """public synchronized void org.apache.commons.collections4.map.AbstractSortedMapDecorator$SortedMapIterator.reset()"""
        super(SortedMapIterator, self).reset()

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.next()"""
        return object._wrap(super(EntrySetToMapIteratorAdapter, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.remove()"""
        super(EntrySetToMapIteratorAdapter, self).remove()

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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.getKey()"""
        return object._wrap(super(EntrySetToMapIteratorAdapter, self).getKey())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.getValue()"""
        return object._wrap(super(EntrySetToMapIteratorAdapter, self).getValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.setValue(V)"""
        return object._wrap(super(_EntrySetToMapIteratorAdapter, self).setValue(arg0))

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractMapDecorator
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMapDecorator():
    """org.apache.commons.collections4.map.AbstractMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMapDecorator) -> 'AbstractMapDecorator':
        return AbstractMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMapDecorator):
        """
        Dynamic initializer for AbstractMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMapDecorator, self).putAll(arg0)

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.CaseInsensitiveMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
import java.lang.Object as _object
import org.apache.commons.collections4.map.CaseInsensitiveMap as _CaseInsensitiveMap
_CaseInsensitiveMap = _CaseInsensitiveMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Float as _float
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CaseInsensitiveMap():
    """org.apache.commons.collections4.map.CaseInsensitiveMap"""
 
    @staticmethod
    def _wrap(java_value: _CaseInsensitiveMap) -> 'CaseInsensitiveMap':
        return CaseInsensitiveMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CaseInsensitiveMap):
        """
        Dynamic initializer for CaseInsensitiveMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CaseInsensitiveMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CaseInsensitiveMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap()"""
        val = _CaseInsensitiveMap()
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsValue(arg0))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap(int)"""
        val = _CaseInsensitiveMap(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool._wrap(super(AbstractHashedMap, self).isEmpty())

    @overload
    def clone(self) -> 'CaseInsensitiveMap':
        """public org.apache.commons.collections4.map.CaseInsensitiveMap<K, V> org.apache.commons.collections4.map.CaseInsensitiveMap.clone()"""
        return 'CaseInsensitiveMap'._wrap(super(CaseInsensitiveMap, self).clone())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int._wrap(super(AbstractHashedMap, self).size())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'._wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractHashedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractHashedMap, self).mapIterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap(int,float)"""
        val = _CaseInsensitiveMap(_int.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap()"""
        val = _CaseInsensitiveMap()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.clear()"""
        super(AbstractHashedMap, self).clear()

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).get(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object._wrap(super(_AbstractHashedMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap(java.util.Map<? extends K, ? extends V>)"""
        val = _CaseInsensitiveMap(arg0)
        self.__wrapper = val

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.ListOrderedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.map.ListOrderedMap as _ListOrderedMap
_ListOrderedMap = _ListOrderedMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ListOrderedMap():
    """org.apache.commons.collections4.map.ListOrderedMap"""
 
    @staticmethod
    def _wrap(java_value: _ListOrderedMap) -> 'ListOrderedMap':
        return ListOrderedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListOrderedMap):
        """
        Dynamic initializer for ListOrderedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListOrderedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListOrderedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.remove(java.lang.Object)"""
        return object._wrap(super(_ListOrderedMap, self).remove(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.ListOrderedMap()"""
        val = _ListOrderedMap()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.lastKey()"""
        return object._wrap(super(ListOrderedMap, self).lastKey())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.ListOrderedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_ListOrderedMap, self).putAll(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.ListOrderedMap.toString()"""
        return str._wrap(super(ListOrderedMap, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @staticmethod
    @overload
    def listOrderedMap(arg0: 'Map') -> 'ListOrderedMap':
        """public static <K,V> org.apache.commons.collections4.map.ListOrderedMap<K, V> org.apache.commons.collections4.map.ListOrderedMap.listOrderedMap(java.util.Map<K, V>)"""
        return ListOrderedMap._wrap(_ListOrderedMap.listOrderedMap(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.nextKey(java.lang.Object)"""
        return object._wrap(super(_ListOrderedMap, self).nextKey(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.ListOrderedMap.values()"""
        return 'Collection'._wrap(super(ListOrderedMap, self).values())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.ListOrderedMap()"""
        val = _ListOrderedMap()
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.ListOrderedMap.clear()"""
        super(ListOrderedMap, self).clear()

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.previousKey(java.lang.Object)"""
        return object._wrap(super(_ListOrderedMap, self).previousKey(arg0))

    @overload
    def valueList(self) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.map.ListOrderedMap.valueList()"""
        return 'List'._wrap(super(ListOrderedMap, self).valueList())

    @overload
    def setValue(self, arg0: int, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.setValue(int,V)"""
        return object._wrap(super(_ListOrderedMap, self).setValue(_int.valueOf(arg0), arg1))

    @overload
    def asList(self) -> 'List':
        """public java.util.List<K> org.apache.commons.collections4.map.ListOrderedMap.asList()"""
        return 'List'._wrap(super(ListOrderedMap, self).asList())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.ListOrderedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(ListOrderedMap, self).mapIterator())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def put(self, arg0: int, arg1: object, arg2: object) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.put(int,K,V)"""
        return object._wrap(super(_ListOrderedMap, self).put(_int.valueOf(arg0), arg1, arg2))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.firstKey()"""
        return object._wrap(super(ListOrderedMap, self).firstKey())

    @overload
    def putAll(self, arg0: int, arg1: 'Map'):
        """public void org.apache.commons.collections4.map.ListOrderedMap.putAll(int,java.util.Map<? extends K, ? extends V>)"""
        super(_ListOrderedMap, self).putAll(_int.valueOf(arg0), arg1)

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: int) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.get(int)"""
        return object._wrap(super(_ListOrderedMap, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.ListOrderedMap.entrySet()"""
        return 'Set'._wrap(super(ListOrderedMap, self).entrySet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def keyList(self) -> 'List':
        """public java.util.List<K> org.apache.commons.collections4.map.ListOrderedMap.keyList()"""
        return 'List'._wrap(super(ListOrderedMap, self).keyList())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.map.ListOrderedMap.indexOf(java.lang.Object)"""
        return int._wrap(super(_ListOrderedMap, self).indexOf(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def getValue(self, arg0: int) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.getValue(int)"""
        return object._wrap(super(_ListOrderedMap, self).getValue(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.put(K,V)"""
        return object._wrap(super(_ListOrderedMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.ListOrderedMap.keySet()"""
        return 'Set'._wrap(super(ListOrderedMap, self).keySet())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def remove(self, arg0: int) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.remove(int)"""
        return object._wrap(super(_ListOrderedMap, self).remove(_int.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.collections4.map.CompositeMap$MapMutator
import org.apache.commons.collections4.map.CompositeMap as _CompositeMap_MapMutator
_MapMutator = _CompositeMap_MapMutator.MapMutator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class MapMutator():
    """org.apache.commons.collections4.map.CompositeMap.MapMutator"""
 
    @staticmethod
    def _wrap(java_value: _MapMutator) -> 'MapMutator':
        return MapMutator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapMutator):
        """
        Dynamic initializer for MapMutator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapMutator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapMutator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def resolveCollision(self, arg0: 'CompositeMap', arg1: 'Map', arg2: 'Map', arg3: 'Collection'):
        """public abstract void org.apache.commons.collections4.map.CompositeMap$MapMutator.resolveCollision(org.apache.commons.collections4.map.CompositeMap<K, V>,java.util.Map<K, V>,java.util.Map<K, V>,java.util.Collection<K>)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'CompositeMap', arg1: 'Map', arg2: 'Map'):
        """public abstract void org.apache.commons.collections4.map.CompositeMap$MapMutator.putAll(org.apache.commons.collections4.map.CompositeMap<K, V>,java.util.Map<K, V>[],java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def put(self, arg0: 'CompositeMap', arg1: 'Map', arg2: object, arg3: object):
        """public abstract V org.apache.commons.collections4.map.CompositeMap$MapMutator.put(org.apache.commons.collections4.map.CompositeMap<K, V>,java.util.Map<K, V>[],K,V)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractOrderedMapDecorator
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
from builtins import bool
from builtins import str
import org.apache.commons.collections4.map.AbstractOrderedMapDecorator as _AbstractOrderedMapDecorator
_AbstractOrderedMapDecorator = _AbstractOrderedMapDecorator
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractOrderedMapDecorator():
    """org.apache.commons.collections4.map.AbstractOrderedMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractOrderedMapDecorator) -> 'AbstractOrderedMapDecorator':
        return AbstractOrderedMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractOrderedMapDecorator):
        """
        Dynamic initializer for AbstractOrderedMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractOrderedMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractOrderedMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.firstKey()"""
        return object._wrap(super(AbstractOrderedMapDecorator, self).firstKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractOrderedMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractOrderedMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMapDecorator, self).putAll(arg0)

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.lastKey()"""
        return object._wrap(super(AbstractOrderedMapDecorator, self).lastKey())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractOrderedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractOrderedMapDecorator, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'OrderedMap'):
        """public org.apache.commons.collections4.map.AbstractOrderedMapDecorator(org.apache.commons.collections4.OrderedMap<K, V>)"""
        val = _AbstractOrderedMapDecorator(arg0)
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.PassiveExpiringMap$ExpirationPolicy
import org.apache.commons.collections4.map.PassiveExpiringMap as _PassiveExpiringMap_ExpirationPolicy
_ExpirationPolicy = _PassiveExpiringMap_ExpirationPolicy.ExpirationPolicy
from abc import abstractmethod, ABC
 
class ExpirationPolicy():
    """org.apache.commons.collections4.map.PassiveExpiringMap.ExpirationPolicy"""
 
    @staticmethod
    def _wrap(java_value: _ExpirationPolicy) -> 'ExpirationPolicy':
        return ExpirationPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExpirationPolicy):
        """
        Dynamic initializer for ExpirationPolicy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExpirationPolicy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExpirationPolicy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def expirationTime(self, arg0: object, arg1: object):
        """public abstract long org.apache.commons.collections4.map.PassiveExpiringMap$ExpirationPolicy.expirationTime(K,V)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$EntrySetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_EntrySetIterator
_EntrySetIterator = _AbstractLinkedMap_EntrySetIterator.EntrySetIterator
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_LinkIterator
_LinkIterator = _AbstractLinkedMap_LinkIterator.LinkIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntrySetIterator():
    """org.apache.commons.collections4.map.AbstractLinkedMap.EntrySetIterator"""
 
    @staticmethod
    def _wrap(java_value: _EntrySetIterator) -> 'EntrySetIterator':
        return EntrySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntrySetIterator):
        """
        Dynamic initializer for EntrySetIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntrySetIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntrySetIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool._wrap(super(LinkIterator, self).hasNext())

    @override
    @overload
    def next(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.map.AbstractLinkedMap$EntrySetIterator.next()"""
        return 'Entry.Map$Entry'._wrap(super(EntrySetIterator, self).next())

    @override
    @overload
    def previous(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.map.AbstractLinkedMap$EntrySetIterator.previous()"""
        return 'Entry.Map$Entry'._wrap(super(EntrySetIterator, self).previous())

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
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str._wrap(super(LinkIterator, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool._wrap(super(LinkIterator, self).hasPrevious())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.LRUMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.lang.Boolean as _boolean
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap
_AbstractLinkedMap = _AbstractLinkedMap
import org.apache.commons.collections4.map.LRUMap as _LRUMap
_LRUMap = _LRUMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.lang.Float as _float
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LRUMap():
    """org.apache.commons.collections4.map.LRUMap"""
 
    @staticmethod
    def _wrap(java_value: _LRUMap) -> 'LRUMap':
        return LRUMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LRUMap):
        """
        Dynamic initializer for LRUMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LRUMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LRUMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.LRUMap.isFull()"""
        return bool._wrap(super(LRUMap, self).isFull())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.lastKey()"""
        return object._wrap(super(AbstractLinkedMap, self).lastKey())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.previousKey(java.lang.Object)"""
        return object._wrap(super(_AbstractLinkedMap, self).previousKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int._wrap(super(AbstractHashedMap, self).size())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public org.apache.commons.collections4.map.LRUMap(int,int,float)"""
        val = _LRUMap(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.LRUMap(java.util.Map<? extends K, ? extends V>)"""
        val = _LRUMap(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Map', arg1: bool):
        """public org.apache.commons.collections4.map.LRUMap(java.util.Map<? extends K, ? extends V>,boolean)"""
        val = _LRUMap(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def isScanUntilRemovable(self) -> bool:
        """public boolean org.apache.commons.collections4.map.LRUMap.isScanUntilRemovable()"""
        return bool._wrap(super(LRUMap, self).isScanUntilRemovable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsKey(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.nextKey(java.lang.Object)"""
        return object._wrap(super(_AbstractLinkedMap, self).nextKey(arg0))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.firstKey()"""
        return object._wrap(super(AbstractLinkedMap, self).firstKey())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object._wrap(super(_AbstractHashedMap, self).put(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.LRUMap.get(java.lang.Object)"""
        return object._wrap(super(_LRUMap, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: bool):
        """public org.apache.commons.collections4.map.LRUMap(int,float,boolean)"""
        val = _LRUMap(_int.valueOf(arg0), _float.valueOf(arg1), _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def get(self, arg0: object, arg1: bool) -> object:
        """public V org.apache.commons.collections4.map.LRUMap.get(java.lang.Object,boolean)"""
        return object._wrap(super(_LRUMap, self).get(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public org.apache.commons.collections4.map.LRUMap(int,boolean)"""
        val = _LRUMap(_int.valueOf(arg0), _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public org.apache.commons.collections4.map.LRUMap(int,float)"""
        val = _LRUMap(_int.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool._wrap(super(AbstractHashedMap, self).isEmpty())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.collections4.map.LRUMap(int,int)"""
        val = _LRUMap(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'._wrap(super(AbstractHashedMap, self).values())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.LRUMap(int)"""
        val = _LRUMap(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.LRUMap.maxSize()"""
        return int._wrap(super(LRUMap, self).maxSize())

    @overload
    def clone(self) -> 'LRUMap':
        """public org.apache.commons.collections4.map.LRUMap<K, V> org.apache.commons.collections4.map.LRUMap.clone()"""
        return 'LRUMap'._wrap(super(LRUMap, self).clone())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap.clear()"""
        super(AbstractLinkedMap, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractLinkedMap, self).containsValue(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.LRUMap()"""
        val = _LRUMap()
        self.__wrapper = val

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).keySet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractLinkedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractLinkedMap, self).mapIterator())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: bool):
        """public org.apache.commons.collections4.map.LRUMap(int,int,float,boolean)"""
        val = _LRUMap(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.LRUMap()"""
        val = _LRUMap()
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.map.CompositeMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.CompositeMap as _CompositeMap
_CompositeMap = _CompositeMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CompositeMap():
    """org.apache.commons.collections4.map.CompositeMap"""
 
    @staticmethod
    def _wrap(java_value: _CompositeMap) -> 'CompositeMap':
        return CompositeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CompositeMap):
        """
        Dynamic initializer for CompositeMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CompositeMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CompositeMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.CompositeMap.values()"""
        return 'Collection'._wrap(super(CompositeMap, self).values())

    @overload
    def __init__(self, *arg0: 'Map'):
        """public org.apache.commons.collections4.map.CompositeMap(java.util.Map<K, V>...)"""
        val = _CompositeMap(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addComposited(self, arg0: 'Map'):
        """public synchronized void org.apache.commons.collections4.map.CompositeMap.addComposited(java.util.Map<K, V>) throws java.lang.IllegalArgumentException"""
        super(_CompositeMap, self).addComposited(arg0)

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.CompositeMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_CompositeMap, self).putAll(arg0)

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
    def __init__(self, ):
        """public org.apache.commons.collections4.map.CompositeMap()"""
        val = _CompositeMap()
        self.__wrapper = val

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def setMutator(self, arg0: 'MapMutator'):
        """public void org.apache.commons.collections4.map.CompositeMap.setMutator(org.apache.commons.collections4.map.CompositeMap$MapMutator<K, V>)"""
        super(_CompositeMap, self).setMutator(arg0)

    @overload
    def removeComposited(self, arg0: 'Map') -> 'Map':
        """public synchronized java.util.Map<K, V> org.apache.commons.collections4.map.CompositeMap.removeComposited(java.util.Map<K, V>)"""
        return 'Map'._wrap(super(_CompositeMap, self).removeComposited(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.CompositeMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_CompositeMap, self).containsKey(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.CompositeMap.size()"""
        return int._wrap(super(CompositeMap, self).size())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.CompositeMap()"""
        val = _CompositeMap()
        self.__wrapper = val

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.CompositeMap.remove(java.lang.Object)"""
        return object._wrap(super(_CompositeMap, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.CompositeMap.get(java.lang.Object)"""
        return object._wrap(super(_CompositeMap, self).get(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.CompositeMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_CompositeMap, self).containsValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Map', arg1: 'MapMutator'):
        """public org.apache.commons.collections4.map.CompositeMap(java.util.Map<K, V>[],org.apache.commons.collections4.map.CompositeMap$MapMutator<K, V>)"""
        val = _CompositeMap(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.CompositeMap.clear()"""
        super(CompositeMap, self).clear()

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.CompositeMap.put(K,V)"""
        return object._wrap(super(_CompositeMap, self).put(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.CompositeMap.hashCode()"""
        return int._wrap(super(CompositeMap, self).hashCode())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.CompositeMap.keySet()"""
        return 'Set'._wrap(super(CompositeMap, self).keySet())

    @overload
    def __init__(self, arg0: 'Map', arg1: 'Map', arg2: 'MapMutator'):
        """public org.apache.commons.collections4.map.CompositeMap(java.util.Map<K, V>,java.util.Map<K, V>,org.apache.commons.collections4.map.CompositeMap$MapMutator<K, V>)"""
        val = _CompositeMap(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.CompositeMap.entrySet()"""
        return 'Set'._wrap(super(CompositeMap, self).entrySet())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.CompositeMap.equals(java.lang.Object)"""
        return bool._wrap(super(_CompositeMap, self).equals(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.CompositeMap.isEmpty()"""
        return bool._wrap(super(CompositeMap, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Map', arg1: 'Map'):
        """public org.apache.commons.collections4.map.CompositeMap(java.util.Map<K, V>,java.util.Map<K, V>)"""
        val = _CompositeMap(arg0, arg1)
        self.__wrapper = val

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableEntrySet
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import org.apache.commons.collections4.map.UnmodifiableEntrySet as _UnmodifiableEntrySet
_UnmodifiableEntrySet = _UnmodifiableEntrySet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Map.Entry as Entry
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableEntrySet():
    """org.apache.commons.collections4.map.UnmodifiableEntrySet"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableEntrySet) -> 'UnmodifiableEntrySet':
        return UnmodifiableEntrySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableEntrySet):
        """
        Dynamic initializer for UnmodifiableEntrySet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableEntrySet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableEntrySet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableEntrySet, self).retainAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableEntrySet.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableEntrySet, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.addAll(java.util.Collection<? extends java.util.Map$Entry<K, V>>)"""
        return bool._wrap(super(_UnmodifiableEntrySet, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(set.AbstractSetDecorator, self).hashCode())

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
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableEntrySet, self).removeAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_set.AbstractSetDecorator, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.map.UnmodifiableEntrySet.toArray(T[])"""
        return List[object]._wrap(super(_UnmodifiableEntrySet, self).toArray(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @staticmethod
    @overload
    def unmodifiableEntrySet(arg0: 'Set') -> 'Set':
        """public static <K,V> java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableEntrySet.unmodifiableEntrySet(java.util.Set<java.util.Map$Entry<K, V>>)"""
        return Set._wrap(_UnmodifiableEntrySet.unmodifiableEntrySet(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.map.UnmodifiableEntrySet.toArray()"""
        return List[object]._wrap(super(UnmodifiableEntrySet, self).toArray())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableEntrySet, self).remove(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.removeIf(java.util.function.Predicate<? super java.util.Map$Entry<K, V>>)"""
        return bool._wrap(super(_UnmodifiableEntrySet, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def add(self, arg0: 'Entry') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.add(java.util.Map$Entry<K, V>)"""
        return bool._wrap(super(_UnmodifiableEntrySet, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableEntrySet.clear()"""
        super(UnmodifiableEntrySet, self).clear() 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_LinkMapIterator
_LinkMapIterator = _AbstractLinkedMap_LinkMapIterator.LinkMapIterator
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_LinkIterator
_LinkIterator = _AbstractLinkedMap_LinkIterator.LinkIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinkMapIterator():
    """org.apache.commons.collections4.map.AbstractLinkedMap.LinkMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _LinkMapIterator) -> 'LinkMapIterator':
        return LinkMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinkMapIterator):
        """
        Dynamic initializer for LinkMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinkMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinkMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool._wrap(super(LinkIterator, self).hasNext())

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
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.getValue()"""
        return object._wrap(super(LinkMapIterator, self).getValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.setValue(V)"""
        return object._wrap(super(_LinkMapIterator, self).setValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.getKey()"""
        return object._wrap(super(LinkMapIterator, self).getKey())

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.previous()"""
        return object._wrap(super(LinkMapIterator, self).previous())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str._wrap(super(LinkIterator, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.next()"""
        return object._wrap(super(LinkMapIterator, self).next())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool._wrap(super(LinkIterator, self).hasPrevious())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.FixedSizeMap
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.map.FixedSizeMap as _FixedSizeMap
_FixedSizeMap = _FixedSizeMap
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FixedSizeMap():
    """org.apache.commons.collections4.map.FixedSizeMap"""
 
    @staticmethod
    def _wrap(java_value: _FixedSizeMap) -> 'FixedSizeMap':
        return FixedSizeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FixedSizeMap):
        """
        Dynamic initializer for FixedSizeMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FixedSizeMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FixedSizeMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.FixedSizeMap.maxSize()"""
        return int._wrap(super(FixedSizeMap, self).maxSize())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.FixedSizeMap.put(K,V)"""
        return object._wrap(super(_FixedSizeMap, self).put(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.FixedSizeMap.clear()"""
        super(FixedSizeMap, self).clear()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @staticmethod
    @overload
    def fixedSizeMap(arg0: 'Map') -> 'FixedSizeMap':
        """public static <K,V> org.apache.commons.collections4.map.FixedSizeMap<K, V> org.apache.commons.collections4.map.FixedSizeMap.fixedSizeMap(java.util.Map<K, V>)"""
        return FixedSizeMap._wrap(_FixedSizeMap.fixedSizeMap(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.FixedSizeMap.values()"""
        return 'Collection'._wrap(super(FixedSizeMap, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.FixedSizeMap.keySet()"""
        return 'Set'._wrap(super(FixedSizeMap, self).keySet())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.FixedSizeMap.remove(java.lang.Object)"""
        return object._wrap(super(_FixedSizeMap, self).remove(arg0))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.FixedSizeMap.isFull()"""
        return bool._wrap(super(FixedSizeMap, self).isFull())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.FixedSizeMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_FixedSizeMap, self).putAll(arg0)

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.FixedSizeMap.entrySet()"""
        return 'Set'._wrap(super(FixedSizeMap, self).entrySet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.MultiValueMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.MultiValueMap as _MultiValueMap
_MultiValueMap = _MultiValueMap
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.util.Iterator as Iterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiValueMap():
    """org.apache.commons.collections4.map.MultiValueMap"""
 
    @staticmethod
    def _wrap(java_value: _MultiValueMap) -> 'MultiValueMap':
        return MultiValueMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiValueMap):
        """
        Dynamic initializer for MultiValueMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiValueMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiValueMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public java.lang.Object org.apache.commons.collections4.map.MultiValueMap.put(K,java.lang.Object)"""
        return object._wrap(super(_MultiValueMap, self).put(arg0, arg1))

    @overload
    def putAll(self, arg0: object, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.MultiValueMap.putAll(K,java.util.Collection<V>)"""
        return bool._wrap(super(_MultiValueMap, self).putAll(arg0, arg1))

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map', arg1: 'Class') -> 'MultiValueMap':
        """public static <K,V,C extends java.util.Collection<V>> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.map.MultiValueMap.multiValueMap(java.util.Map<K, ? super C>,java.lang.Class<C>)"""
        return MultiValueMap._wrap(_MultiValueMap.multiValueMap(arg0, arg1))

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map') -> 'MultiValueMap':
        """public static <K,V> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.map.MultiValueMap.multiValueMap(java.util.Map<K, ? super java.util.Collection<V>>)"""
        return MultiValueMap._wrap(_MultiValueMap.multiValueMap(arg0))

    @overload
    def iterator(self, arg0: object) -> 'Iterator':
        """public java.util.Iterator<V> org.apache.commons.collections4.map.MultiValueMap.iterator(java.lang.Object)"""
        return 'Iterator'._wrap(super(_MultiValueMap, self).iterator(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.MultiValueMap()"""
        val = _MultiValueMap()
        self.__wrapper = val

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, java.lang.Object>> org.apache.commons.collections4.map.MultiValueMap.entrySet()"""
        return 'Set'._wrap(super(MultiValueMap, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.MultiValueMap.putAll(java.util.Map<? extends K, ?>)"""
        super(_MultiValueMap, self).putAll(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.MultiValueMap.iterator()"""
        return 'Iterator'._wrap(super(MultiValueMap, self).iterator())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def containsValue(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiValueMap.containsValue(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiValueMap, self).containsValue(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.MultiValueMap.clear()"""
        super(MultiValueMap, self).clear()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.MultiValueMap()"""
        val = _MultiValueMap()
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiValueMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_MultiValueMap, self).containsValue(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiValueMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiValueMap, self).removeMapping(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map', arg1: 'Factory') -> 'MultiValueMap':
        """public static <K,V,C extends java.util.Collection<V>> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.map.MultiValueMap.multiValueMap(java.util.Map<K, ? super C>,org.apache.commons.collections4.Factory<C>)"""
        return MultiValueMap._wrap(_MultiValueMap.multiValueMap(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<java.lang.Object> org.apache.commons.collections4.map.MultiValueMap.values()"""
        return 'Collection'._wrap(super(MultiValueMap, self).values())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

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

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def totalSize(self) -> int:
        """public int org.apache.commons.collections4.map.MultiValueMap.totalSize()"""
        return int._wrap(super(MultiValueMap, self).totalSize())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def getCollection(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.MultiValueMap.getCollection(java.lang.Object)"""
        return 'Collection'._wrap(super(_MultiValueMap, self).getCollection(arg0))

    @overload
    def size(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.map.MultiValueMap.size(java.lang.Object)"""
        return int._wrap(super(_MultiValueMap, self).size(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$HashEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashEntry
_HashEntry = _AbstractHashedMap_HashEntry.HashEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashEntry():
    """org.apache.commons.collections4.map.AbstractHashedMap.HashEntry"""
 
    @staticmethod
    def _wrap(java_value: _HashEntry) -> 'HashEntry':
        return HashEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashEntry):
        """
        Dynamic initializer for HashEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashEntry__wrapper":
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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.getKey()"""
        return object._wrap(super(HashEntry, self).getKey())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.setValue(V)"""
        return object._wrap(super(_HashEntry, self).setValue(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.getValue()"""
        return object._wrap(super(HashEntry, self).getValue())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_HashEntry, self).equals(arg0))

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
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.toString()"""
        return str._wrap(super(HashEntry, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.hashCode()"""
        return int._wrap(super(HashEntry, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractHashedMap():
    """org.apache.commons.collections4.map.AbstractHashedMap"""
 
    @staticmethod
    def _wrap(java_value: _AbstractHashedMap) -> 'AbstractHashedMap':
        return AbstractHashedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractHashedMap):
        """
        Dynamic initializer for AbstractHashedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractHashedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractHashedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool._wrap(super(AbstractHashedMap, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int._wrap(super(AbstractHashedMap, self).size())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'._wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractHashedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractHashedMap, self).mapIterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.clear()"""
        super(AbstractHashedMap, self).clear()

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).get(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object._wrap(super(_AbstractHashedMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableOrderedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
from builtins import bool
from builtins import str
import org.apache.commons.collections4.map.AbstractOrderedMapDecorator as _AbstractOrderedMapDecorator
_AbstractOrderedMapDecorator = _AbstractOrderedMapDecorator
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
import org.apache.commons.collections4.map.UnmodifiableOrderedMap as _UnmodifiableOrderedMap
_UnmodifiableOrderedMap = _UnmodifiableOrderedMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableOrderedMap():
    """org.apache.commons.collections4.map.UnmodifiableOrderedMap"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableOrderedMap) -> 'UnmodifiableOrderedMap':
        return UnmodifiableOrderedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableOrderedMap):
        """
        Dynamic initializer for UnmodifiableOrderedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableOrderedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableOrderedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.firstKey()"""
        return object._wrap(super(AbstractOrderedMapDecorator, self).firstKey())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableOrderedMap.clear()"""
        super(UnmodifiableOrderedMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractOrderedMapDecorator, self).previousKey(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractOrderedMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def unmodifiableOrderedMap(arg0: 'OrderedMap') -> 'collections4.OrderedMap':
        """public static <K,V> org.apache.commons.collections4.OrderedMap<K, V> org.apache.commons.collections4.map.UnmodifiableOrderedMap.unmodifiableOrderedMap(org.apache.commons.collections4.OrderedMap<? extends K, ? extends V>)"""
        return collections4.OrderedMap._wrap(_UnmodifiableOrderedMap.unmodifiableOrderedMap(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.UnmodifiableOrderedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(UnmodifiableOrderedMap, self).mapIterator())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableOrderedMap.put(K,V)"""
        return object._wrap(super(_UnmodifiableOrderedMap, self).put(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableOrderedMap.remove(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableOrderedMap, self).remove(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

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

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.UnmodifiableOrderedMap.values()"""
        return 'Collection'._wrap(super(UnmodifiableOrderedMap, self).values())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.lastKey()"""
        return object._wrap(super(AbstractOrderedMapDecorator, self).lastKey())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.UnmodifiableOrderedMap.keySet()"""
        return 'Set'._wrap(super(UnmodifiableOrderedMap, self).keySet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.UnmodifiableOrderedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_UnmodifiableOrderedMap, self).putAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableOrderedMap.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableOrderedMap, self).entrySet())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.map.UnmodifiableMap as _UnmodifiableMap
_UnmodifiableMap = _UnmodifiableMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableMap():
    """org.apache.commons.collections4.map.UnmodifiableMap"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableMap) -> 'UnmodifiableMap':
        return UnmodifiableMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableMap):
        """
        Dynamic initializer for UnmodifiableMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableMap.put(K,V)"""
        return object._wrap(super(_UnmodifiableMap, self).put(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableMap.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableMap, self).entrySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.UnmodifiableMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_UnmodifiableMap, self).putAll(arg0)

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.UnmodifiableMap.values()"""
        return 'Collection'._wrap(super(UnmodifiableMap, self).values())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.UnmodifiableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(UnmodifiableMap, self).mapIterator())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableMap(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.map.UnmodifiableMap.unmodifiableMap(java.util.Map<? extends K, ? extends V>)"""
        return Map._wrap(_UnmodifiableMap.unmodifiableMap(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.UnmodifiableMap.keySet()"""
        return 'Set'._wrap(super(UnmodifiableMap, self).keySet())

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

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableMap.remove(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableMap, self).remove(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableMap.clear()"""
        super(UnmodifiableMap, self).clear()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength
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
import org.apache.commons.collections4.map.AbstractReferenceMap as _AbstractReferenceMap_ReferenceStrength
_ReferenceStrength = _AbstractReferenceMap_ReferenceStrength.ReferenceStrength
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReferenceStrength():
    """org.apache.commons.collections4.map.AbstractReferenceMap.ReferenceStrength"""
 
    @staticmethod
    def _wrap(java_value: _ReferenceStrength) -> 'ReferenceStrength':
        return ReferenceStrength(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReferenceStrength):
        """
        Dynamic initializer for ReferenceStrength.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReferenceStrength__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReferenceStrength__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['ReferenceStrength']:
        """public static org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength[] org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength.values()"""
        return List[ReferenceStrength]._wrap(_ReferenceStrength.values())

    @staticmethod
    @overload
    def resolve(arg0: int) -> 'ReferenceStrength':
        """public static org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength.resolve(int)"""
        return ReferenceStrength._wrap(_ReferenceStrength.resolve(_int.valueOf(arg0)))

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
    def valueOf(arg0: str) -> 'ReferenceStrength':
        """public static org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength.valueOf(java.lang.String)"""
        return ReferenceStrength._wrap(_ReferenceStrength.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractReferenceMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.map.AbstractReferenceMap as _AbstractReferenceMap
_AbstractReferenceMap = _AbstractReferenceMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractReferenceMap():
    """org.apache.commons.collections4.map.AbstractReferenceMap"""
 
    @staticmethod
    def _wrap(java_value: _AbstractReferenceMap) -> 'AbstractReferenceMap':
        return AbstractReferenceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractReferenceMap):
        """
        Dynamic initializer for AbstractReferenceMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractReferenceMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractReferenceMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractReferenceMap.entrySet()"""
        return 'Set'._wrap(super(AbstractReferenceMap, self).entrySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractReferenceMap, self).remove(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractReferenceMap.size()"""
        return int._wrap(super(AbstractReferenceMap, self).size())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.isEmpty()"""
        return bool._wrap(super(AbstractReferenceMap, self).isEmpty())

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
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractReferenceMap.keySet()"""
        return 'Set'._wrap(super(AbstractReferenceMap, self).keySet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractReferenceMap, self).get(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractReferenceMap, self).containsValue(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractReferenceMap, self).containsKey(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractReferenceMap.values()"""
        return 'Collection'._wrap(super(AbstractReferenceMap, self).values())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractReferenceMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractReferenceMap, self).mapIterator())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.put(K,V)"""
        return object._wrap(super(_AbstractReferenceMap, self).put(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractReferenceMap.clear()"""
        super(AbstractReferenceMap, self).clear()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.ReferenceMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.lang.Boolean as _boolean
import org.apache.commons.collections4.map.ReferenceMap as _ReferenceMap
_ReferenceMap = _ReferenceMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Float as _float
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.map.AbstractReferenceMap as _AbstractReferenceMap
_AbstractReferenceMap = _AbstractReferenceMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReferenceMap():
    """org.apache.commons.collections4.map.ReferenceMap"""
 
    @staticmethod
    def _wrap(java_value: _ReferenceMap) -> 'ReferenceMap':
        return ReferenceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReferenceMap):
        """
        Dynamic initializer for ReferenceMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReferenceMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReferenceMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractReferenceMap.entrySet()"""
        return 'Set'._wrap(super(AbstractReferenceMap, self).entrySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractReferenceMap, self).remove(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractReferenceMap.size()"""
        return int._wrap(super(AbstractReferenceMap, self).size())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.isEmpty()"""
        return bool._wrap(super(AbstractReferenceMap, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength'):
        """public org.apache.commons.collections4.map.ReferenceMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength)"""
        val = _ReferenceMap(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractReferenceMap.keySet()"""
        return 'Set'._wrap(super(AbstractReferenceMap, self).keySet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractReferenceMap, self).get(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.ReferenceMap()"""
        val = _ReferenceMap()
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractReferenceMap, self).containsValue(arg0))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: int, arg3: float, arg4: bool):
        """public org.apache.commons.collections4.map.ReferenceMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,int,float,boolean)"""
        val = _ReferenceMap(arg0, arg1, _int.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: bool):
        """public org.apache.commons.collections4.map.ReferenceMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,boolean)"""
        val = _ReferenceMap(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractReferenceMap, self).containsKey(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractReferenceMap.values()"""
        return 'Collection'._wrap(super(AbstractReferenceMap, self).values())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractReferenceMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractReferenceMap, self).mapIterator())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.put(K,V)"""
        return object._wrap(super(_AbstractReferenceMap, self).put(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: int, arg3: float):
        """public org.apache.commons.collections4.map.ReferenceMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,int,float)"""
        val = _ReferenceMap(arg0, arg1, _int.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractReferenceMap.clear()"""
        super(AbstractReferenceMap, self).clear()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.ReferenceMap()"""
        val = _ReferenceMap()
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$EntrySetIterator
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashIterator
_HashIterator = _AbstractHashedMap_HashIterator.HashIterator
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_EntrySetIterator
_EntrySetIterator = _AbstractHashedMap_EntrySetIterator.EntrySetIterator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntrySetIterator():
    """org.apache.commons.collections4.map.AbstractHashedMap.EntrySetIterator"""
 
    @staticmethod
    def _wrap(java_value: _EntrySetIterator) -> 'EntrySetIterator':
        return EntrySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntrySetIterator):
        """
        Dynamic initializer for EntrySetIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntrySetIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntrySetIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str._wrap(super(HashIterator, self).toString())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.map.AbstractHashedMap$EntrySetIterator.next()"""
        return 'Entry.Map$Entry'._wrap(super(EntrySetIterator, self).next())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool._wrap(super(HashIterator, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractSortedMapDecorator
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
import java.util.Set as _Set
_Set = _Set
import java.util.SequencedCollection as SequencedCollection
import java.util.Map.Entry as Entry
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import java.util.SortedMap as SortedMap
import java.util.SequencedSet as SequencedSet
from builtins import bool
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from builtins import str
from pyquantum_helper import override
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as _AbstractSortedMapDecorator
_AbstractSortedMapDecorator = _AbstractSortedMapDecorator
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractSortedMapDecorator():
    """org.apache.commons.collections4.map.AbstractSortedMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractSortedMapDecorator) -> 'AbstractSortedMapDecorator':
        return AbstractSortedMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractSortedMapDecorator):
        """
        Dynamic initializer for AbstractSortedMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractSortedMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractSortedMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractSortedMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractSortedMapDecorator, self).mapIterator())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.firstKey()"""
        return object._wrap(super(AbstractSortedMapDecorator, self).firstKey())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMapDecorator, self).putAll(arg0)

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.lastKey()"""
        return object._wrap(super(AbstractSortedMapDecorator, self).lastKey())

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractSortedMapDecorator, self).nextKey(arg0))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_AbstractSortedMapDecorator, self).subMap(arg0, arg1))

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def __init__(self, arg0: 'SortedMap'):
        """public org.apache.commons.collections4.map.AbstractSortedMapDecorator(java.util.SortedMap<K, V>)"""
        val = _AbstractSortedMapDecorator(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.tailMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractSortedMapDecorator, self).tailMap(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.headMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractSortedMapDecorator, self).headMap(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.AbstractSortedMapDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedMapDecorator, self).comparator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$ValuesIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_ValuesIterator
_ValuesIterator = _AbstractLinkedMap_ValuesIterator.ValuesIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_LinkIterator
_LinkIterator = _AbstractLinkedMap_LinkIterator.LinkIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValuesIterator():
    """org.apache.commons.collections4.map.AbstractLinkedMap.ValuesIterator"""
 
    @staticmethod
    def _wrap(java_value: _ValuesIterator) -> 'ValuesIterator':
        return ValuesIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValuesIterator):
        """
        Dynamic initializer for ValuesIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValuesIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValuesIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool._wrap(super(LinkIterator, self).hasNext())

    @override
    @overload
    def previous(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractLinkedMap$ValuesIterator.previous()"""
        return object._wrap(super(ValuesIterator, self).previous())

    @override
    @overload
    def next(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractLinkedMap$ValuesIterator.next()"""
        return object._wrap(super(ValuesIterator, self).next())

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
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str._wrap(super(LinkIterator, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool._wrap(super(LinkIterator, self).hasPrevious())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$KeySetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_KeySetIterator
_KeySetIterator = _AbstractLinkedMap_KeySetIterator.KeySetIterator
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_LinkIterator
_LinkIterator = _AbstractLinkedMap_LinkIterator.LinkIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeySetIterator():
    """org.apache.commons.collections4.map.AbstractLinkedMap.KeySetIterator"""
 
    @staticmethod
    def _wrap(java_value: _KeySetIterator) -> 'KeySetIterator':
        return KeySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeySetIterator):
        """
        Dynamic initializer for KeySetIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeySetIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeySetIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool._wrap(super(LinkIterator, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$KeySetIterator.previous()"""
        return object._wrap(super(KeySetIterator, self).previous())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$KeySetIterator.next()"""
        return object._wrap(super(KeySetIterator, self).next())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str._wrap(super(LinkIterator, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool._wrap(super(LinkIterator, self).hasPrevious())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.HashedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap
_AbstractHashedMap = _AbstractHashedMap
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Float as _float
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
import org.apache.commons.collections4.map.HashedMap as _HashedMap
_HashedMap = _HashedMap
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashedMap():
    """org.apache.commons.collections4.map.HashedMap"""
 
    @staticmethod
    def _wrap(java_value: _HashedMap) -> 'HashedMap':
        return HashedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashedMap):
        """
        Dynamic initializer for HashedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool._wrap(super(AbstractHashedMap, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int._wrap(super(AbstractHashedMap, self).size())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'._wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractHashedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractHashedMap, self).mapIterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str._wrap(super(AbstractHashedMap, self).toString())

    @overload
    def clone(self) -> 'HashedMap':
        """public org.apache.commons.collections4.map.HashedMap<K, V> org.apache.commons.collections4.map.HashedMap.clone()"""
        return 'HashedMap'._wrap(super(HashedMap, self).clone())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.HashedMap()"""
        val = _HashedMap()
        self.__wrapper = val

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.HashedMap(int)"""
        val = _HashedMap(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int._wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public org.apache.commons.collections4.map.HashedMap(int,float)"""
        val = _HashedMap(_int.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractHashedMap, self).equals(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.HashedMap(java.util.Map<? extends K, ? extends V>)"""
        val = _HashedMap(arg0)
        self.__wrapper = val

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.clear()"""
        super(AbstractHashedMap, self).clear()

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractHashedMap, self).get(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'._wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object._wrap(super(_AbstractHashedMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.HashedMap()"""
        val = _HashedMap()
        self.__wrapper = val

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractHashedMap, self).putAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractIterableMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.Get as _Get
_Get = _Get
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.Put as _Put
_Put = _Put
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractIterableMap():
    """org.apache.commons.collections4.map.AbstractIterableMap"""
 
    @staticmethod
    def _wrap(java_value: _AbstractIterableMap) -> 'AbstractIterableMap':
        return AbstractIterableMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractIterableMap):
        """
        Dynamic initializer for AbstractIterableMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractIterableMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractIterableMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

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

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.AbstractIterableMap()"""
        val = _AbstractIterableMap()
        self.__wrapper = val

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.AbstractIterableMap()"""
        val = _AbstractIterableMap()
        self.__wrapper = val

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.MultiKeyMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.util.Set as _Set
_Set = _Set
try:
    from pyapache.collections4 import keyvalue
except ImportError:
    keyvalue = _import_once("pyapache.collections4.keyvalue")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
import org.apache.commons.collections4.map.MultiKeyMap as _MultiKeyMap
_MultiKeyMap = _MultiKeyMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiKeyMap():
    """org.apache.commons.collections4.map.MultiKeyMap"""
 
    @staticmethod
    def _wrap(java_value: _MultiKeyMap) -> 'MultiKeyMap':
        return MultiKeyMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiKeyMap):
        """
        Dynamic initializer for MultiKeyMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiKeyMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiKeyMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.get(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_MultiKeyMap, self).get(arg0, arg1, arg2, arg3, arg4))

    @overload
    def removeAll(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.removeAll(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiKeyMap, self).removeAll(arg0, arg1))

    @overload
    def containsKey(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.containsKey(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiKeyMap, self).containsKey(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<org.apache.commons.collections4.keyvalue.MultiKey<? extends K>, V> org.apache.commons.collections4.map.MultiKeyMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(MultiKeyMap, self).mapIterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(K,K,K,K,V)"""
        return object._wrap(super(_MultiKeyMap, self).put(arg0, arg1, arg2, arg3, arg4))

    @overload
    def removeMultiKey(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.removeMultiKey(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_MultiKeyMap, self).removeMultiKey(arg0, arg1, arg2))

    @overload
    def containsKey(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.containsKey(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiKeyMap, self).containsKey(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

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
    def put(self, arg0: 'MultiKey', arg1: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(org.apache.commons.collections4.keyvalue.MultiKey<? extends K>,V)"""
        return object._wrap(super(_MultiKeyMap, self).put(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.MultiKeyMap.putAll(java.util.Map<? extends org.apache.commons.collections4.keyvalue.MultiKey<? extends K>, ? extends V>)"""
        super(_MultiKeyMap, self).putAll(arg0)

    @overload
    def removeMultiKey(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.removeMultiKey(java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_MultiKeyMap, self).removeMultiKey(arg0, arg1))

    @overload
    def get(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.get(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_MultiKeyMap, self).get(arg0, arg1, arg2))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(K,K,V)"""
        return object._wrap(super(_MultiKeyMap, self).put(arg0, arg1, arg2))

    @overload
    def removeAll(self, arg0: object, arg1: object, arg2: object, arg3: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.removeAll(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiKeyMap, self).removeAll(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(K,K,K,K,K,V)"""
        return object._wrap(super(_MultiKeyMap, self).put(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def containsKey(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.containsKey(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiKeyMap, self).containsKey(arg0, arg1, arg2, arg3, arg4))

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.get(java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_MultiKeyMap, self).get(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.MultiKeyMap()"""
        val = _MultiKeyMap()
        self.__wrapper = val

    @overload
    def containsKey(self, arg0: object, arg1: object, arg2: object, arg3: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.containsKey(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiKeyMap, self).containsKey(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.MultiKeyMap()"""
        val = _MultiKeyMap()
        self.__wrapper = val

    @overload
    def removeAll(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.removeAll(java.lang.Object)"""
        return bool._wrap(super(_MultiKeyMap, self).removeAll(arg0))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object, arg3: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(K,K,K,V)"""
        return object._wrap(super(_MultiKeyMap, self).put(arg0, arg1, arg2, arg3))

    @overload
    def removeMultiKey(self, arg0: object, arg1: object, arg2: object, arg3: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.removeMultiKey(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_MultiKeyMap, self).removeMultiKey(arg0, arg1, arg2, arg3))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def multiKeyMap(arg0: 'AbstractHashedMap') -> 'MultiKeyMap':
        """public static <K,V> org.apache.commons.collections4.map.MultiKeyMap<K, V> org.apache.commons.collections4.map.MultiKeyMap.multiKeyMap(org.apache.commons.collections4.map.AbstractHashedMap<org.apache.commons.collections4.keyvalue.MultiKey<? extends K>, V>)"""
        return MultiKeyMap._wrap(_MultiKeyMap.multiKeyMap(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def get(self, arg0: object, arg1: object, arg2: object, arg3: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.get(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_MultiKeyMap, self).get(arg0, arg1, arg2, arg3))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def removeMultiKey(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.removeMultiKey(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_MultiKeyMap, self).removeMultiKey(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def removeAll(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.removeAll(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_MultiKeyMap, self).removeAll(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def clone(self) -> 'MultiKeyMap':
        """public org.apache.commons.collections4.map.MultiKeyMap<K, V> org.apache.commons.collections4.map.MultiKeyMap.clone()"""
        return 'MultiKeyMap'._wrap(super(MultiKeyMap, self).clone()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$ValuesIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashIterator
_HashIterator = _AbstractHashedMap_HashIterator.HashIterator
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_ValuesIterator
_ValuesIterator = _AbstractHashedMap_ValuesIterator.ValuesIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValuesIterator():
    """org.apache.commons.collections4.map.AbstractHashedMap.ValuesIterator"""
 
    @staticmethod
    def _wrap(java_value: _ValuesIterator) -> 'ValuesIterator':
        return ValuesIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValuesIterator):
        """
        Dynamic initializer for ValuesIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValuesIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValuesIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def next(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$ValuesIterator.next()"""
        return object._wrap(super(ValuesIterator, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str._wrap(super(HashIterator, self).toString())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool._wrap(super(HashIterator, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.PassiveExpiringMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.map.PassiveExpiringMap as _PassiveExpiringMap
_PassiveExpiringMap = _PassiveExpiringMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PassiveExpiringMap():
    """org.apache.commons.collections4.map.PassiveExpiringMap"""
 
    @staticmethod
    def _wrap(java_value: _PassiveExpiringMap) -> 'PassiveExpiringMap':
        return PassiveExpiringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PassiveExpiringMap):
        """
        Dynamic initializer for PassiveExpiringMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PassiveExpiringMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PassiveExpiringMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.PassiveExpiringMap.keySet()"""
        return 'Set'._wrap(super(PassiveExpiringMap, self).keySet())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.PassiveExpiringMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_PassiveExpiringMap, self).putAll(arg0)

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.PassiveExpiringMap.put(K,V)"""
        return object._wrap(super(_PassiveExpiringMap, self).put(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.PassiveExpiringMap()"""
        val = _PassiveExpiringMap()
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.PassiveExpiringMap.size()"""
        return int._wrap(super(PassiveExpiringMap, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.PassiveExpiringMap.entrySet()"""
        return 'Set'._wrap(super(PassiveExpiringMap, self).entrySet())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(long)"""
        val = _PassiveExpiringMap(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def __init__(self, arg0: 'ExpirationPolicy', arg1: 'Map'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(org.apache.commons.collections4.map.PassiveExpiringMap$ExpirationPolicy<K, V>,java.util.Map<K, V>)"""
        val = _PassiveExpiringMap(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'TimeUnit', arg2: 'Map'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(long,java.util.concurrent.TimeUnit,java.util.Map<K, V>)"""
        val = _PassiveExpiringMap(_long.valueOf(arg0), arg1, arg2)
        self.__wrapper = val

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.PassiveExpiringMap.isEmpty()"""
        return bool._wrap(super(PassiveExpiringMap, self).isEmpty())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.PassiveExpiringMap.values()"""
        return 'Collection'._wrap(super(PassiveExpiringMap, self).values())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

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
    def __init__(self, arg0: int, arg1: 'TimeUnit'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(long,java.util.concurrent.TimeUnit)"""
        val = _PassiveExpiringMap(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.PassiveExpiringMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_PassiveExpiringMap, self).containsKey(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.PassiveExpiringMap.clear()"""
        super(PassiveExpiringMap, self).clear()

    @overload
    def __init__(self, arg0: 'ExpirationPolicy'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(org.apache.commons.collections4.map.PassiveExpiringMap$ExpirationPolicy<K, V>)"""
        val = _PassiveExpiringMap(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'Map'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(long,java.util.Map<K, V>)"""
        val = _PassiveExpiringMap(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.PassiveExpiringMap.get(java.lang.Object)"""
        return object._wrap(super(_PassiveExpiringMap, self).get(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.PassiveExpiringMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_PassiveExpiringMap, self).containsValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.PassiveExpiringMap()"""
        val = _PassiveExpiringMap()
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.PassiveExpiringMap.remove(java.lang.Object)"""
        return object._wrap(super(_PassiveExpiringMap, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(java.util.Map<K, V>)"""
        val = _PassiveExpiringMap(arg0)
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableSortedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
import java.util.Set as _Set
_Set = _Set
import java.util.SequencedCollection as SequencedCollection
import org.apache.commons.collections4.map.UnmodifiableSortedMap as _UnmodifiableSortedMap
_UnmodifiableSortedMap = _UnmodifiableSortedMap
import java.util.Map.Entry as Entry
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import java.util.SortedMap as SortedMap
import java.util.SequencedSet as SequencedSet
from builtins import bool
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from builtins import str
from pyquantum_helper import override
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as _AbstractSortedMapDecorator
_AbstractSortedMapDecorator = _AbstractSortedMapDecorator
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableSortedMap():
    """org.apache.commons.collections4.map.UnmodifiableSortedMap"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableSortedMap) -> 'UnmodifiableSortedMap':
        return UnmodifiableSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableSortedMap):
        """
        Dynamic initializer for UnmodifiableSortedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableSortedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableSortedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableSortedMap.clear()"""
        super(UnmodifiableSortedMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractSortedMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.UnmodifiableSortedMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableSortedMap, self).subMap(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractSortedMapDecorator, self).mapIterator())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.UnmodifiableSortedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_UnmodifiableSortedMap, self).putAll(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractSortedMapDecorator, self).nextKey(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.UnmodifiableSortedMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableSortedMap, self).tailMap(arg0))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.UnmodifiableSortedMap.lastKey()"""
        return object._wrap(super(UnmodifiableSortedMap, self).lastKey())

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableSortedMap(arg0: 'SortedMap') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.map.UnmodifiableSortedMap.unmodifiableSortedMap(java.util.SortedMap<K, ? extends V>)"""
        return SortedMap._wrap(_UnmodifiableSortedMap.unmodifiableSortedMap(arg0))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.UnmodifiableSortedMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableSortedMap, self).headMap(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableSortedMap.put(K,V)"""
        return object._wrap(super(_UnmodifiableSortedMap, self).put(arg0, arg1))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableSortedMap.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableSortedMap, self).entrySet())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.UnmodifiableSortedMap.keySet()"""
        return 'Set'._wrap(super(UnmodifiableSortedMap, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableSortedMap.remove(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableSortedMap, self).remove(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.UnmodifiableSortedMap.values()"""
        return 'Collection'._wrap(super(UnmodifiableSortedMap, self).values())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.UnmodifiableSortedMap.comparator()"""
        return 'Comparator'._wrap(super(UnmodifiableSortedMap, self).comparator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.UnmodifiableSortedMap.firstKey()"""
        return object._wrap(super(UnmodifiableSortedMap, self).firstKey())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.PredicatedSortedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import java.util.SequencedCollection as SequencedCollection
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
import java.util.Map.Entry as Entry
import org.apache.commons.collections4.map.PredicatedSortedMap as _PredicatedSortedMap
_PredicatedSortedMap = _PredicatedSortedMap
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import java.util.SortedMap as SortedMap
import java.util.SequencedSet as SequencedSet
from builtins import bool
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.PredicatedMap as _PredicatedMap
_PredicatedMap = _PredicatedMap
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedSortedMap():
    """org.apache.commons.collections4.map.PredicatedSortedMap"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedSortedMap) -> 'PredicatedSortedMap':
        return PredicatedSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedSortedMap):
        """
        Dynamic initializer for PredicatedSortedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedSortedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedSortedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def predicatedSortedMap(arg0: 'SortedMap', arg1: 'Predicate', arg2: 'Predicate') -> 'PredicatedSortedMap':
        """public static <K,V> org.apache.commons.collections4.map.PredicatedSortedMap<K, V> org.apache.commons.collections4.map.PredicatedSortedMap.predicatedSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return PredicatedSortedMap._wrap(_PredicatedSortedMap.predicatedSortedMap(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.PredicatedSortedMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_PredicatedSortedMap, self).subMap(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.PredicatedSortedMap.comparator()"""
        return 'Comparator'._wrap(super(PredicatedSortedMap, self).comparator())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.PredicatedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_PredicatedMap, self).putAll(arg0)

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.PredicatedMap.put(K,V)"""
        return object._wrap(super(_PredicatedMap, self).put(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.PredicatedSortedMap.firstKey()"""
        return object._wrap(super(PredicatedSortedMap, self).firstKey())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.PredicatedSortedMap.lastKey()"""
        return object._wrap(super(PredicatedSortedMap, self).lastKey())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.PredicatedSortedMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_PredicatedSortedMap, self).tailMap(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @staticmethod
    @overload
    def predicatedMap(arg0: 'Map', arg1: 'Predicate', arg2: 'Predicate') -> 'PredicatedMap':
        """public static <K,V> org.apache.commons.collections4.map.PredicatedMap<K, V> org.apache.commons.collections4.map.PredicatedMap.predicatedMap(java.util.Map<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return PredicatedMap._wrap(_PredicatedMap.predicatedMap(arg0, arg1, arg2))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.PredicatedSortedMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_PredicatedSortedMap, self).headMap(arg0))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.collections4.map.AbstractReferenceMap as _AbstractReferenceMap_ReferenceEntry
_ReferenceEntry = _AbstractReferenceMap_ReferenceEntry.ReferenceEntry
from builtins import bool
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashEntry
_HashEntry = _AbstractHashedMap_HashEntry.HashEntry
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReferenceEntry():
    """org.apache.commons.collections4.map.AbstractReferenceMap.ReferenceEntry"""
 
    @staticmethod
    def _wrap(java_value: _ReferenceEntry) -> 'ReferenceEntry':
        return ReferenceEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReferenceEntry):
        """
        Dynamic initializer for ReferenceEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReferenceEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReferenceEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.getKey()"""
        return object._wrap(super(ReferenceEntry, self).getKey())

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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.getValue()"""
        return object._wrap(super(ReferenceEntry, self).getValue())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.hashCode()"""
        return int._wrap(super(ReferenceEntry, self).hashCode())

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
    def __init__(self, arg0: 'AbstractReferenceMap', arg1: 'HashEntry', arg2: int, arg3: object, arg4: object):
        """public org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry(org.apache.commons.collections4.map.AbstractReferenceMap<K, V>,org.apache.commons.collections4.map.AbstractHashedMap$HashEntry<K, V>,int,K,V)"""
        val = _ReferenceEntry(arg0, arg1, _int.valueOf(arg2), arg3, arg4)
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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.setValue(V)"""
        return object._wrap(super(_ReferenceEntry, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.toString()"""
        return str._wrap(super(HashEntry, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_ReferenceEntry, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.LazyMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.map.LazyMap as _LazyMap
_LazyMap = _LazyMap
import org.apache.commons.collections4.map.AbstractIterableMap as _AbstractIterableMap
_AbstractIterableMap = _AbstractIterableMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LazyMap():
    """org.apache.commons.collections4.map.LazyMap"""
 
    @staticmethod
    def _wrap(java_value: _LazyMap) -> 'LazyMap':
        return LazyMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LazyMap):
        """
        Dynamic initializer for LazyMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LazyMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LazyMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Transformer') -> 'LazyMap':
        """public static <V,K> org.apache.commons.collections4.map.LazyMap<K, V> org.apache.commons.collections4.map.LazyMap.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return LazyMap._wrap(_LazyMap.lazyMap(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMapDecorator, self).values())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMapDecorator, self).putAll(arg0)

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.LazyMap.get(java.lang.Object)"""
        return object._wrap(super(_LazyMap, self).get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Factory') -> 'LazyMap':
        """public static <K,V> org.apache.commons.collections4.map.LazyMap<K, V> org.apache.commons.collections4.map.LazyMap.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return LazyMap._wrap(_LazyMap.lazyMap(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.FixedSizeSortedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
import java.util.Set as _Set
_Set = _Set
import java.util.SequencedCollection as SequencedCollection
import java.util.Map.Entry as Entry
import java.util.SortedMap as _SortedMap
_SortedMap = _SortedMap
import java.util.SortedMap as SortedMap
import java.util.SequencedSet as SequencedSet
from builtins import bool
import java.util.SequencedMap as _SequencedMap
_SequencedMap = _SequencedMap
from builtins import str
import org.apache.commons.collections4.map.FixedSizeSortedMap as _FixedSizeSortedMap
_FixedSizeSortedMap = _FixedSizeSortedMap
from pyquantum_helper import override
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as _AbstractSortedMapDecorator
_AbstractSortedMapDecorator = _AbstractSortedMapDecorator
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FixedSizeSortedMap():
    """org.apache.commons.collections4.map.FixedSizeSortedMap"""
 
    @staticmethod
    def _wrap(java_value: _FixedSizeSortedMap) -> 'FixedSizeSortedMap':
        return FixedSizeSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FixedSizeSortedMap):
        """
        Dynamic initializer for FixedSizeSortedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FixedSizeSortedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FixedSizeSortedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def fixedSizeSortedMap(arg0: 'SortedMap') -> 'FixedSizeSortedMap':
        """public static <K,V> org.apache.commons.collections4.map.FixedSizeSortedMap<K, V> org.apache.commons.collections4.map.FixedSizeSortedMap.fixedSizeSortedMap(java.util.SortedMap<K, V>)"""
        return FixedSizeSortedMap._wrap(_FixedSizeSortedMap.fixedSizeSortedMap(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.FixedSizeSortedMap.entrySet()"""
        return 'Set'._wrap(super(FixedSizeSortedMap, self).entrySet())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.FixedSizeSortedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_FixedSizeSortedMap, self).putAll(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractSortedMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.FixedSizeSortedMap.isFull()"""
        return bool._wrap(super(FixedSizeSortedMap, self).isFull())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractSortedMapDecorator, self).mapIterator())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.firstKey()"""
        return object._wrap(super(AbstractSortedMapDecorator, self).firstKey())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.FixedSizeSortedMap.clear()"""
        super(FixedSizeSortedMap, self).clear()

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.FixedSizeSortedMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_FixedSizeSortedMap, self).tailMap(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.lastKey()"""
        return object._wrap(super(AbstractSortedMapDecorator, self).lastKey())

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.FixedSizeSortedMap.maxSize()"""
        return int._wrap(super(FixedSizeSortedMap, self).maxSize())

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractSortedMapDecorator, self).nextKey(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.FixedSizeSortedMap.remove(java.lang.Object)"""
        return object._wrap(super(_FixedSizeSortedMap, self).remove(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.FixedSizeSortedMap.put(K,V)"""
        return object._wrap(super(_FixedSizeSortedMap, self).put(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.FixedSizeSortedMap.values()"""
        return 'Collection'._wrap(super(FixedSizeSortedMap, self).values())

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'._wrap(super(SortedMap, self).reversed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMapDecorator, self).get(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.FixedSizeSortedMap.keySet()"""
        return 'Set'._wrap(super(FixedSizeSortedMap, self).keySet())

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.FixedSizeSortedMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_FixedSizeSortedMap, self).headMap(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsKey(arg0))

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
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.FixedSizeSortedMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_FixedSizeSortedMap, self).subMap(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.AbstractSortedMapDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedMapDecorator, self).comparator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$LinkEntry
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.map.AbstractLinkedMap as _AbstractLinkedMap_LinkEntry
_LinkEntry = _AbstractLinkedMap_LinkEntry.LinkEntry
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
from builtins import bool
import org.apache.commons.collections4.map.AbstractHashedMap as _AbstractHashedMap_HashEntry
_HashEntry = _AbstractHashedMap_HashEntry.HashEntry
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinkEntry():
    """org.apache.commons.collections4.map.AbstractLinkedMap.LinkEntry"""
 
    @staticmethod
    def _wrap(java_value: _LinkEntry) -> 'LinkEntry':
        return LinkEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinkEntry):
        """
        Dynamic initializer for LinkEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinkEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinkEntry__wrapper":
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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.getKey()"""
        return object._wrap(super(HashEntry, self).getKey())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.setValue(V)"""
        return object._wrap(super(_HashEntry, self).setValue(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.getValue()"""
        return object._wrap(super(HashEntry, self).getValue())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_HashEntry, self).equals(arg0))

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
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.toString()"""
        return str._wrap(super(HashEntry, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.hashCode()"""
        return int._wrap(super(HashEntry, self).hashCode())