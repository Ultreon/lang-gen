from __future__ import annotations
from overload import overload


 
from builtins import str
import org.apache.commons.lang3.tuple.Triple as _Triple
_Triple = _Triple
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Triple():
    """org.apache.commons.lang3.tuple.Triple"""
 
    @staticmethod
    def _wrap(java_value: _Triple) -> 'Triple':
        return Triple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Triple):
        """
        Dynamic initializer for Triple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Triple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Triple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.of(L,M,R)"""
        return Triple._wrap(_Triple.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.ofNonNull(L,M,R)"""
        return Triple._wrap(_Triple.ofNonNull(arg0, arg1, arg2))

    @abstractmethod
    def getMiddle(self, ):
        """public abstract M org.apache.commons.lang3.tuple.Triple.getMiddle()"""
        pass

    @staticmethod
    @overload
    def emptyArray() -> List['Triple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R>[] org.apache.commons.lang3.tuple.Triple.emptyArray()"""
        return List[Triple]._wrap(_Triple.emptyArray())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Triple.hashCode()"""
        return int._wrap(super(Triple, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString()"""
        return str._wrap(super(Triple, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Triple.equals(java.lang.Object)"""
        return bool._wrap(super(_Triple, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.Triple()"""
        val = _Triple()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.Triple()"""
        val = _Triple()
        self.__wrapper = val

    @abstractmethod
    def getRight(self, ):
        """public abstract R org.apache.commons.lang3.tuple.Triple.getRight()"""
        pass

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def getLeft(self, ):
        """public abstract L org.apache.commons.lang3.tuple.Triple.getLeft()"""
        pass

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString(java.lang.String)"""
        return str._wrap(super(_Triple, self).toString(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Triple') -> int:
        """public int org.apache.commons.lang3.tuple.Triple.compareTo(org.apache.commons.lang3.tuple.Triple<L, M, R>)"""
        return int._wrap(super(_Triple, self).compareTo(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.tuple.Triple
from builtins import str
import org.apache.commons.lang3.tuple.Triple as _Triple
_Triple = _Triple
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Triple():
    """org.apache.commons.lang3.tuple.Triple"""
 
    @staticmethod
    def _wrap(java_value: _Triple) -> 'Triple':
        return Triple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Triple):
        """
        Dynamic initializer for Triple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Triple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Triple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.of(L,M,R)"""
        return Triple._wrap(_Triple.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.ofNonNull(L,M,R)"""
        return Triple._wrap(_Triple.ofNonNull(arg0, arg1, arg2))

    @abstractmethod
    def getMiddle(self, ):
        """public abstract M org.apache.commons.lang3.tuple.Triple.getMiddle()"""
        pass

    @staticmethod
    @overload
    def emptyArray() -> List['Triple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R>[] org.apache.commons.lang3.tuple.Triple.emptyArray()"""
        return List[Triple]._wrap(_Triple.emptyArray())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Triple.hashCode()"""
        return int._wrap(super(Triple, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString()"""
        return str._wrap(super(Triple, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Triple.equals(java.lang.Object)"""
        return bool._wrap(super(_Triple, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.Triple()"""
        val = _Triple()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.Triple()"""
        val = _Triple()
        self.__wrapper = val

    @abstractmethod
    def getRight(self, ):
        """public abstract R org.apache.commons.lang3.tuple.Triple.getRight()"""
        pass

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def getLeft(self, ):
        """public abstract L org.apache.commons.lang3.tuple.Triple.getLeft()"""
        pass

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString(java.lang.String)"""
        return str._wrap(super(_Triple, self).toString(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Triple') -> int:
        """public int org.apache.commons.lang3.tuple.Triple.compareTo(org.apache.commons.lang3.tuple.Triple<L, M, R>)"""
        return int._wrap(super(_Triple, self).compareTo(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.tuple.Triple 
 
 
# CLASS: org.apache.commons.lang3.tuple.ImmutablePair
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import org.apache.commons.lang3.tuple.ImmutablePair as _ImmutablePair
_ImmutablePair = _ImmutablePair
import org.apache.commons.lang3.tuple.Pair as _Pair
_Pair = _Pair
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImmutablePair():
    """org.apache.commons.lang3.tuple.ImmutablePair"""
 
    @staticmethod
    def _wrap(java_value: _ImmutablePair) -> 'ImmutablePair':
        return ImmutablePair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutablePair):
        """
        Dynamic initializer for ImmutablePair.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutablePair__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutablePair__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setValue(self, arg0: object) -> object:
        """public R org.apache.commons.lang3.tuple.ImmutablePair.setValue(R)"""
        return object._wrap(super(_ImmutablePair, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString()"""
        return str._wrap(super(Pair, self).toString())

    @staticmethod
    @overload
    def right(arg0: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.right(R)"""
        return Pair._wrap(_ImmutablePair.right(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str._wrap(super(_Pair, self).toString(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object._wrap(super(Pair, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object._wrap(super(Pair, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def emptyArray() -> List['ImmutablePair']:
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R>[] org.apache.commons.lang3.tuple.ImmutablePair.emptyArray()"""
        return List[ImmutablePair]._wrap(_ImmutablePair.emptyArray())

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
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.ImmutablePair.getRight()"""
        return object._wrap(super(ImmutablePair, self).getRight())

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return Pair._wrap(_Pair.of(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int._wrap(super(Pair, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool._wrap(super(_Pair, self).equals(arg0))

    @override
    @overload
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.ImmutablePair.getLeft()"""
        return object._wrap(super(ImmutablePair, self).getLeft())

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return Pair._wrap(_Pair.of(arg0, arg1))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return Pair._wrap(_Pair.ofNonNull(arg0, arg1))

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int._wrap(super(_Pair, self).compareTo(arg0))

    @staticmethod
    @overload
    def nullPair() -> 'ImmutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.nullPair()"""
        return ImmutablePair._wrap(_ImmutablePair.nullPair())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.lang3.tuple.ImmutablePair(L,R)"""
        val = _ImmutablePair(arg0, arg1)
        self.__wrapper = val

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'ImmutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.of(L,R)"""
        return ImmutablePair._wrap(_ImmutablePair.of(arg0, arg1))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'ImmutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.ofNonNull(L,R)"""
        return ImmutablePair._wrap(_ImmutablePair.ofNonNull(arg0, arg1))

    @staticmethod
    @overload
    def left(arg0: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.left(L)"""
        return Pair._wrap(_ImmutablePair.left(arg0))

    @staticmethod
    @overload
    def emptyArray() -> List['Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[Pair]._wrap(_Pair.emptyArray())

    @override
    @overload
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(_Pair, self).accept(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object._wrap(super(_Pair, self).apply(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'ImmutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.ImmutablePair<L, R> org.apache.commons.lang3.tuple.ImmutablePair.of(java.util.Map$Entry<L, R>)"""
        return ImmutablePair._wrap(_ImmutablePair.of(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.tuple.MutablePair
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.lang3.tuple.MutablePair as _MutablePair
_MutablePair = _MutablePair
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import org.apache.commons.lang3.tuple.Pair as _Pair
_Pair = _Pair
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutablePair():
    """org.apache.commons.lang3.tuple.MutablePair"""
 
    @staticmethod
    def _wrap(java_value: _MutablePair) -> 'MutablePair':
        return MutablePair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutablePair):
        """
        Dynamic initializer for MutablePair.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutablePair__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutablePair__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString()"""
        return str._wrap(super(Pair, self).toString())

    @override
    @overload
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.MutablePair.getLeft()"""
        return object._wrap(super(MutablePair, self).getLeft())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str._wrap(super(_Pair, self).toString(arg0))

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.lang3.tuple.MutablePair(L,R)"""
        val = _MutablePair(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object._wrap(super(Pair, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object._wrap(super(Pair, self).getKey())

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.of(L,R)"""
        return MutablePair._wrap(_MutablePair.of(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.of(java.util.Map$Entry<L, R>)"""
        return MutablePair._wrap(_MutablePair.of(arg0))

    @overload
    def setRight(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutablePair.setRight(R)"""
        super(_MutablePair, self).setRight(arg0)

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
    def setLeft(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutablePair.setLeft(L)"""
        super(_MutablePair, self).setLeft(arg0)

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return Pair._wrap(_Pair.of(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int._wrap(super(Pair, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool._wrap(super(_Pair, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.MutablePair()"""
        val = _MutablePair()
        self.__wrapper = val

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return Pair._wrap(_Pair.of(arg0, arg1))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return Pair._wrap(_Pair.ofNonNull(arg0, arg1))

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int._wrap(super(_Pair, self).compareTo(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.MutablePair()"""
        val = _MutablePair()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setValue(self, arg0: object) -> object:
        """public R org.apache.commons.lang3.tuple.MutablePair.setValue(R)"""
        return object._wrap(super(_MutablePair, self).setValue(arg0))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'MutablePair':
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R> org.apache.commons.lang3.tuple.MutablePair.ofNonNull(L,R)"""
        return MutablePair._wrap(_MutablePair.ofNonNull(arg0, arg1))

    @staticmethod
    @overload
    def emptyArray() -> List['Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[Pair]._wrap(_Pair.emptyArray())

    @override
    @overload
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(_Pair, self).accept(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def emptyArray() -> List['MutablePair']:
        """public static <L,R> org.apache.commons.lang3.tuple.MutablePair<L, R>[] org.apache.commons.lang3.tuple.MutablePair.emptyArray()"""
        return List[MutablePair]._wrap(_MutablePair.emptyArray())

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object._wrap(super(_Pair, self).apply(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.MutablePair.getRight()"""
        return object._wrap(super(MutablePair, self).getRight()) 
 
 
# CLASS: org.apache.commons.lang3.tuple.MutableTriple
from builtins import str
import org.apache.commons.lang3.tuple.Triple as _Triple
_Triple = _Triple
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.lang3.tuple.MutableTriple as _MutableTriple
_MutableTriple = _MutableTriple
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableTriple():
    """org.apache.commons.lang3.tuple.MutableTriple"""
 
    @staticmethod
    def _wrap(java_value: _MutableTriple) -> 'MutableTriple':
        return MutableTriple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableTriple):
        """
        Dynamic initializer for MutableTriple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableTriple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableTriple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.of(L,M,R)"""
        return Triple._wrap(_Triple.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def emptyArray() -> List['Triple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R>[] org.apache.commons.lang3.tuple.Triple.emptyArray()"""
        return List[Triple]._wrap(_Triple.emptyArray())

    @overload
    def setRight(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutableTriple.setRight(R)"""
        super(_MutableTriple, self).setRight(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def setMiddle(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutableTriple.setMiddle(M)"""
        super(_MutableTriple, self).setMiddle(arg0)

    @override
    @overload
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.MutableTriple.getLeft()"""
        return object._wrap(super(MutableTriple, self).getLeft())

    @overload
    def setLeft(self, arg0: object):
        """public void org.apache.commons.lang3.tuple.MutableTriple.setLeft(L)"""
        super(_MutableTriple, self).setLeft(arg0)

    @overload
    def compareTo(self, arg0: 'Triple') -> int:
        """public int org.apache.commons.lang3.tuple.Triple.compareTo(org.apache.commons.lang3.tuple.Triple<L, M, R>)"""
        return int._wrap(super(_Triple, self).compareTo(arg0))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'MutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.MutableTriple<L, M, R> org.apache.commons.lang3.tuple.MutableTriple.ofNonNull(L,M,R)"""
        return MutableTriple._wrap(_MutableTriple.ofNonNull(arg0, arg1, arg2))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.ofNonNull(L,M,R)"""
        return Triple._wrap(_Triple.ofNonNull(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def emptyArray() -> List['MutableTriple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.MutableTriple<L, M, R>[] org.apache.commons.lang3.tuple.MutableTriple.emptyArray()"""
        return List[MutableTriple]._wrap(_MutableTriple.emptyArray())

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'MutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.MutableTriple<L, M, R> org.apache.commons.lang3.tuple.MutableTriple.of(L,M,R)"""
        return MutableTriple._wrap(_MutableTriple.of(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Triple.hashCode()"""
        return int._wrap(super(Triple, self).hashCode())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public org.apache.commons.lang3.tuple.MutableTriple(L,M,R)"""
        val = _MutableTriple(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString()"""
        return str._wrap(super(Triple, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.MutableTriple()"""
        val = _MutableTriple()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Triple.equals(java.lang.Object)"""
        return bool._wrap(super(_Triple, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString(java.lang.String)"""
        return str._wrap(super(_Triple, self).toString(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.MutableTriple()"""
        val = _MutableTriple()
        self.__wrapper = val

    @override
    @overload
    def getMiddle(self) -> object:
        """public M org.apache.commons.lang3.tuple.MutableTriple.getMiddle()"""
        return object._wrap(super(MutableTriple, self).getMiddle())

    @override
    @overload
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.MutableTriple.getRight()"""
        return object._wrap(super(MutableTriple, self).getRight()) 
 
 
# CLASS: org.apache.commons.lang3.tuple.ImmutableTriple
from builtins import str
import org.apache.commons.lang3.tuple.Triple as _Triple
_Triple = _Triple
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import org.apache.commons.lang3.tuple.ImmutableTriple as _ImmutableTriple
_ImmutableTriple = _ImmutableTriple
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableTriple():
    """org.apache.commons.lang3.tuple.ImmutableTriple"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableTriple) -> 'ImmutableTriple':
        return ImmutableTriple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableTriple):
        """
        Dynamic initializer for ImmutableTriple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableTriple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableTriple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.of(L,M,R)"""
        return Triple._wrap(_Triple.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'Triple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R> org.apache.commons.lang3.tuple.Triple.ofNonNull(L,M,R)"""
        return Triple._wrap(_Triple.ofNonNull(arg0, arg1, arg2))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object, arg2: object) -> 'ImmutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.ImmutableTriple<L, M, R> org.apache.commons.lang3.tuple.ImmutableTriple.ofNonNull(L,M,R)"""
        return ImmutableTriple._wrap(_ImmutableTriple.ofNonNull(arg0, arg1, arg2))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> 'ImmutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.ImmutableTriple<L, M, R> org.apache.commons.lang3.tuple.ImmutableTriple.of(L,M,R)"""
        return ImmutableTriple._wrap(_ImmutableTriple.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def emptyArray() -> List['Triple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.Triple<L, M, R>[] org.apache.commons.lang3.tuple.Triple.emptyArray()"""
        return List[Triple]._wrap(_Triple.emptyArray())

    @override
    @overload
    def getRight(self) -> object:
        """public R org.apache.commons.lang3.tuple.ImmutableTriple.getRight()"""
        return object._wrap(super(ImmutableTriple, self).getRight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Triple.hashCode()"""
        return int._wrap(super(Triple, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString()"""
        return str._wrap(super(Triple, self).toString())

    @override
    @overload
    def getMiddle(self) -> object:
        """public M org.apache.commons.lang3.tuple.ImmutableTriple.getMiddle()"""
        return object._wrap(super(ImmutableTriple, self).getMiddle())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Triple.equals(java.lang.Object)"""
        return bool._wrap(super(_Triple, self).equals(arg0))

    @staticmethod
    @overload
    def nullTriple() -> 'ImmutableTriple':
        """public static <L,M,R> org.apache.commons.lang3.tuple.ImmutableTriple<L, M, R> org.apache.commons.lang3.tuple.ImmutableTriple.nullTriple()"""
        return ImmutableTriple._wrap(_ImmutableTriple.nullTriple())

    @staticmethod
    @overload
    def emptyArray() -> List['ImmutableTriple']:
        """public static <L,M,R> org.apache.commons.lang3.tuple.ImmutableTriple<L, M, R>[] org.apache.commons.lang3.tuple.ImmutableTriple.emptyArray()"""
        return List[ImmutableTriple]._wrap(_ImmutableTriple.emptyArray())

    @override
    @overload
    def getLeft(self) -> object:
        """public L org.apache.commons.lang3.tuple.ImmutableTriple.getLeft()"""
        return object._wrap(super(ImmutableTriple, self).getLeft())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Triple.toString(java.lang.String)"""
        return str._wrap(super(_Triple, self).toString(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public org.apache.commons.lang3.tuple.ImmutableTriple(L,M,R)"""
        val = _ImmutableTriple(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Triple') -> int:
        """public int org.apache.commons.lang3.tuple.Triple.compareTo(org.apache.commons.lang3.tuple.Triple<L, M, R>)"""
        return int._wrap(super(_Triple, self).compareTo(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.tuple.Pair
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from abc import abstractmethod, ABC
from typing import List
import java.lang.String as _string
import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import java.util.Map as _Map_Entry
_Entry = _Map_Entry.Entry
import org.apache.commons.lang3.tuple.Pair as _Pair
_Pair = _Pair
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pair():
    """org.apache.commons.lang3.tuple.Pair"""
 
    @staticmethod
    def _wrap(java_value: _Pair) -> 'Pair':
        return Pair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pair):
        """
        Dynamic initializer for Pair.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pair__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pair__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool._wrap(super(_Pair, self).equals(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return Pair._wrap(_Pair.of(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString()"""
        return str._wrap(super(Pair, self).toString())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str._wrap(super(_Pair, self).toString(arg0))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return Pair._wrap(_Pair.ofNonNull(arg0, arg1))

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int._wrap(super(_Pair, self).compareTo(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract V java.util.Map$Entry.setValue(V)"""
        pass

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object._wrap(super(Pair, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object._wrap(super(Pair, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.tuple.Pair()"""
        val = _Pair()
        self.__wrapper = val

    @abstractmethod
    def getRight(self, ):
        """public abstract R org.apache.commons.lang3.tuple.Pair.getRight()"""
        pass

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.tuple.Pair()"""
        val = _Pair()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def emptyArray() -> List['Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[Pair]._wrap(_Pair.emptyArray())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(_Pair, self).accept(arg0)

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object._wrap(super(_Pair, self).apply(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int._wrap(super(Pair, self).hashCode())

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return Pair._wrap(_Pair.of(arg0))