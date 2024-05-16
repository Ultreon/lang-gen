from __future__ import annotations
from overload import overload


 
import java.util.AbstractMap as __AbstractMap
__AbstractMap = __AbstractMap
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import com.google.gson.internal.LinkedTreeMap as __LinkedTreeMap
__LinkedTreeMap = __LinkedTreeMap
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class LinkedTreeMap():
    """com.google.gson.internal.LinkedTreeMap"""
 
    @staticmethod
    def __wrap(java_value: __LinkedTreeMap) -> 'LinkedTreeMap':
        return LinkedTreeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkedTreeMap):
        """
        Dynamic initializer for LinkedTreeMap.
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
        """public boolean com.google.gson.internal.LinkedTreeMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__LinkedTreeMap, self).containsKey(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> com.google.gson.internal.LinkedTreeMap.keySet()"""
        return 'Set'.__wrap(super(LinkedTreeMap, self).keySet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractMap.toString()"""
        return str.__wrap(super(AbstractMap, self).toString())

    @overload
    def __init__(self):
        """public com.google.gson.internal.LinkedTreeMap()"""
        val = __LinkedTreeMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int com.google.gson.internal.LinkedTreeMap.size()"""
        return int.__wrap(super(LinkedTreeMap, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> java.util.AbstractMap.values()"""
        return 'Collection'.__wrap(super(AbstractMap, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).containsValue(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.get(java.lang.Object)"""
        return object.__wrap(super(__LinkedTreeMap, self).get(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.put(K,V)"""
        return object.__wrap(super(__LinkedTreeMap, self).put(arg0, arg1))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

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

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.remove(java.lang.Object)"""
        return object.__wrap(super(__LinkedTreeMap, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

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
    def __init__(self, ):
        """public com.google.gson.internal.LinkedTreeMap()"""
        val = __LinkedTreeMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def __init__(self, arg0: bool):
        """public com.google.gson.internal.LinkedTreeMap(boolean)"""
        val = __LinkedTreeMap(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Comparator', arg1: bool):
        """public com.google.gson.internal.LinkedTreeMap(java.util.Comparator<? super K>,boolean)"""
        val = __LinkedTreeMap(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> com.google.gson.internal.LinkedTreeMap.entrySet()"""
        return 'Set'.__wrap(super(LinkedTreeMap, self).entrySet())

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
    def clear(self):
        """public void com.google.gson.internal.LinkedTreeMap.clear()"""
        super(LinkedTreeMap, self).clear()

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

 
 
 
# CLASS: com.google.gson.internal.LinkedTreeMap
import java.util.AbstractMap as __AbstractMap
__AbstractMap = __AbstractMap
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import com.google.gson.internal.LinkedTreeMap as __LinkedTreeMap
__LinkedTreeMap = __LinkedTreeMap
import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class LinkedTreeMap():
    """com.google.gson.internal.LinkedTreeMap"""
 
    @staticmethod
    def __wrap(java_value: __LinkedTreeMap) -> 'LinkedTreeMap':
        return LinkedTreeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkedTreeMap):
        """
        Dynamic initializer for LinkedTreeMap.
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
        """public boolean com.google.gson.internal.LinkedTreeMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__LinkedTreeMap, self).containsKey(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> com.google.gson.internal.LinkedTreeMap.keySet()"""
        return 'Set'.__wrap(super(LinkedTreeMap, self).keySet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractMap.toString()"""
        return str.__wrap(super(AbstractMap, self).toString())

    @overload
    def __init__(self):
        """public com.google.gson.internal.LinkedTreeMap()"""
        val = __LinkedTreeMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int com.google.gson.internal.LinkedTreeMap.size()"""
        return int.__wrap(super(LinkedTreeMap, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> java.util.AbstractMap.values()"""
        return 'Collection'.__wrap(super(AbstractMap, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.AbstractMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMap, self).containsValue(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.get(java.lang.Object)"""
        return object.__wrap(super(__LinkedTreeMap, self).get(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.put(K,V)"""
        return object.__wrap(super(__LinkedTreeMap, self).put(arg0, arg1))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

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

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V com.google.gson.internal.LinkedTreeMap.remove(java.lang.Object)"""
        return object.__wrap(super(__LinkedTreeMap, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

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
    def __init__(self, ):
        """public com.google.gson.internal.LinkedTreeMap()"""
        val = __LinkedTreeMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def __init__(self, arg0: bool):
        """public com.google.gson.internal.LinkedTreeMap(boolean)"""
        val = __LinkedTreeMap(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Comparator', arg1: bool):
        """public com.google.gson.internal.LinkedTreeMap(java.util.Comparator<? super K>,boolean)"""
        val = __LinkedTreeMap(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> com.google.gson.internal.LinkedTreeMap.entrySet()"""
        return 'Set'.__wrap(super(LinkedTreeMap, self).entrySet())

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
    def clear(self):
        """public void com.google.gson.internal.LinkedTreeMap.clear()"""
        super(LinkedTreeMap, self).clear()

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

 
 
 
# CLASS: com.google.gson.internal.LinkedTreeMap 
 
 
# CLASS: com.google.gson.internal.$Gson$Types
import java.lang.reflect.GenericArrayType as GenericArrayType
from builtins import str
import java.lang.reflect.WildcardType as WildcardType
import java.lang.reflect.GenericArrayType as __GenericArrayType
__GenericArrayType = __GenericArrayType
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.ParameterizedType as ParameterizedType
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
import java.lang.reflect.ParameterizedType as __ParameterizedType
__ParameterizedType = __ParameterizedType
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.gson.internal. as ___Gson_Types
__$Gson$Types = ___Gson_Types.Gson.Types
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.WildcardType as __WildcardType
__WildcardType = __WildcardType
from builtins import int
 
class $Gson$Types():
    """com.google.gson.internal..Gson.Types"""
 
    @staticmethod
    def __wrap(java_value: __$Gson$Types) -> '$Gson$Types':
        return $Gson$Types(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __$Gson$Types):
        """
        Dynamic initializer for $Gson$Types.
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

    @staticmethod
    @overload
    def resolve(arg0: 'Type', arg1: 'Class', arg2: 'Type') -> 'Type':
        """public static java.lang.reflect.Type com.google.gson.internal.$Gson$Types.resolve(java.lang.reflect.Type,java.lang.Class<?>,java.lang.reflect.Type)"""
        return Type.__wrap(__$Gson$Types.resolve(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getCollectionElementType(arg0: 'Type', arg1: 'Class') -> 'Type':
        """public static java.lang.reflect.Type com.google.gson.internal.$Gson$Types.getCollectionElementType(java.lang.reflect.Type,java.lang.Class<?>)"""
        return Type.__wrap(__$Gson$Types.getCollectionElementType(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getRawType(arg0: 'Type') -> 'type.Class':
        """public static java.lang.Class<?> com.google.gson.internal.$Gson$Types.getRawType(java.lang.reflect.Type)"""
        return type.Class.__wrap(__$Gson$Types.getRawType(arg0))

    @staticmethod
    @overload
    def subtypeOf(arg0: 'Type') -> 'WildcardType':
        """public static java.lang.reflect.WildcardType com.google.gson.internal.$Gson$Types.subtypeOf(java.lang.reflect.Type)"""
        return WildcardType.__wrap(__$Gson$Types.subtypeOf(arg0))

    @staticmethod
    @overload
    def getMapKeyAndValueTypes(arg0: 'Type', arg1: 'Class') -> List['Type']:
        """public static java.lang.reflect.Type[] com.google.gson.internal.$Gson$Types.getMapKeyAndValueTypes(java.lang.reflect.Type,java.lang.Class<?>)"""
        return List[Type].__wrap(__$Gson$Types.getMapKeyAndValueTypes(arg0, arg1))

    @staticmethod
    @overload
    def arrayOf(arg0: 'Type') -> 'GenericArrayType':
        """public static java.lang.reflect.GenericArrayType com.google.gson.internal.$Gson$Types.arrayOf(java.lang.reflect.Type)"""
        return GenericArrayType.__wrap(__$Gson$Types.arrayOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def equals(arg0: 'Type', arg1: 'Type') -> bool:
        """public static boolean com.google.gson.internal.$Gson$Types.equals(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return bool.__wrap(__$Gson$Types.equals(arg0, arg1))

    @staticmethod
    @overload
    def typeToString(arg0: 'Type') -> str:
        """public static java.lang.String com.google.gson.internal.$Gson$Types.typeToString(java.lang.reflect.Type)"""
        return str.__wrap(__$Gson$Types.typeToString(arg0))

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

    @staticmethod
    @overload
    def canonicalize(arg0: 'Type') -> 'Type':
        """public static java.lang.reflect.Type com.google.gson.internal.$Gson$Types.canonicalize(java.lang.reflect.Type)"""
        return Type.__wrap(__$Gson$Types.canonicalize(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getArrayComponentType(arg0: 'Type') -> 'Type':
        """public static java.lang.reflect.Type com.google.gson.internal.$Gson$Types.getArrayComponentType(java.lang.reflect.Type)"""
        return Type.__wrap(__$Gson$Types.getArrayComponentType(arg0))

    @staticmethod
    @overload
    def supertypeOf(arg0: 'Type') -> 'WildcardType':
        """public static java.lang.reflect.WildcardType com.google.gson.internal.$Gson$Types.supertypeOf(java.lang.reflect.Type)"""
        return WildcardType.__wrap(__$Gson$Types.supertypeOf(arg0))

    @staticmethod
    @overload
    def newParameterizedTypeWithOwner(arg0: 'Type', arg1: 'Type', *arg2: 'Type') -> 'ParameterizedType':
        """public static java.lang.reflect.ParameterizedType com.google.gson.internal.$Gson$Types.newParameterizedTypeWithOwner(java.lang.reflect.Type,java.lang.reflect.Type,java.lang.reflect.Type...)"""
        return ParameterizedType.__wrap(__$Gson$Types.newParameterizedTypeWithOwner(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.LazilyParsedNumber
import com.google.gson.internal.LazilyParsedNumber as __LazilyParsedNumber
__LazilyParsedNumber = __LazilyParsedNumber
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
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
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class LazilyParsedNumber():
    """com.google.gson.internal.LazilyParsedNumber"""
 
    @staticmethod
    def __wrap(java_value: __LazilyParsedNumber) -> 'LazilyParsedNumber':
        return LazilyParsedNumber(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LazilyParsedNumber):
        """
        Dynamic initializer for LazilyParsedNumber.
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
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.LazilyParsedNumber.equals(java.lang.Object)"""
        return bool.__wrap(super(__LazilyParsedNumber, self).equals(arg0))

    @override
    @overload
    def floatValue(self) -> float:
        """public float com.google.gson.internal.LazilyParsedNumber.floatValue()"""
        return float.__wrap(super(LazilyParsedNumber, self).floatValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def intValue(self) -> int:
        """public int com.google.gson.internal.LazilyParsedNumber.intValue()"""
        return int.__wrap(super(LazilyParsedNumber, self).intValue())

    @overload
    def __init__(self, arg0: str):
        """public com.google.gson.internal.LazilyParsedNumber(java.lang.String)"""
        val = __LazilyParsedNumber(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def longValue(self) -> int:
        """public long com.google.gson.internal.LazilyParsedNumber.longValue()"""
        return int.__wrap(super(LazilyParsedNumber, self).longValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def doubleValue(self) -> float:
        """public double com.google.gson.internal.LazilyParsedNumber.doubleValue()"""
        return float.__wrap(super(LazilyParsedNumber, self).doubleValue())

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.internal.LazilyParsedNumber.hashCode()"""
        return int.__wrap(super(LazilyParsedNumber, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.gson.internal.LazilyParsedNumber.toString()"""
        return str.__wrap(super(LazilyParsedNumber, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.gson.internal.UnsafeAllocator
from builtins import str
from pyquantum_helper import override
import com.google.gson.internal.UnsafeAllocator as __UnsafeAllocator
__UnsafeAllocator = __UnsafeAllocator
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
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
 
class UnsafeAllocator(ABC):
    """com.google.gson.internal.UnsafeAllocator"""
 
    @staticmethod
    def __wrap(java_value: __UnsafeAllocator) -> 'UnsafeAllocator':
        return UnsafeAllocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnsafeAllocator):
        """
        Dynamic initializer for UnsafeAllocator.
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

    @abstractmethod
    def newInstance(self, arg0: 'Class'):
        """public abstract <T> T com.google.gson.internal.UnsafeAllocator.newInstance(java.lang.Class<T>) throws java.lang.Exception"""
        pass

    @overload
    def __init__(self):
        """public com.google.gson.internal.UnsafeAllocator()"""
        val = __UnsafeAllocator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.UnsafeAllocator()"""
        val = __UnsafeAllocator()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.google.gson.internal.NonNullElementWrapperList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
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
import java.util.ArrayList as ArrayList
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.AbstractList as __AbstractList
__AbstractList = __AbstractList
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import com.google.gson.internal.NonNullElementWrapperList as __NonNullElementWrapperList
__NonNullElementWrapperList = __NonNullElementWrapperList
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class NonNullElementWrapperList():
    """com.google.gson.internal.NonNullElementWrapperList"""
 
    @staticmethod
    def __wrap(java_value: __NonNullElementWrapperList) -> 'NonNullElementWrapperList':
        return NonNullElementWrapperList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NonNullElementWrapperList):
        """
        Dynamic initializer for NonNullElementWrapperList.
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
    def contains(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.contains(java.lang.Object)"""
        return bool.__wrap(super(__NonNullElementWrapperList, self).contains(arg0))

    @overload
    def __init__(self, arg0: 'ArrayList'):
        """public com.google.gson.internal.NonNullElementWrapperList(java.util.ArrayList<E>)"""
        val = __NonNullElementWrapperList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void com.google.gson.internal.NonNullElementWrapperList.add(int,E)"""
        super(__NonNullElementWrapperList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.AbstractList.listIterator()"""
        return 'ListIterator'.__wrap(super(AbstractList, self).listIterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__NonNullElementWrapperList, self).retainAll(arg0))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.AbstractList.iterator()"""
        return 'Iterator'.__wrap(super(AbstractList, self).iterator())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.AbstractList.subList(int,int)"""
        return 'List'.__wrap(super(__AbstractList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

    @override
    @overload
    def clear(self):
        """public void com.google.gson.internal.NonNullElementWrapperList.clear()"""
        super(NonNullElementWrapperList, self).clear()

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] com.google.gson.internal.NonNullElementWrapperList.toArray(T[])"""
        return List[object].__wrap(super(__NonNullElementWrapperList, self).toArray(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractList.add(E)"""
        return bool.__wrap(super(__AbstractList, self).add(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E com.google.gson.internal.NonNullElementWrapperList.remove(int)"""
        return object.__wrap(super(__NonNullElementWrapperList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool.__wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.remove(java.lang.Object)"""
        return bool.__wrap(super(__NonNullElementWrapperList, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] com.google.gson.internal.NonNullElementWrapperList.toArray()"""
        return List[object].__wrap(super(NonNullElementWrapperList, self).toArray())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.AbstractList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.gson.internal.NonNullElementWrapperList.hashCode()"""
        return int.__wrap(super(NonNullElementWrapperList, self).hashCode())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__NonNullElementWrapperList, self).removeAll(arg0))

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int com.google.gson.internal.NonNullElementWrapperList.size()"""
        return int.__wrap(super(NonNullElementWrapperList, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int com.google.gson.internal.NonNullElementWrapperList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__NonNullElementWrapperList, self).lastIndexOf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E com.google.gson.internal.NonNullElementWrapperList.get(int)"""
        return object.__wrap(super(__NonNullElementWrapperList, self).get(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.google.gson.internal.NonNullElementWrapperList.equals(java.lang.Object)"""
        return bool.__wrap(super(__NonNullElementWrapperList, self).equals(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E com.google.gson.internal.NonNullElementWrapperList.set(int,E)"""
        return object.__wrap(super(__NonNullElementWrapperList, self).set(__int.valueOf(arg0), arg1))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int com.google.gson.internal.NonNullElementWrapperList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__NonNullElementWrapperList, self).indexOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.AbstractList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__AbstractList, self).listIterator(__int.valueOf(arg0)))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed()) 
 
 
# CLASS: com.google.gson.internal.ObjectConstructor
import com.google.gson.internal.ObjectConstructor as __ObjectConstructor
__ObjectConstructor = __ObjectConstructor
from abc import abstractmethod, ABC
 
class ObjectConstructor(ABC):
    """com.google.gson.internal.ObjectConstructor"""
 
    @staticmethod
    def __wrap(java_value: __ObjectConstructor) -> 'ObjectConstructor':
        return ObjectConstructor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectConstructor):
        """
        Dynamic initializer for ObjectConstructor.
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
    def construct(self, ):
        """public abstract T com.google.gson.internal.ObjectConstructor.construct()"""
        pass 
 
 
# CLASS: com.google.gson.internal.ReflectionAccessFilterHelper
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.gson.internal.ReflectionAccessFilterHelper as __ReflectionAccessFilterHelper
__ReflectionAccessFilterHelper = __ReflectionAccessFilterHelper
from builtins import type
import com.google.gson.ReflectionAccessFilter as __ReflectionAccessFilter_FilterResult
__FilterResult = __ReflectionAccessFilter_FilterResult.FilterResult
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.reflect.AccessibleObject as AccessibleObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ReflectionAccessFilterHelper():
    """com.google.gson.internal.ReflectionAccessFilterHelper"""
 
    @staticmethod
    def __wrap(java_value: __ReflectionAccessFilterHelper) -> 'ReflectionAccessFilterHelper':
        return ReflectionAccessFilterHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectionAccessFilterHelper):
        """
        Dynamic initializer for ReflectionAccessFilterHelper.
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
    def getFilterResult(arg0: 'List', arg1: 'Class') -> 'pygson.ReflectionAccessFilter$FilterResult':
        """public static com.google.gson.ReflectionAccessFilter$FilterResult com.google.gson.internal.ReflectionAccessFilterHelper.getFilterResult(java.util.List<com.google.gson.ReflectionAccessFilter>,java.lang.Class<?>)"""
        return pygson.ReflectionAccessFilter$FilterResult.__wrap(__ReflectionAccessFilterHelper.getFilterResult(arg0, arg1))

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
    def isAndroidType(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.ReflectionAccessFilterHelper.isAndroidType(java.lang.Class<?>)"""
        return bool.__wrap(__ReflectionAccessFilterHelper.isAndroidType(arg0))

    @staticmethod
    @overload
    def canAccess(arg0: 'AccessibleObject', arg1: object) -> bool:
        """public static boolean com.google.gson.internal.ReflectionAccessFilterHelper.canAccess(java.lang.reflect.AccessibleObject,java.lang.Object)"""
        return bool.__wrap(__ReflectionAccessFilterHelper.canAccess(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isJavaType(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.ReflectionAccessFilterHelper.isJavaType(java.lang.Class<?>)"""
        return bool.__wrap(__ReflectionAccessFilterHelper.isJavaType(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def isAnyPlatformType(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.ReflectionAccessFilterHelper.isAnyPlatformType(java.lang.Class<?>)"""
        return bool.__wrap(__ReflectionAccessFilterHelper.isAnyPlatformType(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.Streams
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import com.google.gson.JsonElement as __JsonElement
__JsonElement = __JsonElement
import java.lang.Appendable as Appendable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.google.gson.internal.Streams as __Streams
__Streams = __Streams
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class Streams():
    """com.google.gson.internal.Streams"""
 
    @staticmethod
    def __wrap(java_value: __Streams) -> 'Streams':
        return Streams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Streams):
        """
        Dynamic initializer for Streams.
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

    @staticmethod
    @overload
    def writerForAppendable(arg0: 'Appendable') -> 'Writer':
        """public static java.io.Writer com.google.gson.internal.Streams.writerForAppendable(java.lang.Appendable)"""
        return Writer.__wrap(__Streams.writerForAppendable(arg0))

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
    def write(arg0: 'JsonElement', arg1: 'JsonWriter'):
        """public static void com.google.gson.internal.Streams.write(com.google.gson.JsonElement,com.google.gson.stream.JsonWriter) throws java.io.IOException"""
        __Streams.write(arg0, arg1)

    @staticmethod
    @overload
    def parse(arg0: 'JsonReader') -> 'pygson.JsonElement':
        """public static com.google.gson.JsonElement com.google.gson.internal.Streams.parse(com.google.gson.stream.JsonReader) throws com.google.gson.JsonParseException"""
        return pygson.JsonElement.__wrap(__Streams.parse(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.gson.internal.JavaVersion
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.gson.internal.JavaVersion as __JavaVersion
__JavaVersion = __JavaVersion
from builtins import int
 
class JavaVersion():
    """com.google.gson.internal.JavaVersion"""
 
    @staticmethod
    def __wrap(java_value: __JavaVersion) -> 'JavaVersion':
        return JavaVersion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JavaVersion):
        """
        Dynamic initializer for JavaVersion.
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

    @staticmethod
    @overload
    def getMajorJavaVersion() -> int:
        """public static int com.google.gson.internal.JavaVersion.getMajorJavaVersion()"""
        return int.__wrap(__JavaVersion.getMajorJavaVersion())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isJava9OrLater() -> bool:
        """public static boolean com.google.gson.internal.JavaVersion.isJava9OrLater()"""
        return bool.__wrap(__JavaVersion.isJava9OrLater())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.gson.internal.GsonBuildConfig
import com.google.gson.internal.GsonBuildConfig as __GsonBuildConfig
__GsonBuildConfig = __GsonBuildConfig
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GsonBuildConfig():
    """com.google.gson.internal.GsonBuildConfig"""
 
    @staticmethod
    def __wrap(java_value: __GsonBuildConfig) -> 'GsonBuildConfig':
        return GsonBuildConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GsonBuildConfig):
        """
        Dynamic initializer for GsonBuildConfig.
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.gson.internal.Primitives
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Type as Type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.gson.internal.Primitives as __Primitives
__Primitives = __Primitives
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Primitives():
    """com.google.gson.internal.Primitives"""
 
    @staticmethod
    def __wrap(java_value: __Primitives) -> 'Primitives':
        return Primitives(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Primitives):
        """
        Dynamic initializer for Primitives.
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
    def unwrap(arg0: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> com.google.gson.internal.Primitives.unwrap(java.lang.Class<T>)"""
        return type.Class.__wrap(__Primitives.unwrap(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def wrap(arg0: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> com.google.gson.internal.Primitives.wrap(java.lang.Class<T>)"""
        return type.Class.__wrap(__Primitives.wrap(arg0))

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

    @staticmethod
    @overload
    def isWrapperType(arg0: 'Type') -> bool:
        """public static boolean com.google.gson.internal.Primitives.isWrapperType(java.lang.reflect.Type)"""
        return bool.__wrap(__Primitives.isWrapperType(arg0))

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

    @staticmethod
    @overload
    def isPrimitive(arg0: 'Type') -> bool:
        """public static boolean com.google.gson.internal.Primitives.isPrimitive(java.lang.reflect.Type)"""
        return bool.__wrap(__Primitives.isPrimitive(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.gson.internal.$Gson$Preconditions
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.gson.internal. as ___Gson_Preconditions
__$Gson$Preconditions = ___Gson_Preconditions.Gson.Preconditions
from builtins import object
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
 
class $Gson$Preconditions():
    """com.google.gson.internal..Gson.Preconditions"""
 
    @staticmethod
    def __wrap(java_value: __$Gson$Preconditions) -> '$Gson$Preconditions':
        return $Gson$Preconditions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __$Gson$Preconditions):
        """
        Dynamic initializer for $Gson$Preconditions.
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

    @staticmethod
    @overload
    def checkArgument(arg0: bool):
        """public static void com.google.gson.internal.$Gson$Preconditions.checkArgument(boolean)"""
        __$Gson$Preconditions.checkArgument(__boolean.valueOf(arg0))

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
    def checkNotNull(arg0: object) -> object:
        """public static <T> T com.google.gson.internal.$Gson$Preconditions.checkNotNull(T)"""
        return object.__wrap(__$Gson$Preconditions.checkNotNull(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.gson.internal.PreJava9DateFormatProvider
import com.google.gson.internal.PreJava9DateFormatProvider as __PreJava9DateFormatProvider
__PreJava9DateFormatProvider = __PreJava9DateFormatProvider
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.text.DateFormat as __DateFormat
__DateFormat = __DateFormat
import java.lang.Object as __Object
__Object = __Object
import java.text.DateFormat as DateFormat
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PreJava9DateFormatProvider():
    """com.google.gson.internal.PreJava9DateFormatProvider"""
 
    @staticmethod
    def __wrap(java_value: __PreJava9DateFormatProvider) -> 'PreJava9DateFormatProvider':
        return PreJava9DateFormatProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PreJava9DateFormatProvider):
        """
        Dynamic initializer for PreJava9DateFormatProvider.
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
    def __init__(self, ):
        """public com.google.gson.internal.PreJava9DateFormatProvider()"""
        val = __PreJava9DateFormatProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getUSDateFormat(arg0: int) -> 'DateFormat':
        """public static java.text.DateFormat com.google.gson.internal.PreJava9DateFormatProvider.getUSDateFormat(int)"""
        return DateFormat.__wrap(__PreJava9DateFormatProvider.getUSDateFormat(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getUSDateTimeFormat(arg0: int, arg1: int) -> 'DateFormat':
        """public static java.text.DateFormat com.google.gson.internal.PreJava9DateFormatProvider.getUSDateTimeFormat(int,int)"""
        return DateFormat.__wrap(__PreJava9DateFormatProvider.getUSDateTimeFormat(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def __init__(self):
        """public com.google.gson.internal.PreJava9DateFormatProvider()"""
        val = __PreJava9DateFormatProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.google.gson.internal.ConstructorConstructor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

import com.google.gson.internal.ObjectConstructor as __ObjectConstructor
__ObjectConstructor = __ObjectConstructor
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
import com.google.gson.internal.ConstructorConstructor as __ConstructorConstructor
__ConstructorConstructor = __ConstructorConstructor
from builtins import int
import java.util.List as List
 
class ConstructorConstructor():
    """com.google.gson.internal.ConstructorConstructor"""
 
    @staticmethod
    def __wrap(java_value: __ConstructorConstructor) -> 'ConstructorConstructor':
        return ConstructorConstructor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstructorConstructor):
        """
        Dynamic initializer for ConstructorConstructor.
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
    def toString(self) -> str:
        """public java.lang.String com.google.gson.internal.ConstructorConstructor.toString()"""
        return str.__wrap(super(ConstructorConstructor, self).toString())

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

    @overload
    def get(self, arg0: 'TypeToken') -> 'ObjectConstructor':
        """public <T> com.google.gson.internal.ObjectConstructor<T> com.google.gson.internal.ConstructorConstructor.get(com.google.gson.reflect.TypeToken<T>)"""
        return 'ObjectConstructor'.__wrap(super(__ConstructorConstructor, self).get(arg0))

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Map', arg1: bool, arg2: 'List'):
        """public com.google.gson.internal.ConstructorConstructor(java.util.Map<java.lang.reflect.Type, com.google.gson.InstanceCreator<?>>,boolean,java.util.List<com.google.gson.ReflectionAccessFilter>)"""
        val = __ConstructorConstructor(arg0, __boolean.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.gson.internal.JsonReaderInternalAccess
from pyquantum_helper import import_once as __import_once__
import com.google.gson.internal.JsonReaderInternalAccess as __JsonReaderInternalAccess
__JsonReaderInternalAccess = __JsonReaderInternalAccess
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygson import stream
except ImportError:
    stream = __import_once__("pygson.stream")

from builtins import int
 
class JsonReaderInternalAccess(ABC):
    """com.google.gson.internal.JsonReaderInternalAccess"""
 
    @staticmethod
    def __wrap(java_value: __JsonReaderInternalAccess) -> 'JsonReaderInternalAccess':
        return JsonReaderInternalAccess(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonReaderInternalAccess):
        """
        Dynamic initializer for JsonReaderInternalAccess.
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

    @abstractmethod
    def promoteNameToValue(self, arg0: 'JsonReader'):
        """public abstract void com.google.gson.internal.JsonReaderInternalAccess.promoteNameToValue(com.google.gson.stream.JsonReader) throws java.io.IOException"""
        pass

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.JsonReaderInternalAccess()"""
        val = __JsonReaderInternalAccess()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.google.gson.internal.JsonReaderInternalAccess()"""
        val = __JsonReaderInternalAccess()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.google.gson.internal.Excluder
from pyquantum_helper import import_once as __import_once__
try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import com.google.gson.internal.Excluder as __Excluder
__Excluder = __Excluder
from builtins import type
import java.lang.reflect.Field as Field
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygson import reflect
except ImportError:
    reflect = __import_once__("pygson.reflect")

import com.google.gson.TypeAdapter as __TypeAdapter
__TypeAdapter = __TypeAdapter
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Excluder():
    """com.google.gson.internal.Excluder"""
 
    @staticmethod
    def __wrap(java_value: __Excluder) -> 'Excluder':
        return Excluder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Excluder):
        """
        Dynamic initializer for Excluder.
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
    def excludeFieldsWithoutExposeAnnotation(self) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.excludeFieldsWithoutExposeAnnotation()"""
        return 'Excluder'.__wrap(super(Excluder, self).excludeFieldsWithoutExposeAnnotation())

    @overload
    def __init__(self):
        """public com.google.gson.internal.Excluder()"""
        val = __Excluder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def withVersion(self, arg0: float) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.withVersion(double)"""
        return 'Excluder'.__wrap(super(__Excluder, self).withVersion(__double.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.Excluder()"""
        val = __Excluder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def create(self, arg0: 'Gson', arg1: 'TypeToken') -> 'pygson.TypeAdapter':
        """public <T> com.google.gson.TypeAdapter<T> com.google.gson.internal.Excluder.create(com.google.gson.Gson,com.google.gson.reflect.TypeToken<T>)"""
        return 'pygson.TypeAdapter'.__wrap(super(__Excluder, self).create(arg0, arg1))

    @overload
    def withExclusionStrategy(self, arg0: 'ExclusionStrategy', arg1: bool, arg2: bool) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.withExclusionStrategy(com.google.gson.ExclusionStrategy,boolean,boolean)"""
        return 'Excluder'.__wrap(super(__Excluder, self).withExclusionStrategy(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def withModifiers(self, *arg0: int) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.withModifiers(int...)"""
        return 'Excluder'.__wrap(super(__Excluder, self).withModifiers(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def disableInnerClassSerialization(self) -> 'Excluder':
        """public com.google.gson.internal.Excluder com.google.gson.internal.Excluder.disableInnerClassSerialization()"""
        return 'Excluder'.__wrap(super(Excluder, self).disableInnerClassSerialization())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def excludeField(self, arg0: 'Field', arg1: bool) -> bool:
        """public boolean com.google.gson.internal.Excluder.excludeField(java.lang.reflect.Field,boolean)"""
        return bool.__wrap(super(__Excluder, self).excludeField(arg0, __boolean.valueOf(arg1)))

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
    def excludeClass(self, arg0: 'Class', arg1: bool) -> bool:
        """public boolean com.google.gson.internal.Excluder.excludeClass(java.lang.Class<?>,boolean)"""
        return bool.__wrap(super(__Excluder, self).excludeClass(arg0, __boolean.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))