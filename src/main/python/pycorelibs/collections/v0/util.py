from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.collections.v0.util.ArrayUtils as _ArrayUtils
_ArrayUtils = _ArrayUtils
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayUtils():
    """dev.ultreon.libs.collections.v0.util.ArrayUtils"""
 
    @staticmethod
    def _wrap(java_value: _ArrayUtils) -> 'ArrayUtils':
        return ArrayUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayUtils):
        """
        Dynamic initializer for ArrayUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def add(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] dev.ultreon.libs.collections.v0.util.ArrayUtils.add(T[],T)"""
        return List[object]._wrap(_ArrayUtils.add(arg0, arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.util.ArrayUtils()"""
        val = _ArrayUtils()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.util.ArrayUtils()"""
        val = _ArrayUtils()
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.util.ArrayUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.collections.v0.util.ArrayUtils as _ArrayUtils
_ArrayUtils = _ArrayUtils
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayUtils():
    """dev.ultreon.libs.collections.v0.util.ArrayUtils"""
 
    @staticmethod
    def _wrap(java_value: _ArrayUtils) -> 'ArrayUtils':
        return ArrayUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayUtils):
        """
        Dynamic initializer for ArrayUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def add(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] dev.ultreon.libs.collections.v0.util.ArrayUtils.add(T[],T)"""
        return List[object]._wrap(_ArrayUtils.add(arg0, arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.util.ArrayUtils()"""
        val = _ArrayUtils()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.util.ArrayUtils()"""
        val = _ArrayUtils()
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.util.ArrayUtils 
 
 
# CLASS: dev.ultreon.libs.collections.v0.util.Range
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import dev.ultreon.libs.collections.v0.iterator.DoubleIterator as _DoubleIterator
_DoubleIterator = _DoubleIterator
try:
    from pycorelibs.collections.v0 import iterator
except ImportError:
    iterator = _import_once("pycorelibs.collections.v0.iterator")

import java.lang.String as _String
_String = _String
import dev.ultreon.libs.collections.v0.util.Range as _Range
_Range = _Range
import dev.ultreon.libs.collections.v0.iterator.DoubleIterable as _DoubleIterable
_DoubleIterable = _DoubleIterable
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Range():
    """dev.ultreon.libs.collections.v0.util.Range"""
 
    @staticmethod
    def _wrap(java_value: _Range) -> 'Range':
        return Range(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Range):
        """
        Dynamic initializer for Range.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Range__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Range__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.util.Range.toString()"""
        return str._wrap(super(Range, self).toString())

    @overload
    def end(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.end()"""
        return float._wrap(super(Range, self).end())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def start(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.start()"""
        return float._wrap(super(Range, self).start())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.util.Range.hashCode()"""
        return int._wrap(super(Range, self).hashCode())

    @overload
    def step(self) -> float:
        """public double dev.ultreon.libs.collections.v0.util.Range.step()"""
        return float._wrap(super(Range, self).step())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def iterable(self) -> 'iterator.DoubleIterable':
        """public dev.ultreon.libs.collections.v0.iterator.DoubleIterable dev.ultreon.libs.collections.v0.util.Range.iterable()"""
        return 'iterator.DoubleIterable'._wrap(super(Range, self).iterable())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.collections.v0.util.Range(double,double)"""
        val = _Range(_double.valueOf(arg0), _double.valueOf(arg1))
        self.__wrapper = val

    @overload
    def iterator(self) -> 'iterator.DoubleIterator':
        """public dev.ultreon.libs.collections.v0.iterator.DoubleIterator dev.ultreon.libs.collections.v0.util.Range.iterator()"""
        return 'iterator.DoubleIterator'._wrap(super(Range, self).iterator())

    @overload
    def contains(self, arg0: float) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.util.Range.contains(double)"""
        return bool._wrap(super(_Range, self).contains(_double.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.libs.collections.v0.util.Range(double)"""
        val = _Range(_double.valueOf(arg0))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.util.Range.equals(java.lang.Object)"""
        return bool._wrap(super(_Range, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()