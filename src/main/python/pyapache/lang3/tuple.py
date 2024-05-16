from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.lang3.tuple.Pair as __Pair
__Pair = __Pair
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import java.util.Map.Entry as Entry
import java.lang.Long as __long
import org.apache.commons.lang3.tuple.MutablePair as __MutablePair
__MutablePair = __MutablePair
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MutablePair():
    """org.apache.commons.lang3.tuple.MutablePair"""
 
    @staticmethod
    def __wrap(java_value: __MutablePair) -> 'MutablePair':
        return MutablePair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutablePair):
        """
        Dynamic initializer for MutablePair.
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
    def of(arg0: 'Entry') -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.of(java.util.Map$Entry<L, R>)"""
        return MutablePair.__wrap(__MutablePair.of(arg0))

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object.__wrap(super(__Pair, self).apply(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.MutablePair()"""
        val = __MutablePair()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: object) -> object:
        """public R org.apache.commons.lang3.tuple.MutablePair.setValue(R)"""
        return object.__wrap(super(__MutablePair, self).setValue(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object.__wrap(super(Pair, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.MutablePair.getRight()"""
        return object.__wrap(super(MutablePair, self).getRight())

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return Pair.__wrap(__Pair.ofNonNull(arg0, arg1))

    @override
    @overload
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(__Pair, self).accept(arg0)

    @staticmethod
    @overload
    def emptyArray() -> List['MutablePair']:
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R>[] org.apache.commons.lang3.tuple.MutablePair.emptyArray()"""
        return List[MutablePair].__wrap(__MutablePair.emptyArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.of(L,R)"""
        return MutablePair.__wrap(__MutablePair.of(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool.__wrap(super(__Pair, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.MutablePair()"""
        val = __MutablePair()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.ofNonNull(L,R)"""
        return MutablePair.__wrap(__MutablePair.ofNonNull(arg0, arg1))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return Pair.__wrap(__Pair.of(arg0, arg1))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str.__wrap(super(__Pair, self).toString(arg0))

    @overload
    def setRight(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutablePair.setRight(R)"""
        super(__MutablePair, self).setRight(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object.__wrap(super(Pair, self).getKey())

    @override
    @overload
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.MutablePair.getLeft()"""
        return object.__wrap(super(MutablePair, self).getLeft())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setLeft(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutablePair.setLeft(L)"""
        super(__MutablePair, self).setLeft(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString()"""
        return str.__wrap(super(Pair, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int.__wrap(super(Pair, self).hashCode())

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.lang3.tuple.MutablePair(L,R)"""
        val = __MutablePair(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int.__wrap(super(__Pair, self).compareTo(arg0))

    @staticmethod
    @overload
    def emptyArray() -> List['Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[Pair].__wrap(__Pair.emptyArray())

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return Pair.__wrap(__Pair.of(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.tuple.MutablePair
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.lang3.tuple.Pair as __Pair
__Pair = __Pair
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import java.util.Map.Entry as Entry
import java.lang.Long as __long
import org.apache.commons.lang3.tuple.MutablePair as __MutablePair
__MutablePair = __MutablePair
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MutablePair():
    """org.apache.commons.lang3.tuple.MutablePair"""
 
    @staticmethod
    def __wrap(java_value: __MutablePair) -> 'MutablePair':
        return MutablePair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutablePair):
        """
        Dynamic initializer for MutablePair.
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
    def of(arg0: 'Entry') -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.of(java.util.Map$Entry<L, R>)"""
        return MutablePair.__wrap(__MutablePair.of(arg0))

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object.__wrap(super(__Pair, self).apply(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.MutablePair()"""
        val = __MutablePair()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setValue(self, arg0: object) -> object:
        """public R org.apache.commons.lang3.tuple.MutablePair.setValue(R)"""
        return object.__wrap(super(__MutablePair, self).setValue(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object.__wrap(super(Pair, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.MutablePair.getRight()"""
        return object.__wrap(super(MutablePair, self).getRight())

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return Pair.__wrap(__Pair.ofNonNull(arg0, arg1))

    @override
    @overload
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(__Pair, self).accept(arg0)

    @staticmethod
    @overload
    def emptyArray() -> List['MutablePair']:
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R>[] org.apache.commons.lang3.tuple.MutablePair.emptyArray()"""
        return List[MutablePair].__wrap(__MutablePair.emptyArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.of(L,R)"""
        return MutablePair.__wrap(__MutablePair.of(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool.__wrap(super(__Pair, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.MutablePair()"""
        val = __MutablePair()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.ofNonNull(L,R)"""
        return MutablePair.__wrap(__MutablePair.ofNonNull(arg0, arg1))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return Pair.__wrap(__Pair.of(arg0, arg1))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str.__wrap(super(__Pair, self).toString(arg0))

    @overload
    def setRight(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutablePair.setRight(R)"""
        super(__MutablePair, self).setRight(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object.__wrap(super(Pair, self).getKey())

    @override
    @overload
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.MutablePair.getLeft()"""
        return object.__wrap(super(MutablePair, self).getLeft())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setLeft(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutablePair.setLeft(L)"""
        super(__MutablePair, self).setLeft(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString()"""
        return str.__wrap(super(Pair, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int.__wrap(super(Pair, self).hashCode())

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.lang3.tuple.MutablePair(L,R)"""
        val = __MutablePair(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int.__wrap(super(__Pair, self).compareTo(arg0))

    @staticmethod
    @overload
    def emptyArray() -> List['Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[Pair].__wrap(__Pair.emptyArray())

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return Pair.__wrap(__Pair.of(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.tuple.MutablePair 
 
 
# CLASS: org.apache.commons.lang3.tuple.MutableTriple
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.tuple.Triple as __Triple
__Triple = __Triple
import org.apache.commons.lang3.tuple.MutableTriple as __MutableTriple
__MutableTriple = __MutableTriple
from builtins import object
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
 
class MutableTriple():
    """org.apache.commons.lang3.tuple.MutableTriple"""
 
    @staticmethod
    def __wrap(java_value: __MutableTriple) -> 'MutableTriple':
        return MutableTriple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableTriple):
        """
        Dynamic initializer for MutableTriple.
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
    def emptyArray() -> List['Triple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R>[] org.apache.commons.lang3.tuple.Triple.emptyArray()"""
        return List[Triple].__wrap(__Triple.emptyArray())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.MutableTriple.getRight()"""
        return object.__wrap(super(MutableTriple, self).getRight())

    @overload
    def setMiddle(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutableTriple.setMiddle(M)"""
        super(__MutableTriple, self).setMiddle(arg0)

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'MutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.MutableTriple<L, M, R> org.apache.commons.lang3.tuple.MutableTriple.of(L,M,R)"""
        return MutableTriple.__wrap(__MutableTriple.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.ofNonNull(L,M,R)"""
        return Triple.__wrap(__Triple.ofNonNull(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLeft(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutableTriple.setLeft(L)"""
        super(__MutableTriple, self).setLeft(arg0)

    @override
    @overload
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.MutableTriple.getLeft()"""
        return object.__wrap(super(MutableTriple, self).getLeft())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.MutableTriple()"""
        val = __MutableTriple()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compareTo(self, arg0: 'Triple') -> int:
        """public int org.apache.commons.lang3.tuple.Triple.compareTo(org.apache.commons.lang3.tuple.Triple<L, M, R>)"""
        return int.__wrap(super(__Triple, self).compareTo(arg0))

    @staticmethod
    @overload
    def emptyArray() -> List['MutableTriple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.MutableTriple<L, M, R>[] org.apache.commons.lang3.tuple.MutableTriple.emptyArray()"""
        return List[MutableTriple].__wrap(__MutableTriple.emptyArray())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Triple.hashCode()"""
        return int.__wrap(super(Triple, self).hashCode())

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.of(L,M,R)"""
        return Triple.__wrap(__Triple.of(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public org.apache.commons.lang3.tuple.MutableTriple(L,M,R)"""
        val = __MutableTriple(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString(java.lang.String)"""
        return str.__wrap(super(__Triple, self).toString(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.MutableTriple()"""
        val = __MutableTriple()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Triple.equals(java.lang.Object)"""
        return bool.__wrap(super(__Triple, self).equals(arg0))

    @override
    @overload
    def getMiddle(self) -> object:
        """public M org.apache.commons.lang3.tuple.MutableTriple.getMiddle()"""
        return object.__wrap(super(MutableTriple, self).getMiddle())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString()"""
        return str.__wrap(super(Triple, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'MutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.MutableTriple<L, M, R> org.apache.commons.lang3.tuple.MutableTriple.ofNonNull(L,M,R)"""
        return MutableTriple.__wrap(__MutableTriple.ofNonNull(arg0, arg1, arg2))

    @overload
    def setRight(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutableTriple.setRight(R)"""
        super(__MutableTriple, self).setRight(arg0) 
 
 
# CLASS: org.apache.commons.lang3.tuple.ImmutablePair
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.lang3.tuple.Pair as __Pair
__Pair = __Pair
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import java.util.Map.Entry as Entry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.lang3.tuple.ImmutablePair as __ImmutablePair
__ImmutablePair = __ImmutablePair
from builtins import int
 
class ImmutablePair():
    """org.apache.commons.lang3.tuple.ImmutablePair"""
 
    @staticmethod
    def __wrap(java_value: __ImmutablePair) -> 'ImmutablePair':
        return ImmutablePair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutablePair):
        """
        Dynamic initializer for ImmutablePair.
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
    def setValue(self, arg0: object) -> object:
        """public R org.apache.commons.lang3.tuple.ImmutablePair.setValue(R)"""
        return object.__wrap(super(__ImmutablePair, self).setValue(arg0))

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object.__wrap(super(__Pair, self).apply(arg0))

    @staticmethod
    @overload
    def right(arg0: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.right(R)"""
        return Pair.__wrap(__ImmutablePair.right(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object.__wrap(super(Pair, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'ImmutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.ofNonNull(L,R)"""
        return ImmutablePair.__wrap(__ImmutablePair.ofNonNull(arg0, arg1))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'ImmutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.of(L,R)"""
        return ImmutablePair.__wrap(__ImmutablePair.of(arg0, arg1))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return Pair.__wrap(__Pair.ofNonNull(arg0, arg1))

    @override
    @overload
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(__Pair, self).accept(arg0)

    @staticmethod
    @overload
    def nullPair() -> 'ImmutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.nullPair()"""
        return ImmutablePair.__wrap(__ImmutablePair.nullPair())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool.__wrap(super(__Pair, self).equals(arg0))

    @staticmethod
    @overload
    def left(arg0: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.left(L)"""
        return Pair.__wrap(__ImmutablePair.left(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'ImmutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.of(java.util.Map$Entry<L, R>)"""
        return ImmutablePair.__wrap(__ImmutablePair.of(arg0))

    @staticmethod
    @overload
    def emptyArray() -> List['ImmutablePair']:
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R>[] org.apache.commons.lang3.tuple.ImmutablePair.emptyArray()"""
        return List[ImmutablePair].__wrap(__ImmutablePair.emptyArray())

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.lang3.tuple.ImmutablePair(L,R)"""
        val = __ImmutablePair(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.ImmutablePair.getLeft()"""
        return object.__wrap(super(ImmutablePair, self).getLeft())

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return Pair.__wrap(__Pair.of(arg0, arg1))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str.__wrap(super(__Pair, self).toString(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object.__wrap(super(Pair, self).getKey())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.ImmutablePair.getRight()"""
        return object.__wrap(super(ImmutablePair, self).getRight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString()"""
        return str.__wrap(super(Pair, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int.__wrap(super(Pair, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int.__wrap(super(__Pair, self).compareTo(arg0))

    @staticmethod
    @overload
    def emptyArray() -> List['Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[Pair].__wrap(__Pair.emptyArray())

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return Pair.__wrap(__Pair.of(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.tuple.ImmutableTriple
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.tuple.Triple as __Triple
__Triple = __Triple
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.tuple.ImmutableTriple as __ImmutableTriple
__ImmutableTriple = __ImmutableTriple
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ImmutableTriple():
    """org.apache.commons.lang3.tuple.ImmutableTriple"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableTriple) -> 'ImmutableTriple':
        return ImmutableTriple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableTriple):
        """
        Dynamic initializer for ImmutableTriple.
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
    def emptyArray() -> List['Triple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R>[] org.apache.commons.lang3.tuple.Triple.emptyArray()"""
        return List[Triple].__wrap(__Triple.emptyArray())

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'ImmutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.ImmutableTriple<L, M, R> org.apache.commons.lang3.tuple.ImmutableTriple.ofNonNull(L,M,R)"""
        return ImmutableTriple.__wrap(__ImmutableTriple.ofNonNull(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.ImmutableTriple.getRight()"""
        return object.__wrap(super(ImmutableTriple, self).getRight())

    @staticmethod
    @overload
    def emptyArray() -> List['ImmutableTriple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.ImmutableTriple<L, M, R>[] org.apache.commons.lang3.tuple.ImmutableTriple.emptyArray()"""
        return List[ImmutableTriple].__wrap(__ImmutableTriple.emptyArray())

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.ofNonNull(L,M,R)"""
        return Triple.__wrap(__Triple.ofNonNull(arg0, arg1, arg2))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'ImmutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.ImmutableTriple<L, M, R> org.apache.commons.lang3.tuple.ImmutableTriple.of(L,M,R)"""
        return ImmutableTriple.__wrap(__ImmutableTriple.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nullTriple() -> 'ImmutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.ImmutableTriple<L, M, R> org.apache.commons.lang3.tuple.ImmutableTriple.nullTriple()"""
        return ImmutableTriple.__wrap(__ImmutableTriple.nullTriple())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString(java.lang.String)"""
        return str.__wrap(super(__Triple, self).toString(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMiddle(self) -> object:
        """public M org.apache.commons.lang3.tuple.ImmutableTriple.getMiddle()"""
        return object.__wrap(super(ImmutableTriple, self).getMiddle())

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
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.ImmutableTriple.getLeft()"""
        return object.__wrap(super(ImmutableTriple, self).getLeft())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Triple.equals(java.lang.Object)"""
        return bool.__wrap(super(__Triple, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compareTo(self, arg0: 'Triple') -> int:
        """public int org.apache.commons.lang3.tuple.Triple.compareTo(org.apache.commons.lang3.tuple.Triple<L, M, R>)"""
        return int.__wrap(super(__Triple, self).compareTo(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Triple.hashCode()"""
        return int.__wrap(super(Triple, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString()"""
        return str.__wrap(super(Triple, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public org.apache.commons.lang3.tuple.ImmutableTriple(L,M,R)"""
        val = __ImmutableTriple(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.of(L,M,R)"""
        return Triple.__wrap(__Triple.of(arg0, arg1, arg2)) 
 
 
# CLASS: org.apache.commons.lang3.tuple.Pair
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.lang3.tuple.Pair as __Pair
__Pair = __Pair
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
from builtins import object
from abc import abstractmethod, ABC
from typing import List
import java.util.Map.Entry as Entry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Pair(ABC):
    """org.apache.commons.lang3.tuple.Pair"""
 
    @staticmethod
    def __wrap(java_value: __Pair) -> 'Pair':
        return Pair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pair):
        """
        Dynamic initializer for Pair.
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
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(__Pair, self).accept(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object.__wrap(super(__Pair, self).apply(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object.__wrap(super(Pair, self).getValue())

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract V java.util.Map$Entry.setValue(V)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str.__wrap(super(__Pair, self).toString(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return Pair.__wrap(__Pair.of(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.Pair()"""
        val = __Pair()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def getRight(self, ):
        """public abstract R org.apache.commons.lang3.tuple.Pair.getRight()"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object.__wrap(super(Pair, self).getKey())

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return Pair.__wrap(__Pair.ofNonNull(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString()"""
        return str.__wrap(super(Pair, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getLeft(self, ):
        """public abstract L org.apache.commons.lang3.tuple.Pair.getLeft()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int.__wrap(super(Pair, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.Pair()"""
        val = __Pair()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool.__wrap(super(__Pair, self).equals(arg0))

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int.__wrap(super(__Pair, self).compareTo(arg0))

    @staticmethod
    @overload
    def emptyArray() -> List['Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[Pair].__wrap(__Pair.emptyArray())

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return Pair.__wrap(__Pair.of(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.tuple.Triple
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.tuple.Triple as __Triple
__Triple = __Triple
from abc import abstractmethod, ABC
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
 
class Triple(ABC):
    """org.apache.commons.lang3.tuple.Triple"""
 
    @staticmethod
    def __wrap(java_value: __Triple) -> 'Triple':
        return Triple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Triple):
        """
        Dynamic initializer for Triple.
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
    def emptyArray() -> List['Triple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R>[] org.apache.commons.lang3.tuple.Triple.emptyArray()"""
        return List[Triple].__wrap(__Triple.emptyArray())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @abstractmethod
    def getMiddle(self, ):
        """public abstract M org.apache.commons.lang3.tuple.Triple.getMiddle()"""
        pass

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.Triple()"""
        val = __Triple()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.ofNonNull(L,M,R)"""
        return Triple.__wrap(__Triple.ofNonNull(arg0, arg1, arg2))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString(java.lang.String)"""
        return str.__wrap(super(__Triple, self).toString(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.Triple()"""
        val = __Triple()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def getRight(self, ):
        """public abstract R org.apache.commons.lang3.tuple.Triple.getRight()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Triple.equals(java.lang.Object)"""
        return bool.__wrap(super(__Triple, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compareTo(self, arg0: 'Triple') -> int:
        """public int org.apache.commons.lang3.tuple.Triple.compareTo(org.apache.commons.lang3.tuple.Triple<L, M, R>)"""
        return int.__wrap(super(__Triple, self).compareTo(arg0))

    @abstractmethod
    def getLeft(self, ):
        """public abstract L org.apache.commons.lang3.tuple.Triple.getLeft()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Triple.hashCode()"""
        return int.__wrap(super(Triple, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString()"""
        return str.__wrap(super(Triple, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.of(L,M,R)"""
        return Triple.__wrap(__Triple.of(arg0, arg1, arg2))