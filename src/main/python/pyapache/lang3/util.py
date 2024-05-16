from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.util.FluentBitSet as _FluentBitSet
_FluentBitSet = _FluentBitSet
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.BitSet as _BitSet
_BitSet = _BitSet
from typing import List
import java.util.BitSet as BitSet
import java.util.stream.IntStream as _IntStream
_IntStream = _IntStream
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FluentBitSet():
    """org.apache.commons.lang3.util.FluentBitSet"""
 
    @staticmethod
    def _wrap(java_value: _FluentBitSet) -> 'FluentBitSet':
        return FluentBitSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FluentBitSet):
        """
        Dynamic initializer for FluentBitSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FluentBitSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FluentBitSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def and(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.and(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).and(arg0))

    @overload
    def bitSet(self) -> 'BitSet':
        """public java.util.BitSet org.apache.commons.lang3.util.FluentBitSet.bitSet()"""
        return 'BitSet'._wrap(super(FluentBitSet, self).bitSet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def andNot(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.andNot(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).andNot(arg0))

    @overload
    def toByteArray(self) -> List[int]:
        """public byte[] org.apache.commons.lang3.util.FluentBitSet.toByteArray()"""
        return List[int]._wrap(super(FluentBitSet, self).toByteArray())

    @overload
    def __init__(self, arg0: 'BitSet'):
        """public org.apache.commons.lang3.util.FluentBitSet(java.util.BitSet)"""
        val = _FluentBitSet(arg0)
        self.__wrapper = val

    @overload
    def previousSetBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.previousSetBit(int)"""
        return int._wrap(super(_FluentBitSet, self).previousSetBit(_int.valueOf(arg0)))

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
    def clear(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).clear(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.util.FluentBitSet(int)"""
        val = _FluentBitSet(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def and(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.and(java.util.BitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).and(arg0))

    @overload
    def cardinality(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.cardinality()"""
        return int._wrap(super(FluentBitSet, self).cardinality())

    @overload
    def xor(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.xor(java.util.BitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).xor(arg0))

    @overload
    def intersects(self, arg0: 'FluentBitSet') -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.intersects(org.apache.commons.lang3.util.FluentBitSet)"""
        return bool._wrap(super(_FluentBitSet, self).intersects(arg0))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.size()"""
        return int._wrap(super(FluentBitSet, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.equals(java.lang.Object)"""
        return bool._wrap(super(_FluentBitSet, self).equals(arg0))

    @overload
    def clear(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).clear(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def flip(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.flip(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).flip(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.util.FluentBitSet()"""
        val = _FluentBitSet()
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.get(int)"""
        return bool._wrap(super(_FluentBitSet, self).get(_int.valueOf(arg0)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.isEmpty()"""
        return bool._wrap(super(FluentBitSet, self).isEmpty())

    @overload
    def set(self, arg0: int, arg1: bool) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,boolean)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(_int.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def set(self, *arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int...)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(arg0))

    @overload
    def stream(self) -> 'IntStream':
        """public java.util.stream.IntStream org.apache.commons.lang3.util.FluentBitSet.stream()"""
        return 'IntStream'._wrap(super(FluentBitSet, self).stream())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def previousClearBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.previousClearBit(int)"""
        return int._wrap(super(_FluentBitSet, self).previousClearBit(_int.valueOf(arg0)))

    @overload
    def toLongArray(self) -> List[int]:
        """public long[] org.apache.commons.lang3.util.FluentBitSet.toLongArray()"""
        return List[int]._wrap(super(FluentBitSet, self).toLongArray())

    @overload
    def set(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def clone(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.util.FluentBitSet.clone()"""
        return object._wrap(super(FluentBitSet, self).clone())

    @overload
    def set(self, arg0: int, arg1: int, arg2: bool) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,int,boolean)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def or(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(java.util.BitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).or(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.hashCode()"""
        return int._wrap(super(FluentBitSet, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.util.FluentBitSet()"""
        val = _FluentBitSet()
        self.__wrapper = val

    @overload
    def or(self, *arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(org.apache.commons.lang3.util.FluentBitSet...)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).or(arg0))

    @overload
    def flip(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.flip(int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).flip(_int.valueOf(arg0)))

    @overload
    def intersects(self, arg0: 'BitSet') -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.intersects(java.util.BitSet)"""
        return bool._wrap(super(_FluentBitSet, self).intersects(arg0))

    @overload
    def setInclusive(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.setInclusive(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).setInclusive(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def set(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.util.FluentBitSet.toString()"""
        return str._wrap(super(FluentBitSet, self).toString())

    @overload
    def xor(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.xor(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).xor(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def length(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.length()"""
        return int._wrap(super(FluentBitSet, self).length())

    @overload
    def andNot(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.andNot(java.util.BitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).andNot(arg0))

    @overload
    def nextClearBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.nextClearBit(int)"""
        return int._wrap(super(_FluentBitSet, self).nextClearBit(_int.valueOf(arg0)))

    @overload
    def nextSetBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.nextSetBit(int)"""
        return int._wrap(super(_FluentBitSet, self).nextSetBit(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.get(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def clear(self, *arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int...)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).clear(arg0))

    @overload
    def clear(self) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear()"""
        return 'FluentBitSet'._wrap(super(FluentBitSet, self).clear())

    @overload
    def or(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).or(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.util.FluentBitSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.util.FluentBitSet as _FluentBitSet
_FluentBitSet = _FluentBitSet
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.BitSet as _BitSet
_BitSet = _BitSet
from typing import List
import java.util.BitSet as BitSet
import java.util.stream.IntStream as _IntStream
_IntStream = _IntStream
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FluentBitSet():
    """org.apache.commons.lang3.util.FluentBitSet"""
 
    @staticmethod
    def _wrap(java_value: _FluentBitSet) -> 'FluentBitSet':
        return FluentBitSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FluentBitSet):
        """
        Dynamic initializer for FluentBitSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FluentBitSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FluentBitSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def and(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.and(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).and(arg0))

    @overload
    def bitSet(self) -> 'BitSet':
        """public java.util.BitSet org.apache.commons.lang3.util.FluentBitSet.bitSet()"""
        return 'BitSet'._wrap(super(FluentBitSet, self).bitSet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def andNot(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.andNot(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).andNot(arg0))

    @overload
    def toByteArray(self) -> List[int]:
        """public byte[] org.apache.commons.lang3.util.FluentBitSet.toByteArray()"""
        return List[int]._wrap(super(FluentBitSet, self).toByteArray())

    @overload
    def __init__(self, arg0: 'BitSet'):
        """public org.apache.commons.lang3.util.FluentBitSet(java.util.BitSet)"""
        val = _FluentBitSet(arg0)
        self.__wrapper = val

    @overload
    def previousSetBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.previousSetBit(int)"""
        return int._wrap(super(_FluentBitSet, self).previousSetBit(_int.valueOf(arg0)))

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
    def clear(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).clear(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.util.FluentBitSet(int)"""
        val = _FluentBitSet(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def and(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.and(java.util.BitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).and(arg0))

    @overload
    def cardinality(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.cardinality()"""
        return int._wrap(super(FluentBitSet, self).cardinality())

    @overload
    def xor(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.xor(java.util.BitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).xor(arg0))

    @overload
    def intersects(self, arg0: 'FluentBitSet') -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.intersects(org.apache.commons.lang3.util.FluentBitSet)"""
        return bool._wrap(super(_FluentBitSet, self).intersects(arg0))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.size()"""
        return int._wrap(super(FluentBitSet, self).size())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.equals(java.lang.Object)"""
        return bool._wrap(super(_FluentBitSet, self).equals(arg0))

    @overload
    def clear(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).clear(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def flip(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.flip(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).flip(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.util.FluentBitSet()"""
        val = _FluentBitSet()
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.get(int)"""
        return bool._wrap(super(_FluentBitSet, self).get(_int.valueOf(arg0)))

    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.isEmpty()"""
        return bool._wrap(super(FluentBitSet, self).isEmpty())

    @overload
    def set(self, arg0: int, arg1: bool) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,boolean)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(_int.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def set(self, *arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int...)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(arg0))

    @overload
    def stream(self) -> 'IntStream':
        """public java.util.stream.IntStream org.apache.commons.lang3.util.FluentBitSet.stream()"""
        return 'IntStream'._wrap(super(FluentBitSet, self).stream())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def previousClearBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.previousClearBit(int)"""
        return int._wrap(super(_FluentBitSet, self).previousClearBit(_int.valueOf(arg0)))

    @overload
    def toLongArray(self) -> List[int]:
        """public long[] org.apache.commons.lang3.util.FluentBitSet.toLongArray()"""
        return List[int]._wrap(super(FluentBitSet, self).toLongArray())

    @overload
    def set(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def clone(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.util.FluentBitSet.clone()"""
        return object._wrap(super(FluentBitSet, self).clone())

    @overload
    def set(self, arg0: int, arg1: int, arg2: bool) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int,int,boolean)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def or(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(java.util.BitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).or(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.hashCode()"""
        return int._wrap(super(FluentBitSet, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.util.FluentBitSet()"""
        val = _FluentBitSet()
        self.__wrapper = val

    @overload
    def or(self, *arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(org.apache.commons.lang3.util.FluentBitSet...)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).or(arg0))

    @overload
    def flip(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.flip(int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).flip(_int.valueOf(arg0)))

    @overload
    def intersects(self, arg0: 'BitSet') -> bool:
        """public boolean org.apache.commons.lang3.util.FluentBitSet.intersects(java.util.BitSet)"""
        return bool._wrap(super(_FluentBitSet, self).intersects(arg0))

    @overload
    def setInclusive(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.setInclusive(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).setInclusive(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def set(self, arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.set(int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).set(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.util.FluentBitSet.toString()"""
        return str._wrap(super(FluentBitSet, self).toString())

    @overload
    def xor(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.xor(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).xor(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def length(self) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.length()"""
        return int._wrap(super(FluentBitSet, self).length())

    @overload
    def andNot(self, arg0: 'BitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.andNot(java.util.BitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).andNot(arg0))

    @overload
    def nextClearBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.nextClearBit(int)"""
        return int._wrap(super(_FluentBitSet, self).nextClearBit(_int.valueOf(arg0)))

    @overload
    def nextSetBit(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.util.FluentBitSet.nextSetBit(int)"""
        return int._wrap(super(_FluentBitSet, self).nextSetBit(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: int, arg1: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.get(int,int)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def clear(self, *arg0: int) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear(int...)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).clear(arg0))

    @overload
    def clear(self) -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.clear()"""
        return 'FluentBitSet'._wrap(super(FluentBitSet, self).clear())

    @overload
    def or(self, arg0: 'FluentBitSet') -> 'FluentBitSet':
        """public org.apache.commons.lang3.util.FluentBitSet org.apache.commons.lang3.util.FluentBitSet.or(org.apache.commons.lang3.util.FluentBitSet)"""
        return 'FluentBitSet'._wrap(super(_FluentBitSet, self).or(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.util.FluentBitSet