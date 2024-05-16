from __future__ import annotations
from overload import overload


 
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
import org.apache.commons.collections4.bidimap.DualTreeBidiMap as _DualTreeBidiMap_ViewMap
_ViewMap = _DualTreeBidiMap_ViewMap.ViewMap
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
 
class ViewMap():
    """org.apache.commons.collections4.bidimap.DualTreeBidiMap.ViewMap"""
 
    @staticmethod
    def _wrap(java_value: _ViewMap) -> 'ViewMap':
        return ViewMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ViewMap):
        """
        Dynamic initializer for ViewMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ViewMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ViewMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_ViewMap, self).tailMap(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).equals(arg0))

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
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).get(arg0))

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
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_map.AbstractMapDecorator, self).putAll(arg0)

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

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.clear()"""
        super(ViewMap, self).clear()

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.previousKey(K)"""
        return object._wrap(super(_ViewMap, self).previousKey(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.AbstractSortedMapDecorator.comparator()"""
        return 'Comparator'._wrap(super(map.AbstractSortedMapDecorator, self).comparator())

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).keySet())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.firstKey()"""
        return object._wrap(super(map.AbstractSortedMapDecorator, self).firstKey())

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
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_ViewMap, self).containsValue(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(map.AbstractMapDecorator, self).size())

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
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_ViewMap, self).headMap(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.lastKey()"""
        return object._wrap(super(map.AbstractSortedMapDecorator, self).lastKey())

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
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_ViewMap, self).subMap(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(map.AbstractMapDecorator, self).values())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(map.AbstractSortedMapDecorator, self).mapIterator())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.nextKey(K)"""
        return object._wrap(super(_ViewMap, self).nextKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

 
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap
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
import org.apache.commons.collections4.bidimap.DualTreeBidiMap as _DualTreeBidiMap_ViewMap
_ViewMap = _DualTreeBidiMap_ViewMap.ViewMap
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
 
class ViewMap():
    """org.apache.commons.collections4.bidimap.DualTreeBidiMap.ViewMap"""
 
    @staticmethod
    def _wrap(java_value: _ViewMap) -> 'ViewMap':
        return ViewMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ViewMap):
        """
        Dynamic initializer for ViewMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ViewMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ViewMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_ViewMap, self).tailMap(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).equals(arg0))

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
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).get(arg0))

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
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_map.AbstractMapDecorator, self).putAll(arg0)

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

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.clear()"""
        super(ViewMap, self).clear()

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.previousKey(K)"""
        return object._wrap(super(_ViewMap, self).previousKey(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.AbstractSortedMapDecorator.comparator()"""
        return 'Comparator'._wrap(super(map.AbstractSortedMapDecorator, self).comparator())

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).keySet())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.firstKey()"""
        return object._wrap(super(map.AbstractSortedMapDecorator, self).firstKey())

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
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_ViewMap, self).containsValue(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(map.AbstractMapDecorator, self).size())

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
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_ViewMap, self).headMap(arg0))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.lastKey()"""
        return object._wrap(super(map.AbstractSortedMapDecorator, self).lastKey())

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
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_ViewMap, self).subMap(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'._wrap(super(map.AbstractMapDecorator, self).values())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(map.AbstractSortedMapDecorator, self).mapIterator())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap.nextKey(K)"""
        return object._wrap(super(_ViewMap, self).nextKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

 
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualTreeBidiMap$ViewMap 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.apache.commons.collections4.map.AbstractMapDecorator as _AbstractMapDecorator
_AbstractMapDecorator = _AbstractMapDecorator
from builtins import type
import java.util.Map as _Map
_Map = _Map
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as _AbstractBidiMapDecorator
_AbstractBidiMapDecorator = _AbstractBidiMapDecorator
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.BidiMap as _BidiMap
_BidiMap = _BidiMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractBidiMapDecorator():
    """org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractBidiMapDecorator) -> 'AbstractBidiMapDecorator':
        return AbstractBidiMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractBidiMapDecorator):
        """
        Dynamic initializer for AbstractBidiMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractBidiMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractBidiMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).equals(arg0))

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
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.values()"""
        return 'Set'._wrap(super(AbstractBidiMapDecorator, self).values())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).get(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.removeValue(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).removeValue(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_map.AbstractMapDecorator, self).putAll(arg0)

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(map.AbstractMapDecorator, self).size())

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
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).getKey(arg0))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.inverseBidiMap()"""
        return 'collections4.BidiMap'._wrap(super(AbstractBidiMapDecorator, self).inverseBidiMap())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(map.AbstractMapDecorator, self).clear()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractBidiMapDecorator, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(map.AbstractMapDecorator, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(map.AbstractMapDecorator, self).isEmpty())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator
