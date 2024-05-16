from __future__ import annotations
from overload import overload


 
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.trie.PatriciaTrie as _PatriciaTrie
_PatriciaTrie = _PatriciaTrie
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
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
import org.apache.commons.collections4.trie.AbstractPatriciaTrie as _AbstractPatriciaTrie
_AbstractPatriciaTrie = _AbstractPatriciaTrie
from pyquantum_helper import override
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import java.util.AbstractMap as _AbstractMap
_AbstractMap = _AbstractMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.trie.AbstractBitwiseTrie as _AbstractBitwiseTrie
_AbstractBitwiseTrie = _AbstractBitwiseTrie
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PatriciaTrie():
    """org.apache.commons.collections4.trie.PatriciaTrie"""
 
    @staticmethod
    def _wrap(java_value: _PatriciaTrie) -> 'PatriciaTrie':
        return PatriciaTrie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PatriciaTrie):
        """
        Dynamic initializer for PatriciaTrie.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PatriciaTrie__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PatriciaTrie__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractPatriciaTrie.put(K,V)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).put(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractMap.isEmpty()"""
        return bool._wrap(super(AbstractMap, self).isEmpty())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.nextKey(K)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).nextKey(arg0))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.lastKey()"""
        return object._wrap(super(AbstractPatriciaTrie, self).lastKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.PatriciaTrie()"""
        val = _PatriciaTrie()
        self.__wrapper = val

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.headMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractPatriciaTrie, self).headMap(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

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

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.trie.PatriciaTrie(java.util.Map<? extends java.lang.String, ? extends E>)"""
        val = _PatriciaTrie(arg0)
        self.__wrapper = val

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).equals(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.tailMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractPatriciaTrie, self).tailMap(arg0))

    @overload
    def selectValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractPatriciaTrie.selectValue(K)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).selectValue(arg0))

    @overload
    def prefixMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.prefixMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractPatriciaTrie, self).prefixMap(arg0))

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

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_AbstractPatriciaTrie, self).subMap(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.AbstractBitwiseTrie.toString()"""
        return str._wrap(super(AbstractBitwiseTrie, self).toString())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void java.util.AbstractMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMap, self).putAll(arg0)

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).containsValue(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

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
    def __init__(self):
        """public org.apache.commons.collections4.trie.PatriciaTrie()"""
        val = _PatriciaTrie()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.previousKey(K)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).previousKey(arg0))

    @overload
    def select(self, arg0: object) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.select(K)"""
        return 'Entry.Map$Entry'._wrap(super(_AbstractPatriciaTrie, self).select(arg0))

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
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.firstKey()"""
        return object._wrap(super(AbstractPatriciaTrie, self).firstKey())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def selectKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.selectKey(K)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).selectKey(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap.hashCode()"""
        return int._wrap(super(AbstractMap, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

 
 
 
# CLASS: org.apache.commons.collections4.trie.PatriciaTrie
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.trie.PatriciaTrie as _PatriciaTrie
_PatriciaTrie = _PatriciaTrie
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
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
import org.apache.commons.collections4.trie.AbstractPatriciaTrie as _AbstractPatriciaTrie
_AbstractPatriciaTrie = _AbstractPatriciaTrie
from pyquantum_helper import override
import java.util.SequencedCollection as _SequencedCollection
_SequencedCollection = _SequencedCollection
import java.lang.Object as _object
import java.util.AbstractMap as _AbstractMap
_AbstractMap = _AbstractMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.trie.AbstractBitwiseTrie as _AbstractBitwiseTrie
_AbstractBitwiseTrie = _AbstractBitwiseTrie
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PatriciaTrie():
    """org.apache.commons.collections4.trie.PatriciaTrie"""
 
    @staticmethod
    def _wrap(java_value: _PatriciaTrie) -> 'PatriciaTrie':
        return PatriciaTrie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PatriciaTrie):
        """
        Dynamic initializer for PatriciaTrie.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PatriciaTrie__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PatriciaTrie__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractPatriciaTrie.put(K,V)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).put(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractMap.isEmpty()"""
        return bool._wrap(super(AbstractMap, self).isEmpty())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.nextKey(K)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).nextKey(arg0))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.lastKey()"""
        return object._wrap(super(AbstractPatriciaTrie, self).lastKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.PatriciaTrie()"""
        val = _PatriciaTrie()
        self.__wrapper = val

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.headMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractPatriciaTrie, self).headMap(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

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

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.trie.PatriciaTrie(java.util.Map<? extends java.lang.String, ? extends E>)"""
        val = _PatriciaTrie(arg0)
        self.__wrapper = val

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).equals(arg0))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.tailMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractPatriciaTrie, self).tailMap(arg0))

    @overload
    def selectValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractPatriciaTrie.selectValue(K)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).selectValue(arg0))

    @overload
    def prefixMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.prefixMap(K)"""
        return 'SortedMap'._wrap(super(_AbstractPatriciaTrie, self).prefixMap(arg0))

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

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_AbstractPatriciaTrie, self).subMap(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.AbstractBitwiseTrie.toString()"""
        return str._wrap(super(AbstractBitwiseTrie, self).toString())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void java.util.AbstractMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMap, self).putAll(arg0)

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).containsValue(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

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
    def __init__(self):
        """public org.apache.commons.collections4.trie.PatriciaTrie()"""
        val = _PatriciaTrie()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.previousKey(K)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).previousKey(arg0))

    @overload
    def select(self, arg0: object) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.trie.AbstractPatriciaTrie.select(K)"""
        return 'Entry.Map$Entry'._wrap(super(_AbstractPatriciaTrie, self).select(arg0))

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
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.firstKey()"""
        return object._wrap(super(AbstractPatriciaTrie, self).firstKey())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @overload
    def selectKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.AbstractPatriciaTrie.selectKey(K)"""
        return object._wrap(super(_AbstractPatriciaTrie, self).selectKey(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap.hashCode()"""
        return int._wrap(super(AbstractMap, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0)

 
 
 
# CLASS: org.apache.commons.collections4.trie.PatriciaTrie 
 
 
# CLASS: org.apache.commons.collections4.trie.KeyAnalyzer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.trie.KeyAnalyzer as _KeyAnalyzer
_KeyAnalyzer = _KeyAnalyzer
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeyAnalyzer():
    """org.apache.commons.collections4.trie.KeyAnalyzer"""
 
    @staticmethod
    def _wrap(java_value: _KeyAnalyzer) -> 'KeyAnalyzer':
        return KeyAnalyzer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyAnalyzer):
        """
        Dynamic initializer for KeyAnalyzer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyAnalyzer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyAnalyzer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def __init__(self):
        """public org.apache.commons.collections4.trie.KeyAnalyzer()"""
        val = _KeyAnalyzer()
        self.__wrapper = val

    @abstractmethod
    def bitIndex(self, arg0: object, arg1: int, arg2: int, arg3: object, arg4: int, arg5: int):
        """public abstract int org.apache.commons.collections4.trie.KeyAnalyzer.bitIndex(K,int,int,K,int,int)"""
        pass

    @abstractmethod
    def isBitSet(self, arg0: object, arg1: int, arg2: int):
        """public abstract boolean org.apache.commons.collections4.trie.KeyAnalyzer.isBitSet(K,int,int)"""
        pass

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def bitsPerElement(self, ):
        """public abstract int org.apache.commons.collections4.trie.KeyAnalyzer.bitsPerElement()"""
        pass

    @overload
    def compare(self, arg0: object, arg1: object) -> int:
        """public int org.apache.commons.collections4.trie.KeyAnalyzer.compare(K,K)"""
        return int._wrap(super(_KeyAnalyzer, self).compare(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def isPrefix(self, arg0: object, arg1: int, arg2: int, arg3: object):
        """public abstract boolean org.apache.commons.collections4.trie.KeyAnalyzer.isPrefix(K,int,int,K)"""
        pass

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.trie.KeyAnalyzer()"""
        val = _KeyAnalyzer()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.trie.AbstractPatriciaTrie as _AbstractPatriciaTrie_TrieEntry
