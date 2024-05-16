from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator as _AbstractMultiValuedMapDecorator
_AbstractMultiValuedMapDecorator = _AbstractMultiValuedMapDecorator
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
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMultiValuedMapDecorator():
    """org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMultiValuedMapDecorator) -> 'AbstractMultiValuedMapDecorator':
        return AbstractMultiValuedMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMultiValuedMapDecorator):
        """
        Dynamic initializer for AbstractMultiValuedMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMultiValuedMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMultiValuedMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).putAll(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).putAll(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMapDecorator, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMapDecorator, self).hashCode())

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.asMap()"""
        return 'Map'._wrap(super(AbstractMultiValuedMapDecorator, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMapDecorator, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsKey(arg0))

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.get(K)"""
        return 'Collection'._wrap(super(_AbstractMultiValuedMapDecorator, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.toString()"""
        return str._wrap(super(AbstractMultiValuedMapDecorator, self).toString())

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.entries()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMapDecorator, self).entries())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsMapping(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.clear()"""
        super(AbstractMultiValuedMapDecorator, self).clear()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).putAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.size()"""
        return int._wrap(super(AbstractMultiValuedMapDecorator, self).size())

    @overload
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.remove(java.lang.Object)"""
        return 'Collection'._wrap(super(_AbstractMultiValuedMapDecorator, self).remove(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).equals(arg0))

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
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keys()"""
        return 'collections4.MultiSet'._wrap(super(AbstractMultiValuedMapDecorator, self).keys())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMultiValuedMapDecorator, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractMultiValuedMapDecorator, self).mapIterator())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).removeMapping(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.put(K,V)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).put(arg0, arg1))

 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator as _AbstractMultiValuedMapDecorator
_AbstractMultiValuedMapDecorator = _AbstractMultiValuedMapDecorator
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
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMultiValuedMapDecorator():
    """org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMultiValuedMapDecorator) -> 'AbstractMultiValuedMapDecorator':
        return AbstractMultiValuedMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMultiValuedMapDecorator):
        """
        Dynamic initializer for AbstractMultiValuedMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMultiValuedMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMultiValuedMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).putAll(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).putAll(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMapDecorator, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMapDecorator, self).hashCode())

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.asMap()"""
        return 'Map'._wrap(super(AbstractMultiValuedMapDecorator, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMapDecorator, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsKey(arg0))

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.get(K)"""
        return 'Collection'._wrap(super(_AbstractMultiValuedMapDecorator, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.toString()"""
        return str._wrap(super(AbstractMultiValuedMapDecorator, self).toString())

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.entries()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMapDecorator, self).entries())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsMapping(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.clear()"""
        super(AbstractMultiValuedMapDecorator, self).clear()

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).putAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.size()"""
        return int._wrap(super(AbstractMultiValuedMapDecorator, self).size())

    @overload
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.remove(java.lang.Object)"""
        return 'Collection'._wrap(super(_AbstractMultiValuedMapDecorator, self).remove(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).equals(arg0))

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
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keys()"""
        return 'collections4.MultiSet'._wrap(super(AbstractMultiValuedMapDecorator, self).keys())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMultiValuedMapDecorator, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractMultiValuedMapDecorator, self).mapIterator())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).removeMapping(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.put(K,V)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).put(arg0, arg1))

 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractMultiValuedMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as _AbstractMultiValuedMap
