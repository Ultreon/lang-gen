from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.collect.ImmutableSet as __ImmutableSet
__ImmutableSet = __ImmutableSet
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import com.google.common.reflect.ClassPath as __ClassPath
__ClassPath = __ClassPath
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClassPath():
    """com.google.common.reflect.ClassPath"""
 
    @staticmethod
    def __wrap(java_value: __ClassPath) -> 'ClassPath':
        return ClassPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClassPath):
        """
        Dynamic initializer for ClassPath.
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
    def getTopLevelClassesRecursive(self, packageName: str) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClassesRecursive(java.lang.String)"""
        return 'pygcollect.ImmutableSet'.__wrap(super(__ClassPath, self).getTopLevelClassesRecursive(packageName))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getTopLevelClasses(self, packageName: str) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClasses(java.lang.String)"""
        return 'pygcollect.ImmutableSet'.__wrap(super(__ClassPath, self).getTopLevelClasses(packageName))

    @overload
    def getResources(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ResourceInfo> com.google.common.reflect.ClassPath.getResources()"""
        return 'pygcollect.ImmutableSet'.__wrap(super(ClassPath, self).getResources())

    @staticmethod
    @overload
    def from(classloader: 'ClassLoader') -> 'ClassPath':
        """public static com.google.common.reflect.ClassPath com.google.common.reflect.ClassPath.from(java.lang.ClassLoader) throws java.io.IOException"""
        return ClassPath.__wrap(__ClassPath.from(classloader))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAllClasses(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getAllClasses()"""
        return 'pygcollect.ImmutableSet'.__wrap(super(ClassPath, self).getAllClasses())

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
    def getTopLevelClasses(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClasses()"""
        return 'pygcollect.ImmutableSet'.__wrap(super(ClassPath, self).getTopLevelClasses())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.common.reflect.ClassPath
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.collect.ImmutableSet as __ImmutableSet
__ImmutableSet = __ImmutableSet
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import com.google.common.reflect.ClassPath as __ClassPath
__ClassPath = __ClassPath
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClassPath():
    """com.google.common.reflect.ClassPath"""
 
    @staticmethod
    def __wrap(java_value: __ClassPath) -> 'ClassPath':
        return ClassPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClassPath):
        """
        Dynamic initializer for ClassPath.
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
    def getTopLevelClassesRecursive(self, packageName: str) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClassesRecursive(java.lang.String)"""
        return 'pygcollect.ImmutableSet'.__wrap(super(__ClassPath, self).getTopLevelClassesRecursive(packageName))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getTopLevelClasses(self, packageName: str) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClasses(java.lang.String)"""
        return 'pygcollect.ImmutableSet'.__wrap(super(__ClassPath, self).getTopLevelClasses(packageName))

    @overload
    def getResources(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ResourceInfo> com.google.common.reflect.ClassPath.getResources()"""
        return 'pygcollect.ImmutableSet'.__wrap(super(ClassPath, self).getResources())

    @staticmethod
    @overload
    def from(classloader: 'ClassLoader') -> 'ClassPath':
        """public static com.google.common.reflect.ClassPath com.google.common.reflect.ClassPath.from(java.lang.ClassLoader) throws java.io.IOException"""
        return ClassPath.__wrap(__ClassPath.from(classloader))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAllClasses(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getAllClasses()"""
        return 'pygcollect.ImmutableSet'.__wrap(super(ClassPath, self).getAllClasses())

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
    def getTopLevelClasses(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClasses()"""
        return 'pygcollect.ImmutableSet'.__wrap(super(ClassPath, self).getTopLevelClasses())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.common.reflect.ClassPath 
 
 
# CLASS: com.google.common.reflect.MutableTypeToInstanceMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import com.google.common.collect.ForwardingMap as __ForwardingMap
__ForwardingMap = __ForwardingMap
import java.util.Collection as Collection
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.Set as Set
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import com.google.common.reflect.MutableTypeToInstanceMap as __MutableTypeToInstanceMap
__MutableTypeToInstanceMap = __MutableTypeToInstanceMap
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class MutableTypeToInstanceMap():
    """com.google.common.reflect.MutableTypeToInstanceMap"""
 
    @staticmethod
    def __wrap(java_value: __MutableTypeToInstanceMap) -> 'MutableTypeToInstanceMap':
        return MutableTypeToInstanceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableTypeToInstanceMap):
        """
        Dynamic initializer for MutableTypeToInstanceMap.
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
    def hashCode(self) -> int:
        """public int com.google.common.collect.ForwardingMap.hashCode()"""
        return int.__wrap(super(pygcollect.ForwardingMap, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingMap.clear()"""
        super(pygcollect.ForwardingMap, self).clear()

    @overload
    def putInstance(self, type: 'Class', value: object) -> object:
        """public <T extends B> T com.google.common.reflect.MutableTypeToInstanceMap.putInstance(java.lang.Class<T>,T)"""
        return object.__wrap(super(__MutableTypeToInstanceMap, self).putInstance(type, value))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.collect.ForwardingMap.get(java.lang.Object)"""
        return object.__wrap(super(__pygcollect.ForwardingMap, self).get(key))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> com.google.common.collect.ForwardingMap.values()"""
        return 'Collection'.__wrap(super(pygcollect.ForwardingMap, self).values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.google.common.reflect.MutableTypeToInstanceMap()"""
        val = __MutableTypeToInstanceMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def getInstance(self, type: 'Class') -> object:
        """public <T extends B> T com.google.common.reflect.MutableTypeToInstanceMap.getInstance(java.lang.Class<T>)"""
        return object.__wrap(super(__MutableTypeToInstanceMap, self).getInstance(type))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def __init__(self, ):
        """public com.google.common.reflect.MutableTypeToInstanceMap()"""
        val = __MutableTypeToInstanceMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putInstance(self, type: 'TypeToken', value: object) -> object:
        """public <T extends B> T com.google.common.reflect.MutableTypeToInstanceMap.putInstance(com.google.common.reflect.TypeToken<T>,T)"""
        return object.__wrap(super(__MutableTypeToInstanceMap, self).putInstance(type, value))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingMap, self).equals(object))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.isEmpty()"""
        return bool.__wrap(super(pygcollect.ForwardingMap, self).isEmpty())

    @overload
    def containsValue(self, value: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingMap, self).containsValue(value))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<com.google.common.reflect.TypeToken<? extends B>, B>> com.google.common.reflect.MutableTypeToInstanceMap.entrySet()"""
        return 'Set'.__wrap(super(MutableTypeToInstanceMap, self).entrySet())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsKey(self, key: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingMap, self).containsKey(key))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> com.google.common.collect.ForwardingMap.keySet()"""
        return 'Set'.__wrap(super(pygcollect.ForwardingMap, self).keySet())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def put(self, key: 'TypeToken', value: object) -> object:
        """public B com.google.common.reflect.MutableTypeToInstanceMap.put(com.google.common.reflect.TypeToken<? extends B>,B)"""
        return object.__wrap(super(__MutableTypeToInstanceMap, self).put(key, value))

    @overload
    def getInstance(self, type: 'TypeToken') -> object:
        """public <T extends B> T com.google.common.reflect.MutableTypeToInstanceMap.getInstance(com.google.common.reflect.TypeToken<T>)"""
        return object.__wrap(super(__MutableTypeToInstanceMap, self).getInstance(type))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def remove(self, key: object) -> object:
        """public V com.google.common.collect.ForwardingMap.remove(java.lang.Object)"""
        return object.__wrap(super(__pygcollect.ForwardingMap, self).remove(key))

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
    def putAll(self, map: 'Map'):
        """public void com.google.common.reflect.MutableTypeToInstanceMap.putAll(java.util.Map<? extends com.google.common.reflect.TypeToken<? extends B>, ? extends B>)"""
        super(__MutableTypeToInstanceMap, self).putAll(map)

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingMap.size()"""
        return int.__wrap(super(pygcollect.ForwardingMap, self).size()) 
 
 
# CLASS: com.google.common.reflect.TypeResolver
from builtins import str
from pyquantum_helper import override
import com.google.common.reflect.TypeResolver as __TypeResolver
__TypeResolver = __TypeResolver
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
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
 
class TypeResolver():
    """com.google.common.reflect.TypeResolver"""
 
    @staticmethod
    def __wrap(java_value: __TypeResolver) -> 'TypeResolver':
        return TypeResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeResolver):
        """
        Dynamic initializer for TypeResolver.
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
    def resolveType(self, type: 'Type') -> 'Type':
        """public java.lang.reflect.Type com.google.common.reflect.TypeResolver.resolveType(java.lang.reflect.Type)"""
        return 'Type'.__wrap(super(__TypeResolver, self).resolveType(type))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.google.common.reflect.TypeResolver()"""
        val = __TypeResolver()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def where(self, formal: 'Type', actual: 'Type') -> 'TypeResolver':
        """public com.google.common.reflect.TypeResolver com.google.common.reflect.TypeResolver.where(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return 'TypeResolver'.__wrap(super(__TypeResolver, self).where(formal, actual))

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

    @overload
    def __init__(self):
        """public com.google.common.reflect.TypeResolver()"""
        val = __TypeResolver()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.google.common.reflect.ClassPath$ClassInfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
try:
    from pygcommon import io
except ImportError:
    io = __import_once__("pygcommon.io")

import java.lang.Object as __object
from builtins import type
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
import java.net.URL as URL
import com.google.common.reflect.ClassPath as __ClassPath_ClassInfo
__ClassInfo = __ClassPath_ClassInfo.ClassInfo
import com.google.common.reflect.ClassPath as __ClassPath_ResourceInfo
__ResourceInfo = __ClassPath_ResourceInfo.ResourceInfo
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.io.CharSource as __CharSource
__CharSource = __CharSource
import java.lang.String as __String
__String = __String
import java.net.URL as __URL
__URL = __URL
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClassInfo():
    """com.google.common.reflect.ClassPath.ClassInfo"""
 
    @staticmethod
    def __wrap(java_value: __ClassInfo) -> 'ClassInfo':
        return ClassInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClassInfo):
        """
        Dynamic initializer for ClassInfo.
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
    def getName(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ClassInfo.getName()"""
        return str.__wrap(super(ClassInfo, self).getName())

    @overload
    def asCharSource(self, charset: 'Charset') -> 'io.CharSource':
        """public final com.google.common.io.CharSource com.google.common.reflect.ClassPath$ResourceInfo.asCharSource(java.nio.charset.Charset)"""
        return 'io.CharSource'.__wrap(super(__ResourceInfo, self).asCharSource(charset))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPackageName(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ClassInfo.getPackageName()"""
        return str.__wrap(super(ClassInfo, self).getPackageName())

    @overload
    def isTopLevel(self) -> bool:
        """public boolean com.google.common.reflect.ClassPath$ClassInfo.isTopLevel()"""
        return bool.__wrap(super(ClassInfo, self).isTopLevel())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSimpleName(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ClassInfo.getSimpleName()"""
        return str.__wrap(super(ClassInfo, self).getSimpleName())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.ClassPath$ResourceInfo.hashCode()"""
        return int.__wrap(super(ResourceInfo, self).hashCode())

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
    def load(self) -> 'type.Class':
        """public java.lang.Class<?> com.google.common.reflect.ClassPath$ClassInfo.load()"""
        return 'type.Class'.__wrap(super(ClassInfo, self).load())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ClassInfo.toString()"""
        return str.__wrap(super(ClassInfo, self).toString())

    @override
    @overload
    def url(self) -> 'URL':
        """public final java.net.URL com.google.common.reflect.ClassPath$ResourceInfo.url()"""
        return 'URL'.__wrap(super(ResourceInfo, self).url())

    @override
    @overload
    def asByteSource(self) -> 'io.ByteSource':
        """public final com.google.common.io.ByteSource com.google.common.reflect.ClassPath$ResourceInfo.asByteSource()"""
        return 'io.ByteSource'.__wrap(super(ResourceInfo, self).asByteSource())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.ClassPath$ResourceInfo.equals(java.lang.Object)"""
        return bool.__wrap(super(__ResourceInfo, self).equals(obj))

    @override
    @overload
    def getResourceName(self) -> str:
        """public final java.lang.String com.google.common.reflect.ClassPath$ResourceInfo.getResourceName()"""
        return str.__wrap(super(ResourceInfo, self).getResourceName()) 
 
 
# CLASS: com.google.common.reflect.ImmutableTypeToInstanceMap$Builder
import com.google.common.reflect.ImmutableTypeToInstanceMap as __ImmutableTypeToInstanceMap
__ImmutableTypeToInstanceMap = __ImmutableTypeToInstanceMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.reflect.ImmutableTypeToInstanceMap as __ImmutableTypeToInstanceMap_Builder
__Builder = __ImmutableTypeToInstanceMap_Builder.Builder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """com.google.common.reflect.ImmutableTypeToInstanceMap.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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

    @overload
    def put(self, key: 'Class', value: object) -> 'Builder':
        """public <T extends B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder<B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder.put(java.lang.Class<T>,T)"""
        return 'Builder'.__wrap(super(__Builder, self).put(key, value))

    @overload
    def build(self) -> 'ImmutableTypeToInstanceMap':
        """public com.google.common.reflect.ImmutableTypeToInstanceMap<B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder.build()"""
        return 'ImmutableTypeToInstanceMap'.__wrap(super(Builder, self).build())

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
    def put(self, key: 'TypeToken', value: object) -> 'Builder':
        """public <T extends B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder<B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder.put(com.google.common.reflect.TypeToken<T>,T)"""
        return 'Builder'.__wrap(super(__Builder, self).put(key, value))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.reflect.Parameter
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.reflect.TypeToken as __TypeToken
__TypeToken = __TypeToken
from builtins import type
import com.google.common.reflect.Parameter as __Parameter
__Parameter = __Parameter
import java.lang.annotation.Annotation as Annotation
from typing import List
import com.google.common.reflect.Invokable as __Invokable
__Invokable = __Invokable
import java.lang.Long as __long
import java.lang.reflect.AnnotatedType as AnnotatedType
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.AnnotatedType as __AnnotatedType
__AnnotatedType = __AnnotatedType
from builtins import int
 
class Parameter():
    """com.google.common.reflect.Parameter"""
 
    @staticmethod
    def __wrap(java_value: __Parameter) -> 'Parameter':
        return Parameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Parameter):
        """
        Dynamic initializer for Parameter.
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
    def isAnnotationPresent(self, annotationType: 'Class') -> bool:
        """public boolean com.google.common.reflect.Parameter.isAnnotationPresent(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool.__wrap(super(__Parameter, self).isAnnotationPresent(annotationType))

    @override
    @overload
    def getAnnotations(self) -> List['Annotation']:
        """public java.lang.annotation.Annotation[] com.google.common.reflect.Parameter.getAnnotations()"""
        return List['Annotation'].__wrap(super(Parameter, self).getAnnotations())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getDeclaredAnnotation(self, annotationType: 'Class') -> 'Annotation':
        """public <A extends java.lang.annotation.Annotation> A com.google.common.reflect.Parameter.getDeclaredAnnotation(java.lang.Class<A>)"""
        return 'Annotation'.__wrap(super(__Parameter, self).getDeclaredAnnotation(annotationType))

    @overload
    def getAnnotationsByType(self, annotationType: 'Class') -> List['Annotation']:
        """public <A extends java.lang.annotation.Annotation> A[] com.google.common.reflect.Parameter.getAnnotationsByType(java.lang.Class<A>)"""
        return List['Annotation'].__wrap(super(__Parameter, self).getAnnotationsByType(annotationType))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.Parameter.hashCode()"""
        return int.__wrap(super(Parameter, self).hashCode())

    @overload
    def getDeclaredAnnotationsByType(self, annotationType: 'Class') -> List['Annotation']:
        """public <A extends java.lang.annotation.Annotation> A[] com.google.common.reflect.Parameter.getDeclaredAnnotationsByType(java.lang.Class<A>)"""
        return List['Annotation'].__wrap(super(__Parameter, self).getDeclaredAnnotationsByType(annotationType))

    @overload
    def getAnnotatedType(self) -> 'AnnotatedType':
        """public java.lang.reflect.AnnotatedType com.google.common.reflect.Parameter.getAnnotatedType()"""
        return 'AnnotatedType'.__wrap(super(Parameter, self).getAnnotatedType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getType(self) -> 'TypeToken':
        """public com.google.common.reflect.TypeToken<?> com.google.common.reflect.Parameter.getType()"""
        return 'TypeToken'.__wrap(super(Parameter, self).getType())

    @override
    @overload
    def getDeclaredAnnotations(self) -> List['Annotation']:
        """public java.lang.annotation.Annotation[] com.google.common.reflect.Parameter.getDeclaredAnnotations()"""
        return List['Annotation'].__wrap(super(Parameter, self).getDeclaredAnnotations())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getAnnotation(self, annotationType: 'Class') -> 'Annotation':
        """public <A extends java.lang.annotation.Annotation> A com.google.common.reflect.Parameter.getAnnotation(java.lang.Class<A>)"""
        return 'Annotation'.__wrap(super(__Parameter, self).getAnnotation(annotationType))

    @overload
    def getDeclaringInvokable(self) -> 'Invokable':
        """public com.google.common.reflect.Invokable<?, ?> com.google.common.reflect.Parameter.getDeclaringInvokable()"""
        return 'Invokable'.__wrap(super(Parameter, self).getDeclaringInvokable())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.Parameter.equals(java.lang.Object)"""
        return bool.__wrap(super(__Parameter, self).equals(obj))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.Parameter.toString()"""
        return str.__wrap(super(Parameter, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.reflect.Reflection
import java.lang.reflect.InvocationHandler as InvocationHandler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.google.common.reflect.Reflection as __Reflection
__Reflection = __Reflection
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
 
class Reflection():
    """com.google.common.reflect.Reflection"""
 
    @staticmethod
    def __wrap(java_value: __Reflection) -> 'Reflection':
        return Reflection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Reflection):
        """
        Dynamic initializer for Reflection.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def initialize(*classes: 'type.Class'):
        """public static void com.google.common.reflect.Reflection.initialize(java.lang.Class<?>...)"""
        __Reflection.initialize(classes)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def newProxy(interfaceType: 'Class', handler: 'InvocationHandler') -> object:
        """public static <T> T com.google.common.reflect.Reflection.newProxy(java.lang.Class<T>,java.lang.reflect.InvocationHandler)"""
        return object.__wrap(__Reflection.newProxy(interfaceType, handler))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getPackageName(clazz: 'Class') -> str:
        """public static java.lang.String com.google.common.reflect.Reflection.getPackageName(java.lang.Class<?>)"""
        return str.__wrap(__Reflection.getPackageName(clazz))

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

    @staticmethod
    @overload
    def getPackageName(classFullName: str) -> str:
        """public static java.lang.String com.google.common.reflect.Reflection.getPackageName(java.lang.String)"""
        return str.__wrap(__Reflection.getPackageName(classFullName))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.reflect.AbstractInvocationHandler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.reflect.AbstractInvocationHandler as __AbstractInvocationHandler
__AbstractInvocationHandler = __AbstractInvocationHandler
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.Method as Method
from builtins import int
 
class AbstractInvocationHandler(ABC):
    """com.google.common.reflect.AbstractInvocationHandler"""
 
    @staticmethod
    def __wrap(java_value: __AbstractInvocationHandler) -> 'AbstractInvocationHandler':
        return AbstractInvocationHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractInvocationHandler):
        """
        Dynamic initializer for AbstractInvocationHandler.
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
    def hashCode(self) -> int:
        """public int com.google.common.reflect.AbstractInvocationHandler.hashCode()"""
        return int.__wrap(super(AbstractInvocationHandler, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.google.common.reflect.AbstractInvocationHandler()"""
        val = __AbstractInvocationHandler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.AbstractInvocationHandler.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractInvocationHandler, self).equals(obj))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.AbstractInvocationHandler.toString()"""
        return str.__wrap(super(AbstractInvocationHandler, self).toString())

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
    def invoke(self, proxy: object, method: 'Method', args: 'Object') -> object:
        """public final java.lang.Object com.google.common.reflect.AbstractInvocationHandler.invoke(java.lang.Object,java.lang.reflect.Method,java.lang.Object[]) throws java.lang.Throwable"""
        return object.__wrap(super(__AbstractInvocationHandler, self).invoke(proxy, method, args))

    @overload
    def __init__(self):
        """public com.google.common.reflect.AbstractInvocationHandler()"""
        val = __AbstractInvocationHandler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.reflect.Invokable
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.reflect.Member as __Member
__Member = __Member
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as Annotation
import com.google.common.collect.ImmutableList as __ImmutableList
__ImmutableList = __ImmutableList
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from builtins import str
from pyquantum_helper import override
import com.google.common.reflect.TypeToken as __TypeToken
__TypeToken = __TypeToken
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
from typing import List
import com.google.common.reflect.Invokable as __Invokable
__Invokable = __Invokable
import java.lang.Long as __long
import java.util.Set as Set
import java.lang.reflect.AnnotatedElement as __AnnotatedElement
__AnnotatedElement = __AnnotatedElement
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.lang.reflect.Method as Method
import java.lang.reflect.Constructor as Constructor
 
class Invokable(ABC):
    """com.google.common.reflect.Invokable"""
 
    @staticmethod
    def __wrap(java_value: __Invokable) -> 'Invokable':
        return Invokable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Invokable):
        """
        Dynamic initializer for Invokable.
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
    def isAnnotationPresent(self, annotationClass: 'Class') -> bool:
        """public final boolean com.google.common.reflect.Invokable.isAnnotationPresent(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool.__wrap(super(__Invokable, self).isAnnotationPresent(annotationClass))

    @overload
    def isProtected(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isProtected()"""
        return bool.__wrap(super(Invokable, self).isProtected())

    @overload
    def isAbstract(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isAbstract()"""
        return bool.__wrap(super(Invokable, self).isAbstract())

    @overload
    def isNative(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isNative()"""
        return bool.__wrap(super(Invokable, self).isNative())

    @overload
    def returning(self, returnType: 'Class') -> 'Invokable':
        """public final <R1 extends R> com.google.common.reflect.Invokable<T, R1> com.google.common.reflect.Invokable.returning(java.lang.Class<R1>)"""
        return 'Invokable'.__wrap(super(__Invokable, self).returning(returnType))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isStatic(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isStatic()"""
        return bool.__wrap(super(Invokable, self).isStatic())

    @staticmethod
    @overload
    def from(constructor: 'Constructor') -> 'Invokable':
        """public static <T> com.google.common.reflect.Invokable<T, T> com.google.common.reflect.Invokable.from(java.lang.reflect.Constructor<T>)"""
        return Invokable.__wrap(__Invokable.from(constructor))

    @overload
    def trySetAccessible(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.trySetAccessible()"""
        return bool.__wrap(super(Invokable, self).trySetAccessible())

    @overload
    def returning(self, returnType: 'TypeToken') -> 'Invokable':
        """public final <R1 extends R> com.google.common.reflect.Invokable<T, R1> com.google.common.reflect.Invokable.returning(com.google.common.reflect.TypeToken<R1>)"""
        return 'Invokable'.__wrap(super(__Invokable, self).returning(returnType))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAnnotationsByType(self, arg0: 'Class') -> List['Annotation']:
        """public default <T extends java.lang.annotation.Annotation> T[] java.lang.reflect.AnnotatedElement.getAnnotationsByType(java.lang.Class<T>)"""
        return List['Annotation'].__wrap(super(__AnnotatedElement, self).getAnnotationsByType(arg0))

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.Invokable.equals(java.lang.Object)"""
        return bool.__wrap(super(__Invokable, self).equals(obj))

    @overload
    def getDeclaredAnnotationsByType(self, arg0: 'Class') -> List['Annotation']:
        """public default <T extends java.lang.annotation.Annotation> T[] java.lang.reflect.AnnotatedElement.getDeclaredAnnotationsByType(java.lang.Class<T>)"""
        return List['Annotation'].__wrap(super(__AnnotatedElement, self).getDeclaredAnnotationsByType(arg0))

    @overload
    def setAccessible(self, flag: bool):
        """public final void com.google.common.reflect.Invokable.setAccessible(boolean)"""
        super(__Invokable, self).setAccessible(__boolean.valueOf(flag))

    @overload
    def isAccessible(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isAccessible()"""
        return bool.__wrap(super(Invokable, self).isAccessible())

    @overload
    def isPackagePrivate(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isPackagePrivate()"""
        return bool.__wrap(super(Invokable, self).isPackagePrivate())

    @abstractmethod
    def getAnnotatedReturnType(self, ):
        """public abstract java.lang.reflect.AnnotatedType com.google.common.reflect.Invokable.getAnnotatedReturnType()"""
        pass

    @overload
    def isSynchronized(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isSynchronized()"""
        return bool.__wrap(super(Invokable, self).isSynchronized())

    @override
    @overload
    def getAnnotations(self) -> List['Annotation']:
        """public final java.lang.annotation.Annotation[] com.google.common.reflect.Invokable.getAnnotations()"""
        return List['Annotation'].__wrap(super(Invokable, self).getAnnotations())

    @overload
    def isPublic(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isPublic()"""
        return bool.__wrap(super(Invokable, self).isPublic())

    @override
    @overload
    def accessFlags(self) -> 'Set':
        """public default java.util.Set<java.lang.reflect.AccessFlag> java.lang.reflect.Member.accessFlags()"""
        return 'Set'.__wrap(super(Member, self).accessFlags())

    @override
    @overload
    def getModifiers(self) -> int:
        """public final int com.google.common.reflect.Invokable.getModifiers()"""
        return int.__wrap(super(Invokable, self).getModifiers())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.Invokable.hashCode()"""
        return int.__wrap(super(Invokable, self).hashCode())

    @overload
    def isFinal(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isFinal()"""
        return bool.__wrap(super(Invokable, self).isFinal())

    @override
    @overload
    def getDeclaredAnnotations(self) -> List['Annotation']:
        """public final java.lang.annotation.Annotation[] com.google.common.reflect.Invokable.getDeclaredAnnotations()"""
        return List['Annotation'].__wrap(super(Invokable, self).getDeclaredAnnotations())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def invoke(self, receiver: object, *args: object) -> object:
        """public final R com.google.common.reflect.Invokable.invoke(T,java.lang.Object...) throws java.lang.reflect.InvocationTargetException,java.lang.IllegalAccessException"""
        return object.__wrap(super(__Invokable, self).invoke(receiver, args))

    @abstractmethod
    def isVarArgs(self, ):
        """public abstract boolean com.google.common.reflect.Invokable.isVarArgs()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getAnnotation(self, annotationClass: 'Class') -> 'Annotation':
        """public final <A extends java.lang.annotation.Annotation> A com.google.common.reflect.Invokable.getAnnotation(java.lang.Class<A>)"""
        return 'Annotation'.__wrap(super(__Invokable, self).getAnnotation(annotationClass))

    @overload
    def getDeclaredAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public default <T extends java.lang.annotation.Annotation> T java.lang.reflect.AnnotatedElement.getDeclaredAnnotation(java.lang.Class<T>)"""
        return 'Annotation'.__wrap(super(__AnnotatedElement, self).getDeclaredAnnotation(arg0))

    @staticmethod
    @overload
    def from(method: 'Method') -> 'Invokable':
        """public static com.google.common.reflect.Invokable<?, java.lang.Object> com.google.common.reflect.Invokable.from(java.lang.reflect.Method)"""
        return Invokable.__wrap(__Invokable.from(method))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<? super T> com.google.common.reflect.Invokable.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Invokable, self).getDeclaringClass())

    @abstractmethod
    def getTypeParameters(self, ):
        """public abstract java.lang.reflect.TypeVariable<?>[] com.google.common.reflect.Invokable.getTypeParameters()"""
        pass

    @overload
    def getExceptionTypes(self) -> 'pygcollect.ImmutableList':
        """public final com.google.common.collect.ImmutableList<com.google.common.reflect.TypeToken<? extends java.lang.Throwable>> com.google.common.reflect.Invokable.getExceptionTypes()"""
        return 'pygcollect.ImmutableList'.__wrap(super(Invokable, self).getExceptionTypes())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String com.google.common.reflect.Invokable.getName()"""
        return str.__wrap(super(Invokable, self).getName())

    @override
    @overload
    def isSynthetic(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isSynthetic()"""
        return bool.__wrap(super(Invokable, self).isSynthetic())

    @abstractmethod
    def isOverridable(self, ):
        """public abstract boolean com.google.common.reflect.Invokable.isOverridable()"""
        pass

    @overload
    def getOwnerType(self) -> 'TypeToken':
        """public com.google.common.reflect.TypeToken<T> com.google.common.reflect.Invokable.getOwnerType()"""
        return 'TypeToken'.__wrap(super(Invokable, self).getOwnerType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isPrivate(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isPrivate()"""
        return bool.__wrap(super(Invokable, self).isPrivate())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.Invokable.toString()"""
        return str.__wrap(super(Invokable, self).toString())

    @overload
    def getReturnType(self) -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<? extends R> com.google.common.reflect.Invokable.getReturnType()"""
        return 'TypeToken'.__wrap(super(Invokable, self).getReturnType())

    @overload
    def getParameters(self) -> 'pygcollect.ImmutableList':
        """public final com.google.common.collect.ImmutableList<com.google.common.reflect.Parameter> com.google.common.reflect.Invokable.getParameters()"""
        return 'pygcollect.ImmutableList'.__wrap(super(Invokable, self).getParameters()) 
 
 
# CLASS: com.google.common.reflect.ImmutableTypeToInstanceMap
import com.google.common.reflect.ImmutableTypeToInstanceMap as __ImmutableTypeToInstanceMap
__ImmutableTypeToInstanceMap = __ImmutableTypeToInstanceMap
from builtins import type
import java.util.Map as __Map
__Map = __Map
import com.google.common.collect.ForwardingMap as __ForwardingMap
__ForwardingMap = __ForwardingMap
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import com.google.common.reflect.ImmutableTypeToInstanceMap as __ImmutableTypeToInstanceMap_Builder
__Builder = __ImmutableTypeToInstanceMap_Builder.Builder
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.Set as Set
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class ImmutableTypeToInstanceMap():
    """com.google.common.reflect.ImmutableTypeToInstanceMap"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableTypeToInstanceMap) -> 'ImmutableTypeToInstanceMap':
        return ImmutableTypeToInstanceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableTypeToInstanceMap):
        """
        Dynamic initializer for ImmutableTypeToInstanceMap.
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
    def hashCode(self) -> int:
        """public int com.google.common.collect.ForwardingMap.hashCode()"""
        return int.__wrap(super(pygcollect.ForwardingMap, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getInstance(self, type: 'TypeToken') -> object:
        """public <T extends B> T com.google.common.reflect.ImmutableTypeToInstanceMap.getInstance(com.google.common.reflect.TypeToken<T>)"""
        return object.__wrap(super(__ImmutableTypeToInstanceMap, self).getInstance(type))

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingMap.clear()"""
        super(pygcollect.ForwardingMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.collect.ForwardingMap.get(java.lang.Object)"""
        return object.__wrap(super(__pygcollect.ForwardingMap, self).get(key))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> com.google.common.collect.ForwardingMap.values()"""
        return 'Collection'.__wrap(super(pygcollect.ForwardingMap, self).values())

    @overload
    def put(self, key: 'TypeToken', value: object) -> object:
        """public B com.google.common.reflect.ImmutableTypeToInstanceMap.put(com.google.common.reflect.TypeToken<? extends B>,B)"""
        return object.__wrap(super(__ImmutableTypeToInstanceMap, self).put(key, value))

    @overload
    def putInstance(self, type: 'Class', value: object) -> object:
        """public <T extends B> T com.google.common.reflect.ImmutableTypeToInstanceMap.putInstance(java.lang.Class<T>,T)"""
        return object.__wrap(super(__ImmutableTypeToInstanceMap, self).putInstance(type, value))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putInstance(self, type: 'TypeToken', value: object) -> object:
        """public <T extends B> T com.google.common.reflect.ImmutableTypeToInstanceMap.putInstance(com.google.common.reflect.TypeToken<T>,T)"""
        return object.__wrap(super(__ImmutableTypeToInstanceMap, self).putInstance(type, value))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def getInstance(self, type: 'Class') -> object:
        """public <T extends B> T com.google.common.reflect.ImmutableTypeToInstanceMap.getInstance(java.lang.Class<T>)"""
        return object.__wrap(super(__ImmutableTypeToInstanceMap, self).getInstance(type))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> com.google.common.collect.ForwardingMap.entrySet()"""
        return 'Set'.__wrap(super(pygcollect.ForwardingMap, self).entrySet())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingMap, self).equals(object))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.isEmpty()"""
        return bool.__wrap(super(pygcollect.ForwardingMap, self).isEmpty())

    @overload
    def containsValue(self, value: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingMap, self).containsValue(value))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @staticmethod
    @overload
    def of() -> 'ImmutableTypeToInstanceMap':
        """public static <B> com.google.common.reflect.ImmutableTypeToInstanceMap<B> com.google.common.reflect.ImmutableTypeToInstanceMap.of()"""
        return ImmutableTypeToInstanceMap.__wrap(__ImmutableTypeToInstanceMap.of())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def putAll(self, map: 'Map'):
        """public void com.google.common.reflect.ImmutableTypeToInstanceMap.putAll(java.util.Map<? extends com.google.common.reflect.TypeToken<? extends B>, ? extends B>)"""
        super(__ImmutableTypeToInstanceMap, self).putAll(map)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsKey(self, key: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingMap, self).containsKey(key))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> com.google.common.collect.ForwardingMap.keySet()"""
        return 'Set'.__wrap(super(pygcollect.ForwardingMap, self).keySet())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def remove(self, key: object) -> object:
        """public V com.google.common.collect.ForwardingMap.remove(java.lang.Object)"""
        return object.__wrap(super(__pygcollect.ForwardingMap, self).remove(key))

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static <B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder<B> com.google.common.reflect.ImmutableTypeToInstanceMap.builder()"""
        return Builder.__wrap(__ImmutableTypeToInstanceMap.builder())

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

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingMap.size()"""
        return int.__wrap(super(pygcollect.ForwardingMap, self).size()) 
 
 
# CLASS: com.google.common.reflect.TypeToken$TypeSet
import java.util.function.Predicate as Predicate
import com.google.common.collect.ForwardingCollection as __ForwardingCollection
__ForwardingCollection = __ForwardingCollection
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.google.common.reflect.TypeToken as __TypeToken_TypeSet
__TypeSet = __TypeToken_TypeSet.TypeSet
import com.google.common.collect.ForwardingSet as __ForwardingSet
__ForwardingSet = __ForwardingSet
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Set as Set
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TypeSet():
    """com.google.common.reflect.TypeToken.TypeSet"""
 
    @staticmethod
    def __wrap(java_value: __TypeSet) -> 'TypeSet':
        return TypeSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeSet):
        """
        Dynamic initializer for TypeSet.
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
    def contains(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.contains(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).contains(object))

    @overload
    def retainAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).retainAll(collection))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).removeAll(collection))

    @overload
    def rawTypes(self) -> 'Set':
        """public java.util.Set<java.lang.Class<? super T>> com.google.common.reflect.TypeToken$TypeSet.rawTypes()"""
        return 'Set'.__wrap(super(TypeSet, self).rawTypes())

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingCollection.size()"""
        return int.__wrap(super(pygcollect.ForwardingCollection, self).size())

    @overload
    def containsAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).containsAll(collection))

    @overload
    def interfaces(self) -> 'TypeSet':
        """public com.google.common.reflect.TypeToken<T>$TypeSet com.google.common.reflect.TypeToken$TypeSet.interfaces()"""
        return 'TypeSet'.__wrap(super(TypeSet, self).interfaces())

    @overload
    def addAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).addAll(collection))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.isEmpty()"""
        return bool.__wrap(super(pygcollect.ForwardingCollection, self).isEmpty())

    @overload
    def classes(self) -> 'TypeSet':
        """public com.google.common.reflect.TypeToken<T>$TypeSet com.google.common.reflect.TypeToken$TypeSet.classes()"""
        return 'TypeSet'.__wrap(super(TypeSet, self).classes())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.collect.ForwardingSet.hashCode()"""
        return int.__wrap(super(pygcollect.ForwardingSet, self).hashCode())

    @overload
    def remove(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).remove(object))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingCollection.clear()"""
        super(pygcollect.ForwardingCollection, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] com.google.common.collect.ForwardingCollection.toArray()"""
        return List[object].__wrap(super(pygcollect.ForwardingCollection, self).toArray())

    @overload
    def add(self, element: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.add(E)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).add(element))

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> com.google.common.collect.ForwardingCollection.iterator()"""
        return 'Iterator'.__wrap(super(pygcollect.ForwardingCollection, self).iterator())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingSet, self).equals(object))

    @overload
    def toArray(self, array: 'Object') -> List[object]:
        """public <T> T[] com.google.common.collect.ForwardingCollection.toArray(T[])"""
        return List[object].__wrap(super(__pygcollect.ForwardingCollection, self).toArray(array))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.reflect.TypeToken
from builtins import str
from pyquantum_helper import override
import com.google.common.reflect.TypeToken as __TypeToken
__TypeToken = __TypeToken
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
import com.google.common.reflect.Invokable as __Invokable
__Invokable = __Invokable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.reflect.TypeToken as __TypeToken_TypeSet
__TypeSet = __TypeToken_TypeSet.TypeSet
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.Method as Method
from builtins import int
import java.lang.reflect.Constructor as Constructor
 
class TypeToken(ABC):
    """com.google.common.reflect.TypeToken"""
 
    @staticmethod
    def __wrap(java_value: __TypeToken) -> 'TypeToken':
        return TypeToken(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeToken):
        """
        Dynamic initializer for TypeToken.
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
    def wrap(self) -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.wrap()"""
        return 'TypeToken'.__wrap(super(TypeToken, self).wrap())

    @overload
    def getSupertype(self, superclass: 'Class') -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<? super T> com.google.common.reflect.TypeToken.getSupertype(java.lang.Class<? super T>)"""
        return 'TypeToken'.__wrap(super(__TypeToken, self).getSupertype(superclass))

    @overload
    def constructor(self, constructor: 'Constructor') -> 'Invokable':
        """public final com.google.common.reflect.Invokable<T, T> com.google.common.reflect.TypeToken.constructor(java.lang.reflect.Constructor<?>)"""
        return 'Invokable'.__wrap(super(__TypeToken, self).constructor(constructor))

    @overload
    def unwrap(self) -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.unwrap()"""
        return 'TypeToken'.__wrap(super(TypeToken, self).unwrap())

    @overload
    def getRawType(self) -> 'type.Class':
        """public final java.lang.Class<? super T> com.google.common.reflect.TypeToken.getRawType()"""
        return 'type.Class'.__wrap(super(TypeToken, self).getRawType())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean com.google.common.reflect.TypeToken.equals(java.lang.Object)"""
        return bool.__wrap(super(__TypeToken, self).equals(o))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.TypeToken.hashCode()"""
        return int.__wrap(super(TypeToken, self).hashCode())

    @overload
    def isSubtypeOf(self, supertype: 'Type') -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isSubtypeOf(java.lang.reflect.Type)"""
        return bool.__wrap(super(__TypeToken, self).isSubtypeOf(supertype))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def of(type: 'Type') -> 'TypeToken':
        """public static com.google.common.reflect.TypeToken<?> com.google.common.reflect.TypeToken.of(java.lang.reflect.Type)"""
        return TypeToken.__wrap(__TypeToken.of(type))

    @overload
    def isSupertypeOf(self, type: 'TypeToken') -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isSupertypeOf(com.google.common.reflect.TypeToken<?>)"""
        return bool.__wrap(super(__TypeToken, self).isSupertypeOf(type))

    @overload
    def getTypes(self) -> 'TypeSet':
        """public final com.google.common.reflect.TypeToken<T>$TypeSet com.google.common.reflect.TypeToken.getTypes()"""
        return 'TypeSet'.__wrap(super(TypeToken, self).getTypes())

    @overload
    def resolveType(self, type: 'Type') -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<?> com.google.common.reflect.TypeToken.resolveType(java.lang.reflect.Type)"""
        return 'TypeToken'.__wrap(super(__TypeToken, self).resolveType(type))

    @overload
    def isSupertypeOf(self, type: 'Type') -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isSupertypeOf(java.lang.reflect.Type)"""
        return bool.__wrap(super(__TypeToken, self).isSupertypeOf(type))

    @overload
    def where(self, typeParam: 'TypeParameter', typeArg: 'Class') -> 'TypeToken':
        """public final <X> com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.where(com.google.common.reflect.TypeParameter<X>,java.lang.Class<X>)"""
        return 'TypeToken'.__wrap(super(__TypeToken, self).where(typeParam, typeArg))

    @overload
    def method(self, method: 'Method') -> 'Invokable':
        """public final com.google.common.reflect.Invokable<T, java.lang.Object> com.google.common.reflect.TypeToken.method(java.lang.reflect.Method)"""
        return 'Invokable'.__wrap(super(__TypeToken, self).method(method))

    @overload
    def getSubtype(self, subclass: 'Class') -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<? extends T> com.google.common.reflect.TypeToken.getSubtype(java.lang.Class<?>)"""
        return 'TypeToken'.__wrap(super(__TypeToken, self).getSubtype(subclass))

    @overload
    def getType(self) -> 'Type':
        """public final java.lang.reflect.Type com.google.common.reflect.TypeToken.getType()"""
        return 'Type'.__wrap(super(TypeToken, self).getType())

    @overload
    def where(self, typeParam: 'TypeParameter', typeArg: 'TypeToken') -> 'TypeToken':
        """public final <X> com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.where(com.google.common.reflect.TypeParameter<X>,com.google.common.reflect.TypeToken<X>)"""
        return 'TypeToken'.__wrap(super(__TypeToken, self).where(typeParam, typeArg))

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

    @staticmethod
    @overload
    def of(type: 'Class') -> 'TypeToken':
        """public static <T> com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.of(java.lang.Class<T>)"""
        return TypeToken.__wrap(__TypeToken.of(type))

    @overload
    def getComponentType(self) -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<?> com.google.common.reflect.TypeToken.getComponentType()"""
        return 'TypeToken'.__wrap(super(TypeToken, self).getComponentType())

    @overload
    def isPrimitive(self) -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isPrimitive()"""
        return bool.__wrap(super(TypeToken, self).isPrimitive())

    @overload
    def isArray(self) -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isArray()"""
        return bool.__wrap(super(TypeToken, self).isArray())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isSubtypeOf(self, type: 'TypeToken') -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isSubtypeOf(com.google.common.reflect.TypeToken<?>)"""
        return bool.__wrap(super(__TypeToken, self).isSubtypeOf(type))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.TypeToken.toString()"""
        return str.__wrap(super(TypeToken, self).toString()) 
 
 
# CLASS: com.google.common.reflect.ClassPath$ResourceInfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
try:
    from pygcommon import io
except ImportError:
    io = __import_once__("pygcommon.io")

import java.lang.Object as __object
from builtins import type
import com.google.common.io.ByteSource as __ByteSource
__ByteSource = __ByteSource
import java.net.URL as URL
import com.google.common.reflect.ClassPath as __ClassPath_ResourceInfo
__ResourceInfo = __ClassPath_ResourceInfo.ResourceInfo
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.io.CharSource as __CharSource
__CharSource = __CharSource
import java.lang.String as __String
__String = __String
import java.net.URL as __URL
__URL = __URL
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ResourceInfo():
    """com.google.common.reflect.ClassPath.ResourceInfo"""
 
    @staticmethod
    def __wrap(java_value: __ResourceInfo) -> 'ResourceInfo':
        return ResourceInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceInfo):
        """
        Dynamic initializer for ResourceInfo.
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
    def asCharSource(self, charset: 'Charset') -> 'io.CharSource':
        """public final com.google.common.io.CharSource com.google.common.reflect.ClassPath$ResourceInfo.asCharSource(java.nio.charset.Charset)"""
        return 'io.CharSource'.__wrap(super(__ResourceInfo, self).asCharSource(charset))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def url(self) -> 'URL':
        """public final java.net.URL com.google.common.reflect.ClassPath$ResourceInfo.url()"""
        return 'URL'.__wrap(super(ResourceInfo, self).url())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.ClassPath$ResourceInfo.hashCode()"""
        return int.__wrap(super(ResourceInfo, self).hashCode())

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
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ResourceInfo.toString()"""
        return str.__wrap(super(ResourceInfo, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.ClassPath$ResourceInfo.equals(java.lang.Object)"""
        return bool.__wrap(super(__ResourceInfo, self).equals(obj))

    @overload
    def asByteSource(self) -> 'io.ByteSource':
        """public final com.google.common.io.ByteSource com.google.common.reflect.ClassPath$ResourceInfo.asByteSource()"""
        return 'io.ByteSource'.__wrap(super(ResourceInfo, self).asByteSource())

    @overload
    def getResourceName(self) -> str:
        """public final java.lang.String com.google.common.reflect.ClassPath$ResourceInfo.getResourceName()"""
        return str.__wrap(super(ResourceInfo, self).getResourceName()) 
 
 
# CLASS: com.google.common.reflect.TypeToInstanceMap
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import com.google.common.reflect.TypeToInstanceMap as __TypeToInstanceMap
__TypeToInstanceMap = __TypeToInstanceMap
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class TypeToInstanceMap(ABC):
    """com.google.common.reflect.TypeToInstanceMap"""
 
    @staticmethod
    def __wrap(java_value: __TypeToInstanceMap) -> 'TypeToInstanceMap':
        return TypeToInstanceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeToInstanceMap):
        """
        Dynamic initializer for TypeToInstanceMap.
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
    def getInstance(self, type: 'Class'):
        """public abstract <T extends B> T com.google.common.reflect.TypeToInstanceMap.getInstance(java.lang.Class<T>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def getInstance(self, type: 'TypeToken'):
        """public abstract <T extends B> T com.google.common.reflect.TypeToInstanceMap.getInstance(com.google.common.reflect.TypeToken<T>)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @abstractmethod
    def putInstance(self, type: 'TypeToken', value: object):
        """public abstract <T extends B> T com.google.common.reflect.TypeToInstanceMap.putInstance(com.google.common.reflect.TypeToken<T>,T)"""
        pass

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @abstractmethod
    def putInstance(self, type: 'Class', value: object):
        """public abstract <T extends B> T com.google.common.reflect.TypeToInstanceMap.putInstance(java.lang.Class<T>,T)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass 
 
 
# CLASS: com.google.common.reflect.TypeParameter
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.google.common.reflect.TypeParameter as __TypeParameter
__TypeParameter = __TypeParameter
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TypeParameter(ABC):
    """com.google.common.reflect.TypeParameter"""
 
    @staticmethod
    def __wrap(java_value: __TypeParameter) -> 'TypeParameter':
        return TypeParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeParameter):
        """
        Dynamic initializer for TypeParameter.
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
        """public java.lang.String com.google.common.reflect.TypeParameter.toString()"""
        return str.__wrap(super(TypeParameter, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.reflect.TypeParameter.hashCode()"""
        return int.__wrap(super(TypeParameter, self).hashCode())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, o: object) -> bool:
        """public final boolean com.google.common.reflect.TypeParameter.equals(java.lang.Object)"""
        return bool.__wrap(super(__TypeParameter, self).equals(o))