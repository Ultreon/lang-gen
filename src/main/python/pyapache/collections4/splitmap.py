from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator as _AbstractIterableGetMapDecorator
_AbstractIterableGetMapDecorator = _AbstractIterableGetMapDecorator
import java.util.Collection as Collection
import org.apache.commons.collections4.splitmap.TransformedSplitMap as _TransformedSplitMap
_TransformedSplitMap = _TransformedSplitMap
from builtins import object
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
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedSplitMap():
    """org.apache.commons.collections4.splitmap.TransformedSplitMap"""
 
    @staticmethod
    def _wrap(java_value: _TransformedSplitMap) -> 'TransformedSplitMap':
        return TransformedSplitMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedSplitMap):
        """
        Dynamic initializer for TransformedSplitMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedSplitMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedSplitMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractIterableGetMapDecorator, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.size()"""
        return int._wrap(super(AbstractIterableGetMapDecorator, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractIterableGetMapDecorator, self).remove(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractIterableGetMapDecorator, self).entrySet())

    @staticmethod
    @overload
    def transformingMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedSplitMap':
        """public static <J,K,U,V> org.apache.commons.collections4.splitmap.TransformedSplitMap<J, K, U, V> org.apache.commons.collections4.splitmap.TransformedSplitMap.transformingMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super J, ? extends K>,org.apache.commons.collections4.Transformer<? super U, ? extends V>)"""
        return TransformedSplitMap._wrap(_TransformedSplitMap.transformingMap(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.splitmap.TransformedSplitMap.putAll(java.util.Map<? extends J, ? extends U>)"""
        super(_TransformedSplitMap, self).putAll(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.hashCode()"""
        return int._wrap(super(AbstractIterableGetMapDecorator, self).hashCode())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableGetMapDecorator, self).mapIterator())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractIterableGetMapDecorator, self).get(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractIterableGetMapDecorator, self).isEmpty())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.toString()"""
        return str._wrap(super(AbstractIterableGetMapDecorator, self).toString())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.splitmap.TransformedSplitMap.put(J,U)"""
        return object._wrap(super(_TransformedSplitMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractIterableGetMapDecorator, self).values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.splitmap.TransformedSplitMap.clear()"""
        super(TransformedSplitMap, self).clear()

 
 
 
# CLASS: org.apache.commons.collections4.splitmap.TransformedSplitMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator as _AbstractIterableGetMapDecorator
_AbstractIterableGetMapDecorator = _AbstractIterableGetMapDecorator
import java.util.Collection as Collection
import org.apache.commons.collections4.splitmap.TransformedSplitMap as _TransformedSplitMap
_TransformedSplitMap = _TransformedSplitMap
from builtins import object
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
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedSplitMap():
    """org.apache.commons.collections4.splitmap.TransformedSplitMap"""
 
    @staticmethod
    def _wrap(java_value: _TransformedSplitMap) -> 'TransformedSplitMap':
        return TransformedSplitMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedSplitMap):
        """
        Dynamic initializer for TransformedSplitMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedSplitMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedSplitMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractIterableGetMapDecorator, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.size()"""
        return int._wrap(super(AbstractIterableGetMapDecorator, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractIterableGetMapDecorator, self).remove(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractIterableGetMapDecorator, self).entrySet())

    @staticmethod
    @overload
    def transformingMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedSplitMap':
        """public static <J,K,U,V> org.apache.commons.collections4.splitmap.TransformedSplitMap<J, K, U, V> org.apache.commons.collections4.splitmap.TransformedSplitMap.transformingMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super J, ? extends K>,org.apache.commons.collections4.Transformer<? super U, ? extends V>)"""
        return TransformedSplitMap._wrap(_TransformedSplitMap.transformingMap(arg0, arg1, arg2))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.splitmap.TransformedSplitMap.putAll(java.util.Map<? extends J, ? extends U>)"""
        super(_TransformedSplitMap, self).putAll(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.hashCode()"""
        return int._wrap(super(AbstractIterableGetMapDecorator, self).hashCode())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableGetMapDecorator, self).mapIterator())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractIterableGetMapDecorator, self).get(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractIterableGetMapDecorator, self).isEmpty())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.toString()"""
        return str._wrap(super(AbstractIterableGetMapDecorator, self).toString())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.splitmap.TransformedSplitMap.put(J,U)"""
        return object._wrap(super(_TransformedSplitMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractIterableGetMapDecorator, self).values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.splitmap.TransformedSplitMap.clear()"""
        super(TransformedSplitMap, self).clear()

 
 
 
# CLASS: org.apache.commons.collections4.splitmap.TransformedSplitMap 
 
 
# CLASS: org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator as _AbstractIterableGetMapDecorator
_AbstractIterableGetMapDecorator = _AbstractIterableGetMapDecorator
import java.util.Collection as Collection
from builtins import object
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
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractIterableGetMapDecorator():
    """org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractIterableGetMapDecorator) -> 'AbstractIterableGetMapDecorator':
        return AbstractIterableGetMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractIterableGetMapDecorator):
        """
        Dynamic initializer for AbstractIterableGetMapDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractIterableGetMapDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractIterableGetMapDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsValue(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.keySet()"""
        return 'Set'._wrap(super(AbstractIterableGetMapDecorator, self).keySet())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.size()"""
        return int._wrap(super(AbstractIterableGetMapDecorator, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractIterableGetMapDecorator, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.remove(java.lang.Object)"""
        return object._wrap(super(_AbstractIterableGetMapDecorator, self).remove(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.entrySet()"""
        return 'Set'._wrap(super(AbstractIterableGetMapDecorator, self).entrySet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.hashCode()"""
        return int._wrap(super(AbstractIterableGetMapDecorator, self).hashCode())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.mapIterator()"""
        return 'collections4.MapIterator'._wrap(super(AbstractIterableGetMapDecorator, self).mapIterator())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.get(java.lang.Object)"""
        return object._wrap(super(_AbstractIterableGetMapDecorator, self).get(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.isEmpty()"""
        return bool._wrap(super(AbstractIterableGetMapDecorator, self).isEmpty())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.toString()"""
        return str._wrap(super(AbstractIterableGetMapDecorator, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator.values()"""
        return 'Collection'._wrap(super(AbstractIterableGetMapDecorator, self).values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.splitmap.AbstractIterableGetMapDecorator(java.util.Map<K, V>)"""
        val = _AbstractIterableGetMapDecorator(arg0)
        self.__wrapper = val