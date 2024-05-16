from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.NullPredicate as _NullPredicate
_NullPredicate = _NullPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullPredicate():
    """org.apache.commons.collections4.functors.NullPredicate"""
 
    @staticmethod
    def _wrap(java_value: _NullPredicate) -> 'NullPredicate':
        return NullPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullPredicate):
        """
        Dynamic initializer for NullPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullPredicate.evaluate(T)"""
        return bool._wrap(super(_NullPredicate, self).evaluate(arg0))

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

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nullPredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullPredicate.nullPredicate()"""
        return collections4.Predicate._wrap(_NullPredicate.nullPredicate())

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

 
 
 
# CLASS: org.apache.commons.collections4.functors.NullPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.NullPredicate as _NullPredicate
_NullPredicate = _NullPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullPredicate():
    """org.apache.commons.collections4.functors.NullPredicate"""
 
    @staticmethod
    def _wrap(java_value: _NullPredicate) -> 'NullPredicate':
        return NullPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullPredicate):
        """
        Dynamic initializer for NullPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullPredicate.evaluate(T)"""
        return bool._wrap(super(_NullPredicate, self).evaluate(arg0))

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

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nullPredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullPredicate.nullPredicate()"""
        return collections4.Predicate._wrap(_NullPredicate.nullPredicate())

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

 
 
 
# CLASS: org.apache.commons.collections4.functors.NullPredicate 
 
 
# CLASS: org.apache.commons.collections4.functors.InstanceofPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import org.apache.commons.collections4.functors.InstanceofPredicate as _InstanceofPredicate
_InstanceofPredicate = _InstanceofPredicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class InstanceofPredicate():
    """org.apache.commons.collections4.functors.InstanceofPredicate"""
 
    @staticmethod
    def _wrap(java_value: _InstanceofPredicate) -> 'InstanceofPredicate':
        return InstanceofPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InstanceofPredicate):
        """
        Dynamic initializer for InstanceofPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InstanceofPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InstanceofPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<?> org.apache.commons.collections4.functors.InstanceofPredicate.getType()"""
        return 'type.Class'._wrap(super(InstanceofPredicate, self).getType())

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.InstanceofPredicate.evaluate(java.lang.Object)"""
        return bool._wrap(super(_InstanceofPredicate, self).evaluate(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def instanceOfPredicate(arg0: 'Class') -> 'collections4.Predicate':
        """public static org.apache.commons.collections4.Predicate<java.lang.Object> org.apache.commons.collections4.functors.InstanceofPredicate.instanceOfPredicate(java.lang.Class<?>)"""
        return collections4.Predicate._wrap(_InstanceofPredicate.instanceOfPredicate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.collections4.functors.InstanceofPredicate(java.lang.Class<?>)"""
        val = _InstanceofPredicate(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.PrototypeFactory
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.PrototypeFactory as _PrototypeFactory
_PrototypeFactory = _PrototypeFactory
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.Factory as _Factory
_Factory = _Factory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PrototypeFactory():
    """org.apache.commons.collections4.functors.PrototypeFactory"""
 
    @staticmethod
    def _wrap(java_value: _PrototypeFactory) -> 'PrototypeFactory':
        return PrototypeFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrototypeFactory):
        """
        Dynamic initializer for PrototypeFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrototypeFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrototypeFactory__wrapper":
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
    def prototypeFactory(arg0: object) -> 'collections4.Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.functors.PrototypeFactory.prototypeFactory(T)"""
        return collections4.Factory._wrap(_PrototypeFactory.prototypeFactory(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.functors.NullIsExceptionPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.NullIsExceptionPredicate as _NullIsExceptionPredicate
_NullIsExceptionPredicate = _NullIsExceptionPredicate
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullIsExceptionPredicate():
    """org.apache.commons.collections4.functors.NullIsExceptionPredicate"""
 
    @staticmethod
    def _wrap(java_value: _NullIsExceptionPredicate) -> 'NullIsExceptionPredicate':
        return NullIsExceptionPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullIsExceptionPredicate):
        """
        Dynamic initializer for NullIsExceptionPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullIsExceptionPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullIsExceptionPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nullIsExceptionPredicate(arg0: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullIsExceptionPredicate.nullIsExceptionPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate._wrap(_NullIsExceptionPredicate.nullIsExceptionPredicate(arg0))

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.NullIsExceptionPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(NullIsExceptionPredicate, self).getPredicates())

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
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.NullIsExceptionPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        val = _NullIsExceptionPredicate(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullIsExceptionPredicate.evaluate(T)"""
        return bool._wrap(super(_NullIsExceptionPredicate, self).evaluate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.ExceptionPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.functors.ExceptionPredicate as _ExceptionPredicate
_ExceptionPredicate = _ExceptionPredicate
import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExceptionPredicate():
    """org.apache.commons.collections4.functors.ExceptionPredicate"""
 
    @staticmethod
    def _wrap(java_value: _ExceptionPredicate) -> 'ExceptionPredicate':
        return ExceptionPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExceptionPredicate):
        """
        Dynamic initializer for ExceptionPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExceptionPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExceptionPredicate__wrapper":
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
    def exceptionPredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.ExceptionPredicate.exceptionPredicate()"""
        return collections4.Predicate._wrap(_ExceptionPredicate.exceptionPredicate())

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.ExceptionPredicate.evaluate(T)"""
        return bool._wrap(super(_ExceptionPredicate, self).evaluate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.PredicateDecorator
import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import org.apache.commons.collections4.functors.PredicateDecorator as _PredicateDecorator
_PredicateDecorator = _PredicateDecorator
from abc import abstractmethod, ABC
 
class PredicateDecorator():
    """org.apache.commons.collections4.functors.PredicateDecorator"""
 
    @staticmethod
    def _wrap(java_value: _PredicateDecorator) -> 'PredicateDecorator':
        return PredicateDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicateDecorator):
        """
        Dynamic initializer for PredicateDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicateDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicateDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getPredicates(self, ):
        """public abstract org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.PredicateDecorator.getPredicates()"""
        pass

    @abstractmethod
    def evaluate(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Predicate.evaluate(T)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.functors.ComparatorPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.functors.ComparatorPredicate as _ComparatorPredicate
_ComparatorPredicate = _ComparatorPredicate
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComparatorPredicate():
    """org.apache.commons.collections4.functors.ComparatorPredicate"""
 
    @staticmethod
    def _wrap(java_value: _ComparatorPredicate) -> 'ComparatorPredicate':
        return ComparatorPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComparatorPredicate):
        """
        Dynamic initializer for ComparatorPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComparatorPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComparatorPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: 'Comparator', arg2: 'Criterion'):
        """public org.apache.commons.collections4.functors.ComparatorPredicate(T,java.util.Comparator<T>,org.apache.commons.collections4.functors.ComparatorPredicate$Criterion)"""
        val = _ComparatorPredicate(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.ComparatorPredicate.evaluate(T)"""
        return bool._wrap(super(_ComparatorPredicate, self).evaluate(arg0))

    @staticmethod
    @overload
    def comparatorPredicate(arg0: object, arg1: 'Comparator', arg2: 'Criterion') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.ComparatorPredicate.comparatorPredicate(T,java.util.Comparator<T>,org.apache.commons.collections4.functors.ComparatorPredicate$Criterion)"""
        return collections4.Predicate._wrap(_ComparatorPredicate.comparatorPredicate(arg0, arg1, arg2))

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

    @staticmethod
    @overload
    def comparatorPredicate(arg0: object, arg1: 'Comparator') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.ComparatorPredicate.comparatorPredicate(T,java.util.Comparator<T>)"""
        return collections4.Predicate._wrap(_ComparatorPredicate.comparatorPredicate(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.AllPredicate
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.functors.AllPredicate as _AllPredicate
_AllPredicate = _AllPredicate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as _AbstractQuantifierPredicate
_AbstractQuantifierPredicate = _AbstractQuantifierPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AllPredicate():
    """org.apache.commons.collections4.functors.AllPredicate"""
 
    @staticmethod
    def _wrap(java_value: _AllPredicate) -> 'AllPredicate':
        return AllPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AllPredicate):
        """
        Dynamic initializer for AllPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AllPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AllPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def allPredicate(*arg0: 'collections4.Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AllPredicate.allPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return collections4.Predicate._wrap(_AllPredicate.allPredicate(arg0))

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.AllPredicate.evaluate(T)"""
        return bool._wrap(super(_AllPredicate, self).evaluate(arg0))

    @staticmethod
    @overload
    def allPredicate(arg0: 'Collection') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AllPredicate.allPredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return collections4.Predicate._wrap(_AllPredicate.allPredicate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(AbstractQuantifierPredicate, self).getPredicates())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.AllPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = _AllPredicate(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.FactoryTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.functors.FactoryTransformer as _FactoryTransformer
_FactoryTransformer = _FactoryTransformer
import org.apache.commons.collections4.Factory as _Factory
_Factory = _Factory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FactoryTransformer():
    """org.apache.commons.collections4.functors.FactoryTransformer"""
 
    @staticmethod
    def _wrap(java_value: _FactoryTransformer) -> 'FactoryTransformer':
        return FactoryTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FactoryTransformer):
        """
        Dynamic initializer for FactoryTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FactoryTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FactoryTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.FactoryTransformer.transform(I)"""
        return object._wrap(super(_FactoryTransformer, self).transform(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def __init__(self, arg0: 'Factory'):
        """public org.apache.commons.collections4.functors.FactoryTransformer(org.apache.commons.collections4.Factory<? extends O>)"""
        val = _FactoryTransformer(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def factoryTransformer(arg0: 'Factory') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.FactoryTransformer.factoryTransformer(org.apache.commons.collections4.Factory<? extends O>)"""
        return collections4.Transformer._wrap(_FactoryTransformer.factoryTransformer(arg0))

    @overload
    def getFactory(self) -> 'collections4.Factory':
        """public org.apache.commons.collections4.Factory<? extends O> org.apache.commons.collections4.functors.FactoryTransformer.getFactory()"""
        return 'collections4.Factory'._wrap(super(FactoryTransformer, self).getFactory())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.ForClosure
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.functors.ForClosure as _ForClosure
_ForClosure = _ForClosure
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ForClosure():
    """org.apache.commons.collections4.functors.ForClosure"""
 
    @staticmethod
    def _wrap(java_value: _ForClosure) -> 'ForClosure':
        return ForClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForClosure):
        """
        Dynamic initializer for ForClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: 'Closure'):
        """public org.apache.commons.collections4.functors.ForClosure(int,org.apache.commons.collections4.Closure<? super E>)"""
        val = _ForClosure(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.ForClosure.getClosure()"""
        return 'collections4.Closure'._wrap(super(ForClosure, self).getClosure())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.ForClosure.execute(E)"""
        super(_ForClosure, self).execute(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def forClosure(arg0: int, arg1: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ForClosure.forClosure(int,org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure._wrap(_ForClosure.forClosure(_int.valueOf(arg0), arg1))

    @overload
    def getCount(self) -> int:
        """public int org.apache.commons.collections4.functors.ForClosure.getCount()"""
        return int._wrap(super(ForClosure, self).getCount())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.IfClosure
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.IfClosure as _IfClosure
_IfClosure = _IfClosure
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IfClosure():
    """org.apache.commons.collections4.functors.IfClosure"""
 
    @staticmethod
    def _wrap(java_value: _IfClosure) -> 'IfClosure':
        return IfClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IfClosure):
        """
        Dynamic initializer for IfClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IfClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IfClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.IfClosure.execute(E)"""
        super(_IfClosure, self).execute(arg0)

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Closure'):
        """public org.apache.commons.collections4.functors.IfClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        val = _IfClosure(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure'):
        """public org.apache.commons.collections4.functors.IfClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        val = _IfClosure(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ifClosure(arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.IfClosure.ifClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure._wrap(_IfClosure.ifClosure(arg0, arg1, arg2))

    @staticmethod
    @overload
    def ifClosure(arg0: 'Predicate', arg1: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.IfClosure.ifClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure._wrap(_IfClosure.ifClosure(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getTrueClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.IfClosure.getTrueClosure()"""
        return 'collections4.Closure'._wrap(super(IfClosure, self).getTrueClosure())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getFalseClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.IfClosure.getFalseClosure()"""
        return 'collections4.Closure'._wrap(super(IfClosure, self).getFalseClosure())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.functors.IfClosure.getPredicate()"""
        return 'collections4.Predicate'._wrap(super(IfClosure, self).getPredicate())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.InstantiateFactory
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.functors.InstantiateFactory as _InstantiateFactory
_InstantiateFactory = _InstantiateFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.Factory as _Factory
_Factory = _Factory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InstantiateFactory():
    """org.apache.commons.collections4.functors.InstantiateFactory"""
 
    @staticmethod
    def _wrap(java_value: _InstantiateFactory) -> 'InstantiateFactory':
        return InstantiateFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InstantiateFactory):
        """
        Dynamic initializer for InstantiateFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InstantiateFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InstantiateFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def instantiateFactory(arg0: 'Class', arg1: 'Class', arg2: 'Object') -> 'collections4.Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.functors.InstantiateFactory.instantiateFactory(java.lang.Class<T>,java.lang.Class<?>[],java.lang.Object[])"""
        return collections4.Factory._wrap(_InstantiateFactory.instantiateFactory(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.collections4.functors.InstantiateFactory(java.lang.Class<T>)"""
        val = _InstantiateFactory(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def create(self) -> object:
        """public T org.apache.commons.collections4.functors.InstantiateFactory.create()"""
        return object._wrap(super(InstantiateFactory, self).create())

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
    def __init__(self, arg0: 'Class', arg1: 'Class', arg2: 'Object'):
        """public org.apache.commons.collections4.functors.InstantiateFactory(java.lang.Class<T>,java.lang.Class<?>[],java.lang.Object[])"""
        val = _InstantiateFactory(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.UniquePredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.UniquePredicate as _UniquePredicate
_UniquePredicate = _UniquePredicate
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UniquePredicate():
    """org.apache.commons.collections4.functors.UniquePredicate"""
 
    @staticmethod
    def _wrap(java_value: _UniquePredicate) -> 'UniquePredicate':
        return UniquePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UniquePredicate):
        """
        Dynamic initializer for UniquePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UniquePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UniquePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.functors.UniquePredicate()"""
        val = _UniquePredicate()
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.functors.UniquePredicate()"""
        val = _UniquePredicate()
        self.__wrapper = val

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.UniquePredicate.evaluate(T)"""
        return bool._wrap(super(_UniquePredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def uniquePredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.UniquePredicate.uniquePredicate()"""
        return collections4.Predicate._wrap(_UniquePredicate.uniquePredicate())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.SwitchTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.functors.SwitchTransformer as _SwitchTransformer
_SwitchTransformer = _SwitchTransformer
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SwitchTransformer():
    """org.apache.commons.collections4.functors.SwitchTransformer"""
 
    @staticmethod
    def _wrap(java_value: _SwitchTransformer) -> 'SwitchTransformer':
        return SwitchTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SwitchTransformer):
        """
        Dynamic initializer for SwitchTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SwitchTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SwitchTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super I>[] org.apache.commons.collections4.functors.SwitchTransformer.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(SwitchTransformer, self).getPredicates())

    @overload
    def getDefaultTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O> org.apache.commons.collections4.functors.SwitchTransformer.getDefaultTransformer()"""
        return 'collections4.Transformer'._wrap(super(SwitchTransformer, self).getDefaultTransformer())

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
    def __init__(self, arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer'):
        """public org.apache.commons.collections4.functors.SwitchTransformer(org.apache.commons.collections4.Predicate<? super I>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = _SwitchTransformer(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTransformers(self) -> List['collections4.Transformer']:
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O>[] org.apache.commons.collections4.functors.SwitchTransformer.getTransformers()"""
        return List['collections4.Transformer']._wrap(super(SwitchTransformer, self).getTransformers())

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

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Map') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.SwitchTransformer.switchTransformer(java.util.Map<? extends org.apache.commons.collections4.Predicate<? super I>, ? extends org.apache.commons.collections4.Transformer<? super I, ? extends O>>)"""
        return collections4.Transformer._wrap(_SwitchTransformer.switchTransformer(arg0))

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.SwitchTransformer.switchTransformer(org.apache.commons.collections4.Predicate<? super I>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return collections4.Transformer._wrap(_SwitchTransformer.switchTransformer(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.SwitchTransformer.transform(I)"""
        return object._wrap(super(_SwitchTransformer, self).transform(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.TransformedPredicate
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.functors.TransformedPredicate as _TransformedPredicate
_TransformedPredicate = _TransformedPredicate
import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedPredicate():
    """org.apache.commons.collections4.functors.TransformedPredicate"""
 
    @staticmethod
    def _wrap(java_value: _TransformedPredicate) -> 'TransformedPredicate':
        return TransformedPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedPredicate):
        """
        Dynamic initializer for TransformedPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def transformedPredicate(arg0: 'Transformer', arg1: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.TransformedPredicate.transformedPredicate(org.apache.commons.collections4.Transformer<? super T, ? extends T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate._wrap(_TransformedPredicate.transformedPredicate(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Transformer', arg1: 'Predicate'):
        """public org.apache.commons.collections4.functors.TransformedPredicate(org.apache.commons.collections4.Transformer<? super T, ? extends T>,org.apache.commons.collections4.Predicate<? super T>)"""
        val = _TransformedPredicate(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.TransformedPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(TransformedPredicate, self).getPredicates())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.TransformedPredicate.evaluate(T)"""
        return bool._wrap(super(_TransformedPredicate, self).evaluate(arg0))

    @overload
    def getTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super T, ? extends T> org.apache.commons.collections4.functors.TransformedPredicate.getTransformer()"""
        return 'collections4.Transformer'._wrap(super(TransformedPredicate, self).getTransformer())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.ChainedClosure
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.functors.ChainedClosure as _ChainedClosure
_ChainedClosure = _ChainedClosure
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChainedClosure():
    """org.apache.commons.collections4.functors.ChainedClosure"""
 
    @staticmethod
    def _wrap(java_value: _ChainedClosure) -> 'ChainedClosure':
        return ChainedClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChainedClosure):
        """
        Dynamic initializer for ChainedClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChainedClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChainedClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getClosures(self) -> List['collections4.Closure']:
        """public org.apache.commons.collections4.Closure<? super E>[] org.apache.commons.collections4.functors.ChainedClosure.getClosures()"""
        return List['collections4.Closure']._wrap(super(ChainedClosure, self).getClosures())

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

    @staticmethod
    @overload
    def chainedClosure(arg0: 'Collection') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ChainedClosure.chainedClosure(java.util.Collection<? extends org.apache.commons.collections4.Closure<? super E>>)"""
        return collections4.Closure._wrap(_ChainedClosure.chainedClosure(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def chainedClosure(*arg0: 'collections4.Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ChainedClosure.chainedClosure(org.apache.commons.collections4.Closure<? super E>...)"""
        return collections4.Closure._wrap(_ChainedClosure.chainedClosure(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.ChainedClosure.execute(E)"""
        super(_ChainedClosure, self).execute(arg0)

    @overload
    def __init__(self, *arg0: 'collections4.Closure'):
        """public org.apache.commons.collections4.functors.ChainedClosure(org.apache.commons.collections4.Closure<? super E>...)"""
        val = _ChainedClosure(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.AbstractQuantifierPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as _AbstractQuantifierPredicate
_AbstractQuantifierPredicate = _AbstractQuantifierPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractQuantifierPredicate():
    """org.apache.commons.collections4.functors.AbstractQuantifierPredicate"""
 
    @staticmethod
    def _wrap(java_value: _AbstractQuantifierPredicate) -> 'AbstractQuantifierPredicate':
        return AbstractQuantifierPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractQuantifierPredicate):
        """
        Dynamic initializer for AbstractQuantifierPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractQuantifierPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractQuantifierPredicate__wrapper":
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
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(AbstractQuantifierPredicate, self).getPredicates())

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

    @abstractmethod
    def evaluate(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Predicate.evaluate(T)"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.AbstractQuantifierPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = _AbstractQuantifierPredicate(arg0)
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.collections4.functors.TransformerClosure
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.TransformerClosure as _TransformerClosure
_TransformerClosure = _TransformerClosure
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformerClosure():
    """org.apache.commons.collections4.functors.TransformerClosure"""
 
    @staticmethod
    def _wrap(java_value: _TransformerClosure) -> 'TransformerClosure':
        return TransformerClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformerClosure):
        """
        Dynamic initializer for TransformerClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformerClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformerClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.TransformerClosure.execute(E)"""
        super(_TransformerClosure, self).execute(arg0)

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
    def transformerClosure(arg0: 'Transformer') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.TransformerClosure.transformerClosure(org.apache.commons.collections4.Transformer<? super E, ?>)"""
        return collections4.Closure._wrap(_TransformerClosure.transformerClosure(arg0))

    @overload
    def getTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super E, ?> org.apache.commons.collections4.functors.TransformerClosure.getTransformer()"""
        return 'collections4.Transformer'._wrap(super(TransformerClosure, self).getTransformer())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.functors.TransformerClosure(org.apache.commons.collections4.Transformer<? super E, ?>)"""
        val = _TransformerClosure(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.NullIsFalsePredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.functors.NullIsFalsePredicate as _NullIsFalsePredicate
_NullIsFalsePredicate = _NullIsFalsePredicate
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullIsFalsePredicate():
    """org.apache.commons.collections4.functors.NullIsFalsePredicate"""
 
    @staticmethod
    def _wrap(java_value: _NullIsFalsePredicate) -> 'NullIsFalsePredicate':
        return NullIsFalsePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullIsFalsePredicate):
        """
        Dynamic initializer for NullIsFalsePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullIsFalsePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullIsFalsePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.NullIsFalsePredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(NullIsFalsePredicate, self).getPredicates())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullIsFalsePredicate.evaluate(T)"""
        return bool._wrap(super(_NullIsFalsePredicate, self).evaluate(arg0))

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

    @staticmethod
    @overload
    def nullIsFalsePredicate(arg0: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullIsFalsePredicate.nullIsFalsePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate._wrap(_NullIsFalsePredicate.nullIsFalsePredicate(arg0))

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.NullIsFalsePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        val = _NullIsFalsePredicate(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.InvokerTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.InvokerTransformer as _InvokerTransformer
_InvokerTransformer = _InvokerTransformer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvokerTransformer():
    """org.apache.commons.collections4.functors.InvokerTransformer"""
 
    @staticmethod
    def _wrap(java_value: _InvokerTransformer) -> 'InvokerTransformer':
        return InvokerTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvokerTransformer):
        """
        Dynamic initializer for InvokerTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvokerTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvokerTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def invokerTransformer(arg0: str, arg1: 'Class', arg2: 'Object') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.InvokerTransformer.invokerTransformer(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        return collections4.Transformer._wrap(_InvokerTransformer.invokerTransformer(arg0, arg1, arg2))

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

    @staticmethod
    @overload
    def invokerTransformer(arg0: str) -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.InvokerTransformer.invokerTransformer(java.lang.String)"""
        return collections4.Transformer._wrap(_InvokerTransformer.invokerTransformer(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Class', arg2: 'Object'):
        """public org.apache.commons.collections4.functors.InvokerTransformer(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        val = _InvokerTransformer(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.InvokerTransformer.transform(java.lang.Object)"""
        return object._wrap(super(_InvokerTransformer, self).transform(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.InstantiateTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.functors.InstantiateTransformer as _InstantiateTransformer
_InstantiateTransformer = _InstantiateTransformer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InstantiateTransformer():
    """org.apache.commons.collections4.functors.InstantiateTransformer"""
 
    @staticmethod
    def _wrap(java_value: _InstantiateTransformer) -> 'InstantiateTransformer':
        return InstantiateTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InstantiateTransformer):
        """
        Dynamic initializer for InstantiateTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InstantiateTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InstantiateTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def instantiateTransformer(arg0: 'Class', arg1: 'Object') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<java.lang.Class<? extends T>, T> org.apache.commons.collections4.functors.InstantiateTransformer.instantiateTransformer(java.lang.Class<?>[],java.lang.Object[])"""
        return collections4.Transformer._wrap(_InstantiateTransformer.instantiateTransformer(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def instantiateTransformer() -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<java.lang.Class<? extends T>, T> org.apache.commons.collections4.functors.InstantiateTransformer.instantiateTransformer()"""
        return collections4.Transformer._wrap(_InstantiateTransformer.instantiateTransformer())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def transform(self, arg0: 'Class') -> object:
        """public T org.apache.commons.collections4.functors.InstantiateTransformer.transform(java.lang.Class<? extends T>)"""
        return object._wrap(super(_InstantiateTransformer, self).transform(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Class', arg1: 'Object'):
        """public org.apache.commons.collections4.functors.InstantiateTransformer(java.lang.Class<?>[],java.lang.Object[])"""
        val = _InstantiateTransformer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.NOPTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.functors.NOPTransformer as _NOPTransformer
_NOPTransformer = _NOPTransformer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NOPTransformer():
    """org.apache.commons.collections4.functors.NOPTransformer"""
 
    @staticmethod
    def _wrap(java_value: _NOPTransformer) -> 'NOPTransformer':
        return NOPTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NOPTransformer):
        """
        Dynamic initializer for NOPTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NOPTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NOPTransformer__wrapper":
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def transform(self, arg0: object) -> object:
        """public T org.apache.commons.collections4.functors.NOPTransformer.transform(T)"""
        return object._wrap(super(_NOPTransformer, self).transform(arg0))

    @staticmethod
    @overload
    def nopTransformer() -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.NOPTransformer.nopTransformer()"""
        return collections4.Transformer._wrap(_NOPTransformer.nopTransformer())

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
 
 
# CLASS: org.apache.commons.collections4.functors.StringValueTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.functors.StringValueTransformer as _StringValueTransformer
_StringValueTransformer = _StringValueTransformer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringValueTransformer():
    """org.apache.commons.collections4.functors.StringValueTransformer"""
 
    @staticmethod
    def _wrap(java_value: _StringValueTransformer) -> 'StringValueTransformer':
        return StringValueTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringValueTransformer):
        """
        Dynamic initializer for StringValueTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringValueTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringValueTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def transform(self, arg0: object) -> str:
        """public java.lang.String org.apache.commons.collections4.functors.StringValueTransformer.transform(T)"""
        return str._wrap(super(_StringValueTransformer, self).transform(arg0))

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

    @staticmethod
    @overload
    def stringValueTransformer() -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, java.lang.String> org.apache.commons.collections4.functors.StringValueTransformer.stringValueTransformer()"""
        return collections4.Transformer._wrap(_StringValueTransformer.stringValueTransformer())

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
 
 
# CLASS: org.apache.commons.collections4.functors.NullIsTruePredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.functors.NullIsTruePredicate as _NullIsTruePredicate
_NullIsTruePredicate = _NullIsTruePredicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullIsTruePredicate():
    """org.apache.commons.collections4.functors.NullIsTruePredicate"""
 
    @staticmethod
    def _wrap(java_value: _NullIsTruePredicate) -> 'NullIsTruePredicate':
        return NullIsTruePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullIsTruePredicate):
        """
        Dynamic initializer for NullIsTruePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullIsTruePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullIsTruePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.NullIsTruePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        val = _NullIsTruePredicate(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullIsTruePredicate.evaluate(T)"""
        return bool._wrap(super(_NullIsTruePredicate, self).evaluate(arg0))

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

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.NullIsTruePredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(NullIsTruePredicate, self).getPredicates())

    @staticmethod
    @overload
    def nullIsTruePredicate(arg0: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullIsTruePredicate.nullIsTruePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate._wrap(_NullIsTruePredicate.nullIsTruePredicate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.OnePredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.OnePredicate as _OnePredicate
_OnePredicate = _OnePredicate
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as _AbstractQuantifierPredicate
_AbstractQuantifierPredicate = _AbstractQuantifierPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OnePredicate():
    """org.apache.commons.collections4.functors.OnePredicate"""
 
    @staticmethod
    def _wrap(java_value: _OnePredicate) -> 'OnePredicate':
        return OnePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OnePredicate):
        """
        Dynamic initializer for OnePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OnePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OnePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.OnePredicate.evaluate(T)"""
        return bool._wrap(super(_OnePredicate, self).evaluate(arg0))

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
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.OnePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = _OnePredicate(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def onePredicate(*arg0: 'collections4.Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.OnePredicate.onePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return collections4.Predicate._wrap(_OnePredicate.onePredicate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def onePredicate(arg0: 'Collection') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.OnePredicate.onePredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return collections4.Predicate._wrap(_OnePredicate.onePredicate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(AbstractQuantifierPredicate, self).getPredicates())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.TruePredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.TruePredicate as _TruePredicate
_TruePredicate = _TruePredicate
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TruePredicate():
    """org.apache.commons.collections4.functors.TruePredicate"""
 
    @staticmethod
    def _wrap(java_value: _TruePredicate) -> 'TruePredicate':
        return TruePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TruePredicate):
        """
        Dynamic initializer for TruePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TruePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TruePredicate__wrapper":
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
    def truePredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.TruePredicate.truePredicate()"""
        return collections4.Predicate._wrap(_TruePredicate.truePredicate())

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

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.TruePredicate.evaluate(T)"""
        return bool._wrap(super(_TruePredicate, self).evaluate(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.functors.NotPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.NotPredicate as _NotPredicate
_NotPredicate = _NotPredicate
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotPredicate():
    """org.apache.commons.collections4.functors.NotPredicate"""
 
    @staticmethod
    def _wrap(java_value: _NotPredicate) -> 'NotPredicate':
        return NotPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotPredicate):
        """
        Dynamic initializer for NotPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.NotPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(NotPredicate, self).getPredicates())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NotPredicate.evaluate(T)"""
        return bool._wrap(super(_NotPredicate, self).evaluate(arg0))

    @staticmethod
    @overload
    def notPredicate(arg0: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NotPredicate.notPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate._wrap(_NotPredicate.notPredicate(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.NotPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        val = _NotPredicate(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.FalsePredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.FalsePredicate as _FalsePredicate
_FalsePredicate = _FalsePredicate
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FalsePredicate():
    """org.apache.commons.collections4.functors.FalsePredicate"""
 
    @staticmethod
    def _wrap(java_value: _FalsePredicate) -> 'FalsePredicate':
        return FalsePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FalsePredicate):
        """
        Dynamic initializer for FalsePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FalsePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FalsePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.FalsePredicate.evaluate(T)"""
        return bool._wrap(super(_FalsePredicate, self).evaluate(arg0))

    @staticmethod
    @overload
    def falsePredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.FalsePredicate.falsePredicate()"""
        return collections4.Predicate._wrap(_FalsePredicate.falsePredicate())

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
 
 
# CLASS: org.apache.commons.collections4.functors.ComparatorPredicate$Criterion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import org.apache.commons.collections4.functors.ComparatorPredicate as _ComparatorPredicate_Criterion
_Criterion = _ComparatorPredicate_Criterion.Criterion
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Criterion():
    """org.apache.commons.collections4.functors.ComparatorPredicate.Criterion"""
 
    @staticmethod
    def _wrap(java_value: _Criterion) -> 'Criterion':
        return Criterion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Criterion):
        """
        Dynamic initializer for Criterion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Criterion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Criterion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Criterion':
        """public static org.apache.commons.collections4.functors.ComparatorPredicate$Criterion org.apache.commons.collections4.functors.ComparatorPredicate$Criterion.valueOf(java.lang.String)"""
        return Criterion._wrap(_Criterion.valueOf(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['Criterion']:
        """public static org.apache.commons.collections4.functors.ComparatorPredicate$Criterion[] org.apache.commons.collections4.functors.ComparatorPredicate$Criterion.values()"""
        return List[Criterion]._wrap(_Criterion.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.functors.SwitchClosure
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.commons.collections4.functors.SwitchClosure as _SwitchClosure
_SwitchClosure = _SwitchClosure
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SwitchClosure():
    """org.apache.commons.collections4.functors.SwitchClosure"""
 
    @staticmethod
    def _wrap(java_value: _SwitchClosure) -> 'SwitchClosure':
        return SwitchClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SwitchClosure):
        """
        Dynamic initializer for SwitchClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SwitchClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SwitchClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def switchClosure(arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.SwitchClosure.switchClosure(org.apache.commons.collections4.Predicate<? super E>[],org.apache.commons.collections4.Closure<? super E>[],org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure._wrap(_SwitchClosure.switchClosure(arg0, arg1, arg2))

    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super E>[] org.apache.commons.collections4.functors.SwitchClosure.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(SwitchClosure, self).getPredicates())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.SwitchClosure.execute(E)"""
        super(_SwitchClosure, self).execute(arg0)

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure'):
        """public org.apache.commons.collections4.functors.SwitchClosure(org.apache.commons.collections4.Predicate<? super E>[],org.apache.commons.collections4.Closure<? super E>[],org.apache.commons.collections4.Closure<? super E>)"""
        val = _SwitchClosure(arg0, arg1, arg2)
        self.__wrapper = val

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
    def switchClosure(arg0: 'Map') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.SwitchClosure.switchClosure(java.util.Map<org.apache.commons.collections4.Predicate<E>, org.apache.commons.collections4.Closure<E>>)"""
        return collections4.Closure._wrap(_SwitchClosure.switchClosure(arg0))

    @overload
    def getClosures(self) -> List['collections4.Closure']:
        """public org.apache.commons.collections4.Closure<? super E>[] org.apache.commons.collections4.functors.SwitchClosure.getClosures()"""
        return List['collections4.Closure']._wrap(super(SwitchClosure, self).getClosures())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getDefaultClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.SwitchClosure.getDefaultClosure()"""
        return 'collections4.Closure'._wrap(super(SwitchClosure, self).getDefaultClosure())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.TransformerPredicate
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.TransformerPredicate as _TransformerPredicate
_TransformerPredicate = _TransformerPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformerPredicate():
    """org.apache.commons.collections4.functors.TransformerPredicate"""
 
    @staticmethod
    def _wrap(java_value: _TransformerPredicate) -> 'TransformerPredicate':
        return TransformerPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformerPredicate):
        """
        Dynamic initializer for TransformerPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformerPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformerPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def transformerPredicate(arg0: 'Transformer') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.TransformerPredicate.transformerPredicate(org.apache.commons.collections4.Transformer<? super T, java.lang.Boolean>)"""
        return collections4.Predicate._wrap(_TransformerPredicate.transformerPredicate(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def getTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super T, java.lang.Boolean> org.apache.commons.collections4.functors.TransformerPredicate.getTransformer()"""
        return 'collections4.Transformer'._wrap(super(TransformerPredicate, self).getTransformer())

    @overload
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.functors.TransformerPredicate(org.apache.commons.collections4.Transformer<? super T, java.lang.Boolean>)"""
        val = _TransformerPredicate(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.TransformerPredicate.evaluate(T)"""
        return bool._wrap(super(_TransformerPredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.ChainedTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.ChainedTransformer as _ChainedTransformer
_ChainedTransformer = _ChainedTransformer
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChainedTransformer():
    """org.apache.commons.collections4.functors.ChainedTransformer"""
 
    @staticmethod
    def _wrap(java_value: _ChainedTransformer) -> 'ChainedTransformer':
        return ChainedTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChainedTransformer):
        """
        Dynamic initializer for ChainedTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChainedTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChainedTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTransformers(self) -> List['collections4.Transformer']:
        """public org.apache.commons.collections4.Transformer<? super T, ? extends T>[] org.apache.commons.collections4.functors.ChainedTransformer.getTransformers()"""
        return List['collections4.Transformer']._wrap(super(ChainedTransformer, self).getTransformers())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def chainedTransformer(arg0: 'Collection') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.ChainedTransformer.chainedTransformer(java.util.Collection<? extends org.apache.commons.collections4.Transformer<? super T, ? extends T>>)"""
        return collections4.Transformer._wrap(_ChainedTransformer.chainedTransformer(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def chainedTransformer(*arg0: 'collections4.Transformer') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.ChainedTransformer.chainedTransformer(org.apache.commons.collections4.Transformer<? super T, ? extends T>...)"""
        return collections4.Transformer._wrap(_ChainedTransformer.chainedTransformer(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def transform(self, arg0: object) -> object:
        """public T org.apache.commons.collections4.functors.ChainedTransformer.transform(T)"""
        return object._wrap(super(_ChainedTransformer, self).transform(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, *arg0: 'collections4.Transformer'):
        """public org.apache.commons.collections4.functors.ChainedTransformer(org.apache.commons.collections4.Transformer<? super T, ? extends T>...)"""
        val = _ChainedTransformer(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.CloneTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.functors.CloneTransformer as _CloneTransformer
_CloneTransformer = _CloneTransformer
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CloneTransformer():
    """org.apache.commons.collections4.functors.CloneTransformer"""
 
    @staticmethod
    def _wrap(java_value: _CloneTransformer) -> 'CloneTransformer':
        return CloneTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CloneTransformer):
        """
        Dynamic initializer for CloneTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CloneTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CloneTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def transform(self, arg0: object) -> object:
        """public T org.apache.commons.collections4.functors.CloneTransformer.transform(T)"""
        return object._wrap(super(_CloneTransformer, self).transform(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def cloneTransformer() -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.CloneTransformer.cloneTransformer()"""
        return collections4.Transformer._wrap(_CloneTransformer.cloneTransformer())

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
 
 
# CLASS: org.apache.commons.collections4.functors.OrPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.OrPredicate as _OrPredicate
_OrPredicate = _OrPredicate
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OrPredicate():
    """org.apache.commons.collections4.functors.OrPredicate"""
 
    @staticmethod
    def _wrap(java_value: _OrPredicate) -> 'OrPredicate':
        return OrPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrPredicate):
        """
        Dynamic initializer for OrPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.OrPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(OrPredicate, self).getPredicates())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def orPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.OrPredicate.orPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate._wrap(_OrPredicate.orPredicate(arg0, arg1))

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.OrPredicate.evaluate(T)"""
        return bool._wrap(super(_OrPredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Predicate'):
        """public org.apache.commons.collections4.functors.OrPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        val = _OrPredicate(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.ExceptionClosure
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.functors.ExceptionClosure as _ExceptionClosure
_ExceptionClosure = _ExceptionClosure
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExceptionClosure():
    """org.apache.commons.collections4.functors.ExceptionClosure"""
 
    @staticmethod
    def _wrap(java_value: _ExceptionClosure) -> 'ExceptionClosure':
        return ExceptionClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExceptionClosure):
        """
        Dynamic initializer for ExceptionClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExceptionClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExceptionClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.ExceptionClosure.execute(E)"""
        super(_ExceptionClosure, self).execute(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def exceptionClosure() -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ExceptionClosure.exceptionClosure()"""
        return collections4.Closure._wrap(_ExceptionClosure.exceptionClosure())

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
 
 
# CLASS: org.apache.commons.collections4.functors.ExceptionTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.ExceptionTransformer as _ExceptionTransformer
_ExceptionTransformer = _ExceptionTransformer
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExceptionTransformer():
    """org.apache.commons.collections4.functors.ExceptionTransformer"""
 
    @staticmethod
    def _wrap(java_value: _ExceptionTransformer) -> 'ExceptionTransformer':
        return ExceptionTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExceptionTransformer):
        """
        Dynamic initializer for ExceptionTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExceptionTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExceptionTransformer__wrapper":
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

    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.ExceptionTransformer.transform(I)"""
        return object._wrap(super(_ExceptionTransformer, self).transform(arg0))

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

    @staticmethod
    @overload
    def exceptionTransformer() -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.ExceptionTransformer.exceptionTransformer()"""
        return collections4.Transformer._wrap(_ExceptionTransformer.exceptionTransformer())

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
 
 
# CLASS: org.apache.commons.collections4.functors.IdentityPredicate
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
import org.apache.commons.collections4.functors.IdentityPredicate as _IdentityPredicate
_IdentityPredicate = _IdentityPredicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IdentityPredicate():
    """org.apache.commons.collections4.functors.IdentityPredicate"""
 
    @staticmethod
    def _wrap(java_value: _IdentityPredicate) -> 'IdentityPredicate':
        return IdentityPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IdentityPredicate):
        """
        Dynamic initializer for IdentityPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IdentityPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IdentityPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getValue(self) -> object:
        """public T org.apache.commons.collections4.functors.IdentityPredicate.getValue()"""
        return object._wrap(super(IdentityPredicate, self).getValue())

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.IdentityPredicate.evaluate(T)"""
        return bool._wrap(super(_IdentityPredicate, self).evaluate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.functors.IdentityPredicate(T)"""
        val = _IdentityPredicate(arg0)
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def identityPredicate(arg0: object) -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.IdentityPredicate.identityPredicate(T)"""
        return collections4.Predicate._wrap(_IdentityPredicate.identityPredicate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.MapTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.functors.MapTransformer as _MapTransformer
_MapTransformer = _MapTransformer
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapTransformer():
    """org.apache.commons.collections4.functors.MapTransformer"""
 
    @staticmethod
    def _wrap(java_value: _MapTransformer) -> 'MapTransformer':
        return MapTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapTransformer):
        """
        Dynamic initializer for MapTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getMap(self) -> 'Map':
        """public java.util.Map<? super I, ? extends O> org.apache.commons.collections4.functors.MapTransformer.getMap()"""
        return 'Map'._wrap(super(MapTransformer, self).getMap())

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

    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.MapTransformer.transform(I)"""
        return object._wrap(super(_MapTransformer, self).transform(arg0))

    @staticmethod
    @overload
    def mapTransformer(arg0: 'Map') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.MapTransformer.mapTransformer(java.util.Map<? super I, ? extends O>)"""
        return collections4.Transformer._wrap(_MapTransformer.mapTransformer(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.functors.ClosureTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.functors.ClosureTransformer as _ClosureTransformer
_ClosureTransformer = _ClosureTransformer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClosureTransformer():
    """org.apache.commons.collections4.functors.ClosureTransformer"""
 
    @staticmethod
    def _wrap(java_value: _ClosureTransformer) -> 'ClosureTransformer':
        return ClosureTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosureTransformer):
        """
        Dynamic initializer for ClosureTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosureTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosureTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, arg0: 'Closure'):
        """public org.apache.commons.collections4.functors.ClosureTransformer(org.apache.commons.collections4.Closure<? super T>)"""
        val = _ClosureTransformer(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def closureTransformer(arg0: 'Closure') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.ClosureTransformer.closureTransformer(org.apache.commons.collections4.Closure<? super T>)"""
        return collections4.Transformer._wrap(_ClosureTransformer.closureTransformer(arg0))

    @overload
    def transform(self, arg0: object) -> object:
        """public T org.apache.commons.collections4.functors.ClosureTransformer.transform(T)"""
        return object._wrap(super(_ClosureTransformer, self).transform(arg0))

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
    def getClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super T> org.apache.commons.collections4.functors.ClosureTransformer.getClosure()"""
        return 'collections4.Closure'._wrap(super(ClosureTransformer, self).getClosure())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.PredicateTransformer
from pyquantum_helper import import_once as _import_once
import java.lang.Boolean as Boolean
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import org.apache.commons.collections4.functors.PredicateTransformer as _PredicateTransformer
_PredicateTransformer = _PredicateTransformer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicateTransformer():
    """org.apache.commons.collections4.functors.PredicateTransformer"""
 
    @staticmethod
    def _wrap(java_value: _PredicateTransformer) -> 'PredicateTransformer':
        return PredicateTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicateTransformer):
        """
        Dynamic initializer for PredicateTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicateTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicateTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super T> org.apache.commons.collections4.functors.PredicateTransformer.getPredicate()"""
        return 'collections4.Predicate'._wrap(super(PredicateTransformer, self).getPredicate())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.PredicateTransformer(org.apache.commons.collections4.Predicate<? super T>)"""
        val = _PredicateTransformer(arg0)
        self.__wrapper = val

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
    def predicateTransformer(arg0: 'Predicate') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, java.lang.Boolean> org.apache.commons.collections4.functors.PredicateTransformer.predicateTransformer(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Transformer._wrap(_PredicateTransformer.predicateTransformer(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def transform(self, arg0: object) -> 'Boolean':
        """public java.lang.Boolean org.apache.commons.collections4.functors.PredicateTransformer.transform(T)"""
        return 'Boolean'._wrap(super(_PredicateTransformer, self).transform(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.AnyPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.AnyPredicate as _AnyPredicate
_AnyPredicate = _AnyPredicate
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as _AbstractQuantifierPredicate
_AbstractQuantifierPredicate = _AbstractQuantifierPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AnyPredicate():
    """org.apache.commons.collections4.functors.AnyPredicate"""
 
    @staticmethod
    def _wrap(java_value: _AnyPredicate) -> 'AnyPredicate':
        return AnyPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnyPredicate):
        """
        Dynamic initializer for AnyPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnyPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnyPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def anyPredicate(arg0: 'Collection') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AnyPredicate.anyPredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return collections4.Predicate._wrap(_AnyPredicate.anyPredicate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.AnyPredicate.evaluate(T)"""
        return bool._wrap(super(_AnyPredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def anyPredicate(*arg0: 'collections4.Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AnyPredicate.anyPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return collections4.Predicate._wrap(_AnyPredicate.anyPredicate(arg0))

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(AbstractQuantifierPredicate, self).getPredicates())

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
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.AnyPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = _AnyPredicate(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.AndPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.functors.AndPredicate as _AndPredicate
_AndPredicate = _AndPredicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AndPredicate():
    """org.apache.commons.collections4.functors.AndPredicate"""
 
    @staticmethod
    def _wrap(java_value: _AndPredicate) -> 'AndPredicate':
        return AndPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AndPredicate):
        """
        Dynamic initializer for AndPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AndPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AndPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AndPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(AndPredicate, self).getPredicates())

    @staticmethod
    @overload
    def andPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AndPredicate.andPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate._wrap(_AndPredicate.andPredicate(arg0, arg1))

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.AndPredicate.evaluate(T)"""
        return bool._wrap(super(_AndPredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Predicate'):
        """public org.apache.commons.collections4.functors.AndPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        val = _AndPredicate(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.IfTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.IfTransformer as _IfTransformer
_IfTransformer = _IfTransformer
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IfTransformer():
    """org.apache.commons.collections4.functors.IfTransformer"""
 
    @staticmethod
    def _wrap(java_value: _IfTransformer) -> 'IfTransformer':
        return IfTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IfTransformer):
        """
        Dynamic initializer for IfTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IfTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IfTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTrueTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O> org.apache.commons.collections4.functors.IfTransformer.getTrueTransformer()"""
        return 'collections4.Transformer'._wrap(super(IfTransformer, self).getTrueTransformer())

    @overload
    def getFalseTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O> org.apache.commons.collections4.functors.IfTransformer.getFalseTransformer()"""
        return 'collections4.Transformer'._wrap(super(IfTransformer, self).getFalseTransformer())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ifTransformer(arg0: 'Predicate', arg1: 'Transformer') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.IfTransformer.ifTransformer(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Transformer<? super T, ? extends T>)"""
        return collections4.Transformer._wrap(_IfTransformer.ifTransformer(arg0, arg1))

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

    @staticmethod
    @overload
    def ifTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.IfTransformer.ifTransformer(org.apache.commons.collections4.Predicate<? super I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return collections4.Transformer._wrap(_IfTransformer.ifTransformer(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super I> org.apache.commons.collections4.functors.IfTransformer.getPredicate()"""
        return 'collections4.Predicate'._wrap(super(IfTransformer, self).getPredicate())

    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.IfTransformer.transform(I)"""
        return object._wrap(super(_IfTransformer, self).transform(arg0))

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer'):
        """public org.apache.commons.collections4.functors.IfTransformer(org.apache.commons.collections4.Predicate<? super I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = _IfTransformer(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.ConstantTransformer
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.Transformer as _Transformer
_Transformer = _Transformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.functors.ConstantTransformer as _ConstantTransformer
_ConstantTransformer = _ConstantTransformer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstantTransformer():
    """org.apache.commons.collections4.functors.ConstantTransformer"""
 
    @staticmethod
    def _wrap(java_value: _ConstantTransformer) -> 'ConstantTransformer':
        return ConstantTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantTransformer):
        """
        Dynamic initializer for ConstantTransformer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantTransformer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantTransformer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getConstant(self) -> object:
        """public O org.apache.commons.collections4.functors.ConstantTransformer.getConstant()"""
        return object._wrap(super(ConstantTransformer, self).getConstant())

    @staticmethod
    @overload
    def constantTransformer(arg0: object) -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.ConstantTransformer.constantTransformer(O)"""
        return collections4.Transformer._wrap(_ConstantTransformer.constantTransformer(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nullTransformer() -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.ConstantTransformer.nullTransformer()"""
        return collections4.Transformer._wrap(_ConstantTransformer.nullTransformer())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.functors.ConstantTransformer(O)"""
        val = _ConstantTransformer(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.ConstantTransformer.equals(java.lang.Object)"""
        return bool._wrap(super(_ConstantTransformer, self).equals(arg0))

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
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.ConstantTransformer.transform(I)"""
        return object._wrap(super(_ConstantTransformer, self).transform(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.functors.ConstantTransformer.hashCode()"""
        return int._wrap(super(ConstantTransformer, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.EqualPredicate
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.functors.EqualPredicate as _EqualPredicate
_EqualPredicate = _EqualPredicate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EqualPredicate():
    """org.apache.commons.collections4.functors.EqualPredicate"""
 
    @staticmethod
    def _wrap(java_value: _EqualPredicate) -> 'EqualPredicate':
        return EqualPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EqualPredicate):
        """
        Dynamic initializer for EqualPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EqualPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EqualPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.functors.EqualPredicate(T)"""
        val = _EqualPredicate(arg0)
        self.__wrapper = val

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
    def getValue(self) -> object:
        """public java.lang.Object org.apache.commons.collections4.functors.EqualPredicate.getValue()"""
        return object._wrap(super(EqualPredicate, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def equalPredicate(arg0: object, arg1: 'Equator') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.EqualPredicate.equalPredicate(T,org.apache.commons.collections4.Equator<T>)"""
        return collections4.Predicate._wrap(_EqualPredicate.equalPredicate(arg0, arg1))

    @overload
    def __init__(self, arg0: object, arg1: 'Equator'):
        """public org.apache.commons.collections4.functors.EqualPredicate(T,org.apache.commons.collections4.Equator<T>)"""
        val = _EqualPredicate(arg0, arg1)
        self.__wrapper = val

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.EqualPredicate.evaluate(T)"""
        return bool._wrap(super(_EqualPredicate, self).evaluate(arg0))

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

    @staticmethod
    @overload
    def equalPredicate(arg0: object) -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.EqualPredicate.equalPredicate(T)"""
        return collections4.Predicate._wrap(_EqualPredicate.equalPredicate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.CatchAndRethrowClosure
import org.apache.commons.collections4.functors.CatchAndRethrowClosure as _CatchAndRethrowClosure
_CatchAndRethrowClosure = _CatchAndRethrowClosure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CatchAndRethrowClosure():
    """org.apache.commons.collections4.functors.CatchAndRethrowClosure"""
 
    @staticmethod
    def _wrap(java_value: _CatchAndRethrowClosure) -> 'CatchAndRethrowClosure':
        return CatchAndRethrowClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CatchAndRethrowClosure):
        """
        Dynamic initializer for CatchAndRethrowClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CatchAndRethrowClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CatchAndRethrowClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.functors.CatchAndRethrowClosure()"""
        val = _CatchAndRethrowClosure()
        self.__wrapper = val

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
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.CatchAndRethrowClosure.execute(E)"""
        super(_CatchAndRethrowClosure, self).execute(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.functors.CatchAndRethrowClosure()"""
        val = _CatchAndRethrowClosure()
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.collections4.functors.NonePredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import org.apache.commons.collections4.functors.NonePredicate as _NonePredicate
_NonePredicate = _NonePredicate
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as _AbstractQuantifierPredicate
_AbstractQuantifierPredicate = _AbstractQuantifierPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NonePredicate():
    """org.apache.commons.collections4.functors.NonePredicate"""
 
    @staticmethod
    def _wrap(java_value: _NonePredicate) -> 'NonePredicate':
        return NonePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NonePredicate):
        """
        Dynamic initializer for NonePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NonePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NonePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NonePredicate.evaluate(T)"""
        return bool._wrap(super(_NonePredicate, self).evaluate(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nonePredicate(arg0: 'Collection') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NonePredicate.nonePredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return collections4.Predicate._wrap(_NonePredicate.nonePredicate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate']._wrap(super(AbstractQuantifierPredicate, self).getPredicates())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.NonePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = _NonePredicate(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nonePredicate(*arg0: 'collections4.Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NonePredicate.nonePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return collections4.Predicate._wrap(_NonePredicate.nonePredicate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.NOPClosure
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import org.apache.commons.collections4.functors.NOPClosure as _NOPClosure
_NOPClosure = _NOPClosure
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NOPClosure():
    """org.apache.commons.collections4.functors.NOPClosure"""
 
    @staticmethod
    def _wrap(java_value: _NOPClosure) -> 'NOPClosure':
        return NOPClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NOPClosure):
        """
        Dynamic initializer for NOPClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NOPClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NOPClosure__wrapper":
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

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.NOPClosure.execute(E)"""
        super(_NOPClosure, self).execute(arg0)

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

    @staticmethod
    @overload
    def nopClosure() -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.NOPClosure.nopClosure()"""
        return collections4.Closure._wrap(_NOPClosure.nopClosure())

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
 
 
# CLASS: org.apache.commons.collections4.functors.NotNullPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.functors.NotNullPredicate as _NotNullPredicate
_NotNullPredicate = _NotNullPredicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotNullPredicate():
    """org.apache.commons.collections4.functors.NotNullPredicate"""
 
    @staticmethod
    def _wrap(java_value: _NotNullPredicate) -> 'NotNullPredicate':
        return NotNullPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotNullPredicate):
        """
        Dynamic initializer for NotNullPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotNullPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotNullPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NotNullPredicate.evaluate(T)"""
        return bool._wrap(super(_NotNullPredicate, self).evaluate(arg0))

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

    @staticmethod
    @overload
    def notNullPredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NotNullPredicate.notNullPredicate()"""
        return collections4.Predicate._wrap(_NotNullPredicate.notNullPredicate())

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
 
 
# CLASS: org.apache.commons.collections4.functors.ExceptionFactory
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
import org.apache.commons.collections4.functors.ExceptionFactory as _ExceptionFactory
_ExceptionFactory = _ExceptionFactory
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.Factory as _Factory
_Factory = _Factory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExceptionFactory():
    """org.apache.commons.collections4.functors.ExceptionFactory"""
 
    @staticmethod
    def _wrap(java_value: _ExceptionFactory) -> 'ExceptionFactory':
        return ExceptionFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExceptionFactory):
        """
        Dynamic initializer for ExceptionFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExceptionFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExceptionFactory__wrapper":
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def create(self) -> object:
        """public T org.apache.commons.collections4.functors.ExceptionFactory.create()"""
        return object._wrap(super(ExceptionFactory, self).create())

    @staticmethod
    @overload
    def exceptionFactory() -> 'collections4.Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.functors.ExceptionFactory.exceptionFactory()"""
        return collections4.Factory._wrap(_ExceptionFactory.exceptionFactory())

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
 
 
# CLASS: org.apache.commons.collections4.functors.DefaultEquator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import org.apache.commons.collections4.functors.DefaultEquator as _DefaultEquator
_DefaultEquator = _DefaultEquator
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultEquator():
    """org.apache.commons.collections4.functors.DefaultEquator"""
 
    @staticmethod
    def _wrap(java_value: _DefaultEquator) -> 'DefaultEquator':
        return DefaultEquator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultEquator):
        """
        Dynamic initializer for DefaultEquator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultEquator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultEquator__wrapper":
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

    @overload
    def equate(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.DefaultEquator.equate(T,T)"""
        return bool._wrap(super(_DefaultEquator, self).equate(arg0, arg1))

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

    @overload
    def hash(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.functors.DefaultEquator.hash(T)"""
        return int._wrap(super(_DefaultEquator, self).hash(arg0))

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

    @staticmethod
    @overload
    def defaultEquator() -> 'DefaultEquator':
        """public static <T> org.apache.commons.collections4.functors.DefaultEquator<T> org.apache.commons.collections4.functors.DefaultEquator.defaultEquator()"""
        return DefaultEquator._wrap(_DefaultEquator.defaultEquator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.WhileClosure
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.apache.commons.collections4.Closure as _Closure
_Closure = _Closure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.functors.WhileClosure as _WhileClosure
_WhileClosure = _WhileClosure
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import org.apache.commons.collections4.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WhileClosure():
    """org.apache.commons.collections4.functors.WhileClosure"""
 
    @staticmethod
    def _wrap(java_value: _WhileClosure) -> 'WhileClosure':
        return WhileClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WhileClosure):
        """
        Dynamic initializer for WhileClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WhileClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WhileClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isDoLoop(self) -> bool:
        """public boolean org.apache.commons.collections4.functors.WhileClosure.isDoLoop()"""
        return bool._wrap(super(WhileClosure, self).isDoLoop())

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.functors.WhileClosure.getPredicate()"""
        return 'collections4.Predicate'._wrap(super(WhileClosure, self).getPredicate())

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.WhileClosure.execute(E)"""
        super(_WhileClosure, self).execute(arg0)

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

    @staticmethod
    @overload
    def whileClosure(arg0: 'Predicate', arg1: 'Closure', arg2: bool) -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.WhileClosure.whileClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,boolean)"""
        return collections4.Closure._wrap(_WhileClosure.whileClosure(arg0, arg1, _boolean.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Closure', arg2: bool):
        """public org.apache.commons.collections4.functors.WhileClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,boolean)"""
        val = _WhileClosure(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.WhileClosure.getClosure()"""
        return 'collections4.Closure'._wrap(super(WhileClosure, self).getClosure())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.functors.ConstantFactory
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.collections4.functors.ConstantFactory as _ConstantFactory
_ConstantFactory = _ConstantFactory
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.lang.Integer as _int
import org.apache.commons.collections4.Factory as _Factory
_Factory = _Factory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstantFactory():
    """org.apache.commons.collections4.functors.ConstantFactory"""
 
    @staticmethod
    def _wrap(java_value: _ConstantFactory) -> 'ConstantFactory':
        return ConstantFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantFactory):
        """
        Dynamic initializer for ConstantFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.functors.ConstantFactory(T)"""
        val = _ConstantFactory(arg0)
        self.__wrapper = val

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
    def create(self) -> object:
        """public T org.apache.commons.collections4.functors.ConstantFactory.create()"""
        return object._wrap(super(ConstantFactory, self).create())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def constantFactory(arg0: object) -> 'collections4.Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.functors.ConstantFactory.constantFactory(T)"""
        return collections4.Factory._wrap(_ConstantFactory.constantFactory(arg0))

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
    def getConstant(self) -> object:
        """public T org.apache.commons.collections4.functors.ConstantFactory.getConstant()"""
        return object._wrap(super(ConstantFactory, self).getConstant())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())