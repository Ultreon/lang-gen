from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.libs.collections.v0.util.Range as __Range
__Range = __Range
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.libs.collections.v0.iterator.DoubleIterable as __DoubleIterable
__DoubleIterable = __DoubleIterable
try:
    from pycorelibs.collections.v0 import iterator
except ImportError:
    iterator = __import_once__("pycorelibs.collections.v0.iterator")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.collections.v0.iterator.DoubleIterator as __DoubleIterator
__DoubleIterator = __DoubleIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Range():
    """dev.ultreon.libs.collections.v0.util.Range"""
 
    @staticmethod
    def __wrap(java_value: __Range) -> 'Range':
        return Range(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Range):
        """
        Dynamic initializer for Range.
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
    def __init__(self, arg0: float):
        """public dev.ultreon.libs.collections.v0.util.Range(double)"""
        val = __Range(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.collections.v0.util.Range(double,double)"""
        val = __Range(__double.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def contains(self, arg0: float) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.util.Range.contains(double)"""
        return bool.__wrap(super(__Range, self).contains(__double.valueOf(arg0)))

    @overload
    def iterator(self) -> 'iterator.DoubleIterator':
        """public dev.ultreon.libs.collections.v0.iterator.DoubleIterator dev.ultreon.libs.collections.v0.util.Range.iterator()"""
        return 'iterator.DoubleIterator'.__wrap(super(Range, self).iterator())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.util.Range.equals(java.lang.Object)"""
        return bool.__wrap(super(__Range, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.util.Range.hashCode()"""
        return int.__wrap(super(Range, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def start(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.start()"""
        return float.__wrap(super(Range, self).start())

    @overload
    def end(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.end()"""
        return float.__wrap(super(Range, self).end())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.util.Range.toString()"""
        return str.__wrap(super(Range, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def step(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.step()"""
        return float.__wrap(super(Range, self).step())

    @overload
    def iterable(self) -> 'iterator.DoubleIterable':
        """public dev.ultreon.libs.collections.v0.iterator.DoubleIterable dev.ultreon.libs.collections.v0.util.Range.iterable()"""
        return 'iterator.DoubleIterable'.__wrap(super(Range, self).iterable())

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.util.Range
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.libs.collections.v0.util.Range as __Range
__Range = __Range
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.libs.collections.v0.iterator.DoubleIterable as __DoubleIterable
__DoubleIterable = __DoubleIterable
try:
    from pycorelibs.collections.v0 import iterator
except ImportError:
    iterator = __import_once__("pycorelibs.collections.v0.iterator")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.collections.v0.iterator.DoubleIterator as __DoubleIterator
__DoubleIterator = __DoubleIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Range():
    """dev.ultreon.libs.collections.v0.util.Range"""
 
    @staticmethod
    def __wrap(java_value: __Range) -> 'Range':
        return Range(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Range):
        """
        Dynamic initializer for Range.
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
    def __init__(self, arg0: float):
        """public dev.ultreon.libs.collections.v0.util.Range(double)"""
        val = __Range(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.collections.v0.util.Range(double,double)"""
        val = __Range(__double.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def contains(self, arg0: float) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.util.Range.contains(double)"""
        return bool.__wrap(super(__Range, self).contains(__double.valueOf(arg0)))

    @overload
    def iterator(self) -> 'iterator.DoubleIterator':
        """public dev.ultreon.libs.collections.v0.iterator.DoubleIterator dev.ultreon.libs.collections.v0.util.Range.iterator()"""
        return 'iterator.DoubleIterator'.__wrap(super(Range, self).iterator())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.util.Range.equals(java.lang.Object)"""
        return bool.__wrap(super(__Range, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.util.Range.hashCode()"""
        return int.__wrap(super(Range, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def start(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.start()"""
        return float.__wrap(super(Range, self).start())

    @overload
    def end(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.end()"""
        return float.__wrap(super(Range, self).end())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.util.Range.toString()"""
        return str.__wrap(super(Range, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def step(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.step()"""
        return float.__wrap(super(Range, self).step())

    @overload
    def iterable(self) -> 'iterator.DoubleIterable':
        """public dev.ultreon.libs.collections.v0.iterator.DoubleIterable dev.ultreon.libs.collections.v0.util.Range.iterable()"""
        return 'iterator.DoubleIterable'.__wrap(super(Range, self).iterable())

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.util.Range 
 
 
# CLASS: dev.ultreon.libs.collections.v0.util.ArrayUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.collections.v0.util.ArrayUtils as __ArrayUtils
__ArrayUtils = __ArrayUtils
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ArrayUtils():
    """dev.ultreon.libs.collections.v0.util.ArrayUtils"""
 
    @staticmethod
    def __wrap(java_value: __ArrayUtils) -> 'ArrayUtils':
        return ArrayUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayUtils):
        """
        Dynamic initializer for ArrayUtils.
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
        """public dev.ultreon.libs.collections.v0.util.ArrayUtils()"""
        val = __ArrayUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.util.ArrayUtils()"""
        val = __ArrayUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def add(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] dev.ultreon.libs.collections.v0.util.ArrayUtils.add(T[],T)"""
        return List[object].__wrap(__ArrayUtils.add(arg0, arg1))

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