from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as __AbstractMultiValuedMap
__AbstractMultiValuedMap = __AbstractMultiValuedMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.multimap.ArrayListValuedHashMap as __ArrayListValuedHashMap
__ArrayListValuedHashMap = __ArrayListValuedHashMap
from builtins import bool
import org.apache.commons.collections4.multimap.AbstractListValuedMap as __AbstractListValuedMap
__AbstractListValuedMap = __AbstractListValuedMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import java.lang.Iterable as Iterable
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class ArrayListValuedHashMap(__AbstractListValuedMap, AbstractListValuedMap, __Serializable, Serializable):
    """org.apache.commons.collections4.multimap.ArrayListValuedHashMap"""
 
    @staticmethod
    def __wrap(java_value: __ArrayListValuedHashMap) -> 'ArrayListValuedHashMap':
        return ArrayListValuedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayListValuedHashMap):
        """
        Dynamic initializer for ArrayListValuedHashMap.
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
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsKey(arg0))

    @overload
    def __init__(self, arg0: 'MultiValuedMap'):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        val = __ArrayListValuedHashMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap()"""
        val = __ArrayListValuedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap()"""
        val = __ArrayListValuedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def trimToSize(self):
        """public void org.apache.commons.collections4.multimap.ArrayListValuedHashMap.trimToSize()"""
        super(ArrayListValuedHashMap, self).trimToSize()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).equals(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsValue(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def get(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.get(K)"""
        return 'List'.__wrap(super(__AbstractListValuedMap, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(int,int)"""
        val = __ArrayListValuedHashMap(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).entries())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'.__wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str.__wrap(super(AbstractMultiValuedMap, self).toString())

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).hashCode())

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(java.util.Map<? extends K, ? extends V>)"""
        val = __ArrayListValuedHashMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMap, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.remove(java.lang.Object)"""
        return 'List'.__wrap(super(__AbstractListValuedMap, self).remove(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractMultiValuedMap, self).keySet())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(int)"""
        val = __ArrayListValuedHashMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'.__wrap(super(AbstractMultiValuedMap, self).keys())

 
 
 
# CLASS: org.apache.commons.collections4.multimap.ArrayListValuedHashMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as __AbstractMultiValuedMap
__AbstractMultiValuedMap = __AbstractMultiValuedMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.multimap.ArrayListValuedHashMap as __ArrayListValuedHashMap
__ArrayListValuedHashMap = __ArrayListValuedHashMap
from builtins import bool
import org.apache.commons.collections4.multimap.AbstractListValuedMap as __AbstractListValuedMap
__AbstractListValuedMap = __AbstractListValuedMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import java.lang.Iterable as Iterable
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class ArrayListValuedHashMap(__AbstractListValuedMap, AbstractListValuedMap, __Serializable, Serializable):
    """org.apache.commons.collections4.multimap.ArrayListValuedHashMap"""
 
    @staticmethod
    def __wrap(java_value: __ArrayListValuedHashMap) -> 'ArrayListValuedHashMap':
        return ArrayListValuedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayListValuedHashMap):
        """
        Dynamic initializer for ArrayListValuedHashMap.
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
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsKey(arg0))

    @overload
    def __init__(self, arg0: 'MultiValuedMap'):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        val = __ArrayListValuedHashMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap()"""
        val = __ArrayListValuedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap()"""
        val = __ArrayListValuedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def trimToSize(self):
        """public void org.apache.commons.collections4.multimap.ArrayListValuedHashMap.trimToSize()"""
        super(ArrayListValuedHashMap, self).trimToSize()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).equals(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsValue(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def get(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.get(K)"""
        return 'List'.__wrap(super(__AbstractListValuedMap, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(int,int)"""
        val = __ArrayListValuedHashMap(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).entries())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'.__wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str.__wrap(super(AbstractMultiValuedMap, self).toString())

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).hashCode())

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(java.util.Map<? extends K, ? extends V>)"""
        val = __ArrayListValuedHashMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMap, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.remove(java.lang.Object)"""
        return 'List'.__wrap(super(__AbstractListValuedMap, self).remove(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractMultiValuedMap, self).keySet())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(int)"""
        val = __ArrayListValuedHashMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'.__wrap(super(AbstractMultiValuedMap, self).keys())

 
 
 
# CLASS: org.apache.commons.collections4.multimap.ArrayListValuedHashMap 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractMultiValuedMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as __AbstractMultiValuedMap
__AbstractMultiValuedMap = __AbstractMultiValuedMap
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class AbstractMultiValuedMap(ABC, pyapache.__MultiValuedMap, collections4.MultiValuedMap):
    """org.apache.commons.collections4.multimap.AbstractMultiValuedMap"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMultiValuedMap) -> 'AbstractMultiValuedMap':
        return AbstractMultiValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMultiValuedMap):
        """
        Dynamic initializer for AbstractMultiValuedMap.
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
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsKey(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).equals(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.remove(java.lang.Object)"""
        return 'Collection'.__wrap(super(__AbstractMultiValuedMap, self).remove(arg0))

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.get(K)"""
        return 'Collection'.__wrap(super(__AbstractMultiValuedMap, self).get(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsValue(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).entries())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'.__wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str.__wrap(super(AbstractMultiValuedMap, self).toString())

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).hashCode())

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMap, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractMultiValuedMap, self).keySet())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'.__wrap(super(AbstractMultiValuedMap, self).keys()) 
 
 
# CLASS: org.apache.commons.collections4.multimap.HashSetValuedHashMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.multimap.AbstractSetValuedMap as __AbstractSetValuedMap
__AbstractSetValuedMap = __AbstractSetValuedMap
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as __AbstractMultiValuedMap
__AbstractMultiValuedMap = __AbstractMultiValuedMap
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.multimap.HashSetValuedHashMap as __HashSetValuedHashMap
__HashSetValuedHashMap = __HashSetValuedHashMap
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class HashSetValuedHashMap(__AbstractSetValuedMap, AbstractSetValuedMap, __Serializable, Serializable):
    """org.apache.commons.collections4.multimap.HashSetValuedHashMap"""
 
    @staticmethod
    def __wrap(java_value: __HashSetValuedHashMap) -> 'HashSetValuedHashMap':
        return HashSetValuedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashSetValuedHashMap):
        """
        Dynamic initializer for HashSetValuedHashMap.
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
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsKey(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).equals(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap(java.util.Map<? extends K, ? extends V>)"""
        val = __HashSetValuedHashMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsValue(arg0))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap(int)"""
        val = __HashSetValuedHashMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @overload
    def remove(self, arg0: object) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.multimap.AbstractSetValuedMap.remove(java.lang.Object)"""
        return 'Set'.__wrap(super(__AbstractSetValuedMap, self).remove(arg0))

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).entries())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap()"""
        val = __HashSetValuedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'.__wrap(super(AbstractMultiValuedMap, self).asMap())

    @overload
    def get(self, arg0: object) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.multimap.AbstractSetValuedMap.get(K)"""
        return 'Set'.__wrap(super(__AbstractSetValuedMap, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str.__wrap(super(AbstractMultiValuedMap, self).toString())

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).hashCode())

    @overload
    def __init__(self, arg0: 'MultiValuedMap'):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        val = __HashSetValuedHashMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMap, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractMultiValuedMap, self).keySet())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap(int,int)"""
        val = __HashSetValuedHashMap(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'.__wrap(super(AbstractMultiValuedMap, self).keys())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap()"""
        val = __HashSetValuedHashMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractListValuedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as __AbstractMultiValuedMap
