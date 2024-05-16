from __future__ import annotations
from overload import overload


 
import java.util.BitSet as __BitSet
__BitSet = __BitSet
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import org.apache.commons.lang3.util.FluentBitSet as __FluentBitSet
__FluentBitSet = __FluentBitSet
import java.util.BitSet as BitSet
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
 
class FluentBitSet():
    """org.apache.commons.lang3.util.FluentBitSet"""
 
    @staticmethod
    def __wrap(java_value: __FluentBitSet) -> 'FluentBitSet':
        return FluentBitSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FluentBitSet):
        """
        Dynamic initializer for FluentBitSet.
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
    def intersects(self, arg0: 'BitSet') -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.intersects(java.util.BitSet)"""
        return bool.__wrap(super(__FluentBitSet, self).intersects(arg0))

    @overload
    def and(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.and(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).and(arg0))

    @overload
    def stream(self) -> 'IntStream':
        """public java.util.stream.IntStream org.apache.commons.lang3.util.FluentBitSet.stream()"""
        return 'IntStream'.__wrap(super(FluentBitSet, self).stream())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.util.FluentBitSet()"""
        val = __FluentBitSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, *arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int...)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def length(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.length()"""
        return int.__wrap(super(FluentBitSet, self).length())

    @overload
    def set(self, arg0: int, arg1: int, arg2: bool) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,int,boolean)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2)))

    @overload
    def xor(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.xor(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).xor(arg0))

    @overload
    def nextClearBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.nextClearBit(int)"""
        return int.__wrap(super(__FluentBitSet, self).nextClearBit(__int.valueOf(arg0)))

    @overload
    def bitSet(self) -> 'BitSet':
        """public java.util.BitSet org.apache.commons.lang3.util.FluentBitSet.bitSet()"""
        return 'BitSet'.__wrap(super(FluentBitSet, self).bitSet())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def andNot(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.andNot(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).andNot(arg0))

    @overload
    def get(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.get(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def flip(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.flip(int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).flip(__int.valueOf(arg0)))

    @overload
    def or(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).or(arg0))

    @overload
    def __init__(self, arg0: 'BitSet'):
        """public org.apache.commons.lang3.util.FluentBitSet(java.util.BitSet)"""
        val = __FluentBitSet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.size()"""
        return int.__wrap(super(FluentBitSet, self).size())

    @overload
    def clear(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).clear(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def flip(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.flip(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).flip(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def intersects(self, arg0: 'FluentBitSet') -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.intersects(org.apache.commons.lang3.util.FluentBitSet)"""
        return bool.__wrap(super(__FluentBitSet, self).intersects(arg0))

    @overload
    def clear(self) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear()"""
        return 'FluentBitSet'.__wrap(super(FluentBitSet, self).clear())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setInclusive(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.setInclusive(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).setInclusive(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.util.FluentBitSet(int)"""
        val = __FluentBitSet(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def nextSetBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.nextSetBit(int)"""
        return int.__wrap(super(__FluentBitSet, self).nextSetBit(__int.valueOf(arg0)))

    @overload
    def previousClearBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.previousClearBit(int)"""
        return int.__wrap(super(__FluentBitSet, self).previousClearBit(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.util.FluentBitSet.toString()"""
        return str.__wrap(super(FluentBitSet, self).toString())

    @overload
    def and(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.and(java.util.BitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).and(arg0))

    @overload
    def set(self, arg0: int, arg1: bool) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,boolean)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def toLongArray(self) -> List[int]:
        """public long[] org.apache.commons.lang3.util.FluentBitSet.toLongArray()"""
        return List[int].__wrap(super(FluentBitSet, self).toLongArray())

    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.isEmpty()"""
        return bool.__wrap(super(FluentBitSet, self).isEmpty())

    @overload
    def clear(self, *arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int...)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).clear(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.util.FluentBitSet()"""
        val = __FluentBitSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).clear(__int.valueOf(arg0)))

    @overload
    def clone(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.util.FluentBitSet.clone()"""
        return object.__wrap(super(FluentBitSet, self).clone())

    @overload
    def cardinality(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.cardinality()"""
        return int.__wrap(super(FluentBitSet, self).cardinality())

    @overload
    def andNot(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.andNot(java.util.BitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).andNot(arg0))

    @overload
    def get(self, arg0: int) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.get(int)"""
        return bool.__wrap(super(__FluentBitSet, self).get(__int.valueOf(arg0)))

    @overload
    def previousSetBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.previousSetBit(int)"""
        return int.__wrap(super(__FluentBitSet, self).previousSetBit(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.hashCode()"""
        return int.__wrap(super(FluentBitSet, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__FluentBitSet, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(__int.valueOf(arg0)))

    @overload
    def xor(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.xor(java.util.BitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).xor(arg0))

    @overload
    def or(self, *arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(org.apache.commons.lang3.util.FluentBitSet...)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).or(arg0))

    @overload
    def toByteArray(self) -> List[int]:
        """public byte[] org.apache.commons.lang3.util.FluentBitSet.toByteArray()"""
        return List[int].__wrap(super(FluentBitSet, self).toByteArray())

    @overload
    def or(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(java.util.BitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).or(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.util.FluentBitSet
import java.util.BitSet as __BitSet
__BitSet = __BitSet
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import org.apache.commons.lang3.util.FluentBitSet as __FluentBitSet
__FluentBitSet = __FluentBitSet
import java.util.BitSet as BitSet
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
 
class FluentBitSet():
    """org.apache.commons.lang3.util.FluentBitSet"""
 
    @staticmethod
    def __wrap(java_value: __FluentBitSet) -> 'FluentBitSet':
        return FluentBitSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FluentBitSet):
        """
        Dynamic initializer for FluentBitSet.
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
    def intersects(self, arg0: 'BitSet') -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.intersects(java.util.BitSet)"""
        return bool.__wrap(super(__FluentBitSet, self).intersects(arg0))

    @overload
    def and(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.and(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).and(arg0))

    @overload
    def stream(self) -> 'IntStream':
        """public java.util.stream.IntStream org.apache.commons.lang3.util.FluentBitSet.stream()"""
        return 'IntStream'.__wrap(super(FluentBitSet, self).stream())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.util.FluentBitSet()"""
        val = __FluentBitSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, *arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int...)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def length(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.length()"""
        return int.__wrap(super(FluentBitSet, self).length())

    @overload
    def set(self, arg0: int, arg1: int, arg2: bool) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,int,boolean)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2)))

    @overload
    def xor(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.xor(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).xor(arg0))

    @overload
    def nextClearBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.nextClearBit(int)"""
        return int.__wrap(super(__FluentBitSet, self).nextClearBit(__int.valueOf(arg0)))

    @overload
    def bitSet(self) -> 'BitSet':
        """public java.util.BitSet org.apache.commons.lang3.util.FluentBitSet.bitSet()"""
        return 'BitSet'.__wrap(super(FluentBitSet, self).bitSet())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def andNot(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.andNot(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).andNot(arg0))

    @overload
    def get(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.get(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def flip(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.flip(int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).flip(__int.valueOf(arg0)))

    @overload
    def or(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).or(arg0))

    @overload
    def __init__(self, arg0: 'BitSet'):
        """public org.apache.commons.lang3.util.FluentBitSet(java.util.BitSet)"""
        val = __FluentBitSet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.size()"""
        return int.__wrap(super(FluentBitSet, self).size())

    @overload
    def clear(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).clear(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def flip(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.flip(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).flip(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def intersects(self, arg0: 'FluentBitSet') -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.intersects(org.apache.commons.lang3.util.FluentBitSet)"""
        return bool.__wrap(super(__FluentBitSet, self).intersects(arg0))

    @overload
    def clear(self) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear()"""
        return 'FluentBitSet'.__wrap(super(FluentBitSet, self).clear())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setInclusive(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.setInclusive(int,int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).setInclusive(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.util.FluentBitSet(int)"""
        val = __FluentBitSet(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def nextSetBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.nextSetBit(int)"""
        return int.__wrap(super(__FluentBitSet, self).nextSetBit(__int.valueOf(arg0)))

    @overload
    def previousClearBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.previousClearBit(int)"""
        return int.__wrap(super(__FluentBitSet, self).previousClearBit(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.util.FluentBitSet.toString()"""
        return str.__wrap(super(FluentBitSet, self).toString())

    @overload
    def and(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.and(java.util.BitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).and(arg0))

    @overload
    def set(self, arg0: int, arg1: bool) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,boolean)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def toLongArray(self) -> List[int]:
        """public long[] org.apache.commons.lang3.util.FluentBitSet.toLongArray()"""
        return List[int].__wrap(super(FluentBitSet, self).toLongArray())

    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.isEmpty()"""
        return bool.__wrap(super(FluentBitSet, self).isEmpty())

    @overload
    def clear(self, *arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int...)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).clear(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.util.FluentBitSet()"""
        val = __FluentBitSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).clear(__int.valueOf(arg0)))

    @overload
    def clone(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.util.FluentBitSet.clone()"""
        return object.__wrap(super(FluentBitSet, self).clone())

    @overload
    def cardinality(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.cardinality()"""
        return int.__wrap(super(FluentBitSet, self).cardinality())

    @overload
    def andNot(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.andNot(java.util.BitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).andNot(arg0))

    @overload
    def get(self, arg0: int) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.get(int)"""
        return bool.__wrap(super(__FluentBitSet, self).get(__int.valueOf(arg0)))

    @overload
    def previousSetBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.previousSetBit(int)"""
        return int.__wrap(super(__FluentBitSet, self).previousSetBit(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.hashCode()"""
        return int.__wrap(super(FluentBitSet, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__FluentBitSet, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).set(__int.valueOf(arg0)))

    @overload
    def xor(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.xor(java.util.BitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).xor(arg0))

    @overload
    def or(self, *arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(org.apache.commons.lang3.util.FluentBitSet...)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).or(arg0))

    @overload
    def toByteArray(self) -> List[int]:
        """public byte[] org.apache.commons.lang3.util.FluentBitSet.toByteArray()"""
        return List[int].__wrap(super(FluentBitSet, self).toByteArray())

    @overload
    def or(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(java.util.BitSet)"""
        return 'FluentBitSet'.__wrap(super(__FluentBitSet, self).or(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.util.FluentBitSet