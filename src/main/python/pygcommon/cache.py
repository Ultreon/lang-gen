from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import com.google.common.cache.ForwardingLoadingCache as __ForwardingLoadingCache
__ForwardingLoadingCache = __ForwardingLoadingCache
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
import com.google.common.cache.ForwardingCache as __ForwardingCache
__ForwardingCache = __ForwardingCache
import java.util.function.Function as __Function
__Function = __Function
from builtins import object
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
import java.util.concurrent.ConcurrentMap as __ConcurrentMap
__ConcurrentMap = __ConcurrentMap
from builtins import int
 
class ForwardingLoadingCache(ABC):
    """com.google.common.cache.ForwardingLoadingCache"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingLoadingCache) -> 'ForwardingLoadingCache':
        return ForwardingLoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingLoadingCache):
        """
        Dynamic initializer for ForwardingLoadingCache.
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
    def apply(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.apply(K)"""
        return object.__wrap(super(__ForwardingLoadingCache, self).apply(key))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingCache, self).get(key, valueLoader))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def refresh(self, key: object):
        """public void com.google.common.cache.ForwardingLoadingCache.refresh(K)"""
        super(__ForwardingLoadingCache, self).refresh(key)

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__ForwardingCache, self).putAll(m)

    @overload
    def getAll(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingLoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__ForwardingLoadingCache, self).getAll(keys))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getUnchecked(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.getUnchecked(K)"""
        return object.__wrap(super(__ForwardingLoadingCache, self).getUnchecked(key))

    @overload
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object.__wrap(super(__ForwardingCache, self).getIfPresent(key))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(__ForwardingCache, self).invalidate(key)

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(__ForwardingCache, self).put(key, value)

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'.__wrap(super(ForwardingCache, self).asMap())

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
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'.__wrap(super(ForwardingCache, self).stats())

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int.__wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(__ForwardingCache, self).invalidateAll(keys)

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingLoadingCache, self).get(key))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

 
 
 
# CLASS: com.google.common.cache.ForwardingLoadingCache
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import com.google.common.cache.ForwardingLoadingCache as __ForwardingLoadingCache
__ForwardingLoadingCache = __ForwardingLoadingCache
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
import com.google.common.cache.ForwardingCache as __ForwardingCache
__ForwardingCache = __ForwardingCache
import java.util.function.Function as __Function
__Function = __Function
from builtins import object
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
import java.util.concurrent.ConcurrentMap as __ConcurrentMap
__ConcurrentMap = __ConcurrentMap
from builtins import int
 
class ForwardingLoadingCache(ABC):
    """com.google.common.cache.ForwardingLoadingCache"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingLoadingCache) -> 'ForwardingLoadingCache':
        return ForwardingLoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingLoadingCache):
        """
        Dynamic initializer for ForwardingLoadingCache.
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
    def apply(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.apply(K)"""
        return object.__wrap(super(__ForwardingLoadingCache, self).apply(key))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingCache, self).get(key, valueLoader))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def refresh(self, key: object):
        """public void com.google.common.cache.ForwardingLoadingCache.refresh(K)"""
        super(__ForwardingLoadingCache, self).refresh(key)

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__ForwardingCache, self).putAll(m)

    @overload
    def getAll(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingLoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__ForwardingLoadingCache, self).getAll(keys))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getUnchecked(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.getUnchecked(K)"""
        return object.__wrap(super(__ForwardingLoadingCache, self).getUnchecked(key))

    @overload
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object.__wrap(super(__ForwardingCache, self).getIfPresent(key))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(__ForwardingCache, self).invalidate(key)

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(__ForwardingCache, self).put(key, value)

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'.__wrap(super(ForwardingCache, self).asMap())

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
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'.__wrap(super(ForwardingCache, self).stats())

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int.__wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(__ForwardingCache, self).invalidateAll(keys)

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingLoadingCache, self).get(key))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

 
 
 
# CLASS: com.google.common.cache.ForwardingLoadingCache 
 
 
# CLASS: com.google.common.cache.CacheBuilderSpec
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.cache.CacheBuilderSpec as __CacheBuilderSpec
__CacheBuilderSpec = __CacheBuilderSpec
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CacheBuilderSpec():
    """com.google.common.cache.CacheBuilderSpec"""
 
    @staticmethod
    def __wrap(java_value: __CacheBuilderSpec) -> 'CacheBuilderSpec':
        return CacheBuilderSpec(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CacheBuilderSpec):
        """
        Dynamic initializer for CacheBuilderSpec.
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
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.cache.CacheBuilderSpec.equals(java.lang.Object)"""
        return bool.__wrap(super(__CacheBuilderSpec, self).equals(obj))

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

    @staticmethod
    @overload
    def parse(cacheBuilderSpecification: str) -> 'CacheBuilderSpec':
        """public static com.google.common.cache.CacheBuilderSpec com.google.common.cache.CacheBuilderSpec.parse(java.lang.String)"""
        return CacheBuilderSpec.__wrap(__CacheBuilderSpec.parse(cacheBuilderSpecification))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.cache.CacheBuilderSpec.toString()"""
        return str.__wrap(super(CacheBuilderSpec, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.cache.CacheBuilderSpec.hashCode()"""
        return int.__wrap(super(CacheBuilderSpec, self).hashCode())

    @staticmethod
    @overload
    def disableCaching() -> 'CacheBuilderSpec':
        """public static com.google.common.cache.CacheBuilderSpec com.google.common.cache.CacheBuilderSpec.disableCaching()"""
        return CacheBuilderSpec.__wrap(__CacheBuilderSpec.disableCaching())

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
    def toParsableString(self) -> str:
        """public java.lang.String com.google.common.cache.CacheBuilderSpec.toParsableString()"""
        return str.__wrap(super(CacheBuilderSpec, self).toParsableString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.cache.ForwardingCache
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import com.google.common.cache.ForwardingCache as __ForwardingCache
__ForwardingCache = __ForwardingCache
import java.lang.Iterable as Iterable
from builtins import object
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
import java.util.concurrent.ConcurrentMap as __ConcurrentMap
__ConcurrentMap = __ConcurrentMap
from builtins import int
 
class ForwardingCache(ABC):
    """com.google.common.cache.ForwardingCache"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingCache) -> 'ForwardingCache':
        return ForwardingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingCache):
        """
        Dynamic initializer for ForwardingCache.
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
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object.__wrap(super(__ForwardingCache, self).getIfPresent(key))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(__ForwardingCache, self).invalidate(key)

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(__ForwardingCache, self).put(key, value)

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingCache, self).get(key, valueLoader))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'.__wrap(super(ForwardingCache, self).asMap())

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
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'.__wrap(super(ForwardingCache, self).stats())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int.__wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__ForwardingCache, self).putAll(m)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(__ForwardingCache, self).invalidateAll(keys)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.cache.CacheLoader
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygcommon.util import concurrent
except ImportError:
    concurrent = __import_once__("pygcommon.util.concurrent")

