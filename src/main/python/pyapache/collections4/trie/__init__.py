from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.trie.AbstractBitwiseTrie as __AbstractBitwiseTrie_BasicEntry
__BasicEntry = __AbstractBitwiseTrie_BasicEntry.BasicEntry
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.trie.AbstractPatriciaTrie as __AbstractPatriciaTrie_TrieEntry
__TrieEntry = __AbstractPatriciaTrie_TrieEntry.TrieEntry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TrieEntry():
    """org.apache.commons.collections4.trie.AbstractPatriciaTrie.TrieEntry"""
 
    @staticmethod
    def __wrap(java_value: __TrieEntry) -> 'TrieEntry':
        return TrieEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TrieEntry):
        """
        Dynamic initializer for TrieEntry.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isEmpty()"""
        return bool.__wrap(super(TrieEntry, self).isEmpty())

    @overload
    def setKeyValue(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.setKeyValue(K,V)"""
        return object.__wrap(super(__BasicEntry, self).setKeyValue(arg0, arg1))

    @overload
    def isExternalNode(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isExternalNode()"""
        return bool.__wrap(super(TrieEntry, self).isExternalNode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.getValue()"""
        return object.__wrap(super(BasicEntry, self).getValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__BasicEntry, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isInternalNode(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isInternalNode()"""
        return bool.__wrap(super(TrieEntry, self).isInternalNode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.hashCode()"""
        return int.__wrap(super(BasicEntry, self).hashCode())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.setValue(V)"""
        return object.__wrap(super(__BasicEntry, self).setValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.getKey()"""
        return object.__wrap(super(BasicEntry, self).getKey())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.toString()"""
        return str.__wrap(super(TrieEntry, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: int):
        """public org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry(K,V,int)"""
        val = __TrieEntry(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.trie.AbstractBitwiseTrie as __AbstractBitwiseTrie_BasicEntry
__BasicEntry = __AbstractBitwiseTrie_BasicEntry.BasicEntry
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.trie.AbstractPatriciaTrie as __AbstractPatriciaTrie_TrieEntry
__TrieEntry = __AbstractPatriciaTrie_TrieEntry.TrieEntry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TrieEntry():
    """org.apache.commons.collections4.trie.AbstractPatriciaTrie.TrieEntry"""
 
    @staticmethod
    def __wrap(java_value: __TrieEntry) -> 'TrieEntry':
        return TrieEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TrieEntry):
        """
        Dynamic initializer for TrieEntry.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isEmpty()"""
        return bool.__wrap(super(TrieEntry, self).isEmpty())

    @overload
    def setKeyValue(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.setKeyValue(K,V)"""
        return object.__wrap(super(__BasicEntry, self).setKeyValue(arg0, arg1))

    @overload
    def isExternalNode(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isExternalNode()"""
        return bool.__wrap(super(TrieEntry, self).isExternalNode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.getValue()"""
        return object.__wrap(super(BasicEntry, self).getValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__BasicEntry, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isInternalNode(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isInternalNode()"""
        return bool.__wrap(super(TrieEntry, self).isInternalNode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.hashCode()"""
        return int.__wrap(super(BasicEntry, self).hashCode())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.setValue(V)"""
        return object.__wrap(super(__BasicEntry, self).setValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.getKey()"""
        return object.__wrap(super(BasicEntry, self).getKey())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.toString()"""
        return str.__wrap(super(TrieEntry, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: int):
        """public org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry(K,V,int)"""
        val = __TrieEntry(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry 
 
 
# CLASS: org.apache.commons.collections4.trie.UnmodifiableTrie
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.Trie as __Trie
__Trie = __Trie
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
import org.apache.commons.collections4.trie.UnmodifiableTrie as __UnmodifiableTrie
__UnmodifiableTrie = __UnmodifiableTrie
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class UnmodifiableTrie():
    """org.apache.commons.collections4.trie.UnmodifiableTrie"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableTrie) -> 'UnmodifiableTrie':
        return UnmodifiableTrie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableTrie):
        """
        Dynamic initializer for UnmodifiableTrie.
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
 
    @staticmethod
    @overload
    def unmodifiableTrie(arg0: 'Trie') -> 'collections4.Trie':
        """public static <K,V> org.apache.commons.collections4.Trie<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.unmodifiableTrie(org.apache.commons.collections4.Trie<K, ? extends V>)"""
        return collections4.Trie.__wrap(__UnmodifiableTrie.unmodifiableTrie(arg0))

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.headMap(K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableTrie, self).headMap(arg0))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.UnmodifiableTrie.previousKey(K)"""
        return object.__wrap(super(__UnmodifiableTrie, self).previousKey(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.UnmodifiableTrie.nextKey(K)"""
        return object.__wrap(super(__UnmodifiableTrie, self).nextKey(arg0))

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.UnmodifiableTrie.remove(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableTrie, self).remove(arg0))

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.UnmodifiableTrie.isEmpty()"""
        return bool.__wrap(super(UnmodifiableTrie, self).isEmpty())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.trie.UnmodifiableTrie.put(K,V)"""
        return object.__wrap(super(__UnmodifiableTrie, self).put(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.trie.UnmodifiableTrie.firstKey()"""
        return object.__wrap(super(UnmodifiableTrie, self).firstKey())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.UnmodifiableTrie.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableTrie, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.trie.UnmodifiableTrie.clear()"""
        super(UnmodifiableTrie, self).clear()

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

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
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

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
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.trie.UnmodifiableTrie.lastKey()"""
        return object.__wrap(super(UnmodifiableTrie, self).lastKey())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.trie.UnmodifiableTrie.comparator()"""
        return 'Comparator'.__wrap(super(UnmodifiableTrie, self).comparator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.UnmodifiableTrie.equals(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableTrie, self).equals(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.trie.UnmodifiableTrie.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__UnmodifiableTrie, self).putAll(arg0)

    @overload
    def __init__(self, arg0: 'Trie'):
        """public org.apache.commons.collections4.trie.UnmodifiableTrie(org.apache.commons.collections4.Trie<K, ? extends V>)"""
        val = __UnmodifiableTrie(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.trie.UnmodifiableTrie.entrySet()"""
        return 'Set'.__wrap(super(UnmodifiableTrie, self).entrySet())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableTrie, self).subMap(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.trie.UnmodifiableTrie.size()"""
        return int.__wrap(super(UnmodifiableTrie, self).size())

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.trie.UnmodifiableTrie.keySet()"""
        return 'Set'.__wrap(super(UnmodifiableTrie, self).keySet())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.UnmodifiableTrie.toString()"""
        return str.__wrap(super(UnmodifiableTrie, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(UnmodifiableTrie, self).mapIterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.trie.UnmodifiableTrie.hashCode()"""
        return int.__wrap(super(UnmodifiableTrie, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.UnmodifiableTrie.get(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableTrie, self).get(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.trie.UnmodifiableTrie.values()"""
        return 'Collection'.__wrap(super(UnmodifiableTrie, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.UnmodifiableTrie.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableTrie, self).containsValue(arg0))

    @overload
    def prefixMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.prefixMap(K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableTrie, self).prefixMap(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableTrie, self).tailMap(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.trie.KeyAnalyzer
from builtins import str
import org.apache.commons.collections4.trie.KeyAnalyzer as __KeyAnalyzer
__KeyAnalyzer = __KeyAnalyzer
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
 
class KeyAnalyzer(ABC):
    """org.apache.commons.collections4.trie.KeyAnalyzer"""
 
    @staticmethod
    def __wrap(java_value: __KeyAnalyzer) -> 'KeyAnalyzer':
        return KeyAnalyzer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyAnalyzer):
        """
        Dynamic initializer for KeyAnalyzer.
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @abstractmethod
    def lengthInBits(self, arg0: object):
        """public abstract int org.apache.commons.collections4.trie.KeyAnalyzer.lengthInBits(K)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @abstractmethod
    def bitIndex(self, arg0: object, arg1: int, arg2: int, arg3: object, arg4: int, arg5: int):
        """public abstract int org.apache.commons.collections4.trie.KeyAnalyzer.bitIndex(K,int,int,K,int,int)"""
        pass

    @abstractmethod
    def isBitSet(self, arg0: object, arg1: int, arg2: int):
        """public abstract boolean org.apache.commons.collections4.trie.KeyAnalyzer.isBitSet(K,int,int)"""
        pass

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.KeyAnalyzer()"""
        val = __KeyAnalyzer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def bitsPerElement(self, ):
        """public abstract int org.apache.commons.collections4.trie.KeyAnalyzer.bitsPerElement()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @abstractmethod
    def isPrefix(self, arg0: object, arg1: int, arg2: int, arg3: object):
        """public abstract boolean org.apache.commons.collections4.trie.KeyAnalyzer.isPrefix(K,int,int,K)"""
        pass

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.trie.KeyAnalyzer()"""
        val = __KeyAnalyzer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.trie.KeyAnalyzer.compare(K,K)"""
        return int.__wrap(super(__KeyAnalyzer, self).compare(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.trie.PatriciaTrie
import java.util.AbstractMap as __AbstractMap
__AbstractMap = __AbstractMap
import org.apache.commons.collections4.trie.AbstractPatriciaTrie as __AbstractPatriciaTrie
__AbstractPatriciaTrie = __AbstractPatriciaTrie
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.SequencedCollection as SequencedCollection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import org.apache.commons.collections4.trie.PatriciaTrie as __PatriciaTrie
__PatriciaTrie = __PatriciaTrie
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.trie.AbstractBitwiseTrie as __AbstractBitwiseTrie
__AbstractBitwiseTrie = __AbstractBitwiseTrie
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class PatriciaTrie():
    """org.apache.commons.collections4.trie.PatriciaTrie"""
 
    @staticmethod
    def __wrap(java_value: __PatriciaTrie) -> 'PatriciaTrie':
        return PatriciaTrie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PatriciaTrie):
        """
        Dynamic initializer for PatriciaTrie.
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
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @overload
    def prefixMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.prefixMap(K)"""
        return 'SortedMap'.__wrap(super(__AbstractPatriciaTrie, self).prefixMap(arg0))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.headMap(K)"""
        return 'SortedMap'.__wrap(super(__AbstractPatriciaTrie, self).headMap(arg0))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractPatriciaTrie.put(K,V)"""
        return object.__wrap(super(__AbstractPatriciaTrie, self).put(arg0, arg1))

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.PatriciaTrie()"""
        val = __PatriciaTrie()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__AbstractPatriciaTrie, self).subMap(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).containsValue(arg0))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.firstKey()"""
        return object.__wrap(super(AbstractPatriciaTrie, self).firstKey())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap.hashCode()"""
        return int.__wrap(super(AbstractMap, self).hashCode())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractMap.isEmpty()"""
        return bool.__wrap(super(AbstractMap, self).isEmpty())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @overload
    def select(self, arg0: object) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.select(K)"""
        return 'Entry.Map$Entry'.__wrap(super(__AbstractPatriciaTrie, self).select(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def selectKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.selectKey(K)"""
        return object.__wrap(super(__AbstractPatriciaTrie, self).selectKey(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__AbstractPatriciaTrie, self).tailMap(arg0))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.trie.PatriciaTrie()"""
        val = __PatriciaTrie()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.nextKey(K)"""
        return object.__wrap(super(__AbstractPatriciaTrie, self).nextKey(arg0))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def selectValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractPatriciaTrie.selectValue(K)"""
        return object.__wrap(super(__AbstractPatriciaTrie, self).selectValue(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.previousKey(K)"""
        return object.__wrap(super(__AbstractPatriciaTrie, self).previousKey(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void java.util.AbstractMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractMap, self).putAll(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.AbstractBitwiseTrie.toString()"""
        return str.__wrap(super(AbstractBitwiseTrie, self).toString())

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
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.trie.PatriciaTrie(java.util.Map<? extends java.lang.String, ? extends E>)"""
        val = __PatriciaTrie(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.lastKey()"""
        return object.__wrap(super(AbstractPatriciaTrie, self).lastKey())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.trie.AbstractBitwiseTrie
import java.util.AbstractMap as __AbstractMap
__AbstractMap = __AbstractMap
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.SequencedCollection as SequencedCollection
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import org.apache.commons.collections4.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.Trie as __Trie
__Trie = __Trie
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.trie.AbstractBitwiseTrie as __AbstractBitwiseTrie
__AbstractBitwiseTrie = __AbstractBitwiseTrie
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class AbstractBitwiseTrie(ABC):
    """org.apache.commons.collections4.trie.AbstractBitwiseTrie"""
 
    @staticmethod
    def __wrap(java_value: __AbstractBitwiseTrie) -> 'AbstractBitwiseTrie':
        return AbstractBitwiseTrie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractBitwiseTrie):
        """
        Dynamic initializer for AbstractBitwiseTrie.
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
    def remove(self, arg0: object) -> object:
        """public V java.util.AbstractMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMap, self).remove(arg0))

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @overload
    def get(self, arg0: object) -> object:
        """public V java.util.AbstractMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMap, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).containsValue(arg0))

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap.hashCode()"""
        return int.__wrap(super(AbstractMap, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def tailMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.tailMap(K)"""
        pass

    @abstractmethod
    def prefixMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> org.apache.commons.collections4.Trie.prefixMap(K)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def firstKey(self, ):
        """public abstract K java.util.SortedMap.firstKey()"""
        pass

    @abstractmethod
    def lastKey(self, ):
        """public abstract K java.util.SortedMap.lastKey()"""
        pass

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int java.util.AbstractMap.size()"""
        return int.__wrap(super(AbstractMap, self).size())

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void java.util.AbstractMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractMap, self).putAll(arg0)

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).containsKey(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.AbstractBitwiseTrie.toString()"""
        return str.__wrap(super(AbstractBitwiseTrie, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> java.util.AbstractMap.values()"""
        return 'Collection'.__wrap(super(AbstractMap, self).values())

    @abstractmethod
    def headMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.headMap(K)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def subMap(self, arg0: object, arg1: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.subMap(K,K)"""
        pass

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractMap.isEmpty()"""
        return bool.__wrap(super(AbstractMap, self).isEmpty())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> java.util.AbstractMap.keySet()"""
        return 'Set'.__wrap(super(AbstractMap, self).keySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V java.util.AbstractMap.put(K,V)"""
        return object.__wrap(super(__AbstractMap, self).put(arg0, arg1))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

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

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super K> java.util.SortedMap.comparator()"""
        pass

    @override
    @overload
    def clear(self):
        """public void java.util.AbstractMap.clear()"""
        super(AbstractMap, self).clear()

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.AbstractMap.entrySet()"""
        pass