__AbstractMultiValuedMap = __AbstractMultiValuedMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.multimap.AbstractListValuedMap as __AbstractListValuedMap
__AbstractListValuedMap = __AbstractListValuedMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import java.lang.Iterable as Iterable
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class AbstractListValuedMap(ABC, __AbstractMultiValuedMap, AbstractMultiValuedMap, pyapache.__ListValuedMap, collections4.ListValuedMap):
    """org.apache.commons.collections4.multimap.AbstractListValuedMap"""
 
    @staticmethod
    def __wrap(java_value: __AbstractListValuedMap) -> 'AbstractListValuedMap':
        return AbstractListValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractListValuedMap):
        """
        Dynamic initializer for AbstractListValuedMap.
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
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsKey(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).equals(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsValue(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def get(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.get(K)"""
        return 'List'.__wrap(super(__AbstractListValuedMap, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).entries())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'.__wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str.__wrap(super(AbstractMultiValuedMap, self).toString())

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).hashCode())

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMap, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.remove(java.lang.Object)"""
        return 'List'.__wrap(super(__AbstractListValuedMap, self).remove(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractMultiValuedMap, self).keySet())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'.__wrap(super(AbstractMultiValuedMap, self).keys()) 
 
 
# CLASS: org.apache.commons.collections4.multimap.TransformedMultiValuedMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator as __AbstractMultiValuedMapDecorator
__AbstractMultiValuedMapDecorator = __AbstractMultiValuedMapDecorator
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import org.apache.commons.collections4.multimap.TransformedMultiValuedMap as __TransformedMultiValuedMap
__TransformedMultiValuedMap = __TransformedMultiValuedMap
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class TransformedMultiValuedMap(__AbstractMultiValuedMapDecorator, AbstractMultiValuedMapDecorator):
    """org.apache.commons.collections4.multimap.TransformedMultiValuedMap"""
 
    @staticmethod
    def __wrap(java_value: __TransformedMultiValuedMap) -> 'TransformedMultiValuedMap':
        return TransformedMultiValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedMultiValuedMap):
        """
        Dynamic initializer for TransformedMultiValuedMap.
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
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.TransformedMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__TransformedMultiValuedMap, self).putAll(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMapDecorator, self).hashCode())

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.asMap()"""
        return 'Map'.__wrap(super(AbstractMultiValuedMapDecorator, self).asMap())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractMultiValuedMapDecorator, self).mapIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.remove(java.lang.Object)"""
        return 'Collection'.__wrap(super(__AbstractMultiValuedMapDecorator, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMapDecorator, self).isEmpty())

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keys()"""
        return 'collections4.MultiSet'.__wrap(super(AbstractMultiValuedMapDecorator, self).keys())

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.TransformedMultiValuedMap.put(K,V)"""
        return bool.__wrap(super(__TransformedMultiValuedMap, self).put(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.toString()"""
        return str.__wrap(super(AbstractMultiValuedMapDecorator, self).toString())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsMapping(arg0, arg1))

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.TransformedMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__TransformedMultiValuedMap, self).putAll(arg0))

    @staticmethod
    @overload
    def transformingMap(arg0: 'MultiValuedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.multimap.TransformedMultiValuedMap<K, V> org.apache.commons.collections4.multimap.TransformedMultiValuedMap.transformingMap(org.apache.commons.collections4.MultiValuedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMultiValuedMap.__wrap(__TransformedMultiValuedMap.transformingMap(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMapDecorator, self).values())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.clear()"""
        super(AbstractMultiValuedMapDecorator, self).clear()

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).removeMapping(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.get(K)"""
        return 'Collection'.__wrap(super(__AbstractMultiValuedMapDecorator, self).get(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.size()"""
        return int.__wrap(super(AbstractMultiValuedMapDecorator, self).size())

    @staticmethod
    @overload
    def transformedMap(arg0: 'MultiValuedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.multimap.TransformedMultiValuedMap<K, V> org.apache.commons.collections4.multimap.TransformedMultiValuedMap.transformedMap(org.apache.commons.collections4.MultiValuedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMultiValuedMap.__wrap(__TransformedMultiValuedMap.transformedMap(arg0, arg1, arg2))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMultiValuedMapDecorator, self).keySet())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.entries()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMapDecorator, self).entries())

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.TransformedMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__TransformedMultiValuedMap, self).putAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap as __UnmodifiableMultiValuedMap
__UnmodifiableMultiValuedMap = __UnmodifiableMultiValuedMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator as __AbstractMultiValuedMapDecorator
__AbstractMultiValuedMapDecorator = __AbstractMultiValuedMapDecorator
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class UnmodifiableMultiValuedMap(__AbstractMultiValuedMapDecorator, AbstractMultiValuedMapDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableMultiValuedMap) -> 'UnmodifiableMultiValuedMap':
        return UnmodifiableMultiValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableMultiValuedMap):
        """
        Dynamic initializer for UnmodifiableMultiValuedMap.
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
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__UnmodifiableMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.values()"""
        return 'Collection'.__wrap(super(UnmodifiableMultiValuedMap, self).values())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMapDecorator, self).hashCode())

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.entries()"""
        return 'Collection'.__wrap(super(UnmodifiableMultiValuedMap, self).entries())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(UnmodifiableMultiValuedMap, self).mapIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMapDecorator, self).isEmpty())

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__UnmodifiableMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.toString()"""
        return str.__wrap(super(AbstractMultiValuedMapDecorator, self).toString())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsMapping(arg0, arg1))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__UnmodifiableMultiValuedMap, self).putAll(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.keySet()"""
        return 'Set'.__wrap(super(UnmodifiableMultiValuedMap, self).keySet())

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.asMap()"""
        return 'Map'.__wrap(super(UnmodifiableMultiValuedMap, self).asMap())

    @staticmethod
    @overload
    def unmodifiableMultiValuedMap(arg0: 'MultiValuedMap') -> 'UnmodifiableMultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap<K, V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.unmodifiableMultiValuedMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return UnmodifiableMultiValuedMap.__wrap(__UnmodifiableMultiValuedMap.unmodifiableMultiValuedMap(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.put(K,V)"""
        return bool.__wrap(super(__UnmodifiableMultiValuedMap, self).put(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsKey(arg0))

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.get(K)"""
        return 'Collection'.__wrap(super(__UnmodifiableMultiValuedMap, self).get(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.clear()"""
        super(UnmodifiableMultiValuedMap, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).equals(arg0))

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
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.size()"""
        return int.__wrap(super(AbstractMultiValuedMapDecorator, self).size())

    @overload
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.remove(java.lang.Object)"""
        return 'Collection'.__wrap(super(__UnmodifiableMultiValuedMap, self).remove(arg0))

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableMultiValuedMap, self).removeMapping(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.keys()"""
        return 'collections4.MultiSet'.__wrap(super(UnmodifiableMultiValuedMap, self).keys()) 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractSetValuedMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.multimap.AbstractSetValuedMap as __AbstractSetValuedMap
__AbstractSetValuedMap = __AbstractSetValuedMap
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as __AbstractMultiValuedMap
__AbstractMultiValuedMap = __AbstractMultiValuedMap
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class AbstractSetValuedMap(ABC, __AbstractMultiValuedMap, AbstractMultiValuedMap, pyapache.__SetValuedMap, collections4.SetValuedMap):
    """org.apache.commons.collections4.multimap.AbstractSetValuedMap"""
 
    @staticmethod
    def __wrap(java_value: __AbstractSetValuedMap) -> 'AbstractSetValuedMap':
        return AbstractSetValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractSetValuedMap):
        """
        Dynamic initializer for AbstractSetValuedMap.
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
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsKey(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).equals(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsValue(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @overload
    def remove(self, arg0: object) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.multimap.AbstractSetValuedMap.remove(java.lang.Object)"""
        return 'Set'.__wrap(super(__AbstractSetValuedMap, self).remove(arg0))

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMap, self).entries())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'.__wrap(super(AbstractMultiValuedMap, self).asMap())

    @overload
    def get(self, arg0: object) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.multimap.AbstractSetValuedMap.get(K)"""
        return 'Set'.__wrap(super(__AbstractSetValuedMap, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str.__wrap(super(AbstractMultiValuedMap, self).toString())

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMap, self).hashCode())

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMap, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractMultiValuedMap, self).keySet())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'.__wrap(super(AbstractMultiValuedMap, self).keys()) 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator as __AbstractMultiValuedMapDecorator
__AbstractMultiValuedMapDecorator = __AbstractMultiValuedMapDecorator
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class AbstractMultiValuedMapDecorator(ABC, pyapache.__MultiValuedMap, collections4.MultiValuedMap, __Serializable, Serializable):
    """org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMultiValuedMapDecorator) -> 'AbstractMultiValuedMapDecorator':
        return AbstractMultiValuedMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMultiValuedMapDecorator):
        """
        Dynamic initializer for AbstractMultiValuedMapDecorator.
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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMultiValuedMapDecorator, self).hashCode())

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.asMap()"""
        return 'Map'.__wrap(super(AbstractMultiValuedMapDecorator, self).asMap())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractMultiValuedMapDecorator, self).mapIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).putAll(arg0))

    @overload
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.remove(java.lang.Object)"""
        return 'Collection'.__wrap(super(__AbstractMultiValuedMapDecorator, self).remove(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMultiValuedMapDecorator, self).isEmpty())

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keys()"""
        return 'collections4.MultiSet'.__wrap(super(AbstractMultiValuedMapDecorator, self).keys())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.toString()"""
        return str.__wrap(super(AbstractMultiValuedMapDecorator, self).toString())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsMapping(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.put(K,V)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).put(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMapDecorator, self).values())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.clear()"""
        super(AbstractMultiValuedMapDecorator, self).clear()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).putAll(arg0))

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).removeMapping(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.get(K)"""
        return 'Collection'.__wrap(super(__AbstractMultiValuedMapDecorator, self).get(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.size()"""
        return int.__wrap(super(AbstractMultiValuedMapDecorator, self).size())

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).putAll(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMultiValuedMapDecorator, self).keySet())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMultiValuedMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.entries()"""
        return 'Collection'.__wrap(super(AbstractMultiValuedMapDecorator, self).entries())