import java.util.Map as __Map
__Map = __Map
import java.lang.Iterable as Iterable
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
import java.lang.Long as __long
import com.google.common.cache.CacheLoader as __CacheLoader
__CacheLoader = __CacheLoader
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class CacheLoader(ABC):
    """com.google.common.cache.CacheLoader"""
 
    @staticmethod
    def __wrap(java_value: __CacheLoader) -> 'CacheLoader':
        return CacheLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CacheLoader):
        """
        Dynamic initializer for CacheLoader.
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

    @staticmethod
    @overload
    def from(supplier: 'Supplier') -> 'CacheLoader':
        """public static <V> com.google.common.cache.CacheLoader<java.lang.Object, V> com.google.common.cache.CacheLoader.from(com.google.common.base.Supplier<V>)"""
        return CacheLoader.__wrap(__CacheLoader.from(supplier))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def reload(self, key: object, oldValue: object) -> 'concurrent.ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<V> com.google.common.cache.CacheLoader.reload(K,V) throws java.lang.Exception"""
        return 'concurrent.ListenableFuture'.__wrap(super(__CacheLoader, self).reload(key, oldValue))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def load(self, key: object):
        """public abstract V com.google.common.cache.CacheLoader.load(K) throws java.lang.Exception"""
        pass

    @overload
    def loadAll(self, keys: 'Iterable') -> 'Map':
        """public java.util.Map<K, V> com.google.common.cache.CacheLoader.loadAll(java.lang.Iterable<? extends K>) throws java.lang.Exception"""
        return 'Map'.__wrap(super(__CacheLoader, self).loadAll(keys))

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

    @staticmethod
    @overload
    def from(function: 'Function') -> 'CacheLoader':
        """public static <K,V> com.google.common.cache.CacheLoader<K, V> com.google.common.cache.CacheLoader.from(com.google.common.base.Function<K, V>)"""
        return CacheLoader.__wrap(__CacheLoader.from(function))

    @staticmethod
    @overload
    def asyncReloading(loader: 'CacheLoader', executor: 'Executor') -> 'CacheLoader':
        """public static <K,V> com.google.common.cache.CacheLoader<K, V> com.google.common.cache.CacheLoader.asyncReloading(com.google.common.cache.CacheLoader<K, V>,java.util.concurrent.Executor)"""
        return CacheLoader.__wrap(__CacheLoader.asyncReloading(loader, executor))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.cache.ForwardingLoadingCache$SimpleForwardingLoadingCache
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import com.google.common.cache.ForwardingLoadingCache as __ForwardingLoadingCache
__ForwardingLoadingCache = __ForwardingLoadingCache
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
import com.google.common.cache.ForwardingCache as __ForwardingCache
__ForwardingCache = __ForwardingCache
import java.util.function.Function as __Function
__Function = __Function
from builtins import object
import com.google.common.cache.ForwardingLoadingCache as __ForwardingLoadingCache_SimpleForwardingLoadingCache
__SimpleForwardingLoadingCache = __ForwardingLoadingCache_SimpleForwardingLoadingCache.SimpleForwardingLoadingCache
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
import java.util.concurrent.ConcurrentMap as __ConcurrentMap
__ConcurrentMap = __ConcurrentMap
from builtins import int
 
class SimpleForwardingLoadingCache(ABC):
    """com.google.common.cache.ForwardingLoadingCache.SimpleForwardingLoadingCache"""
 
    @staticmethod
    def __wrap(java_value: __SimpleForwardingLoadingCache) -> 'SimpleForwardingLoadingCache':
        return SimpleForwardingLoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleForwardingLoadingCache):
        """
        Dynamic initializer for SimpleForwardingLoadingCache.
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
    def apply(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.apply(K)"""
        return object.__wrap(super(__ForwardingLoadingCache, self).apply(key))

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingCache, self).get(key, valueLoader))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def refresh(self, key: object):
        """public void com.google.common.cache.ForwardingLoadingCache.refresh(K)"""
        super(__ForwardingLoadingCache, self).refresh(key)

    @overload
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__ForwardingCache, self).putAll(m)

    @overload
    def getAll(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingLoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__ForwardingLoadingCache, self).getAll(keys))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getUnchecked(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.getUnchecked(K)"""
        return object.__wrap(super(__ForwardingLoadingCache, self).getUnchecked(key))

    @overload
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object.__wrap(super(__ForwardingCache, self).getIfPresent(key))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(__ForwardingCache, self).invalidate(key)

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(__ForwardingCache, self).put(key, value)

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'.__wrap(super(ForwardingCache, self).asMap())

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
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'.__wrap(super(ForwardingCache, self).stats())

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int.__wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(__ForwardingCache, self).invalidateAll(keys)

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingLoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingLoadingCache, self).get(key))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0)) 
 
 
# CLASS: com.google.common.cache.CacheLoader$InvalidCacheLoadException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import com.google.common.cache.CacheLoader as __CacheLoader_InvalidCacheLoadException
__InvalidCacheLoadException = __CacheLoader_InvalidCacheLoadException.InvalidCacheLoadException
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidCacheLoadException():
    """com.google.common.cache.CacheLoader.InvalidCacheLoadException"""
 
    @staticmethod
    def __wrap(java_value: __InvalidCacheLoadException) -> 'InvalidCacheLoadException':
        return InvalidCacheLoadException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidCacheLoadException):
        """
        Dynamic initializer for InvalidCacheLoadException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, message: str):
        """public com.google.common.cache.CacheLoader$InvalidCacheLoadException(java.lang.String)"""
        val = __InvalidCacheLoadException(message)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.google.common.cache.RemovalListeners