_TrieEntry = _AbstractPatriciaTrie_TrieEntry.TrieEntry
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
from builtins import bool
import org.apache.commons.collections4.trie.AbstractBitwiseTrie as _AbstractBitwiseTrie_BasicEntry
_BasicEntry = _AbstractBitwiseTrie_BasicEntry.BasicEntry
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TrieEntry():
    """org.apache.commons.collections4.trie.AbstractPatriciaTrie.TrieEntry"""
 
    @staticmethod
    def _wrap(java_value: _TrieEntry) -> 'TrieEntry':
        return TrieEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TrieEntry):
        """
        Dynamic initializer for TrieEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TrieEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TrieEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.getValue()"""
        return object._wrap(super(BasicEntry, self).getValue())

    @overload
    def isInternalNode(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isInternalNode()"""
        return bool._wrap(super(TrieEntry, self).isInternalNode())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: int):
        """public org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry(K,V,int)"""
        val = _TrieEntry(arg0, arg1, _int.valueOf(arg2))
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.toString()"""
        return str._wrap(super(TrieEntry, self).toString())

    @overload
    def isExternalNode(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isExternalNode()"""
        return bool._wrap(super(TrieEntry, self).isExternalNode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.equals(java.lang.Object)"""
        return bool._wrap(super(_BasicEntry, self).equals(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.setValue(V)"""
        return object._wrap(super(_BasicEntry, self).setValue(arg0))

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
    def setKeyValue(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.setKeyValue(K,V)"""
        return object._wrap(super(_BasicEntry, self).setKeyValue(arg0, arg1))

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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.AbstractPatriciaTrie$TrieEntry.isEmpty()"""
        return bool._wrap(super(TrieEntry, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.hashCode()"""
        return int._wrap(super(BasicEntry, self).hashCode())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.trie.AbstractBitwiseTrie$BasicEntry.getKey()"""
        return object._wrap(super(BasicEntry, self).getKey()) 
 
 
# CLASS: org.apache.commons.collections4.trie.AbstractBitwiseTrie
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.SequencedSet as _SequencedSet
_SequencedSet = _SequencedSet
from abc import abstractmethod, ABC
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
import java.util.AbstractMap as _AbstractMap
_AbstractMap = _AbstractMap
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.collections4.OrderedMap as _OrderedMap
_OrderedMap = _OrderedMap
import org.apache.commons.collections4.trie.AbstractBitwiseTrie as _AbstractBitwiseTrie
_AbstractBitwiseTrie = _AbstractBitwiseTrie
import java.util.function.Function as Function
import org.apache.commons.collections4.Trie as _Trie
_Trie = _Trie
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractBitwiseTrie():
    """org.apache.commons.collections4.trie.AbstractBitwiseTrie"""
 
    @staticmethod
    def _wrap(java_value: _AbstractBitwiseTrie) -> 'AbstractBitwiseTrie':
        return AbstractBitwiseTrie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractBitwiseTrie):
        """
        Dynamic initializer for AbstractBitwiseTrie.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractBitwiseTrie__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractBitwiseTrie__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractMap.isEmpty()"""
        return bool._wrap(super(AbstractMap, self).isEmpty())

    @override
    @overload
    def size(self) -> int:
        """public int java.util.AbstractMap.size()"""
        return int._wrap(super(AbstractMap, self).size())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
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

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollLastEntry())

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).equals(arg0))

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
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @abstractmethod
    def firstKey(self, ):
        """public abstract K java.util.SortedMap.firstKey()"""
        pass

    @overload
    def get(self, arg0: object) -> object:
        """public V java.util.AbstractMap.get(java.lang.Object)"""
        return object._wrap(super(_AbstractMap, self).get(arg0))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K java.util.SortedMap.lastKey()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @overload
    def remove(self, arg0: object) -> object:
        """public V java.util.AbstractMap.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractMap, self).remove(arg0))

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.AbstractBitwiseTrie.toString()"""
        return str._wrap(super(AbstractBitwiseTrie, self).toString())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> java.util.AbstractMap.keySet()"""
        return 'Set'._wrap(super(AbstractMap, self).keySet())

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
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @abstractmethod
    def headMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.headMap(K)"""
        pass

    @abstractmethod
    def subMap(self, arg0: object, arg1: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.subMap(K,K)"""
        pass

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
    def values(self) -> 'Collection':
        """public java.util.Collection<V> java.util.AbstractMap.values()"""
        return 'Collection'._wrap(super(AbstractMap, self).values())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).containsKey(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void java.util.AbstractMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_AbstractMap, self).putAll(arg0)

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V java.util.AbstractMap.put(K,V)"""
        return object._wrap(super(_AbstractMap, self).put(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMap, self).containsValue(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super K> java.util.SortedMap.comparator()"""
        pass

    @override
    @overload
    def clear(self):
        """public void java.util.AbstractMap.clear()"""
        super(AbstractMap, self).clear()

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'._wrap(super(SequencedMap, self).sequencedValues())

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.AbstractMap.entrySet()"""
        pass

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap.hashCode()"""
        return int._wrap(super(AbstractMap, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.trie.UnmodifiableTrie
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
import org.apache.commons.collections4.trie.UnmodifiableTrie as _UnmodifiableTrie
_UnmodifiableTrie = _UnmodifiableTrie
import org.apache.commons.collections4.Trie as _Trie
_Trie = _Trie
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableTrie():
    """org.apache.commons.collections4.trie.UnmodifiableTrie"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableTrie) -> 'UnmodifiableTrie':
        return UnmodifiableTrie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableTrie):
        """
        Dynamic initializer for UnmodifiableTrie.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableTrie__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableTrie__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Trie'):
        """public org.apache.commons.collections4.trie.UnmodifiableTrie(org.apache.commons.collections4.Trie<K, ? extends V>)"""
        val = _UnmodifiableTrie(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.subMap(K,K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableTrie, self).subMap(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.trie.UnmodifiableTrie.toString()"""
        return str._wrap(super(UnmodifiableTrie, self).toString())

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.trie.UnmodifiableTrie.firstKey()"""
        return object._wrap(super(UnmodifiableTrie, self).firstKey())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.UnmodifiableTrie.containsKey(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableTrie, self).containsKey(arg0))

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
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.UnmodifiableTrie.get(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableTrie, self).get(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.trie.UnmodifiableTrie.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(_UnmodifiableTrie, self).putAll(arg0)

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.trie.UnmodifiableTrie.remove(java.lang.Object)"""
        return object._wrap(super(_UnmodifiableTrie, self).remove(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.trie.UnmodifiableTrie.comparator()"""
        return 'Comparator'._wrap(super(UnmodifiableTrie, self).comparator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.UnmodifiableTrie.equals(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableTrie, self).equals(arg0))

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
        """public K org.apache.commons.collections4.trie.UnmodifiableTrie.lastKey()"""
        return object._wrap(super(UnmodifiableTrie, self).lastKey())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.trie.UnmodifiableTrie.clear()"""
        super(UnmodifiableTrie, self).clear()

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.trie.UnmodifiableTrie.values()"""
        return 'Collection'._wrap(super(UnmodifiableTrie, self).values())

    @staticmethod
    @overload
    def unmodifiableTrie(arg0: 'Trie') -> 'collections4.Trie':
        """public static <K,V> org.apache.commons.collections4.Trie<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.unmodifiableTrie(org.apache.commons.collections4.Trie<K, ? extends V>)"""
        return collections4.Trie._wrap(_UnmodifiableTrie.unmodifiableTrie(arg0))

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
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.trie.UnmodifiableTrie.entrySet()"""
        return 'Set'._wrap(super(UnmodifiableTrie, self).entrySet())

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
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.mapIterator()"""
        return 'collections4.OrderedMapIterator'._wrap(super(UnmodifiableTrie, self).mapIterator())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object._wrap(super(_SortedMap, self).putFirst(arg0, arg1))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.UnmodifiableTrie.previousKey(K)"""
        return object._wrap(super(_UnmodifiableTrie, self).previousKey(arg0))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.headMap(K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableTrie, self).headMap(arg0))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'._wrap(super(SequencedMap, self).sequencedKeySet())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.trie.UnmodifiableTrie.put(K,V)"""
        return object._wrap(super(_UnmodifiableTrie, self).put(arg0, arg1))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.trie.UnmodifiableTrie.nextKey(K)"""
        return object._wrap(super(_UnmodifiableTrie, self).nextKey(arg0))

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.trie.UnmodifiableTrie.isEmpty()"""
        return bool._wrap(super(UnmodifiableTrie, self).isEmpty())

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'._wrap(super(SequencedMap, self).firstEntry())

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
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.trie.UnmodifiableTrie.keySet()"""
        return 'Set'._wrap(super(UnmodifiableTrie, self).keySet())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.trie.UnmodifiableTrie.hashCode()"""
        return int._wrap(super(UnmodifiableTrie, self).hashCode())

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
    def prefixMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.prefixMap(K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableTrie, self).prefixMap(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.trie.UnmodifiableTrie.containsValue(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableTrie, self).containsValue(arg0))

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

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.trie.UnmodifiableTrie.tailMap(K)"""
        return 'SortedMap'._wrap(super(_UnmodifiableTrie, self).tailMap(arg0))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.trie.UnmodifiableTrie.size()"""
        return int._wrap(super(UnmodifiableTrie, self).size())