_AbstractMultiValuedMap = _AbstractMultiValuedMap
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMultiValuedMap():
    """org.apache.commons.collections4.multimap.AbstractMultiValuedMap"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMultiValuedMap) -> 'AbstractMultiValuedMap':
        return AbstractMultiValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMultiValuedMap):
        """
        Dynamic initializer for AbstractMultiValuedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMultiValuedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMultiValuedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).equals(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).entries())

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.get(K)"""
        return 'Collection'._wrap(super(_AbstractMultiValuedMap, self).get(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsKey(arg0))

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'._wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMap, self).hashCode())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int._wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'._wrap(super(AbstractMultiValuedMap, self).keySet())

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'._wrap(super(AbstractMultiValuedMap, self).keys())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str._wrap(super(AbstractMultiValuedMap, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMap, self).isEmpty())

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
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.remove(java.lang.Object)"""
        return 'Collection'._wrap(super(_AbstractMultiValuedMap, self).remove(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).put(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.multimap.HashSetValuedHashMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.apache.commons.collections4.multimap.AbstractSetValuedMap as _AbstractSetValuedMap
_AbstractSetValuedMap = _AbstractSetValuedMap
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.multimap.HashSetValuedHashMap as _HashSetValuedHashMap
_HashSetValuedHashMap = _HashSetValuedHashMap
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as _AbstractMultiValuedMap
_AbstractMultiValuedMap = _AbstractMultiValuedMap
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashSetValuedHashMap():
    """org.apache.commons.collections4.multimap.HashSetValuedHashMap"""
 
    @staticmethod
    def _wrap(java_value: _HashSetValuedHashMap) -> 'HashSetValuedHashMap':
        return HashSetValuedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashSetValuedHashMap):
        """
        Dynamic initializer for HashSetValuedHashMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashSetValuedHashMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashSetValuedHashMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).equals(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap(int)"""
        val = _HashSetValuedHashMap(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap()"""
        val = _HashSetValuedHashMap()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap(int,int)"""
        val = _HashSetValuedHashMap(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).entries())

    @overload
    def remove(self, arg0: object) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.multimap.AbstractSetValuedMap.remove(java.lang.Object)"""
        return 'Set'._wrap(super(_AbstractSetValuedMap, self).remove(arg0))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap(java.util.Map<? extends K, ? extends V>)"""
        val = _HashSetValuedHashMap(arg0)
        self.__wrapper = val

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsKey(arg0))

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'._wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: object) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.multimap.AbstractSetValuedMap.get(K)"""
        return 'Set'._wrap(super(_AbstractSetValuedMap, self).get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMap, self).hashCode())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap()"""
        val = _HashSetValuedHashMap()
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int._wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @overload
    def __init__(self, arg0: 'MultiValuedMap'):
        """public org.apache.commons.collections4.multimap.HashSetValuedHashMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        val = _HashSetValuedHashMap(arg0)
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'._wrap(super(AbstractMultiValuedMap, self).keySet())

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'._wrap(super(AbstractMultiValuedMap, self).keys())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str._wrap(super(AbstractMultiValuedMap, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMap, self).isEmpty())

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
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).put(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.multimap.ArrayListValuedHashMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as _AbstractMultiValuedMap
_AbstractMultiValuedMap = _AbstractMultiValuedMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import org.apache.commons.collections4.multimap.ArrayListValuedHashMap as _ArrayListValuedHashMap
_ArrayListValuedHashMap = _ArrayListValuedHashMap
import java.lang.Integer as _int
import org.apache.commons.collections4.multimap.AbstractListValuedMap as _AbstractListValuedMap
_AbstractListValuedMap = _AbstractListValuedMap
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayListValuedHashMap():
    """org.apache.commons.collections4.multimap.ArrayListValuedHashMap"""
 
    @staticmethod
    def _wrap(java_value: _ArrayListValuedHashMap) -> 'ArrayListValuedHashMap':
        return ArrayListValuedHashMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayListValuedHashMap):
        """
        Dynamic initializer for ArrayListValuedHashMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayListValuedHashMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayListValuedHashMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).equals(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @overload
    def trimToSize(self):
        """public void org.apache.commons.collections4.multimap.ArrayListValuedHashMap.trimToSize()"""
        super(ArrayListValuedHashMap, self).trimToSize()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).entries())

    @overload
    def remove(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.remove(java.lang.Object)"""
        return 'List'._wrap(super(_AbstractListValuedMap, self).remove(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsKey(arg0))

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap()"""
        val = _ArrayListValuedHashMap()
        self.__wrapper = val

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'._wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap()"""
        val = _ArrayListValuedHashMap()
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(java.util.Map<? extends K, ? extends V>)"""
        val = _ArrayListValuedHashMap(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(int,int)"""
        val = _ArrayListValuedHashMap(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMap, self).hashCode())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int._wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def __init__(self, arg0: 'MultiValuedMap'):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        val = _ArrayListValuedHashMap(arg0)
        self.__wrapper = val

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'._wrap(super(AbstractMultiValuedMap, self).keySet())

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'._wrap(super(AbstractMultiValuedMap, self).keys())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str._wrap(super(AbstractMultiValuedMap, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMap, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.get(K)"""
        return 'List'._wrap(super(_AbstractListValuedMap, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.multimap.ArrayListValuedHashMap(int)"""
        val = _ArrayListValuedHashMap(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).put(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator as _AbstractMultiValuedMapDecorator
_AbstractMultiValuedMapDecorator = _AbstractMultiValuedMapDecorator
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
import org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap as _UnmodifiableMultiValuedMap
_UnmodifiableMultiValuedMap = _UnmodifiableMultiValuedMap
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableMultiValuedMap():
    """org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableMultiValuedMap) -> 'UnmodifiableMultiValuedMap':
        return UnmodifiableMultiValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableMultiValuedMap):
        """
        Dynamic initializer for UnmodifiableMultiValuedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableMultiValuedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableMultiValuedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_UnmodifiableMultiValuedMap, self).putAll(arg0))

    @overload
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.remove(java.lang.Object)"""
        return 'Collection'._wrap(super(_UnmodifiableMultiValuedMap, self).remove(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMapDecorator, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMapDecorator, self).hashCode())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(UnmodifiableMultiValuedMap, self).mapIterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.values()"""
        return 'Collection'._wrap(super(UnmodifiableMultiValuedMap, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.entries()"""
        return 'Collection'._wrap(super(UnmodifiableMultiValuedMap, self).entries())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsKey(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.put(K,V)"""
        return bool._wrap(super(_UnmodifiableMultiValuedMap, self).put(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.toString()"""
        return str._wrap(super(AbstractMultiValuedMapDecorator, self).toString())

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_UnmodifiableMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.asMap()"""
        return 'Map'._wrap(super(UnmodifiableMultiValuedMap, self).asMap())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsMapping(arg0, arg1))

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.keys()"""
        return 'collections4.MultiSet'._wrap(super(UnmodifiableMultiValuedMap, self).keys())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.get(K)"""
        return 'Collection'._wrap(super(_UnmodifiableMultiValuedMap, self).get(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.clear()"""
        super(UnmodifiableMultiValuedMap, self).clear()

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_UnmodifiableMultiValuedMap, self).putAll(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableMultiValuedMap(arg0: 'MultiValuedMap') -> 'UnmodifiableMultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap<K, V> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.unmodifiableMultiValuedMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return UnmodifiableMultiValuedMap._wrap(_UnmodifiableMultiValuedMap.unmodifiableMultiValuedMap(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.size()"""
        return int._wrap(super(AbstractMultiValuedMapDecorator, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).equals(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.keySet()"""
        return 'Set'._wrap(super(UnmodifiableMultiValuedMap, self).keySet())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.UnmodifiableMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractListValuedMap
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as _AbstractMultiValuedMap
_AbstractMultiValuedMap = _AbstractMultiValuedMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.multimap.AbstractListValuedMap as _AbstractListValuedMap
_AbstractListValuedMap = _AbstractListValuedMap
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractListValuedMap():
    """org.apache.commons.collections4.multimap.AbstractListValuedMap"""
 
    @staticmethod
    def _wrap(java_value: _AbstractListValuedMap) -> 'AbstractListValuedMap':
        return AbstractListValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractListValuedMap):
        """
        Dynamic initializer for AbstractListValuedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractListValuedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractListValuedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).equals(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).entries())

    @overload
    def remove(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.remove(java.lang.Object)"""
        return 'List'._wrap(super(_AbstractListValuedMap, self).remove(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsKey(arg0))

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'._wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMap, self).hashCode())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int._wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'._wrap(super(AbstractMultiValuedMap, self).keySet())

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'._wrap(super(AbstractMultiValuedMap, self).keys())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str._wrap(super(AbstractMultiValuedMap, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMap, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: object) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.multimap.AbstractListValuedMap.get(K)"""
        return 'List'._wrap(super(_AbstractListValuedMap, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).put(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.multimap.TransformedMultiValuedMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator as _AbstractMultiValuedMapDecorator
_AbstractMultiValuedMapDecorator = _AbstractMultiValuedMapDecorator
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import org.apache.commons.collections4.multimap.TransformedMultiValuedMap as _TransformedMultiValuedMap
_TransformedMultiValuedMap = _TransformedMultiValuedMap
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedMultiValuedMap():
    """org.apache.commons.collections4.multimap.TransformedMultiValuedMap"""
 
    @staticmethod
    def _wrap(java_value: _TransformedMultiValuedMap) -> 'TransformedMultiValuedMap':
        return TransformedMultiValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedMultiValuedMap):
        """
        Dynamic initializer for TransformedMultiValuedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedMultiValuedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedMultiValuedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMapDecorator, self).isEmpty())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMapDecorator, self).hashCode())

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.asMap()"""
        return 'Map'._wrap(super(AbstractMultiValuedMapDecorator, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMapDecorator, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsKey(arg0))

    @overload
    def get(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.get(K)"""
        return 'Collection'._wrap(super(_AbstractMultiValuedMapDecorator, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.toString()"""
        return str._wrap(super(AbstractMultiValuedMapDecorator, self).toString())

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.TransformedMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_TransformedMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.entries()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMapDecorator, self).entries())

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).containsMapping(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.clear()"""
        super(AbstractMultiValuedMapDecorator, self).clear()

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.TransformedMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_TransformedMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.TransformedMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_TransformedMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.size()"""
        return int._wrap(super(AbstractMultiValuedMapDecorator, self).size())

    @overload
    def remove(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.remove(java.lang.Object)"""
        return 'Collection'._wrap(super(_AbstractMultiValuedMapDecorator, self).remove(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.TransformedMultiValuedMap.put(K,V)"""
        return bool._wrap(super(_TransformedMultiValuedMap, self).put(arg0, arg1))

    @staticmethod
    @overload
    def transformedMap(arg0: 'MultiValuedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.multimap.TransformedMultiValuedMap<K, V> org.apache.commons.collections4.multimap.TransformedMultiValuedMap.transformedMap(org.apache.commons.collections4.MultiValuedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMultiValuedMap._wrap(_TransformedMultiValuedMap.transformedMap(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keys()"""
        return 'collections4.MultiSet'._wrap(super(AbstractMultiValuedMapDecorator, self).keys())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractMultiValuedMapDecorator, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractMultiValuedMapDecorator, self).mapIterator())

    @staticmethod
    @overload
    def transformingMap(arg0: 'MultiValuedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.multimap.TransformedMultiValuedMap<K, V> org.apache.commons.collections4.multimap.TransformedMultiValuedMap.transformingMap(org.apache.commons.collections4.MultiValuedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMultiValuedMap._wrap(_TransformedMultiValuedMap.transformingMap(arg0, arg1, arg2))

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMapDecorator.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMapDecorator, self).removeMapping(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.multimap.AbstractSetValuedMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.multimap.AbstractSetValuedMap as _AbstractSetValuedMap
_AbstractSetValuedMap = _AbstractSetValuedMap
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.collections4.MultiSet as _MultiSet
_MultiSet = _MultiSet
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import org.apache.commons.collections4.MapIterator as _MapIterator
_MapIterator = _MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import org.apache.commons.collections4.multimap.AbstractMultiValuedMap as _AbstractMultiValuedMap
_AbstractMultiValuedMap = _AbstractMultiValuedMap
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractSetValuedMap():
    """org.apache.commons.collections4.multimap.AbstractSetValuedMap"""
 
    @staticmethod
    def _wrap(java_value: _AbstractSetValuedMap) -> 'AbstractSetValuedMap':
        return AbstractSetValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractSetValuedMap):
        """
        Dynamic initializer for AbstractSetValuedMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractSetValuedMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractSetValuedMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).equals(arg0))

    @overload
    def putAll(self, arg0: object, arg1: 'Iterable') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MultiValuedMap') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def entries(self) -> 'Collection':
        """public java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.entries()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).entries())

    @overload
    def remove(self, arg0: object) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.multimap.AbstractSetValuedMap.remove(java.lang.Object)"""
        return 'Set'._wrap(super(_AbstractSetValuedMap, self).remove(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsKey(arg0))

    @overload
    def containsMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsMapping(arg0, arg1))

    @override
    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.asMap()"""
        return 'Map'._wrap(super(AbstractMultiValuedMap, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).containsValue(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: object) -> 'Set':
        """public java.util.Set<V> org.apache.commons.collections4.multimap.AbstractSetValuedMap.get(K)"""
        return 'Set'._wrap(super(_AbstractSetValuedMap, self).get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.hashCode()"""
        return int._wrap(super(AbstractMultiValuedMap, self).hashCode())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.values()"""
        return 'Collection'._wrap(super(AbstractMultiValuedMap, self).values())

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).removeMapping(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.multimap.AbstractMultiValuedMap.size()"""
        return int._wrap(super(AbstractMultiValuedMap, self).size())

    @overload
    def putAll(self, arg0: 'Map') -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).putAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.multimap.AbstractMultiValuedMap.clear()"""
        super(AbstractMultiValuedMap, self).clear()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keySet()"""
        return 'Set'._wrap(super(AbstractMultiValuedMap, self).keySet())

    @override
    @overload
    def keys(self) -> 'collections4.MultiSet':
        """public org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.keys()"""
        return 'collections4.MultiSet'._wrap(super(AbstractMultiValuedMap, self).keys())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.multimap.AbstractMultiValuedMap.toString()"""
        return str._wrap(super(AbstractMultiValuedMap, self).toString())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.multimap.AbstractMultiValuedMap.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractMultiValuedMap, self).mapIterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.isEmpty()"""
        return bool._wrap(super(AbstractMultiValuedMap, self).isEmpty())

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
    def put(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.multimap.AbstractMultiValuedMap.put(K,V)"""
        return bool._wrap(super(_AbstractMultiValuedMap, self).put(arg0, arg1))