from builtins import str
import com.google.common.cache.RemovalListeners as __RemovalListeners
__RemovalListeners = __RemovalListeners
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import com.google.common.cache.RemovalListener as __RemovalListener
__RemovalListener = __RemovalListener
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RemovalListeners():
    """com.google.common.cache.RemovalListeners"""
 
    @staticmethod
    def __wrap(java_value: __RemovalListeners) -> 'RemovalListeners':
        return RemovalListeners(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemovalListeners):
        """
        Dynamic initializer for RemovalListeners.
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

    @staticmethod
    @overload
    def asynchronous(listener: 'RemovalListener', executor: 'Executor') -> 'RemovalListener':
        """public static <K,V> com.google.common.cache.RemovalListener<K, V> com.google.common.cache.RemovalListeners.asynchronous(com.google.common.cache.RemovalListener<K, V>,java.util.concurrent.Executor)"""
        return RemovalListener.__wrap(__RemovalListeners.asynchronous(listener, executor))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.cache.CacheBuilder
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.time.Duration as Duration
import com.google.common.cache.Cache as __Cache
__Cache = __Cache
import java.lang.Long as __long
import com.google.common.cache.LoadingCache as __LoadingCache
__LoadingCache = __LoadingCache
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.cache.CacheBuilder as __CacheBuilder
__CacheBuilder = __CacheBuilder
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CacheBuilder():
    """com.google.common.cache.CacheBuilder"""
 
    @staticmethod
    def __wrap(java_value: __CacheBuilder) -> 'CacheBuilder':
        return CacheBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CacheBuilder):
        """
        Dynamic initializer for CacheBuilder.
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
    def concurrencyLevel(self, concurrencyLevel: int) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.concurrencyLevel(int)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).concurrencyLevel(__int.valueOf(concurrencyLevel)))

    @overload
    def softValues(self) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.softValues()"""
        return 'CacheBuilder'.__wrap(super(CacheBuilder, self).softValues())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.cache.CacheBuilder.toString()"""
        return str.__wrap(super(CacheBuilder, self).toString())

    @overload
    def refreshAfterWrite(self, duration: int, unit: 'TimeUnit') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.refreshAfterWrite(long,java.util.concurrent.TimeUnit)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).refreshAfterWrite(__long.valueOf(duration), unit))

    @overload
    def expireAfterAccess(self, duration: int, unit: 'TimeUnit') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.expireAfterAccess(long,java.util.concurrent.TimeUnit)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).expireAfterAccess(__long.valueOf(duration), unit))

    @overload
    def expireAfterWrite(self, duration: int, unit: 'TimeUnit') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.expireAfterWrite(long,java.util.concurrent.TimeUnit)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).expireAfterWrite(__long.valueOf(duration), unit))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def refreshAfterWrite(self, duration: 'Duration') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.refreshAfterWrite(java.time.Duration)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).refreshAfterWrite(duration))

    @overload
    def weakKeys(self) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.weakKeys()"""
        return 'CacheBuilder'.__wrap(super(CacheBuilder, self).weakKeys())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def initialCapacity(self, initialCapacity: int) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.initialCapacity(int)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).initialCapacity(__int.valueOf(initialCapacity)))

    @staticmethod
    @overload
    def from(spec: str) -> 'CacheBuilder':
        """public static com.google.common.cache.CacheBuilder<java.lang.Object, java.lang.Object> com.google.common.cache.CacheBuilder.from(java.lang.String)"""
        return CacheBuilder.__wrap(__CacheBuilder.from(spec))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def build(self) -> 'Cache':
        """public <K1 extends K,V1 extends V> com.google.common.cache.Cache<K1, V1> com.google.common.cache.CacheBuilder.build()"""
        return 'Cache'.__wrap(super(CacheBuilder, self).build())

    @overload
    def build(self, loader: 'CacheLoader') -> 'LoadingCache':
        """public <K1 extends K,V1 extends V> com.google.common.cache.LoadingCache<K1, V1> com.google.common.cache.CacheBuilder.build(com.google.common.cache.CacheLoader<? super K1, V1>)"""
        return 'LoadingCache'.__wrap(super(__CacheBuilder, self).build(loader))

    @overload
    def maximumWeight(self, maximumWeight: int) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.maximumWeight(long)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).maximumWeight(__long.valueOf(maximumWeight)))

    @overload
    def weigher(self, weigher: 'Weigher') -> 'CacheBuilder':
        """public <K1 extends K,V1 extends V> com.google.common.cache.CacheBuilder<K1, V1> com.google.common.cache.CacheBuilder.weigher(com.google.common.cache.Weigher<? super K1, ? super V1>)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).weigher(weigher))

    @overload
    def ticker(self, ticker: 'Ticker') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.ticker(com.google.common.base.Ticker)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).ticker(ticker))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def maximumSize(self, maximumSize: int) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.maximumSize(long)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).maximumSize(__long.valueOf(maximumSize)))

    @overload
    def expireAfterWrite(self, duration: 'Duration') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.expireAfterWrite(java.time.Duration)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).expireAfterWrite(duration))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def expireAfterAccess(self, duration: 'Duration') -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.expireAfterAccess(java.time.Duration)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).expireAfterAccess(duration))

    @overload
    def recordStats(self) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.recordStats()"""
        return 'CacheBuilder'.__wrap(super(CacheBuilder, self).recordStats())

    @overload
    def weakValues(self) -> 'CacheBuilder':
        """public com.google.common.cache.CacheBuilder<K, V> com.google.common.cache.CacheBuilder.weakValues()"""
        return 'CacheBuilder'.__wrap(super(CacheBuilder, self).weakValues())

    @staticmethod
    @overload
    def newBuilder() -> 'CacheBuilder':
        """public static com.google.common.cache.CacheBuilder<java.lang.Object, java.lang.Object> com.google.common.cache.CacheBuilder.newBuilder()"""
        return CacheBuilder.__wrap(__CacheBuilder.newBuilder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def from(spec: 'CacheBuilderSpec') -> 'CacheBuilder':
        """public static com.google.common.cache.CacheBuilder<java.lang.Object, java.lang.Object> com.google.common.cache.CacheBuilder.from(com.google.common.cache.CacheBuilderSpec)"""
        return CacheBuilder.__wrap(__CacheBuilder.from(spec))

    @overload
    def removalListener(self, listener: 'RemovalListener') -> 'CacheBuilder':
        """public <K1 extends K,V1 extends V> com.google.common.cache.CacheBuilder<K1, V1> com.google.common.cache.CacheBuilder.removalListener(com.google.common.cache.RemovalListener<? super K1, ? super V1>)"""
        return 'CacheBuilder'.__wrap(super(__CacheBuilder, self).removalListener(listener)) 
 
 
# CLASS: com.google.common.cache.AbstractCache$StatsCounter
from abc import abstractmethod, ABC
import com.google.common.cache.AbstractCache as __AbstractCache_StatsCounter
__StatsCounter = __AbstractCache_StatsCounter.StatsCounter
 
class StatsCounter(ABC):
    """com.google.common.cache.AbstractCache.StatsCounter"""
 
    @staticmethod
    def __wrap(java_value: __StatsCounter) -> 'StatsCounter':
        return StatsCounter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StatsCounter):
        """
        Dynamic initializer for StatsCounter.
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
    def recordLoadException(self, loadTime: int):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordLoadException(long)"""
        pass

    @abstractmethod
    def recordLoadSuccess(self, loadTime: int):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordLoadSuccess(long)"""
        pass

    @abstractmethod
    def recordEviction(self, ):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordEviction()"""
        pass

    @abstractmethod
    def recordHits(self, count: int):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordHits(int)"""
        pass

    @abstractmethod
    def snapshot(self, ):
        """public abstract com.google.common.cache.CacheStats com.google.common.cache.AbstractCache$StatsCounter.snapshot()"""
        pass

    @abstractmethod
    def recordMisses(self, count: int):
        """public abstract void com.google.common.cache.AbstractCache$StatsCounter.recordMisses(int)"""
        pass 
 
 
