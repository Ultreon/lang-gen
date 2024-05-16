from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.LongMap as __LongMap_Entries
__Entries = __LongMap_Entries.Entries
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.LongMap as __LongMap_Keys
__Keys = __LongMap_Keys.Keys
import com.badlogic.gdx.utils.LongMap as __LongMap
__LongMap = __LongMap
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.LongMap as __LongMap_Values
__Values = __LongMap_Values.Values
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class LongMap():
    """com.badlogic.gdx.utils.LongMap"""
 
    @staticmethod
    def __wrap(java_value: __LongMap) -> 'LongMap':
        return LongMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongMap):
        """
        Dynamic initializer for LongMap.
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
    def putAll(self, arg0: 'LongMap'):
        """public void com.badlogic.gdx.utils.LongMap.putAll(com.badlogic.gdx.utils.LongMap<? extends V>)"""
        super(__LongMap, self).putAll(arg0)

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.LongMap$Values<V> com.badlogic.gdx.utils.LongMap.values()"""
        return 'Values'.__wrap(super(LongMap, self).values())

    @overload
    def findKey(self, arg0: object, arg1: bool, arg2: int) -> int:
        """public long com.badlogic.gdx.utils.LongMap.findKey(java.lang.Object,boolean,long)"""
        return int.__wrap(super(__LongMap, self).findKey(arg0, __boolean.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: int) -> object:
        """public V com.badlogic.gdx.utils.LongMap.remove(long)"""
        return object.__wrap(super(__LongMap, self).remove(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__LongMap, self).equals(arg0))

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongMap.clear(int)"""
        super(__LongMap, self).clear(__int.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.LongMap()"""
        val = __LongMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.LongMap$Entries<V> com.badlogic.gdx.utils.LongMap.entries()"""
        return 'Entries'.__wrap(super(LongMap, self).entries())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.LongMap.clear()"""
        super(LongMap, self).clear()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.containsValue(java.lang.Object,boolean)"""
        return bool.__wrap(super(__LongMap, self).containsValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def get(self, arg0: int) -> object:
        """public V com.badlogic.gdx.utils.LongMap.get(long)"""
        return object.__wrap(super(__LongMap, self).get(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'LongMap'):
        """public com.badlogic.gdx.utils.LongMap(com.badlogic.gdx.utils.LongMap<? extends V>)"""
        val = __LongMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.LongMap$Entry<V>> com.badlogic.gdx.utils.LongMap.iterator()"""
        return 'Iterator'.__wrap(super(LongMap, self).iterator())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.LongMap(int,float)"""
        val = __LongMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.LongMap.hashCode()"""
        return int.__wrap(super(LongMap, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.LongMap.toString()"""
        return str.__wrap(super(LongMap, self).toString())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.notEmpty()"""
        return bool.__wrap(super(LongMap, self).notEmpty())

    @overload
    def get(self, arg0: int, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.LongMap.get(long,V)"""
        return object.__wrap(super(__LongMap, self).get(__long.valueOf(arg0), arg1))

    @overload
    def containsKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.containsKey(long)"""
        return bool.__wrap(super(__LongMap, self).containsKey(__long.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.LongMap.put(long,V)"""
        return object.__wrap(super(__LongMap, self).put(__long.valueOf(arg0), arg1))

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.LongMap$Keys com.badlogic.gdx.utils.LongMap.keys()"""
        return 'Keys'.__wrap(super(LongMap, self).keys())

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.LongMap(int)"""
        val = __LongMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.isEmpty()"""
        return bool.__wrap(super(LongMap, self).isEmpty())

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongMap.shrink(int)"""
        super(__LongMap, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.LongMap()"""
        val = __LongMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongMap.ensureCapacity(int)"""
        super(__LongMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__LongMap, self).equalsIdentity(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.LongMap
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.LongMap as __LongMap_Entries
__Entries = __LongMap_Entries.Entries
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.LongMap as __LongMap_Keys
__Keys = __LongMap_Keys.Keys
import com.badlogic.gdx.utils.LongMap as __LongMap
__LongMap = __LongMap
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.LongMap as __LongMap_Values
__Values = __LongMap_Values.Values
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class LongMap():
    """com.badlogic.gdx.utils.LongMap"""
 
    @staticmethod
    def __wrap(java_value: __LongMap) -> 'LongMap':
        return LongMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongMap):
        """
        Dynamic initializer for LongMap.
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
    def putAll(self, arg0: 'LongMap'):
        """public void com.badlogic.gdx.utils.LongMap.putAll(com.badlogic.gdx.utils.LongMap<? extends V>)"""
        super(__LongMap, self).putAll(arg0)

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.LongMap$Values<V> com.badlogic.gdx.utils.LongMap.values()"""
        return 'Values'.__wrap(super(LongMap, self).values())

    @overload
    def findKey(self, arg0: object, arg1: bool, arg2: int) -> int:
        """public long com.badlogic.gdx.utils.LongMap.findKey(java.lang.Object,boolean,long)"""
        return int.__wrap(super(__LongMap, self).findKey(arg0, __boolean.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: int) -> object:
        """public V com.badlogic.gdx.utils.LongMap.remove(long)"""
        return object.__wrap(super(__LongMap, self).remove(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__LongMap, self).equals(arg0))

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongMap.clear(int)"""
        super(__LongMap, self).clear(__int.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.LongMap()"""
        val = __LongMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.LongMap$Entries<V> com.badlogic.gdx.utils.LongMap.entries()"""
        return 'Entries'.__wrap(super(LongMap, self).entries())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.LongMap.clear()"""
        super(LongMap, self).clear()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def containsValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.containsValue(java.lang.Object,boolean)"""
        return bool.__wrap(super(__LongMap, self).containsValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def get(self, arg0: int) -> object:
        """public V com.badlogic.gdx.utils.LongMap.get(long)"""
        return object.__wrap(super(__LongMap, self).get(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'LongMap'):
        """public com.badlogic.gdx.utils.LongMap(com.badlogic.gdx.utils.LongMap<? extends V>)"""
        val = __LongMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.LongMap$Entry<V>> com.badlogic.gdx.utils.LongMap.iterator()"""
        return 'Iterator'.__wrap(super(LongMap, self).iterator())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.LongMap(int,float)"""
        val = __LongMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.LongMap.hashCode()"""
        return int.__wrap(super(LongMap, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.LongMap.toString()"""
        return str.__wrap(super(LongMap, self).toString())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.notEmpty()"""
        return bool.__wrap(super(LongMap, self).notEmpty())

    @overload
    def get(self, arg0: int, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.LongMap.get(long,V)"""
        return object.__wrap(super(__LongMap, self).get(__long.valueOf(arg0), arg1))

    @overload
    def containsKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.containsKey(long)"""
        return bool.__wrap(super(__LongMap, self).containsKey(__long.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.LongMap.put(long,V)"""
        return object.__wrap(super(__LongMap, self).put(__long.valueOf(arg0), arg1))

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.LongMap$Keys com.badlogic.gdx.utils.LongMap.keys()"""
        return 'Keys'.__wrap(super(LongMap, self).keys())

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.LongMap(int)"""
        val = __LongMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.isEmpty()"""
        return bool.__wrap(super(LongMap, self).isEmpty())

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongMap.shrink(int)"""
        super(__LongMap, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.LongMap()"""
        val = __LongMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongMap.ensureCapacity(int)"""
        super(__LongMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__LongMap, self).equalsIdentity(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.LongMap 
 
 
# CLASS: com.badlogic.gdx.utils.LongArray
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from typing import List
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
import com.badlogic.gdx.utils.LongArray as __LongArray
__LongArray = __LongArray
from builtins import int
 
class LongArray():
    """com.badlogic.gdx.utils.LongArray"""
 
    @staticmethod
    def __wrap(java_value: __LongArray) -> 'LongArray':
        return LongArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongArray):
        """
        Dynamic initializer for LongArray.
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
    def addAll(self, arg0: 'LongArray', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.LongArray.addAll(com.badlogic.gdx.utils.LongArray,int,int)"""
        super(__LongArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def removeAll(self, arg0: 'LongArray') -> bool:
        """public boolean com.badlogic.gdx.utils.LongArray.removeAll(com.badlogic.gdx.utils.LongArray)"""
        return bool.__wrap(super(__LongArray, self).removeAll(arg0))

    @overload
    def first(self) -> int:
        """public long com.badlogic.gdx.utils.LongArray.first()"""
        return int.__wrap(super(LongArray, self).first())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.LongArray(int)"""
        val = __LongArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def indexOf(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.LongArray.indexOf(long)"""
        return int.__wrap(super(__LongArray, self).indexOf(__long.valueOf(arg0)))

    @overload
    def incr(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongArray.incr(long)"""
        super(__LongArray, self).incr(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.LongArray()"""
        val = __LongArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def mul(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongArray.mul(long)"""
        super(__LongArray, self).mul(__long.valueOf(arg0))

    @overload
    def setSize(self, arg0: int) -> List[int]:
        """public long[] com.badlogic.gdx.utils.LongArray.setSize(int)"""
        return List[int].__wrap(super(__LongArray, self).setSize(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: bool, arg1: 'long', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.LongArray(boolean,long[],int,int)"""
        val = __LongArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.LongArray.insertRange(int,int)"""
        super(__LongArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def add(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.LongArray.add(long,long,long,long)"""
        super(__LongArray, self).add(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @overload
    def removeValue(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.LongArray.removeValue(long)"""
        return bool.__wrap(super(__LongArray, self).removeValue(__long.valueOf(arg0)))

    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.LongArray.sort()"""
        super(LongArray, self).sort()

    @overload
    def add(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongArray.add(long)"""
        super(__LongArray, self).add(__long.valueOf(arg0))

    @overload
    def random(self) -> int:
        """public long com.badlogic.gdx.utils.LongArray.random()"""
        return int.__wrap(super(LongArray, self).random())

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.LongArray.lastIndexOf(char)"""
        return int.__wrap(super(__LongArray, self).lastIndexOf(__char.valueOf(arg0)))

    @overload
    def contains(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.LongArray.contains(long)"""
        return bool.__wrap(super(__LongArray, self).contains(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def with(*arg0: int) -> 'LongArray':
        """public static com.badlogic.gdx.utils.LongArray com.badlogic.gdx.utils.LongArray.with(long...)"""
        return LongArray.__wrap(__LongArray.with(arg0))

    @overload
    def addAll(self, arg0: 'long', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.LongArray.addAll(long[],int,int)"""
        super(__LongArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def addAll(self, *arg0: int):
        """public void com.badlogic.gdx.utils.LongArray.addAll(long...)"""
        super(__LongArray, self).addAll(arg0)

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongArray.notEmpty()"""
        return bool.__wrap(super(LongArray, self).notEmpty())

    @overload
    def mul(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.LongArray.mul(int,long)"""
        super(__LongArray, self).mul(__int.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.LongArray.shuffle()"""
        super(LongArray, self).shuffle()

    @overload
    def add(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.LongArray.add(long,long)"""
        super(__LongArray, self).add(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongArray.isEmpty()"""
        return bool.__wrap(super(LongArray, self).isEmpty())

    @overload
    def __init__(self, arg0: 'long'):
        """public com.badlogic.gdx.utils.LongArray(long[])"""
        val = __LongArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def peek(self) -> int:
        """public long com.badlogic.gdx.utils.LongArray.peek()"""
        return int.__wrap(super(LongArray, self).peek())

    @overload
    def toArray(self) -> List[int]:
        """public long[] com.badlogic.gdx.utils.LongArray.toArray()"""
        return List[int].__wrap(super(LongArray, self).toArray())

    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.LongArray.removeRange(int,int)"""
        super(__LongArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.LongArray.set(int,long)"""
        super(__LongArray, self).set(__int.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def get(self, arg0: int) -> int:
        """public long com.badlogic.gdx.utils.LongArray.get(int)"""
        return int.__wrap(super(__LongArray, self).get(__int.valueOf(arg0)))

    @overload
    def shrink(self) -> List[int]:
        """public long[] com.badlogic.gdx.utils.LongArray.shrink()"""
        return List[int].__wrap(super(LongArray, self).shrink())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.LongArray.toString(java.lang.String)"""
        return str.__wrap(super(__LongArray, self).toString(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.LongArray()"""
        val = __LongArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ensureCapacity(self, arg0: int) -> List[int]:
        """public long[] com.badlogic.gdx.utils.LongArray.ensureCapacity(int)"""
        return List[int].__wrap(super(__LongArray, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def incr(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.LongArray.incr(int,long)"""
        super(__LongArray, self).incr(__int.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def add(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.LongArray.add(long,long,long)"""
        super(__LongArray, self).add(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.LongArray.swap(int,int)"""
        super(__LongArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.LongArray.reverse()"""
        super(LongArray, self).reverse()

    @overload
    def __init__(self, arg0: 'LongArray'):
        """public com.badlogic.gdx.utils.LongArray(com.badlogic.gdx.utils.LongArray)"""
        val = __LongArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.LongArray.hashCode()"""
        return int.__wrap(super(LongArray, self).hashCode())

    @overload
    def insert(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.LongArray.insert(int,long)"""
        super(__LongArray, self).insert(__int.valueOf(arg0), __long.valueOf(arg1))

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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.LongArray.toString()"""
        return str.__wrap(super(LongArray, self).toString())

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongArray.truncate(int)"""
        super(__LongArray, self).truncate(__int.valueOf(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.LongArray.clear()"""
        super(LongArray, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.LongArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__LongArray, self).equals(arg0))

    @overload
    def removeIndex(self, arg0: int) -> int:
        """public long com.badlogic.gdx.utils.LongArray.removeIndex(int)"""
        return int.__wrap(super(__LongArray, self).removeIndex(__int.valueOf(arg0)))

    @overload
    def pop(self) -> int:
        """public long com.badlogic.gdx.utils.LongArray.pop()"""
        return int.__wrap(super(LongArray, self).pop())

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.LongArray(boolean,int)"""
        val = __LongArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAll(self, arg0: 'LongArray'):
        """public void com.badlogic.gdx.utils.LongArray.addAll(com.badlogic.gdx.utils.LongArray)"""
        super(__LongArray, self).addAll(arg0) 
 
 
# CLASS: com.badlogic.gdx.utils.DataInput
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.io.FilterInputStream as __FilterInputStream
__FilterInputStream = __FilterInputStream
import java.io.DataInput as DataInput
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import com.badlogic.gdx.utils.DataInput as __DataInput
__DataInput = __DataInput
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.io.DataInputStream as __DataInputStream
__DataInputStream = __DataInputStream
from builtins import int
 
class DataInput():
    """com.badlogic.gdx.utils.DataInput"""
 
    @staticmethod
    def __wrap(java_value: __DataInput) -> 'DataInput':
        return DataInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataInput):
        """
        Dynamic initializer for DataInput.
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
    def readByte(self) -> int:
        """public final byte java.io.DataInputStream.readByte() throws java.io.IOException"""
        return int.__wrap(super(DataInputStream, self).readByte())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def readLong(self) -> int:
        """public final long java.io.DataInputStream.readLong() throws java.io.IOException"""
        return int.__wrap(super(DataInputStream, self).readLong())

    @staticmethod
    @overload
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream.__wrap(__InputStream.nullInputStream())

    @overload
    def readInt(self, arg0: bool) -> int:
        """public int com.badlogic.gdx.utils.DataInput.readInt(boolean) throws java.io.IOException"""
        return int.__wrap(super(__DataInput, self).readInt(__boolean.valueOf(arg0)))

    @override
    @overload
    def read(self) -> int:
        """public int java.io.FilterInputStream.read() throws java.io.IOException"""
        return int.__wrap(super(FilterInputStream, self).read())

    @override
    @overload
    def available(self) -> int:
        """public int java.io.FilterInputStream.available() throws java.io.IOException"""
        return int.__wrap(super(FilterInputStream, self).available())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'InputStream'):
        """public com.badlogic.gdx.utils.DataInput(java.io.InputStream)"""
        val = __DataInput(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def readInt(self) -> int:
        """public final int java.io.DataInputStream.readInt() throws java.io.IOException"""
        return int.__wrap(super(DataInputStream, self).readInt())

    @override
    @overload
    def readFully(self, arg0: bytes):
        """public final void java.io.DataInputStream.readFully(byte[]) throws java.io.IOException"""
        super(__DataInputStream, self).readFully(bytes)

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean java.io.FilterInputStream.markSupported()"""
        return bool.__wrap(super(FilterInputStream, self).markSupported())

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int].__wrap(super(InputStream, self).readAllBytes())

    @overload
    def read(self, arg0: bytes) -> int:
        """public final int java.io.DataInputStream.read(byte[]) throws java.io.IOException"""
        return int.__wrap(super(__DataInputStream, self).read(bytes))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def skipBytes(self, arg0: int) -> int:
        """public final int java.io.DataInputStream.skipBytes(int) throws java.io.IOException"""
        return int.__wrap(super(__DataInputStream, self).skipBytes(__int.valueOf(arg0)))

    @overload
    def read(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public final int java.io.DataInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__DataInputStream, self).read(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def readDouble(self) -> float:
        """public final double java.io.DataInputStream.readDouble() throws java.io.IOException"""
        return float.__wrap(super(DataInputStream, self).readDouble())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def readLine(self) -> str:
        """public final java.lang.String java.io.DataInputStream.readLine() throws java.io.IOException"""
        return str.__wrap(super(DataInputStream, self).readLine())

    @override
    @overload
    def readUTF(self) -> str:
        """public final java.lang.String java.io.DataInputStream.readUTF() throws java.io.IOException"""
        return str.__wrap(super(DataInputStream, self).readUTF())

    @override
    @overload
    def readFully(self, arg0: bytes, arg1: int, arg2: int):
        """public final void java.io.DataInputStream.readFully(byte[],int,int) throws java.io.IOException"""
        super(__DataInputStream, self).readFully(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def reset(self):
        """public void java.io.FilterInputStream.reset() throws java.io.IOException"""
        super(FilterInputStream, self).reset()

    @overload
    def skip(self, arg0: int) -> int:
        """public long java.io.FilterInputStream.skip(long) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).skip(__long.valueOf(arg0)))

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).transferTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def readChar(self) -> str:
        """public final char java.io.DataInputStream.readChar() throws java.io.IOException"""
        return str.__wrap(super(DataInputStream, self).readChar())

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int].__wrap(super(__InputStream, self).readNBytes(__int.valueOf(arg0)))

    @override
    @overload
    def readFloat(self) -> float:
        """public final float java.io.DataInputStream.readFloat() throws java.io.IOException"""
        return float.__wrap(super(DataInputStream, self).readFloat())

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).readNBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def mark(self, arg0: int):
        """public void java.io.FilterInputStream.mark(int)"""
        super(__FilterInputStream, self).mark(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def close(self):
        """public void java.io.FilterInputStream.close() throws java.io.IOException"""
        super(FilterInputStream, self).close()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def readUTF(arg0: 'DataInput') -> str:
        """public static final java.lang.String java.io.DataInputStream.readUTF(java.io.DataInput) throws java.io.IOException"""
        return str.__wrap(__DataInputStream.readUTF(arg0))

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(__InputStream, self).skipNBytes(__long.valueOf(arg0))

    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.DataInput.readString() throws java.io.IOException"""
        return str.__wrap(super(DataInput, self).readString())

    @override
    @overload
    def readBoolean(self) -> bool:
        """public final boolean java.io.DataInputStream.readBoolean() throws java.io.IOException"""
        return bool.__wrap(super(DataInputStream, self).readBoolean())

    @override
    @overload
    def readUnsignedByte(self) -> int:
        """public final int java.io.DataInputStream.readUnsignedByte() throws java.io.IOException"""
        return int.__wrap(super(DataInputStream, self).readUnsignedByte())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def readUnsignedShort(self) -> int:
        """public final int java.io.DataInputStream.readUnsignedShort() throws java.io.IOException"""
        return int.__wrap(super(DataInputStream, self).readUnsignedShort())

    @override
    @overload
    def readShort(self) -> int:
        """public final short java.io.DataInputStream.readShort() throws java.io.IOException"""
        return int.__wrap(super(DataInputStream, self).readShort()) 
 
 
# CLASS: com.badlogic.gdx.utils.Null
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import com.badlogic.gdx.utils.Null as __Null
__Null = __Null
from abc import abstractmethod, ABC
 
class Null(ABC):
    """com.badlogic.gdx.utils.Null"""
 
    @staticmethod
    def __wrap(java_value: __Null) -> 'Null':
        return Null(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Null):
        """
        Dynamic initializer for Null.
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
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectSet as __ObjectSet_ObjectSetIterator
__ObjectSetIterator = __ObjectSet_ObjectSetIterator.ObjectSetIterator
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.ObjectSet as __ObjectSet
__ObjectSet = __ObjectSet
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ObjectSet():
    """com.badlogic.gdx.utils.ObjectSet"""
 
    @staticmethod
    def __wrap(java_value: __ObjectSet) -> 'ObjectSet':
        return ObjectSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectSet):
        """
        Dynamic initializer for ObjectSet.
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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.ObjectSet(int)"""
        val = __ObjectSet(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'ObjectSetIterator':
        """public com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator<T> com.badlogic.gdx.utils.ObjectSet.iterator()"""
        return 'ObjectSetIterator'.__wrap(super(ObjectSet, self).iterator())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectSet()"""
        val = __ObjectSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectSet.ensureCapacity(int)"""
        super(__ObjectSet, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.utils.ObjectSet.first()"""
        return object.__wrap(super(ObjectSet, self).first())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ObjectSet.hashCode()"""
        return int.__wrap(super(ObjectSet, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectSet()"""
        val = __ObjectSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAll(self, arg0: 'ObjectSet'):
        """public void com.badlogic.gdx.utils.ObjectSet.addAll(com.badlogic.gdx.utils.ObjectSet<T>)"""
        super(__ObjectSet, self).addAll(arg0)

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.ObjectSet(int,float)"""
        val = __ObjectSet(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.remove(T)"""
        return bool.__wrap(super(__ObjectSet, self).remove(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.add(T)"""
        return bool.__wrap(super(__ObjectSet, self).add(arg0))

    @overload
    def addAll(self, arg0: 'Array', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ObjectSet.addAll(com.badlogic.gdx.utils.Array<? extends T>,int,int)"""
        super(__ObjectSet, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectSet.shrink(int)"""
        super(__ObjectSet, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectSet.toString(java.lang.String)"""
        return str.__wrap(super(__ObjectSet, self).toString(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public T com.badlogic.gdx.utils.ObjectSet.get(T)"""
        return object.__wrap(super(__ObjectSet, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectSet, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectSet.toString()"""
        return str.__wrap(super(ObjectSet, self).toString())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.notEmpty()"""
        return bool.__wrap(super(ObjectSet, self).notEmpty())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.isEmpty()"""
        return bool.__wrap(super(ObjectSet, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ObjectSet'):
        """public com.badlogic.gdx.utils.ObjectSet(com.badlogic.gdx.utils.ObjectSet<? extends T>)"""
        val = __ObjectSet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.ObjectSet.addAll(com.badlogic.gdx.utils.Array<? extends T>)"""
        super(__ObjectSet, self).addAll(arg0)

    @staticmethod
    @overload
    def with(*arg0: object) -> 'ObjectSet':
        """public static <T> com.badlogic.gdx.utils.ObjectSet<T> com.badlogic.gdx.utils.ObjectSet.with(T...)"""
        return ObjectSet.__wrap(__ObjectSet.with(arg0))

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectSet.clear(int)"""
        super(__ObjectSet, self).clear(__int.valueOf(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.contains(T)"""
        return bool.__wrap(super(__ObjectSet, self).contains(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ObjectSet.clear()"""
        super(ObjectSet, self).clear()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def addAll(self, arg0: 'Object', arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.addAll(T[],int,int)"""
        return bool.__wrap(super(__ObjectSet, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def addAll(self, *arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.addAll(T...)"""
        return bool.__wrap(super(__ObjectSet, self).addAll(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.LittleEndianInputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.io.FilterInputStream as __FilterInputStream
__FilterInputStream = __FilterInputStream
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.LittleEndianInputStream as __LittleEndianInputStream
__LittleEndianInputStream = __LittleEndianInputStream
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LittleEndianInputStream():
    """com.badlogic.gdx.utils.LittleEndianInputStream"""
 
    @staticmethod
    def __wrap(java_value: __LittleEndianInputStream) -> 'LittleEndianInputStream':
        return LittleEndianInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LittleEndianInputStream):
        """
        Dynamic initializer for LittleEndianInputStream.
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
    def readLine(self) -> str:
        """public final java.lang.String com.badlogic.gdx.utils.LittleEndianInputStream.readLine() throws java.io.IOException"""
        return str.__wrap(super(LittleEndianInputStream, self).readLine())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream.__wrap(__InputStream.nullInputStream())

    @override
    @overload
    def readFully(self, arg0: bytes):
        """public void com.badlogic.gdx.utils.LittleEndianInputStream.readFully(byte[]) throws java.io.IOException"""
        super(__LittleEndianInputStream, self).readFully(bytes)

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.FilterInputStream.read(byte[]) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).read(bytes))

    @override
    @overload
    def read(self) -> int:
        """public int java.io.FilterInputStream.read() throws java.io.IOException"""
        return int.__wrap(super(FilterInputStream, self).read())

    @override
    @overload
    def available(self) -> int:
        """public int java.io.FilterInputStream.available() throws java.io.IOException"""
        return int.__wrap(super(FilterInputStream, self).available())

    @overload
    def skipBytes(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.LittleEndianInputStream.skipBytes(int) throws java.io.IOException"""
        return int.__wrap(super(__LittleEndianInputStream, self).skipBytes(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean java.io.FilterInputStream.markSupported()"""
        return bool.__wrap(super(FilterInputStream, self).markSupported())

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int].__wrap(super(InputStream, self).readAllBytes())

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
    def readUnsignedByte(self) -> int:
        """public int com.badlogic.gdx.utils.LittleEndianInputStream.readUnsignedByte() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianInputStream, self).readUnsignedByte())

    @override
    @overload
    def readFloat(self) -> float:
        """public float com.badlogic.gdx.utils.LittleEndianInputStream.readFloat() throws java.io.IOException"""
        return float.__wrap(super(LittleEndianInputStream, self).readFloat())

    @override
    @overload
    def readUnsignedShort(self) -> int:
        """public int com.badlogic.gdx.utils.LittleEndianInputStream.readUnsignedShort() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianInputStream, self).readUnsignedShort())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def readDouble(self) -> float:
        """public double com.badlogic.gdx.utils.LittleEndianInputStream.readDouble() throws java.io.IOException"""
        return float.__wrap(super(LittleEndianInputStream, self).readDouble())

    @override
    @overload
    def reset(self):
        """public void java.io.FilterInputStream.reset() throws java.io.IOException"""
        super(FilterInputStream, self).reset()

    @overload
    def skip(self, arg0: int) -> int:
        """public long java.io.FilterInputStream.skip(long) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).skip(__long.valueOf(arg0)))

    @override
    @overload
    def readLong(self) -> int:
        """public long com.badlogic.gdx.utils.LittleEndianInputStream.readLong() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianInputStream, self).readLong())

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).transferTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int].__wrap(super(__InputStream, self).readNBytes(__int.valueOf(arg0)))

    @override
    @overload
    def readUTF(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.LittleEndianInputStream.readUTF() throws java.io.IOException"""
        return str.__wrap(super(LittleEndianInputStream, self).readUTF())

    @override
    @overload
    def readChar(self) -> str:
        """public char com.badlogic.gdx.utils.LittleEndianInputStream.readChar() throws java.io.IOException"""
        return str.__wrap(super(LittleEndianInputStream, self).readChar())

    @override
    @overload
    def readShort(self) -> int:
        """public short com.badlogic.gdx.utils.LittleEndianInputStream.readShort() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianInputStream, self).readShort())

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).readNBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def mark(self, arg0: int):
        """public void java.io.FilterInputStream.mark(int)"""
        super(__FilterInputStream, self).mark(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'InputStream'):
        """public com.badlogic.gdx.utils.LittleEndianInputStream(java.io.InputStream)"""
        val = __LittleEndianInputStream(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public void java.io.FilterInputStream.close() throws java.io.IOException"""
        super(FilterInputStream, self).close()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(__InputStream, self).skipNBytes(__long.valueOf(arg0))

    @override
    @overload
    def readInt(self) -> int:
        """public int com.badlogic.gdx.utils.LittleEndianInputStream.readInt() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianInputStream, self).readInt())

    @override
    @overload
    def readByte(self) -> int:
        """public byte com.badlogic.gdx.utils.LittleEndianInputStream.readByte() throws java.io.IOException"""
        return int.__wrap(super(LittleEndianInputStream, self).readByte())

    @override
    @overload
    def readFully(self, arg0: bytes, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.LittleEndianInputStream.readFully(byte[],int,int) throws java.io.IOException"""
        super(__LittleEndianInputStream, self).readFully(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def readBoolean(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LittleEndianInputStream.readBoolean() throws java.io.IOException"""
        return bool.__wrap(super(LittleEndianInputStream, self).readBoolean())

    @overload
    def read(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.FilterInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__FilterInputStream, self).read(bytes, __int.valueOf(arg1), __int.valueOf(arg2))) 
 
 
# CLASS: com.badlogic.gdx.utils.Pools
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.Pools as __Pools
__Pools = __Pools
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Pools():
    """com.badlogic.gdx.utils.Pools"""
 
    @staticmethod
    def __wrap(java_value: __Pools) -> 'Pools':
        return Pools(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pools):
        """
        Dynamic initializer for Pools.
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
    def set(arg0: 'Class', arg1: 'Pool'):
        """public static <T> void com.badlogic.gdx.utils.Pools.set(java.lang.Class<T>,com.badlogic.gdx.utils.Pool<T>)"""
        __Pools.set(arg0, arg1)

    @staticmethod
    @overload
    def freeAll(arg0: 'Array'):
        """public static void com.badlogic.gdx.utils.Pools.freeAll(com.badlogic.gdx.utils.Array)"""
        __Pools.freeAll(arg0)

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
    def get(arg0: 'Class') -> 'Pool':
        """public static <T> com.badlogic.gdx.utils.Pool<T> com.badlogic.gdx.utils.Pools.get(java.lang.Class<T>)"""
        return Pool.__wrap(__Pools.get(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Class', arg1: int) -> 'Pool':
        """public static <T> com.badlogic.gdx.utils.Pool<T> com.badlogic.gdx.utils.Pools.get(java.lang.Class<T>,int)"""
        return Pool.__wrap(__Pools.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def obtain(arg0: 'Class') -> object:
        """public static <T> T com.badlogic.gdx.utils.Pools.obtain(java.lang.Class<T>)"""
        return object.__wrap(__Pools.obtain(arg0))

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

    @staticmethod
    @overload
    def free(arg0: object):
        """public static void com.badlogic.gdx.utils.Pools.free(java.lang.Object)"""
        __Pools.free(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def freeAll(arg0: 'Array', arg1: bool):
        """public static void com.badlogic.gdx.utils.Pools.freeAll(com.badlogic.gdx.utils.Array,boolean)"""
        __Pools.freeAll(arg0, __boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.PerformanceCounter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.PerformanceCounter as __PerformanceCounter
__PerformanceCounter = __PerformanceCounter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PerformanceCounter():
    """com.badlogic.gdx.utils.PerformanceCounter"""
 
    @staticmethod
    def __wrap(java_value: __PerformanceCounter) -> 'PerformanceCounter':
        return PerformanceCounter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PerformanceCounter):
        """
        Dynamic initializer for PerformanceCounter.
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
    def reset(self):
        """public void com.badlogic.gdx.utils.PerformanceCounter.reset()"""
        super(PerformanceCounter, self).reset()

    @overload
    def toString(self, arg0: 'StringBuilder') -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.PerformanceCounter.toString(com.badlogic.gdx.utils.StringBuilder)"""
        return 'StringBuilder'.__wrap(super(__PerformanceCounter, self).toString(arg0))

    @overload
    def tick(self):
        """public void com.badlogic.gdx.utils.PerformanceCounter.tick()"""
        super(PerformanceCounter, self).tick()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.PerformanceCounter(java.lang.String)"""
        val = __PerformanceCounter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def start(self):
        """public void com.badlogic.gdx.utils.PerformanceCounter.start()"""
        super(PerformanceCounter, self).start()

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
        """public java.lang.String com.badlogic.gdx.utils.PerformanceCounter.toString()"""
        return str.__wrap(super(PerformanceCounter, self).toString())

    @overload
    def stop(self):
        """public void com.badlogic.gdx.utils.PerformanceCounter.stop()"""
        super(PerformanceCounter, self).stop()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def tick(self, arg0: float):
        """public void com.badlogic.gdx.utils.PerformanceCounter.tick(float)"""
        super(__PerformanceCounter, self).tick(__float.valueOf(arg0))

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
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.utils.PerformanceCounter(java.lang.String,int)"""
        val = __PerformanceCounter(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.ArrayMap$Keys
from builtins import str
import com.badlogic.gdx.utils.ArrayMap as __ArrayMap_Keys
__Keys = __ArrayMap_Keys.Keys
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Keys():
    """com.badlogic.gdx.utils.ArrayMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ArrayMap$Keys.toArray()"""
        return 'Array'.__wrap(super(Keys, self).toArray())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.ArrayMap$Keys.remove()"""
        super(Keys, self).remove()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reset(self):
        """public void com.badlogic.gdx.utils.ArrayMap$Keys.reset()"""
        super(Keys, self).reset()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ArrayMap'):
        """public com.badlogic.gdx.utils.ArrayMap$Keys(com.badlogic.gdx.utils.ArrayMap<K, java.lang.Object>)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ArrayMap$Keys.toArray(com.badlogic.gdx.utils.Array)"""
        return 'Array'.__wrap(super(__Keys, self).toArray(arg0))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap$Keys.hasNext()"""
        return bool.__wrap(super(Keys, self).hasNext())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> com.badlogic.gdx.utils.ArrayMap$Keys.iterator()"""
        return 'Iterator'.__wrap(super(Keys, self).iterator())

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> object:
        """public K com.badlogic.gdx.utils.ArrayMap$Keys.next()"""
        return object.__wrap(super(Keys, self).next())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Base64Coder
from builtins import str
import com.badlogic.gdx.utils.Base64Coder as __Base64Coder
__Base64Coder = __Base64Coder
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Base64Coder():
    """com.badlogic.gdx.utils.Base64Coder"""
 
    @staticmethod
    def __wrap(java_value: __Base64Coder) -> 'Base64Coder':
        return Base64Coder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Base64Coder):
        """
        Dynamic initializer for Base64Coder.
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
    def decode(arg0: 'char', arg1: int, arg2: int, arg3: bytes) -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decode(char[],int,int,byte[])"""
        return List[int].__wrap(__Base64Coder.decode(arg0, __int.valueOf(arg1), __int.valueOf(arg2), bytes))

    @staticmethod
    @overload
    def decode(arg0: 'char') -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decode(char[])"""
        return List[int].__wrap(__Base64Coder.decode(arg0))

    @staticmethod
    @overload
    def decodeLines(arg0: str, arg1: bytes) -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decodeLines(java.lang.String,byte[])"""
        return List[int].__wrap(__Base64Coder.decodeLines(arg0, bytes))

    @staticmethod
    @overload
    def decodeString(arg0: str) -> str:
        """public static java.lang.String com.badlogic.gdx.utils.Base64Coder.decodeString(java.lang.String)"""
        return str.__wrap(__Base64Coder.decodeString(arg0))

    @staticmethod
    @overload
    def decode(arg0: str) -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decode(java.lang.String)"""
        return List[int].__wrap(__Base64Coder.decode(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def decode(arg0: 'char', arg1: int, arg2: int, arg3: 'CharMap') -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decode(char[],int,int,com.badlogic.gdx.utils.Base64Coder$CharMap)"""
        return List[int].__wrap(__Base64Coder.decode(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def encodeLines(arg0: bytes, arg1: int, arg2: int, arg3: int, arg4: str, arg5: 'CharMap') -> str:
        """public static java.lang.String com.badlogic.gdx.utils.Base64Coder.encodeLines(byte[],int,int,int,java.lang.String,com.badlogic.gdx.utils.Base64Coder$CharMap)"""
        return str.__wrap(__Base64Coder.encodeLines(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5))

    @staticmethod
    @overload
    def decode(arg0: 'char', arg1: 'CharMap') -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decode(char[],com.badlogic.gdx.utils.Base64Coder$CharMap)"""
        return List[int].__wrap(__Base64Coder.decode(arg0, arg1))

    @staticmethod
    @overload
    def encodeString(arg0: str) -> str:
        """public static java.lang.String com.badlogic.gdx.utils.Base64Coder.encodeString(java.lang.String)"""
        return str.__wrap(__Base64Coder.encodeString(arg0))

    @staticmethod
    @overload
    def encode(arg0: bytes, arg1: 'char') -> List[str]:
        """public static char[] com.badlogic.gdx.utils.Base64Coder.encode(byte[],char[])"""
        return List[str].__wrap(__Base64Coder.encode(bytes, arg1))

    @staticmethod
    @overload
    def encode(arg0: bytes, arg1: 'CharMap') -> List[str]:
        """public static char[] com.badlogic.gdx.utils.Base64Coder.encode(byte[],com.badlogic.gdx.utils.Base64Coder$CharMap)"""
        return List[str].__wrap(__Base64Coder.encode(bytes, arg1))

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
    def encodeLines(arg0: bytes) -> str:
        """public static java.lang.String com.badlogic.gdx.utils.Base64Coder.encodeLines(byte[])"""
        return str.__wrap(__Base64Coder.encodeLines(bytes))

    @staticmethod
    @overload
    def encodeString(arg0: str, arg1: bool) -> str:
        """public static java.lang.String com.badlogic.gdx.utils.Base64Coder.encodeString(java.lang.String,boolean)"""
        return str.__wrap(__Base64Coder.encodeString(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def decodeLines(arg0: str, arg1: 'CharMap') -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decodeLines(java.lang.String,com.badlogic.gdx.utils.Base64Coder$CharMap)"""
        return List[int].__wrap(__Base64Coder.decodeLines(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def decode(arg0: str, arg1: 'CharMap') -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decode(java.lang.String,com.badlogic.gdx.utils.Base64Coder$CharMap)"""
        return List[int].__wrap(__Base64Coder.decode(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def decodeLines(arg0: str) -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decodeLines(java.lang.String)"""
        return List[int].__wrap(__Base64Coder.decodeLines(arg0))

    @staticmethod
    @overload
    def decodeString(arg0: str, arg1: bool) -> str:
        """public static java.lang.String com.badlogic.gdx.utils.Base64Coder.decodeString(java.lang.String,boolean)"""
        return str.__wrap(__Base64Coder.decodeString(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def encode(arg0: bytes, arg1: int, arg2: int, arg3: 'char') -> List[str]:
        """public static char[] com.badlogic.gdx.utils.Base64Coder.encode(byte[],int,int,char[])"""
        return List[str].__wrap(__Base64Coder.encode(bytes, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def encode(arg0: bytes, arg1: int, arg2: int, arg3: 'CharMap') -> List[str]:
        """public static char[] com.badlogic.gdx.utils.Base64Coder.encode(byte[],int,int,com.badlogic.gdx.utils.Base64Coder$CharMap)"""
        return List[str].__wrap(__Base64Coder.encode(bytes, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def encode(arg0: bytes) -> List[str]:
        """public static char[] com.badlogic.gdx.utils.Base64Coder.encode(byte[])"""
        return List[str].__wrap(__Base64Coder.encode(bytes))

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
    def decode(arg0: 'char', arg1: bytes) -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.Base64Coder.decode(char[],byte[])"""
        return List[int].__wrap(__Base64Coder.decode(arg0, bytes))

    @staticmethod
    @overload
    def encodeLines(arg0: bytes, arg1: int, arg2: int, arg3: int, arg4: str, arg5: 'char') -> str:
        """public static java.lang.String com.badlogic.gdx.utils.Base64Coder.encodeLines(byte[],int,int,int,java.lang.String,char[])"""
        return str.__wrap(__Base64Coder.encodeLines(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def encode(arg0: bytes, arg1: int) -> List[str]:
        """public static char[] com.badlogic.gdx.utils.Base64Coder.encode(byte[],int)"""
        return List[str].__wrap(__Base64Coder.encode(bytes, __int.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.utils.Logger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.Logger as __Logger
__Logger = __Logger
import java.lang.Exception as Exception
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Logger():
    """com.badlogic.gdx.utils.Logger"""
 
    @staticmethod
    def __wrap(java_value: __Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Logger):
        """
        Dynamic initializer for Logger.
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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.Logger(java.lang.String)"""
        val = __Logger(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def error(self, arg0: str):
        """public void com.badlogic.gdx.utils.Logger.error(java.lang.String)"""
        super(__Logger, self).error(arg0)

    @overload
    def getLevel(self) -> int:
        """public int com.badlogic.gdx.utils.Logger.getLevel()"""
        return int.__wrap(super(Logger, self).getLevel())

    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void com.badlogic.gdx.utils.Logger.error(java.lang.String,java.lang.Throwable)"""
        super(__Logger, self).error(arg0, arg1)

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
    def info(self, arg0: str):
        """public void com.badlogic.gdx.utils.Logger.info(java.lang.String)"""
        super(__Logger, self).info(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.utils.Logger(java.lang.String,int)"""
        val = __Logger(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def debug(self, arg0: str):
        """public void com.badlogic.gdx.utils.Logger.debug(java.lang.String)"""
        super(__Logger, self).debug(arg0)

    @overload
    def debug(self, arg0: str, arg1: 'Exception'):
        """public void com.badlogic.gdx.utils.Logger.debug(java.lang.String,java.lang.Exception)"""
        super(__Logger, self).debug(arg0, arg1)

    @overload
    def setLevel(self, arg0: int):
        """public void com.badlogic.gdx.utils.Logger.setLevel(int)"""
        super(__Logger, self).setLevel(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def info(self, arg0: str, arg1: 'Exception'):
        """public void com.badlogic.gdx.utils.Logger.info(java.lang.String,java.lang.Exception)"""
        super(__Logger, self).info(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.utils.IntMap
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import com.badlogic.gdx.utils.IntMap as __IntMap
__IntMap = __IntMap
import com.badlogic.gdx.utils.IntMap as __IntMap_Keys
__Keys = __IntMap_Keys.Keys
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.utils.IntMap as __IntMap_Values
__Values = __IntMap_Values.Values
from builtins import bool
import com.badlogic.gdx.utils.IntMap as __IntMap_Entries
__Entries = __IntMap_Entries.Entries
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class IntMap():
    """com.badlogic.gdx.utils.IntMap"""
 
    @staticmethod
    def __wrap(java_value: __IntMap) -> 'IntMap':
        return IntMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntMap):
        """
        Dynamic initializer for IntMap.
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
    def containsValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.IntMap.containsValue(java.lang.Object,boolean)"""
        return bool.__wrap(super(__IntMap, self).containsValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntMap.isEmpty()"""
        return bool.__wrap(super(IntMap, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: int) -> object:
        """public V com.badlogic.gdx.utils.IntMap.get(int)"""
        return object.__wrap(super(__IntMap, self).get(__int.valueOf(arg0)))

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.IntMap.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__IntMap, self).equalsIdentity(arg0))

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntMap.shrink(int)"""
        super(__IntMap, self).shrink(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IntMap()"""
        val = __IntMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def findKey(self, arg0: object, arg1: bool, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.IntMap.findKey(java.lang.Object,boolean,int)"""
        return int.__wrap(super(__IntMap, self).findKey(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.IntMap$Entries<V> com.badlogic.gdx.utils.IntMap.entries()"""
        return 'Entries'.__wrap(super(IntMap, self).entries())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.IntMap(int)"""
        val = __IntMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: int) -> object:
        """public V com.badlogic.gdx.utils.IntMap.remove(int)"""
        return object.__wrap(super(__IntMap, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.IntMap(int,float)"""
        val = __IntMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.IntMap$Values<V> com.badlogic.gdx.utils.IntMap.values()"""
        return 'Values'.__wrap(super(IntMap, self).values())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.IntMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntMap, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.IntMap.hashCode()"""
        return int.__wrap(super(IntMap, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.IntMap.toString()"""
        return str.__wrap(super(IntMap, self).toString())

    @overload
    def containsKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntMap.containsKey(int)"""
        return bool.__wrap(super(__IntMap, self).containsKey(__int.valueOf(arg0)))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.IntMap.clear()"""
        super(IntMap, self).clear()

    @overload
    def get(self, arg0: int, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.IntMap.get(int,V)"""
        return object.__wrap(super(__IntMap, self).get(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IntMap()"""
        val = __IntMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntMap.notEmpty()"""
        return bool.__wrap(super(IntMap, self).notEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def put(self, arg0: int, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.IntMap.put(int,V)"""
        return object.__wrap(super(__IntMap, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntMap.clear(int)"""
        super(__IntMap, self).clear(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'IntMap'):
        """public com.badlogic.gdx.utils.IntMap(com.badlogic.gdx.utils.IntMap<? extends V>)"""
        val = __IntMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putAll(self, arg0: 'IntMap'):
        """public void com.badlogic.gdx.utils.IntMap.putAll(com.badlogic.gdx.utils.IntMap<? extends V>)"""
        super(__IntMap, self).putAll(arg0)

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.IntMap$Keys com.badlogic.gdx.utils.IntMap.keys()"""
        return 'Keys'.__wrap(super(IntMap, self).keys())

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntMap.ensureCapacity(int)"""
        super(__IntMap, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.IntMap$Entry<V>> com.badlogic.gdx.utils.IntMap.iterator()"""
        return 'Iterator'.__wrap(super(IntMap, self).iterator()) 
 
 
# CLASS: com.badlogic.gdx.utils.Pool
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
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Pool(ABC):
    """com.badlogic.gdx.utils.Pool"""
 
    @staticmethod
    def __wrap(java_value: __Pool) -> 'Pool':
        return Pool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pool):
        """
        Dynamic initializer for Pool.
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
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(Pool, self).clear()

    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int.__wrap(super(Pool, self).getFree())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Pool()"""
        val = __Pool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.Pool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__Pool, self).freeAll(arg0)

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
    def __init__(self):
        """public com.badlogic.gdx.utils.Pool()"""
        val = __Pool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(__Pool, self).fill(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.utils.Pool(int,int)"""
        val = __Pool(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.Pool(int)"""
        val = __Pool(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def obtain(self) -> object:
        """public T com.badlogic.gdx.utils.Pool.obtain()"""
        return object.__wrap(super(Pool, self).obtain())

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
    def free(self, arg0: object):
        """public void com.badlogic.gdx.utils.Pool.free(T)"""
        super(__Pool, self).free(arg0) 
 
 
# CLASS: com.badlogic.gdx.utils.Disposable
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
 
class Disposable(ABC):
    """com.badlogic.gdx.utils.Disposable"""
 
    @staticmethod
    def __wrap(java_value: __Disposable) -> 'Disposable':
        return Disposable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Disposable):
        """
        Dynamic initializer for Disposable.
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
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.utils.IntIntMap$Entry
from builtins import str
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap_Entry
__Entry = __IntIntMap_Entry.Entry
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
 
class Entry():
    """com.badlogic.gdx.utils.IntIntMap.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.IntIntMap$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IntIntMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IntIntMap$Entry()"""
        val = __Entry()
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
 
 
# CLASS: com.badlogic.gdx.utils.AtomicQueue
from builtins import str
import com.badlogic.gdx.utils.AtomicQueue as __AtomicQueue
__AtomicQueue = __AtomicQueue
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
 
class AtomicQueue():
    """com.badlogic.gdx.utils.AtomicQueue"""
 
    @staticmethod
    def __wrap(java_value: __AtomicQueue) -> 'AtomicQueue':
        return AtomicQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtomicQueue):
        """
        Dynamic initializer for AtomicQueue.
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

    @overload
    def put(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.AtomicQueue.put(T)"""
        return bool.__wrap(super(__AtomicQueue, self).put(arg0))

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
    def poll(self) -> object:
        """public T com.badlogic.gdx.utils.AtomicQueue.poll()"""
        return object.__wrap(super(AtomicQueue, self).poll())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.AtomicQueue(int)"""
        val = __AtomicQueue(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.LongQueue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.LongQueue as __LongQueue
__LongQueue = __LongQueue
from builtins import int
 
class LongQueue():
    """com.badlogic.gdx.utils.LongQueue"""
 
    @staticmethod
    def __wrap(java_value: __LongQueue) -> 'LongQueue':
        return LongQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongQueue):
        """
        Dynamic initializer for LongQueue.
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
    def removeIndex(self, arg0: int) -> int:
        """public long com.badlogic.gdx.utils.LongQueue.removeIndex(int)"""
        return int.__wrap(super(__LongQueue, self).removeIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.LongQueue()"""
        val = __LongQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.LongQueue()"""
        val = __LongQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def last(self) -> int:
        """public long com.badlogic.gdx.utils.LongQueue.last()"""
        return int.__wrap(super(LongQueue, self).last())

    @overload
    def first(self) -> int:
        """public long com.badlogic.gdx.utils.LongQueue.first()"""
        return int.__wrap(super(LongQueue, self).first())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongQueue.ensureCapacity(int)"""
        super(__LongQueue, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongQueue.notEmpty()"""
        return bool.__wrap(super(LongQueue, self).notEmpty())

    @overload
    def addFirst(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongQueue.addFirst(long)"""
        super(__LongQueue, self).addFirst(__long.valueOf(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.LongQueue.toString(java.lang.String)"""
        return str.__wrap(super(__LongQueue, self).toString(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.LongQueue.clear()"""
        super(LongQueue, self).clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.LongQueue.toString()"""
        return str.__wrap(super(LongQueue, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.LongQueue.equals(java.lang.Object)"""
        return bool.__wrap(super(__LongQueue, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.LongQueue(int)"""
        val = __LongQueue(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeFirst(self) -> int:
        """public long com.badlogic.gdx.utils.LongQueue.removeFirst()"""
        return int.__wrap(super(LongQueue, self).removeFirst())

    @overload
    def removeLast(self) -> int:
        """public long com.badlogic.gdx.utils.LongQueue.removeLast()"""
        return int.__wrap(super(LongQueue, self).removeLast())

    @overload
    def indexOf(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.LongQueue.indexOf(long)"""
        return int.__wrap(super(__LongQueue, self).indexOf(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def addLast(self, arg0: int):
        """public void com.badlogic.gdx.utils.LongQueue.addLast(long)"""
        super(__LongQueue, self).addLast(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def removeValue(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.LongQueue.removeValue(long)"""
        return bool.__wrap(super(__LongQueue, self).removeValue(__long.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> int:
        """public long com.badlogic.gdx.utils.LongQueue.get(int)"""
        return int.__wrap(super(__LongQueue, self).get(__int.valueOf(arg0)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongQueue.isEmpty()"""
        return bool.__wrap(super(LongQueue, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.LongQueue.hashCode()"""
        return int.__wrap(super(LongQueue, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.SortedIntList$Iterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.SortedIntList as __SortedIntList_Iterator
__Iterator = __SortedIntList_Iterator.Iterator
import com.badlogic.gdx.utils.SortedIntList as __SortedIntList_Node
__Node = __SortedIntList_Node.Node
import java.util.function.Consumer as Consumer
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
 
class Iterator():
    """com.badlogic.gdx.utils.SortedIntList.Iterator"""
 
    @staticmethod
    def __wrap(java_value: __Iterator) -> 'Iterator':
        return Iterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Iterator):
        """
        Dynamic initializer for Iterator.
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
    def remove(self):
        """public void com.badlogic.gdx.utils.SortedIntList$Iterator.remove()"""
        super(Iterator, self).remove()

    @overload
    def __init__(self, arg0: 'SortedIntList'):
        """public com.badlogic.gdx.utils.SortedIntList$Iterator(com.badlogic.gdx.utils.SortedIntList)"""
        val = __Iterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.SortedIntList$Iterator.hasNext()"""
        return bool.__wrap(super(Iterator, self).hasNext())

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

    @override
    @overload
    def next(self) -> 'Node':
        """public com.badlogic.gdx.utils.SortedIntList$Node<E> com.badlogic.gdx.utils.SortedIntList$Iterator.next()"""
        return 'Node'.__wrap(super(Iterator, self).next())

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

    @overload
    def reset(self) -> 'Iterator':
        """public com.badlogic.gdx.utils.SortedIntList<E>$Iterator com.badlogic.gdx.utils.SortedIntList$Iterator.reset()"""
        return 'Iterator'.__wrap(super(Iterator, self).reset())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Pool$Poolable
import com.badlogic.gdx.utils.Pool as __Pool_Poolable
__Poolable = __Pool_Poolable.Poolable
from abc import abstractmethod, ABC
 
class Poolable(ABC):
    """com.badlogic.gdx.utils.Pool.Poolable"""
 
    @staticmethod
    def __wrap(java_value: __Poolable) -> 'Poolable':
        return Poolable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Poolable):
        """
        Dynamic initializer for Poolable.
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
    def reset(self, ):
        """public abstract void com.badlogic.gdx.utils.Pool$Poolable.reset()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.utils.Json$Serializable
import com.badlogic.gdx.utils.Json as __Json_Serializable
__Serializable = __Json_Serializable.Serializable
from abc import abstractmethod, ABC
 
class Serializable(ABC):
    """com.badlogic.gdx.utils.Json.Serializable"""
 
    @staticmethod
    def __wrap(java_value: __Serializable) -> 'Serializable':
        return Serializable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Serializable):
        """
        Dynamic initializer for Serializable.
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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public abstract void com.badlogic.gdx.utils.Json$Serializable.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        pass

    @abstractmethod
    def write(self, arg0: 'Json'):
        """public abstract void com.badlogic.gdx.utils.Json$Serializable.write(com.badlogic.gdx.utils.Json)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.utils.IdentityMap
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.IdentityMap as __IdentityMap
__IdentityMap = __IdentityMap
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap
__ObjectMap = __ObjectMap
from builtins import object
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entries
__Entries = __ObjectMap_Entries.Entries
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Values
__Values = __ObjectMap_Values.Values
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Keys
__Keys = __ObjectMap_Keys.Keys
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class IdentityMap():
    """com.badlogic.gdx.utils.IdentityMap"""
 
    @staticmethod
    def __wrap(java_value: __IdentityMap) -> 'IdentityMap':
        return IdentityMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IdentityMap):
        """
        Dynamic initializer for IdentityMap.
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
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectMap$Entries<K, V> com.badlogic.gdx.utils.ObjectMap.entries()"""
        return 'Entries'.__wrap(super(ObjectMap, self).entries())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__ObjectMap, self).equalsIdentity(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.IdentityMap(int,float)"""
        val = __IdentityMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def putAll(self, arg0: 'ObjectMap'):
        """public void com.badlogic.gdx.utils.ObjectMap.putAll(com.badlogic.gdx.utils.ObjectMap<? extends K, ? extends V>)"""
        super(__ObjectMap, self).putAll(arg0)

    @overload
    def __init__(self, arg0: 'IdentityMap'):
        """public com.badlogic.gdx.utils.IdentityMap(com.badlogic.gdx.utils.IdentityMap<K, V>)"""
        val = __IdentityMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectMap$Entries<K, V> com.badlogic.gdx.utils.ObjectMap.iterator()"""
        return 'Entries'.__wrap(super(ObjectMap, self).iterator())

    @overload
    def findKey(self, arg0: object, arg1: bool) -> object:
        """public K com.badlogic.gdx.utils.ObjectMap.findKey(java.lang.Object,boolean)"""
        return object.__wrap(super(__ObjectMap, self).findKey(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: object) -> object:
        """public <T extends K> V com.badlogic.gdx.utils.ObjectMap.get(T)"""
        return object.__wrap(super(__ObjectMap, self).get(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.ObjectMap.put(K,V)"""
        return object.__wrap(super(__ObjectMap, self).put(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectMap.toString()"""
        return str.__wrap(super(ObjectMap, self).toString())

    @override
    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectMap.shrink(int)"""
        super(__ObjectMap, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectMap$Values<V> com.badlogic.gdx.utils.ObjectMap.values()"""
        return 'Values'.__wrap(super(ObjectMap, self).values())

    @override
    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectMap.clear(int)"""
        super(__ObjectMap, self).clear(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.IdentityMap.hashCode()"""
        return int.__wrap(super(IdentityMap, self).hashCode())

    @override
    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.notEmpty()"""
        return bool.__wrap(super(ObjectMap, self).notEmpty())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectMap.toString(java.lang.String)"""
        return str.__wrap(super(__ObjectMap, self).toString(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IdentityMap()"""
        val = __IdentityMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ObjectMap.clear()"""
        super(ObjectMap, self).clear()

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.ObjectMap.get(K,V)"""
        return object.__wrap(super(__ObjectMap, self).get(arg0, arg1))

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
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.isEmpty()"""
        return bool.__wrap(super(ObjectMap, self).isEmpty())

    @overload
    def remove(self, arg0: object) -> object:
        """public V com.badlogic.gdx.utils.ObjectMap.remove(K)"""
        return object.__wrap(super(__ObjectMap, self).remove(arg0))

    @override
    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectMap$Keys<K> com.badlogic.gdx.utils.ObjectMap.keys()"""
        return 'Keys'.__wrap(super(ObjectMap, self).keys())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.IdentityMap(int)"""
        val = __IdentityMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IdentityMap()"""
        val = __IdentityMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.containsValue(java.lang.Object,boolean)"""
        return bool.__wrap(super(__ObjectMap, self).containsValue(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectMap, self).equals(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.containsKey(K)"""
        return bool.__wrap(super(__ObjectMap, self).containsKey(arg0))

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectMap.ensureCapacity(int)"""
        super(__ObjectMap, self).ensureCapacity(__int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.StringBuilder
from builtins import str
import java.lang.Character as __char
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Integer as __int
import java.lang.Double as __double
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
 
class StringBuilder():
    """com.badlogic.gdx.utils.StringBuilder"""
 
    @staticmethod
    def __wrap(java_value: __StringBuilder) -> 'StringBuilder':
        return StringBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringBuilder):
        """
        Dynamic initializer for StringBuilder.
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
    def setCharAt(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.utils.StringBuilder.setCharAt(int,char)"""
        super(__StringBuilder, self).setCharAt(__int.valueOf(arg0), __char.valueOf(arg1))

    @overload
    def substring(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.utils.StringBuilder.substring(int,int)"""
        return str.__wrap(super(__StringBuilder, self).substring(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def appendCodePoint(self, arg0: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.appendCodePoint(int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).appendCodePoint(__int.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,java.lang.String)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'CharSequence'):
        """public com.badlogic.gdx.utils.StringBuilder(java.lang.CharSequence)"""
        val = __StringBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: 'CharSequence', arg1: int, arg2: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(java.lang.CharSequence,int,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def append(self, arg0: float) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(float)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__float.valueOf(arg0)))

    @overload
    def append(self, arg0: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(long)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__long.valueOf(arg0)))

    @overload
    def append(self, arg0: int, arg1: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(int,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def append(self, arg0: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(char)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__char.valueOf(arg0)))

    @overload
    def append(self, arg0: int, arg1: int, arg2: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(int,int,char)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__int.valueOf(arg0), __int.valueOf(arg1), __char.valueOf(arg2)))

    @overload
    def append(self, arg0: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(java.lang.String)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: int, arg1: int, arg2: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(long,int,char)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__long.valueOf(arg0), __int.valueOf(arg1), __char.valueOf(arg2)))

    @overload
    def setLength(self, arg0: int):
        """public void com.badlogic.gdx.utils.StringBuilder.setLength(int)"""
        super(__StringBuilder, self).setLength(__int.valueOf(arg0))

    @overload
    def subSequence(self, arg0: int, arg1: int) -> 'CharSequence':
        """public java.lang.CharSequence com.badlogic.gdx.utils.StringBuilder.subSequence(int,int)"""
        return 'CharSequence'.__wrap(super(__StringBuilder, self).subSequence(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.StringBuilder()"""
        val = __StringBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def insert(self, arg0: int, arg1: 'CharSequence', arg2: int, arg3: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,java.lang.CharSequence,int,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def containsIgnoreCase(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.StringBuilder.containsIgnoreCase(java.lang.String)"""
        return bool.__wrap(super(__StringBuilder, self).containsIgnoreCase(arg0))

    @overload
    def append(self, arg0: 'StringBuilder') -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(com.badlogic.gdx.utils.StringBuilder)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.StringBuilder.clear()"""
        super(StringBuilder, self).clear()

    @overload
    def insert(self, arg0: int, arg1: float) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,double)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def replace(self, arg0: str, arg1: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.replace(char,java.lang.String)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).replace(__char.valueOf(arg0), arg1))

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.StringBuilder.ensureCapacity(int)"""
        super(__StringBuilder, self).ensureCapacity(__int.valueOf(arg0))

    @staticmethod
    @overload
    def numChars(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.utils.StringBuilder.numChars(int,int)"""
        return int.__wrap(__StringBuilder.numChars(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.hashCode()"""
        return int.__wrap(super(StringBuilder, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.StringBuilder.equals(java.lang.Object)"""
        return bool.__wrap(super(__StringBuilder, self).equals(arg0))

    @overload
    def toStringAndClear(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.StringBuilder.toStringAndClear()"""
        return str.__wrap(super(StringBuilder, self).toStringAndClear())

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.indexOf(java.lang.String,int)"""
        return int.__wrap(super(__StringBuilder, self).indexOf(arg0, __int.valueOf(arg1)))

    @overload
    def capacity(self) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.capacity()"""
        return int.__wrap(super(StringBuilder, self).capacity())

    @overload
    def append(self, arg0: 'CharSequence') -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(java.lang.CharSequence)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0))

    @overload
    def equalsIgnoreCase(self, arg0: 'StringBuilder') -> bool:
        """public boolean com.badlogic.gdx.utils.StringBuilder.equalsIgnoreCase(com.badlogic.gdx.utils.StringBuilder)"""
        return bool.__wrap(super(__StringBuilder, self).equalsIgnoreCase(arg0))

    @override
    @overload
    def codePoints(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.codePoints()"""
        return 'IntStream'.__wrap(super(CharSequence, self).codePoints())

    @override
    @overload
    def chars(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.chars()"""
        return 'IntStream'.__wrap(super(CharSequence, self).chars())

    @overload
    def append(self, arg0: 'char', arg1: int, arg2: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(char[],int,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def offsetByCodePoints(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.offsetByCodePoints(int,int)"""
        return int.__wrap(super(__StringBuilder, self).offsetByCodePoints(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(java.lang.String,java.lang.String)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0, arg1))

    @overload
    def insert(self, arg0: int, arg1: bool) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,boolean)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def delete(self, arg0: int, arg1: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.delete(int,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).delete(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def insert(self, arg0: int, arg1: 'char', arg2: int, arg3: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,char[],int,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.lastIndexOf(java.lang.String)"""
        return int.__wrap(super(__StringBuilder, self).lastIndexOf(arg0))

    @overload
    def substring(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.utils.StringBuilder.substring(int)"""
        return str.__wrap(super(__StringBuilder, self).substring(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def append(self, arg0: int, arg1: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(long,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def numChars(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.utils.StringBuilder.numChars(long,int)"""
        return int.__wrap(__StringBuilder.numChars(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'StringBuilder'):
        """public com.badlogic.gdx.utils.StringBuilder(com.badlogic.gdx.utils.StringBuilder)"""
        val = __StringBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def append(self, arg0: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__int.valueOf(arg0)))

    @overload
    def insert(self, arg0: int, arg1: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.StringBuilder(int)"""
        val = __StringBuilder(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def insert(self, arg0: int, arg1: 'CharSequence') -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,java.lang.CharSequence)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), arg1))

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.StringBuilder.notEmpty()"""
        return bool.__wrap(super(StringBuilder, self).notEmpty())

    @overload
    def append(self, arg0: 'char') -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(char[])"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0))

    @overload
    def codePointCount(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.codePointCount(int,int)"""
        return int.__wrap(super(__StringBuilder, self).codePointCount(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equalsIgnoreCase(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.StringBuilder.equalsIgnoreCase(java.lang.String)"""
        return bool.__wrap(super(__StringBuilder, self).equalsIgnoreCase(arg0))

    @overload
    def append(self, arg0: bool) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(boolean)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.StringBuilder(java.lang.String)"""
        val = __StringBuilder(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def codePointAt(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.codePointAt(int)"""
        return int.__wrap(super(__StringBuilder, self).codePointAt(__int.valueOf(arg0)))

    @overload
    def deleteCharAt(self, arg0: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.deleteCharAt(int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).deleteCharAt(__int.valueOf(arg0)))

    @overload
    def indexOfIgnoreCase(self, arg0: str, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.indexOfIgnoreCase(java.lang.String,int)"""
        return int.__wrap(super(__StringBuilder, self).indexOfIgnoreCase(arg0, __int.valueOf(arg1)))

    @overload
    def insert(self, arg0: int, arg1: object) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,java.lang.Object)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), arg1))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.indexOf(java.lang.String)"""
        return int.__wrap(super(__StringBuilder, self).indexOf(arg0))

    @overload
    def append(self, arg0: float) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(double)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(__double.valueOf(arg0)))

    @override
    @overload
    def length(self) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.length()"""
        return int.__wrap(super(StringBuilder, self).length())

    @overload
    def append(self, arg0: 'StringBuilder', arg1: int, arg2: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(com.badlogic.gdx.utils.StringBuilder,int,int)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def replace(self, arg0: str, arg1: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.replace(java.lang.String,java.lang.String)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).replace(arg0, arg1))

    @overload
    def replace(self, arg0: int, arg1: int, arg2: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.replace(int,int,java.lang.String)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).replace(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def trimToSize(self):
        """public void com.badlogic.gdx.utils.StringBuilder.trimToSize()"""
        super(StringBuilder, self).trimToSize()

    @overload
    def appendLine(self, arg0: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.appendLine(java.lang.String)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).appendLine(arg0))

    @overload
    def insert(self, arg0: int, arg1: 'char') -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,char[])"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), arg1))

    @overload
    def insert(self, arg0: int, arg1: float) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,float)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def codePointBefore(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.codePointBefore(int)"""
        return int.__wrap(super(__StringBuilder, self).codePointBefore(__int.valueOf(arg0)))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.StringBuilder.contains(java.lang.String)"""
        return bool.__wrap(super(__StringBuilder, self).contains(arg0))

    @overload
    def getChars(self, arg0: int, arg1: int, arg2: 'char', arg3: int):
        """public void com.badlogic.gdx.utils.StringBuilder.getChars(int,int,char[],int)"""
        super(__StringBuilder, self).getChars(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.StringBuilder.isEmpty()"""
        return bool.__wrap(super(StringBuilder, self).isEmpty())

    @overload
    def insert(self, arg0: int, arg1: int) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,long)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def append(self, arg0: object) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.append(java.lang.Object)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).append(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def reverse(self) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.reverse()"""
        return 'StringBuilder'.__wrap(super(StringBuilder, self).reverse())

    @overload
    def insert(self, arg0: int, arg1: str) -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.StringBuilder.insert(int,char)"""
        return 'StringBuilder'.__wrap(super(__StringBuilder, self).insert(__int.valueOf(arg0), __char.valueOf(arg1)))

    @overload
    def charAt(self, arg0: int) -> str:
        """public char com.badlogic.gdx.utils.StringBuilder.charAt(int)"""
        return str.__wrap(super(__StringBuilder, self).charAt(__int.valueOf(arg0)))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.StringBuilder.lastIndexOf(java.lang.String,int)"""
        return int.__wrap(super(__StringBuilder, self).lastIndexOf(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.StringBuilder.toString()"""
        return str.__wrap(super(StringBuilder, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.StringBuilder()"""
        val = __StringBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.LongMap$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.LongMap as __LongMap_Keys
__Keys = __LongMap_Keys.Keys
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.LongArray as __LongArray
__LongArray = __LongArray
from builtins import int
 
class Keys():
    """com.badlogic.gdx.utils.LongMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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
    def toArray(self) -> 'LongArray':
        """public com.badlogic.gdx.utils.LongArray com.badlogic.gdx.utils.LongMap$Keys.toArray()"""
        return 'LongArray'.__wrap(super(Keys, self).toArray())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArray(self, arg0: 'LongArray') -> 'LongArray':
        """public com.badlogic.gdx.utils.LongArray com.badlogic.gdx.utils.LongMap$Keys.toArray(com.badlogic.gdx.utils.LongArray)"""
        return 'LongArray'.__wrap(super(__Keys, self).toArray(arg0))

    @overload
    def next(self) -> int:
        """public long com.badlogic.gdx.utils.LongMap$Keys.next()"""
        return int.__wrap(super(Keys, self).next())

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

    @overload
    def __init__(self, arg0: 'LongMap'):
        """public com.badlogic.gdx.utils.LongMap$Keys(com.badlogic.gdx.utils.LongMap)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Queue$QueueIterable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.Queue as __Queue_QueueIterable
__QueueIterable = __Queue_QueueIterable.QueueIterable
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class QueueIterable():
    """com.badlogic.gdx.utils.Queue.QueueIterable"""
 
    @staticmethod
    def __wrap(java_value: __QueueIterable) -> 'QueueIterable':
        return QueueIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QueueIterable):
        """
        Dynamic initializer for QueueIterable.
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
    def __init__(self, arg0: 'Queue', arg1: bool):
        """public com.badlogic.gdx.utils.Queue$QueueIterable(com.badlogic.gdx.utils.Queue<T>,boolean)"""
        val = __QueueIterable(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'Queue'):
        """public com.badlogic.gdx.utils.Queue$QueueIterable(com.badlogic.gdx.utils.Queue<T>)"""
        val = __QueueIterable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.gdx.utils.Queue$QueueIterable.iterator()"""
        return 'Iterator'.__wrap(super(QueueIterable, self).iterator())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.OrderedMap$OrderedMapValues
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import com.badlogic.gdx.utils.OrderedMap as __OrderedMap_OrderedMapValues
__OrderedMapValues = __OrderedMap_OrderedMapValues.OrderedMapValues
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Values
__Values = __ObjectMap_Values.Values
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class OrderedMapValues():
    """com.badlogic.gdx.utils.OrderedMap.OrderedMapValues"""
 
    @staticmethod
    def __wrap(java_value: __OrderedMapValues) -> 'OrderedMapValues':
        return OrderedMapValues(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedMapValues):
        """
        Dynamic initializer for OrderedMapValues.
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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.utils.OrderedMap$OrderedMapValues.reset()"""
        super(OrderedMapValues, self).reset()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'OrderedMap'):
        """public com.badlogic.gdx.utils.OrderedMap$OrderedMapValues(com.badlogic.gdx.utils.OrderedMap<?, V>)"""
        val = __OrderedMapValues(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<V> com.badlogic.gdx.utils.OrderedMap$OrderedMapValues.toArray()"""
        return 'Array'.__wrap(super(OrderedMapValues, self).toArray())

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<V> com.badlogic.gdx.utils.OrderedMap$OrderedMapValues.toArray(com.badlogic.gdx.utils.Array<V>)"""
        return 'Array'.__wrap(super(__OrderedMapValues, self).toArray(arg0))

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
    def next(self) -> object:
        """public V com.badlogic.gdx.utils.OrderedMap$OrderedMapValues.next()"""
        return object.__wrap(super(OrderedMapValues, self).next())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectMap$Values<V> com.badlogic.gdx.utils.ObjectMap$Values.iterator()"""
        return 'Values'.__wrap(super(Values, self).iterator())

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.OrderedMap$OrderedMapValues.remove()"""
        super(OrderedMapValues, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectMap$Entries
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entries
__Entries = __ObjectMap_Entries.Entries
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entry
__Entry = __ObjectMap_Entry.Entry
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.ObjectMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectMap$Entries<K, V> com.badlogic.gdx.utils.ObjectMap$Entries.iterator()"""
        return 'Entries'.__wrap(super(Entries, self).iterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ObjectMap'):
        """public com.badlogic.gdx.utils.ObjectMap$Entries(com.badlogic.gdx.utils.ObjectMap<K, V>)"""
        val = __Entries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.ObjectMap$Entry<K, V> com.badlogic.gdx.utils.ObjectMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectLongMap$Values
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap_Values
__Values = __ObjectLongMap_Values.Values
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.LongArray as __LongArray
__LongArray = __LongArray
from builtins import int
 
class Values():
    """com.badlogic.gdx.utils.ObjectLongMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def toArray(self) -> 'LongArray':
        """public com.badlogic.gdx.utils.LongArray com.badlogic.gdx.utils.ObjectLongMap$Values.toArray()"""
        return 'LongArray'.__wrap(super(Values, self).toArray())

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def next(self) -> int:
        """public long com.badlogic.gdx.utils.ObjectLongMap$Values.next()"""
        return int.__wrap(super(Values, self).next())

    @overload
    def toArray(self, arg0: 'LongArray') -> 'LongArray':
        """public com.badlogic.gdx.utils.LongArray com.badlogic.gdx.utils.ObjectLongMap$Values.toArray(com.badlogic.gdx.utils.LongArray)"""
        return 'LongArray'.__wrap(super(__Values, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def iterator(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectLongMap$Values com.badlogic.gdx.utils.ObjectLongMap$Values.iterator()"""
        return 'Values'.__wrap(super(Values, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ObjectLongMap'):
        """public com.badlogic.gdx.utils.ObjectLongMap$Values(com.badlogic.gdx.utils.ObjectLongMap<?>)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectLongMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectMap
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap
__ObjectMap = __ObjectMap
from builtins import object
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entries
__Entries = __ObjectMap_Entries.Entries
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Values
__Values = __ObjectMap_Values.Values
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Keys
__Keys = __ObjectMap_Keys.Keys
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ObjectMap():
    """com.badlogic.gdx.utils.ObjectMap"""
 
    @staticmethod
    def __wrap(java_value: __ObjectMap) -> 'ObjectMap':
        return ObjectMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectMap):
        """
        Dynamic initializer for ObjectMap.
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
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__ObjectMap, self).equalsIdentity(arg0))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.isEmpty()"""
        return bool.__wrap(super(ObjectMap, self).isEmpty())

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectMap.shrink(int)"""
        super(__ObjectMap, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def putAll(self, arg0: 'ObjectMap'):
        """public void com.badlogic.gdx.utils.ObjectMap.putAll(com.badlogic.gdx.utils.ObjectMap<? extends K, ? extends V>)"""
        super(__ObjectMap, self).putAll(arg0)

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectMap$Entries<K, V> com.badlogic.gdx.utils.ObjectMap.entries()"""
        return 'Entries'.__wrap(super(ObjectMap, self).entries())

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectMap$Entries<K, V> com.badlogic.gdx.utils.ObjectMap.iterator()"""
        return 'Entries'.__wrap(super(ObjectMap, self).iterator())

    @overload
    def findKey(self, arg0: object, arg1: bool) -> object:
        """public K com.badlogic.gdx.utils.ObjectMap.findKey(java.lang.Object,boolean)"""
        return object.__wrap(super(__ObjectMap, self).findKey(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: object) -> object:
        """public <T extends K> V com.badlogic.gdx.utils.ObjectMap.get(T)"""
        return object.__wrap(super(__ObjectMap, self).get(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.ObjectMap(int)"""
        val = __ObjectMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.ObjectMap.put(K,V)"""
        return object.__wrap(super(__ObjectMap, self).put(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectMap.toString()"""
        return str.__wrap(super(ObjectMap, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.ObjectMap(int,float)"""
        val = __ObjectMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ObjectMap'):
        """public com.badlogic.gdx.utils.ObjectMap(com.badlogic.gdx.utils.ObjectMap<? extends K, ? extends V>)"""
        val = __ObjectMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ObjectMap.clear()"""
        super(ObjectMap, self).clear()

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectMap.toString(java.lang.String)"""
        return str.__wrap(super(__ObjectMap, self).toString(arg0))

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectMap$Values<V> com.badlogic.gdx.utils.ObjectMap.values()"""
        return 'Values'.__wrap(super(ObjectMap, self).values())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectMap()"""
        val = __ObjectMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectMap$Keys<K> com.badlogic.gdx.utils.ObjectMap.keys()"""
        return 'Keys'.__wrap(super(ObjectMap, self).keys())

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectMap.ensureCapacity(int)"""
        super(__ObjectMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectMap()"""
        val = __ObjectMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.ObjectMap.get(K,V)"""
        return object.__wrap(super(__ObjectMap, self).get(arg0, arg1))

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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ObjectMap.hashCode()"""
        return int.__wrap(super(ObjectMap, self).hashCode())

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectMap.clear(int)"""
        super(__ObjectMap, self).clear(__int.valueOf(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V com.badlogic.gdx.utils.ObjectMap.remove(K)"""
        return object.__wrap(super(__ObjectMap, self).remove(arg0))

    @overload
    def containsValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.containsValue(java.lang.Object,boolean)"""
        return bool.__wrap(super(__ObjectMap, self).containsValue(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectMap, self).equals(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.containsKey(K)"""
        return bool.__wrap(super(__ObjectMap, self).containsKey(arg0))

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.notEmpty()"""
        return bool.__wrap(super(ObjectMap, self).notEmpty()) 
 
 
# CLASS: com.badlogic.gdx.utils.UBJsonWriter
from builtins import str
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.UBJsonWriter as __UBJsonWriter
__UBJsonWriter = __UBJsonWriter
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class UBJsonWriter():
    """com.badlogic.gdx.utils.UBJsonWriter"""
 
    @staticmethod
    def __wrap(java_value: __UBJsonWriter) -> 'UBJsonWriter':
        return UBJsonWriter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UBJsonWriter):
        """
        Dynamic initializer for UBJsonWriter.
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
    def value(self, arg0: float) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(double) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(__double.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: str, arg1: 'char') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,char[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @overload
    def value(self, arg0: int) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(short) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(__short.valueOf(arg0)))

    @overload
    def value(self, arg0: int) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(byte) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(__byte.valueOf(arg0)))

    @overload
    def set(self, arg0: str, arg1: int) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,short) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, __short.valueOf(arg1)))

    @overload
    def set(self, arg0: str, arg1: int) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,long) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, __long.valueOf(arg1)))

    @overload
    def set(self, arg0: str, arg1: 'long') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,long[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def value(self, arg0: object) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(java.lang.Object) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def value(self, arg0: 'char') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(char[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def set(self, arg0: str, arg1: 'short') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,short[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def object(self) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.object() throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(UBJsonWriter, self).object())

    @overload
    def value(self, arg0: int) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(long) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: str, arg1: str) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,char) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, __char.valueOf(arg1)))

    @overload
    def set(self, arg0: str, arg1: str) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,java.lang.String) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: str, arg1: 'float') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,float[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @overload
    def name(self, arg0: str) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.name(java.lang.String) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).name(arg0))

    @overload
    def value(self, arg0: str) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(java.lang.String) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def set(self, arg0: str, arg1: bytes) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,byte[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, bytes))

    @overload
    def set(self, arg0: str, arg1: bool) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,boolean) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, __boolean.valueOf(arg1)))

    @overload
    def value(self, arg0: 'short') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(short[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def set(self, arg0: str, arg1: 'int') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,int[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @overload
    def value(self, arg0: 'JsonValue') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(com.badlogic.gdx.utils.JsonValue) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def value(self, arg0: 'double') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(double[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @override
    @overload
    def close(self):
        """public void com.badlogic.gdx.utils.UBJsonWriter.close() throws java.io.IOException"""
        super(UBJsonWriter, self).close()

    @overload
    def value(self, arg0: bool) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(boolean) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(__boolean.valueOf(arg0)))

    @overload
    def set(self, arg0: str, arg1: float) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,double) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, __double.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def array(self, arg0: str) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.array(java.lang.String) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).array(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def value(self, arg0: int) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(int) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(__int.valueOf(arg0)))

    @overload
    def value(self, arg0: str) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(char) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(__char.valueOf(arg0)))

    @overload
    def value(self, arg0: 'boolean') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(boolean[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def value(self, arg0: 'long') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(long[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def value(self, arg0: 'float') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(float[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def value(self, arg0: 'String') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(java.lang.String[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def set(self, arg0: str, arg1: float) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,float) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, __float.valueOf(arg1)))

    @overload
    def flush(self):
        """public void com.badlogic.gdx.utils.UBJsonWriter.flush() throws java.io.IOException"""
        super(UBJsonWriter, self).flush()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def value(self, arg0: float) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(float) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(__float.valueOf(arg0)))

    @overload
    def set(self, arg0: str, arg1: int) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,byte) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, __byte.valueOf(arg1)))

    @overload
    def set(self, arg0: str, arg1: 'boolean') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,boolean[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @overload
    def value(self, arg0: 'int') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(int[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(arg0))

    @overload
    def set(self, arg0: str) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0))

    @overload
    def set(self, arg0: str, arg1: 'double') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,double[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @overload
    def __init__(self, arg0: 'OutputStream'):
        """public com.badlogic.gdx.utils.UBJsonWriter(java.io.OutputStream)"""
        val = __UBJsonWriter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def array(self) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.array() throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(UBJsonWriter, self).array())

    @overload
    def pop(self) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.pop() throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(UBJsonWriter, self).pop())

    @overload
    def set(self, arg0: str, arg1: 'String') -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,java.lang.String[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, arg1))

    @overload
    def set(self, arg0: str, arg1: int) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.set(java.lang.String,int) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).set(arg0, __int.valueOf(arg1)))

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
    def value(self, arg0: bytes) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value(byte[]) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).value(bytes))

    @overload
    def object(self, arg0: str) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.object(java.lang.String) throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(__UBJsonWriter, self).object(arg0))

    @overload
    def value(self) -> 'UBJsonWriter':
        """public com.badlogic.gdx.utils.UBJsonWriter com.badlogic.gdx.utils.UBJsonWriter.value() throws java.io.IOException"""
        return 'UBJsonWriter'.__wrap(super(UBJsonWriter, self).value()) 
 
 
# CLASS: com.badlogic.gdx.utils.Select
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.utils.Select as __Select
__Select = __Select
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Comparator as Comparator
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
 
class Select():
    """com.badlogic.gdx.utils.Select"""
 
    @staticmethod
    def __wrap(java_value: __Select) -> 'Select':
        return Select(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Select):
        """
        Dynamic initializer for Select.
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
        """public com.badlogic.gdx.utils.Select()"""
        val = __Select()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def instance() -> 'Select':
        """public static com.badlogic.gdx.utils.Select com.badlogic.gdx.utils.Select.instance()"""
        return Select.__wrap(__Select.instance())

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
    def selectIndex(self, arg0: 'Object', arg1: 'Comparator', arg2: int, arg3: int) -> int:
        """public <T> int com.badlogic.gdx.utils.Select.selectIndex(T[],java.util.Comparator<T>,int,int)"""
        return int.__wrap(super(__Select, self).selectIndex(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Select()"""
        val = __Select()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def select(self, arg0: 'Object', arg1: 'Comparator', arg2: int, arg3: int) -> object:
        """public <T> T com.badlogic.gdx.utils.Select.select(T[],java.util.Comparator<T>,int,int)"""
        return object.__wrap(super(__Select, self).select(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Array$ArrayIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.Array as __Array_ArrayIterator
__ArrayIterator = __Array_ArrayIterator.ArrayIterator
from builtins import object
import java.util.function.Consumer as Consumer
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ArrayIterator():
    """com.badlogic.gdx.utils.Array.ArrayIterator"""
 
    @staticmethod
    def __wrap(java_value: __ArrayIterator) -> 'ArrayIterator':
        return ArrayIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayIterator):
        """
        Dynamic initializer for ArrayIterator.
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
    def reset(self):
        """public void com.badlogic.gdx.utils.Array$ArrayIterator.reset()"""
        super(ArrayIterator, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array$ArrayIterator.hasNext()"""
        return bool.__wrap(super(ArrayIterator, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.Array$ArrayIterator.remove()"""
        super(ArrayIterator, self).remove()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.utils.Array$ArrayIterator(com.badlogic.gdx.utils.Array<T>)"""
        val = __ArrayIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'ArrayIterator':
        """public com.badlogic.gdx.utils.Array$ArrayIterator<T> com.badlogic.gdx.utils.Array$ArrayIterator.iterator()"""
        return 'ArrayIterator'.__wrap(super(ArrayIterator, self).iterator())

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
    def __init__(self, arg0: 'Array', arg1: bool):
        """public com.badlogic.gdx.utils.Array$ArrayIterator(com.badlogic.gdx.utils.Array<T>,boolean)"""
        val = __ArrayIterator(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def next(self) -> object:
        """public T com.badlogic.gdx.utils.Array$ArrayIterator.next()"""
        return object.__wrap(super(ArrayIterator, self).next())

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

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.QuadTreeFloat
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.QuadTreeFloat as __QuadTreeFloat
__QuadTreeFloat = __QuadTreeFloat
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class QuadTreeFloat():
    """com.badlogic.gdx.utils.QuadTreeFloat"""
 
    @staticmethod
    def __wrap(java_value: __QuadTreeFloat) -> 'QuadTreeFloat':
        return QuadTreeFloat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QuadTreeFloat):
        """
        Dynamic initializer for QuadTreeFloat.
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
    def query(self, arg0: float, arg1: float, arg2: float, arg3: 'FloatArray'):
        """public void com.badlogic.gdx.utils.QuadTreeFloat.query(float,float,float,com.badlogic.gdx.utils.FloatArray)"""
        super(__QuadTreeFloat, self).query(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3)

    @overload
    def query(self, arg0: 'Rectangle', arg1: 'FloatArray'):
        """public void com.badlogic.gdx.utils.QuadTreeFloat.query(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.utils.FloatArray)"""
        super(__QuadTreeFloat, self).query(arg0, arg1)

    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.utils.QuadTreeFloat.setBounds(float,float,float,float)"""
        super(__QuadTreeFloat, self).setBounds(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def nearest(self, arg0: float, arg1: float, arg2: 'FloatArray') -> bool:
        """public boolean com.badlogic.gdx.utils.QuadTreeFloat.nearest(float,float,com.badlogic.gdx.utils.FloatArray)"""
        return bool.__wrap(super(__QuadTreeFloat, self).nearest(__float.valueOf(arg0), __float.valueOf(arg1), arg2))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.QuadTreeFloat()"""
        val = __QuadTreeFloat()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.utils.QuadTreeFloat.add(float,float,float)"""
        super(__QuadTreeFloat, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

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
    def reset(self):
        """public void com.badlogic.gdx.utils.QuadTreeFloat.reset()"""
        super(QuadTreeFloat, self).reset()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.QuadTreeFloat()"""
        val = __QuadTreeFloat()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.utils.QuadTreeFloat(int,int)"""
        val = __QuadTreeFloat(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.StreamUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.utils.StreamUtils as __StreamUtils
__StreamUtils = __StreamUtils
import java.io.Closeable as Closeable
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class StreamUtils():
    """com.badlogic.gdx.utils.StreamUtils"""
 
    @staticmethod
    def __wrap(java_value: __StreamUtils) -> 'StreamUtils':
        return StreamUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StreamUtils):
        """
        Dynamic initializer for StreamUtils.
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
    def copyStream(arg0: 'InputStream', arg1: 'ByteBuffer', arg2: int):
        """public static void com.badlogic.gdx.utils.StreamUtils.copyStream(java.io.InputStream,java.nio.ByteBuffer,int) throws java.io.IOException"""
        __StreamUtils.copyStream(arg0, arg1, __int.valueOf(arg2))

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
    def __init__(self):
        """public com.badlogic.gdx.utils.StreamUtils()"""
        val = __StreamUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def copyStream(arg0: 'InputStream', arg1: 'OutputStream'):
        """public static void com.badlogic.gdx.utils.StreamUtils.copyStream(java.io.InputStream,java.io.OutputStream) throws java.io.IOException"""
        __StreamUtils.copyStream(arg0, arg1)

    @staticmethod
    @overload
    def copyStreamToString(arg0: 'InputStream', arg1: int) -> str:
        """public static java.lang.String com.badlogic.gdx.utils.StreamUtils.copyStreamToString(java.io.InputStream,int) throws java.io.IOException"""
        return str.__wrap(__StreamUtils.copyStreamToString(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def copyStream(arg0: 'InputStream', arg1: 'OutputStream', arg2: bytes):
        """public static void com.badlogic.gdx.utils.StreamUtils.copyStream(java.io.InputStream,java.io.OutputStream,byte[]) throws java.io.IOException"""
        __StreamUtils.copyStream(arg0, arg1, bytes)

    @staticmethod
    @overload
    def copyStreamToByteArray(arg0: 'InputStream', arg1: int) -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.StreamUtils.copyStreamToByteArray(java.io.InputStream,int) throws java.io.IOException"""
        return List[int].__wrap(__StreamUtils.copyStreamToByteArray(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def copyStream(arg0: 'InputStream', arg1: 'ByteBuffer'):
        """public static void com.badlogic.gdx.utils.StreamUtils.copyStream(java.io.InputStream,java.nio.ByteBuffer) throws java.io.IOException"""
        __StreamUtils.copyStream(arg0, arg1)

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
    def copyStreamToByteArray(arg0: 'InputStream') -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.StreamUtils.copyStreamToByteArray(java.io.InputStream) throws java.io.IOException"""
        return List[int].__wrap(__StreamUtils.copyStreamToByteArray(arg0))

    @staticmethod
    @overload
    def copyStream(arg0: 'InputStream', arg1: 'ByteBuffer', arg2: bytes) -> int:
        """public static int com.badlogic.gdx.utils.StreamUtils.copyStream(java.io.InputStream,java.nio.ByteBuffer,byte[]) throws java.io.IOException"""
        return int.__wrap(__StreamUtils.copyStream(arg0, arg1, bytes))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def closeQuietly(arg0: 'Closeable'):
        """public static void com.badlogic.gdx.utils.StreamUtils.closeQuietly(java.io.Closeable)"""
        __StreamUtils.closeQuietly(arg0)

    @staticmethod
    @overload
    def copyStreamToString(arg0: 'InputStream', arg1: int, arg2: str) -> str:
        """public static java.lang.String com.badlogic.gdx.utils.StreamUtils.copyStreamToString(java.io.InputStream,int,java.lang.String) throws java.io.IOException"""
        return str.__wrap(__StreamUtils.copyStreamToString(arg0, __int.valueOf(arg1), arg2))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.StreamUtils()"""
        val = __StreamUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def copyStreamToString(arg0: 'InputStream') -> str:
        """public static java.lang.String com.badlogic.gdx.utils.StreamUtils.copyStreamToString(java.io.InputStream) throws java.io.IOException"""
        return str.__wrap(__StreamUtils.copyStreamToString(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def copyStream(arg0: 'InputStream', arg1: 'OutputStream', arg2: int):
        """public static void com.badlogic.gdx.utils.StreamUtils.copyStream(java.io.InputStream,java.io.OutputStream,int) throws java.io.IOException"""
        __StreamUtils.copyStream(arg0, arg1, __int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Json
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.utils.Json as __Json
__Json = __Json
from builtins import type
from builtins import object
try:
    from pygdx.utils import reflect
except ImportError:
    reflect = __import_once__("pygdx.utils.reflect")

import com.badlogic.gdx.utils.JsonWriter as __JsonWriter
__JsonWriter = __JsonWriter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.io.InputStream as InputStream
import com.badlogic.gdx.utils.Json as __Json_Serializer
__Serializer = __Json_Serializer.Serializer
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class Json():
    """com.badlogic.gdx.utils.Json"""
 
    @staticmethod
    def __wrap(java_value: __Json) -> 'Json':
        return Json(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Json):
        """
        Dynamic initializer for Json.
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
    def writeArrayStart(self):
        """public void com.badlogic.gdx.utils.Json.writeArrayStart()"""
        super(Json, self).writeArrayStart()

    @overload
    def writeValue(self, arg0: object, arg1: 'Class', arg2: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeValue(java.lang.Object,java.lang.Class,java.lang.Class)"""
        super(__Json, self).writeValue(arg0, arg1, arg2)

    @overload
    def copyFields(self, arg0: object, arg1: object):
        """public void com.badlogic.gdx.utils.Json.copyFields(java.lang.Object,java.lang.Object)"""
        super(__Json, self).copyFields(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toJson(self, arg0: object, arg1: 'FileHandle'):
        """public void com.badlogic.gdx.utils.Json.toJson(java.lang.Object,com.badlogic.gdx.files.FileHandle)"""
        super(__Json, self).toJson(arg0, arg1)

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'Class', arg2: 'InputStream') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,java.lang.Class,java.io.InputStream)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1, arg2))

    @overload
    def readField(self, arg0: object, arg1: str, arg2: str, arg3: 'Class', arg4: 'JsonValue'):
        """public void com.badlogic.gdx.utils.Json.readField(java.lang.Object,java.lang.String,java.lang.String,java.lang.Class,com.badlogic.gdx.utils.JsonValue)"""
        super(__Json, self).readField(arg0, arg1, arg2, arg3, arg4)

    @overload
    def writeValue(self, arg0: object, arg1: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeValue(java.lang.Object,java.lang.Class)"""
        super(__Json, self).writeValue(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def writeField(self, arg0: object, arg1: str, arg2: str):
        """public void com.badlogic.gdx.utils.Json.writeField(java.lang.Object,java.lang.String,java.lang.String)"""
        super(__Json, self).writeField(arg0, arg1, arg2)

    @overload
    def writeArrayStart(self, arg0: str):
        """public void com.badlogic.gdx.utils.Json.writeArrayStart(java.lang.String)"""
        super(__Json, self).writeArrayStart(arg0)

    @overload
    def getSerializer(self, arg0: 'Class') -> 'Serializer':
        """public <T> com.badlogic.gdx.utils.Json$Serializer<T> com.badlogic.gdx.utils.Json.getSerializer(java.lang.Class<T>)"""
        return 'Serializer'.__wrap(super(__Json, self).getSerializer(arg0))

    @overload
    def readValue(self, arg0: str, arg1: 'Class', arg2: 'JsonValue') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.readValue(java.lang.String,java.lang.Class<T>,com.badlogic.gdx.utils.JsonValue)"""
        return object.__wrap(super(__Json, self).readValue(arg0, arg1, arg2))

    @overload
    def writeObjectStart(self):
        """public void com.badlogic.gdx.utils.Json.writeObjectStart()"""
        super(Json, self).writeObjectStart()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def readValue(self, arg0: str, arg1: 'Class', arg2: 'Class', arg3: object, arg4: 'JsonValue') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.readValue(java.lang.String,java.lang.Class<T>,java.lang.Class,T,com.badlogic.gdx.utils.JsonValue)"""
        return object.__wrap(super(__Json, self).readValue(arg0, arg1, arg2, arg3, arg4))

    @overload
    def setSerializer(self, arg0: 'Class', arg1: 'Serializer'):
        """public <T> void com.badlogic.gdx.utils.Json.setSerializer(java.lang.Class<T>,com.badlogic.gdx.utils.Json$Serializer<T>)"""
        super(__Json, self).setSerializer(arg0, arg1)

    @overload
    def setWriter(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.utils.Json.setWriter(java.io.Writer)"""
        super(__Json, self).setWriter(arg0)

    @overload
    def getTag(self, arg0: 'Class') -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.getTag(java.lang.Class)"""
        return str.__wrap(super(__Json, self).getTag(arg0))

    @overload
    def readValue(self, arg0: 'Class', arg1: 'Class', arg2: object, arg3: 'JsonValue') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.readValue(java.lang.Class<T>,java.lang.Class,T,com.badlogic.gdx.utils.JsonValue)"""
        return object.__wrap(super(__Json, self).readValue(arg0, arg1, arg2, arg3))

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'Reader') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,java.io.Reader)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1))

    @overload
    def setOutputType(self, arg0: 'OutputType'):
        """public void com.badlogic.gdx.utils.Json.setOutputType(com.badlogic.gdx.utils.JsonWriter$OutputType)"""
        super(__Json, self).setOutputType(arg0)

    @overload
    def setSortFields(self, arg0: bool):
        """public void com.badlogic.gdx.utils.Json.setSortFields(boolean)"""
        super(__Json, self).setSortFields(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def writeFields(self, arg0: object):
        """public void com.badlogic.gdx.utils.Json.writeFields(java.lang.Object)"""
        super(__Json, self).writeFields(arg0)

    @overload
    def prettyPrint(self, arg0: str, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.prettyPrint(java.lang.String,int)"""
        return str.__wrap(super(__Json, self).prettyPrint(arg0, __int.valueOf(arg1)))

    @overload
    def setUsePrototypes(self, arg0: bool):
        """public void com.badlogic.gdx.utils.Json.setUsePrototypes(boolean)"""
        super(__Json, self).setUsePrototypes(__boolean.valueOf(arg0))

    @overload
    def writeField(self, arg0: object, arg1: str):
        """public void com.badlogic.gdx.utils.Json.writeField(java.lang.Object,java.lang.String)"""
        super(__Json, self).writeField(arg0, arg1)

    @overload
    def readValue(self, arg0: str, arg1: 'Class', arg2: 'Class', arg3: 'JsonValue') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.readValue(java.lang.String,java.lang.Class<T>,java.lang.Class,com.badlogic.gdx.utils.JsonValue)"""
        return object.__wrap(super(__Json, self).readValue(arg0, arg1, arg2, arg3))

    @overload
    def toJson(self, arg0: object, arg1: 'Class', arg2: 'Class', arg3: 'Writer'):
        """public void com.badlogic.gdx.utils.Json.toJson(java.lang.Object,java.lang.Class,java.lang.Class,java.io.Writer)"""
        super(__Json, self).toJson(arg0, arg1, arg2, arg3)

    @overload
    def writeArrayEnd(self):
        """public void com.badlogic.gdx.utils.Json.writeArrayEnd()"""
        super(Json, self).writeArrayEnd()

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'Class', arg2: 'FileHandle') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,java.lang.Class,com.badlogic.gdx.files.FileHandle)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1, arg2))

    @overload
    def prettyPrint(self, arg0: object, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.prettyPrint(java.lang.Object,int)"""
        return str.__wrap(super(__Json, self).prettyPrint(arg0, __int.valueOf(arg1)))

    @overload
    def readValue(self, arg0: 'Class', arg1: 'Class', arg2: 'JsonValue') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.readValue(java.lang.Class<T>,java.lang.Class,com.badlogic.gdx.utils.JsonValue)"""
        return object.__wrap(super(__Json, self).readValue(arg0, arg1, arg2))

    @overload
    def toJson(self, arg0: object, arg1: 'Class', arg2: 'Class') -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.toJson(java.lang.Object,java.lang.Class,java.lang.Class)"""
        return str.__wrap(super(__Json, self).toJson(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIgnoreUnknownFields(self, arg0: bool):
        """public void com.badlogic.gdx.utils.Json.setIgnoreUnknownFields(boolean)"""
        super(__Json, self).setIgnoreUnknownFields(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'OutputType'):
        """public com.badlogic.gdx.utils.Json(com.badlogic.gdx.utils.JsonWriter$OutputType)"""
        val = __Json(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def writeObjectStart(self, arg0: 'Class', arg1: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeObjectStart(java.lang.Class,java.lang.Class)"""
        super(__Json, self).writeObjectStart(arg0, arg1)

    @overload
    def writeObjectEnd(self):
        """public void com.badlogic.gdx.utils.Json.writeObjectEnd()"""
        super(Json, self).writeObjectEnd()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'char', arg2: int, arg3: int) -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,char[],int,int)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def readValue(self, arg0: 'Class', arg1: 'JsonValue') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.readValue(java.lang.Class<T>,com.badlogic.gdx.utils.JsonValue)"""
        return object.__wrap(super(__Json, self).readValue(arg0, arg1))

    @overload
    def getClass(self, arg0: str) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.Json.getClass(java.lang.String)"""
        return 'type.Class'.__wrap(super(__Json, self).getClass(arg0))

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'FileHandle') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,com.badlogic.gdx.files.FileHandle)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: object, arg1: 'Class') -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.toJson(java.lang.Object,java.lang.Class)"""
        return str.__wrap(super(__Json, self).toJson(arg0, arg1))

    @overload
    def toJson(self, arg0: object, arg1: 'Class', arg2: 'Class', arg3: 'FileHandle'):
        """public void com.badlogic.gdx.utils.Json.toJson(java.lang.Object,java.lang.Class,java.lang.Class,com.badlogic.gdx.files.FileHandle)"""
        super(__Json, self).toJson(arg0, arg1, arg2, arg3)

    @overload
    def setQuoteLongValues(self, arg0: bool):
        """public void com.badlogic.gdx.utils.Json.setQuoteLongValues(boolean)"""
        super(__Json, self).setQuoteLongValues(__boolean.valueOf(arg0))

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'InputStream') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,java.io.InputStream)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1))

    @overload
    def toJson(self, arg0: object, arg1: 'Class', arg2: 'Writer'):
        """public void com.badlogic.gdx.utils.Json.toJson(java.lang.Object,java.lang.Class,java.io.Writer)"""
        super(__Json, self).toJson(arg0, arg1, arg2)

    @overload
    def getIgnoreUnknownFields(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Json.getIgnoreUnknownFields()"""
        return bool.__wrap(super(Json, self).getIgnoreUnknownFields())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Json()"""
        val = __Json()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def readValue(self, arg0: str, arg1: 'Class', arg2: object, arg3: 'JsonValue') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.readValue(java.lang.String,java.lang.Class<T>,T,com.badlogic.gdx.utils.JsonValue)"""
        return object.__wrap(super(__Json, self).readValue(arg0, arg1, arg2, arg3))

    @overload
    def prettyPrint(self, arg0: object, arg1: 'PrettyPrintSettings') -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.prettyPrint(java.lang.Object,com.badlogic.gdx.utils.JsonValue$PrettyPrintSettings)"""
        return str.__wrap(super(__Json, self).prettyPrint(arg0, arg1))

    @overload
    def fromJson(self, arg0: 'Class', arg1: str) -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,java.lang.String)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1))

    @overload
    def writeField(self, arg0: object, arg1: str, arg2: str, arg3: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeField(java.lang.Object,java.lang.String,java.lang.String,java.lang.Class)"""
        super(__Json, self).writeField(arg0, arg1, arg2, arg3)

    @overload
    def setTypeName(self, arg0: str):
        """public void com.badlogic.gdx.utils.Json.setTypeName(java.lang.String)"""
        super(__Json, self).setTypeName(arg0)

    @overload
    def writeType(self, arg0: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeType(java.lang.Class)"""
        super(__Json, self).writeType(arg0)

    @overload
    def setEnumNames(self, arg0: bool):
        """public void com.badlogic.gdx.utils.Json.setEnumNames(boolean)"""
        super(__Json, self).setEnumNames(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def readField(self, arg0: object, arg1: str, arg2: str, arg3: 'JsonValue'):
        """public void com.badlogic.gdx.utils.Json.readField(java.lang.Object,java.lang.String,java.lang.String,com.badlogic.gdx.utils.JsonValue)"""
        super(__Json, self).readField(arg0, arg1, arg2, arg3)

    @overload
    def writeObjectStart(self, arg0: str):
        """public void com.badlogic.gdx.utils.Json.writeObjectStart(java.lang.String)"""
        super(__Json, self).writeObjectStart(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Json()"""
        val = __Json()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addClassTag(self, arg0: str, arg1: 'Class'):
        """public void com.badlogic.gdx.utils.Json.addClassTag(java.lang.String,java.lang.Class)"""
        super(__Json, self).addClassTag(arg0, arg1)

    @overload
    def toJson(self, arg0: object) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.toJson(java.lang.Object)"""
        return str.__wrap(super(__Json, self).toJson(arg0))

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'Class', arg2: str) -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,java.lang.Class,java.lang.String)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1, arg2))

    @overload
    def writeField(self, arg0: object, arg1: str, arg2: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeField(java.lang.Object,java.lang.String,java.lang.Class)"""
        super(__Json, self).writeField(arg0, arg1, arg2)

    @overload
    def writeValue(self, arg0: str, arg1: object):
        """public void com.badlogic.gdx.utils.Json.writeValue(java.lang.String,java.lang.Object)"""
        super(__Json, self).writeValue(arg0, arg1)

    @overload
    def prettyPrint(self, arg0: str, arg1: 'PrettyPrintSettings') -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.prettyPrint(java.lang.String,com.badlogic.gdx.utils.JsonValue$PrettyPrintSettings)"""
        return str.__wrap(super(__Json, self).prettyPrint(arg0, arg1))

    @overload
    def setDeprecated(self, arg0: 'Class', arg1: str, arg2: bool):
        """public void com.badlogic.gdx.utils.Json.setDeprecated(java.lang.Class,java.lang.String,boolean)"""
        super(__Json, self).setDeprecated(arg0, arg1, __boolean.valueOf(arg2))

    @overload
    def setDefaultSerializer(self, arg0: 'Serializer'):
        """public void com.badlogic.gdx.utils.Json.setDefaultSerializer(com.badlogic.gdx.utils.Json$Serializer)"""
        super(__Json, self).setDefaultSerializer(arg0)

    @overload
    def prettyPrint(self, arg0: object) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.prettyPrint(java.lang.Object)"""
        return str.__wrap(super(__Json, self).prettyPrint(arg0))

    @overload
    def toJson(self, arg0: object, arg1: 'Class', arg2: 'FileHandle'):
        """public void com.badlogic.gdx.utils.Json.toJson(java.lang.Object,java.lang.Class,com.badlogic.gdx.files.FileHandle)"""
        super(__Json, self).toJson(arg0, arg1, arg2)

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'Class', arg2: 'Reader') -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,java.lang.Class,java.io.Reader)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def writeValue(self, arg0: str, arg1: object, arg2: 'Class', arg3: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeValue(java.lang.String,java.lang.Object,java.lang.Class,java.lang.Class)"""
        super(__Json, self).writeValue(arg0, arg1, arg2, arg3)

    @overload
    def readField(self, arg0: object, arg1: str, arg2: 'Class', arg3: 'JsonValue'):
        """public void com.badlogic.gdx.utils.Json.readField(java.lang.Object,java.lang.String,java.lang.Class,com.badlogic.gdx.utils.JsonValue)"""
        super(__Json, self).readField(arg0, arg1, arg2, arg3)

    @overload
    def setIgnoreDeprecated(self, arg0: bool):
        """public void com.badlogic.gdx.utils.Json.setIgnoreDeprecated(boolean)"""
        super(__Json, self).setIgnoreDeprecated(__boolean.valueOf(arg0))

    @overload
    def readField(self, arg0: object, arg1: str, arg2: 'JsonValue'):
        """public void com.badlogic.gdx.utils.Json.readField(java.lang.Object,java.lang.String,com.badlogic.gdx.utils.JsonValue)"""
        super(__Json, self).readField(arg0, arg1, arg2)

    @overload
    def readField(self, arg0: object, arg1: 'Field', arg2: str, arg3: 'Class', arg4: 'JsonValue'):
        """public void com.badlogic.gdx.utils.Json.readField(java.lang.Object,com.badlogic.gdx.utils.reflect.Field,java.lang.String,java.lang.Class,com.badlogic.gdx.utils.JsonValue)"""
        super(__Json, self).readField(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def writeObjectStart(self, arg0: str, arg1: 'Class', arg2: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeObjectStart(java.lang.String,java.lang.Class,java.lang.Class)"""
        super(__Json, self).writeObjectStart(arg0, arg1, arg2)

    @overload
    def writeValue(self, arg0: str, arg1: object, arg2: 'Class'):
        """public void com.badlogic.gdx.utils.Json.writeValue(java.lang.String,java.lang.Object,java.lang.Class)"""
        super(__Json, self).writeValue(arg0, arg1, arg2)

    @overload
    def getWriter(self) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.Json.getWriter()"""
        return 'JsonWriter'.__wrap(super(Json, self).getWriter())

    @overload
    def readFields(self, arg0: object, arg1: 'JsonValue'):
        """public void com.badlogic.gdx.utils.Json.readFields(java.lang.Object,com.badlogic.gdx.utils.JsonValue)"""
        super(__Json, self).readFields(arg0, arg1)

    @overload
    def setReadDeprecated(self, arg0: bool):
        """public void com.badlogic.gdx.utils.Json.setReadDeprecated(boolean)"""
        super(__Json, self).setReadDeprecated(__boolean.valueOf(arg0))

    @overload
    def writeValue(self, arg0: object):
        """public void com.badlogic.gdx.utils.Json.writeValue(java.lang.Object)"""
        super(__Json, self).writeValue(arg0)

    @overload
    def setElementType(self, arg0: 'Class', arg1: str, arg2: 'Class'):
        """public void com.badlogic.gdx.utils.Json.setElementType(java.lang.Class,java.lang.String,java.lang.Class)"""
        super(__Json, self).setElementType(arg0, arg1, arg2)

    @overload
    def prettyPrint(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Json.prettyPrint(java.lang.String)"""
        return str.__wrap(super(__Json, self).prettyPrint(arg0))

    @overload
    def fromJson(self, arg0: 'Class', arg1: 'Class', arg2: 'char', arg3: int, arg4: int) -> object:
        """public <T> T com.badlogic.gdx.utils.Json.fromJson(java.lang.Class<T>,java.lang.Class,char[],int,int)"""
        return object.__wrap(super(__Json, self).fromJson(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def toJson(self, arg0: object, arg1: 'Writer'):
        """public void com.badlogic.gdx.utils.Json.toJson(java.lang.Object,java.io.Writer)"""
        super(__Json, self).toJson(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.utils.JsonValue$ValueType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.utils.JsonValue as __JsonValue_ValueType
__ValueType = __JsonValue_ValueType.ValueType
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
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class ValueType():
    """com.badlogic.gdx.utils.JsonValue.ValueType"""
 
    @staticmethod
    def __wrap(java_value: __ValueType) -> 'ValueType':
        return ValueType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueType):
        """
        Dynamic initializer for ValueType.
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

    @staticmethod
    @overload
    def values() -> List['ValueType']:
        """public static com.badlogic.gdx.utils.JsonValue$ValueType[] com.badlogic.gdx.utils.JsonValue$ValueType.values()"""
        return List[ValueType].__wrap(__ValueType.values())

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
    def valueOf(arg0: str) -> 'ValueType':
        """public static com.badlogic.gdx.utils.JsonValue$ValueType com.badlogic.gdx.utils.JsonValue$ValueType.valueOf(java.lang.String)"""
        return ValueType.__wrap(__ValueType.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntFloatMap$Values
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.utils.FloatArray as __FloatArray
__FloatArray = __FloatArray
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap_Values
__Values = __IntFloatMap_Values.Values
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
 
class Values():
    """com.badlogic.gdx.utils.IntFloatMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntFloatMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def next(self) -> float:
        """public float com.badlogic.gdx.utils.IntFloatMap$Values.next()"""
        return float.__wrap(super(Values, self).next())

    @overload
    def toArray(self, arg0: 'FloatArray') -> 'FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.utils.IntFloatMap$Values.toArray(com.badlogic.gdx.utils.FloatArray)"""
        return 'FloatArray'.__wrap(super(__Values, self).toArray(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArray(self) -> 'FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.utils.IntFloatMap$Values.toArray()"""
        return 'FloatArray'.__wrap(super(Values, self).toArray())

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
    def iterator(self) -> 'Values':
        """public com.badlogic.gdx.utils.IntFloatMap$Values com.badlogic.gdx.utils.IntFloatMap$Values.iterator()"""
        return 'Values'.__wrap(super(Values, self).iterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'IntFloatMap'):
        """public com.badlogic.gdx.utils.IntFloatMap$Values(com.badlogic.gdx.utils.IntFloatMap)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.JsonValue$PrettyPrintSettings
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import com.badlogic.gdx.utils.JsonValue as __JsonValue_PrettyPrintSettings
__PrettyPrintSettings = __JsonValue_PrettyPrintSettings.PrettyPrintSettings
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PrettyPrintSettings():
    """com.badlogic.gdx.utils.JsonValue.PrettyPrintSettings"""
 
    @staticmethod
    def __wrap(java_value: __PrettyPrintSettings) -> 'PrettyPrintSettings':
        return PrettyPrintSettings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PrettyPrintSettings):
        """
        Dynamic initializer for PrettyPrintSettings.
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
    def __init__(self):
        """public com.badlogic.gdx.utils.JsonValue$PrettyPrintSettings()"""
        val = __PrettyPrintSettings()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.JsonValue$PrettyPrintSettings()"""
        val = __PrettyPrintSettings()
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
 
 
# CLASS: com.badlogic.gdx.utils.PropertiesUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.utils.PropertiesUtils as __PropertiesUtils
__PropertiesUtils = __PropertiesUtils
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PropertiesUtils():
    """com.badlogic.gdx.utils.PropertiesUtils"""
 
    @staticmethod
    def __wrap(java_value: __PropertiesUtils) -> 'PropertiesUtils':
        return PropertiesUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PropertiesUtils):
        """
        Dynamic initializer for PropertiesUtils.
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

    @staticmethod
    @overload
    def load(arg0: 'ObjectMap', arg1: 'Reader'):
        """public static void com.badlogic.gdx.utils.PropertiesUtils.load(com.badlogic.gdx.utils.ObjectMap<java.lang.String, java.lang.String>,java.io.Reader) throws java.io.IOException"""
        __PropertiesUtils.load(arg0, arg1)

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

    @staticmethod
    @overload
    def store(arg0: 'ObjectMap', arg1: 'Writer', arg2: str):
        """public static void com.badlogic.gdx.utils.PropertiesUtils.store(com.badlogic.gdx.utils.ObjectMap<java.lang.String, java.lang.String>,java.io.Writer,java.lang.String) throws java.io.IOException"""
        __PropertiesUtils.store(arg0, arg1, arg2) 
 
 
# CLASS: com.badlogic.gdx.utils.Queue
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.Queue as __Queue
__Queue = __Queue
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
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
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Queue():
    """com.badlogic.gdx.utils.Queue"""
 
    @staticmethod
    def __wrap(java_value: __Queue) -> 'Queue':
        return Queue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Queue):
        """
        Dynamic initializer for Queue.
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
    def removeLast(self) -> object:
        """public T com.badlogic.gdx.utils.Queue.removeLast()"""
        return object.__wrap(super(Queue, self).removeLast())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Queue.toString(java.lang.String)"""
        return str.__wrap(super(__Queue, self).toString(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Queue.toString()"""
        return str.__wrap(super(Queue, self).toString())

    @overload
    def removeIndex(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Queue.removeIndex(int)"""
        return object.__wrap(super(__Queue, self).removeIndex(__int.valueOf(arg0)))

    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.utils.Queue.first()"""
        return object.__wrap(super(Queue, self).first())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.Queue(int)"""
        val = __Queue(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addLast(self, arg0: object):
        """public void com.badlogic.gdx.utils.Queue.addLast(T)"""
        super(__Queue, self).addLast(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.Queue.hashCode()"""
        return int.__wrap(super(Queue, self).hashCode())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Queue.isEmpty()"""
        return bool.__wrap(super(Queue, self).isEmpty())

    @overload
    def last(self) -> object:
        """public T com.badlogic.gdx.utils.Queue.last()"""
        return object.__wrap(super(Queue, self).last())

    @overload
    def removeValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Queue.removeValue(T,boolean)"""
        return bool.__wrap(super(__Queue, self).removeValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Queue.get(int)"""
        return object.__wrap(super(__Queue, self).get(__int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Queue.indexOf(T,boolean)"""
        return int.__wrap(super(__Queue, self).indexOf(arg0, __boolean.valueOf(arg1)))

    @overload
    def addFirst(self, arg0: object):
        """public void com.badlogic.gdx.utils.Queue.addFirst(T)"""
        super(__Queue, self).addFirst(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Queue.equals(java.lang.Object)"""
        return bool.__wrap(super(__Queue, self).equals(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Queue()"""
        val = __Queue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'Class'):
        """public com.badlogic.gdx.utils.Queue(int,java.lang.Class<T>)"""
        val = __Queue(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Queue.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__Queue, self).equalsIdentity(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Queue.clear()"""
        super(Queue, self).clear()

    @overload
    def removeFirst(self) -> object:
        """public T com.badlogic.gdx.utils.Queue.removeFirst()"""
        return object.__wrap(super(Queue, self).removeFirst())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Queue.notEmpty()"""
        return bool.__wrap(super(Queue, self).notEmpty())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.gdx.utils.Queue.iterator()"""
        return 'Iterator'.__wrap(super(Queue, self).iterator())

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.Queue.ensureCapacity(int)"""
        super(__Queue, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Queue()"""
        val = __Queue()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.BinaryHeap
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.BinaryHeap as __BinaryHeap_Node
__Node = __BinaryHeap_Node.Node
import com.badlogic.gdx.utils.BinaryHeap as __BinaryHeap
__BinaryHeap = __BinaryHeap
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BinaryHeap():
    """com.badlogic.gdx.utils.BinaryHeap"""
 
    @staticmethod
    def __wrap(java_value: __BinaryHeap) -> 'BinaryHeap':
        return BinaryHeap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BinaryHeap):
        """
        Dynamic initializer for BinaryHeap.
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
        """public com.badlogic.gdx.utils.BinaryHeap()"""
        val = __BinaryHeap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.BinaryHeap.isEmpty()"""
        return bool.__wrap(super(BinaryHeap, self).isEmpty())

    @overload
    def setValue(self, arg0: 'Node', arg1: float):
        """public void com.badlogic.gdx.utils.BinaryHeap.setValue(T,float)"""
        super(__BinaryHeap, self).setValue(arg0, __float.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.BinaryHeap.notEmpty()"""
        return bool.__wrap(super(BinaryHeap, self).notEmpty())

    @overload
    def pop(self) -> 'Node':
        """public T com.badlogic.gdx.utils.BinaryHeap.pop()"""
        return 'Node'.__wrap(super(BinaryHeap, self).pop())

    @overload
    def contains(self, arg0: 'Node', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.BinaryHeap.contains(T,boolean)"""
        return bool.__wrap(super(__BinaryHeap, self).contains(arg0, __boolean.valueOf(arg1)))

    @overload
    def peek(self) -> 'Node':
        """public T com.badlogic.gdx.utils.BinaryHeap.peek()"""
        return 'Node'.__wrap(super(BinaryHeap, self).peek())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.BinaryHeap.equals(java.lang.Object)"""
        return bool.__wrap(super(__BinaryHeap, self).equals(arg0))

    @overload
    def add(self, arg0: 'Node', arg1: float) -> 'Node':
        """public T com.badlogic.gdx.utils.BinaryHeap.add(T,float)"""
        return 'Node'.__wrap(super(__BinaryHeap, self).add(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public com.badlogic.gdx.utils.BinaryHeap(int,boolean)"""
        val = __BinaryHeap(__int.valueOf(arg0), __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.BinaryHeap.clear()"""
        super(BinaryHeap, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.BinaryHeap.hashCode()"""
        return int.__wrap(super(BinaryHeap, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'Node') -> 'Node':
        """public T com.badlogic.gdx.utils.BinaryHeap.add(T)"""
        return 'Node'.__wrap(super(__BinaryHeap, self).add(arg0))

    @overload
    def remove(self, arg0: 'Node') -> 'Node':
        """public T com.badlogic.gdx.utils.BinaryHeap.remove(T)"""
        return 'Node'.__wrap(super(__BinaryHeap, self).remove(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.BinaryHeap()"""
        val = __BinaryHeap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.BinaryHeap.toString()"""
        return str.__wrap(super(BinaryHeap, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.utils.LongMap$Entry
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
import com.badlogic.gdx.utils.LongMap as __LongMap_Entry
__Entry = __LongMap_Entry.Entry
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Entry():
    """com.badlogic.gdx.utils.LongMap.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.LongMap$Entry()"""
        val = __Entry()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.LongMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public java.lang.String com.badlogic.gdx.utils.LongMap$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.FloatArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.utils.FloatArray as __FloatArray
__FloatArray = __FloatArray
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FloatArray():
    """com.badlogic.gdx.utils.FloatArray"""
 
    @staticmethod
    def __wrap(java_value: __FloatArray) -> 'FloatArray':
        return FloatArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatArray):
        """
        Dynamic initializer for FloatArray.
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
    def addAll(self, arg0: 'FloatArray', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.FloatArray.addAll(com.badlogic.gdx.utils.FloatArray,int,int)"""
        super(__FloatArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.FloatArray.swap(int,int)"""
        super(__FloatArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def with(*arg0: float) -> 'FloatArray':
        """public static com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.utils.FloatArray.with(float...)"""
        return FloatArray.__wrap(__FloatArray.with(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def first(self) -> float:
        """public float com.badlogic.gdx.utils.FloatArray.first()"""
        return float.__wrap(super(FloatArray, self).first())

    @overload
    def incr(self, arg0: float):
        """public void com.badlogic.gdx.utils.FloatArray.incr(float)"""
        super(__FloatArray, self).incr(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.FloatArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__FloatArray, self).equals(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: 'float', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.FloatArray(boolean,float[],int,int)"""
        val = __FloatArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def mul(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.utils.FloatArray.mul(int,float)"""
        super(__FloatArray, self).mul(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.FloatArray.hashCode()"""
        return int.__wrap(super(FloatArray, self).hashCode())

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.utils.FloatArray.add(float,float,float,float)"""
        super(__FloatArray, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.FloatArray.shuffle()"""
        super(FloatArray, self).shuffle()

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.FloatArray.notEmpty()"""
        return bool.__wrap(super(FloatArray, self).notEmpty())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.FloatArray.clear()"""
        super(FloatArray, self).clear()

    @overload
    def pop(self) -> float:
        """public float com.badlogic.gdx.utils.FloatArray.pop()"""
        return float.__wrap(super(FloatArray, self).pop())

    @overload
    def toArray(self) -> List[float]:
        """public float[] com.badlogic.gdx.utils.FloatArray.toArray()"""
        return List[float].__wrap(super(FloatArray, self).toArray())

    @overload
    def removeValue(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.utils.FloatArray.removeValue(float)"""
        return bool.__wrap(super(__FloatArray, self).removeValue(__float.valueOf(arg0)))

    @overload
    def lastIndexOf(self, arg0: float) -> int:
        """public int com.badlogic.gdx.utils.FloatArray.lastIndexOf(float)"""
        return int.__wrap(super(__FloatArray, self).lastIndexOf(__float.valueOf(arg0)))

    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.FloatArray.removeRange(int,int)"""
        super(__FloatArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def ensureCapacity(self, arg0: int) -> List[float]:
        """public float[] com.badlogic.gdx.utils.FloatArray.ensureCapacity(int)"""
        return List[float].__wrap(super(__FloatArray, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.FloatArray.toString(java.lang.String)"""
        return str.__wrap(super(__FloatArray, self).toString(arg0))

    @overload
    def incr(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.utils.FloatArray.incr(int,float)"""
        super(__FloatArray, self).incr(__int.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.FloatArray(int)"""
        val = __FloatArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def peek(self) -> float:
        """public float com.badlogic.gdx.utils.FloatArray.peek()"""
        return float.__wrap(super(FloatArray, self).peek())

    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.FloatArray.sort()"""
        super(FloatArray, self).sort()

    @overload
    def equals(self, arg0: object, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.utils.FloatArray.equals(java.lang.Object,float)"""
        return bool.__wrap(super(__FloatArray, self).equals(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.FloatArray.toString()"""
        return str.__wrap(super(FloatArray, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.utils.FloatArray.contains(float)"""
        return bool.__wrap(super(__FloatArray, self).contains(__float.valueOf(arg0)))

    @overload
    def setSize(self, arg0: int) -> List[float]:
        """public float[] com.badlogic.gdx.utils.FloatArray.setSize(int)"""
        return List[float].__wrap(super(__FloatArray, self).setSize(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.FloatArray()"""
        val = __FloatArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> float:
        """public float com.badlogic.gdx.utils.FloatArray.get(int)"""
        return float.__wrap(super(__FloatArray, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.FloatArray.truncate(int)"""
        super(__FloatArray, self).truncate(__int.valueOf(arg0))

    @overload
    def indexOf(self, arg0: float) -> int:
        """public int com.badlogic.gdx.utils.FloatArray.indexOf(float)"""
        return int.__wrap(super(__FloatArray, self).indexOf(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.utils.FloatArray(float[])"""
        val = __FloatArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FloatArray'):
        """public com.badlogic.gdx.utils.FloatArray(com.badlogic.gdx.utils.FloatArray)"""
        val = __FloatArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def insert(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.utils.FloatArray.insert(int,float)"""
        super(__FloatArray, self).insert(__int.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def add(self, arg0: float):
        """public void com.badlogic.gdx.utils.FloatArray.add(float)"""
        super(__FloatArray, self).add(__float.valueOf(arg0))

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.FloatArray.reverse()"""
        super(FloatArray, self).reverse()

    @overload
    def set(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.utils.FloatArray.set(int,float)"""
        super(__FloatArray, self).set(__int.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def mul(self, arg0: float):
        """public void com.badlogic.gdx.utils.FloatArray.mul(float)"""
        super(__FloatArray, self).mul(__float.valueOf(arg0))

    @overload
    def shrink(self) -> List[float]:
        """public float[] com.badlogic.gdx.utils.FloatArray.shrink()"""
        return List[float].__wrap(super(FloatArray, self).shrink())

    @overload
    def removeIndex(self, arg0: int) -> float:
        """public float com.badlogic.gdx.utils.FloatArray.removeIndex(int)"""
        return float.__wrap(super(__FloatArray, self).removeIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.FloatArray(boolean,int)"""
        val = __FloatArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.FloatArray.add(float,float)"""
        super(__FloatArray, self).add(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.FloatArray.insertRange(int,int)"""
        super(__FloatArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.FloatArray()"""
        val = __FloatArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeAll(self, arg0: 'FloatArray') -> bool:
        """public boolean com.badlogic.gdx.utils.FloatArray.removeAll(com.badlogic.gdx.utils.FloatArray)"""
        return bool.__wrap(super(__FloatArray, self).removeAll(arg0))

    @overload
    def random(self) -> float:
        """public float com.badlogic.gdx.utils.FloatArray.random()"""
        return float.__wrap(super(FloatArray, self).random())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.FloatArray.isEmpty()"""
        return bool.__wrap(super(FloatArray, self).isEmpty())

    @overload
    def addAll(self, arg0: 'FloatArray'):
        """public void com.badlogic.gdx.utils.FloatArray.addAll(com.badlogic.gdx.utils.FloatArray)"""
        super(__FloatArray, self).addAll(arg0)

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
    def addAll(self, *arg0: float):
        """public void com.badlogic.gdx.utils.FloatArray.addAll(float...)"""
        super(__FloatArray, self).addAll(arg0)

    @overload
    def addAll(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.FloatArray.addAll(float[],int,int)"""
        super(__FloatArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.utils.FloatArray.add(float,float,float)"""
        super(__FloatArray, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.IntArray as __IntArray
__IntArray = __IntArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntArray():
    """com.badlogic.gdx.utils.IntArray"""
 
    @staticmethod
    def __wrap(java_value: __IntArray) -> 'IntArray':
        return IntArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntArray):
        """
        Dynamic initializer for IntArray.
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
    def addAll(self, arg0: 'IntArray'):
        """public void com.badlogic.gdx.utils.IntArray.addAll(com.badlogic.gdx.utils.IntArray)"""
        super(__IntArray, self).addAll(arg0)

    @overload
    def random(self) -> int:
        """public int com.badlogic.gdx.utils.IntArray.random()"""
        return int.__wrap(super(IntArray, self).random())

    @overload
    def removeValue(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntArray.removeValue(int)"""
        return bool.__wrap(super(__IntArray, self).removeValue(__int.valueOf(arg0)))

    @overload
    def incr(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntArray.incr(int)"""
        super(__IntArray, self).incr(__int.valueOf(arg0))

    @overload
    def removeIndex(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.IntArray.removeIndex(int)"""
        return int.__wrap(super(__IntArray, self).removeIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def lastIndexOf(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.IntArray.lastIndexOf(int)"""
        return int.__wrap(super(__IntArray, self).lastIndexOf(__int.valueOf(arg0)))

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntArray.truncate(int)"""
        super(__IntArray, self).truncate(__int.valueOf(arg0))

    @overload
    def shrink(self) -> List[int]:
        """public int[] com.badlogic.gdx.utils.IntArray.shrink()"""
        return List[int].__wrap(super(IntArray, self).shrink())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def peek(self) -> int:
        """public int com.badlogic.gdx.utils.IntArray.peek()"""
        return int.__wrap(super(IntArray, self).peek())

    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntArray.swap(int,int)"""
        super(__IntArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.IntArray(int)"""
        val = __IntArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'IntArray'):
        """public com.badlogic.gdx.utils.IntArray(com.badlogic.gdx.utils.IntArray)"""
        val = __IntArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeAll(self, arg0: 'IntArray') -> bool:
        """public boolean com.badlogic.gdx.utils.IntArray.removeAll(com.badlogic.gdx.utils.IntArray)"""
        return bool.__wrap(super(__IntArray, self).removeAll(arg0))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntArray.isEmpty()"""
        return bool.__wrap(super(IntArray, self).isEmpty())

    @overload
    def get(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.IntArray.get(int)"""
        return int.__wrap(super(__IntArray, self).get(__int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: 'IntArray', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.IntArray.addAll(com.badlogic.gdx.utils.IntArray,int,int)"""
        super(__IntArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'int'):
        """public com.badlogic.gdx.utils.IntArray(int[])"""
        val = __IntArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool, arg1: 'int', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.IntArray(boolean,int[],int,int)"""
        val = __IntArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.IntArray.add(int,int,int,int)"""
        super(__IntArray, self).add(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def add(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.IntArray.add(int,int,int)"""
        super(__IntArray, self).add(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def add(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntArray.add(int)"""
        super(__IntArray, self).add(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.IntArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntArray, self).equals(arg0))

    @overload
    def set(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntArray.set(int,int)"""
        super(__IntArray, self).set(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntArray.removeRange(int,int)"""
        super(__IntArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IntArray()"""
        val = __IntArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def incr(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntArray.incr(int,int)"""
        super(__IntArray, self).incr(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.IntArray.clear()"""
        super(IntArray, self).clear()

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.IntArray.toString(java.lang.String)"""
        return str.__wrap(super(__IntArray, self).toString(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IntArray()"""
        val = __IntArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setSize(self, arg0: int) -> List[int]:
        """public int[] com.badlogic.gdx.utils.IntArray.setSize(int)"""
        return List[int].__wrap(super(__IntArray, self).setSize(__int.valueOf(arg0)))

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.IntArray.reverse()"""
        super(IntArray, self).reverse()

    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntArray.insertRange(int,int)"""
        super(__IntArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def with(*arg0: int) -> 'IntArray':
        """public static com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntArray.with(int...)"""
        return IntArray.__wrap(__IntArray.with(arg0))

    @overload
    def indexOf(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.IntArray.indexOf(int)"""
        return int.__wrap(super(__IntArray, self).indexOf(__int.valueOf(arg0)))

    @overload
    def toArray(self) -> List[int]:
        """public int[] com.badlogic.gdx.utils.IntArray.toArray()"""
        return List[int].__wrap(super(IntArray, self).toArray())

    @overload
    def contains(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntArray.contains(int)"""
        return bool.__wrap(super(__IntArray, self).contains(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.IntArray.hashCode()"""
        return int.__wrap(super(IntArray, self).hashCode())

    @overload
    def insert(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntArray.insert(int,int)"""
        super(__IntArray, self).insert(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addAll(self, *arg0: int):
        """public void com.badlogic.gdx.utils.IntArray.addAll(int...)"""
        super(__IntArray, self).addAll(arg0)

    @overload
    def add(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntArray.add(int,int)"""
        super(__IntArray, self).add(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.IntArray.toString()"""
        return str.__wrap(super(IntArray, self).toString())

    @overload
    def mul(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntArray.mul(int,int)"""
        super(__IntArray, self).mul(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def ensureCapacity(self, arg0: int) -> List[int]:
        """public int[] com.badlogic.gdx.utils.IntArray.ensureCapacity(int)"""
        return List[int].__wrap(super(__IntArray, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntArray.notEmpty()"""
        return bool.__wrap(super(IntArray, self).notEmpty())

    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.IntArray.sort()"""
        super(IntArray, self).sort()

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.IntArray(boolean,int)"""
        val = __IntArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def addAll(self, arg0: 'int', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.IntArray.addAll(int[],int,int)"""
        super(__IntArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def first(self) -> int:
        """public int com.badlogic.gdx.utils.IntArray.first()"""
        return int.__wrap(super(IntArray, self).first())

    @overload
    def mul(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntArray.mul(int)"""
        super(__IntArray, self).mul(__int.valueOf(arg0))

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.IntArray.shuffle()"""
        super(IntArray, self).shuffle()

    @overload
    def pop(self) -> int:
        """public int com.badlogic.gdx.utils.IntArray.pop()"""
        return int.__wrap(super(IntArray, self).pop()) 
 
 
# CLASS: com.badlogic.gdx.utils.IntFloatMap$Entries
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap_Entries
__Entries = __IntFloatMap_Entries.Entries
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap_Entry
__Entry = __IntFloatMap_Entry.Entry
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.IntFloatMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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
    def remove(self):
        """public void com.badlogic.gdx.utils.IntFloatMap$Entries.remove()"""
        super(Entries, self).remove()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.IntFloatMap$Entry> com.badlogic.gdx.utils.IntFloatMap$Entries.iterator()"""
        return 'Iterator'.__wrap(super(Entries, self).iterator())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntFloatMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'IntFloatMap'):
        """public com.badlogic.gdx.utils.IntFloatMap$Entries(com.badlogic.gdx.utils.IntFloatMap)"""
        val = __Entries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.IntFloatMap$Entry com.badlogic.gdx.utils.IntFloatMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectMap$Values
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Values
__Values = __ObjectMap_Values.Values
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Values():
    """com.badlogic.gdx.utils.ObjectMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'ObjectMap'):
        """public com.badlogic.gdx.utils.ObjectMap$Values(com.badlogic.gdx.utils.ObjectMap<?, V>)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def next(self) -> object:
        """public V com.badlogic.gdx.utils.ObjectMap$Values.next()"""
        return object.__wrap(super(Values, self).next())

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

    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<V> com.badlogic.gdx.utils.ObjectMap$Values.toArray()"""
        return 'Array'.__wrap(super(Values, self).toArray())

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
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<V> com.badlogic.gdx.utils.ObjectMap$Values.toArray(com.badlogic.gdx.utils.Array<V>)"""
        return 'Array'.__wrap(super(__Values, self).toArray(arg0))

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectMap$Values<V> com.badlogic.gdx.utils.ObjectMap$Values.iterator()"""
        return 'Values'.__wrap(super(Values, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.SortedIntList
from builtins import str
import com.badlogic.gdx.utils.SortedIntList as __SortedIntList
__SortedIntList = __SortedIntList
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SortedIntList():
    """com.badlogic.gdx.utils.SortedIntList"""
 
    @staticmethod
    def __wrap(java_value: __SortedIntList) -> 'SortedIntList':
        return SortedIntList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedIntList):
        """
        Dynamic initializer for SortedIntList.
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
    def __init__(self):
        """public com.badlogic.gdx.utils.SortedIntList()"""
        val = __SortedIntList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.SortedIntList$Node<E>> com.badlogic.gdx.utils.SortedIntList.iterator()"""
        return 'Iterator'.__wrap(super(SortedIntList, self).iterator())

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
    def clear(self):
        """public void com.badlogic.gdx.utils.SortedIntList.clear()"""
        super(SortedIntList, self).clear()

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.SortedIntList.isEmpty()"""
        return bool.__wrap(super(SortedIntList, self).isEmpty())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def insert(self, arg0: int, arg1: object) -> object:
        """public E com.badlogic.gdx.utils.SortedIntList.insert(int,E)"""
        return object.__wrap(super(__SortedIntList, self).insert(__int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.SortedIntList()"""
        val = __SortedIntList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.utils.SortedIntList.size()"""
        return int.__wrap(super(SortedIntList, self).size())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.SortedIntList.notEmpty()"""
        return bool.__wrap(super(SortedIntList, self).notEmpty())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E com.badlogic.gdx.utils.SortedIntList.get(int)"""
        return object.__wrap(super(__SortedIntList, self).get(__int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.utils.OrderedMap
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entries
__Entries = __ObjectMap_Entries.Entries
import com.badlogic.gdx.utils.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Values
__Values = __ObjectMap_Values.Values
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap
__ObjectMap = __ObjectMap
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Keys
__Keys = __ObjectMap_Keys.Keys
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class OrderedMap():
    """com.badlogic.gdx.utils.OrderedMap"""
 
    @staticmethod
    def __wrap(java_value: __OrderedMap) -> 'OrderedMap':
        return OrderedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedMap):
        """
        Dynamic initializer for OrderedMap.
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
    def removeIndex(self, arg0: int) -> object:
        """public V com.badlogic.gdx.utils.OrderedMap.removeIndex(int)"""
        return object.__wrap(super(__OrderedMap, self).removeIndex(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.OrderedMap()"""
        val = __OrderedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__ObjectMap, self).equalsIdentity(arg0))

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectMap$Entries<K, V> com.badlogic.gdx.utils.OrderedMap.iterator()"""
        return 'Entries'.__wrap(super(OrderedMap, self).iterator())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.OrderedMap(int,float)"""
        val = __OrderedMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.OrderedMap.clear(int)"""
        super(__OrderedMap, self).clear(__int.valueOf(arg0))

    @override
    @overload
    def putAll(self, arg0: 'ObjectMap'):
        """public void com.badlogic.gdx.utils.ObjectMap.putAll(com.badlogic.gdx.utils.ObjectMap<? extends K, ? extends V>)"""
        super(__ObjectMap, self).putAll(arg0)

    @overload
    def remove(self, arg0: object) -> object:
        """public V com.badlogic.gdx.utils.OrderedMap.remove(K)"""
        return object.__wrap(super(__OrderedMap, self).remove(arg0))

    @overload
    def orderedKeys(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.OrderedMap.orderedKeys()"""
        return 'Array'.__wrap(super(OrderedMap, self).orderedKeys())

    @overload
    def findKey(self, arg0: object, arg1: bool) -> object:
        """public K com.badlogic.gdx.utils.ObjectMap.findKey(java.lang.Object,boolean)"""
        return object.__wrap(super(__ObjectMap, self).findKey(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: object) -> object:
        """public <T extends K> V com.badlogic.gdx.utils.ObjectMap.get(T)"""
        return object.__wrap(super(__ObjectMap, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectMap.toString()"""
        return str.__wrap(super(ObjectMap, self).toString())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.OrderedMap.clear()"""
        super(OrderedMap, self).clear()

    @override
    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectMap.shrink(int)"""
        super(__ObjectMap, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.notEmpty()"""
        return bool.__wrap(super(ObjectMap, self).notEmpty())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectMap.toString(java.lang.String)"""
        return str.__wrap(super(__ObjectMap, self).toString(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.OrderedMap()"""
        val = __OrderedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def alterIndex(self, arg0: int, arg1: object) -> bool:
        """public boolean com.badlogic.gdx.utils.OrderedMap.alterIndex(int,K)"""
        return bool.__wrap(super(__OrderedMap, self).alterIndex(__int.valueOf(arg0), arg1))

    @override
    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectMap$Keys<K> com.badlogic.gdx.utils.OrderedMap.keys()"""
        return 'Keys'.__wrap(super(OrderedMap, self).keys())

    @override
    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectMap$Entries<K, V> com.badlogic.gdx.utils.OrderedMap.entries()"""
        return 'Entries'.__wrap(super(OrderedMap, self).entries())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.OrderedMap(int)"""
        val = __OrderedMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.ObjectMap.get(K,V)"""
        return object.__wrap(super(__ObjectMap, self).get(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def putAll(self, arg0: 'OrderedMap'):
        """public <T extends K> void com.badlogic.gdx.utils.OrderedMap.putAll(com.badlogic.gdx.utils.OrderedMap<T, ? extends V>)"""
        super(__OrderedMap, self).putAll(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectMap$Values<V> com.badlogic.gdx.utils.OrderedMap.values()"""
        return 'Values'.__wrap(super(OrderedMap, self).values())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ObjectMap.hashCode()"""
        return int.__wrap(super(ObjectMap, self).hashCode())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.isEmpty()"""
        return bool.__wrap(super(ObjectMap, self).isEmpty())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.OrderedMap.put(K,V)"""
        return object.__wrap(super(__OrderedMap, self).put(arg0, arg1))

    @overload
    def __init__(self, arg0: 'OrderedMap'):
        """public com.badlogic.gdx.utils.OrderedMap(com.badlogic.gdx.utils.OrderedMap<? extends K, ? extends V>)"""
        val = __OrderedMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.containsValue(java.lang.Object,boolean)"""
        return bool.__wrap(super(__ObjectMap, self).containsValue(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectMap, self).equals(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap.containsKey(K)"""
        return bool.__wrap(super(__ObjectMap, self).containsKey(arg0))

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectMap.ensureCapacity(int)"""
        super(__ObjectMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def alter(self, arg0: object, arg1: object) -> bool:
        """public boolean com.badlogic.gdx.utils.OrderedMap.alter(K,K)"""
        return bool.__wrap(super(__OrderedMap, self).alter(arg0, arg1)) 
 
 
# CLASS: com.badlogic.gdx.utils.PerformanceCounters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.PerformanceCounters as __PerformanceCounters
__PerformanceCounters = __PerformanceCounters
import com.badlogic.gdx.utils.PerformanceCounter as __PerformanceCounter
__PerformanceCounter = __PerformanceCounter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PerformanceCounters():
    """com.badlogic.gdx.utils.PerformanceCounters"""
 
    @staticmethod
    def __wrap(java_value: __PerformanceCounters) -> 'PerformanceCounters':
        return PerformanceCounters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PerformanceCounters):
        """
        Dynamic initializer for PerformanceCounters.
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
    def add(self, arg0: str) -> 'PerformanceCounter':
        """public com.badlogic.gdx.utils.PerformanceCounter com.badlogic.gdx.utils.PerformanceCounters.add(java.lang.String)"""
        return 'PerformanceCounter'.__wrap(super(__PerformanceCounters, self).add(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, arg0: str, arg1: int) -> 'PerformanceCounter':
        """public com.badlogic.gdx.utils.PerformanceCounter com.badlogic.gdx.utils.PerformanceCounters.add(java.lang.String,int)"""
        return 'PerformanceCounter'.__wrap(super(__PerformanceCounters, self).add(arg0, __int.valueOf(arg1)))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.PerformanceCounters()"""
        val = __PerformanceCounters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.PerformanceCounters()"""
        val = __PerformanceCounters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toString(self, arg0: 'StringBuilder') -> 'StringBuilder':
        """public com.badlogic.gdx.utils.StringBuilder com.badlogic.gdx.utils.PerformanceCounters.toString(com.badlogic.gdx.utils.StringBuilder)"""
        return 'StringBuilder'.__wrap(super(__PerformanceCounters, self).toString(arg0))

    @overload
    def tick(self):
        """public void com.badlogic.gdx.utils.PerformanceCounters.tick()"""
        super(PerformanceCounters, self).tick()

    @overload
    def tick(self, arg0: float):
        """public void com.badlogic.gdx.utils.PerformanceCounters.tick(float)"""
        super(__PerformanceCounters, self).tick(__float.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.utils.StreamUtils$OptimizedByteArrayOutputStream
from builtins import str
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
import com.badlogic.gdx.utils.StreamUtils as __StreamUtils_OptimizedByteArrayOutputStream
__OptimizedByteArrayOutputStream = __StreamUtils_OptimizedByteArrayOutputStream.OptimizedByteArrayOutputStream
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.io.ByteArrayOutputStream as __ByteArrayOutputStream
__ByteArrayOutputStream = __ByteArrayOutputStream
 
class OptimizedByteArrayOutputStream():
    """com.badlogic.gdx.utils.StreamUtils.OptimizedByteArrayOutputStream"""
 
    @staticmethod
    def __wrap(java_value: __OptimizedByteArrayOutputStream) -> 'OptimizedByteArrayOutputStream':
        return OptimizedByteArrayOutputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OptimizedByteArrayOutputStream):
        """
        Dynamic initializer for OptimizedByteArrayOutputStream.
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
    def reset(self):
        """public synchronized void java.io.ByteArrayOutputStream.reset()"""
        super(ByteArrayOutputStream, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public synchronized java.lang.String java.io.ByteArrayOutputStream.toString()"""
        return str.__wrap(super(ByteArrayOutputStream, self).toString())

    @override
    @overload
    def write(self, arg0: bytes, arg1: int, arg2: int):
        """public synchronized void java.io.ByteArrayOutputStream.write(byte[],int,int)"""
        super(__ByteArrayOutputStream, self).write(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getBuffer(self) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.StreamUtils$OptimizedByteArrayOutputStream.getBuffer()"""
        return List[int].__wrap(super(OptimizedByteArrayOutputStream, self).getBuffer())

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.OutputStream.write(byte[]) throws java.io.IOException"""
        super(__OutputStream, self).write(bytes)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def close(self):
        """public void java.io.ByteArrayOutputStream.close() throws java.io.IOException"""
        super(ByteArrayOutputStream, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def writeTo(self, arg0: 'OutputStream'):
        """public synchronized void java.io.ByteArrayOutputStream.writeTo(java.io.OutputStream) throws java.io.IOException"""
        super(__ByteArrayOutputStream, self).writeTo(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def flush(self):
        """public void java.io.OutputStream.flush() throws java.io.IOException"""
        super(OutputStream, self).flush()

    @override
    @overload
    def size(self) -> int:
        """public synchronized int java.io.ByteArrayOutputStream.size()"""
        return int.__wrap(super(ByteArrayOutputStream, self).size())

    @override
    @overload
    def writeBytes(self, arg0: bytes):
        """public void java.io.ByteArrayOutputStream.writeBytes(byte[])"""
        super(__ByteArrayOutputStream, self).writeBytes(bytes)

    @overload
    def toString(self, arg0: int) -> str:
        """public synchronized java.lang.String java.io.ByteArrayOutputStream.toString(int)"""
        return str.__wrap(super(__ByteArrayOutputStream, self).toString(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream.__wrap(__OutputStream.nullOutputStream())

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
    def toString(self, arg0: 'Charset') -> str:
        """public synchronized java.lang.String java.io.ByteArrayOutputStream.toString(java.nio.charset.Charset)"""
        return str.__wrap(super(__ByteArrayOutputStream, self).toString(arg0))

    @override
    @overload
    def toByteArray(self) -> List[int]:
        """public synchronized byte[] com.badlogic.gdx.utils.StreamUtils$OptimizedByteArrayOutputStream.toByteArray()"""
        return List[int].__wrap(super(OptimizedByteArrayOutputStream, self).toByteArray())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: int):
        """public synchronized void java.io.ByteArrayOutputStream.write(int)"""
        super(__ByteArrayOutputStream, self).write(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.StreamUtils$OptimizedByteArrayOutputStream(int)"""
        val = __OptimizedByteArrayOutputStream(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toString(self, arg0: str) -> str:
        """public synchronized java.lang.String java.io.ByteArrayOutputStream.toString(java.lang.String) throws java.io.UnsupportedEncodingException"""
        return str.__wrap(super(__ByteArrayOutputStream, self).toString(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntIntMap$Entries
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap_Entries
__Entries = __IntIntMap_Entries.Entries
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap_Entry
__Entry = __IntIntMap_Entry.Entry
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.IntIntMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.IntIntMap$Entry> com.badlogic.gdx.utils.IntIntMap$Entries.iterator()"""
        return 'Iterator'.__wrap(super(Entries, self).iterator())

    @override
    @overload
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.IntIntMap$Entry com.badlogic.gdx.utils.IntIntMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntIntMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'IntIntMap'):
        """public com.badlogic.gdx.utils.IntIntMap$Entries(com.badlogic.gdx.utils.IntIntMap)"""
        val = __Entries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectFloatMap$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap_Keys
__Keys = __ObjectFloatMap_Keys.Keys
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Keys():
    """com.badlogic.gdx.utils.ObjectFloatMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectFloatMap$Keys.toArray(com.badlogic.gdx.utils.Array<K>)"""
        return 'Array'.__wrap(super(__Keys, self).toArray(arg0))

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

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap$Keys.hasNext()"""
        return bool.__wrap(super(Keys, self).hasNext())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectFloatMap$Keys.toArray()"""
        return 'Array'.__wrap(super(Keys, self).toArray())

    @override
    @overload
    def iterator(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectFloatMap$Keys<K> com.badlogic.gdx.utils.ObjectFloatMap$Keys.iterator()"""
        return 'Keys'.__wrap(super(Keys, self).iterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def next(self) -> object:
        """public K com.badlogic.gdx.utils.ObjectFloatMap$Keys.next()"""
        return object.__wrap(super(Keys, self).next())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ObjectFloatMap'):
        """public com.badlogic.gdx.utils.ObjectFloatMap$Keys(com.badlogic.gdx.utils.ObjectFloatMap<K>)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectLongMap$Entry
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
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap_Entry
__Entry = __ObjectLongMap_Entry.Entry
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Entry():
    """com.badlogic.gdx.utils.ObjectLongMap.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectLongMap$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectLongMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectLongMap$Entry()"""
        val = __Entry()
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
 
 
# CLASS: com.badlogic.gdx.utils.Timer$Task
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.Timer as __Timer_Task
__Task = __Timer_Task.Task
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
 
class Task(ABC):
    """com.badlogic.gdx.utils.Timer.Task"""
 
    @staticmethod
    def __wrap(java_value: __Task) -> 'Task':
        return Task(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Task):
        """
        Dynamic initializer for Task.
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
    def run(self, ):
        """public abstract void com.badlogic.gdx.utils.Timer$Task.run()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Timer$Task()"""
        val = __Task()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getExecuteTimeMillis(self) -> int:
        """public synchronized long com.badlogic.gdx.utils.Timer$Task.getExecuteTimeMillis()"""
        return int.__wrap(super(Task, self).getExecuteTimeMillis())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Timer$Task()"""
        val = __Task()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.utils.Timer$Task.cancel()"""
        super(Task, self).cancel()

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
    def isScheduled(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Timer$Task.isScheduled()"""
        return bool.__wrap(super(Task, self).isScheduled())

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
 
 
# CLASS: com.badlogic.gdx.utils.OrderedMap$OrderedMapKeys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Keys
__Keys = __ObjectMap_Keys.Keys
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.OrderedMap as __OrderedMap_OrderedMapKeys
__OrderedMapKeys = __OrderedMap_OrderedMapKeys.OrderedMapKeys
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class OrderedMapKeys():
    """com.badlogic.gdx.utils.OrderedMap.OrderedMapKeys"""
 
    @staticmethod
    def __wrap(java_value: __OrderedMapKeys) -> 'OrderedMapKeys':
        return OrderedMapKeys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedMapKeys):
        """
        Dynamic initializer for OrderedMapKeys.
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
    def next(self) -> object:
        """public K com.badlogic.gdx.utils.OrderedMap$OrderedMapKeys.next()"""
        return object.__wrap(super(OrderedMapKeys, self).next())

    @override
    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.OrderedMap$OrderedMapKeys.toArray()"""
        return 'Array'.__wrap(super(OrderedMapKeys, self).toArray())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap$Keys.hasNext()"""
        return bool.__wrap(super(Keys, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def iterator(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectMap$Keys<K> com.badlogic.gdx.utils.ObjectMap$Keys.iterator()"""
        return 'Keys'.__wrap(super(Keys, self).iterator())

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.OrderedMap$OrderedMapKeys.toArray(com.badlogic.gdx.utils.Array<K>)"""
        return 'Array'.__wrap(super(__OrderedMapKeys, self).toArray(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.utils.OrderedMap$OrderedMapKeys.reset()"""
        super(OrderedMapKeys, self).reset()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.OrderedMap$OrderedMapKeys.remove()"""
        super(OrderedMapKeys, self).remove()

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'OrderedMap'):
        """public com.badlogic.gdx.utils.OrderedMap$OrderedMapKeys(com.badlogic.gdx.utils.OrderedMap<K, ?>)"""
        val = __OrderedMapKeys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Base64Coder$CharMap
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.Base64Coder as __Base64Coder_CharMap
__CharMap = __Base64Coder_CharMap.CharMap
from typing import List
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
 
class CharMap():
    """com.badlogic.gdx.utils.Base64Coder.CharMap"""
 
    @staticmethod
    def __wrap(java_value: __CharMap) -> 'CharMap':
        return CharMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharMap):
        """
        Dynamic initializer for CharMap.
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
    def getEncodingMap(self) -> List[str]:
        """public char[] com.badlogic.gdx.utils.Base64Coder$CharMap.getEncodingMap()"""
        return List[str].__wrap(super(CharMap, self).getEncodingMap())

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
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.utils.Base64Coder$CharMap(char,char)"""
        val = __CharMap(__char.valueOf(arg0), __char.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDecodingMap(self) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.Base64Coder$CharMap.getDecodingMap()"""
        return List[int].__wrap(super(CharMap, self).getDecodingMap())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntFloatMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap_Entries
__Entries = __IntFloatMap_Entries.Entries
from builtins import type
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap
__IntFloatMap = __IntFloatMap
from builtins import float
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap_Keys
__Keys = __IntFloatMap_Keys.Keys
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap_Values
__Values = __IntFloatMap_Values.Values
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class IntFloatMap():
    """com.badlogic.gdx.utils.IntFloatMap"""
 
    @staticmethod
    def __wrap(java_value: __IntFloatMap) -> 'IntFloatMap':
        return IntFloatMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntFloatMap):
        """
        Dynamic initializer for IntFloatMap.
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
        """public java.lang.String com.badlogic.gdx.utils.IntFloatMap.toString()"""
        return str.__wrap(super(IntFloatMap, self).toString())

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntFloatMap.shrink(int)"""
        super(__IntFloatMap, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'IntFloatMap'):
        """public com.badlogic.gdx.utils.IntFloatMap(com.badlogic.gdx.utils.IntFloatMap)"""
        val = __IntFloatMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntFloatMap.containsKey(int)"""
        return bool.__wrap(super(__IntFloatMap, self).containsKey(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.IntFloatMap$Keys com.badlogic.gdx.utils.IntFloatMap.keys()"""
        return 'Keys'.__wrap(super(IntFloatMap, self).keys())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IntFloatMap()"""
        val = __IntFloatMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.IntFloatMap.clear()"""
        super(IntFloatMap, self).clear()

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntFloatMap.ensureCapacity(int)"""
        super(__IntFloatMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.IntFloatMap$Entries com.badlogic.gdx.utils.IntFloatMap.entries()"""
        return 'Entries'.__wrap(super(IntFloatMap, self).entries())

    @overload
    def findKey(self, arg0: float, arg1: float, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.IntFloatMap.findKey(float,float,int)"""
        return int.__wrap(super(__IntFloatMap, self).findKey(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntFloatMap.clear(int)"""
        super(__IntFloatMap, self).clear(__int.valueOf(arg0))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntFloatMap.isEmpty()"""
        return bool.__wrap(super(IntFloatMap, self).isEmpty())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.IntFloatMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntFloatMap, self).equals(arg0))

    @overload
    def get(self, arg0: int, arg1: float) -> float:
        """public float com.badlogic.gdx.utils.IntFloatMap.get(int,float)"""
        return float.__wrap(super(__IntFloatMap, self).get(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def put(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.utils.IntFloatMap.put(int,float)"""
        super(__IntFloatMap, self).put(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.IntFloatMap.hashCode()"""
        return int.__wrap(super(IntFloatMap, self).hashCode())

    @overload
    def containsValue(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.utils.IntFloatMap.containsValue(float)"""
        return bool.__wrap(super(__IntFloatMap, self).containsValue(__float.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.IntFloatMap$Entry> com.badlogic.gdx.utils.IntFloatMap.iterator()"""
        return 'Iterator'.__wrap(super(IntFloatMap, self).iterator())

    @overload
    def findKey(self, arg0: float, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.IntFloatMap.findKey(float,int)"""
        return int.__wrap(super(__IntFloatMap, self).findKey(__float.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsValue(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.utils.IntFloatMap.containsValue(float,float)"""
        return bool.__wrap(super(__IntFloatMap, self).containsValue(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IntFloatMap()"""
        val = __IntFloatMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.IntFloatMap(int,float)"""
        val = __IntFloatMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putAll(self, arg0: 'IntFloatMap'):
        """public void com.badlogic.gdx.utils.IntFloatMap.putAll(com.badlogic.gdx.utils.IntFloatMap)"""
        super(__IntFloatMap, self).putAll(arg0)

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.IntFloatMap(int)"""
        val = __IntFloatMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: int, arg1: float) -> float:
        """public float com.badlogic.gdx.utils.IntFloatMap.remove(int,float)"""
        return float.__wrap(super(__IntFloatMap, self).remove(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def getAndIncrement(self, arg0: int, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.utils.IntFloatMap.getAndIncrement(int,float,float)"""
        return float.__wrap(super(__IntFloatMap, self).getAndIncrement(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def put(self, arg0: int, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.utils.IntFloatMap.put(int,float,float)"""
        return float.__wrap(super(__IntFloatMap, self).put(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntFloatMap.notEmpty()"""
        return bool.__wrap(super(IntFloatMap, self).notEmpty())

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.IntFloatMap$Values com.badlogic.gdx.utils.IntFloatMap.values()"""
        return 'Values'.__wrap(super(IntFloatMap, self).values()) 
 
 
# CLASS: com.badlogic.gdx.utils.BufferUtils
from pyquantum_helper import import_once as __import_once__
import java.nio.IntBuffer as IntBuffer
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import com.badlogic.gdx.utils.BufferUtils as __BufferUtils
__BufferUtils = __BufferUtils
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Class as __Class
__Class = __Class
import java.nio.CharBuffer as CharBuffer
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import java.lang.String as __String
__String = __String
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.nio.DoubleBuffer as __DoubleBuffer
__DoubleBuffer = __DoubleBuffer
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
import java.nio.CharBuffer as __CharBuffer
__CharBuffer = __CharBuffer
from builtins import int
 
class BufferUtils():
    """com.badlogic.gdx.utils.BufferUtils"""
 
    @staticmethod
    def __wrap(java_value: __BufferUtils) -> 'BufferUtils':
        return BufferUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BufferUtils):
        """
        Dynamic initializer for BufferUtils.
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
    def newFloatBuffer(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer com.badlogic.gdx.utils.BufferUtils.newFloatBuffer(int)"""
        return FloatBuffer.__wrap(__BufferUtils.newFloatBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def findFloats(arg0: 'float', arg1: int, arg2: 'float', arg3: int, arg4: float) -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.findFloats(float[],int,float[],int,float)"""
        return int.__wrap(__BufferUtils.findFloats(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __float.valueOf(arg4)))

    @staticmethod
    @overload
    def transform(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'Matrix4'):
        """public static void com.badlogic.gdx.utils.BufferUtils.transform(float[],int,int,int,com.badlogic.gdx.math.Matrix4)"""
        __BufferUtils.transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)

    @staticmethod
    @overload
    def copy(arg0: 'float', arg1: 'Buffer', arg2: int, arg3: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(float[],java.nio.Buffer,int,int)"""
        __BufferUtils.copy(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def newIntBuffer(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer com.badlogic.gdx.utils.BufferUtils.newIntBuffer(int)"""
        return IntBuffer.__wrap(__BufferUtils.newIntBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def transform(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'Matrix4'):
        """public static void com.badlogic.gdx.utils.BufferUtils.transform(java.nio.Buffer,int,int,int,com.badlogic.gdx.math.Matrix4)"""
        __BufferUtils.transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def transform(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'Matrix4', arg5: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.transform(java.nio.Buffer,int,int,int,com.badlogic.gdx.math.Matrix4,int)"""
        __BufferUtils.transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def newUnsafeByteBuffer(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer com.badlogic.gdx.utils.BufferUtils.newUnsafeByteBuffer(java.nio.ByteBuffer)"""
        return ByteBuffer.__wrap(__BufferUtils.newUnsafeByteBuffer(arg0))

    @staticmethod
    @overload
    def getUnsafeBufferAddress(arg0: 'Buffer') -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.getUnsafeBufferAddress(java.nio.Buffer)"""
        return int.__wrap(__BufferUtils.getUnsafeBufferAddress(arg0))

    @staticmethod
    @overload
    def copy(arg0: 'short', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(short[],int,java.nio.Buffer,int)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def newByteBuffer(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer com.badlogic.gdx.utils.BufferUtils.newByteBuffer(int)"""
        return ByteBuffer.__wrap(__BufferUtils.newByteBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def findFloats(arg0: 'Buffer', arg1: int, arg2: 'float', arg3: int, arg4: float) -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.findFloats(java.nio.Buffer,int,float[],int,float)"""
        return int.__wrap(__BufferUtils.findFloats(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __float.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def findFloats(arg0: 'float', arg1: int, arg2: 'Buffer', arg3: int) -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.findFloats(float[],int,java.nio.Buffer,int)"""
        return int.__wrap(__BufferUtils.findFloats(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def transform(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'Matrix3', arg5: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.transform(java.nio.Buffer,int,int,int,com.badlogic.gdx.math.Matrix3,int)"""
        __BufferUtils.transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def transform(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'Matrix3'):
        """public static void com.badlogic.gdx.utils.BufferUtils.transform(float[],int,int,int,com.badlogic.gdx.math.Matrix3)"""
        __BufferUtils.transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)

    @staticmethod
    @overload
    def newDoubleBuffer(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer com.badlogic.gdx.utils.BufferUtils.newDoubleBuffer(int)"""
        return DoubleBuffer.__wrap(__BufferUtils.newDoubleBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def findFloats(arg0: 'Buffer', arg1: int, arg2: 'float', arg3: int) -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.findFloats(java.nio.Buffer,int,float[],int)"""
        return int.__wrap(__BufferUtils.findFloats(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def copy(arg0: 'long', arg1: int, arg2: int, arg3: 'Buffer'):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(long[],int,int,java.nio.Buffer)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def newLongBuffer(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer com.badlogic.gdx.utils.BufferUtils.newLongBuffer(int)"""
        return LongBuffer.__wrap(__BufferUtils.newLongBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def copy(arg0: 'int', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(int[],int,java.nio.Buffer,int)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def disposeUnsafeByteBuffer(arg0: 'ByteBuffer'):
        """public static void com.badlogic.gdx.utils.BufferUtils.disposeUnsafeByteBuffer(java.nio.ByteBuffer)"""
        __BufferUtils.disposeUnsafeByteBuffer(arg0)

    @staticmethod
    @overload
    def clear(arg0: 'ByteBuffer', arg1: int):
        """public static native void com.badlogic.gdx.utils.BufferUtils.clear(java.nio.ByteBuffer,int)"""
        __BufferUtils.clear(arg0, __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def transform(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'Matrix3', arg5: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.transform(float[],int,int,int,com.badlogic.gdx.math.Matrix3,int)"""
        __BufferUtils.transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def findFloats(arg0: 'Buffer', arg1: int, arg2: 'Buffer', arg3: int, arg4: float) -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.findFloats(java.nio.Buffer,int,java.nio.Buffer,int,float)"""
        return int.__wrap(__BufferUtils.findFloats(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __float.valueOf(arg4)))

    @staticmethod
    @overload
    def copy(arg0: 'Buffer', arg1: 'Buffer', arg2: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(java.nio.Buffer,java.nio.Buffer,int)"""
        __BufferUtils.copy(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def findFloats(arg0: 'Buffer', arg1: int, arg2: 'Buffer', arg3: int) -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.findFloats(java.nio.Buffer,int,java.nio.Buffer,int)"""
        return int.__wrap(__BufferUtils.findFloats(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def copy(arg0: 'double', arg1: int, arg2: int, arg3: 'Buffer'):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(double[],int,int,java.nio.Buffer)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def copy(arg0: 'double', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(double[],int,java.nio.Buffer,int)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def copy(arg0: 'long', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(long[],int,java.nio.Buffer,int)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def copy(arg0: 'float', arg1: int, arg2: int, arg3: 'Buffer'):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(float[],int,int,java.nio.Buffer)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def copy(arg0: 'int', arg1: int, arg2: int, arg3: 'Buffer'):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(int[],int,int,java.nio.Buffer)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def copy(arg0: 'char', arg1: int, arg2: int, arg3: 'Buffer'):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(char[],int,int,java.nio.Buffer)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def newCharBuffer(arg0: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer com.badlogic.gdx.utils.BufferUtils.newCharBuffer(int)"""
        return CharBuffer.__wrap(__BufferUtils.newCharBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def findFloats(arg0: 'float', arg1: int, arg2: 'Buffer', arg3: int, arg4: float) -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.findFloats(float[],int,java.nio.Buffer,int,float)"""
        return int.__wrap(__BufferUtils.findFloats(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __float.valueOf(arg4)))

    @staticmethod
    @overload
    def copy(arg0: 'float', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(float[],int,java.nio.Buffer,int)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def transform(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'Matrix4', arg5: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.transform(float[],int,int,int,com.badlogic.gdx.math.Matrix4,int)"""
        __BufferUtils.transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def copy(arg0: bytes, arg1: int, arg2: 'Buffer', arg3: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(byte[],int,java.nio.Buffer,int)"""
        __BufferUtils.copy(bytes, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def findFloats(arg0: 'float', arg1: int, arg2: 'float', arg3: int) -> int:
        """public static long com.badlogic.gdx.utils.BufferUtils.findFloats(float[],int,float[],int)"""
        return int.__wrap(__BufferUtils.findFloats(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def newUnsafeByteBuffer(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer com.badlogic.gdx.utils.BufferUtils.newUnsafeByteBuffer(int)"""
        return ByteBuffer.__wrap(__BufferUtils.newUnsafeByteBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getAllocatedBytesUnsafe() -> int:
        """public static int com.badlogic.gdx.utils.BufferUtils.getAllocatedBytesUnsafe()"""
        return int.__wrap(__BufferUtils.getAllocatedBytesUnsafe())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def transform(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'Matrix3'):
        """public static void com.badlogic.gdx.utils.BufferUtils.transform(java.nio.Buffer,int,int,int,com.badlogic.gdx.math.Matrix3)"""
        __BufferUtils.transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)

    @staticmethod
    @overload
    def newShortBuffer(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer com.badlogic.gdx.utils.BufferUtils.newShortBuffer(int)"""
        return ShortBuffer.__wrap(__BufferUtils.newShortBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def isUnsafeByteBuffer(arg0: 'ByteBuffer') -> bool:
        """public static boolean com.badlogic.gdx.utils.BufferUtils.isUnsafeByteBuffer(java.nio.ByteBuffer)"""
        return bool.__wrap(__BufferUtils.isUnsafeByteBuffer(arg0))

    @staticmethod
    @overload
    def copy(arg0: 'char', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void com.badlogic.gdx.utils.BufferUtils.copy(char[],int,java.nio.Buffer,int)"""
        __BufferUtils.copy(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)) 
 
 
# CLASS: com.badlogic.gdx.utils.ByteArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.ByteArray as __ByteArray
__ByteArray = __ByteArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ByteArray():
    """com.badlogic.gdx.utils.ByteArray"""
 
    @staticmethod
    def __wrap(java_value: __ByteArray) -> 'ByteArray':
        return ByteArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteArray):
        """
        Dynamic initializer for ByteArray.
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
    def peek(self) -> int:
        """public byte com.badlogic.gdx.utils.ByteArray.peek()"""
        return int.__wrap(super(ByteArray, self).peek())

    @overload
    def incr(self, arg0: int):
        """public void com.badlogic.gdx.utils.ByteArray.incr(byte)"""
        super(__ByteArray, self).incr(__byte.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ByteArray.hashCode()"""
        return int.__wrap(super(ByteArray, self).hashCode())

    @overload
    def contains(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.ByteArray.contains(byte)"""
        return bool.__wrap(super(__ByteArray, self).contains(__byte.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def with(*arg0: int) -> 'ByteArray':
        """public static com.badlogic.gdx.utils.ByteArray com.badlogic.gdx.utils.ByteArray.with(byte...)"""
        return ByteArray.__wrap(__ByteArray.with(bytes))

    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ByteArray.removeRange(int,int)"""
        super(__ByteArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ByteArray.add(byte,byte)"""
        super(__ByteArray, self).add(__byte.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def add(self, arg0: int):
        """public void com.badlogic.gdx.utils.ByteArray.add(byte)"""
        super(__ByteArray, self).add(__byte.valueOf(arg0))

    @overload
    def removeIndex(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.ByteArray.removeIndex(int)"""
        return int.__wrap(super(__ByteArray, self).removeIndex(__int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: 'ByteArray', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ByteArray.addAll(com.badlogic.gdx.utils.ByteArray,int,int)"""
        super(__ByteArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def removeAll(self, arg0: 'ByteArray') -> bool:
        """public boolean com.badlogic.gdx.utils.ByteArray.removeAll(com.badlogic.gdx.utils.ByteArray)"""
        return bool.__wrap(super(__ByteArray, self).removeAll(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: bytes, arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.ByteArray(boolean,byte[],int,int)"""
        val = __ByteArray(__boolean.valueOf(arg0), bytes, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.ByteArray.shuffle()"""
        super(ByteArray, self).shuffle()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ByteArray()"""
        val = __ByteArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ByteArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__ByteArray, self).equals(arg0))

    @overload
    def set(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ByteArray.set(int,byte)"""
        super(__ByteArray, self).set(__int.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def shrink(self) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.ByteArray.shrink()"""
        return List[int].__wrap(super(ByteArray, self).shrink())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ByteArray.isEmpty()"""
        return bool.__wrap(super(ByteArray, self).isEmpty())

    @overload
    def pop(self) -> int:
        """public byte com.badlogic.gdx.utils.ByteArray.pop()"""
        return int.__wrap(super(ByteArray, self).pop())

    @overload
    def insert(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ByteArray.insert(int,byte)"""
        super(__ByteArray, self).insert(__int.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ByteArray.toString(java.lang.String)"""
        return str.__wrap(super(__ByteArray, self).toString(arg0))

    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ByteArray.swap(int,int)"""
        super(__ByteArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ByteArray.insertRange(int,int)"""
        super(__ByteArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.ByteArray(int)"""
        val = __ByteArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ByteArray.toString()"""
        return str.__wrap(super(ByteArray, self).toString())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ByteArray.notEmpty()"""
        return bool.__wrap(super(ByteArray, self).notEmpty())

    @overload
    def add(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ByteArray.add(byte,byte,byte)"""
        super(__ByteArray, self).add(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2))

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.ByteArray.truncate(int)"""
        super(__ByteArray, self).truncate(__int.valueOf(arg0))

    @overload
    def ensureCapacity(self, arg0: int) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.ByteArray.ensureCapacity(int)"""
        return List[int].__wrap(super(__ByteArray, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def add(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.ByteArray.add(byte,byte,byte,byte)"""
        super(__ByteArray, self).add(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2), __byte.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def lastIndexOf(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.ByteArray.lastIndexOf(byte)"""
        return int.__wrap(super(__ByteArray, self).lastIndexOf(__byte.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mul(self, arg0: int):
        """public void com.badlogic.gdx.utils.ByteArray.mul(byte)"""
        super(__ByteArray, self).mul(__byte.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ByteArray'):
        """public com.badlogic.gdx.utils.ByteArray(com.badlogic.gdx.utils.ByteArray)"""
        val = __ByteArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def first(self) -> int:
        """public byte com.badlogic.gdx.utils.ByteArray.first()"""
        return int.__wrap(super(ByteArray, self).first())

    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.ByteArray.sort()"""
        super(ByteArray, self).sort()

    @overload
    def indexOf(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.ByteArray.indexOf(byte)"""
        return int.__wrap(super(__ByteArray, self).indexOf(__byte.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ByteArray()"""
        val = __ByteArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.ByteArray(boolean,int)"""
        val = __ByteArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ByteArray.clear()"""
        super(ByteArray, self).clear()

    @overload
    def addAll(self, arg0: bytes, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ByteArray.addAll(byte[],int,int)"""
        super(__ByteArray, self).addAll(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def toArray(self) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.ByteArray.toArray()"""
        return List[int].__wrap(super(ByteArray, self).toArray())

    @overload
    def incr(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ByteArray.incr(int,byte)"""
        super(__ByteArray, self).incr(__int.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def removeValue(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.ByteArray.removeValue(byte)"""
        return bool.__wrap(super(__ByteArray, self).removeValue(__byte.valueOf(arg0)))

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.ByteArray.reverse()"""
        super(ByteArray, self).reverse()

    @overload
    def mul(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ByteArray.mul(int,byte)"""
        super(__ByteArray, self).mul(__int.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def get(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.ByteArray.get(int)"""
        return int.__wrap(super(__ByteArray, self).get(__int.valueOf(arg0)))

    @overload
    def addAll(self, *arg0: int):
        """public void com.badlogic.gdx.utils.ByteArray.addAll(byte...)"""
        super(__ByteArray, self).addAll(bytes)

    @overload
    def random(self) -> int:
        """public byte com.badlogic.gdx.utils.ByteArray.random()"""
        return int.__wrap(super(ByteArray, self).random())

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
    def addAll(self, arg0: 'ByteArray'):
        """public void com.badlogic.gdx.utils.ByteArray.addAll(com.badlogic.gdx.utils.ByteArray)"""
        super(__ByteArray, self).addAll(arg0)

    @overload
    def __init__(self, arg0: bytes):
        """public com.badlogic.gdx.utils.ByteArray(byte[])"""
        val = __ByteArray(bytes)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setSize(self, arg0: int) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.ByteArray.setSize(int)"""
        return List[int].__wrap(super(__ByteArray, self).setSize(__int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.utils.Json$ReadOnlySerializer
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
import com.badlogic.gdx.utils.Json as __Json_ReadOnlySerializer
__ReadOnlySerializer = __Json_ReadOnlySerializer.ReadOnlySerializer
from builtins import bool
from builtins import int
 
class ReadOnlySerializer(ABC):
    """com.badlogic.gdx.utils.Json.ReadOnlySerializer"""
 
    @staticmethod
    def __wrap(java_value: __ReadOnlySerializer) -> 'ReadOnlySerializer':
        return ReadOnlySerializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReadOnlySerializer):
        """
        Dynamic initializer for ReadOnlySerializer.
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
    def __init__(self):
        """public com.badlogic.gdx.utils.Json$ReadOnlySerializer()"""
        val = __ReadOnlySerializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def read(self, arg0: 'Json', arg1: 'JsonValue', arg2: 'Class'):
        """public abstract T com.badlogic.gdx.utils.Json$ReadOnlySerializer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue,java.lang.Class)"""
        pass

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

    @override
    @overload
    def write(self, arg0: 'Json', arg1: object, arg2: 'Class'):
        """public void com.badlogic.gdx.utils.Json$ReadOnlySerializer.write(com.badlogic.gdx.utils.Json,T,java.lang.Class)"""
        super(__ReadOnlySerializer, self).write(arg0, arg1, arg2)

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Json$ReadOnlySerializer()"""
        val = __ReadOnlySerializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Predicate$PredicateIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.Predicate as __Predicate_PredicateIterator
__PredicateIterator = __Predicate_PredicateIterator.PredicateIterator
import java.lang.Iterable as Iterable
from builtins import object
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
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
 
class PredicateIterator():
    """com.badlogic.gdx.utils.Predicate.PredicateIterator"""
 
    @staticmethod
    def __wrap(java_value: __PredicateIterator) -> 'PredicateIterator':
        return PredicateIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicateIterator):
        """
        Dynamic initializer for PredicateIterator.
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
    def __init__(self, arg0: 'Iterable', arg1: 'Predicate'):
        """public com.badlogic.gdx.utils.Predicate$PredicateIterator(java.lang.Iterable<T>,com.badlogic.gdx.utils.Predicate<T>)"""
        val = __PredicateIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Iterator', arg1: 'Predicate'):
        """public void com.badlogic.gdx.utils.Predicate$PredicateIterator.set(java.util.Iterator<T>,com.badlogic.gdx.utils.Predicate<T>)"""
        super(__PredicateIterator, self).set(arg0, arg1)

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.Predicate$PredicateIterator.remove()"""
        super(PredicateIterator, self).remove()

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

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Predicate$PredicateIterator.hasNext()"""
        return bool.__wrap(super(PredicateIterator, self).hasNext())

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
    def next(self) -> object:
        """public T com.badlogic.gdx.utils.Predicate$PredicateIterator.next()"""
        return object.__wrap(super(PredicateIterator, self).next())

    @overload
    def __init__(self, arg0: 'Iterator', arg1: 'Predicate'):
        """public com.badlogic.gdx.utils.Predicate$PredicateIterator(java.util.Iterator<T>,com.badlogic.gdx.utils.Predicate<T>)"""
        val = __PredicateIterator(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: 'Iterable', arg1: 'Predicate'):
        """public void com.badlogic.gdx.utils.Predicate$PredicateIterator.set(java.lang.Iterable<T>,com.badlogic.gdx.utils.Predicate<T>)"""
        super(__PredicateIterator, self).set(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectLongMap$Entries
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap_Entry
__Entry = __ObjectLongMap_Entry.Entry
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap_Entries
__Entries = __ObjectLongMap_Entries.Entries
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.ObjectLongMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectLongMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

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

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectLongMap$Entries<K> com.badlogic.gdx.utils.ObjectLongMap$Entries.iterator()"""
        return 'Entries'.__wrap(super(Entries, self).iterator())

    @override
    @overload
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.ObjectLongMap$Entry<K> com.badlogic.gdx.utils.ObjectLongMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

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
    def __init__(self, arg0: 'ObjectLongMap'):
        """public com.badlogic.gdx.utils.ObjectLongMap$Entries(com.badlogic.gdx.utils.ObjectLongMap<K>)"""
        val = __Entries(arg0)
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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.SortedIntList$Node
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
import com.badlogic.gdx.utils.SortedIntList as __SortedIntList_Node
__Node = __SortedIntList_Node.Node
from builtins import bool
from builtins import int
 
class Node():
    """com.badlogic.gdx.utils.SortedIntList.Node"""
 
    @staticmethod
    def __wrap(java_value: __Node) -> 'Node':
        return Node(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Node):
        """
        Dynamic initializer for Node.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.SortedIntList$Node()"""
        val = __Node()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.SortedIntList$Node()"""
        val = __Node()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.utils.ArrayMap$Entries
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entry
__Entry = __ObjectMap_Entry.Entry
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ArrayMap as __ArrayMap_Entries
__Entries = __ArrayMap_Entries.Entries
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.ArrayMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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
    def reset(self):
        """public void com.badlogic.gdx.utils.ArrayMap$Entries.reset()"""
        super(Entries, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.ObjectMap$Entry<K, V>> com.badlogic.gdx.utils.ArrayMap$Entries.iterator()"""
        return 'Iterator'.__wrap(super(Entries, self).iterator())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

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
    def remove(self):
        """public void com.badlogic.gdx.utils.ArrayMap$Entries.remove()"""
        super(Entries, self).remove()

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
    def __init__(self, arg0: 'ArrayMap'):
        """public com.badlogic.gdx.utils.ArrayMap$Entries(com.badlogic.gdx.utils.ArrayMap<K, V>)"""
        val = __Entries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.ObjectMap$Entry<K, V> com.badlogic.gdx.utils.ArrayMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.BooleanArray
from builtins import str
import com.badlogic.gdx.utils.BooleanArray as __BooleanArray
__BooleanArray = __BooleanArray
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BooleanArray():
    """com.badlogic.gdx.utils.BooleanArray"""
 
    @staticmethod
    def __wrap(java_value: __BooleanArray) -> 'BooleanArray':
        return BooleanArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanArray):
        """
        Dynamic initializer for BooleanArray.
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
        """public java.lang.String com.badlogic.gdx.utils.BooleanArray.toString()"""
        return str.__wrap(super(BooleanArray, self).toString())

    @overload
    def addAll(self, arg0: 'boolean', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.BooleanArray.addAll(boolean[],int,int)"""
        super(__BooleanArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.BooleanArray.hashCode()"""
        return int.__wrap(super(BooleanArray, self).hashCode())

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.BooleanArray.shuffle()"""
        super(BooleanArray, self).shuffle()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__BooleanArray, self).equals(arg0))

    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.BooleanArray.insertRange(int,int)"""
        super(__BooleanArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def add(self, arg0: bool, arg1: bool, arg2: bool):
        """public void com.badlogic.gdx.utils.BooleanArray.add(boolean,boolean,boolean)"""
        super(__BooleanArray, self).add(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.isEmpty()"""
        return bool.__wrap(super(BooleanArray, self).isEmpty())

    @overload
    def first(self) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.first()"""
        return bool.__wrap(super(BooleanArray, self).first())

    @overload
    def add(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.utils.BooleanArray.add(boolean,boolean)"""
        super(__BooleanArray, self).add(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.notEmpty()"""
        return bool.__wrap(super(BooleanArray, self).notEmpty())

    @overload
    def __init__(self, arg0: 'boolean'):
        """public com.badlogic.gdx.utils.BooleanArray(boolean[])"""
        val = __BooleanArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.BooleanArray.removeRange(int,int)"""
        super(__BooleanArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.BooleanArray.toString(java.lang.String)"""
        return str.__wrap(super(__BooleanArray, self).toString(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.utils.BooleanArray.set(int,boolean)"""
        super(__BooleanArray, self).set(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def shrink(self) -> List[bool]:
        """public boolean[] com.badlogic.gdx.utils.BooleanArray.shrink()"""
        return List[bool].__wrap(super(BooleanArray, self).shrink())

    @overload
    def addAll(self, arg0: 'BooleanArray', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.BooleanArray.addAll(com.badlogic.gdx.utils.BooleanArray,int,int)"""
        super(__BooleanArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'BooleanArray'):
        """public com.badlogic.gdx.utils.BooleanArray(com.badlogic.gdx.utils.BooleanArray)"""
        val = __BooleanArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def insert(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.utils.BooleanArray.insert(int,boolean)"""
        super(__BooleanArray, self).insert(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def peek(self) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.peek()"""
        return bool.__wrap(super(BooleanArray, self).peek())

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.BooleanArray(boolean,int)"""
        val = __BooleanArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.get(int)"""
        return bool.__wrap(super(__BooleanArray, self).get(__int.valueOf(arg0)))

    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.BooleanArray.swap(int,int)"""
        super(__BooleanArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setSize(self, arg0: int) -> List[bool]:
        """public boolean[] com.badlogic.gdx.utils.BooleanArray.setSize(int)"""
        return List[bool].__wrap(super(__BooleanArray, self).setSize(__int.valueOf(arg0)))

    @overload
    def add(self, arg0: bool):
        """public void com.badlogic.gdx.utils.BooleanArray.add(boolean)"""
        super(__BooleanArray, self).add(__boolean.valueOf(arg0))

    @overload
    def random(self) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.random()"""
        return bool.__wrap(super(BooleanArray, self).random())

    @overload
    def ensureCapacity(self, arg0: int) -> List[bool]:
        """public boolean[] com.badlogic.gdx.utils.BooleanArray.ensureCapacity(int)"""
        return List[bool].__wrap(super(__BooleanArray, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def removeIndex(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.removeIndex(int)"""
        return bool.__wrap(super(__BooleanArray, self).removeIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.BooleanArray()"""
        val = __BooleanArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.BooleanArray.clear()"""
        super(BooleanArray, self).clear()

    @overload
    def toArray(self) -> List[bool]:
        """public boolean[] com.badlogic.gdx.utils.BooleanArray.toArray()"""
        return List[bool].__wrap(super(BooleanArray, self).toArray())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.BooleanArray.reverse()"""
        super(BooleanArray, self).reverse()

    @staticmethod
    @overload
    def with(*arg0: bool) -> 'BooleanArray':
        """public static com.badlogic.gdx.utils.BooleanArray com.badlogic.gdx.utils.BooleanArray.with(boolean...)"""
        return BooleanArray.__wrap(__BooleanArray.with(arg0))

    @overload
    def addAll(self, arg0: 'BooleanArray'):
        """public void com.badlogic.gdx.utils.BooleanArray.addAll(com.badlogic.gdx.utils.BooleanArray)"""
        super(__BooleanArray, self).addAll(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.BooleanArray(int)"""
        val = __BooleanArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.BooleanArray()"""
        val = __BooleanArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def pop(self) -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.pop()"""
        return bool.__wrap(super(BooleanArray, self).pop())

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.BooleanArray.truncate(int)"""
        super(__BooleanArray, self).truncate(__int.valueOf(arg0))

    @overload
    def add(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.utils.BooleanArray.add(boolean,boolean,boolean,boolean)"""
        super(__BooleanArray, self).add(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def addAll(self, *arg0: bool):
        """public void com.badlogic.gdx.utils.BooleanArray.addAll(boolean...)"""
        super(__BooleanArray, self).addAll(arg0)

    @overload
    def removeAll(self, arg0: 'BooleanArray') -> bool:
        """public boolean com.badlogic.gdx.utils.BooleanArray.removeAll(com.badlogic.gdx.utils.BooleanArray)"""
        return bool.__wrap(super(__BooleanArray, self).removeAll(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: bool, arg1: 'boolean', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.BooleanArray(boolean,boolean[],int,int)"""
        val = __BooleanArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.ReflectionPool
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
import com.badlogic.gdx.utils.ReflectionPool as __ReflectionPool
__ReflectionPool = __ReflectionPool
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ReflectionPool():
    """com.badlogic.gdx.utils.ReflectionPool"""
 
    @staticmethod
    def __wrap(java_value: __ReflectionPool) -> 'ReflectionPool':
        return ReflectionPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectionPool):
        """
        Dynamic initializer for ReflectionPool.
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
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(Pool, self).clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Class', arg1: int):
        """public com.badlogic.gdx.utils.ReflectionPool(java.lang.Class<T>,int)"""
        val = __ReflectionPool(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.Pool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__Pool, self).freeAll(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def free(self, arg0: object):
        """public void com.badlogic.gdx.utils.Pool.free(T)"""
        super(__Pool, self).free(arg0)

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
    def __init__(self, arg0: 'Class', arg1: int, arg2: int):
        """public com.badlogic.gdx.utils.ReflectionPool(java.lang.Class<T>,int,int)"""
        val = __ReflectionPool(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def obtain(self) -> object:
        """public T com.badlogic.gdx.utils.Pool.obtain()"""
        return object.__wrap(super(Pool, self).obtain())

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int.__wrap(super(Pool, self).getFree())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(__Pool, self).fill(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Class'):
        """public com.badlogic.gdx.utils.ReflectionPool(java.lang.Class<T>)"""
        val = __ReflectionPool(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntMap$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.utils.IntMap as __IntMap_Keys
__Keys = __IntMap_Keys.Keys
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.IntArray as __IntArray
__IntArray = __IntArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Keys():
    """com.badlogic.gdx.utils.IntMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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
    def toArray(self) -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntMap$Keys.toArray()"""
        return 'IntArray'.__wrap(super(Keys, self).toArray())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'IntMap'):
        """public com.badlogic.gdx.utils.IntMap$Keys(com.badlogic.gdx.utils.IntMap)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArray(self, arg0: 'IntArray') -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntMap$Keys.toArray(com.badlogic.gdx.utils.IntArray)"""
        return 'IntArray'.__wrap(super(__Keys, self).toArray(arg0))

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
    def next(self) -> int:
        """public int com.badlogic.gdx.utils.IntMap$Keys.next()"""
        return int.__wrap(super(Keys, self).next())

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
 
 
# CLASS: com.badlogic.gdx.utils.IntIntMap$Values
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap_Values
__Values = __IntIntMap_Values.Values
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.IntArray as __IntArray
__IntArray = __IntArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Values():
    """com.badlogic.gdx.utils.IntIntMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntIntMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def iterator(self) -> 'Values':
        """public com.badlogic.gdx.utils.IntIntMap$Values com.badlogic.gdx.utils.IntIntMap$Values.iterator()"""
        return 'Values'.__wrap(super(Values, self).iterator())

    @overload
    def toArray(self, arg0: 'IntArray') -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntIntMap$Values.toArray(com.badlogic.gdx.utils.IntArray)"""
        return 'IntArray'.__wrap(super(__Values, self).toArray(arg0))

    @overload
    def toArray(self) -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntIntMap$Values.toArray()"""
        return 'IntArray'.__wrap(super(Values, self).toArray())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def next(self) -> int:
        """public int com.badlogic.gdx.utils.IntIntMap$Values.next()"""
        return int.__wrap(super(Values, self).next())

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
    def __init__(self, arg0: 'IntIntMap'):
        """public com.badlogic.gdx.utils.IntIntMap$Values(com.badlogic.gdx.utils.IntIntMap)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.ArrayMap
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.utils.ArrayMap as __ArrayMap_Keys
__Keys = __ArrayMap_Keys.Keys
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ArrayMap as __ArrayMap_Entries
__Entries = __ArrayMap_Entries.Entries
import com.badlogic.gdx.utils.ArrayMap as __ArrayMap
__ArrayMap = __ArrayMap
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.ArrayMap as __ArrayMap_Values
__Values = __ArrayMap_Values.Values
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ArrayMap():
    """com.badlogic.gdx.utils.ArrayMap"""
 
    @staticmethod
    def __wrap(java_value: __ArrayMap) -> 'ArrayMap':
        return ArrayMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayMap):
        """
        Dynamic initializer for ArrayMap.
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
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__ArrayMap, self).equalsIdentity(arg0))

    @overload
    def removeIndex(self, arg0: int):
        """public void com.badlogic.gdx.utils.ArrayMap.removeIndex(int)"""
        super(__ArrayMap, self).removeIndex(__int.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ArrayMap()"""
        val = __ArrayMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putAll(self, arg0: 'ArrayMap', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ArrayMap.putAll(com.badlogic.gdx.utils.ArrayMap<? extends K, ? extends V>,int,int)"""
        super(__ArrayMap, self).putAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def putAll(self, arg0: 'ArrayMap'):
        """public void com.badlogic.gdx.utils.ArrayMap.putAll(com.badlogic.gdx.utils.ArrayMap<? extends K, ? extends V>)"""
        super(__ArrayMap, self).putAll(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.ObjectMap$Entry<K, V>> com.badlogic.gdx.utils.ArrayMap.iterator()"""
        return 'Iterator'.__wrap(super(ArrayMap, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def containsValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap.containsValue(V,boolean)"""
        return bool.__wrap(super(__ArrayMap, self).containsValue(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.ArrayMap.truncate(int)"""
        super(__ArrayMap, self).truncate(__int.valueOf(arg0))

    @overload
    def indexOfKey(self, arg0: object) -> int:
        """public int com.badlogic.gdx.utils.ArrayMap.indexOfKey(K)"""
        return int.__wrap(super(__ArrayMap, self).indexOfKey(arg0))

    @overload
    def removeValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap.removeValue(V,boolean)"""
        return bool.__wrap(super(__ArrayMap, self).removeValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ArrayMap()"""
        val = __ArrayMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ArrayMap.toString()"""
        return str.__wrap(super(ArrayMap, self).toString())

    @overload
    def getValueAt(self, arg0: int) -> object:
        """public V com.badlogic.gdx.utils.ArrayMap.getValueAt(int)"""
        return object.__wrap(super(__ArrayMap, self).getValueAt(__int.valueOf(arg0)))

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ArrayMap$Entries<K, V> com.badlogic.gdx.utils.ArrayMap.entries()"""
        return 'Entries'.__wrap(super(ArrayMap, self).entries())

    @overload
    def setValue(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.ArrayMap.setValue(int,V)"""
        super(__ArrayMap, self).setValue(__int.valueOf(arg0), arg1)

    @overload
    def shrink(self):
        """public void com.badlogic.gdx.utils.ArrayMap.shrink()"""
        super(ArrayMap, self).shrink()

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.ArrayMap.clear(int)"""
        super(__ArrayMap, self).clear(__int.valueOf(arg0))

    @overload
    def setKey(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.ArrayMap.setKey(int,K)"""
        super(__ArrayMap, self).setKey(__int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ArrayMap.clear()"""
        super(ArrayMap, self).clear()

    @overload
    def insert(self, arg0: int, arg1: object, arg2: object):
        """public void com.badlogic.gdx.utils.ArrayMap.insert(int,K,V)"""
        super(__ArrayMap, self).insert(__int.valueOf(arg0), arg1, arg2)

    @overload
    def indexOfValue(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.ArrayMap.indexOfValue(V,boolean)"""
        return int.__wrap(super(__ArrayMap, self).indexOfValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ArrayMap'):
        """public com.badlogic.gdx.utils.ArrayMap(com.badlogic.gdx.utils.ArrayMap)"""
        val = __ArrayMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__ArrayMap, self).equals(arg0))

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ArrayMap$Keys<K> com.badlogic.gdx.utils.ArrayMap.keys()"""
        return 'Keys'.__wrap(super(ArrayMap, self).keys())

    @overload
    def getKey(self, arg0: object, arg1: bool) -> object:
        """public K com.badlogic.gdx.utils.ArrayMap.getKey(V,boolean)"""
        return object.__wrap(super(__ArrayMap, self).getKey(arg0, __boolean.valueOf(arg1)))

    @overload
    def firstKey(self) -> object:
        """public K com.badlogic.gdx.utils.ArrayMap.firstKey()"""
        return object.__wrap(super(ArrayMap, self).firstKey())

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.ArrayMap.reverse()"""
        super(ArrayMap, self).reverse()

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.ArrayMap.shuffle()"""
        super(ArrayMap, self).shuffle()

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V com.badlogic.gdx.utils.ArrayMap.get(K,V)"""
        return object.__wrap(super(__ArrayMap, self).get(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.ArrayMap.put(K,V,int)"""
        return int.__wrap(super(__ArrayMap, self).put(arg0, arg1, __int.valueOf(arg2)))

    @overload
    def getKeyAt(self, arg0: int) -> object:
        """public K com.badlogic.gdx.utils.ArrayMap.getKeyAt(int)"""
        return object.__wrap(super(__ArrayMap, self).getKeyAt(__int.valueOf(arg0)))

    @overload
    def peekKey(self) -> object:
        """public K com.badlogic.gdx.utils.ArrayMap.peekKey()"""
        return object.__wrap(super(ArrayMap, self).peekKey())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ArrayMap.hashCode()"""
        return int.__wrap(super(ArrayMap, self).hashCode())

    @overload
    def peekValue(self) -> object:
        """public V com.badlogic.gdx.utils.ArrayMap.peekValue()"""
        return object.__wrap(super(ArrayMap, self).peekValue())

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'Class', arg3: 'Class'):
        """public com.badlogic.gdx.utils.ArrayMap(boolean,int,java.lang.Class,java.lang.Class)"""
        val = __ArrayMap(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: object) -> object:
        """public V com.badlogic.gdx.utils.ArrayMap.get(K)"""
        return object.__wrap(super(__ArrayMap, self).get(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.ArrayMap(boolean,int)"""
        val = __ArrayMap(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ArrayMap.ensureCapacity(int)"""
        super(__ArrayMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Class', arg1: 'Class'):
        """public com.badlogic.gdx.utils.ArrayMap(java.lang.Class,java.lang.Class)"""
        val = __ArrayMap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap.isEmpty()"""
        return bool.__wrap(super(ArrayMap, self).isEmpty())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.ArrayMap(int)"""
        val = __ArrayMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap.notEmpty()"""
        return bool.__wrap(super(ArrayMap, self).notEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> int:
        """public int com.badlogic.gdx.utils.ArrayMap.put(K,V)"""
        return int.__wrap(super(__ArrayMap, self).put(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.ArrayMap$Values<V> com.badlogic.gdx.utils.ArrayMap.values()"""
        return 'Values'.__wrap(super(ArrayMap, self).values())

    @overload
    def removeKey(self, arg0: object) -> object:
        """public V com.badlogic.gdx.utils.ArrayMap.removeKey(K)"""
        return object.__wrap(super(__ArrayMap, self).removeKey(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap.containsKey(K)"""
        return bool.__wrap(super(__ArrayMap, self).containsKey(arg0))

    @overload
    def firstValue(self) -> object:
        """public V com.badlogic.gdx.utils.ArrayMap.firstValue()"""
        return object.__wrap(super(ArrayMap, self).firstValue()) 
 
 
# CLASS: com.badlogic.gdx.utils.Queue$QueueIterator
import com.badlogic.gdx.utils.Queue as __Queue_QueueIterator
__QueueIterator = __Queue_QueueIterator.QueueIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class QueueIterator():
    """com.badlogic.gdx.utils.Queue.QueueIterator"""
 
    @staticmethod
    def __wrap(java_value: __QueueIterator) -> 'QueueIterator':
        return QueueIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QueueIterator):
        """
        Dynamic initializer for QueueIterator.
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

    @override
    @overload
    def next(self) -> object:
        """public T com.badlogic.gdx.utils.Queue$QueueIterator.next()"""
        return object.__wrap(super(QueueIterator, self).next())

    @overload
    def reset(self):
        """public void com.badlogic.gdx.utils.Queue$QueueIterator.reset()"""
        super(QueueIterator, self).reset()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.gdx.utils.Queue$QueueIterator.iterator()"""
        return 'Iterator'.__wrap(super(QueueIterator, self).iterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Queue', arg1: bool):
        """public com.badlogic.gdx.utils.Queue$QueueIterator(com.badlogic.gdx.utils.Queue<T>,boolean)"""
        val = __QueueIterator(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Queue'):
        """public com.badlogic.gdx.utils.Queue$QueueIterator(com.badlogic.gdx.utils.Queue<T>)"""
        val = __QueueIterator(arg0)
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
    def remove(self):
        """public void com.badlogic.gdx.utils.Queue$QueueIterator.remove()"""
        super(QueueIterator, self).remove()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Queue$QueueIterator.hasNext()"""
        return bool.__wrap(super(QueueIterator, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.GdxRuntimeException
import com.badlogic.gdx.utils.GdxRuntimeException as __GdxRuntimeException
__GdxRuntimeException = __GdxRuntimeException
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
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GdxRuntimeException():
    """com.badlogic.gdx.utils.GdxRuntimeException"""
 
    @staticmethod
    def __wrap(java_value: __GdxRuntimeException) -> 'GdxRuntimeException':
        return GdxRuntimeException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GdxRuntimeException):
        """
        Dynamic initializer for GdxRuntimeException.
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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.utils.GdxRuntimeException(java.lang.String,java.lang.Throwable)"""
        val = __GdxRuntimeException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.GdxRuntimeException(java.lang.String)"""
        val = __GdxRuntimeException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.utils.GdxRuntimeException(java.lang.Throwable)"""
        val = __GdxRuntimeException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.utils.DelayedRemovalArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.utils.Array as __Array_ArrayIterator
__ArrayIterator = __Array_ArrayIterator.ArrayIterator
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.Comparator as Comparator
import com.badlogic.gdx.utils.DelayedRemovalArray as __DelayedRemovalArray
__DelayedRemovalArray = __DelayedRemovalArray
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class DelayedRemovalArray():
    """com.badlogic.gdx.utils.DelayedRemovalArray"""
 
    @staticmethod
    def __wrap(java_value: __DelayedRemovalArray) -> 'DelayedRemovalArray':
        return DelayedRemovalArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DelayedRemovalArray):
        """
        Dynamic initializer for DelayedRemovalArray.
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
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString(java.lang.String)"""
        return str.__wrap(super(__Array, self).toString(arg0))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.begin()"""
        super(DelayedRemovalArray, self).begin()

    @overload
    def removeAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.removeAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__Array, self).removeAll(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.removeRange(int,int)"""
        super(__DelayedRemovalArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.DelayedRemovalArray()"""
        val = __DelayedRemovalArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def lastIndexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.lastIndexOf(T,boolean)"""
        return int.__wrap(super(__Array, self).lastIndexOf(arg0, __boolean.valueOf(arg1)))

    @overload
    def contains(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.contains(T,boolean)"""
        return bool.__wrap(super(__Array, self).contains(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def insert(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.insert(int,T)"""
        super(__DelayedRemovalArray, self).insert(__int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: 'Object'):
        """public com.badlogic.gdx.utils.DelayedRemovalArray(T[])"""
        val = __DelayedRemovalArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def of(arg0: 'Class') -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(java.lang.Class<T>)"""
        return Array.__wrap(__Array.of(arg0))

    @override
    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.Array.addAll(com.badlogic.gdx.utils.Array<? extends T>)"""
        super(__Array, self).addAll(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.DelayedRemovalArray()"""
        val = __DelayedRemovalArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString()"""
        return str.__wrap(super(Array, self).toString())

    @staticmethod
    @overload
    def with(*arg0: object) -> 'DelayedRemovalArray':
        """public static <T> com.badlogic.gdx.utils.DelayedRemovalArray<T> com.badlogic.gdx.utils.DelayedRemovalArray.with(T...)"""
        return DelayedRemovalArray.__wrap(__DelayedRemovalArray.with(arg0))

    @override
    @overload
    def add(self, arg0: object, arg1: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T)"""
        super(__Array, self).add(arg0, arg1)

    @override
    @overload
    def addAll(self, arg0: 'Array', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.Array.addAll(com.badlogic.gdx.utils.Array<? extends T>,int,int)"""
        super(__Array, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.Array.hashCode()"""
        return int.__wrap(super(Array, self).hashCode())

    @override
    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.reverse()"""
        super(DelayedRemovalArray, self).reverse()

    @override
    @overload
    def add(self, arg0: object, arg1: object, arg2: object, arg3: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T,T,T)"""
        super(__Array, self).add(arg0, arg1, arg2, arg3)

    @overload
    def selectRankedIndex(self, arg0: 'Comparator', arg1: int) -> int:
        """public int com.badlogic.gdx.utils.Array.selectRankedIndex(java.util.Comparator<T>,int)"""
        return int.__wrap(super(__Array, self).selectRankedIndex(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.utils.Array.first()"""
        return object.__wrap(super(Array, self).first())

    @overload
    def removeValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.DelayedRemovalArray.removeValue(T,boolean)"""
        return bool.__wrap(super(__DelayedRemovalArray, self).removeValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'Class'):
        """public com.badlogic.gdx.utils.DelayedRemovalArray(boolean,int,java.lang.Class)"""
        val = __DelayedRemovalArray(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public <V> V[] com.badlogic.gdx.utils.Array.toArray(java.lang.Class<V>)"""
        return List[object].__wrap(super(__Array, self).toArray(arg0))

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.utils.DelayedRemovalArray(com.badlogic.gdx.utils.Array)"""
        val = __DelayedRemovalArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.sort()"""
        super(DelayedRemovalArray, self).sort()

    @overload
    def removeIndex(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.DelayedRemovalArray.removeIndex(int)"""
        return object.__wrap(super(__DelayedRemovalArray, self).removeIndex(__int.valueOf(arg0)))

    @override
    @overload
    def addAll(self, *arg0: object):
        """public void com.badlogic.gdx.utils.Array.addAll(T...)"""
        super(__Array, self).addAll(arg0)

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.DelayedRemovalArray(int)"""
        val = __DelayedRemovalArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.shuffle()"""
        super(DelayedRemovalArray, self).shuffle()

    @override
    @overload
    def add(self, arg0: object, arg1: object, arg2: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T,T)"""
        super(__Array, self).add(arg0, arg1, arg2)

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Array.get(int)"""
        return object.__wrap(super(__Array, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def selectRanked(self, arg0: 'Comparator', arg1: int) -> object:
        """public T com.badlogic.gdx.utils.Array.selectRanked(java.util.Comparator<T>,int)"""
        return object.__wrap(super(__Array, self).selectRanked(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def end(self):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.end()"""
        super(DelayedRemovalArray, self).end()

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__Array, self).equalsIdentity(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.toArray()"""
        return List[object].__wrap(super(Array, self).toArray())

    @override
    @overload
    def iterator(self) -> 'ArrayIterator':
        """public com.badlogic.gdx.utils.Array$ArrayIterator<T> com.badlogic.gdx.utils.Array.iterator()"""
        return 'ArrayIterator'.__wrap(super(Array, self).iterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.isEmpty()"""
        return bool.__wrap(super(Array, self).isEmpty())

    @override
    @overload
    def set(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.set(int,T)"""
        super(__DelayedRemovalArray, self).set(__int.valueOf(arg0), arg1)

    @overload
    def setSize(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.DelayedRemovalArray.setSize(int)"""
        return List[object].__wrap(super(__DelayedRemovalArray, self).setSize(__int.valueOf(arg0)))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.sort(java.util.Comparator<? super T>)"""
        super(__DelayedRemovalArray, self).sort(arg0)

    @overload
    def containsAny(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAny(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__Array, self).containsAny(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def shrink(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.shrink()"""
        return List[object].__wrap(super(Array, self).shrink())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equals(java.lang.Object)"""
        return bool.__wrap(super(__Array, self).equals(arg0))

    @overload
    def ensureCapacity(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.ensureCapacity(int)"""
        return List[object].__wrap(super(__Array, self).ensureCapacity(__int.valueOf(arg0)))

    @override
    @overload
    def peek(self) -> object:
        """public T com.badlogic.gdx.utils.Array.peek()"""
        return object.__wrap(super(Array, self).peek())

    @staticmethod
    @overload
    def of(arg0: bool, arg1: int, arg2: 'Class') -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(boolean,int,java.lang.Class<T>)"""
        return Array.__wrap(__Array.of(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.DelayedRemovalArray(boolean,int)"""
        val = __DelayedRemovalArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def random(self) -> object:
        """public T com.badlogic.gdx.utils.Array.random()"""
        return object.__wrap(super(Array, self).random())

    @override
    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.utils.Array.add(T)"""
        super(__Array, self).add(arg0)

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.indexOf(T,boolean)"""
        return int.__wrap(super(__Array, self).indexOf(arg0, __boolean.valueOf(arg1)))

    @overload
    def containsAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__Array, self).containsAll(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.swap(int,int)"""
        super(__DelayedRemovalArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.notEmpty()"""
        return bool.__wrap(super(Array, self).notEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: 'Object', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.DelayedRemovalArray(boolean,T[],int,int)"""
        val = __DelayedRemovalArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def pop(self) -> object:
        """public T com.badlogic.gdx.utils.DelayedRemovalArray.pop()"""
        return object.__wrap(super(DelayedRemovalArray, self).pop())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.clear()"""
        super(DelayedRemovalArray, self).clear()

    @override
    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.insertRange(int,int)"""
        super(__DelayedRemovalArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def addAll(self, arg0: 'Object', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.Array.addAll(T[],int,int)"""
        super(__Array, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.DelayedRemovalArray.truncate(int)"""
        super(__DelayedRemovalArray, self).truncate(__int.valueOf(arg0))

    @overload
    def select(self, arg0: 'Predicate') -> 'Iterable':
        """public java.lang.Iterable<T> com.badlogic.gdx.utils.Array.select(com.badlogic.gdx.utils.Predicate<T>)"""
        return 'Iterable'.__wrap(super(__Array, self).select(arg0))

    @staticmethod
    @overload
    def with(*arg0: object) -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.with(T...)"""
        return Array.__wrap(__Array.with(arg0))

    @overload
    def __init__(self, arg0: 'Class'):
        """public com.badlogic.gdx.utils.DelayedRemovalArray(java.lang.Class)"""
        val = __DelayedRemovalArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.PauseableThread
import java.lang.Thread as Thread
import java.lang.Boolean as __boolean
import com.badlogic.gdx.utils.PauseableThread as __PauseableThread
__PauseableThread = __PauseableThread
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.ClassLoader as __ClassLoader
__ClassLoader = __ClassLoader
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import java.lang.Thread.Builder.OfPlatform as OfPlatform
import java.lang.Thread.Builder.OfVirtual as OfVirtual
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.ClassLoader as ClassLoader
from builtins import bool
import java.lang.Thread.State as State
import java.lang.ThreadGroup as __ThreadGroup
__ThreadGroup = __ThreadGroup
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Thread as __Thread_State
__State = __Thread_State.State
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
import java.lang.Thread as __Thread
__Thread = __Thread
import java.lang.Thread as __Thread_UncaughtExceptionHandler
__UncaughtExceptionHandler = __Thread_UncaughtExceptionHandler.UncaughtExceptionHandler
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Thread as __Thread_Builder_OfVirtual
__OfVirtual = __Thread_Builder_OfVirtual.Builder.OfVirtual
import java.lang.Object as __Object
__Object = __Object
import java.lang.ThreadGroup as ThreadGroup
import java.lang.Thread as __Thread_Builder_OfPlatform
__OfPlatform = __Thread_Builder_OfPlatform.Builder.OfPlatform
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class PauseableThread():
    """com.badlogic.gdx.utils.PauseableThread"""
 
    @staticmethod
    def __wrap(java_value: __PauseableThread) -> 'PauseableThread':
        return PauseableThread(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PauseableThread):
        """
        Dynamic initializer for PauseableThread.
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
    def activeCount() -> int:
        """public static int java.lang.Thread.activeCount()"""
        return int.__wrap(__Thread.activeCount())

    @override
    @overload
    def getId(self) -> int:
        """public long java.lang.Thread.getId()"""
        return int.__wrap(super(Thread, self).getId())

    @staticmethod
    @overload
    def interrupted() -> bool:
        """public static boolean java.lang.Thread.interrupted()"""
        return bool.__wrap(__Thread.interrupted())

    @override
    @overload
    def join(self, arg0: int):
        """public final void java.lang.Thread.join(long) throws java.lang.InterruptedException"""
        super(__Thread, self).join(__long.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def onPause(self):
        """public void com.badlogic.gdx.utils.PauseableThread.onPause()"""
        super(PauseableThread, self).onPause()

    @overload
    def onResume(self):
        """public void com.badlogic.gdx.utils.PauseableThread.onResume()"""
        super(PauseableThread, self).onResume()

    @override
    @overload
    def setUncaughtExceptionHandler(self, arg0: 'UncaughtExceptionHandler'):
        """public void java.lang.Thread.setUncaughtExceptionHandler(java.lang.Thread$UncaughtExceptionHandler)"""
        super(__Thread, self).setUncaughtExceptionHandler(arg0)

    @override
    @overload
    def join(self):
        """public final void java.lang.Thread.join() throws java.lang.InterruptedException"""
        super(Thread, self).join()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def dumpStack():
            """public static void java.lang.Thread.dumpStack()"""
            __Thread.dumpStack()

    @staticmethod
    @overload
    def currentThread() -> 'Thread':
        """public static native java.lang.Thread java.lang.Thread.currentThread()"""
        return Thread.__wrap(__Thread.currentThread())

    @staticmethod
    @overload
    def sleep(arg0: 'Duration'):
        """public static void java.lang.Thread.sleep(java.time.Duration) throws java.lang.InterruptedException"""
        __Thread.sleep(arg0)

    @override
    @overload
    def join(self, arg0: int, arg1: int):
        """public final void java.lang.Thread.join(long,int) throws java.lang.InterruptedException"""
        super(__Thread, self).join(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def resume(self):
        """public final void java.lang.Thread.resume()"""
        super(Thread, self).resume()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def setDefaultUncaughtExceptionHandler(arg0: 'UncaughtExceptionHandler'):
        """public static void java.lang.Thread.setDefaultUncaughtExceptionHandler(java.lang.Thread$UncaughtExceptionHandler)"""
        __Thread.setDefaultUncaughtExceptionHandler(arg0)

    @override
    @overload
    def checkAccess(self):
        """public final void java.lang.Thread.checkAccess()"""
        super(Thread, self).checkAccess()

    @override
    @overload
    def threadId(self) -> int:
        """public final long java.lang.Thread.threadId()"""
        return int.__wrap(super(Thread, self).threadId())

        @staticmethod
        @overload
        def yield():
            """public static void java.lang.Thread.yield()"""
            __Thread.yield()

    @override
    @overload
    def getPriority(self) -> int:
        """public final int java.lang.Thread.getPriority()"""
        return int.__wrap(super(Thread, self).getPriority())

    @override
    @overload
    def setPriority(self, arg0: int):
        """public final void java.lang.Thread.setPriority(int)"""
        super(__Thread, self).setPriority(__int.valueOf(arg0))

    @override
    @overload
    def getThreadGroup(self) -> 'ThreadGroup':
        """public final java.lang.ThreadGroup java.lang.Thread.getThreadGroup()"""
        return 'ThreadGroup'.__wrap(super(Thread, self).getThreadGroup())

    @override
    @overload
    def isDaemon(self) -> bool:
        """public final boolean java.lang.Thread.isDaemon()"""
        return bool.__wrap(super(Thread, self).isDaemon())

    @override
    @overload
    def isVirtual(self) -> bool:
        """public final boolean java.lang.Thread.isVirtual()"""
        return bool.__wrap(super(Thread, self).isVirtual())

    @staticmethod
    @overload
    def getAllStackTraces() -> 'Map':
        """public static java.util.Map<java.lang.Thread, java.lang.StackTraceElement[]> java.lang.Thread.getAllStackTraces()"""
        return Map.__wrap(__Thread.getAllStackTraces())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Thread.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Thread, self).getStackTrace())

    @staticmethod
    @overload
    def sleep(arg0: int):
        """public static void java.lang.Thread.sleep(long) throws java.lang.InterruptedException"""
        __Thread.sleep(__long.valueOf(arg0))

        @staticmethod
        @overload
        def onSpinWait():
            """public static void java.lang.Thread.onSpinWait()"""
            __Thread.onSpinWait()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getDefaultUncaughtExceptionHandler() -> 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler':
        """public static java.lang.Thread$UncaughtExceptionHandler java.lang.Thread.getDefaultUncaughtExceptionHandler()"""
        return UncaughtExceptionHandler.Thread$UncaughtExceptionHandler.__wrap(__Thread.getDefaultUncaughtExceptionHandler())

    @staticmethod
    @overload
    def ofPlatform() -> 'OfPlatform.Thread$Builder$OfPlatform':
        """public static java.lang.Thread$Builder$OfPlatform java.lang.Thread.ofPlatform()"""
        return OfPlatform.Thread$Builder$OfPlatform.__wrap(__Thread.ofPlatform())

    @override
    @overload
    def start(self):
        """public void java.lang.Thread.start()"""
        super(Thread, self).start()

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String java.lang.Thread.getName()"""
        return str.__wrap(super(Thread, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setContextClassLoader(self, arg0: 'ClassLoader'):
        """public void java.lang.Thread.setContextClassLoader(java.lang.ClassLoader)"""
        super(__Thread, self).setContextClassLoader(arg0)

    @override
    @overload
    def suspend(self):
        """public final void java.lang.Thread.suspend()"""
        super(Thread, self).suspend()

    @override
    @overload
    def setName(self, arg0: str):
        """public final synchronized void java.lang.Thread.setName(java.lang.String)"""
        super(__Thread, self).setName(arg0)

    @staticmethod
    @overload
    def enumerate(arg0: 'Thread') -> int:
        """public static int java.lang.Thread.enumerate(java.lang.Thread[])"""
        return int.__wrap(__Thread.enumerate(arg0))

    @overload
    def stopThread(self):
        """public void com.badlogic.gdx.utils.PauseableThread.stopThread()"""
        super(PauseableThread, self).stopThread()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Thread.toString()"""
        return str.__wrap(super(Thread, self).toString())

    @override
    @overload
    def interrupt(self):
        """public void java.lang.Thread.interrupt()"""
        super(Thread, self).interrupt()

    @override
    @overload
    def stop(self):
        """public final void java.lang.Thread.stop()"""
        super(Thread, self).stop()

    @override
    @overload
    def countStackFrames(self) -> int:
        """public int java.lang.Thread.countStackFrames()"""
        return int.__wrap(super(Thread, self).countStackFrames())

    @overload
    def join(self, arg0: 'Duration') -> bool:
        """public final boolean java.lang.Thread.join(java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Thread, self).join(arg0))

    @staticmethod
    @overload
    def startVirtualThread(arg0: 'Runnable') -> 'Thread':
        """public static java.lang.Thread java.lang.Thread.startVirtualThread(java.lang.Runnable)"""
        return Thread.__wrap(__Thread.startVirtualThread(arg0))

    @overload
    def isPaused(self) -> bool:
        """public boolean com.badlogic.gdx.utils.PauseableThread.isPaused()"""
        return bool.__wrap(super(PauseableThread, self).isPaused())

    @staticmethod
    @overload
    def holdsLock(arg0: object) -> bool:
        """public static native boolean java.lang.Thread.holdsLock(java.lang.Object)"""
        return bool.__wrap(__Thread.holdsLock(arg0))

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
    def setDaemon(self, arg0: bool):
        """public final void java.lang.Thread.setDaemon(boolean)"""
        super(__Thread, self).setDaemon(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Runnable'):
        """public com.badlogic.gdx.utils.PauseableThread(java.lang.Runnable)"""
        val = __PauseableThread(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def sleep(arg0: int, arg1: int):
        """public static void java.lang.Thread.sleep(long,int) throws java.lang.InterruptedException"""
        __Thread.sleep(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isInterrupted(self) -> bool:
        """public boolean java.lang.Thread.isInterrupted()"""
        return bool.__wrap(super(Thread, self).isInterrupted())

    @override
    @overload
    def isAlive(self) -> bool:
        """public final boolean java.lang.Thread.isAlive()"""
        return bool.__wrap(super(Thread, self).isAlive())

    @override
    @overload
    def getUncaughtExceptionHandler(self) -> 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler':
        """public java.lang.Thread$UncaughtExceptionHandler java.lang.Thread.getUncaughtExceptionHandler()"""
        return 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler'.__wrap(super(Thread, self).getUncaughtExceptionHandler())

    @staticmethod
    @overload
    def ofVirtual() -> 'OfVirtual.Thread$Builder$OfVirtual':
        """public static java.lang.Thread$Builder$OfVirtual java.lang.Thread.ofVirtual()"""
        return OfVirtual.Thread$Builder$OfVirtual.__wrap(__Thread.ofVirtual())

    @override
    @overload
    def getState(self) -> 'State.Thread$State':
        """public java.lang.Thread$State java.lang.Thread.getState()"""
        return 'State.Thread$State'.__wrap(super(Thread, self).getState())

    @override
    @overload
    def getContextClassLoader(self) -> 'ClassLoader':
        """public java.lang.ClassLoader java.lang.Thread.getContextClassLoader()"""
        return 'ClassLoader'.__wrap(super(Thread, self).getContextClassLoader())

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.utils.PauseableThread.run()"""
        super(PauseableThread, self).run() 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectIntMap$Entries
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap_Entry
__Entry = __ObjectIntMap_Entry.Entry
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap_Entries
__Entries = __ObjectIntMap_Entries.Entries
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.ObjectIntMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectIntMap$Entries<K> com.badlogic.gdx.utils.ObjectIntMap$Entries.iterator()"""
        return 'Entries'.__wrap(super(Entries, self).iterator())

    @override
    @overload
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.ObjectIntMap$Entry<K> com.badlogic.gdx.utils.ObjectIntMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

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
    def __init__(self, arg0: 'ObjectIntMap'):
        """public com.badlogic.gdx.utils.ObjectIntMap$Entries(com.badlogic.gdx.utils.ObjectIntMap<K>)"""
        val = __Entries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectIntMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectMap$Entry
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
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entry
__Entry = __ObjectMap_Entry.Entry
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Entry():
    """com.badlogic.gdx.utils.ObjectMap.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectMap$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

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
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.XmlWriter
import com.badlogic.gdx.utils.XmlWriter as __XmlWriter
__XmlWriter = __XmlWriter
from builtins import str
import java.lang.Character as __char
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class XmlWriter():
    """com.badlogic.gdx.utils.XmlWriter"""
 
    @staticmethod
    def __wrap(java_value: __XmlWriter) -> 'XmlWriter':
        return XmlWriter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __XmlWriter):
        """
        Dynamic initializer for XmlWriter.
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
    def flush(self):
        """public void com.badlogic.gdx.utils.XmlWriter.flush() throws java.io.IOException"""
        super(XmlWriter, self).flush()

    @override
    @overload
    def write(self, arg0: int):
        """public void java.io.Writer.write(int) throws java.io.IOException"""
        super(__Writer, self).write(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Writer'):
        """public com.badlogic.gdx.utils.XmlWriter(java.io.Writer)"""
        val = __XmlWriter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public void com.badlogic.gdx.utils.XmlWriter.close() throws java.io.IOException"""
        super(XmlWriter, self).close()

    @overload
    def text(self, arg0: object) -> 'XmlWriter':
        """public com.badlogic.gdx.utils.XmlWriter com.badlogic.gdx.utils.XmlWriter.text(java.lang.Object) throws java.io.IOException"""
        return 'XmlWriter'.__wrap(super(__XmlWriter, self).text(arg0))

    @override
    @overload
    def write(self, arg0: 'char'):
        """public void java.io.Writer.write(char[]) throws java.io.IOException"""
        super(__Writer, self).write(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def attribute(self, arg0: str, arg1: object) -> 'XmlWriter':
        """public com.badlogic.gdx.utils.XmlWriter com.badlogic.gdx.utils.XmlWriter.attribute(java.lang.String,java.lang.Object) throws java.io.IOException"""
        return 'XmlWriter'.__wrap(super(__XmlWriter, self).attribute(arg0, arg1))

    @staticmethod
    @overload
    def nullWriter() -> 'Writer':
        """public static java.io.Writer java.io.Writer.nullWriter()"""
        return Writer.__wrap(__Writer.nullWriter())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def pop(self) -> 'XmlWriter':
        """public com.badlogic.gdx.utils.XmlWriter com.badlogic.gdx.utils.XmlWriter.pop() throws java.io.IOException"""
        return 'XmlWriter'.__wrap(super(XmlWriter, self).pop())

    @override
    @overload
    def write(self, arg0: str):
        """public void java.io.Writer.write(java.lang.String) throws java.io.IOException"""
        super(__Writer, self).write(arg0)

    @overload
    def append(self, arg0: str) -> 'Writer':
        """public java.io.Writer java.io.Writer.append(char) throws java.io.IOException"""
        return 'Writer'.__wrap(super(__Writer, self).append(__char.valueOf(arg0)))

    @override
    @overload
    def write(self, arg0: 'char', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.XmlWriter.write(char[],int,int) throws java.io.IOException"""
        super(__XmlWriter, self).write(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def append(self, arg0: 'CharSequence') -> 'Writer':
        """public java.io.Writer java.io.Writer.append(java.lang.CharSequence) throws java.io.IOException"""
        return 'Writer'.__wrap(super(__Writer, self).append(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: str, arg1: int, arg2: int):
        """public void java.io.Writer.write(java.lang.String,int,int) throws java.io.IOException"""
        super(__Writer, self).write(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def append(self, arg0: 'CharSequence', arg1: int, arg2: int) -> 'Writer':
        """public java.io.Writer java.io.Writer.append(java.lang.CharSequence,int,int) throws java.io.IOException"""
        return 'Writer'.__wrap(super(__Writer, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def element(self, arg0: str) -> 'XmlWriter':
        """public com.badlogic.gdx.utils.XmlWriter com.badlogic.gdx.utils.XmlWriter.element(java.lang.String) throws java.io.IOException"""
        return 'XmlWriter'.__wrap(super(__XmlWriter, self).element(arg0))

    @overload
    def element(self, arg0: str, arg1: object) -> 'XmlWriter':
        """public com.badlogic.gdx.utils.XmlWriter com.badlogic.gdx.utils.XmlWriter.element(java.lang.String,java.lang.Object) throws java.io.IOException"""
        return 'XmlWriter'.__wrap(super(__XmlWriter, self).element(arg0, arg1)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectIntMap$Values
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap_Values
__Values = __ObjectIntMap_Values.Values
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
import com.badlogic.gdx.utils.IntArray as __IntArray
__IntArray = __IntArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Values():
    """com.badlogic.gdx.utils.ObjectIntMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def next(self) -> int:
        """public int com.badlogic.gdx.utils.ObjectIntMap$Values.next()"""
        return int.__wrap(super(Values, self).next())

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

    @overload
    def iterator(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectIntMap$Values com.badlogic.gdx.utils.ObjectIntMap$Values.iterator()"""
        return 'Values'.__wrap(super(Values, self).iterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toArray(self) -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.ObjectIntMap$Values.toArray()"""
        return 'IntArray'.__wrap(super(Values, self).toArray())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectIntMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

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

    @overload
    def toArray(self, arg0: 'IntArray') -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.ObjectIntMap$Values.toArray(com.badlogic.gdx.utils.IntArray)"""
        return 'IntArray'.__wrap(super(__Values, self).toArray(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ObjectIntMap'):
        """public com.badlogic.gdx.utils.ObjectIntMap$Values(com.badlogic.gdx.utils.ObjectIntMap<?>)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ArrayMap$Values
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import com.badlogic.gdx.utils.ArrayMap as __ArrayMap_Values
__Values = __ArrayMap_Values.Values
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Values():
    """com.badlogic.gdx.utils.ArrayMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def reset(self):
        """public void com.badlogic.gdx.utils.ArrayMap$Values.reset()"""
        super(Values, self).reset()

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
    def __init__(self, arg0: 'ArrayMap'):
        """public com.badlogic.gdx.utils.ArrayMap$Values(com.badlogic.gdx.utils.ArrayMap<java.lang.Object, V>)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<V> com.badlogic.gdx.utils.ArrayMap$Values.toArray()"""
        return 'Array'.__wrap(super(Values, self).toArray())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<V> com.badlogic.gdx.utils.ArrayMap$Values.iterator()"""
        return 'Iterator'.__wrap(super(Values, self).iterator())

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.ArrayMap$Values.remove()"""
        super(Values, self).remove()

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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ArrayMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public V com.badlogic.gdx.utils.ArrayMap$Values.next()"""
        return object.__wrap(super(Values, self).next())

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<V> com.badlogic.gdx.utils.ArrayMap$Values.toArray(com.badlogic.gdx.utils.Array)"""
        return 'Array'.__wrap(super(__Values, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Array$ArrayIterable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.Array as __Array_ArrayIterator
__ArrayIterator = __Array_ArrayIterator.ArrayIterator
import com.badlogic.gdx.utils.Array as __Array_ArrayIterable
__ArrayIterable = __Array_ArrayIterable.ArrayIterable
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ArrayIterable():
    """com.badlogic.gdx.utils.Array.ArrayIterable"""
 
    @staticmethod
    def __wrap(java_value: __ArrayIterable) -> 'ArrayIterable':
        return ArrayIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayIterable):
        """
        Dynamic initializer for ArrayIterable.
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

    @override
    @overload
    def iterator(self) -> 'ArrayIterator':
        """public com.badlogic.gdx.utils.Array$ArrayIterator<T> com.badlogic.gdx.utils.Array$ArrayIterable.iterator()"""
        return 'ArrayIterator'.__wrap(super(ArrayIterable, self).iterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Array', arg1: bool):
        """public com.badlogic.gdx.utils.Array$ArrayIterable(com.badlogic.gdx.utils.Array<T>,boolean)"""
        val = __ArrayIterable(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.utils.Array$ArrayIterable(com.badlogic.gdx.utils.Array<T>)"""
        val = __ArrayIterable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Clipboard
import com.badlogic.gdx.utils.Clipboard as __Clipboard
__Clipboard = __Clipboard
from abc import abstractmethod, ABC
 
class Clipboard(ABC):
    """com.badlogic.gdx.utils.Clipboard"""
 
    @staticmethod
    def __wrap(java_value: __Clipboard) -> 'Clipboard':
        return Clipboard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Clipboard):
        """
        Dynamic initializer for Clipboard.
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
    def hasContents(self, ):
        """public abstract boolean com.badlogic.gdx.utils.Clipboard.hasContents()"""
        pass

    @abstractmethod
    def getContents(self, ):
        """public abstract java.lang.String com.badlogic.gdx.utils.Clipboard.getContents()"""
        pass

    @abstractmethod
    def setContents(self, arg0: str):
        """public abstract void com.badlogic.gdx.utils.Clipboard.setContents(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.utils.LongMap$Values
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.LongMap as __LongMap_Values
__Values = __LongMap_Values.Values
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Values():
    """com.badlogic.gdx.utils.LongMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<V> com.badlogic.gdx.utils.LongMap$Values.iterator()"""
        return 'Iterator'.__wrap(super(Values, self).iterator())

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

    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<V> com.badlogic.gdx.utils.LongMap$Values.toArray()"""
        return 'Array'.__wrap(super(Values, self).toArray())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def next(self) -> object:
        """public V com.badlogic.gdx.utils.LongMap$Values.next()"""
        return object.__wrap(super(Values, self).next())

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
    def __init__(self, arg0: 'LongMap'):
        """public com.badlogic.gdx.utils.LongMap$Values(com.badlogic.gdx.utils.LongMap<V>)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Timer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.Timer as __Timer_Task
__Task = __Timer_Task.Task
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.Timer as __Timer
__Timer = __Timer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Timer():
    """com.badlogic.gdx.utils.Timer"""
 
    @staticmethod
    def __wrap(java_value: __Timer) -> 'Timer':
        return Timer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Timer):
        """
        Dynamic initializer for Timer.
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
    def clear(self):
        """public synchronized void com.badlogic.gdx.utils.Timer.clear()"""
        super(Timer, self).clear()

    @staticmethod
    @overload
    def schedule(arg0: 'Task', arg1: float) -> 'Task':
        """public static com.badlogic.gdx.utils.Timer$Task com.badlogic.gdx.utils.Timer.schedule(com.badlogic.gdx.utils.Timer$Task,float)"""
        return Task.__wrap(__Timer.schedule(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def start(self):
        """public void com.badlogic.gdx.utils.Timer.start()"""
        super(Timer, self).start()

    @overload
    def stop(self):
        """public void com.badlogic.gdx.utils.Timer.stop()"""
        super(Timer, self).stop()

    @overload
    def scheduleTask(self, arg0: 'Task', arg1: float, arg2: float) -> 'Task':
        """public com.badlogic.gdx.utils.Timer$Task com.badlogic.gdx.utils.Timer.scheduleTask(com.badlogic.gdx.utils.Timer$Task,float,float)"""
        return 'Task'.__wrap(super(__Timer, self).scheduleTask(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def schedule(arg0: 'Task', arg1: float, arg2: float, arg3: int) -> 'Task':
        """public static com.badlogic.gdx.utils.Timer$Task com.badlogic.gdx.utils.Timer.schedule(com.badlogic.gdx.utils.Timer$Task,float,float,int)"""
        return Task.__wrap(__Timer.schedule(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @overload
    def scheduleTask(self, arg0: 'Task', arg1: float, arg2: float, arg3: int) -> 'Task':
        """public com.badlogic.gdx.utils.Timer$Task com.badlogic.gdx.utils.Timer.scheduleTask(com.badlogic.gdx.utils.Timer$Task,float,float,int)"""
        return 'Task'.__wrap(super(__Timer, self).scheduleTask(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def post(arg0: 'Task') -> 'Task':
        """public static com.badlogic.gdx.utils.Timer$Task com.badlogic.gdx.utils.Timer.post(com.badlogic.gdx.utils.Timer$Task)"""
        return Task.__wrap(__Timer.post(arg0))

    @overload
    def scheduleTask(self, arg0: 'Task', arg1: float) -> 'Task':
        """public com.badlogic.gdx.utils.Timer$Task com.badlogic.gdx.utils.Timer.scheduleTask(com.badlogic.gdx.utils.Timer$Task,float)"""
        return 'Task'.__wrap(super(__Timer, self).scheduleTask(arg0, __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isEmpty(self) -> bool:
        """public synchronized boolean com.badlogic.gdx.utils.Timer.isEmpty()"""
        return bool.__wrap(super(Timer, self).isEmpty())

    @staticmethod
    @overload
    def instance() -> 'Timer':
        """public static com.badlogic.gdx.utils.Timer com.badlogic.gdx.utils.Timer.instance()"""
        return Timer.__wrap(__Timer.instance())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Timer()"""
        val = __Timer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def postTask(self, arg0: 'Task') -> 'Task':
        """public com.badlogic.gdx.utils.Timer$Task com.badlogic.gdx.utils.Timer.postTask(com.badlogic.gdx.utils.Timer$Task)"""
        return 'Task'.__wrap(super(__Timer, self).postTask(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Timer()"""
        val = __Timer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def delay(self, arg0: int):
        """public synchronized void com.badlogic.gdx.utils.Timer.delay(long)"""
        super(__Timer, self).delay(__long.valueOf(arg0))

    @staticmethod
    @overload
    def schedule(arg0: 'Task', arg1: float, arg2: float) -> 'Task':
        """public static com.badlogic.gdx.utils.Timer$Task com.badlogic.gdx.utils.Timer.schedule(com.badlogic.gdx.utils.Timer$Task,float,float)"""
        return Task.__wrap(__Timer.schedule(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.utils.BinaryHeap$Node
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.utils.BinaryHeap as __BinaryHeap_Node
__Node = __BinaryHeap_Node.Node
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Node():
    """com.badlogic.gdx.utils.BinaryHeap.Node"""
 
    @staticmethod
    def __wrap(java_value: __Node) -> 'Node':
        return Node(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Node):
        """
        Dynamic initializer for Node.
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

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.utils.BinaryHeap$Node(float)"""
        val = __Node(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.BinaryHeap$Node.toString()"""
        return str.__wrap(super(Node, self).toString())

    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.utils.BinaryHeap$Node.getValue()"""
        return float.__wrap(super(Node, self).getValue())

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
 
 
# CLASS: com.badlogic.gdx.utils.Collections
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
import com.badlogic.gdx.utils.Collections as __Collections
__Collections = __Collections
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Collections():
    """com.badlogic.gdx.utils.Collections"""
 
    @staticmethod
    def __wrap(java_value: __Collections) -> 'Collections':
        return Collections(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Collections):
        """
        Dynamic initializer for Collections.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Collections()"""
        val = __Collections()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Collections()"""
        val = __Collections()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.utils.JsonReader
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.utils.JsonReader as __JsonReader
__JsonReader = __JsonReader
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.JsonValue as __JsonValue
__JsonValue = __JsonValue
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class JsonReader():
    """com.badlogic.gdx.utils.JsonReader"""
 
    @staticmethod
    def __wrap(java_value: __JsonReader) -> 'JsonReader':
        return JsonReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonReader):
        """
        Dynamic initializer for JsonReader.
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
    def parse(self, arg0: 'FileHandle') -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonReader.parse(com.badlogic.gdx.files.FileHandle)"""
        return 'JsonValue'.__wrap(super(__JsonReader, self).parse(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def parse(self, arg0: 'Reader') -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonReader.parse(java.io.Reader)"""
        return 'JsonValue'.__wrap(super(__JsonReader, self).parse(arg0))

    @overload
    def parse(self, arg0: str) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonReader.parse(java.lang.String)"""
        return 'JsonValue'.__wrap(super(__JsonReader, self).parse(arg0))

    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonReader.isStopped()"""
        return bool.__wrap(super(JsonReader, self).isStopped())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def parse(self, arg0: 'char', arg1: int, arg2: int) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonReader.parse(char[],int,int)"""
        return 'JsonValue'.__wrap(super(__JsonReader, self).parse(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def stop(self):
        """public void com.badlogic.gdx.utils.JsonReader.stop()"""
        super(JsonReader, self).stop()

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.JsonReader()"""
        val = __JsonReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def parse(self, arg0: 'InputStream') -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonReader.parse(java.io.InputStream)"""
        return 'JsonValue'.__wrap(super(__JsonReader, self).parse(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.JsonReader()"""
        val = __JsonReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.LongMap$Entries
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.LongMap as __LongMap_Entries
__Entries = __LongMap_Entries.Entries
import com.badlogic.gdx.utils.LongMap as __LongMap_Entry
__Entry = __LongMap_Entry.Entry
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.LongMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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
    def __init__(self, arg0: 'LongMap'):
        """public com.badlogic.gdx.utils.LongMap$Entries(com.badlogic.gdx.utils.LongMap)"""
        val = __Entries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.LongMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.LongMap$Entry<V> com.badlogic.gdx.utils.LongMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.LongMap$Entry<V>> com.badlogic.gdx.utils.LongMap$Entries.iterator()"""
        return 'Iterator'.__wrap(super(Entries, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.JsonWriter$OutputType
from builtins import str
import com.badlogic.gdx.utils.JsonWriter as __JsonWriter_OutputType
__OutputType = __JsonWriter_OutputType.OutputType
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
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class OutputType():
    """com.badlogic.gdx.utils.JsonWriter.OutputType"""
 
    @staticmethod
    def __wrap(java_value: __OutputType) -> 'OutputType':
        return OutputType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OutputType):
        """
        Dynamic initializer for OutputType.
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
    def values() -> List['OutputType']:
        """public static com.badlogic.gdx.utils.JsonWriter$OutputType[] com.badlogic.gdx.utils.JsonWriter$OutputType.values()"""
        return List[OutputType].__wrap(__OutputType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'OutputType':
        """public static com.badlogic.gdx.utils.JsonWriter$OutputType com.badlogic.gdx.utils.JsonWriter$OutputType.valueOf(java.lang.String)"""
        return OutputType.__wrap(__OutputType.valueOf(arg0))

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

    @overload
    def quoteName(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonWriter$OutputType.quoteName(java.lang.String)"""
        return str.__wrap(super(__OutputType, self).quoteName(arg0))

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

    @overload
    def quoteValue(self, arg0: object) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonWriter$OutputType.quoteValue(java.lang.Object)"""
        return str.__wrap(super(__OutputType, self).quoteValue(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Align
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.utils.Align as __Align
__Align = __Align
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Align():
    """com.badlogic.gdx.utils.Align"""
 
    @staticmethod
    def __wrap(java_value: __Align) -> 'Align':
        return Align(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Align):
        """
        Dynamic initializer for Align.
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
        """public com.badlogic.gdx.utils.Align()"""
        val = __Align()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def isCenterVertical(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.Align.isCenterVertical(int)"""
        return bool.__wrap(__Align.isCenterVertical(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def isBottom(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.Align.isBottom(int)"""
        return bool.__wrap(__Align.isBottom(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def isRight(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.Align.isRight(int)"""
        return bool.__wrap(__Align.isRight(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Align()"""
        val = __Align()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isCenterHorizontal(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.Align.isCenterHorizontal(int)"""
        return bool.__wrap(__Align.isCenterHorizontal(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def isTop(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.Align.isTop(int)"""
        return bool.__wrap(__Align.isTop(__int.valueOf(arg0)))

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
    def toString(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.utils.Align.toString(int)"""
        return str.__wrap(__Align.toString(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def isLeft(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.Align.isLeft(int)"""
        return bool.__wrap(__Align.isLeft(__int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.utils.SerializationException
from builtins import str
import com.badlogic.gdx.utils.SerializationException as __SerializationException
__SerializationException = __SerializationException
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
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SerializationException():
    """com.badlogic.gdx.utils.SerializationException"""
 
    @staticmethod
    def __wrap(java_value: __SerializationException) -> 'SerializationException':
        return SerializationException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SerializationException):
        """
        Dynamic initializer for SerializationException.
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
    def getMessage(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.SerializationException.getMessage()"""
        return str.__wrap(super(SerializationException, self).getMessage())

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

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.SerializationException(java.lang.String)"""
        val = __SerializationException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.SerializationException()"""
        val = __SerializationException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.utils.SerializationException(java.lang.Throwable)"""
        val = __SerializationException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.SerializationException()"""
        val = __SerializationException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.utils.SerializationException(java.lang.String,java.lang.Throwable)"""
        val = __SerializationException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def addTrace(self, arg0: str):
        """public void com.badlogic.gdx.utils.SerializationException.addTrace(java.lang.String)"""
        super(__SerializationException, self).addTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def causedBy(self, arg0: 'Class') -> bool:
        """public boolean com.badlogic.gdx.utils.SerializationException.causedBy(java.lang.Class)"""
        return bool.__wrap(super(__SerializationException, self).causedBy(arg0))

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

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.badlogic.gdx.utils.XmlReader$Element
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap
__ObjectMap = __ObjectMap
import com.badlogic.gdx.utils.XmlReader as __XmlReader_Element
__Element = __XmlReader_Element.Element
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Element():
    """com.badlogic.gdx.utils.XmlReader.Element"""
 
    @staticmethod
    def __wrap(java_value: __Element) -> 'Element':
        return Element(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Element):
        """
        Dynamic initializer for Element.
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
        """public java.lang.String com.badlogic.gdx.utils.XmlReader$Element.getName()"""
        return str.__wrap(super(Element, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getIntAttribute(self, arg0: str, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.XmlReader$Element.getIntAttribute(java.lang.String,int)"""
        return int.__wrap(super(__Element, self).getIntAttribute(arg0, __int.valueOf(arg1)))

    @overload
    def removeChild(self, arg0: 'Element'):
        """public void com.badlogic.gdx.utils.XmlReader$Element.removeChild(com.badlogic.gdx.utils.XmlReader$Element)"""
        super(__Element, self).removeChild(arg0)

    @overload
    def getInt(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.XmlReader$Element.getInt(java.lang.String)"""
        return int.__wrap(super(__Element, self).getInt(arg0))

    @overload
    def getIntAttribute(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.XmlReader$Element.getIntAttribute(java.lang.String)"""
        return int.__wrap(super(__Element, self).getIntAttribute(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAttribute(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.utils.XmlReader$Element.setAttribute(java.lang.String,java.lang.String)"""
        super(__Element, self).setAttribute(arg0, arg1)

    @overload
    def hasAttribute(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.XmlReader$Element.hasAttribute(java.lang.String)"""
        return bool.__wrap(super(__Element, self).hasAttribute(arg0))

    @overload
    def hasChildRecursive(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.XmlReader$Element.hasChildRecursive(java.lang.String)"""
        return bool.__wrap(super(__Element, self).hasChildRecursive(arg0))

    @overload
    def getFloatAttribute(self, arg0: str) -> float:
        """public float com.badlogic.gdx.utils.XmlReader$Element.getFloatAttribute(java.lang.String)"""
        return float.__wrap(super(__Element, self).getFloatAttribute(arg0))

    @overload
    def getFloatAttribute(self, arg0: str, arg1: float) -> float:
        """public float com.badlogic.gdx.utils.XmlReader$Element.getFloatAttribute(java.lang.String,float)"""
        return float.__wrap(super(__Element, self).getFloatAttribute(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: str, arg1: 'Element'):
        """public com.badlogic.gdx.utils.XmlReader$Element(java.lang.String,com.badlogic.gdx.utils.XmlReader$Element)"""
        val = __Element(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.XmlReader$Element.get(java.lang.String)"""
        return str.__wrap(super(__Element, self).get(arg0))

    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.XmlReader$Element.remove()"""
        super(Element, self).remove()

    @overload
    def getBooleanAttribute(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.XmlReader$Element.getBooleanAttribute(java.lang.String)"""
        return bool.__wrap(super(__Element, self).getBooleanAttribute(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBooleanAttribute(self, arg0: str, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.XmlReader$Element.getBooleanAttribute(java.lang.String,boolean)"""
        return bool.__wrap(super(__Element, self).getBooleanAttribute(arg0, __boolean.valueOf(arg1)))

    @overload
    def getAttribute(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.XmlReader$Element.getAttribute(java.lang.String)"""
        return str.__wrap(super(__Element, self).getAttribute(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getInt(self, arg0: str, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.XmlReader$Element.getInt(java.lang.String,int)"""
        return int.__wrap(super(__Element, self).getInt(arg0, __int.valueOf(arg1)))

    @overload
    def getChildrenByNameRecursively(self, arg0: str) -> 'Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.utils.XmlReader$Element> com.badlogic.gdx.utils.XmlReader$Element.getChildrenByNameRecursively(java.lang.String)"""
        return 'Array'.__wrap(super(__Element, self).getChildrenByNameRecursively(arg0))

    @overload
    def getAttributes(self) -> 'ObjectMap':
        """public com.badlogic.gdx.utils.ObjectMap<java.lang.String, java.lang.String> com.badlogic.gdx.utils.XmlReader$Element.getAttributes()"""
        return 'ObjectMap'.__wrap(super(Element, self).getAttributes())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.XmlReader$Element.toString()"""
        return str.__wrap(super(Element, self).toString())

    @overload
    def addChild(self, arg0: 'Element'):
        """public void com.badlogic.gdx.utils.XmlReader$Element.addChild(com.badlogic.gdx.utils.XmlReader$Element)"""
        super(__Element, self).addChild(arg0)

    @overload
    def getBoolean(self, arg0: str, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.XmlReader$Element.getBoolean(java.lang.String,boolean)"""
        return bool.__wrap(super(__Element, self).getBoolean(arg0, __boolean.valueOf(arg1)))

    @overload
    def getFloat(self, arg0: str) -> float:
        """public float com.badlogic.gdx.utils.XmlReader$Element.getFloat(java.lang.String)"""
        return float.__wrap(super(__Element, self).getFloat(arg0))

    @overload
    def getAttribute(self, arg0: str, arg1: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.XmlReader$Element.getAttribute(java.lang.String,java.lang.String)"""
        return str.__wrap(super(__Element, self).getAttribute(arg0, arg1))

    @overload
    def get(self, arg0: str, arg1: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.XmlReader$Element.get(java.lang.String,java.lang.String)"""
        return str.__wrap(super(__Element, self).get(arg0, arg1))

    @overload
    def getFloat(self, arg0: str, arg1: float) -> float:
        """public float com.badlogic.gdx.utils.XmlReader$Element.getFloat(java.lang.String,float)"""
        return float.__wrap(super(__Element, self).getFloat(arg0, __float.valueOf(arg1)))

    @overload
    def getParent(self) -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader$Element.getParent()"""
        return 'Element'.__wrap(super(Element, self).getParent())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def removeChild(self, arg0: int):
        """public void com.badlogic.gdx.utils.XmlReader$Element.removeChild(int)"""
        super(__Element, self).removeChild(__int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.utils.XmlReader$Element.getChildCount()"""
        return int.__wrap(super(Element, self).getChildCount())

    @overload
    def getChild(self, arg0: int) -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader$Element.getChild(int)"""
        return 'Element'.__wrap(super(__Element, self).getChild(__int.valueOf(arg0)))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.XmlReader$Element.toString(java.lang.String)"""
        return str.__wrap(super(__Element, self).toString(arg0))

    @overload
    def getText(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.XmlReader$Element.getText()"""
        return str.__wrap(super(Element, self).getText())

    @overload
    def getChildByName(self, arg0: str) -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader$Element.getChildByName(java.lang.String)"""
        return 'Element'.__wrap(super(__Element, self).getChildByName(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getChildByNameRecursive(self, arg0: str) -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader$Element.getChildByNameRecursive(java.lang.String)"""
        return 'Element'.__wrap(super(__Element, self).getChildByNameRecursive(arg0))

    @overload
    def getChildrenByName(self, arg0: str) -> 'Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.utils.XmlReader$Element> com.badlogic.gdx.utils.XmlReader$Element.getChildrenByName(java.lang.String)"""
        return 'Array'.__wrap(super(__Element, self).getChildrenByName(arg0))

    @overload
    def hasChild(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.XmlReader$Element.hasChild(java.lang.String)"""
        return bool.__wrap(super(__Element, self).hasChild(arg0))

    @overload
    def getBoolean(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.XmlReader$Element.getBoolean(java.lang.String)"""
        return bool.__wrap(super(__Element, self).getBoolean(arg0))

    @overload
    def setText(self, arg0: str):
        """public void com.badlogic.gdx.utils.XmlReader$Element.setText(java.lang.String)"""
        super(__Element, self).setText(arg0) 
 
 
# CLASS: com.badlogic.gdx.utils.Scaling
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Scaling as __Scaling
__Scaling = __Scaling
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
 
class Scaling(ABC):
    """com.badlogic.gdx.utils.Scaling"""
 
    @staticmethod
    def __wrap(java_value: __Scaling) -> 'Scaling':
        return Scaling(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Scaling):
        """
        Dynamic initializer for Scaling.
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
    def apply(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.Scaling.apply(float,float,float,float)"""
        pass

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Scaling()"""
        val = __Scaling()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public com.badlogic.gdx.utils.Scaling()"""
        val = __Scaling()
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
 
 
# CLASS: com.badlogic.gdx.utils.IntSet$IntSetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.IntSet as __IntSet_IntSetIterator
__IntSetIterator = __IntSet_IntSetIterator.IntSetIterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.IntArray as __IntArray
__IntArray = __IntArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntSetIterator():
    """com.badlogic.gdx.utils.IntSet.IntSetIterator"""
 
    @staticmethod
    def __wrap(java_value: __IntSetIterator) -> 'IntSetIterator':
        return IntSetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntSetIterator):
        """
        Dynamic initializer for IntSetIterator.
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
    def __init__(self, arg0: 'IntSet'):
        """public com.badlogic.gdx.utils.IntSet$IntSetIterator(com.badlogic.gdx.utils.IntSet)"""
        val = __IntSetIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toArray(self) -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntSet$IntSetIterator.toArray()"""
        return 'IntArray'.__wrap(super(IntSetIterator, self).toArray())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def next(self) -> int:
        """public int com.badlogic.gdx.utils.IntSet$IntSetIterator.next()"""
        return int.__wrap(super(IntSetIterator, self).next())

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

    @overload
    def reset(self):
        """public void com.badlogic.gdx.utils.IntSet$IntSetIterator.reset()"""
        super(IntSetIterator, self).reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.IntSet$IntSetIterator.remove()"""
        super(IntSetIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectFloatMap$Entry
from builtins import str
import java.lang.Long as __long
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap_Entry
__Entry = __ObjectFloatMap_Entry.Entry
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
 
class Entry():
    """com.badlogic.gdx.utils.ObjectFloatMap.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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
        """public java.lang.String com.badlogic.gdx.utils.ObjectFloatMap$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectFloatMap$Entry()"""
        val = __Entry()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectFloatMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.IntFloatMap$Entry
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
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap_Entry
__Entry = __IntFloatMap_Entry.Entry
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Entry():
    """com.badlogic.gdx.utils.IntFloatMap.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IntFloatMap$Entry()"""
        val = __Entry()
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
        """public java.lang.String com.badlogic.gdx.utils.IntFloatMap$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IntFloatMap$Entry()"""
        val = __Entry()
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
 
 
# CLASS: com.badlogic.gdx.utils.PooledLinkedList
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.badlogic.gdx.utils.PooledLinkedList as __PooledLinkedList
__PooledLinkedList = __PooledLinkedList
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
 
class PooledLinkedList():
    """com.badlogic.gdx.utils.PooledLinkedList"""
 
    @staticmethod
    def __wrap(java_value: __PooledLinkedList) -> 'PooledLinkedList':
        return PooledLinkedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PooledLinkedList):
        """
        Dynamic initializer for PooledLinkedList.
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
    def clear(self):
        """public void com.badlogic.gdx.utils.PooledLinkedList.clear()"""
        super(PooledLinkedList, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def previous(self) -> object:
        """public T com.badlogic.gdx.utils.PooledLinkedList.previous()"""
        return object.__wrap(super(PooledLinkedList, self).previous())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def next(self) -> object:
        """public T com.badlogic.gdx.utils.PooledLinkedList.next()"""
        return object.__wrap(super(PooledLinkedList, self).next())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.PooledLinkedList.remove()"""
        super(PooledLinkedList, self).remove()

    @overload
    def iterReverse(self):
        """public void com.badlogic.gdx.utils.PooledLinkedList.iterReverse()"""
        super(PooledLinkedList, self).iterReverse()

    @overload
    def removeLast(self) -> object:
        """public T com.badlogic.gdx.utils.PooledLinkedList.removeLast()"""
        return object.__wrap(super(PooledLinkedList, self).removeLast())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def iter(self):
        """public void com.badlogic.gdx.utils.PooledLinkedList.iter()"""
        super(PooledLinkedList, self).iter()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addFirst(self, arg0: object):
        """public void com.badlogic.gdx.utils.PooledLinkedList.addFirst(T)"""
        super(__PooledLinkedList, self).addFirst(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.utils.PooledLinkedList.add(T)"""
        super(__PooledLinkedList, self).add(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.utils.PooledLinkedList.size()"""
        return int.__wrap(super(PooledLinkedList, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.PooledLinkedList(int)"""
        val = __PooledLinkedList(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.OrderedSet$OrderedSetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectSet as __ObjectSet_ObjectSetIterator
__ObjectSetIterator = __ObjectSet_ObjectSetIterator.ObjectSetIterator
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.OrderedSet as __OrderedSet_OrderedSetIterator
__OrderedSetIterator = __OrderedSet_OrderedSetIterator.OrderedSetIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class OrderedSetIterator():
    """com.badlogic.gdx.utils.OrderedSet.OrderedSetIterator"""
 
    @staticmethod
    def __wrap(java_value: __OrderedSetIterator) -> 'OrderedSetIterator':
        return OrderedSetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedSetIterator):
        """
        Dynamic initializer for OrderedSetIterator.
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
    def reset(self):
        """public void com.badlogic.gdx.utils.OrderedSet$OrderedSetIterator.reset()"""
        super(OrderedSetIterator, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.OrderedSet$OrderedSetIterator.remove()"""
        super(OrderedSetIterator, self).remove()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.hasNext()"""
        return bool.__wrap(super(ObjectSetIterator, self).hasNext())

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
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.OrderedSet$OrderedSetIterator.toArray()"""
        return 'Array'.__wrap(super(OrderedSetIterator, self).toArray())

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.OrderedSet$OrderedSetIterator.toArray(com.badlogic.gdx.utils.Array<K>)"""
        return 'Array'.__wrap(super(__OrderedSetIterator, self).toArray(arg0))

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
    def next(self) -> object:
        """public K com.badlogic.gdx.utils.OrderedSet$OrderedSetIterator.next()"""
        return object.__wrap(super(OrderedSetIterator, self).next())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def iterator(self) -> 'ObjectSetIterator':
        """public com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator<K> com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.iterator()"""
        return 'ObjectSetIterator'.__wrap(super(ObjectSetIterator, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def __init__(self, arg0: 'OrderedSet'):
        """public com.badlogic.gdx.utils.OrderedSet$OrderedSetIterator(com.badlogic.gdx.utils.OrderedSet<K>)"""
        val = __OrderedSetIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectFloatMap$Entries
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap_Entry
__Entry = __ObjectFloatMap_Entry.Entry
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap_Entries
__Entries = __ObjectFloatMap_Entries.Entries
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.ObjectFloatMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.ObjectFloatMap$Entry<K> com.badlogic.gdx.utils.ObjectFloatMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

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

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectFloatMap$Entries<K> com.badlogic.gdx.utils.ObjectFloatMap$Entries.iterator()"""
        return 'Entries'.__wrap(super(Entries, self).iterator())

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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'ObjectFloatMap'):
        """public com.badlogic.gdx.utils.ObjectFloatMap$Entries(com.badlogic.gdx.utils.ObjectFloatMap<K>)"""
        val = __Entries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectIntMap$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap_Keys
__Keys = __ObjectIntMap_Keys.Keys
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Keys():
    """com.badlogic.gdx.utils.ObjectIntMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectIntMap$Keys.toArray()"""
        return 'Array'.__wrap(super(Keys, self).toArray())

    @overload
    def __init__(self, arg0: 'ObjectIntMap'):
        """public com.badlogic.gdx.utils.ObjectIntMap$Keys(com.badlogic.gdx.utils.ObjectIntMap<K>)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectIntMap$Keys.toArray(com.badlogic.gdx.utils.Array<K>)"""
        return 'Array'.__wrap(super(__Keys, self).toArray(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def iterator(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectIntMap$Keys<K> com.badlogic.gdx.utils.ObjectIntMap$Keys.iterator()"""
        return 'Keys'.__wrap(super(Keys, self).iterator())

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
    def next(self) -> object:
        """public K com.badlogic.gdx.utils.ObjectIntMap$Keys.next()"""
        return object.__wrap(super(Keys, self).next())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectIntMap$Keys.hasNext()"""
        return bool.__wrap(super(Keys, self).hasNext())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectMap$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Keys
__Keys = __ObjectMap_Keys.Keys
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Keys():
    """com.badlogic.gdx.utils.ObjectMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap$Keys.hasNext()"""
        return bool.__wrap(super(Keys, self).hasNext())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def iterator(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectMap$Keys<K> com.badlogic.gdx.utils.ObjectMap$Keys.iterator()"""
        return 'Keys'.__wrap(super(Keys, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def next(self) -> object:
        """public K com.badlogic.gdx.utils.ObjectMap$Keys.next()"""
        return object.__wrap(super(Keys, self).next())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectMap$Keys.toArray(com.badlogic.gdx.utils.Array<K>)"""
        return 'Array'.__wrap(super(__Keys, self).toArray(arg0))

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

    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectMap$Keys.toArray()"""
        return 'Array'.__wrap(super(Keys, self).toArray())

    @overload
    def __init__(self, arg0: 'ObjectMap'):
        """public com.badlogic.gdx.utils.ObjectMap$Keys(com.badlogic.gdx.utils.ObjectMap<K, ?>)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.FlushablePool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.FlushablePool as __FlushablePool
__FlushablePool = __FlushablePool
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FlushablePool(ABC):
    """com.badlogic.gdx.utils.FlushablePool"""
 
    @staticmethod
    def __wrap(java_value: __FlushablePool) -> 'FlushablePool':
        return FlushablePool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FlushablePool):
        """
        Dynamic initializer for FlushablePool.
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
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.utils.FlushablePool(int,int)"""
        val = __FlushablePool(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.FlushablePool()"""
        val = __FlushablePool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(Pool, self).clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def free(self, arg0: object):
        """public void com.badlogic.gdx.utils.FlushablePool.free(T)"""
        super(__FlushablePool, self).free(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def obtain(self) -> object:
        """public T com.badlogic.gdx.utils.FlushablePool.obtain()"""
        return object.__wrap(super(FlushablePool, self).obtain())

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
    def flush(self):
        """public void com.badlogic.gdx.utils.FlushablePool.flush()"""
        super(FlushablePool, self).flush()

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.FlushablePool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__FlushablePool, self).freeAll(arg0)

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int.__wrap(super(Pool, self).getFree())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(__Pool, self).fill(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.FlushablePool()"""
        val = __FlushablePool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.FlushablePool(int)"""
        val = __FlushablePool(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectIntMap
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap_Values
__Values = __ObjectIntMap_Values.Values
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap
__ObjectIntMap = __ObjectIntMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap_Keys
__Keys = __ObjectIntMap_Keys.Keys
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap_Entries
__Entries = __ObjectIntMap_Entries.Entries
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ObjectIntMap():
    """com.badlogic.gdx.utils.ObjectIntMap"""
 
    @staticmethod
    def __wrap(java_value: __ObjectIntMap) -> 'ObjectIntMap':
        return ObjectIntMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectIntMap):
        """
        Dynamic initializer for ObjectIntMap.
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
    def remove(self, arg0: object, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.ObjectIntMap.remove(K,int)"""
        return int.__wrap(super(__ObjectIntMap, self).remove(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectIntMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectIntMap, self).equals(arg0))

    @overload
    def putAll(self, arg0: 'ObjectIntMap'):
        """public void com.badlogic.gdx.utils.ObjectIntMap.putAll(com.badlogic.gdx.utils.ObjectIntMap<? extends K>)"""
        super(__ObjectIntMap, self).putAll(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectIntMap.toString()"""
        return str.__wrap(super(ObjectIntMap, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectIntMap$Entries<K> com.badlogic.gdx.utils.ObjectIntMap.entries()"""
        return 'Entries'.__wrap(super(ObjectIntMap, self).entries())

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectIntMap.ensureCapacity(int)"""
        super(__ObjectIntMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectIntMap$Keys<K> com.badlogic.gdx.utils.ObjectIntMap.keys()"""
        return 'Keys'.__wrap(super(ObjectIntMap, self).keys())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ObjectIntMap.hashCode()"""
        return int.__wrap(super(ObjectIntMap, self).hashCode())

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectIntMap.clear(int)"""
        super(__ObjectIntMap, self).clear(__int.valueOf(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectIntMap.containsKey(K)"""
        return bool.__wrap(super(__ObjectIntMap, self).containsKey(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.ObjectIntMap(int)"""
        val = __ObjectIntMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ObjectIntMap'):
        """public com.badlogic.gdx.utils.ObjectIntMap(com.badlogic.gdx.utils.ObjectIntMap<? extends K>)"""
        val = __ObjectIntMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def findKey(self, arg0: int) -> object:
        """public K com.badlogic.gdx.utils.ObjectIntMap.findKey(int)"""
        return object.__wrap(super(__ObjectIntMap, self).findKey(__int.valueOf(arg0)))

    @overload
    def getAndIncrement(self, arg0: object, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.ObjectIntMap.getAndIncrement(K,int,int)"""
        return int.__wrap(super(__ObjectIntMap, self).getAndIncrement(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectIntMap.toString(java.lang.String)"""
        return str.__wrap(super(__ObjectIntMap, self).toString(arg0))

    @overload
    def containsValue(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectIntMap.containsValue(int)"""
        return bool.__wrap(super(__ObjectIntMap, self).containsValue(__int.valueOf(arg0)))

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectIntMap.shrink(int)"""
        super(__ObjectIntMap, self).shrink(__int.valueOf(arg0))

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectIntMap$Values com.badlogic.gdx.utils.ObjectIntMap.values()"""
        return 'Values'.__wrap(super(ObjectIntMap, self).values())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.ObjectIntMap(int,float)"""
        val = __ObjectIntMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectIntMap.notEmpty()"""
        return bool.__wrap(super(ObjectIntMap, self).notEmpty())

    @overload
    def put(self, arg0: object, arg1: int):
        """public void com.badlogic.gdx.utils.ObjectIntMap.put(K,int)"""
        super(__ObjectIntMap, self).put(arg0, __int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectIntMap$Entries<K> com.badlogic.gdx.utils.ObjectIntMap.iterator()"""
        return 'Entries'.__wrap(super(ObjectIntMap, self).iterator())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectIntMap()"""
        val = __ObjectIntMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.ObjectIntMap.put(K,int,int)"""
        return int.__wrap(super(__ObjectIntMap, self).put(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ObjectIntMap.clear()"""
        super(ObjectIntMap, self).clear()

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
    def get(self, arg0: object, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.ObjectIntMap.get(K,int)"""
        return int.__wrap(super(__ObjectIntMap, self).get(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectIntMap.isEmpty()"""
        return bool.__wrap(super(ObjectIntMap, self).isEmpty())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectIntMap()"""
        val = __ObjectIntMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.JsonValue$JsonIterator
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.JsonValue as __JsonValue
__JsonValue = __JsonValue
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.JsonValue as __JsonValue_JsonIterator
__JsonIterator = __JsonValue_JsonIterator.JsonIterator
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class JsonIterator():
    """com.badlogic.gdx.utils.JsonValue.JsonIterator"""
 
    @staticmethod
    def __wrap(java_value: __JsonIterator) -> 'JsonIterator':
        return JsonIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonIterator):
        """
        Dynamic initializer for JsonIterator.
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
    def remove(self):
        """public void com.badlogic.gdx.utils.JsonValue$JsonIterator.remove()"""
        super(JsonIterator, self).remove()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue$JsonIterator.hasNext()"""
        return bool.__wrap(super(JsonIterator, self).hasNext())

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

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.JsonValue> com.badlogic.gdx.utils.JsonValue$JsonIterator.iterator()"""
        return 'Iterator'.__wrap(super(JsonIterator, self).iterator())

    @overload
    def __init__(self, arg0: 'JsonValue'):
        """public com.badlogic.gdx.utils.JsonValue$JsonIterator(com.badlogic.gdx.utils.JsonValue)"""
        val = __JsonIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def next(self) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue$JsonIterator.next()"""
        return 'JsonValue'.__wrap(super(JsonIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectIntMap$Entry
from builtins import str
import java.lang.Long as __long
import com.badlogic.gdx.utils.ObjectIntMap as __ObjectIntMap_Entry
__Entry = __ObjectIntMap_Entry.Entry
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
 
class Entry():
    """com.badlogic.gdx.utils.ObjectIntMap.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectIntMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectIntMap$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

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
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectIntMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.Predicate
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Predicate as __Predicate
__Predicate = __Predicate
 
class Predicate(ABC):
    """com.badlogic.gdx.utils.Predicate"""
 
    @staticmethod
    def __wrap(java_value: __Predicate) -> 'Predicate':
        return Predicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Predicate):
        """
        Dynamic initializer for Predicate.
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
    def evaluate(self, arg0: object):
        """public abstract boolean com.badlogic.gdx.utils.Predicate.evaluate(T)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.utils.SnapshotArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.utils.Array as __Array_ArrayIterator
__ArrayIterator = __Array_ArrayIterator.ArrayIterator
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.SnapshotArray as __SnapshotArray
__SnapshotArray = __SnapshotArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SnapshotArray():
    """com.badlogic.gdx.utils.SnapshotArray"""
 
    @staticmethod
    def __wrap(java_value: __SnapshotArray) -> 'SnapshotArray':
        return SnapshotArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SnapshotArray):
        """
        Dynamic initializer for SnapshotArray.
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
    def begin(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.SnapshotArray.begin()"""
        return List[object].__wrap(super(SnapshotArray, self).begin())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString(java.lang.String)"""
        return str.__wrap(super(__Array, self).toString(arg0))

    @override
    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.SnapshotArray.sort()"""
        super(SnapshotArray, self).sort()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.SnapshotArray.insertRange(int,int)"""
        super(__SnapshotArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def lastIndexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.lastIndexOf(T,boolean)"""
        return int.__wrap(super(__Array, self).lastIndexOf(arg0, __boolean.valueOf(arg1)))

    @overload
    def contains(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.contains(T,boolean)"""
        return bool.__wrap(super(__Array, self).contains(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def of(arg0: 'Class') -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(java.lang.Class<T>)"""
        return Array.__wrap(__Array.of(arg0))

    @override
    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.Array.addAll(com.badlogic.gdx.utils.Array<? extends T>)"""
        super(__Array, self).addAll(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'Class'):
        """public com.badlogic.gdx.utils.SnapshotArray(boolean,int,java.lang.Class)"""
        val = __SnapshotArray(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def set(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.SnapshotArray.set(int,T)"""
        super(__SnapshotArray, self).set(__int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString()"""
        return str.__wrap(super(Array, self).toString())

    @overload
    def __init__(self, arg0: 'Object'):
        """public com.badlogic.gdx.utils.SnapshotArray(T[])"""
        val = __SnapshotArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def add(self, arg0: object, arg1: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T)"""
        super(__Array, self).add(arg0, arg1)

    @override
    @overload
    def addAll(self, arg0: 'Array', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.Array.addAll(com.badlogic.gdx.utils.Array<? extends T>,int,int)"""
        super(__Array, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.Array.hashCode()"""
        return int.__wrap(super(Array, self).hashCode())

    @override
    @overload
    def add(self, arg0: object, arg1: object, arg2: object, arg3: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T,T,T)"""
        super(__Array, self).add(arg0, arg1, arg2, arg3)

    @overload
    def selectRankedIndex(self, arg0: 'Comparator', arg1: int) -> int:
        """public int com.badlogic.gdx.utils.Array.selectRankedIndex(java.util.Comparator<T>,int)"""
        return int.__wrap(super(__Array, self).selectRankedIndex(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.utils.Array.first()"""
        return object.__wrap(super(Array, self).first())

    @overload
    def setSize(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.SnapshotArray.setSize(int)"""
        return List[object].__wrap(super(__SnapshotArray, self).setSize(__int.valueOf(arg0)))

    @override
    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.SnapshotArray.shuffle()"""
        super(SnapshotArray, self).shuffle()

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public <V> V[] com.badlogic.gdx.utils.Array.toArray(java.lang.Class<V>)"""
        return List[object].__wrap(super(__Array, self).toArray(arg0))

    @override
    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.SnapshotArray.removeRange(int,int)"""
        super(__SnapshotArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def addAll(self, *arg0: object):
        """public void com.badlogic.gdx.utils.Array.addAll(T...)"""
        super(__Array, self).addAll(arg0)

    @overload
    def end(self):
        """public void com.badlogic.gdx.utils.SnapshotArray.end()"""
        super(SnapshotArray, self).end()

    @overload
    def removeIndex(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.SnapshotArray.removeIndex(int)"""
        return object.__wrap(super(__SnapshotArray, self).removeIndex(__int.valueOf(arg0)))

    @override
    @overload
    def add(self, arg0: object, arg1: object, arg2: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T,T)"""
        super(__Array, self).add(arg0, arg1, arg2)

    @staticmethod
    @overload
    def with(*arg0: object) -> 'SnapshotArray':
        """public static <T> com.badlogic.gdx.utils.SnapshotArray<T> com.badlogic.gdx.utils.SnapshotArray.with(T...)"""
        return SnapshotArray.__wrap(__SnapshotArray.with(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Array.get(int)"""
        return object.__wrap(super(__Array, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def __init__(self, arg0: 'Class'):
        """public com.badlogic.gdx.utils.SnapshotArray(java.lang.Class)"""
        val = __SnapshotArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.SnapshotArray.truncate(int)"""
        super(__SnapshotArray, self).truncate(__int.valueOf(arg0))

    @overload
    def selectRanked(self, arg0: 'Comparator', arg1: int) -> object:
        """public T com.badlogic.gdx.utils.Array.selectRanked(java.util.Comparator<T>,int)"""
        return object.__wrap(super(__Array, self).selectRanked(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__Array, self).equalsIdentity(arg0))

    @override
    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.SnapshotArray.reverse()"""
        super(SnapshotArray, self).reverse()

    @override
    @overload
    def toArray(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.toArray()"""
        return List[object].__wrap(super(Array, self).toArray())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.utils.SnapshotArray(com.badlogic.gdx.utils.Array)"""
        val = __SnapshotArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'ArrayIterator':
        """public com.badlogic.gdx.utils.Array$ArrayIterator<T> com.badlogic.gdx.utils.Array.iterator()"""
        return 'ArrayIterator'.__wrap(super(Array, self).iterator())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void com.badlogic.gdx.utils.SnapshotArray.sort(java.util.Comparator<? super T>)"""
        super(__SnapshotArray, self).sort(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.SnapshotArray()"""
        val = __SnapshotArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.SnapshotArray.swap(int,int)"""
        super(__SnapshotArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.isEmpty()"""
        return bool.__wrap(super(Array, self).isEmpty())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.SnapshotArray.clear()"""
        super(SnapshotArray, self).clear()

    @override
    @overload
    def pop(self) -> object:
        """public T com.badlogic.gdx.utils.SnapshotArray.pop()"""
        return object.__wrap(super(SnapshotArray, self).pop())

    @overload
    def containsAny(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAny(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__Array, self).containsAny(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: bool, arg1: 'Object', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.SnapshotArray(boolean,T[],int,int)"""
        val = __SnapshotArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def shrink(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.shrink()"""
        return List[object].__wrap(super(Array, self).shrink())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equals(java.lang.Object)"""
        return bool.__wrap(super(__Array, self).equals(arg0))

    @overload
    def removeValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.SnapshotArray.removeValue(T,boolean)"""
        return bool.__wrap(super(__SnapshotArray, self).removeValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def ensureCapacity(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.ensureCapacity(int)"""
        return List[object].__wrap(super(__Array, self).ensureCapacity(__int.valueOf(arg0)))

    @override
    @overload
    def peek(self) -> object:
        """public T com.badlogic.gdx.utils.Array.peek()"""
        return object.__wrap(super(Array, self).peek())

    @staticmethod
    @overload
    def of(arg0: bool, arg1: int, arg2: 'Class') -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(boolean,int,java.lang.Class<T>)"""
        return Array.__wrap(__Array.of(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.SnapshotArray(int)"""
        val = __SnapshotArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def random(self) -> object:
        """public T com.badlogic.gdx.utils.Array.random()"""
        return object.__wrap(super(Array, self).random())

    @overload
    def removeAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.SnapshotArray.removeAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__SnapshotArray, self).removeAll(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.utils.Array.add(T)"""
        super(__Array, self).add(arg0)

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.indexOf(T,boolean)"""
        return int.__wrap(super(__Array, self).indexOf(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.SnapshotArray()"""
        val = __SnapshotArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__Array, self).containsAll(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.notEmpty()"""
        return bool.__wrap(super(Array, self).notEmpty())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def addAll(self, arg0: 'Object', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.Array.addAll(T[],int,int)"""
        super(__Array, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.SnapshotArray(boolean,int)"""
        val = __SnapshotArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def select(self, arg0: 'Predicate') -> 'Iterable':
        """public java.lang.Iterable<T> com.badlogic.gdx.utils.Array.select(com.badlogic.gdx.utils.Predicate<T>)"""
        return 'Iterable'.__wrap(super(__Array, self).select(arg0))

    @staticmethod
    @overload
    def with(*arg0: object) -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.with(T...)"""
        return Array.__wrap(__Array.with(arg0))

    @override
    @overload
    def insert(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.SnapshotArray.insert(int,T)"""
        super(__SnapshotArray, self).insert(__int.valueOf(arg0), arg1) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectFloatMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap_Keys
__Keys = __ObjectFloatMap_Keys.Keys
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap
__ObjectFloatMap = __ObjectFloatMap
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap_Values
__Values = __ObjectFloatMap_Values.Values
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap_Entries
__Entries = __ObjectFloatMap_Entries.Entries
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ObjectFloatMap():
    """com.badlogic.gdx.utils.ObjectFloatMap"""
 
    @staticmethod
    def __wrap(java_value: __ObjectFloatMap) -> 'ObjectFloatMap':
        return ObjectFloatMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectFloatMap):
        """
        Dynamic initializer for ObjectFloatMap.
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
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectFloatMap.toString(java.lang.String)"""
        return str.__wrap(super(__ObjectFloatMap, self).toString(arg0))

    @overload
    def putAll(self, arg0: 'ObjectFloatMap'):
        """public void com.badlogic.gdx.utils.ObjectFloatMap.putAll(com.badlogic.gdx.utils.ObjectFloatMap<? extends K>)"""
        super(__ObjectFloatMap, self).putAll(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ObjectFloatMap.hashCode()"""
        return int.__wrap(super(ObjectFloatMap, self).hashCode())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap.isEmpty()"""
        return bool.__wrap(super(ObjectFloatMap, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def findKey(self, arg0: float) -> object:
        """public K com.badlogic.gdx.utils.ObjectFloatMap.findKey(float)"""
        return object.__wrap(super(__ObjectFloatMap, self).findKey(__float.valueOf(arg0)))

    @overload
    def containsValue(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap.containsValue(float,float)"""
        return bool.__wrap(super(__ObjectFloatMap, self).containsValue(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def getAndIncrement(self, arg0: object, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.utils.ObjectFloatMap.getAndIncrement(K,float,float)"""
        return float.__wrap(super(__ObjectFloatMap, self).getAndIncrement(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectFloatMap, self).equals(arg0))

    @overload
    def findKey(self, arg0: float, arg1: float) -> object:
        """public K com.badlogic.gdx.utils.ObjectFloatMap.findKey(float,float)"""
        return object.__wrap(super(__ObjectFloatMap, self).findKey(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectFloatMap()"""
        val = __ObjectFloatMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: object, arg1: float) -> float:
        """public float com.badlogic.gdx.utils.ObjectFloatMap.get(K,float)"""
        return float.__wrap(super(__ObjectFloatMap, self).get(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap.notEmpty()"""
        return bool.__wrap(super(ObjectFloatMap, self).notEmpty())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.ObjectFloatMap(int,float)"""
        val = __ObjectFloatMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectFloatMap$Values com.badlogic.gdx.utils.ObjectFloatMap.values()"""
        return 'Values'.__wrap(super(ObjectFloatMap, self).values())

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectFloatMap.clear(int)"""
        super(__ObjectFloatMap, self).clear(__int.valueOf(arg0))

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectFloatMap.ensureCapacity(int)"""
        super(__ObjectFloatMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ObjectFloatMap.clear()"""
        super(ObjectFloatMap, self).clear()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.ObjectFloatMap(int)"""
        val = __ObjectFloatMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ObjectFloatMap'):
        """public com.badlogic.gdx.utils.ObjectFloatMap(com.badlogic.gdx.utils.ObjectFloatMap<? extends K>)"""
        val = __ObjectFloatMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def put(self, arg0: object, arg1: float):
        """public void com.badlogic.gdx.utils.ObjectFloatMap.put(K,float)"""
        super(__ObjectFloatMap, self).put(arg0, __float.valueOf(arg1))

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectFloatMap.shrink(int)"""
        super(__ObjectFloatMap, self).shrink(__int.valueOf(arg0))

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectFloatMap$Keys<K> com.badlogic.gdx.utils.ObjectFloatMap.keys()"""
        return 'Keys'.__wrap(super(ObjectFloatMap, self).keys())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectFloatMap()"""
        val = __ObjectFloatMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectFloatMap.toString()"""
        return str.__wrap(super(ObjectFloatMap, self).toString())

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectFloatMap$Entries<K> com.badlogic.gdx.utils.ObjectFloatMap.iterator()"""
        return 'Entries'.__wrap(super(ObjectFloatMap, self).iterator())

    @overload
    def containsValue(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap.containsValue(float)"""
        return bool.__wrap(super(__ObjectFloatMap, self).containsValue(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def remove(self, arg0: object, arg1: float) -> float:
        """public float com.badlogic.gdx.utils.ObjectFloatMap.remove(K,float)"""
        return float.__wrap(super(__ObjectFloatMap, self).remove(arg0, __float.valueOf(arg1)))

    @overload
    def put(self, arg0: object, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.utils.ObjectFloatMap.put(K,float,float)"""
        return float.__wrap(super(__ObjectFloatMap, self).put(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap.containsKey(K)"""
        return bool.__wrap(super(__ObjectFloatMap, self).containsKey(arg0))

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectFloatMap$Entries<K> com.badlogic.gdx.utils.ObjectFloatMap.entries()"""
        return 'Entries'.__wrap(super(ObjectFloatMap, self).entries()) 
 
 
# CLASS: com.badlogic.gdx.utils.IntSet
import com.badlogic.gdx.utils.IntSet as __IntSet
__IntSet = __IntSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.IntSet as __IntSet_IntSetIterator
__IntSetIterator = __IntSet_IntSetIterator.IntSetIterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntSet():
    """com.badlogic.gdx.utils.IntSet"""
 
    @staticmethod
    def __wrap(java_value: __IntSet) -> 'IntSet':
        return IntSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntSet):
        """
        Dynamic initializer for IntSet.
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
    def addAll(self, *arg0: int):
        """public void com.badlogic.gdx.utils.IntSet.addAll(int...)"""
        super(__IntSet, self).addAll(arg0)

    @overload
    def first(self) -> int:
        """public int com.badlogic.gdx.utils.IntSet.first()"""
        return int.__wrap(super(IntSet, self).first())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.IntSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntSet, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IntSet()"""
        val = __IntSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.IntSet.toString()"""
        return str.__wrap(super(IntSet, self).toString())

    @overload
    def addAll(self, arg0: 'IntSet'):
        """public void com.badlogic.gdx.utils.IntSet.addAll(com.badlogic.gdx.utils.IntSet)"""
        super(__IntSet, self).addAll(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.IntSet.clear()"""
        super(IntSet, self).clear()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.IntSet(int)"""
        val = __IntSet(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntSet.clear(int)"""
        super(__IntSet, self).clear(__int.valueOf(arg0))

    @overload
    def add(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntSet.add(int)"""
        return bool.__wrap(super(__IntSet, self).add(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def with(*arg0: int) -> 'IntSet':
        """public static com.badlogic.gdx.utils.IntSet com.badlogic.gdx.utils.IntSet.with(int...)"""
        return IntSet.__wrap(__IntSet.with(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.IntSet.hashCode()"""
        return int.__wrap(super(IntSet, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.IntSet(int,float)"""
        val = __IntSet(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IntSet()"""
        val = __IntSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'IntSet'):
        """public com.badlogic.gdx.utils.IntSet(com.badlogic.gdx.utils.IntSet)"""
        val = __IntSet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntSet.ensureCapacity(int)"""
        super(__IntSet, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def contains(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntSet.contains(int)"""
        return bool.__wrap(super(__IntSet, self).contains(__int.valueOf(arg0)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntSet.isEmpty()"""
        return bool.__wrap(super(IntSet, self).isEmpty())

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
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntSet.shrink(int)"""
        super(__IntSet, self).shrink(__int.valueOf(arg0))

    @overload
    def addAll(self, arg0: 'IntArray', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.IntSet.addAll(com.badlogic.gdx.utils.IntArray,int,int)"""
        super(__IntSet, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def addAll(self, arg0: 'int', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.IntSet.addAll(int[],int,int)"""
        super(__IntSet, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def remove(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntSet.remove(int)"""
        return bool.__wrap(super(__IntSet, self).remove(__int.valueOf(arg0)))

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntSet.notEmpty()"""
        return bool.__wrap(super(IntSet, self).notEmpty())

    @overload
    def iterator(self) -> 'IntSetIterator':
        """public com.badlogic.gdx.utils.IntSet$IntSetIterator com.badlogic.gdx.utils.IntSet.iterator()"""
        return 'IntSetIterator'.__wrap(super(IntSet, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, arg0: 'IntArray'):
        """public void com.badlogic.gdx.utils.IntSet.addAll(com.badlogic.gdx.utils.IntArray)"""
        super(__IntSet, self).addAll(arg0) 
 
 
# CLASS: com.badlogic.gdx.utils.JsonWriter
from builtins import str
import java.lang.Character as __char
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import com.badlogic.gdx.utils.JsonWriter as __JsonWriter
__JsonWriter = __JsonWriter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JsonWriter():
    """com.badlogic.gdx.utils.JsonWriter"""
 
    @staticmethod
    def __wrap(java_value: __JsonWriter) -> 'JsonWriter':
        return JsonWriter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonWriter):
        """
        Dynamic initializer for JsonWriter.
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
    def array(self, arg0: str) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.array(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).array(arg0))

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.utils.JsonWriter.flush() throws java.io.IOException"""
        super(JsonWriter, self).flush()

    @override
    @overload
    def write(self, arg0: int):
        """public void java.io.Writer.write(int) throws java.io.IOException"""
        super(__Writer, self).write(__int.valueOf(arg0))

    @overload
    def getWriter(self) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.utils.JsonWriter.getWriter()"""
        return 'Writer'.__wrap(super(JsonWriter, self).getWriter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setQuoteLongValues(self, arg0: bool):
        """public void com.badlogic.gdx.utils.JsonWriter.setQuoteLongValues(boolean)"""
        super(__JsonWriter, self).setQuoteLongValues(__boolean.valueOf(arg0))

    @overload
    def value(self, arg0: object) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.value(java.lang.Object) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).value(arg0))

    @override
    @overload
    def write(self, arg0: 'char'):
        """public void java.io.Writer.write(char[]) throws java.io.IOException"""
        super(__Writer, self).write(arg0)

    @overload
    def json(self, arg0: str, arg1: str) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.json(java.lang.String,java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).json(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def object(self, arg0: str) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.object(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).object(arg0))

    @overload
    def __init__(self, arg0: 'Writer'):
        """public com.badlogic.gdx.utils.JsonWriter(java.io.Writer)"""
        val = __JsonWriter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nullWriter() -> 'Writer':
        """public static java.io.Writer java.io.Writer.nullWriter()"""
        return Writer.__wrap(__Writer.nullWriter())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def array(self) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.array() throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(JsonWriter, self).array())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def write(self, arg0: str):
        """public void java.io.Writer.write(java.lang.String) throws java.io.IOException"""
        super(__Writer, self).write(arg0)

    @override
    @overload
    def close(self):
        """public void com.badlogic.gdx.utils.JsonWriter.close() throws java.io.IOException"""
        super(JsonWriter, self).close()

    @overload
    def object(self) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.object() throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(JsonWriter, self).object())

    @overload
    def append(self, arg0: str) -> 'Writer':
        """public java.io.Writer java.io.Writer.append(char) throws java.io.IOException"""
        return 'Writer'.__wrap(super(__Writer, self).append(__char.valueOf(arg0)))

    @overload
    def append(self, arg0: 'CharSequence') -> 'Writer':
        """public java.io.Writer java.io.Writer.append(java.lang.CharSequence) throws java.io.IOException"""
        return 'Writer'.__wrap(super(__Writer, self).append(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: str, arg1: object) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.set(java.lang.String,java.lang.Object) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).set(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def name(self, arg0: str) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.name(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).name(arg0))

    @override
    @overload
    def write(self, arg0: 'char', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.JsonWriter.write(char[],int,int) throws java.io.IOException"""
        super(__JsonWriter, self).write(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def pop(self) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.pop() throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(JsonWriter, self).pop())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: str, arg1: int, arg2: int):
        """public void java.io.Writer.write(java.lang.String,int,int) throws java.io.IOException"""
        super(__Writer, self).write(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def json(self, arg0: str) -> 'JsonWriter':
        """public com.badlogic.gdx.utils.JsonWriter com.badlogic.gdx.utils.JsonWriter.json(java.lang.String) throws java.io.IOException"""
        return 'JsonWriter'.__wrap(super(__JsonWriter, self).json(arg0))

    @overload
    def append(self, arg0: 'CharSequence', arg1: int, arg2: int) -> 'Writer':
        """public java.io.Writer java.io.Writer.append(java.lang.CharSequence,int,int) throws java.io.IOException"""
        return 'Writer'.__wrap(super(__Writer, self).append(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setOutputType(self, arg0: 'OutputType'):
        """public void com.badlogic.gdx.utils.JsonWriter.setOutputType(com.badlogic.gdx.utils.JsonWriter$OutputType)"""
        super(__JsonWriter, self).setOutputType(arg0) 
 
 
# CLASS: com.badlogic.gdx.utils.IntMap$Values
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.IntMap as __IntMap_Values
__Values = __IntMap_Values.Values
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Values():
    """com.badlogic.gdx.utils.IntMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def next(self) -> object:
        """public V com.badlogic.gdx.utils.IntMap$Values.next()"""
        return object.__wrap(super(Values, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<V> com.badlogic.gdx.utils.IntMap$Values.toArray()"""
        return 'Array'.__wrap(super(Values, self).toArray())

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

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'IntMap'):
        """public com.badlogic.gdx.utils.IntMap$Values(com.badlogic.gdx.utils.IntMap<V>)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<V> com.badlogic.gdx.utils.IntMap$Values.iterator()"""
        return 'Iterator'.__wrap(super(Values, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Json$Serializer
from builtins import type
import com.badlogic.gdx.utils.Json as __Json_Serializer
__Serializer = __Json_Serializer.Serializer
from abc import abstractmethod, ABC
 
class Serializer(ABC):
    """com.badlogic.gdx.utils.Json.Serializer"""
 
    @staticmethod
    def __wrap(java_value: __Serializer) -> 'Serializer':
        return Serializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Serializer):
        """
        Dynamic initializer for Serializer.
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
    def read(self, arg0: 'Json', arg1: 'JsonValue', arg2: 'Class'):
        """public abstract T com.badlogic.gdx.utils.Json$Serializer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue,java.lang.Class)"""
        pass

    @abstractmethod
    def write(self, arg0: 'Json', arg1: object, arg2: 'Class'):
        """public abstract void com.badlogic.gdx.utils.Json$Serializer.write(com.badlogic.gdx.utils.Json,T,java.lang.Class)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.utils.XmlReader
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.XmlReader as __XmlReader_Element
__Element = __XmlReader_Element.Element
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.XmlReader as __XmlReader
__XmlReader = __XmlReader
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class XmlReader():
    """com.badlogic.gdx.utils.XmlReader"""
 
    @staticmethod
    def __wrap(java_value: __XmlReader) -> 'XmlReader':
        return XmlReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __XmlReader):
        """
        Dynamic initializer for XmlReader.
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
    def parse(self, arg0: 'FileHandle') -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader.parse(com.badlogic.gdx.files.FileHandle)"""
        return 'Element'.__wrap(super(__XmlReader, self).parse(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def parse(self, arg0: 'char', arg1: int, arg2: int) -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader.parse(char[],int,int)"""
        return 'Element'.__wrap(super(__XmlReader, self).parse(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

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
        """public com.badlogic.gdx.utils.XmlReader()"""
        val = __XmlReader()
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

    @overload
    def parse(self, arg0: 'InputStream') -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader.parse(java.io.InputStream)"""
        return 'Element'.__wrap(super(__XmlReader, self).parse(arg0))

    @overload
    def parse(self, arg0: str) -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader.parse(java.lang.String)"""
        return 'Element'.__wrap(super(__XmlReader, self).parse(arg0))

    @overload
    def parse(self, arg0: 'Reader') -> 'Element':
        """public com.badlogic.gdx.utils.XmlReader$Element com.badlogic.gdx.utils.XmlReader.parse(java.io.Reader)"""
        return 'Element'.__wrap(super(__XmlReader, self).parse(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.XmlReader()"""
        val = __XmlReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.Bits
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.utils.Bits as __Bits
__Bits = __Bits
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Bits():
    """com.badlogic.gdx.utils.Bits"""
 
    @staticmethod
    def __wrap(java_value: __Bits) -> 'Bits':
        return Bits(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bits):
        """
        Dynamic initializer for Bits.
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
        """public int com.badlogic.gdx.utils.Bits.hashCode()"""
        return int.__wrap(super(Bits, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Bits()"""
        val = __Bits()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def flip(self, arg0: int):
        """public void com.badlogic.gdx.utils.Bits.flip(int)"""
        super(__Bits, self).flip(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Bits'):
        """public com.badlogic.gdx.utils.Bits(com.badlogic.gdx.utils.Bits)"""
        val = __Bits(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.Bits(int)"""
        val = __Bits(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAndClear(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.Bits.getAndClear(int)"""
        return bool.__wrap(super(__Bits, self).getAndClear(__int.valueOf(arg0)))

    @overload
    def nextClearBit(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.Bits.nextClearBit(int)"""
        return int.__wrap(super(__Bits, self).nextClearBit(__int.valueOf(arg0)))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Bits.clear()"""
        super(Bits, self).clear()

    @overload
    def containsAll(self, arg0: 'Bits') -> bool:
        """public boolean com.badlogic.gdx.utils.Bits.containsAll(com.badlogic.gdx.utils.Bits)"""
        return bool.__wrap(super(__Bits, self).containsAll(arg0))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Bits.isEmpty()"""
        return bool.__wrap(super(Bits, self).isEmpty())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Bits.equals(java.lang.Object)"""
        return bool.__wrap(super(__Bits, self).equals(arg0))

    @overload
    def length(self) -> int:
        """public int com.badlogic.gdx.utils.Bits.length()"""
        return int.__wrap(super(Bits, self).length())

    @overload
    def xor(self, arg0: 'Bits'):
        """public void com.badlogic.gdx.utils.Bits.xor(com.badlogic.gdx.utils.Bits)"""
        super(__Bits, self).xor(arg0)

    @overload
    def or(self, arg0: 'Bits'):
        """public void com.badlogic.gdx.utils.Bits.or(com.badlogic.gdx.utils.Bits)"""
        super(__Bits, self).or(arg0)

    @overload
    def and(self, arg0: 'Bits'):
        """public void com.badlogic.gdx.utils.Bits.and(com.badlogic.gdx.utils.Bits)"""
        super(__Bits, self).and(arg0)

    @overload
    def intersects(self, arg0: 'Bits') -> bool:
        """public boolean com.badlogic.gdx.utils.Bits.intersects(com.badlogic.gdx.utils.Bits)"""
        return bool.__wrap(super(__Bits, self).intersects(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Bits.notEmpty()"""
        return bool.__wrap(super(Bits, self).notEmpty())

    @overload
    def nextSetBit(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.Bits.nextSetBit(int)"""
        return int.__wrap(super(__Bits, self).nextSetBit(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Bits()"""
        val = __Bits()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def andNot(self, arg0: 'Bits'):
        """public void com.badlogic.gdx.utils.Bits.andNot(com.badlogic.gdx.utils.Bits)"""
        super(__Bits, self).andNot(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.Bits.clear(int)"""
        super(__Bits, self).clear(__int.valueOf(arg0))

    @overload
    def numBits(self) -> int:
        """public int com.badlogic.gdx.utils.Bits.numBits()"""
        return int.__wrap(super(Bits, self).numBits())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int):
        """public void com.badlogic.gdx.utils.Bits.set(int)"""
        super(__Bits, self).set(__int.valueOf(arg0))

    @overload
    def getAndSet(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.Bits.getAndSet(int)"""
        return bool.__wrap(super(__Bits, self).getAndSet(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.Bits.get(int)"""
        return bool.__wrap(super(__Bits, self).get(__int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectLongMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap_Keys
__Keys = __ObjectLongMap_Keys.Keys
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap_Values
__Values = __ObjectLongMap_Values.Values
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap
__ObjectLongMap = __ObjectLongMap
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap_Entries
__Entries = __ObjectLongMap_Entries.Entries
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ObjectLongMap():
    """com.badlogic.gdx.utils.ObjectLongMap"""
 
    @staticmethod
    def __wrap(java_value: __ObjectLongMap) -> 'ObjectLongMap':
        return ObjectLongMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectLongMap):
        """
        Dynamic initializer for ObjectLongMap.
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
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectLongMap$Keys<K> com.badlogic.gdx.utils.ObjectLongMap.keys()"""
        return 'Keys'.__wrap(super(ObjectLongMap, self).keys())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.ObjectLongMap(int,float)"""
        val = __ObjectLongMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectLongMap.containsKey(K)"""
        return bool.__wrap(super(__ObjectLongMap, self).containsKey(arg0))

    @overload
    def getAndIncrement(self, arg0: object, arg1: int, arg2: int) -> int:
        """public long com.badlogic.gdx.utils.ObjectLongMap.getAndIncrement(K,long,long)"""
        return int.__wrap(super(__ObjectLongMap, self).getAndIncrement(arg0, __long.valueOf(arg1), __long.valueOf(arg2)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ObjectLongMap()"""
        val = __ObjectLongMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectLongMap$Entries<K> com.badlogic.gdx.utils.ObjectLongMap.iterator()"""
        return 'Entries'.__wrap(super(ObjectLongMap, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectLongMap.notEmpty()"""
        return bool.__wrap(super(ObjectLongMap, self).notEmpty())

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectLongMap$Values com.badlogic.gdx.utils.ObjectLongMap.values()"""
        return 'Values'.__wrap(super(ObjectLongMap, self).values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectLongMap.toString()"""
        return str.__wrap(super(ObjectLongMap, self).toString())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectLongMap.isEmpty()"""
        return bool.__wrap(super(ObjectLongMap, self).isEmpty())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.ObjectLongMap(int)"""
        val = __ObjectLongMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectLongMap.ensureCapacity(int)"""
        super(__ObjectLongMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def put(self, arg0: object, arg1: int):
        """public void com.badlogic.gdx.utils.ObjectLongMap.put(K,long)"""
        super(__ObjectLongMap, self).put(arg0, __long.valueOf(arg1))

    @overload
    def findKey(self, arg0: int) -> object:
        """public K com.badlogic.gdx.utils.ObjectLongMap.findKey(long)"""
        return object.__wrap(super(__ObjectLongMap, self).findKey(__long.valueOf(arg0)))

    @overload
    def remove(self, arg0: object, arg1: int) -> int:
        """public long com.badlogic.gdx.utils.ObjectLongMap.remove(K,long)"""
        return int.__wrap(super(__ObjectLongMap, self).remove(arg0, __long.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectLongMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectLongMap, self).equals(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ObjectLongMap.clear()"""
        super(ObjectLongMap, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ObjectLongMap.hashCode()"""
        return int.__wrap(super(ObjectLongMap, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'ObjectLongMap'):
        """public com.badlogic.gdx.utils.ObjectLongMap(com.badlogic.gdx.utils.ObjectLongMap<? extends K>)"""
        val = __ObjectLongMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ObjectLongMap.toString(java.lang.String)"""
        return str.__wrap(super(__ObjectLongMap, self).toString(arg0))

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectLongMap.clear(int)"""
        super(__ObjectLongMap, self).clear(__int.valueOf(arg0))

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectLongMap.shrink(int)"""
        super(__ObjectLongMap, self).shrink(__int.valueOf(arg0))

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectLongMap$Entries<K> com.badlogic.gdx.utils.ObjectLongMap.entries()"""
        return 'Entries'.__wrap(super(ObjectLongMap, self).entries())

    @overload
    def putAll(self, arg0: 'ObjectLongMap'):
        """public void com.badlogic.gdx.utils.ObjectLongMap.putAll(com.badlogic.gdx.utils.ObjectLongMap<? extends K>)"""
        super(__ObjectLongMap, self).putAll(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsValue(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectLongMap.containsValue(long)"""
        return bool.__wrap(super(__ObjectLongMap, self).containsValue(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ObjectLongMap()"""
        val = __ObjectLongMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: int, arg2: int) -> int:
        """public long com.badlogic.gdx.utils.ObjectLongMap.put(K,long,long)"""
        return int.__wrap(super(__ObjectLongMap, self).put(arg0, __long.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def get(self, arg0: object, arg1: int) -> int:
        """public long com.badlogic.gdx.utils.ObjectLongMap.get(K,long)"""
        return int.__wrap(super(__ObjectLongMap, self).get(arg0, __long.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.utils.I18NBundle
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.Locale as Locale
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
from builtins import object
import com.badlogic.gdx.utils.I18NBundle as __I18NBundle
__I18NBundle = __I18NBundle
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import bool
from builtins import int
 
class I18NBundle():
    """com.badlogic.gdx.utils.I18NBundle"""
 
    @staticmethod
    def __wrap(java_value: __I18NBundle) -> 'I18NBundle':
        return I18NBundle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __I18NBundle):
        """
        Dynamic initializer for I18NBundle.
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
    def createBundle(arg0: 'FileHandle', arg1: 'Locale', arg2: str) -> 'I18NBundle':
        """public static com.badlogic.gdx.utils.I18NBundle com.badlogic.gdx.utils.I18NBundle.createBundle(com.badlogic.gdx.files.FileHandle,java.util.Locale,java.lang.String)"""
        return I18NBundle.__wrap(__I18NBundle.createBundle(arg0, arg1, arg2))

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
    def createBundle(arg0: 'FileHandle', arg1: str) -> 'I18NBundle':
        """public static com.badlogic.gdx.utils.I18NBundle com.badlogic.gdx.utils.I18NBundle.createBundle(com.badlogic.gdx.files.FileHandle,java.lang.String)"""
        return I18NBundle.__wrap(__I18NBundle.createBundle(arg0, arg1))

    @overload
    def get(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.I18NBundle.get(java.lang.String)"""
        return str.__wrap(super(__I18NBundle, self).get(arg0))

    @overload
    def format(self, arg0: str, *arg1: object) -> str:
        """public java.lang.String com.badlogic.gdx.utils.I18NBundle.format(java.lang.String,java.lang.Object...)"""
        return str.__wrap(super(__I18NBundle, self).format(arg0, arg1))

    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale com.badlogic.gdx.utils.I18NBundle.getLocale()"""
        return 'Locale'.__wrap(super(I18NBundle, self).getLocale())

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
    def setSimpleFormatter(arg0: bool):
        """public static void com.badlogic.gdx.utils.I18NBundle.setSimpleFormatter(boolean)"""
        __I18NBundle.setSimpleFormatter(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.I18NBundle()"""
        val = __I18NBundle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.I18NBundle()"""
        val = __I18NBundle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getExceptionOnMissingKey() -> bool:
        """public static boolean com.badlogic.gdx.utils.I18NBundle.getExceptionOnMissingKey()"""
        return bool.__wrap(__I18NBundle.getExceptionOnMissingKey())

    @staticmethod
    @overload
    def getSimpleFormatter() -> bool:
        """public static boolean com.badlogic.gdx.utils.I18NBundle.getSimpleFormatter()"""
        return bool.__wrap(__I18NBundle.getSimpleFormatter())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def keys(self) -> 'Set':
        """public java.util.Set<java.lang.String> com.badlogic.gdx.utils.I18NBundle.keys()"""
        return 'Set'.__wrap(super(I18NBundle, self).keys())

    @overload
    def debug(self, arg0: str):
        """public void com.badlogic.gdx.utils.I18NBundle.debug(java.lang.String)"""
        super(__I18NBundle, self).debug(arg0)

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
    def setExceptionOnMissingKey(arg0: bool):
        """public static void com.badlogic.gdx.utils.I18NBundle.setExceptionOnMissingKey(boolean)"""
        __I18NBundle.setExceptionOnMissingKey(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def createBundle(arg0: 'FileHandle', arg1: 'Locale') -> 'I18NBundle':
        """public static com.badlogic.gdx.utils.I18NBundle com.badlogic.gdx.utils.I18NBundle.createBundle(com.badlogic.gdx.files.FileHandle,java.util.Locale)"""
        return I18NBundle.__wrap(__I18NBundle.createBundle(arg0, arg1))

    @staticmethod
    @overload
    def createBundle(arg0: 'FileHandle') -> 'I18NBundle':
        """public static com.badlogic.gdx.utils.I18NBundle com.badlogic.gdx.utils.I18NBundle.createBundle(com.badlogic.gdx.files.FileHandle)"""
        return I18NBundle.__wrap(__I18NBundle.createBundle(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntIntMap$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap_Keys
__Keys = __IntIntMap_Keys.Keys
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.IntArray as __IntArray
__IntArray = __IntArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Keys():
    """com.badlogic.gdx.utils.IntIntMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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
    def toArray(self) -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntIntMap$Keys.toArray()"""
        return 'IntArray'.__wrap(super(Keys, self).toArray())

    @overload
    def toArray(self, arg0: 'IntArray') -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntIntMap$Keys.toArray(com.badlogic.gdx.utils.IntArray)"""
        return 'IntArray'.__wrap(super(__Keys, self).toArray(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def next(self) -> int:
        """public int com.badlogic.gdx.utils.IntIntMap$Keys.next()"""
        return int.__wrap(super(Keys, self).next())

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

    @overload
    def __init__(self, arg0: 'IntIntMap'):
        """public com.badlogic.gdx.utils.IntIntMap$Keys(com.badlogic.gdx.utils.IntIntMap)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.UBJsonReader
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.utils.UBJsonReader as __UBJsonReader
__UBJsonReader = __UBJsonReader
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.JsonValue as __JsonValue
__JsonValue = __JsonValue
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
import java.io.DataInputStream as DataInputStream
from builtins import int
 
class UBJsonReader():
    """com.badlogic.gdx.utils.UBJsonReader"""
 
    @staticmethod
    def __wrap(java_value: __UBJsonReader) -> 'UBJsonReader':
        return UBJsonReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UBJsonReader):
        """
        Dynamic initializer for UBJsonReader.
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
        """public com.badlogic.gdx.utils.UBJsonReader()"""
        val = __UBJsonReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.UBJsonReader()"""
        val = __UBJsonReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def parse(self, arg0: 'FileHandle') -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.UBJsonReader.parse(com.badlogic.gdx.files.FileHandle)"""
        return 'JsonValue'.__wrap(super(__UBJsonReader, self).parse(arg0))

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
    def parse(self, arg0: 'DataInputStream') -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.UBJsonReader.parse(java.io.DataInputStream) throws java.io.IOException"""
        return 'JsonValue'.__wrap(super(__UBJsonReader, self).parse(arg0))

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
    def parse(self, arg0: 'InputStream') -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.UBJsonReader.parse(java.io.InputStream)"""
        return 'JsonValue'.__wrap(super(__UBJsonReader, self).parse(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.OrderedMap$OrderedMapEntries
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entry
__Entry = __ObjectMap_Entry.Entry
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap_Entries
__Entries = __ObjectMap_Entries.Entries
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.OrderedMap as __OrderedMap_OrderedMapEntries
__OrderedMapEntries = __OrderedMap_OrderedMapEntries.OrderedMapEntries
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class OrderedMapEntries():
    """com.badlogic.gdx.utils.OrderedMap.OrderedMapEntries"""
 
    @staticmethod
    def __wrap(java_value: __OrderedMapEntries) -> 'OrderedMapEntries':
        return OrderedMapEntries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedMapEntries):
        """
        Dynamic initializer for OrderedMapEntries.
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
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.ObjectMap$Entry com.badlogic.gdx.utils.OrderedMap$OrderedMapEntries.next()"""
        return 'Entry'.__wrap(super(OrderedMapEntries, self).next())

    @override
    @overload
    def iterator(self) -> 'Entries':
        """public com.badlogic.gdx.utils.ObjectMap$Entries<K, V> com.badlogic.gdx.utils.ObjectMap$Entries.iterator()"""
        return 'Entries'.__wrap(super(Entries, self).iterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'OrderedMap'):
        """public com.badlogic.gdx.utils.OrderedMap$OrderedMapEntries(com.badlogic.gdx.utils.OrderedMap<K, V>)"""
        val = __OrderedMapEntries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.OrderedMap$OrderedMapEntries.remove()"""
        super(OrderedMapEntries, self).remove()

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
    def reset(self):
        """public void com.badlogic.gdx.utils.OrderedMap$OrderedMapEntries.reset()"""
        super(OrderedMapEntries, self).reset()

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectFloatMap$Values
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.utils.FloatArray as __FloatArray
__FloatArray = __FloatArray
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.ObjectFloatMap as __ObjectFloatMap_Values
__Values = __ObjectFloatMap_Values.Values
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Values():
    """com.badlogic.gdx.utils.ObjectFloatMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def __init__(self, arg0: 'ObjectFloatMap'):
        """public com.badlogic.gdx.utils.ObjectFloatMap$Values(com.badlogic.gdx.utils.ObjectFloatMap<?>)"""
        val = __Values(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectFloatMap$Values.hasNext()"""
        return bool.__wrap(super(Values, self).hasNext())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def next(self) -> float:
        """public float com.badlogic.gdx.utils.ObjectFloatMap$Values.next()"""
        return float.__wrap(super(Values, self).next())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def iterator(self) -> 'Values':
        """public com.badlogic.gdx.utils.ObjectFloatMap$Values com.badlogic.gdx.utils.ObjectFloatMap$Values.iterator()"""
        return 'Values'.__wrap(super(Values, self).iterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toArray(self, arg0: 'FloatArray') -> 'FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.utils.ObjectFloatMap$Values.toArray(com.badlogic.gdx.utils.FloatArray)"""
        return 'FloatArray'.__wrap(super(__Values, self).toArray(arg0))

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
    def toArray(self) -> 'FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.utils.ObjectFloatMap$Values.toArray()"""
        return 'FloatArray'.__wrap(super(Values, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.Sort
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Sort as __Sort
__Sort = __Sort
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Sort():
    """com.badlogic.gdx.utils.Sort"""
 
    @staticmethod
    def __wrap(java_value: __Sort) -> 'Sort':
        return Sort(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Sort):
        """
        Dynamic initializer for Sort.
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
    def sort(self, arg0: 'Array'):
        """public <T extends java.lang.Comparable> void com.badlogic.gdx.utils.Sort.sort(com.badlogic.gdx.utils.Array<T>)"""
        super(__Sort, self).sort(arg0)

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
    def instance() -> 'Sort':
        """public static com.badlogic.gdx.utils.Sort com.badlogic.gdx.utils.Sort.instance()"""
        return Sort.__wrap(__Sort.instance())

    @overload
    def sort(self, arg0: 'Object', arg1: 'Comparator', arg2: int, arg3: int):
        """public <T> void com.badlogic.gdx.utils.Sort.sort(T[],java.util.Comparator<? super T>,int,int)"""
        super(__Sort, self).sort(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Sort()"""
        val = __Sort()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def sort(self, arg0: 'Object'):
        """public void com.badlogic.gdx.utils.Sort.sort(java.lang.Object[])"""
        super(__Sort, self).sort(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def sort(self, arg0: 'Array', arg1: 'Comparator'):
        """public <T> void com.badlogic.gdx.utils.Sort.sort(com.badlogic.gdx.utils.Array<T>,java.util.Comparator<? super T>)"""
        super(__Sort, self).sort(arg0, arg1)

    @overload
    def sort(self, arg0: 'Object', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.Sort.sort(java.lang.Object[],int,int)"""
        super(__Sort, self).sort(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Sort()"""
        val = __Sort()
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

    @overload
    def sort(self, arg0: 'Object', arg1: 'Comparator'):
        """public <T> void com.badlogic.gdx.utils.Sort.sort(T[],java.util.Comparator<? super T>)"""
        super(__Sort, self).sort(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.utils.NumberUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import com.badlogic.gdx.utils.NumberUtils as __NumberUtils
__NumberUtils = __NumberUtils
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class NumberUtils():
    """com.badlogic.gdx.utils.NumberUtils"""
 
    @staticmethod
    def __wrap(java_value: __NumberUtils) -> 'NumberUtils':
        return NumberUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NumberUtils):
        """
        Dynamic initializer for NumberUtils.
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
    def doubleToLongBits(arg0: float) -> int:
        """public static long com.badlogic.gdx.utils.NumberUtils.doubleToLongBits(double)"""
        return int.__wrap(__NumberUtils.doubleToLongBits(__double.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def intBitsToFloat(arg0: int) -> float:
        """public static float com.badlogic.gdx.utils.NumberUtils.intBitsToFloat(int)"""
        return float.__wrap(__NumberUtils.intBitsToFloat(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def floatToIntBits(arg0: float) -> int:
        """public static int com.badlogic.gdx.utils.NumberUtils.floatToIntBits(float)"""
        return int.__wrap(__NumberUtils.floatToIntBits(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def floatToIntColor(arg0: float) -> int:
        """public static int com.badlogic.gdx.utils.NumberUtils.floatToIntColor(float)"""
        return int.__wrap(__NumberUtils.floatToIntColor(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.NumberUtils()"""
        val = __NumberUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.NumberUtils()"""
        val = __NumberUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def longBitsToDouble(arg0: int) -> float:
        """public static double com.badlogic.gdx.utils.NumberUtils.longBitsToDouble(long)"""
        return float.__wrap(__NumberUtils.longBitsToDouble(__long.valueOf(arg0)))

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
    def floatToRawIntBits(arg0: float) -> int:
        """public static int com.badlogic.gdx.utils.NumberUtils.floatToRawIntBits(float)"""
        return int.__wrap(__NumberUtils.floatToRawIntBits(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def intToFloatColor(arg0: int) -> float:
        """public static float com.badlogic.gdx.utils.NumberUtils.intToFloatColor(int)"""
        return float.__wrap(__NumberUtils.intToFloatColor(__int.valueOf(arg0)))

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
 
 
# CLASS: com.badlogic.gdx.utils.GdxNativesLoader
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
import com.badlogic.gdx.utils.GdxNativesLoader as __GdxNativesLoader
__GdxNativesLoader = __GdxNativesLoader
from builtins import bool
from builtins import int
 
class GdxNativesLoader():
    """com.badlogic.gdx.utils.GdxNativesLoader"""
 
    @staticmethod
    def __wrap(java_value: __GdxNativesLoader) -> 'GdxNativesLoader':
        return GdxNativesLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GdxNativesLoader):
        """
        Dynamic initializer for GdxNativesLoader.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.GdxNativesLoader()"""
        val = __GdxNativesLoader()
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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.GdxNativesLoader()"""
        val = __GdxNativesLoader()
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

        @staticmethod
        @overload
        def load():
            """public static synchronized void com.badlogic.gdx.utils.GdxNativesLoader.load()"""
            __GdxNativesLoader.load() 
 
 
# CLASS: com.badlogic.gdx.utils.ShortArray
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Short as __short
import com.badlogic.gdx.utils.ShortArray as __ShortArray
__ShortArray = __ShortArray
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ShortArray():
    """com.badlogic.gdx.utils.ShortArray"""
 
    @staticmethod
    def __wrap(java_value: __ShortArray) -> 'ShortArray':
        return ShortArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShortArray):
        """
        Dynamic initializer for ShortArray.
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
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ShortArray.insertRange(int,int)"""
        super(__ShortArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ShortArray.removeRange(int,int)"""
        super(__ShortArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mul(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ShortArray.mul(int,short)"""
        super(__ShortArray, self).mul(__int.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ShortArray()"""
        val = __ShortArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def insert(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ShortArray.insert(int,short)"""
        super(__ShortArray, self).insert(__int.valueOf(arg0), __short.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ShortArray'):
        """public com.badlogic.gdx.utils.ShortArray(com.badlogic.gdx.utils.ShortArray)"""
        val = __ShortArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def shrink(self) -> List[int]:
        """public short[] com.badlogic.gdx.utils.ShortArray.shrink()"""
        return List[int].__wrap(super(ShortArray, self).shrink())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ShortArray.toString()"""
        return str.__wrap(super(ShortArray, self).toString())

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.ShortArray.reverse()"""
        super(ShortArray, self).reverse()

    @overload
    def toArray(self) -> List[int]:
        """public short[] com.badlogic.gdx.utils.ShortArray.toArray()"""
        return List[int].__wrap(super(ShortArray, self).toArray())

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.ShortArray(boolean,int)"""
        val = __ShortArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ShortArray.add(short,short,short)"""
        super(__ShortArray, self).add(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ShortArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__ShortArray, self).equals(arg0))

    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ShortArray.swap(int,int)"""
        super(__ShortArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addAll(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ShortArray.addAll(short[],int,int)"""
        super(__ShortArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def add(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ShortArray.add(short,short)"""
        super(__ShortArray, self).add(__short.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def with(*arg0: int) -> 'ShortArray':
        """public static com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.utils.ShortArray.with(short...)"""
        return ShortArray.__wrap(__ShortArray.with(arg0))

    @overload
    def addAll(self, arg0: 'ShortArray', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ShortArray.addAll(com.badlogic.gdx.utils.ShortArray,int,int)"""
        super(__ShortArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ShortArray.hashCode()"""
        return int.__wrap(super(ShortArray, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def peek(self) -> int:
        """public short com.badlogic.gdx.utils.ShortArray.peek()"""
        return int.__wrap(super(ShortArray, self).peek())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.ShortArray.truncate(int)"""
        super(__ShortArray, self).truncate(__int.valueOf(arg0))

    @overload
    def first(self) -> int:
        """public short com.badlogic.gdx.utils.ShortArray.first()"""
        return int.__wrap(super(ShortArray, self).first())

    @overload
    def incr(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ShortArray.incr(int,short)"""
        super(__ShortArray, self).incr(__int.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.ShortArray(int)"""
        val = __ShortArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setSize(self, arg0: int) -> List[int]:
        """public short[] com.badlogic.gdx.utils.ShortArray.setSize(int)"""
        return List[int].__wrap(super(__ShortArray, self).setSize(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> int:
        """public short com.badlogic.gdx.utils.ShortArray.get(int)"""
        return int.__wrap(super(__ShortArray, self).get(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.ShortArray()"""
        val = __ShortArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def indexOf(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.ShortArray.indexOf(short)"""
        return int.__wrap(super(__ShortArray, self).indexOf(__short.valueOf(arg0)))

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.ShortArray.shuffle()"""
        super(ShortArray, self).shuffle()

    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.ShortArray.sort()"""
        super(ShortArray, self).sort()

    @overload
    def pop(self) -> int:
        """public short com.badlogic.gdx.utils.ShortArray.pop()"""
        return int.__wrap(super(ShortArray, self).pop())

    @overload
    def add(self, arg0: int):
        """public void com.badlogic.gdx.utils.ShortArray.add(int)"""
        super(__ShortArray, self).add(__int.valueOf(arg0))

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ShortArray.notEmpty()"""
        return bool.__wrap(super(ShortArray, self).notEmpty())

    @overload
    def removeIndex(self, arg0: int) -> int:
        """public short com.badlogic.gdx.utils.ShortArray.removeIndex(int)"""
        return int.__wrap(super(__ShortArray, self).removeIndex(__int.valueOf(arg0)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ShortArray.isEmpty()"""
        return bool.__wrap(super(ShortArray, self).isEmpty())

    @overload
    def addAll(self, arg0: 'ShortArray'):
        """public void com.badlogic.gdx.utils.ShortArray.addAll(com.badlogic.gdx.utils.ShortArray)"""
        super(__ShortArray, self).addAll(arg0)

    @overload
    def contains(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.ShortArray.contains(short)"""
        return bool.__wrap(super(__ShortArray, self).contains(__short.valueOf(arg0)))

    @overload
    def random(self) -> int:
        """public short com.badlogic.gdx.utils.ShortArray.random()"""
        return int.__wrap(super(ShortArray, self).random())

    @overload
    def __init__(self, arg0: bool, arg1: 'short', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.ShortArray(boolean,short[],int,int)"""
        val = __ShortArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.ShortArray.lastIndexOf(char)"""
        return int.__wrap(super(__ShortArray, self).lastIndexOf(__char.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.ShortArray.add(short,short,short,short)"""
        super(__ShortArray, self).add(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def ensureCapacity(self, arg0: int) -> List[int]:
        """public short[] com.badlogic.gdx.utils.ShortArray.ensureCapacity(int)"""
        return List[int].__wrap(super(__ShortArray, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def removeValue(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.ShortArray.removeValue(short)"""
        return bool.__wrap(super(__ShortArray, self).removeValue(__short.valueOf(arg0)))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.ShortArray.toString(java.lang.String)"""
        return str.__wrap(super(__ShortArray, self).toString(arg0))

    @overload
    def incr(self, arg0: int):
        """public void com.badlogic.gdx.utils.ShortArray.incr(short)"""
        super(__ShortArray, self).incr(__short.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.ShortArray.set(int,short)"""
        super(__ShortArray, self).set(__int.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def removeAll(self, arg0: 'ShortArray') -> bool:
        """public boolean com.badlogic.gdx.utils.ShortArray.removeAll(com.badlogic.gdx.utils.ShortArray)"""
        return bool.__wrap(super(__ShortArray, self).removeAll(arg0))

    @overload
    def add(self, arg0: int):
        """public void com.badlogic.gdx.utils.ShortArray.add(short)"""
        super(__ShortArray, self).add(__short.valueOf(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.ShortArray.clear()"""
        super(ShortArray, self).clear()

    @overload
    def mul(self, arg0: int):
        """public void com.badlogic.gdx.utils.ShortArray.mul(short)"""
        super(__ShortArray, self).mul(__short.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'short'):
        """public com.badlogic.gdx.utils.ShortArray(short[])"""
        val = __ShortArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAll(self, *arg0: int):
        """public void com.badlogic.gdx.utils.ShortArray.addAll(short...)"""
        super(__ShortArray, self).addAll(arg0) 
 
 
# CLASS: com.badlogic.gdx.utils.ScreenUtils
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.ScreenUtils as __ScreenUtils
__ScreenUtils = __ScreenUtils
from typing import List
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ScreenUtils():
    """com.badlogic.gdx.utils.ScreenUtils"""
 
    @staticmethod
    def __wrap(java_value: __ScreenUtils) -> 'ScreenUtils':
        return ScreenUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScreenUtils):
        """
        Dynamic initializer for ScreenUtils.
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
    def __init__(self):
        """public com.badlogic.gdx.utils.ScreenUtils()"""
        val = __ScreenUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def clear(arg0: 'Color'):
        """public static void com.badlogic.gdx.utils.ScreenUtils.clear(com.badlogic.gdx.graphics.Color)"""
        __ScreenUtils.clear(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getFrameBufferTexture(arg0: int, arg1: int, arg2: int, arg3: int) -> 'g2d.TextureRegion':
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.utils.ScreenUtils.getFrameBufferTexture(int,int,int,int)"""
        return g2d.TextureRegion.__wrap(__ScreenUtils.getFrameBufferTexture(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getFrameBufferPixmap(arg0: int, arg1: int, arg2: int, arg3: int) -> 'graphics.Pixmap':
        """public static com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.utils.ScreenUtils.getFrameBufferPixmap(int,int,int,int)"""
        return graphics.Pixmap.__wrap(__ScreenUtils.getFrameBufferPixmap(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def clear(arg0: float, arg1: float, arg2: float, arg3: float, arg4: bool):
        """public static void com.badlogic.gdx.utils.ScreenUtils.clear(float,float,float,float,boolean)"""
        __ScreenUtils.clear(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4))

    @staticmethod
    @overload
    def clear(arg0: 'Color', arg1: bool):
        """public static void com.badlogic.gdx.utils.ScreenUtils.clear(com.badlogic.gdx.graphics.Color,boolean)"""
        __ScreenUtils.clear(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def clear(arg0: float, arg1: float, arg2: float, arg3: float):
        """public static void com.badlogic.gdx.utils.ScreenUtils.clear(float,float,float,float)"""
        __ScreenUtils.clear(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getFrameBufferTexture() -> 'g2d.TextureRegion':
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.utils.ScreenUtils.getFrameBufferTexture()"""
        return g2d.TextureRegion.__wrap(__ScreenUtils.getFrameBufferTexture())

    @staticmethod
    @overload
    def getFrameBufferPixels(arg0: bool) -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.ScreenUtils.getFrameBufferPixels(boolean)"""
        return List[int].__wrap(__ScreenUtils.getFrameBufferPixels(__boolean.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.ScreenUtils()"""
        val = __ScreenUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getFrameBufferPixels(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool) -> List[int]:
        """public static byte[] com.badlogic.gdx.utils.ScreenUtils.getFrameBufferPixels(int,int,int,int,boolean)"""
        return List[int].__wrap(__ScreenUtils.getFrameBufferPixels(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4))) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectLongMap$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.ObjectLongMap as __ObjectLongMap_Keys
__Keys = __ObjectLongMap_Keys.Keys
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Keys():
    """com.badlogic.gdx.utils.ObjectLongMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectLongMap$Keys.hasNext()"""
        return bool.__wrap(super(Keys, self).hasNext())

    @override
    @overload
    def next(self) -> object:
        """public K com.badlogic.gdx.utils.ObjectLongMap$Keys.next()"""
        return object.__wrap(super(Keys, self).next())

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectLongMap$Keys.toArray(com.badlogic.gdx.utils.Array<K>)"""
        return 'Array'.__wrap(super(__Keys, self).toArray(arg0))

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
    def iterator(self) -> 'Keys':
        """public com.badlogic.gdx.utils.ObjectLongMap$Keys<K> com.badlogic.gdx.utils.ObjectLongMap$Keys.iterator()"""
        return 'Keys'.__wrap(super(Keys, self).iterator())

    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectLongMap$Keys.toArray()"""
        return 'Array'.__wrap(super(Keys, self).toArray())

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'ObjectLongMap'):
        """public com.badlogic.gdx.utils.ObjectLongMap$Keys(com.badlogic.gdx.utils.ObjectLongMap<K>)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.JsonValue
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.utils.JsonValue as __JsonValue
__JsonValue = __JsonValue
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
from builtins import bool
import com.badlogic.gdx.utils.JsonValue as __JsonValue_JsonIterator
__JsonIterator = __JsonValue_JsonIterator.JsonIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.utils.JsonValue as __JsonValue_ValueType
__ValueType = __JsonValue_ValueType.ValueType
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class JsonValue():
    """com.badlogic.gdx.utils.JsonValue"""
 
    @staticmethod
    def __wrap(java_value: __JsonValue) -> 'JsonValue':
        return JsonValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonValue):
        """
        Dynamic initializer for JsonValue.
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
    def prettyPrint(self, arg0: 'OutputType', arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.prettyPrint(com.badlogic.gdx.utils.JsonWriter$OutputType,int)"""
        return str.__wrap(super(__JsonValue, self).prettyPrint(arg0, __int.valueOf(arg1)))

    @overload
    def child(self) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.child()"""
        return 'JsonValue'.__wrap(super(JsonValue, self).child())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def asByte(self) -> int:
        """public byte com.badlogic.gdx.utils.JsonValue.asByte()"""
        return int.__wrap(super(JsonValue, self).asByte())

    @overload
    def getShort(self, arg0: int) -> int:
        """public short com.badlogic.gdx.utils.JsonValue.getShort(int)"""
        return int.__wrap(super(__JsonValue, self).getShort(__int.valueOf(arg0)))

    @overload
    def getBoolean(self, arg0: str, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.getBoolean(java.lang.String,boolean)"""
        return bool.__wrap(super(__JsonValue, self).getBoolean(arg0, __boolean.valueOf(arg1)))

    @overload
    def getDouble(self, arg0: int) -> float:
        """public double com.badlogic.gdx.utils.JsonValue.getDouble(int)"""
        return float.__wrap(super(__JsonValue, self).getDouble(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.toString()"""
        return str.__wrap(super(JsonValue, self).toString())

    @overload
    def asDouble(self) -> float:
        """public double com.badlogic.gdx.utils.JsonValue.asDouble()"""
        return float.__wrap(super(JsonValue, self).asDouble())

    @overload
    def setType(self, arg0: 'ValueType'):
        """public void com.badlogic.gdx.utils.JsonValue.setType(com.badlogic.gdx.utils.JsonValue$ValueType)"""
        super(__JsonValue, self).setType(arg0)

    @overload
    def set(self, arg0: float, arg1: str):
        """public void com.badlogic.gdx.utils.JsonValue.set(double,java.lang.String)"""
        super(__JsonValue, self).set(__double.valueOf(arg0), arg1)

    @overload
    def asByteArray(self) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.JsonValue.asByteArray()"""
        return List[int].__wrap(super(JsonValue, self).asByteArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def asIntArray(self) -> List[int]:
        """public int[] com.badlogic.gdx.utils.JsonValue.asIntArray()"""
        return List[int].__wrap(super(JsonValue, self).asIntArray())

    @overload
    def prettyPrint(self, arg0: 'PrettyPrintSettings') -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.prettyPrint(com.badlogic.gdx.utils.JsonValue$PrettyPrintSettings)"""
        return str.__wrap(super(__JsonValue, self).prettyPrint(arg0))

    @overload
    def asLongArray(self) -> List[int]:
        """public long[] com.badlogic.gdx.utils.JsonValue.asLongArray()"""
        return List[int].__wrap(super(JsonValue, self).asLongArray())

    @overload
    def addChild(self, arg0: str, arg1: 'JsonValue'):
        """public void com.badlogic.gdx.utils.JsonValue.addChild(java.lang.String,com.badlogic.gdx.utils.JsonValue)"""
        super(__JsonValue, self).addChild(arg0, arg1)

    @overload
    def parent(self) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.parent()"""
        return 'JsonValue'.__wrap(super(JsonValue, self).parent())

    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.name()"""
        return str.__wrap(super(JsonValue, self).name())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isObject(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isObject()"""
        return bool.__wrap(super(JsonValue, self).isObject())

    @overload
    def remove(self, arg0: str) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.remove(java.lang.String)"""
        return 'JsonValue'.__wrap(super(__JsonValue, self).remove(arg0))

    @overload
    def remove(self, arg0: int) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.remove(int)"""
        return 'JsonValue'.__wrap(super(__JsonValue, self).remove(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.JsonValue(long)"""
        val = __JsonValue(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'JsonIterator':
        """public com.badlogic.gdx.utils.JsonValue$JsonIterator com.badlogic.gdx.utils.JsonValue.iterator()"""
        return 'JsonIterator'.__wrap(super(JsonValue, self).iterator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def asStringArray(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.utils.JsonValue.asStringArray()"""
        return List[str].__wrap(super(JsonValue, self).asStringArray())

    @overload
    def __init__(self, arg0: int, arg1: str):
        """public com.badlogic.gdx.utils.JsonValue(long,java.lang.String)"""
        val = __JsonValue(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.get(int)"""
        return 'JsonValue'.__wrap(super(__JsonValue, self).get(__int.valueOf(arg0)))

    @overload
    def hasChild(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.hasChild(java.lang.String)"""
        return bool.__wrap(super(__JsonValue, self).hasChild(arg0))

    @overload
    def getByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.JsonValue.getByte(int)"""
        return int.__wrap(super(__JsonValue, self).getByte(__int.valueOf(arg0)))

    @overload
    def getByte(self, arg0: str, arg1: int) -> int:
        """public byte com.badlogic.gdx.utils.JsonValue.getByte(java.lang.String,byte)"""
        return int.__wrap(super(__JsonValue, self).getByte(arg0, __byte.valueOf(arg1)))

    @overload
    def getString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.getString(java.lang.String)"""
        return str.__wrap(super(__JsonValue, self).getString(arg0))

    @overload
    def getInt(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.JsonValue.getInt(int)"""
        return int.__wrap(super(__JsonValue, self).getInt(__int.valueOf(arg0)))

    @overload
    def isNumber(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isNumber()"""
        return bool.__wrap(super(JsonValue, self).isNumber())

    @overload
    def getFloat(self, arg0: str, arg1: float) -> float:
        """public float com.badlogic.gdx.utils.JsonValue.getFloat(java.lang.String,float)"""
        return float.__wrap(super(__JsonValue, self).getFloat(arg0, __float.valueOf(arg1)))

    @overload
    def getChar(self, arg0: int) -> str:
        """public char com.badlogic.gdx.utils.JsonValue.getChar(int)"""
        return str.__wrap(super(__JsonValue, self).getChar(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: str):
        """public com.badlogic.gdx.utils.JsonValue(double,java.lang.String)"""
        val = __JsonValue(__double.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def addChild(self, arg0: 'JsonValue'):
        """public void com.badlogic.gdx.utils.JsonValue.addChild(com.badlogic.gdx.utils.JsonValue)"""
        super(__JsonValue, self).addChild(arg0)

    @overload
    def prettyPrint(self, arg0: 'OutputType', arg1: 'Writer'):
        """public void com.badlogic.gdx.utils.JsonValue.prettyPrint(com.badlogic.gdx.utils.JsonWriter$OutputType,java.io.Writer) throws java.io.IOException"""
        super(__JsonValue, self).prettyPrint(arg0, arg1)

    @overload
    def require(self, arg0: int) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.require(int)"""
        return 'JsonValue'.__wrap(super(__JsonValue, self).require(__int.valueOf(arg0)))

    @overload
    def getByte(self, arg0: str) -> int:
        """public byte com.badlogic.gdx.utils.JsonValue.getByte(java.lang.String)"""
        return int.__wrap(super(__JsonValue, self).getByte(arg0))

    @overload
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.utils.JsonValue(boolean)"""
        val = __JsonValue(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setNext(self, arg0: 'JsonValue'):
        """public void com.badlogic.gdx.utils.JsonValue.setNext(com.badlogic.gdx.utils.JsonValue)"""
        super(__JsonValue, self).setNext(arg0)

    @overload
    def getBoolean(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.getBoolean(int)"""
        return bool.__wrap(super(__JsonValue, self).getBoolean(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.JsonValue(java.lang.String)"""
        val = __JsonValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def asInt(self) -> int:
        """public int com.badlogic.gdx.utils.JsonValue.asInt()"""
        return int.__wrap(super(JsonValue, self).asInt())

    @overload
    def type(self) -> 'ValueType':
        """public com.badlogic.gdx.utils.JsonValue$ValueType com.badlogic.gdx.utils.JsonValue.type()"""
        return 'ValueType'.__wrap(super(JsonValue, self).type())

    @overload
    def trace(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.trace()"""
        return str.__wrap(super(JsonValue, self).trace())

    @overload
    def prev(self) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.prev()"""
        return 'JsonValue'.__wrap(super(JsonValue, self).prev())

    @overload
    def get(self, arg0: str) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.get(java.lang.String)"""
        return 'JsonValue'.__wrap(super(__JsonValue, self).get(arg0))

    @overload
    def asChar(self) -> str:
        """public char com.badlogic.gdx.utils.JsonValue.asChar()"""
        return str.__wrap(super(JsonValue, self).asChar())

    @overload
    def getShort(self, arg0: str) -> int:
        """public short com.badlogic.gdx.utils.JsonValue.getShort(java.lang.String)"""
        return int.__wrap(super(__JsonValue, self).getShort(arg0))

    @overload
    def isString(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isString()"""
        return bool.__wrap(super(JsonValue, self).isString())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.notEmpty()"""
        return bool.__wrap(super(JsonValue, self).notEmpty())

    @overload
    def asFloat(self) -> float:
        """public float com.badlogic.gdx.utils.JsonValue.asFloat()"""
        return float.__wrap(super(JsonValue, self).asFloat())

    @overload
    def getChild(self, arg0: str) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.getChild(java.lang.String)"""
        return 'JsonValue'.__wrap(super(__JsonValue, self).getChild(arg0))

    @overload
    def asDoubleArray(self) -> List[float]:
        """public double[] com.badlogic.gdx.utils.JsonValue.asDoubleArray()"""
        return List[float].__wrap(super(JsonValue, self).asDoubleArray())

    @overload
    def __init__(self, arg0: 'ValueType'):
        """public com.badlogic.gdx.utils.JsonValue(com.badlogic.gdx.utils.JsonValue$ValueType)"""
        val = __JsonValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getString(self, arg0: str, arg1: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.getString(java.lang.String,java.lang.String)"""
        return str.__wrap(super(__JsonValue, self).getString(arg0, arg1))

    @overload
    def asBoolean(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.asBoolean()"""
        return bool.__wrap(super(JsonValue, self).asBoolean())

    @overload
    def getChar(self, arg0: str) -> str:
        """public char com.badlogic.gdx.utils.JsonValue.getChar(java.lang.String)"""
        return str.__wrap(super(__JsonValue, self).getChar(arg0))

    @overload
    def getLong(self, arg0: str, arg1: int) -> int:
        """public long com.badlogic.gdx.utils.JsonValue.getLong(java.lang.String,long)"""
        return int.__wrap(super(__JsonValue, self).getLong(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toJson(self, arg0: 'OutputType') -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.toJson(com.badlogic.gdx.utils.JsonWriter$OutputType)"""
        return str.__wrap(super(__JsonValue, self).toJson(arg0))

    @overload
    def asShort(self) -> int:
        """public short com.badlogic.gdx.utils.JsonValue.asShort()"""
        return int.__wrap(super(JsonValue, self).asShort())

    @overload
    def getFloat(self, arg0: int) -> float:
        """public float com.badlogic.gdx.utils.JsonValue.getFloat(int)"""
        return float.__wrap(super(__JsonValue, self).getFloat(__int.valueOf(arg0)))

    @overload
    def isNull(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isNull()"""
        return bool.__wrap(super(JsonValue, self).isNull())

    @overload
    def asLong(self) -> int:
        """public long com.badlogic.gdx.utils.JsonValue.asLong()"""
        return int.__wrap(super(JsonValue, self).asLong())

    @overload
    def isLong(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isLong()"""
        return bool.__wrap(super(JsonValue, self).isLong())

    @overload
    def isBoolean(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isBoolean()"""
        return bool.__wrap(super(JsonValue, self).isBoolean())

    @overload
    def asString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.asString()"""
        return str.__wrap(super(JsonValue, self).asString())

    @overload
    def asBooleanArray(self) -> List[bool]:
        """public boolean[] com.badlogic.gdx.utils.JsonValue.asBooleanArray()"""
        return List[bool].__wrap(super(JsonValue, self).asBooleanArray())

    @overload
    def has(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.has(java.lang.String)"""
        return bool.__wrap(super(__JsonValue, self).has(arg0))

    @overload
    def set(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.utils.JsonValue.set(long,java.lang.String)"""
        super(__JsonValue, self).set(__long.valueOf(arg0), arg1)

    @overload
    def require(self, arg0: str) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.require(java.lang.String)"""
        return 'JsonValue'.__wrap(super(__JsonValue, self).require(arg0))

    @overload
    def isValue(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isValue()"""
        return bool.__wrap(super(JsonValue, self).isValue())

    @overload
    def getFloat(self, arg0: str) -> float:
        """public float com.badlogic.gdx.utils.JsonValue.getFloat(java.lang.String)"""
        return float.__wrap(super(__JsonValue, self).getFloat(arg0))

    @overload
    def set(self, arg0: str):
        """public void com.badlogic.gdx.utils.JsonValue.set(java.lang.String)"""
        super(__JsonValue, self).set(arg0)

    @overload
    def asShortArray(self) -> List[int]:
        """public short[] com.badlogic.gdx.utils.JsonValue.asShortArray()"""
        return List[int].__wrap(super(JsonValue, self).asShortArray())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def setPrev(self, arg0: 'JsonValue'):
        """public void com.badlogic.gdx.utils.JsonValue.setPrev(com.badlogic.gdx.utils.JsonValue)"""
        super(__JsonValue, self).setPrev(arg0)

    @overload
    def asCharArray(self) -> List[str]:
        """public char[] com.badlogic.gdx.utils.JsonValue.asCharArray()"""
        return List[str].__wrap(super(JsonValue, self).asCharArray())

    @overload
    def isDouble(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isDouble()"""
        return bool.__wrap(super(JsonValue, self).isDouble())

    @overload
    def getShort(self, arg0: str, arg1: int) -> int:
        """public short com.badlogic.gdx.utils.JsonValue.getShort(java.lang.String,short)"""
        return int.__wrap(super(__JsonValue, self).getShort(arg0, __short.valueOf(arg1)))

    @overload
    def iterator(self, arg0: str) -> 'JsonIterator':
        """public com.badlogic.gdx.utils.JsonValue$JsonIterator com.badlogic.gdx.utils.JsonValue.iterator(java.lang.String)"""
        return 'JsonIterator'.__wrap(super(__JsonValue, self).iterator(arg0))

    @overload
    def getChar(self, arg0: str, arg1: str) -> str:
        """public char com.badlogic.gdx.utils.JsonValue.getChar(java.lang.String,char)"""
        return str.__wrap(super(__JsonValue, self).getChar(arg0, __char.valueOf(arg1)))

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.utils.JsonValue.size()"""
        return int.__wrap(super(JsonValue, self).size())

    @overload
    def getDouble(self, arg0: str, arg1: float) -> float:
        """public double com.badlogic.gdx.utils.JsonValue.getDouble(java.lang.String,double)"""
        return float.__wrap(super(__JsonValue, self).getDouble(arg0, __double.valueOf(arg1)))

    @overload
    def getLong(self, arg0: int) -> int:
        """public long com.badlogic.gdx.utils.JsonValue.getLong(int)"""
        return int.__wrap(super(__JsonValue, self).getLong(__int.valueOf(arg0)))

    @overload
    def getString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.utils.JsonValue.getString(int)"""
        return str.__wrap(super(__JsonValue, self).getString(__int.valueOf(arg0)))

    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.JsonValue.remove()"""
        super(JsonValue, self).remove()

    @overload
    def asFloatArray(self) -> List[float]:
        """public float[] com.badlogic.gdx.utils.JsonValue.asFloatArray()"""
        return List[float].__wrap(super(JsonValue, self).asFloatArray())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.utils.JsonValue.setName(java.lang.String)"""
        super(__JsonValue, self).setName(arg0)

    @overload
    def set(self, arg0: bool):
        """public void com.badlogic.gdx.utils.JsonValue.set(boolean)"""
        super(__JsonValue, self).set(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.utils.JsonValue(double)"""
        val = __JsonValue(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBoolean(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.getBoolean(java.lang.String)"""
        return bool.__wrap(super(__JsonValue, self).getBoolean(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isEmpty()"""
        return bool.__wrap(super(JsonValue, self).isEmpty())

    @overload
    def next(self) -> 'JsonValue':
        """public com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.JsonValue.next()"""
        return 'JsonValue'.__wrap(super(JsonValue, self).next())

    @overload
    def isArray(self) -> bool:
        """public boolean com.badlogic.gdx.utils.JsonValue.isArray()"""
        return bool.__wrap(super(JsonValue, self).isArray())

    @overload
    def getInt(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.JsonValue.getInt(java.lang.String)"""
        return int.__wrap(super(__JsonValue, self).getInt(arg0))

    @overload
    def getLong(self, arg0: str) -> int:
        """public long com.badlogic.gdx.utils.JsonValue.getLong(java.lang.String)"""
        return int.__wrap(super(__JsonValue, self).getLong(arg0))

    @overload
    def getDouble(self, arg0: str) -> float:
        """public double com.badlogic.gdx.utils.JsonValue.getDouble(java.lang.String)"""
        return float.__wrap(super(__JsonValue, self).getDouble(arg0))

    @overload
    def getInt(self, arg0: str, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.JsonValue.getInt(java.lang.String,int)"""
        return int.__wrap(super(__JsonValue, self).getInt(arg0, __int.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.utils.IntFloatMap$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.IntFloatMap as __IntFloatMap_Keys
__Keys = __IntFloatMap_Keys.Keys
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.IntArray as __IntArray
__IntArray = __IntArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Keys():
    """com.badlogic.gdx.utils.IntFloatMap.Keys"""
 
    @staticmethod
    def __wrap(java_value: __Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Keys):
        """
        Dynamic initializer for Keys.
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

    @overload
    def next(self) -> int:
        """public int com.badlogic.gdx.utils.IntFloatMap$Keys.next()"""
        return int.__wrap(super(Keys, self).next())

    @overload
    def __init__(self, arg0: 'IntFloatMap'):
        """public com.badlogic.gdx.utils.IntFloatMap$Keys(com.badlogic.gdx.utils.IntFloatMap)"""
        val = __Keys(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toArray(self, arg0: 'IntArray') -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntFloatMap$Keys.toArray(com.badlogic.gdx.utils.IntArray)"""
        return 'IntArray'.__wrap(super(__Keys, self).toArray(arg0))

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
    def toArray(self) -> 'IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.utils.IntFloatMap$Keys.toArray()"""
        return 'IntArray'.__wrap(super(Keys, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntMap$Entries
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.IntMap as __IntMap_Entry
__Entry = __IntMap_Entry.Entry
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.utils.IntMap as __IntMap_Entries
__Entries = __IntMap_Entries.Entries
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Entries():
    """com.badlogic.gdx.utils.IntMap.Entries"""
 
    @staticmethod
    def __wrap(java_value: __Entries) -> 'Entries':
        return Entries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entries):
        """
        Dynamic initializer for Entries.
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

    @overload
    def __init__(self, arg0: 'IntMap'):
        """public com.badlogic.gdx.utils.IntMap$Entries(com.badlogic.gdx.utils.IntMap)"""
        val = __Entries(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def next(self) -> 'Entry':
        """public com.badlogic.gdx.utils.IntMap$Entry<V> com.badlogic.gdx.utils.IntMap$Entries.next()"""
        return 'Entry'.__wrap(super(Entries, self).next())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntMap$Entries.hasNext()"""
        return bool.__wrap(super(Entries, self).hasNext())

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
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.IntMap$Entry<V>> com.badlogic.gdx.utils.IntMap$Entries.iterator()"""
        return 'Iterator'.__wrap(super(Entries, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.utils.ObjectSet as __ObjectSet_ObjectSetIterator
__ObjectSetIterator = __ObjectSet_ObjectSetIterator.ObjectSetIterator
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ObjectSetIterator():
    """com.badlogic.gdx.utils.ObjectSet.ObjectSetIterator"""
 
    @staticmethod
    def __wrap(java_value: __ObjectSetIterator) -> 'ObjectSetIterator':
        return ObjectSetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectSetIterator):
        """
        Dynamic initializer for ObjectSetIterator.
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
    def next(self) -> object:
        """public K com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.next()"""
        return object.__wrap(super(ObjectSetIterator, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.hasNext()"""
        return bool.__wrap(super(ObjectSetIterator, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def remove(self):
        """public void com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.remove()"""
        super(ObjectSetIterator, self).remove()

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
    def __init__(self, arg0: 'ObjectSet'):
        """public com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator(com.badlogic.gdx.utils.ObjectSet<K>)"""
        val = __ObjectSetIterator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def reset(self):
        """public void com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.reset()"""
        super(ObjectSetIterator, self).reset()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def toArray(self, arg0: 'Array') -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.toArray(com.badlogic.gdx.utils.Array<K>)"""
        return 'Array'.__wrap(super(__ObjectSetIterator, self).toArray(arg0))

    @overload
    def toArray(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<K> com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.toArray()"""
        return 'Array'.__wrap(super(ObjectSetIterator, self).toArray())

    @override
    @overload
    def iterator(self) -> 'ObjectSetIterator':
        """public com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator<K> com.badlogic.gdx.utils.ObjectSet$ObjectSetIterator.iterator()"""
        return 'ObjectSetIterator'.__wrap(super(ObjectSetIterator, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntIntMap
from builtins import str
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap_Entries
__Entries = __IntIntMap_Entries.Entries
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap_Values
__Values = __IntIntMap_Values.Values
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap_Keys
__Keys = __IntIntMap_Keys.Keys
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap
__IntIntMap = __IntIntMap
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class IntIntMap():
    """com.badlogic.gdx.utils.IntIntMap"""
 
    @staticmethod
    def __wrap(java_value: __IntIntMap) -> 'IntIntMap':
        return IntIntMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntIntMap):
        """
        Dynamic initializer for IntIntMap.
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
    def remove(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.IntIntMap.remove(int,int)"""
        return int.__wrap(super(__IntIntMap, self).remove(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.IntIntMap.toString()"""
        return str.__wrap(super(IntIntMap, self).toString())

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntIntMap.ensureCapacity(int)"""
        super(__IntIntMap, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'IntIntMap'):
        """public com.badlogic.gdx.utils.IntIntMap(com.badlogic.gdx.utils.IntIntMap)"""
        val = __IntIntMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.IntIntMap.put(int,int)"""
        super(__IntIntMap, self).put(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.IntIntMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntIntMap, self).equals(arg0))

    @overload
    def containsKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntIntMap.containsKey(int)"""
        return bool.__wrap(super(__IntIntMap, self).containsKey(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAndIncrement(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.IntIntMap.getAndIncrement(int,int,int)"""
        return int.__wrap(super(__IntIntMap, self).getAndIncrement(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def putAll(self, arg0: 'IntIntMap'):
        """public void com.badlogic.gdx.utils.IntIntMap.putAll(com.badlogic.gdx.utils.IntIntMap)"""
        super(__IntIntMap, self).putAll(arg0)

    @overload
    def values(self) -> 'Values':
        """public com.badlogic.gdx.utils.IntIntMap$Values com.badlogic.gdx.utils.IntIntMap.values()"""
        return 'Values'.__wrap(super(IntIntMap, self).values())

    @overload
    def containsValue(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.IntIntMap.containsValue(int)"""
        return bool.__wrap(super(__IntIntMap, self).containsValue(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def keys(self) -> 'Keys':
        """public com.badlogic.gdx.utils.IntIntMap$Keys com.badlogic.gdx.utils.IntIntMap.keys()"""
        return 'Keys'.__wrap(super(IntIntMap, self).keys())

    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntIntMap.shrink(int)"""
        super(__IntIntMap, self).shrink(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.IntIntMap(int,float)"""
        val = __IntIntMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.IntIntMap.get(int,int)"""
        return int.__wrap(super(__IntIntMap, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.IntIntMap(int)"""
        val = __IntIntMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.IntIntMap.clear()"""
        super(IntIntMap, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.IntIntMap.hashCode()"""
        return int.__wrap(super(IntIntMap, self).hashCode())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntIntMap.notEmpty()"""
        return bool.__wrap(super(IntIntMap, self).notEmpty())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IntIntMap()"""
        val = __IntIntMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.IntIntMap.clear(int)"""
        super(__IntIntMap, self).clear(__int.valueOf(arg0))

    @overload
    def findKey(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.utils.IntIntMap.findKey(int,int)"""
        return int.__wrap(super(__IntIntMap, self).findKey(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.IntIntMap.isEmpty()"""
        return bool.__wrap(super(IntIntMap, self).isEmpty())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IntIntMap()"""
        val = __IntIntMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def put(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.IntIntMap.put(int,int,int)"""
        return int.__wrap(super(__IntIntMap, self).put(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def entries(self) -> 'Entries':
        """public com.badlogic.gdx.utils.IntIntMap$Entries com.badlogic.gdx.utils.IntIntMap.entries()"""
        return 'Entries'.__wrap(super(IntIntMap, self).entries())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.utils.IntIntMap$Entry> com.badlogic.gdx.utils.IntIntMap.iterator()"""
        return 'Iterator'.__wrap(super(IntIntMap, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: com.badlogic.gdx.utils.BaseJsonReader
from pyquantum_helper import import_once as __import_once__
import java.io.InputStream as InputStream
import com.badlogic.gdx.utils.BaseJsonReader as __BaseJsonReader
__BaseJsonReader = __BaseJsonReader
from abc import abstractmethod, ABC
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

 
class BaseJsonReader(ABC):
    """com.badlogic.gdx.utils.BaseJsonReader"""
 
    @staticmethod
    def __wrap(java_value: __BaseJsonReader) -> 'BaseJsonReader':
        return BaseJsonReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseJsonReader):
        """
        Dynamic initializer for BaseJsonReader.
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
    def parse(self, arg0: 'InputStream'):
        """public abstract com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.BaseJsonReader.parse(java.io.InputStream)"""
        pass

    @abstractmethod
    def parse(self, arg0: 'FileHandle'):
        """public abstract com.badlogic.gdx.utils.JsonValue com.badlogic.gdx.utils.BaseJsonReader.parse(com.badlogic.gdx.files.FileHandle)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.utils.DataOutput
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.DataOutputStream as __DataOutputStream
__DataOutputStream = __DataOutputStream
from builtins import type
import com.badlogic.gdx.utils.DataOutput as __DataOutput
__DataOutput = __DataOutput
import java.io.FilterOutputStream as __FilterOutputStream
__FilterOutputStream = __FilterOutputStream
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class DataOutput():
    """com.badlogic.gdx.utils.DataOutput"""
 
    @staticmethod
    def __wrap(java_value: __DataOutput) -> 'DataOutput':
        return DataOutput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataOutput):
        """
        Dynamic initializer for DataOutput.
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
    def size(self) -> int:
        """public final int java.io.DataOutputStream.size()"""
        return int.__wrap(super(DataOutputStream, self).size())

    @overload
    def writeString(self, arg0: str):
        """public void com.badlogic.gdx.utils.DataOutput.writeString(java.lang.String) throws java.io.IOException"""
        super(__DataOutput, self).writeString(arg0)

    @override
    @overload
    def writeBoolean(self, arg0: bool):
        """public final void java.io.DataOutputStream.writeBoolean(boolean) throws java.io.IOException"""
        super(__DataOutputStream, self).writeBoolean(__boolean.valueOf(arg0))

    @override
    @overload
    def writeInt(self, arg0: int):
        """public final void java.io.DataOutputStream.writeInt(int) throws java.io.IOException"""
        super(__DataOutputStream, self).writeInt(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def writeChars(self, arg0: str):
        """public final void java.io.DataOutputStream.writeChars(java.lang.String) throws java.io.IOException"""
        super(__DataOutputStream, self).writeChars(arg0)

    @overload
    def writeInt(self, arg0: int, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.DataOutput.writeInt(int,boolean) throws java.io.IOException"""
        return int.__wrap(super(__DataOutput, self).writeInt(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def close(self):
        """public void java.io.FilterOutputStream.close() throws java.io.IOException"""
        super(FilterOutputStream, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def writeDouble(self, arg0: float):
        """public final void java.io.DataOutputStream.writeDouble(double) throws java.io.IOException"""
        super(__DataOutputStream, self).writeDouble(__double.valueOf(arg0))

    @override
    @overload
    def writeFloat(self, arg0: float):
        """public final void java.io.DataOutputStream.writeFloat(float) throws java.io.IOException"""
        super(__DataOutputStream, self).writeFloat(__float.valueOf(arg0))

    @override
    @overload
    def writeByte(self, arg0: int):
        """public final void java.io.DataOutputStream.writeByte(int) throws java.io.IOException"""
        super(__DataOutputStream, self).writeByte(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def writeBytes(self, arg0: str):
        """public final void java.io.DataOutputStream.writeBytes(java.lang.String) throws java.io.IOException"""
        super(__DataOutputStream, self).writeBytes(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream.__wrap(__OutputStream.nullOutputStream())

    @override
    @overload
    def writeUTF(self, arg0: str):
        """public final void java.io.DataOutputStream.writeUTF(java.lang.String) throws java.io.IOException"""
        super(__DataOutputStream, self).writeUTF(arg0)

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
    def write(self, arg0: bytes, arg1: int, arg2: int):
        """public synchronized void java.io.DataOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(__DataOutputStream, self).write(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def writeLong(self, arg0: int):
        """public final void java.io.DataOutputStream.writeLong(long) throws java.io.IOException"""
        super(__DataOutputStream, self).writeLong(__long.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: int):
        """public synchronized void java.io.DataOutputStream.write(int) throws java.io.IOException"""
        super(__DataOutputStream, self).write(__int.valueOf(arg0))

    @override
    @overload
    def flush(self):
        """public void java.io.DataOutputStream.flush() throws java.io.IOException"""
        super(DataOutputStream, self).flush()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def writeChar(self, arg0: int):
        """public final void java.io.DataOutputStream.writeChar(int) throws java.io.IOException"""
        super(__DataOutputStream, self).writeChar(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'OutputStream'):
        """public com.badlogic.gdx.utils.DataOutput(java.io.OutputStream)"""
        val = __DataOutput(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(__FilterOutputStream, self).write(bytes)

    @override
    @overload
    def writeShort(self, arg0: int):
        """public final void java.io.DataOutputStream.writeShort(int) throws java.io.IOException"""
        super(__DataOutputStream, self).writeShort(__int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.QuickSelect
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.QuickSelect as __QuickSelect
__QuickSelect = __QuickSelect
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class QuickSelect():
    """com.badlogic.gdx.utils.QuickSelect"""
 
    @staticmethod
    def __wrap(java_value: __QuickSelect) -> 'QuickSelect':
        return QuickSelect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QuickSelect):
        """
        Dynamic initializer for QuickSelect.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.QuickSelect()"""
        val = __QuickSelect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def select(self, arg0: 'Object', arg1: 'Comparator', arg2: int, arg3: int) -> int:
        """public int com.badlogic.gdx.utils.QuickSelect.select(T[],java.util.Comparator<T>,int,int)"""
        return int.__wrap(super(__QuickSelect, self).select(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.QuickSelect()"""
        val = __QuickSelect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.utils.CharArray
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.utils.CharArray as __CharArray
__CharArray = __CharArray
import java.lang.Object as __object
from builtins import type
from typing import List
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
 
class CharArray():
    """com.badlogic.gdx.utils.CharArray"""
 
    @staticmethod
    def __wrap(java_value: __CharArray) -> 'CharArray':
        return CharArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharArray):
        """
        Dynamic initializer for CharArray.
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
    def __init__(self):
        """public com.badlogic.gdx.utils.CharArray()"""
        val = __CharArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.CharArray.notEmpty()"""
        return bool.__wrap(super(CharArray, self).notEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: int) -> str:
        """public char com.badlogic.gdx.utils.CharArray.get(int)"""
        return str.__wrap(super(__CharArray, self).get(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.CharArray(boolean,int)"""
        val = __CharArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.CharArray.removeRange(int,int)"""
        super(__CharArray, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addAll(self, *arg0: str):
        """public void com.badlogic.gdx.utils.CharArray.addAll(char...)"""
        super(__CharArray, self).addAll(arg0)

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.CharArray.shuffle()"""
        super(CharArray, self).shuffle()

    @overload
    def __init__(self, arg0: 'CharArray'):
        """public com.badlogic.gdx.utils.CharArray(com.badlogic.gdx.utils.CharArray)"""
        val = __CharArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def first(self) -> str:
        """public char com.badlogic.gdx.utils.CharArray.first()"""
        return str.__wrap(super(CharArray, self).first())

    @overload
    def add(self, arg0: str):
        """public void com.badlogic.gdx.utils.CharArray.add(char)"""
        super(__CharArray, self).add(__char.valueOf(arg0))

    @overload
    def pop(self) -> str:
        """public char com.badlogic.gdx.utils.CharArray.pop()"""
        return str.__wrap(super(CharArray, self).pop())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.CharArray.equals(java.lang.Object)"""
        return bool.__wrap(super(__CharArray, self).equals(arg0))

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.CharArray.lastIndexOf(char)"""
        return int.__wrap(super(__CharArray, self).lastIndexOf(__char.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.CharArray(int)"""
        val = __CharArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.CharArray.isEmpty()"""
        return bool.__wrap(super(CharArray, self).isEmpty())

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.CharArray.contains(char)"""
        return bool.__wrap(super(__CharArray, self).contains(__char.valueOf(arg0)))

    @overload
    def random(self) -> str:
        """public char com.badlogic.gdx.utils.CharArray.random()"""
        return str.__wrap(super(CharArray, self).random())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.CharArray.toString(java.lang.String)"""
        return str.__wrap(super(__CharArray, self).toString(arg0))

    @overload
    def setSize(self, arg0: int) -> List[str]:
        """public char[] com.badlogic.gdx.utils.CharArray.setSize(int)"""
        return List[str].__wrap(super(__CharArray, self).setSize(__int.valueOf(arg0)))

    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.CharArray.sort()"""
        super(CharArray, self).sort()

    @overload
    def __init__(self, arg0: bool, arg1: 'char', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.CharArray(boolean,char[],int,int)"""
        val = __CharArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAll(self, arg0: 'CharArray', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.CharArray.addAll(com.badlogic.gdx.utils.CharArray,int,int)"""
        super(__CharArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def peek(self) -> str:
        """public char com.badlogic.gdx.utils.CharArray.peek()"""
        return str.__wrap(super(CharArray, self).peek())

    @overload
    def ensureCapacity(self, arg0: int) -> List[str]:
        """public char[] com.badlogic.gdx.utils.CharArray.ensureCapacity(int)"""
        return List[str].__wrap(super(__CharArray, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: 'char', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.CharArray.addAll(char[],int,int)"""
        super(__CharArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.CharArray.swap(int,int)"""
        super(__CharArray, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeIndex(self, arg0: int) -> str:
        """public char com.badlogic.gdx.utils.CharArray.removeIndex(int)"""
        return str.__wrap(super(__CharArray, self).removeIndex(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def with(*arg0: str) -> 'CharArray':
        """public static com.badlogic.gdx.utils.CharArray com.badlogic.gdx.utils.CharArray.with(char...)"""
        return CharArray.__wrap(__CharArray.with(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.CharArray()"""
        val = __CharArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int com.badlogic.gdx.utils.CharArray.indexOf(char)"""
        return int.__wrap(super(__CharArray, self).indexOf(__char.valueOf(arg0)))

    @overload
    def addAll(self, arg0: 'CharArray'):
        """public void com.badlogic.gdx.utils.CharArray.addAll(com.badlogic.gdx.utils.CharArray)"""
        super(__CharArray, self).addAll(arg0)

    @overload
    def shrink(self) -> List[str]:
        """public char[] com.badlogic.gdx.utils.CharArray.shrink()"""
        return List[str].__wrap(super(CharArray, self).shrink())

    @overload
    def toArray(self) -> List[str]:
        """public char[] com.badlogic.gdx.utils.CharArray.toArray()"""
        return List[str].__wrap(super(CharArray, self).toArray())

    @overload
    def incr(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.utils.CharArray.incr(int,char)"""
        super(__CharArray, self).incr(__int.valueOf(arg0), __char.valueOf(arg1))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.CharArray.clear()"""
        super(CharArray, self).clear()

    @overload
    def add(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.utils.CharArray.add(char,char)"""
        super(__CharArray, self).add(__char.valueOf(arg0), __char.valueOf(arg1))

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.CharArray.truncate(int)"""
        super(__CharArray, self).truncate(__int.valueOf(arg0))

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.CharArray.reverse()"""
        super(CharArray, self).reverse()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.CharArray.hashCode()"""
        return int.__wrap(super(CharArray, self).hashCode())

    @overload
    def add(self, arg0: str, arg1: str, arg2: str):
        """public void com.badlogic.gdx.utils.CharArray.add(char,char,char)"""
        super(__CharArray, self).add(__char.valueOf(arg0), __char.valueOf(arg1), __char.valueOf(arg2))

    @overload
    def mul(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.utils.CharArray.mul(int,char)"""
        super(__CharArray, self).mul(__int.valueOf(arg0), __char.valueOf(arg1))

    @overload
    def add(self, arg0: str, arg1: str, arg2: str, arg3: str):
        """public void com.badlogic.gdx.utils.CharArray.add(char,char,char,char)"""
        super(__CharArray, self).add(__char.valueOf(arg0), __char.valueOf(arg1), __char.valueOf(arg2), __char.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'char'):
        """public com.badlogic.gdx.utils.CharArray(char[])"""
        val = __CharArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeAll(self, arg0: 'CharArray') -> bool:
        """public boolean com.badlogic.gdx.utils.CharArray.removeAll(com.badlogic.gdx.utils.CharArray)"""
        return bool.__wrap(super(__CharArray, self).removeAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def incr(self, arg0: str):
        """public void com.badlogic.gdx.utils.CharArray.incr(char)"""
        super(__CharArray, self).incr(__char.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.CharArray.insertRange(int,int)"""
        super(__CharArray, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.utils.CharArray.set(int,char)"""
        super(__CharArray, self).set(__int.valueOf(arg0), __char.valueOf(arg1))

    @overload
    def mul(self, arg0: str):
        """public void com.badlogic.gdx.utils.CharArray.mul(char)"""
        super(__CharArray, self).mul(__char.valueOf(arg0))

    @overload
    def removeValue(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.utils.CharArray.removeValue(char)"""
        return bool.__wrap(super(__CharArray, self).removeValue(__char.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.CharArray.toString()"""
        return str.__wrap(super(CharArray, self).toString())

    @overload
    def insert(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.utils.CharArray.insert(int,char)"""
        super(__CharArray, self).insert(__int.valueOf(arg0), __char.valueOf(arg1)) 
 
 
# CLASS: com.badlogic.gdx.utils.IntMap$Entry
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
import com.badlogic.gdx.utils.IntMap as __IntMap_Entry
__Entry = __IntMap_Entry.Entry
from builtins import bool
from builtins import int
 
class Entry():
    """com.badlogic.gdx.utils.IntMap.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.IntMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.IntMap$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.IntMap$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.DataBuffer
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.io.DataOutputStream as __DataOutputStream
__DataOutputStream = __DataOutputStream
from builtins import type
import com.badlogic.gdx.utils.DataBuffer as __DataBuffer
__DataBuffer = __DataBuffer
import com.badlogic.gdx.utils.DataOutput as __DataOutput
__DataOutput = __DataOutput
import java.io.FilterOutputStream as __FilterOutputStream
__FilterOutputStream = __FilterOutputStream
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class DataBuffer():
    """com.badlogic.gdx.utils.DataBuffer"""
 
    @staticmethod
    def __wrap(java_value: __DataBuffer) -> 'DataBuffer':
        return DataBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataBuffer):
        """
        Dynamic initializer for DataBuffer.
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
    def size(self) -> int:
        """public final int java.io.DataOutputStream.size()"""
        return int.__wrap(super(DataOutputStream, self).size())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.DataBuffer()"""
        val = __DataBuffer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def writeBoolean(self, arg0: bool):
        """public final void java.io.DataOutputStream.writeBoolean(boolean) throws java.io.IOException"""
        super(__DataOutputStream, self).writeBoolean(__boolean.valueOf(arg0))

    @override
    @overload
    def writeInt(self, arg0: int):
        """public final void java.io.DataOutputStream.writeInt(int) throws java.io.IOException"""
        super(__DataOutputStream, self).writeInt(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def writeChars(self, arg0: str):
        """public final void java.io.DataOutputStream.writeChars(java.lang.String) throws java.io.IOException"""
        super(__DataOutputStream, self).writeChars(arg0)

    @overload
    def writeInt(self, arg0: int, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.DataOutput.writeInt(int,boolean) throws java.io.IOException"""
        return int.__wrap(super(__DataOutput, self).writeInt(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.DataBuffer(int)"""
        val = __DataBuffer(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public void java.io.FilterOutputStream.close() throws java.io.IOException"""
        super(FilterOutputStream, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getBuffer(self) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.DataBuffer.getBuffer()"""
        return List[int].__wrap(super(DataBuffer, self).getBuffer())

    @override
    @overload
    def writeDouble(self, arg0: float):
        """public final void java.io.DataOutputStream.writeDouble(double) throws java.io.IOException"""
        super(__DataOutputStream, self).writeDouble(__double.valueOf(arg0))

    @overload
    def toArray(self) -> List[int]:
        """public byte[] com.badlogic.gdx.utils.DataBuffer.toArray()"""
        return List[int].__wrap(super(DataBuffer, self).toArray())

    @override
    @overload
    def writeFloat(self, arg0: float):
        """public final void java.io.DataOutputStream.writeFloat(float) throws java.io.IOException"""
        super(__DataOutputStream, self).writeFloat(__float.valueOf(arg0))

    @override
    @overload
    def writeByte(self, arg0: int):
        """public final void java.io.DataOutputStream.writeByte(int) throws java.io.IOException"""
        super(__DataOutputStream, self).writeByte(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def writeBytes(self, arg0: str):
        """public final void java.io.DataOutputStream.writeBytes(java.lang.String) throws java.io.IOException"""
        super(__DataOutputStream, self).writeBytes(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def writeString(self, arg0: str):
        """public void com.badlogic.gdx.utils.DataOutput.writeString(java.lang.String) throws java.io.IOException"""
        super(__DataOutput, self).writeString(arg0)

    @staticmethod
    @overload
    def nullOutputStream() -> 'OutputStream':
        """public static java.io.OutputStream java.io.OutputStream.nullOutputStream()"""
        return OutputStream.__wrap(__OutputStream.nullOutputStream())

    @override
    @overload
    def writeUTF(self, arg0: str):
        """public final void java.io.DataOutputStream.writeUTF(java.lang.String) throws java.io.IOException"""
        super(__DataOutputStream, self).writeUTF(arg0)

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
    def write(self, arg0: bytes, arg1: int, arg2: int):
        """public synchronized void java.io.DataOutputStream.write(byte[],int,int) throws java.io.IOException"""
        super(__DataOutputStream, self).write(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def writeLong(self, arg0: int):
        """public final void java.io.DataOutputStream.writeLong(long) throws java.io.IOException"""
        super(__DataOutputStream, self).writeLong(__long.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: int):
        """public synchronized void java.io.DataOutputStream.write(int) throws java.io.IOException"""
        super(__DataOutputStream, self).write(__int.valueOf(arg0))

    @override
    @overload
    def flush(self):
        """public void java.io.DataOutputStream.flush() throws java.io.IOException"""
        super(DataOutputStream, self).flush()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def writeChar(self, arg0: int):
        """public final void java.io.DataOutputStream.writeChar(int) throws java.io.IOException"""
        super(__DataOutputStream, self).writeChar(__int.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: bytes):
        """public void java.io.FilterOutputStream.write(byte[]) throws java.io.IOException"""
        super(__FilterOutputStream, self).write(bytes)

    @override
    @overload
    def writeShort(self, arg0: int):
        """public final void java.io.DataOutputStream.writeShort(int) throws java.io.IOException"""
        super(__DataOutputStream, self).writeShort(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.DataBuffer()"""
        val = __DataBuffer()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.Array
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.utils.Array as __Array_ArrayIterator
__ArrayIterator = __Array_ArrayIterator.ArrayIterator
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Array():
    """com.badlogic.gdx.utils.Array"""
 
    @staticmethod
    def __wrap(java_value: __Array) -> 'Array':
        return Array(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Array):
        """
        Dynamic initializer for Array.
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
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString(java.lang.String)"""
        return str.__wrap(super(__Array, self).toString(arg0))

    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.removeRange(int,int)"""
        super(__Array, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.removeAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__Array, self).removeAll(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addAll(self, arg0: 'Object', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.Array.addAll(T[],int,int)"""
        super(__Array, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def lastIndexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.lastIndexOf(T,boolean)"""
        return int.__wrap(super(__Array, self).lastIndexOf(arg0, __boolean.valueOf(arg1)))

    @overload
    def contains(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.contains(T,boolean)"""
        return bool.__wrap(super(__Array, self).contains(arg0, __boolean.valueOf(arg1)))

    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.utils.Array.first()"""
        return object.__wrap(super(Array, self).first())

    @overload
    def shrink(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.shrink()"""
        return List[object].__wrap(super(Array, self).shrink())

    @staticmethod
    @overload
    def of(arg0: 'Class') -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(java.lang.Class<T>)"""
        return Array.__wrap(__Array.of(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString()"""
        return str.__wrap(super(Array, self).toString())

    @overload
    def random(self) -> object:
        """public T com.badlogic.gdx.utils.Array.random()"""
        return object.__wrap(super(Array, self).random())

    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.Array.truncate(int)"""
        super(__Array, self).truncate(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.Array.hashCode()"""
        return int.__wrap(super(Array, self).hashCode())

    @overload
    def insert(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.Array.insert(int,T)"""
        super(__Array, self).insert(__int.valueOf(arg0), arg1)

    @overload
    def selectRankedIndex(self, arg0: 'Comparator', arg1: int) -> int:
        """public int com.badlogic.gdx.utils.Array.selectRankedIndex(java.util.Comparator<T>,int)"""
        return int.__wrap(super(__Array, self).selectRankedIndex(arg0, __int.valueOf(arg1)))

    @overload
    def add(self, arg0: object, arg1: object, arg2: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T,T)"""
        super(__Array, self).add(arg0, arg1, arg2)

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public <V> V[] com.badlogic.gdx.utils.Array.toArray(java.lang.Class<V>)"""
        return List[object].__wrap(super(__Array, self).toArray(arg0))

    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.Array.reverse()"""
        super(Array, self).reverse()

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.notEmpty()"""
        return bool.__wrap(super(Array, self).notEmpty())

    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.Array.addAll(com.badlogic.gdx.utils.Array<? extends T>)"""
        super(__Array, self).addAll(arg0)

    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Array.clear()"""
        super(Array, self).clear()

    @overload
    def addAll(self, arg0: 'Array', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.Array.addAll(com.badlogic.gdx.utils.Array<? extends T>,int,int)"""
        super(__Array, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def addAll(self, *arg0: object):
        """public void com.badlogic.gdx.utils.Array.addAll(T...)"""
        super(__Array, self).addAll(arg0)

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.isEmpty()"""
        return bool.__wrap(super(Array, self).isEmpty())

    @overload
    def peek(self) -> object:
        """public T com.badlogic.gdx.utils.Array.peek()"""
        return object.__wrap(super(Array, self).peek())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.Array(int)"""
        val = __Array(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Array.get(int)"""
        return object.__wrap(super(__Array, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def pop(self) -> object:
        """public T com.badlogic.gdx.utils.Array.pop()"""
        return object.__wrap(super(Array, self).pop())

    @overload
    def setSize(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.setSize(int)"""
        return List[object].__wrap(super(__Array, self).setSize(__int.valueOf(arg0)))

    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.Array.shuffle()"""
        super(Array, self).shuffle()

    @overload
    def selectRanked(self, arg0: 'Comparator', arg1: int) -> object:
        """public T com.badlogic.gdx.utils.Array.selectRanked(java.util.Comparator<T>,int)"""
        return object.__wrap(super(__Array, self).selectRanked(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__Array, self).equalsIdentity(arg0))

    @override
    @overload
    def iterator(self) -> 'ArrayIterator':
        """public com.badlogic.gdx.utils.Array$ArrayIterator<T> com.badlogic.gdx.utils.Array.iterator()"""
        return 'ArrayIterator'.__wrap(super(Array, self).iterator())

    @overload
    def removeIndex(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Array.removeIndex(int)"""
        return object.__wrap(super(__Array, self).removeIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.utils.Array(boolean,int)"""
        val = __Array(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsAny(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAny(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__Array, self).containsAny(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def sort(self, arg0: 'Comparator'):
        """public void com.badlogic.gdx.utils.Array.sort(java.util.Comparator<? super T>)"""
        super(__Array, self).sort(arg0)

    @overload
    def __init__(self, arg0: 'Object'):
        """public com.badlogic.gdx.utils.Array(T[])"""
        val = __Array(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equals(java.lang.Object)"""
        return bool.__wrap(super(__Array, self).equals(arg0))

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.utils.Array.add(T)"""
        super(__Array, self).add(arg0)

    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.Array.sort()"""
        super(Array, self).sort()

    @overload
    def ensureCapacity(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.ensureCapacity(int)"""
        return List[object].__wrap(super(__Array, self).ensureCapacity(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def of(arg0: bool, arg1: int, arg2: 'Class') -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(boolean,int,java.lang.Class<T>)"""
        return Array.__wrap(__Array.of(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def set(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.Array.set(int,T)"""
        super(__Array, self).set(__int.valueOf(arg0), arg1)

    @overload
    def removeValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.removeValue(T,boolean)"""
        return bool.__wrap(super(__Array, self).removeValue(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.Array()"""
        val = __Array()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.indexOf(T,boolean)"""
        return int.__wrap(super(__Array, self).indexOf(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.utils.Array(com.badlogic.gdx.utils.Array<? extends T>)"""
        val = __Array(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__Array, self).containsAll(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.Array()"""
        val = __Array()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: bool, arg1: int, arg2: 'Class'):
        """public com.badlogic.gdx.utils.Array(boolean,int,java.lang.Class)"""
        val = __Array(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Class'):
        """public com.badlogic.gdx.utils.Array(java.lang.Class)"""
        val = __Array(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: object, arg1: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T)"""
        super(__Array, self).add(arg0, arg1)

    @overload
    def select(self, arg0: 'Predicate') -> 'Iterable':
        """public java.lang.Iterable<T> com.badlogic.gdx.utils.Array.select(com.badlogic.gdx.utils.Predicate<T>)"""
        return 'Iterable'.__wrap(super(__Array, self).select(arg0))

    @overload
    def add(self, arg0: object, arg1: object, arg2: object, arg3: object):
        """public void com.badlogic.gdx.utils.Array.add(T,T,T,T)"""
        super(__Array, self).add(arg0, arg1, arg2, arg3)

    @overload
    def toArray(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.toArray()"""
        return List[object].__wrap(super(Array, self).toArray())

    @staticmethod
    @overload
    def with(*arg0: object) -> 'Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.with(T...)"""
        return Array.__wrap(__Array.with(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: 'Object', arg2: int, arg3: int):
        """public com.badlogic.gdx.utils.Array(boolean,T[],int,int)"""
        val = __Array(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.swap(int,int)"""
        super(__Array, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.insertRange(int,int)"""
        super(__Array, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1)) 
 
 
# CLASS: com.badlogic.gdx.utils.OrderedSet
import com.badlogic.gdx.utils.OrderedSet as __OrderedSet
__OrderedSet = __OrderedSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.utils.OrderedSet as __OrderedSet_OrderedSetIterator
__OrderedSetIterator = __OrderedSet_OrderedSetIterator.OrderedSetIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.utils.ObjectSet as __ObjectSet
__ObjectSet = __ObjectSet
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class OrderedSet():
    """com.badlogic.gdx.utils.OrderedSet"""
 
    @staticmethod
    def __wrap(java_value: __OrderedSet) -> 'OrderedSet':
        return OrderedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedSet):
        """
        Dynamic initializer for OrderedSet.
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
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.notEmpty()"""
        return bool.__wrap(super(ObjectSet, self).notEmpty())

    @overload
    def removeIndex(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.OrderedSet.removeIndex(int)"""
        return object.__wrap(super(__OrderedSet, self).removeIndex(__int.valueOf(arg0)))

    @override
    @overload
    def addAll(self, arg0: 'Array', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.ObjectSet.addAll(com.badlogic.gdx.utils.Array<? extends T>,int,int)"""
        super(__ObjectSet, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def iterator(self) -> 'OrderedSetIterator':
        """public com.badlogic.gdx.utils.OrderedSet$OrderedSetIterator<T> com.badlogic.gdx.utils.OrderedSet.iterator()"""
        return 'OrderedSetIterator'.__wrap(super(OrderedSet, self).iterator())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.OrderedSet()"""
        val = __OrderedSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def alter(self, arg0: object, arg1: object) -> bool:
        """public boolean com.badlogic.gdx.utils.OrderedSet.alter(T,T)"""
        return bool.__wrap(super(__OrderedSet, self).alter(arg0, arg1))

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectSet.ensureCapacity(int)"""
        super(__ObjectSet, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def alterIndex(self, arg0: int, arg1: object) -> bool:
        """public boolean com.badlogic.gdx.utils.OrderedSet.alterIndex(int,T)"""
        return bool.__wrap(super(__OrderedSet, self).alterIndex(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.OrderedSet.remove(T)"""
        return bool.__wrap(super(__OrderedSet, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.ObjectSet.hashCode()"""
        return int.__wrap(super(ObjectSet, self).hashCode())

    @overload
    def orderedItems(self) -> 'Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.OrderedSet.orderedItems()"""
        return 'Array'.__wrap(super(OrderedSet, self).orderedItems())

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.utils.OrderedSet(int,float)"""
        val = __OrderedSet(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'OrderedSet'):
        """public void com.badlogic.gdx.utils.OrderedSet.addAll(com.badlogic.gdx.utils.OrderedSet<T>)"""
        super(__OrderedSet, self).addAll(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.utils.OrderedSet.clear(int)"""
        super(__OrderedSet, self).clear(__int.valueOf(arg0))

    @staticmethod
    @overload
    def with(*arg0: object) -> 'OrderedSet':
        """public static <T> com.badlogic.gdx.utils.OrderedSet<T> com.badlogic.gdx.utils.OrderedSet.with(T...)"""
        return OrderedSet.__wrap(__OrderedSet.with(arg0))

    @override
    @overload
    def shrink(self, arg0: int):
        """public void com.badlogic.gdx.utils.ObjectSet.shrink(int)"""
        super(__ObjectSet, self).shrink(__int.valueOf(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public T com.badlogic.gdx.utils.ObjectSet.get(T)"""
        return object.__wrap(super(__ObjectSet, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectSet, self).equals(arg0))

    @override
    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.utils.ObjectSet.first()"""
        return object.__wrap(super(ObjectSet, self).first())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.OrderedSet.clear()"""
        super(OrderedSet, self).clear()

    @override
    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.ObjectSet.addAll(com.badlogic.gdx.utils.Array<? extends T>)"""
        super(__ObjectSet, self).addAll(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def addAll(self, arg0: 'ObjectSet'):
        """public void com.badlogic.gdx.utils.ObjectSet.addAll(com.badlogic.gdx.utils.ObjectSet<T>)"""
        super(__ObjectSet, self).addAll(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.isEmpty()"""
        return bool.__wrap(super(ObjectSet, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.OrderedSet.add(T)"""
        return bool.__wrap(super(__OrderedSet, self).add(arg0))

    @staticmethod
    @overload
    def with(*arg0: object) -> 'ObjectSet':
        """public static <T> com.badlogic.gdx.utils.ObjectSet<T> com.badlogic.gdx.utils.ObjectSet.with(T...)"""
        return ObjectSet.__wrap(__ObjectSet.with(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.contains(T)"""
        return bool.__wrap(super(__ObjectSet, self).contains(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.OrderedSet(int)"""
        val = __OrderedSet(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.OrderedSet.toString(java.lang.String)"""
        return str.__wrap(super(__OrderedSet, self).toString(arg0))

    @overload
    def addAll(self, arg0: 'Object', arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.addAll(T[],int,int)"""
        return bool.__wrap(super(__ObjectSet, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def addAll(self, *arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.ObjectSet.addAll(T...)"""
        return bool.__wrap(super(__ObjectSet, self).addAll(arg0))

    @overload
    def __init__(self, arg0: 'OrderedSet'):
        """public com.badlogic.gdx.utils.OrderedSet(com.badlogic.gdx.utils.OrderedSet<? extends T>)"""
        val = __OrderedSet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: object, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.utils.OrderedSet.add(T,int)"""
        return bool.__wrap(super(__OrderedSet, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.OrderedSet.toString()"""
        return str.__wrap(super(OrderedSet, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.OrderedSet()"""
        val = __OrderedSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.utils.Predicate$PredicateIterable
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.Predicate as __Predicate_PredicateIterable
__PredicateIterable = __Predicate_PredicateIterable.PredicateIterable
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class PredicateIterable():
    """com.badlogic.gdx.utils.Predicate.PredicateIterable"""
 
    @staticmethod
    def __wrap(java_value: __PredicateIterable) -> 'PredicateIterable':
        return PredicateIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicateIterable):
        """
        Dynamic initializer for PredicateIterable.
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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.gdx.utils.Predicate$PredicateIterable.iterator()"""
        return 'Iterator'.__wrap(super(PredicateIterable, self).iterator())

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Iterable', arg1: 'Predicate'):
        """public com.badlogic.gdx.utils.Predicate$PredicateIterable(java.lang.Iterable<T>,com.badlogic.gdx.utils.Predicate<T>)"""
        val = __PredicateIterable(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def set(self, arg0: 'Iterable', arg1: 'Predicate'):
        """public void com.badlogic.gdx.utils.Predicate$PredicateIterable.set(java.lang.Iterable<T>,com.badlogic.gdx.utils.Predicate<T>)"""
        super(__PredicateIterable, self).set(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.TimeUtils
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.TimeUtils as __TimeUtils
__TimeUtils = __TimeUtils
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TimeUtils():
    """com.badlogic.gdx.utils.TimeUtils"""
 
    @staticmethod
    def __wrap(java_value: __TimeUtils) -> 'TimeUtils':
        return TimeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimeUtils):
        """
        Dynamic initializer for TimeUtils.
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
    def nanoTime() -> int:
        """public static long com.badlogic.gdx.utils.TimeUtils.nanoTime()"""
        return int.__wrap(__TimeUtils.nanoTime())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.TimeUtils()"""
        val = __TimeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def millis() -> int:
        """public static long com.badlogic.gdx.utils.TimeUtils.millis()"""
        return int.__wrap(__TimeUtils.millis())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def timeSinceNanos(arg0: int) -> int:
        """public static long com.badlogic.gdx.utils.TimeUtils.timeSinceNanos(long)"""
        return int.__wrap(__TimeUtils.timeSinceNanos(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.TimeUtils()"""
        val = __TimeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def timeSinceMillis(arg0: int) -> int:
        """public static long com.badlogic.gdx.utils.TimeUtils.timeSinceMillis(long)"""
        return int.__wrap(__TimeUtils.timeSinceMillis(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def millisToNanos(arg0: int) -> int:
        """public static long com.badlogic.gdx.utils.TimeUtils.millisToNanos(long)"""
        return int.__wrap(__TimeUtils.millisToNanos(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nanosToMillis(arg0: int) -> int:
        """public static long com.badlogic.gdx.utils.TimeUtils.nanosToMillis(long)"""
        return int.__wrap(__TimeUtils.nanosToMillis(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))