from builtins import str
import org.apache.commons.collections4.bidimap.DualTreeBidiMap as _DualTreeBidiMap_BidiOrderedMapIterator
_BidiOrderedMapIterator = _DualTreeBidiMap_BidiOrderedMapIterator.BidiOrderedMapIterator
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BidiOrderedMapIterator():
    """org.apache.commons.collections4.bidimap.DualTreeBidiMap.BidiOrderedMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _BidiOrderedMapIterator) -> 'BidiOrderedMapIterator':
        return BidiOrderedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BidiOrderedMapIterator):
        """
        Dynamic initializer for BidiOrderedMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BidiOrderedMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BidiOrderedMapIterator__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.toString()"""
        return str._wrap(super(BidiOrderedMapIterator, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.reset()"""
        super(BidiOrderedMapIterator, self).reset()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.getValue()"""
        return object._wrap(super(BidiOrderedMapIterator, self).getValue())

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.previous()"""
        return object._wrap(super(BidiOrderedMapIterator, self).previous())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.setValue(V)"""
        return object._wrap(super(_BidiOrderedMapIterator, self).setValue(arg0))

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.hasPrevious()"""
        return bool._wrap(super(BidiOrderedMapIterator, self).hasPrevious())

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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.getKey()"""
        return object._wrap(super(BidiOrderedMapIterator, self).getKey())

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
        """public boolean org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.hasNext()"""
        return bool._wrap(super(BidiOrderedMapIterator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.next()"""
        return object._wrap(super(BidiOrderedMapIterator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.DualTreeBidiMap$BidiOrderedMapIterator.remove()"""
        super(BidiOrderedMapIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$MapEntry
from builtins import str
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_MapEntry
_MapEntry = _AbstractDualBidiMap_MapEntry.MapEntry
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator as _AbstractMapEntryDecorator
_AbstractMapEntryDecorator = _AbstractMapEntryDecorator
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapEntry():
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.MapEntry"""
 
    @staticmethod
    def _wrap(java_value: _MapEntry) -> 'MapEntry':
        return MapEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapEntry):
        """
        Dynamic initializer for MapEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_keyvalue.AbstractMapEntryDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap$MapEntry.setValue(V)"""
        return object._wrap(super(_MapEntry, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.toString()"""
        return str._wrap(super(keyvalue.AbstractMapEntryDecorator, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.getKey()"""
        return object._wrap(super(keyvalue.AbstractMapEntryDecorator, self).getKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.hashCode()"""
        return int._wrap(super(keyvalue.AbstractMapEntryDecorator, self).hashCode())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.keyvalue.AbstractMapEntryDecorator.getValue()"""
        return object._wrap(super(keyvalue.AbstractMapEntryDecorator, self).getValue())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualHashBidiMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap
_AbstractDualBidiMap = _AbstractDualBidiMap
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.bidimap.DualHashBidiMap as _DualHashBidiMap
_DualHashBidiMap = _DualHashBidiMap
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
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
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.BidiMap as _BidiMap
_BidiMap = _BidiMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DualHashBidiMap():
    """org.apache.commons.collections4.bidimap.DualHashBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _DualHashBidiMap) -> 'DualHashBidiMap':
        return DualHashBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DualHashBidiMap):
        """
        Dynamic initializer for DualHashBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DualHashBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DualHashBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bidimap.DualHashBidiMap()"""
        val = _DualHashBidiMap()
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.clear()"""
        super(AbstractDualBidiMap, self).clear()

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).getKey(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.size()"""
        return int._wrap(super(AbstractDualBidiMap, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.entrySet()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).containsKey(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractDualBidiMap, self).putAll(arg0)

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.put(K,V)"""
        return object._wrap(super(_AbstractDualBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.removeValue(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).removeValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.hashCode()"""
        return int._wrap(super(AbstractDualBidiMap, self).hashCode())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).get(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.collections4.bidimap.DualHashBidiMap()"""
        val = _DualHashBidiMap()
        self.__wrapper = val

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.inverseBidiMap()"""
        return 'collections4.BidiMap'._wrap(super(AbstractDualBidiMap, self).inverseBidiMap())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.isEmpty()"""
        return bool._wrap(super(AbstractDualBidiMap, self).isEmpty())

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).remove(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).containsValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap.toString()"""
        return str._wrap(super(AbstractDualBidiMap, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractDualBidiMap, self).mapIterator())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.keySet()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).keySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.bidimap.DualHashBidiMap(java.util.Map<? extends K, ? extends V>)"""
        val = _DualHashBidiMap(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.values()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).values())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySetIterator
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
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as _AbstractUntypedIteratorDecorator
_AbstractUntypedIteratorDecorator = _AbstractUntypedIteratorDecorator
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_EntrySetIterator
_EntrySetIterator = _AbstractDualBidiMap_EntrySetIterator.EntrySetIterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntrySetIterator():
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.EntrySetIterator"""
 
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
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def next(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySetIterator.next()"""
        return 'Entry.Map$Entry'._wrap(super(EntrySetIterator, self).next())

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
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySetIterator.remove()"""
        super(EntrySetIterator, self).remove()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool._wrap(super(iterators.AbstractUntypedIteratorDecorator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$Values
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_View
_View = _AbstractDualBidiMap_View.View
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_Values
_Values = _AbstractDualBidiMap_Values.Values
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
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
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
 
class Values():
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.Values"""
 
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
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

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
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_View, self).removeAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int._wrap(super(View, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$Values.iterator()"""
        return 'Iterator'._wrap(super(Values, self).iterator())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$Values.contains(java.lang.Object)"""
        return bool._wrap(super(_Values, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool._wrap(super(_View, self).equals(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_View, self).removeIf(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_View, self).retainAll(arg0))

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

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$Values.remove(java.lang.Object)"""
        return bool._wrap(super(_Values, self).remove(arg0))

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

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_BidiMapIterator
_BidiMapIterator = _AbstractDualBidiMap_BidiMapIterator.BidiMapIterator
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BidiMapIterator():
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.BidiMapIterator"""
 
    @staticmethod
    def _wrap(java_value: _BidiMapIterator) -> 'BidiMapIterator':
        return BidiMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BidiMapIterator):
        """
        Dynamic initializer for BidiMapIterator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BidiMapIterator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BidiMapIterator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.reset()"""
        super(BidiMapIterator, self).reset()

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.setValue(V)"""
        return object._wrap(super(_BidiMapIterator, self).setValue(arg0))

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.remove()"""
        super(BidiMapIterator, self).remove()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.getValue()"""
        return object._wrap(super(BidiMapIterator, self).getValue())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.getKey()"""
        return object._wrap(super(BidiMapIterator, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.toString()"""
        return str._wrap(super(BidiMapIterator, self).toString())

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
    def next(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.next()"""
        return object._wrap(super(BidiMapIterator, self).next())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$BidiMapIterator.hasNext()"""
        return bool._wrap(super(BidiMapIterator, self).hasNext())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
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
import org.apache.commons.collections4.SortedBidiMap as _SortedBidiMap
_SortedBidiMap = _SortedBidiMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as _AbstractBidiMapDecorator
_AbstractBidiMapDecorator = _AbstractBidiMapDecorator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap as _UnmodifiableSortedBidiMap
_UnmodifiableSortedBidiMap = _UnmodifiableSortedBidiMap
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator as _AbstractSortedBidiMapDecorator
_AbstractSortedBidiMapDecorator = _AbstractSortedBidiMapDecorator
import java.util.function.Function as Function
import java.util.Map as Map
import org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator as _AbstractOrderedBidiMapDecorator
_AbstractOrderedBidiMapDecorator = _AbstractOrderedBidiMapDecorator
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableSortedBidiMap():
    """org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableSortedBidiMap) -> 'UnmodifiableSortedBidiMap':
        return UnmodifiableSortedBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableSortedBidiMap):
        """
        Dynamic initializer for UnmodifiableSortedBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableSortedBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableSortedBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(map.AbstractMapDecorator, self).hashCode())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def valueComparator(self) -> 'Comparator':
        """public java.util.Comparator<? super V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.valueComparator()"""
        return 'Comparator'._wrap(super(AbstractSortedBidiMapDecorator, self).valueComparator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableSortedBidiMap, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).get(arg0))

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
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.removeValue(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableSortedBidiMap, self).removeValue(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.keySet()"""
        return 'Set'._wrap(super(UnmodifiableSortedBidiMap, self).keySet())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.firstKey()"""
        return object._wrap(super(AbstractOrderedBidiMapDecorator, self).firstKey())

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
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.put(K,V)"""
        return object._wrap(super(_UnmodifiableSortedBidiMap, self).put(arg0, arg1))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractOrderedBidiMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_UnmodifiableSortedBidiMap, self).putAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

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

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(UnmodifiableSortedBidiMap, self).mapIterator())

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.SortedBidiMap':
        """public org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.inverseBidiMap()"""
        return 'collections4.SortedBidiMap'._wrap(super(UnmodifiableSortedBidiMap, self).inverseBidiMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

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
    def unmodifiableSortedBidiMap(arg0: 'SortedBidiMap') -> 'collections4.SortedBidiMap':
        """public static <K,V> org.apache.commons.collections4.SortedBidiMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.unmodifiableSortedBidiMap(org.apache.commons.collections4.SortedBidiMap<K, ? extends V>)"""
        return collections4.SortedBidiMap._wrap(_UnmodifiableSortedBidiMap.unmodifiableSortedBidiMap(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.remove(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableSortedBidiMap, self).remove(arg0))

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.values()"""
        return 'Set'._wrap(super(UnmodifiableSortedBidiMap, self).values())

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedBidiMapDecorator, self).comparator())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.lastKey()"""
        return object._wrap(super(AbstractOrderedBidiMapDecorator, self).lastKey())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(map.AbstractMapDecorator, self).size())

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableSortedBidiMap, self).tailMap(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractOrderedBidiMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.clear()"""
        super(UnmodifiableSortedBidiMap, self).clear()

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableSortedBidiMap, self).subMap(arg0, arg1))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableSortedBidiMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableSortedBidiMap, self).headMap(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualTreeBidiMap
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap
_AbstractDualBidiMap = _AbstractDualBidiMap
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
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
import org.apache.commons.collections4.SortedBidiMap as _SortedBidiMap
_SortedBidiMap = _SortedBidiMap
import org.apache.commons.collections4.bidimap.DualTreeBidiMap as _DualTreeBidiMap
_DualTreeBidiMap = _DualTreeBidiMap
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
import org.apache.commons.collections4.OrderedBidiMap as _OrderedBidiMap
_OrderedBidiMap = _OrderedBidiMap
import java.util.Comparator as Comparator
import java.util.Set as Set
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
 
class DualTreeBidiMap():
    """org.apache.commons.collections4.bidimap.DualTreeBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _DualTreeBidiMap) -> 'DualTreeBidiMap':
        return DualTreeBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DualTreeBidiMap):
        """
        Dynamic initializer for DualTreeBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DualTreeBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DualTreeBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.headMap(K)"""
        return 'SortedMap'._wrap(super(_DualTreeBidiMap, self).headMap(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.clear()"""
        super(AbstractDualBidiMap, self).clear()

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).getKey(arg0))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.SortedBidiMap':
        """public org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.bidimap.DualTreeBidiMap.inverseBidiMap()"""
        return 'collections4.SortedBidiMap'._wrap(super(DualTreeBidiMap, self).inverseBidiMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.put(K,V)"""
        return object._wrap(super(_AbstractDualBidiMap, self).put(arg0, arg1))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap.previousKey(K)"""
        return object._wrap(super(_DualTreeBidiMap, self).previousKey(arg0))

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
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.bidimap.DualTreeBidiMap.comparator()"""
        return 'Comparator'._wrap(super(DualTreeBidiMap, self).comparator())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.hashCode()"""
        return int._wrap(super(AbstractDualBidiMap, self).hashCode())

    @overload
    def inverseSortedBidiMap(self) -> 'collections4.SortedBidiMap':
        """public org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.bidimap.DualTreeBidiMap.inverseSortedBidiMap()"""
        return 'collections4.SortedBidiMap'._wrap(super(DualTreeBidiMap, self).inverseSortedBidiMap())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.isEmpty()"""
        return bool._wrap(super(AbstractDualBidiMap, self).isEmpty())

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).remove(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).containsValue(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.tailMap(K)"""
        return 'SortedMap'._wrap(super(_DualTreeBidiMap, self).tailMap(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap.toString()"""
        return str._wrap(super(AbstractDualBidiMap, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bidimap.DualTreeBidiMap()"""
        val = _DualTreeBidiMap()
        self.__wrapper = val

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object._wrap(super(_SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).lastEntry())

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

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.values()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).values())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.size()"""
        return int._wrap(super(AbstractDualBidiMap, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.entrySet()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).containsKey(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractDualBidiMap, self).putAll(arg0)

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap.firstKey()"""
        return object._wrap(super(DualTreeBidiMap, self).firstKey())

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.removeValue(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).removeValue(arg0))

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).get(arg0))

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
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap.lastKey()"""
        return object._wrap(super(DualTreeBidiMap, self).lastKey())

    @overload
    def __init__(self, arg0: 'Comparator', arg1: 'Comparator'):
        """public org.apache.commons.collections4.bidimap.DualTreeBidiMap(java.util.Comparator<? super K>,java.util.Comparator<? super V>)"""
        val = _DualTreeBidiMap(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_DualTreeBidiMap, self).subMap(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(DualTreeBidiMap, self).mapIterator())

    @override
    @overload
    def valueComparator(self) -> 'Comparator':
        """public java.util.Comparator<? super V> org.apache.commons.collections4.bidimap.DualTreeBidiMap.valueComparator()"""
        return 'Comparator'._wrap(super(DualTreeBidiMap, self).valueComparator())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.DualTreeBidiMap.nextKey(K)"""
        return object._wrap(super(_DualTreeBidiMap, self).nextKey(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def inverseOrderedBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.DualTreeBidiMap.inverseOrderedBidiMap()"""
        return 'collections4.OrderedBidiMap'._wrap(super(DualTreeBidiMap, self).inverseOrderedBidiMap())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.keySet()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).keySet())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bidimap.DualTreeBidiMap()"""
        val = _DualTreeBidiMap()
        self.__wrapper = val

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
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).equals(arg0))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.bidimap.DualTreeBidiMap(java.util.Map<? extends K, ? extends V>)"""
        val = _DualTreeBidiMap(arg0)
        self.__wrapper = val

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap
_AbstractDualBidiMap = _AbstractDualBidiMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
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
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.BidiMap as _BidiMap
_BidiMap = _BidiMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractDualBidiMap():
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _AbstractDualBidiMap) -> 'AbstractDualBidiMap':
        return AbstractDualBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractDualBidiMap):
        """
        Dynamic initializer for AbstractDualBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractDualBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractDualBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.clear()"""
        super(AbstractDualBidiMap, self).clear()

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).getKey(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.size()"""
        return int._wrap(super(AbstractDualBidiMap, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.entrySet()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).containsKey(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractDualBidiMap, self).putAll(arg0)

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.put(K,V)"""
        return object._wrap(super(_AbstractDualBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.removeValue(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).removeValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.hashCode()"""
        return int._wrap(super(AbstractDualBidiMap, self).hashCode())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).get(arg0))

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
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.inverseBidiMap()"""
        return 'collections4.BidiMap'._wrap(super(AbstractDualBidiMap, self).inverseBidiMap())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.isEmpty()"""
        return bool._wrap(super(AbstractDualBidiMap, self).isEmpty())

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).remove(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).containsValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap.toString()"""
        return str._wrap(super(AbstractDualBidiMap, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractDualBidiMap, self).mapIterator())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.keySet()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).keySet())

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
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.values()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).values())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$ValuesIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_ValuesIterator
_ValuesIterator = _AbstractDualBidiMap_ValuesIterator.ValuesIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as _AbstractUntypedIteratorDecorator
_AbstractUntypedIteratorDecorator = _AbstractUntypedIteratorDecorator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValuesIterator():
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.ValuesIterator"""
 
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
    def next(self) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap$ValuesIterator.next()"""
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
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$ValuesIterator.remove()"""
        super(ValuesIterator, self).remove()

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
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool._wrap(super(iterators.AbstractUntypedIteratorDecorator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
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
import org.apache.commons.collections4.SortedBidiMap as _SortedBidiMap
_SortedBidiMap = _SortedBidiMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as _AbstractBidiMapDecorator
_AbstractBidiMapDecorator = _AbstractBidiMapDecorator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator as _AbstractSortedBidiMapDecorator
_AbstractSortedBidiMapDecorator = _AbstractSortedBidiMapDecorator
import java.util.function.Function as Function
import org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator as _AbstractOrderedBidiMapDecorator
_AbstractOrderedBidiMapDecorator = _AbstractOrderedBidiMapDecorator
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractSortedBidiMapDecorator():
    """org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractSortedBidiMapDecorator) -> 'AbstractSortedBidiMapDecorator':
        return AbstractSortedBidiMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractSortedBidiMapDecorator):
        """
        Dynamic initializer for AbstractSortedBidiMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractSortedBidiMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractSortedBidiMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def valueComparator(self) -> 'Comparator':
        """public java.util.Comparator<? super V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.valueComparator()"""
        return 'Comparator'._wrap(super(AbstractSortedBidiMapDecorator, self).valueComparator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).equals(arg0))

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
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).get(arg0))

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
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_map.AbstractMapDecorator, self).putAll(arg0)

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.firstKey()"""
        return object._wrap(super(AbstractOrderedBidiMapDecorator, self).firstKey())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.tailMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractSortedBidiMapDecorator, self).tailMap(arg0))

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
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractOrderedBidiMapDecorator, self).previousKey(arg0))

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).keySet())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractOrderedBidiMapDecorator, self).mapIterator())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def __init__(self, arg0: 'SortedBidiMap'):
        """public org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator(org.apache.commons.collections4.SortedBidiMap<K, V>)"""
        val = _AbstractSortedBidiMapDecorator(arg0)
        self.__wrapper = val

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.values()"""
        return 'Set'._wrap(super(AbstractBidiMapDecorator, self).values())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.SortedBidiMap':
        """public org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.inverseBidiMap()"""
        return 'collections4.SortedBidiMap'._wrap(super(AbstractSortedBidiMapDecorator, self).inverseBidiMap())

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.removeValue(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).removeValue(arg0))

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedBidiMapDecorator, self).comparator())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.lastKey()"""
        return object._wrap(super(AbstractOrderedBidiMapDecorator, self).lastKey())

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.headMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractSortedBidiMapDecorator, self).headMap(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(map.AbstractMapDecorator, self).size())

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
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractOrderedBidiMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(map.AbstractMapDecorator, self).clear()

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.bidimap.AbstractSortedBidiMapDecorator.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_AbstractSortedBidiMapDecorator, self).subMap(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(map.AbstractMapDecorator, self).isEmpty())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySet
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_EntrySet
_EntrySet = _AbstractDualBidiMap_EntrySet.EntrySet
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_View
_View = _AbstractDualBidiMap_View.View
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
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
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.EntrySet"""
 
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
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

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
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_View, self).removeAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySet.remove(java.lang.Object)"""
        return bool._wrap(super(_EntrySet, self).remove(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int._wrap(super(View, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$EntrySet.iterator()"""
        return 'Iterator'._wrap(super(EntrySet, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool._wrap(super(_View, self).equals(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_View, self).removeIf(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_View, self).retainAll(arg0))

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

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Set as _Set
_Set = _Set
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
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as _AbstractBidiMapDecorator
_AbstractBidiMapDecorator = _AbstractBidiMapDecorator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import org.apache.commons.collections4.OrderedBidiMap as _OrderedBidiMap
_OrderedBidiMap = _OrderedBidiMap
import java.util.Set as Set
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap as _UnmodifiableOrderedBidiMap
_UnmodifiableOrderedBidiMap = _UnmodifiableOrderedBidiMap
import java.util.Map as Map
import org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator as _AbstractOrderedBidiMapDecorator
_AbstractOrderedBidiMapDecorator = _AbstractOrderedBidiMapDecorator
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableOrderedBidiMap():
    """org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableOrderedBidiMap) -> 'UnmodifiableOrderedBidiMap':
        return UnmodifiableOrderedBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableOrderedBidiMap):
        """
        Dynamic initializer for UnmodifiableOrderedBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableOrderedBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableOrderedBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.keySet()"""
        return 'Set'._wrap(super(UnmodifiableOrderedBidiMap, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_UnmodifiableOrderedBidiMap, self).putAll(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).equals(arg0))

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
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.lastKey()"""
        return object._wrap(super(AbstractOrderedBidiMapDecorator, self).lastKey())

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.removeValue(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableOrderedBidiMap, self).removeValue(arg0))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.firstKey()"""
        return object._wrap(super(AbstractOrderedBidiMapDecorator, self).firstKey())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(map.AbstractMapDecorator, self).size())

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

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.values()"""
        return 'Set'._wrap(super(UnmodifiableOrderedBidiMap, self).values())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(UnmodifiableOrderedBidiMap, self).mapIterator())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractOrderedBidiMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.clear()"""
        super(UnmodifiableOrderedBidiMap, self).clear()

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.inverseBidiMap()"""
        return 'collections4.OrderedBidiMap'._wrap(super(UnmodifiableOrderedBidiMap, self).inverseBidiMap())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.put(K,V)"""
        return object._wrap(super(_UnmodifiableOrderedBidiMap, self).put(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableOrderedBidiMap(arg0: 'OrderedBidiMap') -> 'collections4.OrderedBidiMap':
        """public static <K,V> org.apache.commons.collections4.OrderedBidiMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.unmodifiableOrderedBidiMap(org.apache.commons.collections4.OrderedBidiMap<? extends K, ? extends V>)"""
        return collections4.OrderedBidiMap._wrap(_UnmodifiableOrderedBidiMap.unmodifiableOrderedBidiMap(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def inverseOrderedBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.inverseOrderedBidiMap()"""
        return 'collections4.OrderedBidiMap'._wrap(super(UnmodifiableOrderedBidiMap, self).inverseOrderedBidiMap())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractOrderedBidiMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableOrderedBidiMap, self).entrySet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(map.AbstractMapDecorator, self).toString())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableOrderedBidiMap.remove(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableOrderedBidiMap, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(map.AbstractMapDecorator, self).isEmpty())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.TreeBidiMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.bidimap.TreeBidiMap as _TreeBidiMap
_TreeBidiMap = _TreeBidiMap
import java.lang.Comparable as _Comparable
_Comparable = _Comparable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Comparable as Comparable
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import org.apache.commons.collections4.OrderedBidiMap as _OrderedBidiMap
_OrderedBidiMap = _OrderedBidiMap
import java.util.Set as Set
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TreeBidiMap():
    """org.apache.commons.collections4.bidimap.TreeBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _TreeBidiMap) -> 'TreeBidiMap':
        return TreeBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TreeBidiMap):
        """
        Dynamic initializer for TreeBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TreeBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TreeBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.TreeBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_TreeBidiMap, self).putAll(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.TreeBidiMap.toString()"""
        return str._wrap(super(TreeBidiMap, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.TreeBidiMap.entrySet()"""
        return 'Set'._wrap(super(TreeBidiMap, self).entrySet())

    @overload
    def previousKey(self, arg0: 'Comparable') -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.previousKey(K)"""
        return 'Comparable'._wrap(super(_TreeBidiMap, self).previousKey(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.TreeBidiMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_TreeBidiMap, self).containsKey(arg0))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.TreeBidiMap.inverseBidiMap()"""
        return 'collections4.OrderedBidiMap'._wrap(super(TreeBidiMap, self).inverseBidiMap())

    @override
    @overload
    def lastKey(self) -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.lastKey()"""
        return 'Comparable'._wrap(super(TreeBidiMap, self).lastKey())

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
    def put(self, arg0: 'Comparable', arg1: 'Comparable') -> 'Comparable':
        """public V org.apache.commons.collections4.bidimap.TreeBidiMap.put(K,V)"""
        return 'Comparable'._wrap(super(_TreeBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.TreeBidiMap.hashCode()"""
        return int._wrap(super(TreeBidiMap, self).hashCode())

    @overload
    def removeValue(self, arg0: object) -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.removeValue(java.lang.Object)"""
        return 'Comparable'._wrap(super(_TreeBidiMap, self).removeValue(arg0))

    @overload
    def nextKey(self, arg0: 'Comparable') -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.nextKey(K)"""
        return 'Comparable'._wrap(super(_TreeBidiMap, self).nextKey(arg0))

    @overload
    def remove(self, arg0: object) -> 'Comparable':
        """public V org.apache.commons.collections4.bidimap.TreeBidiMap.remove(java.lang.Object)"""
        return 'Comparable'._wrap(super(_TreeBidiMap, self).remove(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bidimap.TreeBidiMap()"""
        val = _TreeBidiMap()
        self.__wrapper = val

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.TreeBidiMap.values()"""
        return 'Set'._wrap(super(TreeBidiMap, self).values())

    @overload
    def get(self, arg0: object) -> 'Comparable':
        """public V org.apache.commons.collections4.bidimap.TreeBidiMap.get(java.lang.Object)"""
        return 'Comparable'._wrap(super(_TreeBidiMap, self).get(arg0))

    @override
    @overload
    def firstKey(self) -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.firstKey()"""
        return 'Comparable'._wrap(super(TreeBidiMap, self).firstKey())

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.TreeBidiMap.size()"""
        return int._wrap(super(TreeBidiMap, self).size())

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
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.TreeBidiMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_TreeBidiMap, self).containsValue(arg0))

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
    def __init__(self):
        """public org.apache.commons.collections4.bidimap.TreeBidiMap()"""
        val = _TreeBidiMap()
        self.__wrapper = val

    @overload
    def getKey(self, arg0: object) -> 'Comparable':
        """public K org.apache.commons.collections4.bidimap.TreeBidiMap.getKey(java.lang.Object)"""
        return 'Comparable'._wrap(super(_TreeBidiMap, self).getKey(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.TreeBidiMap.clear()"""
        super(TreeBidiMap, self).clear()

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.TreeBidiMap.keySet()"""
        return 'Set'._wrap(super(TreeBidiMap, self).keySet())

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

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.TreeBidiMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(TreeBidiMap, self).mapIterator())

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.bidimap.TreeBidiMap(java.util.Map<? extends K, ? extends V>)"""
        val = _TreeBidiMap(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.TreeBidiMap.equals(java.lang.Object)"""
        return bool._wrap(super(_TreeBidiMap, self).equals(arg0))

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
        """public boolean org.apache.commons.collections4.bidimap.TreeBidiMap.isEmpty()"""
        return bool._wrap(super(TreeBidiMap, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_View
_View = _AbstractDualBidiMap_View.View
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_KeySet
_KeySet = _AbstractDualBidiMap_KeySet.KeySet
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
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
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.KeySet"""
 
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
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.contains(java.lang.Object)"""
        return bool._wrap(super(_KeySet, self).contains(arg0))

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
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_View, self).removeAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.remove(java.lang.Object)"""
        return bool._wrap(super(_KeySet, self).remove(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int._wrap(super(View, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool._wrap(super(_View, self).equals(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_View, self).removeIf(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_View, self).retainAll(arg0))

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

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySet.iterator()"""
        return 'Iterator'._wrap(super(KeySet, self).iterator()) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap
_AbstractDualBidiMap = _AbstractDualBidiMap
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap as _DualLinkedHashBidiMap
_DualLinkedHashBidiMap = _DualLinkedHashBidiMap
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
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.BidiMap as _BidiMap
_BidiMap = _BidiMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DualLinkedHashBidiMap():
    """org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _DualLinkedHashBidiMap) -> 'DualLinkedHashBidiMap':
        return DualLinkedHashBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DualLinkedHashBidiMap):
        """
        Dynamic initializer for DualLinkedHashBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DualLinkedHashBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DualLinkedHashBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.clear()"""
        super(AbstractDualBidiMap, self).clear()

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).getKey(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.size()"""
        return int._wrap(super(AbstractDualBidiMap, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.entrySet()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).containsKey(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap()"""
        val = _DualLinkedHashBidiMap()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractDualBidiMap, self).putAll(arg0)

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.put(K,V)"""
        return object._wrap(super(_AbstractDualBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap.removeValue(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).removeValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap.hashCode()"""
        return int._wrap(super(AbstractDualBidiMap, self).hashCode())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).get(arg0))

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
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap(java.util.Map<? extends K, ? extends V>)"""
        val = _DualLinkedHashBidiMap(arg0)
        self.__wrapper = val

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.inverseBidiMap()"""
        return 'collections4.BidiMap'._wrap(super(AbstractDualBidiMap, self).inverseBidiMap())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.isEmpty()"""
        return bool._wrap(super(AbstractDualBidiMap, self).isEmpty())

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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.AbstractDualBidiMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractDualBidiMap, self).remove(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).containsValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.bidimap.AbstractDualBidiMap.toString()"""
        return str._wrap(super(AbstractDualBidiMap, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractDualBidiMap, self).mapIterator())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.keySet()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).keySet())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.bidimap.DualLinkedHashBidiMap()"""
        val = _DualLinkedHashBidiMap()
        self.__wrapper = val

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
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractDualBidiMap, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractDualBidiMap.values()"""
        return 'Set'._wrap(super(AbstractDualBidiMap, self).values())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.UnmodifiableBidiMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.bidimap.UnmodifiableBidiMap as _UnmodifiableBidiMap
_UnmodifiableBidiMap = _UnmodifiableBidiMap
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.BidiMap as _BidiMap
_BidiMap = _BidiMap
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
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as _AbstractBidiMapDecorator
_AbstractBidiMapDecorator = _AbstractBidiMapDecorator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableBidiMap():
    """org.apache.commons.collections4.bidimap.UnmodifiableBidiMap"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableBidiMap) -> 'UnmodifiableBidiMap':
        return UnmodifiableBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableBidiMap):
        """
        Dynamic initializer for UnmodifiableBidiMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableBidiMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableBidiMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(map.AbstractMapDecorator, self).hashCode())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.keySet()"""
        return 'Set'._wrap(super(UnmodifiableBidiMap, self).keySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.remove(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableBidiMap, self).remove(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).equals(arg0))

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
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.values()"""
        return 'Set'._wrap(super(UnmodifiableBidiMap, self).values())

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.BidiMap':
        """public synchronized org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.inverseBidiMap()"""
        return 'collections4.BidiMap'._wrap(super(UnmodifiableBidiMap, self).inverseBidiMap())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableBidiMap, self).entrySet())

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.removeValue(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableBidiMap, self).removeValue(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.put(K,V)"""
        return object._wrap(super(_UnmodifiableBidiMap, self).put(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(map.AbstractMapDecorator, self).size())

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

    @staticmethod
    @overload
    def unmodifiableBidiMap(arg0: 'BidiMap') -> 'collections4.BidiMap':
        """public static <K,V> org.apache.commons.collections4.BidiMap<K, V> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.unmodifiableBidiMap(org.apache.commons.collections4.BidiMap<? extends K, ? extends V>)"""
        return collections4.BidiMap._wrap(_UnmodifiableBidiMap.unmodifiableBidiMap(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).getKey(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(UnmodifiableBidiMap, self).mapIterator())

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

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_UnmodifiableBidiMap, self).putAll(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(map.AbstractMapDecorator, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(map.AbstractMapDecorator, self).isEmpty())

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
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.UnmodifiableBidiMap.clear()"""
        super(UnmodifiableBidiMap, self).clear()

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Set as _Set
_Set = _Set
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
import org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator as _AbstractBidiMapDecorator
_AbstractBidiMapDecorator = _AbstractBidiMapDecorator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.OrderedMapIterator as _OrderedMapIterator
_OrderedMapIterator = _OrderedMapIterator
import org.apache.commons.collections4.OrderedBidiMap as _OrderedBidiMap
_OrderedBidiMap = _OrderedBidiMap
import java.util.Set as Set
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.function.Function as Function
import org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator as _AbstractOrderedBidiMapDecorator
_AbstractOrderedBidiMapDecorator = _AbstractOrderedBidiMapDecorator
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractOrderedBidiMapDecorator():
    """org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractOrderedBidiMapDecorator) -> 'AbstractOrderedBidiMapDecorator':
        return AbstractOrderedBidiMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractOrderedBidiMapDecorator):
        """
        Dynamic initializer for AbstractOrderedBidiMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractOrderedBidiMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractOrderedBidiMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(AbstractOrderedBidiMapDecorator, self).mapIterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int._wrap(super(map.AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).entrySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_map.AbstractMapDecorator, self).equals(arg0))

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
    def values(self) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.values()"""
        return 'Set'._wrap(super(AbstractBidiMapDecorator, self).values())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).get(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeValue(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.removeValue(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).removeValue(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_map.AbstractMapDecorator, self).putAll(arg0)

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.lastKey()"""
        return object._wrap(super(AbstractOrderedBidiMapDecorator, self).lastKey())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.firstKey()"""
        return object._wrap(super(AbstractOrderedBidiMapDecorator, self).firstKey())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int._wrap(super(map.AbstractMapDecorator, self).size())

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
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.previousKey(K)"""
        return object._wrap(super(_AbstractOrderedBidiMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def inverseBidiMap(self) -> 'collections4.OrderedBidiMap':
        """public org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.inverseBidiMap()"""
        return 'collections4.OrderedBidiMap'._wrap(super(AbstractOrderedBidiMapDecorator, self).inverseBidiMap())

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
    def getKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractBidiMapDecorator.getKey(java.lang.Object)"""
        return object._wrap(super(_AbstractBidiMapDecorator, self).getKey(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractOrderedBidiMapDecorator.nextKey(K)"""
        return object._wrap(super(_AbstractOrderedBidiMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_map.AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(map.AbstractMapDecorator, self).clear()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'._wrap(super(map.AbstractMapDecorator, self).keySet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str._wrap(super(map.AbstractMapDecorator, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool._wrap(super(map.AbstractMapDecorator, self).isEmpty())

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
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_View
_View = _AbstractDualBidiMap_View.View
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
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
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
 
class View():
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.View"""
 
    @staticmethod
    def _wrap(java_value: _View) -> 'View':
        return View(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _View):
        """
        Dynamic initializer for View.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_View__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_View__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.clear()"""
        super(View, self).clear()

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
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_View, self).removeAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.hashCode()"""
        return int._wrap(super(View, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.equals(java.lang.Object)"""
        return bool._wrap(super(_View, self).equals(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_View, self).removeIf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.bidimap.AbstractDualBidiMap$View.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_View, self).retainAll(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySetIterator
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.bidimap.AbstractDualBidiMap as _AbstractDualBidiMap_KeySetIterator
_KeySetIterator = _AbstractDualBidiMap_KeySetIterator.KeySetIterator
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator as _AbstractUntypedIteratorDecorator
_AbstractUntypedIteratorDecorator = _AbstractUntypedIteratorDecorator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeySetIterator():
    """org.apache.commons.collections4.bidimap.AbstractDualBidiMap.KeySetIterator"""
 
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

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(_Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySetIterator.remove()"""
        super(KeySetIterator, self).remove()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.iterators.AbstractUntypedIteratorDecorator.hasNext()"""
        return bool._wrap(super(iterators.AbstractUntypedIteratorDecorator, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.bidimap.AbstractDualBidiMap$KeySetIterator.next()"""
        return object._wrap(super(KeySetIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())