# CLASS: com.google.common.cache.ForwardingCache$SimpleForwardingCache
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import com.google.common.cache.ForwardingCache as __ForwardingCache
__ForwardingCache = __ForwardingCache
import java.lang.Iterable as Iterable
import com.google.common.cache.ForwardingCache as __ForwardingCache_SimpleForwardingCache
__SimpleForwardingCache = __ForwardingCache_SimpleForwardingCache.SimpleForwardingCache
from builtins import object
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
import java.util.concurrent.ConcurrentMap as __ConcurrentMap
__ConcurrentMap = __ConcurrentMap
from builtins import int
 
class SimpleForwardingCache(ABC):
    """com.google.common.cache.ForwardingCache.SimpleForwardingCache"""
 
    @staticmethod
    def __wrap(java_value: __SimpleForwardingCache) -> 'SimpleForwardingCache':
        return SimpleForwardingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleForwardingCache):
        """
        Dynamic initializer for SimpleForwardingCache.
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
    def getIfPresent(self, key: object) -> object:
        """public V com.google.common.cache.ForwardingCache.getIfPresent(java.lang.Object)"""
        return object.__wrap(super(__ForwardingCache, self).getIfPresent(key))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.ForwardingCache.invalidate(java.lang.Object)"""
        super(__ForwardingCache, self).invalidate(key)

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.ForwardingCache.put(K,V)"""
        super(__ForwardingCache, self).put(key, value)

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.ForwardingCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingCache, self).get(key, valueLoader))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.ForwardingCache.asMap()"""
        return 'ConcurrentMap'.__wrap(super(ForwardingCache, self).asMap())

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
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.ForwardingCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__ForwardingCache, self).getAllPresent(keys))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.ForwardingCache.invalidateAll()"""
        super(ForwardingCache, self).invalidateAll()

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.ForwardingCache.stats()"""
        return 'CacheStats'.__wrap(super(ForwardingCache, self).stats())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.ForwardingCache.cleanUp()"""
        super(ForwardingCache, self).cleanUp()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.ForwardingCache.size()"""
        return int.__wrap(super(ForwardingCache, self).size())

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.ForwardingCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__ForwardingCache, self).putAll(m)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.ForwardingCache.invalidateAll(java.lang.Iterable<?>)"""
        super(__ForwardingCache, self).invalidateAll(keys)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.cache.AbstractCache
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import java.lang.Iterable as Iterable
from builtins import object
import com.google.common.cache.Cache as __Cache
__Cache = __Cache
from abc import abstractmethod, ABC
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import java.util.concurrent.Callable as Callable
import com.google.common.cache.AbstractCache as __AbstractCache
__AbstractCache = __AbstractCache
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
import java.util.concurrent.ConcurrentMap as __ConcurrentMap
__ConcurrentMap = __ConcurrentMap
from builtins import int
 
class AbstractCache(ABC):
    """com.google.common.cache.AbstractCache"""
 
    @staticmethod
    def __wrap(java_value: __AbstractCache) -> 'AbstractCache':
        return AbstractCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractCache):
        """
        Dynamic initializer for AbstractCache.
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
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.AbstractCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__AbstractCache, self).getAllPresent(keys))

    @abstractmethod
    def getIfPresent(self, key: object):
        """public abstract V com.google.common.cache.Cache.getIfPresent(java.lang.Object)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.AbstractCache.size()"""
        return int.__wrap(super(AbstractCache, self).size())

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.AbstractCache.asMap()"""
        return 'ConcurrentMap'.__wrap(super(AbstractCache, self).asMap())

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.AbstractCache.invalidateAll()"""
        super(AbstractCache, self).invalidateAll()

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.AbstractCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__AbstractCache, self).get(key, valueLoader))

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.AbstractCache.invalidate(java.lang.Object)"""
        super(__AbstractCache, self).invalidate(key)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.AbstractCache.put(K,V)"""
        super(__AbstractCache, self).put(key, value)

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

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.AbstractCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractCache, self).putAll(m)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.AbstractCache.invalidateAll(java.lang.Iterable<?>)"""
        super(__AbstractCache, self).invalidateAll(keys)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.AbstractCache.stats()"""
        return 'CacheStats'.__wrap(super(AbstractCache, self).stats())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.AbstractCache.cleanUp()"""
        super(AbstractCache, self).cleanUp() 
 
 
# CLASS: com.google.common.cache.AbstractCache$SimpleStatsCounter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.cache.AbstractCache as __AbstractCache_SimpleStatsCounter
__SimpleStatsCounter = __AbstractCache_SimpleStatsCounter.SimpleStatsCounter
from builtins import type
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimpleStatsCounter():
    """com.google.common.cache.AbstractCache.SimpleStatsCounter"""
 
    @staticmethod
    def __wrap(java_value: __SimpleStatsCounter) -> 'SimpleStatsCounter':
        return SimpleStatsCounter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleStatsCounter):
        """
        Dynamic initializer for SimpleStatsCounter.
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
    def __init__(self, ):
        """public com.google.common.cache.AbstractCache$SimpleStatsCounter()"""
        val = __SimpleStatsCounter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def incrementBy(self, other: 'StatsCounter'):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.incrementBy(com.google.common.cache.AbstractCache$StatsCounter)"""
        super(__SimpleStatsCounter, self).incrementBy(other)

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

    @override
    @overload
    def recordMisses(self, count: int):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordMisses(int)"""
        super(__SimpleStatsCounter, self).recordMisses(__int.valueOf(count))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def snapshot(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.AbstractCache$SimpleStatsCounter.snapshot()"""
        return 'CacheStats'.__wrap(super(SimpleStatsCounter, self).snapshot())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.common.cache.AbstractCache$SimpleStatsCounter()"""
        val = __SimpleStatsCounter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def recordLoadException(self, loadTime: int):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordLoadException(long)"""
        super(__SimpleStatsCounter, self).recordLoadException(__long.valueOf(loadTime))

    @override
    @overload
    def recordHits(self, count: int):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordHits(int)"""
        super(__SimpleStatsCounter, self).recordHits(__int.valueOf(count))

    @override
    @overload
    def recordLoadSuccess(self, loadTime: int):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordLoadSuccess(long)"""
        super(__SimpleStatsCounter, self).recordLoadSuccess(__long.valueOf(loadTime))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def recordEviction(self):
        """public void com.google.common.cache.AbstractCache$SimpleStatsCounter.recordEviction()"""
        super(SimpleStatsCounter, self).recordEviction() 
 
 
# CLASS: com.google.common.cache.CacheStats
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CacheStats():
    """com.google.common.cache.CacheStats"""
 
    @staticmethod
    def __wrap(java_value: __CacheStats) -> 'CacheStats':
        return CacheStats(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CacheStats):
        """
        Dynamic initializer for CacheStats.
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
    def requestCount(self) -> int:
        """public long com.google.common.cache.CacheStats.requestCount()"""
        return int.__wrap(super(CacheStats, self).requestCount())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.cache.CacheStats.hashCode()"""
        return int.__wrap(super(CacheStats, self).hashCode())

    @overload
    def hitRate(self) -> float:
        """public double com.google.common.cache.CacheStats.hitRate()"""
        return float.__wrap(super(CacheStats, self).hitRate())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def totalLoadTime(self) -> int:
        """public long com.google.common.cache.CacheStats.totalLoadTime()"""
        return int.__wrap(super(CacheStats, self).totalLoadTime())

    @overload
    def loadExceptionRate(self) -> float:
        """public double com.google.common.cache.CacheStats.loadExceptionRate()"""
        return float.__wrap(super(CacheStats, self).loadExceptionRate())

    @overload
    def evictionCount(self) -> int:
        """public long com.google.common.cache.CacheStats.evictionCount()"""
        return int.__wrap(super(CacheStats, self).evictionCount())

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
    def averageLoadPenalty(self) -> float:
        """public double com.google.common.cache.CacheStats.averageLoadPenalty()"""
        return float.__wrap(super(CacheStats, self).averageLoadPenalty())

    @overload
    def __init__(self, hitCount: int, missCount: int, loadSuccessCount: int, loadExceptionCount: int, totalLoadTime: int, evictionCount: int):
        """public com.google.common.cache.CacheStats(long,long,long,long,long,long)"""
        val = __CacheStats(__long.valueOf(hitCount), __long.valueOf(missCount), __long.valueOf(loadSuccessCount), __long.valueOf(loadExceptionCount), __long.valueOf(totalLoadTime), __long.valueOf(evictionCount))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def hitCount(self) -> int:
        """public long com.google.common.cache.CacheStats.hitCount()"""
        return int.__wrap(super(CacheStats, self).hitCount())

    @overload
    def missCount(self) -> int:
        """public long com.google.common.cache.CacheStats.missCount()"""
        return int.__wrap(super(CacheStats, self).missCount())

    @overload
    def missRate(self) -> float:
        """public double com.google.common.cache.CacheStats.missRate()"""
        return float.__wrap(super(CacheStats, self).missRate())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.cache.CacheStats.equals(java.lang.Object)"""
        return bool.__wrap(super(__CacheStats, self).equals(object))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.cache.CacheStats.toString()"""
        return str.__wrap(super(CacheStats, self).toString())

    @overload
    def loadSuccessCount(self) -> int:
        """public long com.google.common.cache.CacheStats.loadSuccessCount()"""
        return int.__wrap(super(CacheStats, self).loadSuccessCount())

    @overload
    def loadExceptionCount(self) -> int:
        """public long com.google.common.cache.CacheStats.loadExceptionCount()"""
        return int.__wrap(super(CacheStats, self).loadExceptionCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def plus(self, other: 'CacheStats') -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.CacheStats.plus(com.google.common.cache.CacheStats)"""
        return 'CacheStats'.__wrap(super(__CacheStats, self).plus(other))

    @overload
    def loadCount(self) -> int:
        """public long com.google.common.cache.CacheStats.loadCount()"""
        return int.__wrap(super(CacheStats, self).loadCount())

    @overload
    def minus(self, other: 'CacheStats') -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.CacheStats.minus(com.google.common.cache.CacheStats)"""
        return 'CacheStats'.__wrap(super(__CacheStats, self).minus(other)) 
 
 
# CLASS: com.google.common.cache.CacheLoader$UnsupportedLoadingOperationException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import com.google.common.cache.CacheLoader as __CacheLoader_UnsupportedLoadingOperationException
__UnsupportedLoadingOperationException = __CacheLoader_UnsupportedLoadingOperationException.UnsupportedLoadingOperationException
from builtins import bool
from builtins import int
 
class UnsupportedLoadingOperationException():
    """com.google.common.cache.CacheLoader.UnsupportedLoadingOperationException"""
 
    @staticmethod
    def __wrap(java_value: __UnsupportedLoadingOperationException) -> 'UnsupportedLoadingOperationException':
        return UnsupportedLoadingOperationException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnsupportedLoadingOperationException):
        """
        Dynamic initializer for UnsupportedLoadingOperationException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.google.common.cache.RemovalNotification
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.google.common.cache.RemovalNotification as __RemovalNotification
__RemovalNotification = __RemovalNotification
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.AbstractMap as __AbstractMap_SimpleImmutableEntry
__SimpleImmutableEntry = __AbstractMap_SimpleImmutableEntry.SimpleImmutableEntry
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.cache.RemovalCause as __RemovalCause
__RemovalCause = __RemovalCause
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RemovalNotification():
    """com.google.common.cache.RemovalNotification"""
 
    @staticmethod
    def __wrap(java_value: __RemovalNotification) -> 'RemovalNotification':
        return RemovalNotification(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemovalNotification):
        """
        Dynamic initializer for RemovalNotification.
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
        """public java.lang.String java.util.AbstractMap$SimpleImmutableEntry.toString()"""
        return str.__wrap(super(SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).toString())

    @staticmethod
    @overload
    def create(key: object, value: object, cause: 'RemovalCause') -> 'RemovalNotification':
        """public static <K,V> com.google.common.cache.RemovalNotification<K, V> com.google.common.cache.RemovalNotification.create(K,V,com.google.common.cache.RemovalCause)"""
        return RemovalNotification.__wrap(__RemovalNotification.create(key, value, cause))

    @override
    @overload
    def getKey(self) -> object:
        """public K java.util.AbstractMap$SimpleImmutableEntry.getKey()"""
        return object.__wrap(super(SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).getKey())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V java.util.AbstractMap$SimpleImmutableEntry.setValue(V)"""
        return object.__wrap(super(__SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).setValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap$SimpleImmutableEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).equals(arg0))

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

    @overload
    def wasEvicted(self) -> bool:
        """public boolean com.google.common.cache.RemovalNotification.wasEvicted()"""
        return bool.__wrap(super(RemovalNotification, self).wasEvicted())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getValue(self) -> object:
        """public V java.util.AbstractMap$SimpleImmutableEntry.getValue()"""
        return object.__wrap(super(SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).getValue())

    @overload
    def getCause(self) -> 'RemovalCause':
        """public com.google.common.cache.RemovalCause com.google.common.cache.RemovalNotification.getCause()"""
        return 'RemovalCause'.__wrap(super(RemovalNotification, self).getCause())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractMap$SimpleImmutableEntry.hashCode()"""
        return int.__wrap(super(SimpleImmutableEntry.AbstractMap$SimpleImmutableEntry, self).hashCode()) 
 
 
# CLASS: com.google.common.cache.RemovalListener
from abc import abstractmethod, ABC
import com.google.common.cache.RemovalListener as __RemovalListener
__RemovalListener = __RemovalListener
 
class RemovalListener(ABC):
    """com.google.common.cache.RemovalListener"""
 
    @staticmethod
    def __wrap(java_value: __RemovalListener) -> 'RemovalListener':
        return RemovalListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemovalListener):
        """
        Dynamic initializer for RemovalListener.
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
    def onRemoval(self, notification: 'RemovalNotification'):
        """public abstract void com.google.common.cache.RemovalListener.onRemoval(com.google.common.cache.RemovalNotification<K, V>)"""
        pass 
 
 
# CLASS: com.google.common.cache.RemovalCause
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.google.common.cache.RemovalCause as __RemovalCause
__RemovalCause = __RemovalCause
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class RemovalCause(ABC):
    """com.google.common.cache.RemovalCause"""
 
    @staticmethod
    def __wrap(java_value: __RemovalCause) -> 'RemovalCause':
        return RemovalCause(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemovalCause):
        """
        Dynamic initializer for RemovalCause.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['RemovalCause']:
        """public static com.google.common.cache.RemovalCause[] com.google.common.cache.RemovalCause.values()"""
        return List[RemovalCause].__wrap(__RemovalCause.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def valueOf(name: str) -> 'RemovalCause':
        """public static com.google.common.cache.RemovalCause com.google.common.cache.RemovalCause.valueOf(java.lang.String)"""
        return RemovalCause.__wrap(__RemovalCause.valueOf(name)) 
 
 
# CLASS: com.google.common.cache.Cache
import java.lang.Iterable as Iterable
import java.util.concurrent.Callable as Callable
import com.google.common.cache.Cache as __Cache
__Cache = __Cache
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class Cache(ABC):
    """com.google.common.cache.Cache"""
 
    @staticmethod
    def __wrap(java_value: __Cache) -> 'Cache':
        return Cache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cache):
        """
        Dynamic initializer for Cache.
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
    def stats(self, ):
        """public abstract com.google.common.cache.CacheStats com.google.common.cache.Cache.stats()"""
        pass

    @abstractmethod
    def invalidate(self, key: object):
        """public abstract void com.google.common.cache.Cache.invalidate(java.lang.Object)"""
        pass

    @abstractmethod
    def invalidateAll(self, keys: 'Iterable'):
        """public abstract void com.google.common.cache.Cache.invalidateAll(java.lang.Iterable<?>)"""
        pass

    @abstractmethod
    def getIfPresent(self, key: object):
        """public abstract V com.google.common.cache.Cache.getIfPresent(java.lang.Object)"""
        pass

    @abstractmethod
    def get(self, key: object, loader: 'Callable'):
        """public abstract V com.google.common.cache.Cache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.Cache.asMap()"""
        pass

    @abstractmethod
    def cleanUp(self, ):
        """public abstract void com.google.common.cache.Cache.cleanUp()"""
        pass

    @abstractmethod
    def putAll(self, m: 'Map'):
        """public abstract void com.google.common.cache.Cache.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def invalidateAll(self, ):
        """public abstract void com.google.common.cache.Cache.invalidateAll()"""
        pass

    @abstractmethod
    def put(self, key: object, value: object):
        """public abstract void com.google.common.cache.Cache.put(K,V)"""
        pass

    @abstractmethod
    def getAllPresent(self, keys: 'Iterable'):
        """public abstract com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.Cache.getAllPresent(java.lang.Iterable<?>)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract long com.google.common.cache.Cache.size()"""
        pass 
 
 
# CLASS: com.google.common.cache.AbstractLoadingCache
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import com.google.common.cache.Cache as __Cache
__Cache = __Cache
from abc import abstractmethod, ABC
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
import com.google.common.cache.LoadingCache as __LoadingCache
__LoadingCache = __LoadingCache
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
import java.util.function.Function as __Function
__Function = __Function
from builtins import object
import com.google.common.cache.CacheStats as __CacheStats
__CacheStats = __CacheStats
import java.lang.Long as __long
import com.google.common.cache.AbstractLoadingCache as __AbstractLoadingCache
__AbstractLoadingCache = __AbstractLoadingCache
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import com.google.common.cache.AbstractCache as __AbstractCache
__AbstractCache = __AbstractCache
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
import java.util.concurrent.ConcurrentMap as __ConcurrentMap
__ConcurrentMap = __ConcurrentMap
from builtins import int
 
class AbstractLoadingCache(ABC):
    """com.google.common.cache.AbstractLoadingCache"""
 
    @staticmethod
    def __wrap(java_value: __AbstractLoadingCache) -> 'AbstractLoadingCache':
        return AbstractLoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractLoadingCache):
        """
        Dynamic initializer for AbstractLoadingCache.
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
    def getAllPresent(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.AbstractCache.getAllPresent(java.lang.Iterable<?>)"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__AbstractCache, self).getAllPresent(keys))

    @override
    @overload
    def size(self) -> int:
        """public long com.google.common.cache.AbstractCache.size()"""
        return int.__wrap(super(AbstractCache, self).size())

    @override
    @overload
    def asMap(self) -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.AbstractCache.asMap()"""
        return 'ConcurrentMap'.__wrap(super(AbstractCache, self).asMap())

    @override
    @overload
    def invalidate(self, key: object):
        """public void com.google.common.cache.AbstractCache.invalidate(java.lang.Object)"""
        super(__AbstractCache, self).invalidate(key)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAll(self, keys: 'Iterable') -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.AbstractLoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        return 'pygcollect.ImmutableMap'.__wrap(super(__AbstractLoadingCache, self).getAll(keys))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.cache.AbstractCache.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractCache, self).putAll(m)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def get(self, key: object):
        """public abstract V com.google.common.cache.LoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def cleanUp(self):
        """public void com.google.common.cache.AbstractCache.cleanUp()"""
        super(AbstractCache, self).cleanUp()

    @abstractmethod
    def getIfPresent(self, key: object):
        """public abstract V com.google.common.cache.Cache.getIfPresent(java.lang.Object)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @override
    @overload
    def invalidateAll(self):
        """public void com.google.common.cache.AbstractCache.invalidateAll()"""
        super(AbstractCache, self).invalidateAll()

    @overload
    def get(self, key: object, valueLoader: 'Callable') -> object:
        """public V com.google.common.cache.AbstractCache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__AbstractCache, self).get(key, valueLoader))

    @override
    @overload
    def put(self, key: object, value: object):
        """public void com.google.common.cache.AbstractCache.put(K,V)"""
        super(__AbstractCache, self).put(key, value)

    @overload
    def getUnchecked(self, key: object) -> object:
        """public V com.google.common.cache.AbstractLoadingCache.getUnchecked(K)"""
        return object.__wrap(super(__AbstractLoadingCache, self).getUnchecked(key))

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
    def refresh(self, key: object):
        """public void com.google.common.cache.AbstractLoadingCache.refresh(K)"""
        super(__AbstractLoadingCache, self).refresh(key)

    @overload
    def apply(self, key: object) -> object:
        """public final V com.google.common.cache.AbstractLoadingCache.apply(K)"""
        return object.__wrap(super(__AbstractLoadingCache, self).apply(key))

    @override
    @overload
    def invalidateAll(self, keys: 'Iterable'):
        """public void com.google.common.cache.AbstractCache.invalidateAll(java.lang.Iterable<?>)"""
        super(__AbstractCache, self).invalidateAll(keys)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def stats(self) -> 'CacheStats':
        """public com.google.common.cache.CacheStats com.google.common.cache.AbstractCache.stats()"""
        return 'CacheStats'.__wrap(super(AbstractCache, self).stats())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0)) 
 
 
# CLASS: com.google.common.cache.Weigher
import com.google.common.cache.Weigher as __Weigher
__Weigher = __Weigher
from abc import abstractmethod, ABC
 
class Weigher(ABC):
    """com.google.common.cache.Weigher"""
 
    @staticmethod
    def __wrap(java_value: __Weigher) -> 'Weigher':
        return Weigher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Weigher):
        """
        Dynamic initializer for Weigher.
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
    def weigh(self, key: object, value: object):
        """public abstract int com.google.common.cache.Weigher.weigh(K,V)"""
        pass 
 
 
# CLASS: com.google.common.cache.LoadingCache
import com.google.common.cache.LoadingCache as __LoadingCache
__LoadingCache = __LoadingCache
from pyquantum_helper import override
import java.lang.Iterable as Iterable
import java.util.function.Function as __Function
__Function = __Function
import com.google.common.base.Function as __Function
__Function = __Function
import java.util.concurrent.Callable as Callable
from abc import abstractmethod, ABC
import com.google.common.cache.Cache as __Cache
__Cache = __Cache
import java.util.function.Function as Function
import java.util.Map as Map
 
class LoadingCache(ABC):
    """com.google.common.cache.LoadingCache"""
 
    @staticmethod
    def __wrap(java_value: __LoadingCache) -> 'LoadingCache':
        return LoadingCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadingCache):
        """
        Dynamic initializer for LoadingCache.
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
    def invalidate(self, key: object):
        """public abstract void com.google.common.cache.Cache.invalidate(java.lang.Object)"""
        pass

    @abstractmethod
    def invalidateAll(self, keys: 'Iterable'):
        """public abstract void com.google.common.cache.Cache.invalidateAll(java.lang.Iterable<?>)"""
        pass

    @abstractmethod
    def getIfPresent(self, key: object):
        """public abstract V com.google.common.cache.Cache.getIfPresent(java.lang.Object)"""
        pass

    @abstractmethod
    def refresh(self, key: object):
        """public abstract void com.google.common.cache.LoadingCache.refresh(K)"""
        pass

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @abstractmethod
    def cleanUp(self, ):
        """public abstract void com.google.common.cache.Cache.cleanUp()"""
        pass

    @abstractmethod
    def putAll(self, m: 'Map'):
        """public abstract void com.google.common.cache.Cache.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.concurrent.ConcurrentMap<K, V> com.google.common.cache.LoadingCache.asMap()"""
        pass

    @abstractmethod
    def getUnchecked(self, key: object):
        """public abstract V com.google.common.cache.LoadingCache.getUnchecked(K)"""
        pass

    @abstractmethod
    def apply(self, key: object):
        """public abstract V com.google.common.cache.LoadingCache.apply(K)"""
        pass

    @abstractmethod
    def invalidateAll(self, ):
        """public abstract void com.google.common.cache.Cache.invalidateAll()"""
        pass

    @abstractmethod
    def getAllPresent(self, keys: 'Iterable'):
        """public abstract com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.Cache.getAllPresent(java.lang.Iterable<?>)"""
        pass

    @abstractmethod
    def getAll(self, keys: 'Iterable'):
        """public abstract com.google.common.collect.ImmutableMap<K, V> com.google.common.cache.LoadingCache.getAll(java.lang.Iterable<? extends K>) throws java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def stats(self, ):
        """public abstract com.google.common.cache.CacheStats com.google.common.cache.Cache.stats()"""
        pass

    @abstractmethod
    def get(self, key: object, loader: 'Callable'):
        """public abstract V com.google.common.cache.Cache.get(K,java.util.concurrent.Callable<? extends V>) throws java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def get(self, key: object):
        """public abstract V com.google.common.cache.LoadingCache.get(K) throws java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def put(self, key: object, value: object):
        """public abstract void com.google.common.cache.Cache.put(K,V)"""
        pass

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

    @abstractmethod
    def size(self, ):
        """public abstract long com.google.common.cache.Cache.size()"""
        pass

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.base.Function.equals(java.lang.Object)"""
        pass