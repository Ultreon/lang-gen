from __future__ import annotations
from overload import overload


 
from builtins import str
import org.slf4j.helpers.Util as _Util
_Util = _Util
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Util():
    """org.slf4j.helpers.Util"""
 
    @staticmethod
    def _wrap(java_value: _Util) -> 'Util':
        return Util(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Util):
        """
        Dynamic initializer for Util.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Util__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Util__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def report(arg0: str):
        """public static final void org.slf4j.helpers.Util.report(java.lang.String)"""
        _Util.report(arg0)

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
    def report(arg0: str, arg1: 'Throwable'):
        """public static final void org.slf4j.helpers.Util.report(java.lang.String,java.lang.Throwable)"""
        _Util.report(arg0, arg1)

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

    @staticmethod
    @overload
    def getCallingClass() -> 'type.Class':
        """public static java.lang.Class<?> org.slf4j.helpers.Util.getCallingClass()"""
        return type.Class._wrap(_Util.getCallingClass())

    @staticmethod
    @overload
    def safeGetBooleanSystemProperty(arg0: str) -> bool:
        """public static boolean org.slf4j.helpers.Util.safeGetBooleanSystemProperty(java.lang.String)"""
        return bool._wrap(_Util.safeGetBooleanSystemProperty(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def safeGetSystemProperty(arg0: str) -> str:
        """public static java.lang.String org.slf4j.helpers.Util.safeGetSystemProperty(java.lang.String)"""
        return str._wrap(_Util.safeGetSystemProperty(arg0))

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

 
 
 
# CLASS: org.slf4j.helpers.Util
from builtins import str
import org.slf4j.helpers.Util as _Util
_Util = _Util
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Util():
    """org.slf4j.helpers.Util"""
 
    @staticmethod
    def _wrap(java_value: _Util) -> 'Util':
        return Util(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Util):
        """
        Dynamic initializer for Util.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Util__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Util__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def report(arg0: str):
        """public static final void org.slf4j.helpers.Util.report(java.lang.String)"""
        _Util.report(arg0)

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
    def report(arg0: str, arg1: 'Throwable'):
        """public static final void org.slf4j.helpers.Util.report(java.lang.String,java.lang.Throwable)"""
        _Util.report(arg0, arg1)

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

    @staticmethod
    @overload
    def getCallingClass() -> 'type.Class':
        """public static java.lang.Class<?> org.slf4j.helpers.Util.getCallingClass()"""
        return type.Class._wrap(_Util.getCallingClass())

    @staticmethod
    @overload
    def safeGetBooleanSystemProperty(arg0: str) -> bool:
        """public static boolean org.slf4j.helpers.Util.safeGetBooleanSystemProperty(java.lang.String)"""
        return bool._wrap(_Util.safeGetBooleanSystemProperty(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def safeGetSystemProperty(arg0: str) -> str:
        """public static java.lang.String org.slf4j.helpers.Util.safeGetSystemProperty(java.lang.String)"""
        return str._wrap(_Util.safeGetSystemProperty(arg0))

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

 
 
 
# CLASS: org.slf4j.helpers.Util 
 
 
# CLASS: org.slf4j.helpers.NOPLoggerFactory
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.slf4j.Logger as _Logger
_Logger = _Logger
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

import org.slf4j.helpers.NOPLoggerFactory as _NOPLoggerFactory
_NOPLoggerFactory = _NOPLoggerFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NOPLoggerFactory():
    """org.slf4j.helpers.NOPLoggerFactory"""
 
    @staticmethod
    def _wrap(java_value: _NOPLoggerFactory) -> 'NOPLoggerFactory':
        return NOPLoggerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NOPLoggerFactory):
        """
        Dynamic initializer for NOPLoggerFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NOPLoggerFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NOPLoggerFactory__wrapper":
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
    def getLogger(self, arg0: str) -> 'slf4py.Logger':
        """public org.slf4j.Logger org.slf4j.helpers.NOPLoggerFactory.getLogger(java.lang.String)"""
        return 'slf4py.Logger'._wrap(super(_NOPLoggerFactory, self).getLogger(arg0))

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
    def __init__(self):
        """public org.slf4j.helpers.NOPLoggerFactory()"""
        val = _NOPLoggerFactory()
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

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.NOPLoggerFactory()"""
        val = _NOPLoggerFactory()
        self.__wrapper = val 
 
 
# CLASS: org.slf4j.helpers.BasicMarker
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.String as _string
import org.slf4j.helpers.BasicMarker as _BasicMarker
_BasicMarker = _BasicMarker
import java.lang.Integer as _int
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BasicMarker():
    """org.slf4j.helpers.BasicMarker"""
 
    @staticmethod
    def _wrap(java_value: _BasicMarker) -> 'BasicMarker':
        return BasicMarker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BasicMarker):
        """
        Dynamic initializer for BasicMarker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BasicMarker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BasicMarker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hasReferences(self) -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.hasReferences()"""
        return bool._wrap(super(BasicMarker, self).hasReferences())

    @override
    @overload
    def hasChildren(self) -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.hasChildren()"""
        return bool._wrap(super(BasicMarker, self).hasChildren())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.BasicMarker.getName()"""
        return str._wrap(super(BasicMarker, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.contains(java.lang.String)"""
        return bool._wrap(super(_BasicMarker, self).contains(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.helpers.BasicMarker.toString()"""
        return str._wrap(super(BasicMarker, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.remove(org.slf4j.Marker)"""
        return bool._wrap(super(_BasicMarker, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.slf4j.helpers.BasicMarker.hashCode()"""
        return int._wrap(super(BasicMarker, self).hashCode())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.slf4j.Marker> org.slf4j.helpers.BasicMarker.iterator()"""
        return 'Iterator'._wrap(super(BasicMarker, self).iterator())

    @override
    @overload
    def add(self, arg0: 'Marker'):
        """public void org.slf4j.helpers.BasicMarker.add(org.slf4j.Marker)"""
        super(_BasicMarker, self).add(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.equals(java.lang.Object)"""
        return bool._wrap(super(_BasicMarker, self).equals(arg0))

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
    def contains(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.contains(org.slf4j.Marker)"""
        return bool._wrap(super(_BasicMarker, self).contains(arg0)) 
 
 
# CLASS: org.slf4j.helpers.BasicMarkerFactory
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.slf4j.Marker as _Marker
_Marker = _Marker
import java.lang.String as _string
import java.lang.Integer as _int
import org.slf4j.helpers.BasicMarkerFactory as _BasicMarkerFactory
_BasicMarkerFactory = _BasicMarkerFactory
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BasicMarkerFactory():
    """org.slf4j.helpers.BasicMarkerFactory"""
 
    @staticmethod
    def _wrap(java_value: _BasicMarkerFactory) -> 'BasicMarkerFactory':
        return BasicMarkerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BasicMarkerFactory):
        """
        Dynamic initializer for BasicMarkerFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BasicMarkerFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BasicMarkerFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.slf4j.helpers.BasicMarkerFactory()"""
        val = _BasicMarkerFactory()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.BasicMarkerFactory()"""
        val = _BasicMarkerFactory()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getMarker(self, arg0: str) -> 'slf4py.Marker':
        """public org.slf4j.Marker org.slf4j.helpers.BasicMarkerFactory.getMarker(java.lang.String)"""
        return 'slf4py.Marker'._wrap(super(_BasicMarkerFactory, self).getMarker(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDetachedMarker(self, arg0: str) -> 'slf4py.Marker':
        """public org.slf4j.Marker org.slf4j.helpers.BasicMarkerFactory.getDetachedMarker(java.lang.String)"""
        return 'slf4py.Marker'._wrap(super(_BasicMarkerFactory, self).getDetachedMarker(arg0))

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
    def exists(self, arg0: str) -> bool:
        """public boolean org.slf4j.helpers.BasicMarkerFactory.exists(java.lang.String)"""
        return bool._wrap(super(_BasicMarkerFactory, self).exists(arg0))

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
    def detachMarker(self, arg0: str) -> bool:
        """public boolean org.slf4j.helpers.BasicMarkerFactory.detachMarker(java.lang.String)"""
        return bool._wrap(super(_BasicMarkerFactory, self).detachMarker(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.helpers.NormalizedParameters
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
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from slf4py import event
except ImportError:
    event = _import_once("slf4py.event")

import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import org.slf4j.helpers.NormalizedParameters as _NormalizedParameters
_NormalizedParameters = _NormalizedParameters
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NormalizedParameters():
    """org.slf4j.helpers.NormalizedParameters"""
 
    @staticmethod
    def _wrap(java_value: _NormalizedParameters) -> 'NormalizedParameters':
        return NormalizedParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NormalizedParameters):
        """
        Dynamic initializer for NormalizedParameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NormalizedParameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NormalizedParameters__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getArguments(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.helpers.NormalizedParameters.getArguments()"""
        return List[object]._wrap(super(NormalizedParameters, self).getArguments())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def trimmedCopy(arg0: 'Object') -> List[object]:
        """public static java.lang.Object[] org.slf4j.helpers.NormalizedParameters.trimmedCopy(java.lang.Object[])"""
        return List[object]._wrap(_NormalizedParameters.trimmedCopy(arg0))

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
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.helpers.NormalizedParameters.getThrowable()"""
        return 'Throwable'._wrap(super(NormalizedParameters, self).getThrowable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Object'):
        """public org.slf4j.helpers.NormalizedParameters(java.lang.String,java.lang.Object[])"""
        val = _NormalizedParameters(arg0, arg1)
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

    @overload
    def __init__(self, arg0: str, arg1: 'Object', arg2: 'Throwable'):
        """public org.slf4j.helpers.NormalizedParameters(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = _NormalizedParameters(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getThrowableCandidate(arg0: 'Object') -> 'Throwable':
        """public static java.lang.Throwable org.slf4j.helpers.NormalizedParameters.getThrowableCandidate(java.lang.Object[])"""
        return Throwable._wrap(_NormalizedParameters.getThrowableCandidate(arg0))

    @staticmethod
    @overload
    def normalize(arg0: 'LoggingEvent') -> 'NormalizedParameters':
        """public static org.slf4j.helpers.NormalizedParameters org.slf4j.helpers.NormalizedParameters.normalize(org.slf4j.event.LoggingEvent)"""
        return NormalizedParameters._wrap(_NormalizedParameters.normalize(arg0))

    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.helpers.NormalizedParameters.getMessage()"""
        return str._wrap(super(NormalizedParameters, self).getMessage())

    @staticmethod
    @overload
    def normalize(arg0: str, arg1: 'Object', arg2: 'Throwable') -> 'NormalizedParameters':
        """public static org.slf4j.helpers.NormalizedParameters org.slf4j.helpers.NormalizedParameters.normalize(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        return NormalizedParameters._wrap(_NormalizedParameters.normalize(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.helpers.MarkerIgnoringBase
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.slf4j.helpers.MarkerIgnoringBase as _MarkerIgnoringBase
_MarkerIgnoringBase = _MarkerIgnoringBase
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import java.lang.String as _String
_String = _String
from builtins import object
import org.slf4j.Logger as _Logger
_Logger = _Logger
from abc import abstractmethod, ABC
import java.lang.String as _string
import org.slf4j.spi.LoggingEventBuilder as _LoggingEventBuilder
_LoggingEventBuilder = _LoggingEventBuilder
import java.lang.Integer as _int
try:
    from slf4py import event
except ImportError:
    event = _import_once("slf4py.event")

import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MarkerIgnoringBase():
    """org.slf4j.helpers.MarkerIgnoringBase"""
 
    @staticmethod
    def _wrap(java_value: _MarkerIgnoringBase) -> 'MarkerIgnoringBase':
        return MarkerIgnoringBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MarkerIgnoringBase):
        """
        Dynamic initializer for MarkerIgnoringBase.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MarkerIgnoringBase__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MarkerIgnoringBase__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def debug(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object...)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).info(arg0, arg1, arg2)

    @abstractmethod
    def trace(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object...)"""
        pass

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String)"""
        super(_MarkerIgnoringBase, self).warn(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isWarnEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_MarkerIgnoringBase, self).isWarnEnabled(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled()"""
        pass

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isTraceEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_MarkerIgnoringBase, self).isTraceEnabled(arg0))

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_MarkerIgnoringBase, self).trace(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_MarkerIgnoringBase, self).warn(arg0, arg1, arg2)

    @abstractmethod
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: str):
        """public abstract void org.slf4j.Logger.error(java.lang.String)"""
        pass

    @abstractmethod
    def trace(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object)"""
        pass

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atTrace())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atWarn())

    @abstractmethod
    def info(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled()"""
        pass

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).debug(arg0, arg1, arg2)

    @abstractmethod
    def info(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool._wrap(super(_slf4py.Logger, self).isEnabledForLevel(arg0))

    @abstractmethod
    def trace(self, arg0: str):
        """public abstract void org.slf4j.Logger.trace(java.lang.String)"""
        pass

    @overload
    def __init__(self):
        """public org.slf4j.helpers.MarkerIgnoringBase()"""
        val = _MarkerIgnoringBase()
        self.__wrapper = val

    @abstractmethod
    def info(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_MarkerIgnoringBase, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).info(arg0, arg1, arg2, arg3)

    @abstractmethod
    def info(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str):
        """public abstract void org.slf4j.Logger.info(java.lang.String)"""
        pass

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_MarkerIgnoringBase, self).error(arg0, arg1, arg2)

    @abstractmethod
    def warn(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object)"""
        pass

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).atLevel(arg0))

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled()"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_MarkerIgnoringBase, self).info(arg0, arg1, arg2)

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isDebugEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_MarkerIgnoringBase, self).isDebugEnabled(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String)"""
        super(_MarkerIgnoringBase, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String)"""
        super(_MarkerIgnoringBase, self).debug(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).debug(arg0, arg1, arg2, arg3)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_MarkerIgnoringBase, self).warn(arg0, arg1, arg2)

    @abstractmethod
    def error(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Throwable)"""
        pass

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isErrorEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_MarkerIgnoringBase, self).isErrorEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String)"""
        super(_MarkerIgnoringBase, self).info(arg0, arg1)

    @abstractmethod
    def debug(self, arg0: str):
        """public abstract void org.slf4j.Logger.debug(java.lang.String)"""
        pass

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.MarkerIgnoringBase()"""
        val = _MarkerIgnoringBase()
        self.__wrapper = val

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_MarkerIgnoringBase, self).trace(arg0, arg1, arg2)

    @abstractmethod
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_MarkerIgnoringBase, self).info(arg0, arg1, arg2)

    @abstractmethod
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Throwable)"""
        pass

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atInfo())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.helpers.MarkerIgnoringBase.toString()"""
        return str._wrap(super(MarkerIgnoringBase, self).toString())

    @abstractmethod
    def warn(self, arg0: str):
        """public abstract void org.slf4j.Logger.warn(java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Object...)"""
        pass

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_MarkerIgnoringBase, self).error(arg0, arg1, arg2)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_MarkerIgnoringBase, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isInfoEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_MarkerIgnoringBase, self).isInfoEnabled(arg0))

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_MarkerIgnoringBase, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String)"""
        super(_MarkerIgnoringBase, self).error(arg0, arg1) 
 
 
# CLASS: org.slf4j.helpers.NOPLogger
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import java.lang.String as _String
_String = _String
from builtins import object
import org.slf4j.Logger as _Logger
_Logger = _Logger
import java.lang.String as _string
import org.slf4j.spi.LoggingEventBuilder as _LoggingEventBuilder
_LoggingEventBuilder = _LoggingEventBuilder
import java.lang.Integer as _int
try:
    from slf4py import event
except ImportError:
    event = _import_once("slf4py.event")

import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

import org.slf4j.helpers.NOPLogger as _NOPLogger
_NOPLogger = _NOPLogger
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NOPLogger():
    """org.slf4j.helpers.NOPLogger"""
 
    @staticmethod
    def _wrap(java_value: _NOPLogger) -> 'NOPLogger':
        return NOPLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NOPLogger):
        """
        Dynamic initializer for NOPLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NOPLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NOPLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.NOPLogger.getName()"""
        return str._wrap(super(NOPLogger, self).getName())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(_NOPLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String)"""
        super(_NOPLogger, self).debug(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def trace(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String)"""
        super(_NOPLogger, self).trace(arg0)

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).trace(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).error(arg0, arg1)

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isDebugEnabled()"""
        return bool._wrap(super(NOPLogger, self).isDebugEnabled())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(_NOPLogger, self).debug(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def warn(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String)"""
        super(_NOPLogger, self).warn(arg0)

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).trace(arg0, arg1)

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isWarnEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_NOPLogger, self).isWarnEnabled(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).info(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isErrorEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_NOPLogger, self).isErrorEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isInfoEnabled()"""
        return bool._wrap(super(NOPLogger, self).isInfoEnabled())

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atTrace())

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.NOPLogger.isInfoEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_NOPLogger, self).isInfoEnabled(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atWarn())

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).debug(arg0, arg1)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isWarnEnabled()"""
        return bool._wrap(super(NOPLogger, self).isWarnEnabled())

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(_NOPLogger, self).error(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String)"""
        super(_NOPLogger, self).info(arg0)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).debug(arg0, arg1, arg2)

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isDebugEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_NOPLogger, self).isDebugEnabled(arg0))

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isTraceEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_NOPLogger, self).isTraceEnabled(arg0))

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool._wrap(super(_slf4py.Logger, self).isEnabledForLevel(arg0))

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isTraceEnabled()"""
        return bool._wrap(super(NOPLogger, self).isTraceEnabled())

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).atLevel(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).info(arg0, arg1)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(_NOPLogger, self).info(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(_NOPLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String)"""
        super(_NOPLogger, self).error(arg0)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).warn(arg0, arg1)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).trace(arg0, arg1, arg2)

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).error(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_NOPLogger, self).debug(arg0, arg1, arg2, arg3)

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).error(arg0, arg1)

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atInfo())

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String,java.lang.Object)"""
        super(_NOPLogger, self).debug(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_NOPLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).warn(arg0, arg1)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isErrorEnabled()"""
        return bool._wrap(super(NOPLogger, self).isErrorEnabled())

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_NOPLogger, self).trace(arg0, arg1) 
 
 
# CLASS: org.slf4j.helpers.NOPMDCAdapter
import org.slf4j.helpers.NOPMDCAdapter as _NOPMDCAdapter
_NOPMDCAdapter = _NOPMDCAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Deque as Deque
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Deque as _Deque
_Deque = _Deque
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NOPMDCAdapter():
    """org.slf4j.helpers.NOPMDCAdapter"""
 
    @staticmethod
    def _wrap(java_value: _NOPMDCAdapter) -> 'NOPMDCAdapter':
        return NOPMDCAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NOPMDCAdapter):
        """
        Dynamic initializer for NOPMDCAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NOPMDCAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NOPMDCAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getCopyOfContextMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.slf4j.helpers.NOPMDCAdapter.getCopyOfContextMap()"""
        return 'Map'._wrap(super(NOPMDCAdapter, self).getCopyOfContextMap())

    @override
    @overload
    def remove(self, arg0: str):
        """public void org.slf4j.helpers.NOPMDCAdapter.remove(java.lang.String)"""
        super(_NOPMDCAdapter, self).remove(arg0)

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
    def put(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.NOPMDCAdapter.put(java.lang.String,java.lang.String)"""
        super(_NOPMDCAdapter, self).put(arg0, arg1)

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
    def get(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.NOPMDCAdapter.get(java.lang.String)"""
        return str._wrap(super(_NOPMDCAdapter, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.NOPMDCAdapter()"""
        val = _NOPMDCAdapter()
        self.__wrapper = val

    @overload
    def popByKey(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.NOPMDCAdapter.popByKey(java.lang.String)"""
        return str._wrap(super(_NOPMDCAdapter, self).popByKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.slf4j.helpers.NOPMDCAdapter()"""
        val = _NOPMDCAdapter()
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.slf4j.helpers.NOPMDCAdapter.clear()"""
        super(NOPMDCAdapter, self).clear()

    @override
    @overload
    def clearDequeByKey(self, arg0: str):
        """public void org.slf4j.helpers.NOPMDCAdapter.clearDequeByKey(java.lang.String)"""
        super(_NOPMDCAdapter, self).clearDequeByKey(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def pushByKey(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.NOPMDCAdapter.pushByKey(java.lang.String,java.lang.String)"""
        super(_NOPMDCAdapter, self).pushByKey(arg0, arg1)

    @overload
    def getCopyOfDequeByKey(self, arg0: str) -> 'Deque':
        """public java.util.Deque<java.lang.String> org.slf4j.helpers.NOPMDCAdapter.getCopyOfDequeByKey(java.lang.String)"""
        return 'Deque'._wrap(super(_NOPMDCAdapter, self).getCopyOfDequeByKey(arg0))

    @override
    @overload
    def setContextMap(self, arg0: 'Map'):
        """public void org.slf4j.helpers.NOPMDCAdapter.setContextMap(java.util.Map<java.lang.String, java.lang.String>)"""
        super(_NOPMDCAdapter, self).setContextMap(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.helpers.ThreadLocalMapOfStacks
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.slf4j.helpers.ThreadLocalMapOfStacks as _ThreadLocalMapOfStacks
_ThreadLocalMapOfStacks = _ThreadLocalMapOfStacks
import java.util.Deque as Deque
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Deque as _Deque
_Deque = _Deque
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadLocalMapOfStacks():
    """org.slf4j.helpers.ThreadLocalMapOfStacks"""
 
    @staticmethod
    def _wrap(java_value: _ThreadLocalMapOfStacks) -> 'ThreadLocalMapOfStacks':
        return ThreadLocalMapOfStacks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadLocalMapOfStacks):
        """
        Dynamic initializer for ThreadLocalMapOfStacks.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadLocalMapOfStacks__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadLocalMapOfStacks__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def pushByKey(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.ThreadLocalMapOfStacks.pushByKey(java.lang.String,java.lang.String)"""
        super(_ThreadLocalMapOfStacks, self).pushByKey(arg0, arg1)

    @overload
    def popByKey(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.ThreadLocalMapOfStacks.popByKey(java.lang.String)"""
        return str._wrap(super(_ThreadLocalMapOfStacks, self).popByKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def clearDequeByKey(self, arg0: str):
        """public void org.slf4j.helpers.ThreadLocalMapOfStacks.clearDequeByKey(java.lang.String)"""
        super(_ThreadLocalMapOfStacks, self).clearDequeByKey(arg0)

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
    def __init__(self):
        """public org.slf4j.helpers.ThreadLocalMapOfStacks()"""
        val = _ThreadLocalMapOfStacks()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.ThreadLocalMapOfStacks()"""
        val = _ThreadLocalMapOfStacks()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getCopyOfDequeByKey(self, arg0: str) -> 'Deque':
        """public java.util.Deque<java.lang.String> org.slf4j.helpers.ThreadLocalMapOfStacks.getCopyOfDequeByKey(java.lang.String)"""
        return 'Deque'._wrap(super(_ThreadLocalMapOfStacks, self).getCopyOfDequeByKey(arg0))

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
 
 
# CLASS: org.slf4j.helpers.SubstituteLoggerFactory
from pyquantum_helper import import_once as _import_once
import java.util.concurrent.LinkedBlockingQueue as LinkedBlockingQueue
from builtins import str
from pyquantum_helper import override
import org.slf4j.helpers.SubstituteLoggerFactory as _SubstituteLoggerFactory
_SubstituteLoggerFactory = _SubstituteLoggerFactory
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.slf4j.Logger as _Logger
_Logger = _Logger
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.String as _string
import java.util.concurrent.LinkedBlockingQueue as _LinkedBlockingQueue
_LinkedBlockingQueue = _LinkedBlockingQueue
import java.lang.Integer as _int
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SubstituteLoggerFactory():
    """org.slf4j.helpers.SubstituteLoggerFactory"""
 
    @staticmethod
    def _wrap(java_value: _SubstituteLoggerFactory) -> 'SubstituteLoggerFactory':
        return SubstituteLoggerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SubstituteLoggerFactory):
        """
        Dynamic initializer for SubstituteLoggerFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SubstituteLoggerFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SubstituteLoggerFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.SubstituteLoggerFactory()"""
        val = _SubstituteLoggerFactory()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.slf4j.helpers.SubstituteLoggerFactory()"""
        val = _SubstituteLoggerFactory()
        self.__wrapper = val

    @overload
    def getLogger(self, arg0: str) -> 'slf4py.Logger':
        """public synchronized org.slf4j.Logger org.slf4j.helpers.SubstituteLoggerFactory.getLogger(java.lang.String)"""
        return 'slf4py.Logger'._wrap(super(_SubstituteLoggerFactory, self).getLogger(arg0))

    @overload
    def getEventQueue(self) -> 'LinkedBlockingQueue':
        """public java.util.concurrent.LinkedBlockingQueue<org.slf4j.event.SubstituteLoggingEvent> org.slf4j.helpers.SubstituteLoggerFactory.getEventQueue()"""
        return 'LinkedBlockingQueue'._wrap(super(SubstituteLoggerFactory, self).getEventQueue())

    @overload
    def postInitialization(self):
        """public void org.slf4j.helpers.SubstituteLoggerFactory.postInitialization()"""
        super(SubstituteLoggerFactory, self).postInitialization()

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
    def clear(self):
        """public void org.slf4j.helpers.SubstituteLoggerFactory.clear()"""
        super(SubstituteLoggerFactory, self).clear()

    @overload
    def getLoggerNames(self) -> 'List':
        """public java.util.List<java.lang.String> org.slf4j.helpers.SubstituteLoggerFactory.getLoggerNames()"""
        return 'List'._wrap(super(SubstituteLoggerFactory, self).getLoggerNames())

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
    def getLoggers(self) -> 'List':
        """public java.util.List<org.slf4j.helpers.SubstituteLogger> org.slf4j.helpers.SubstituteLoggerFactory.getLoggers()"""
        return 'List'._wrap(super(SubstituteLoggerFactory, self).getLoggers())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.helpers.SubstituteLogger
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import java.lang.String as _String
_String = _String
from builtins import object
import org.slf4j.Logger as _Logger
_Logger = _Logger
import java.util.Queue as Queue
import org.slf4j.helpers.SubstituteLogger as _SubstituteLogger
_SubstituteLogger = _SubstituteLogger
import java.lang.String as _string
import org.slf4j.spi.LoggingEventBuilder as _LoggingEventBuilder
_LoggingEventBuilder = _LoggingEventBuilder
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from slf4py import event
except ImportError:
    event = _import_once("slf4py.event")

import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SubstituteLogger():
    """org.slf4j.helpers.SubstituteLogger"""
 
    @staticmethod
    def _wrap(java_value: _SubstituteLogger) -> 'SubstituteLogger':
        return SubstituteLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SubstituteLogger):
        """
        Dynamic initializer for SubstituteLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SubstituteLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SubstituteLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).info(arg0, arg1, arg2)

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isErrorEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_SubstituteLogger, self).isErrorEnabled(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).warn(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atError()"""
        return 'spi.LoggingEventBuilder'._wrap(super(SubstituteLogger, self).atError())

    @overload
    def log(self, arg0: 'LoggingEvent'):
        """public void org.slf4j.helpers.SubstituteLogger.log(org.slf4j.event.LoggingEvent)"""
        super(_SubstituteLogger, self).log(arg0)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).debug(arg0, arg1, arg2)

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDebugEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_SubstituteLogger, self).isDebugEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isInfoEnabled()"""
        return bool._wrap(super(SubstituteLogger, self).isInfoEnabled())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.slf4j.helpers.SubstituteLogger.hashCode()"""
        return int._wrap(super(SubstituteLogger, self).hashCode())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).debug(arg0, arg1, arg2, arg3)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atDebug()"""
        return 'spi.LoggingEventBuilder'._wrap(super(SubstituteLogger, self).atDebug())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(_SubstituteLogger, self).trace(arg0, arg1)

    @overload
    def delegate(self) -> 'slf4py.Logger':
        """public org.slf4j.Logger org.slf4j.helpers.SubstituteLogger.delegate()"""
        return 'slf4py.Logger'._wrap(super(SubstituteLogger, self).delegate())

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_SubstituteLogger, self).atLevel(arg0))

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isTraceEnabled()"""
        return bool._wrap(super(SubstituteLogger, self).isTraceEnabled())

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).debug(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).warn(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).warn(arg0, arg1)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isErrorEnabled()"""
        return bool._wrap(super(SubstituteLogger, self).isErrorEnabled())

    @overload
    def isDelegateNOP(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDelegateNOP()"""
        return bool._wrap(super(SubstituteLogger, self).isDelegateNOP())

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_SubstituteLogger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(_SubstituteLogger, self).warn(arg0, arg1)

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atTrace()"""
        return 'spi.LoggingEventBuilder'._wrap(super(SubstituteLogger, self).atTrace())

    @override
    @overload
    def error(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String)"""
        super(_SubstituteLogger, self).error(arg0)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).info(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).trace(arg0, arg1)

    @overload
    def __init__(self, arg0: str, arg1: 'Queue', arg2: bool):
        """public org.slf4j.helpers.SubstituteLogger(java.lang.String,java.util.Queue<org.slf4j.event.SubstituteLoggingEvent>,boolean)"""
        val = _SubstituteLogger(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def debug(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String)"""
        super(_SubstituteLogger, self).debug(arg0)

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atInfo()"""
        return 'spi.LoggingEventBuilder'._wrap(super(SubstituteLogger, self).atInfo())

    @overload
    def isDelegateNull(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDelegateNull()"""
        return bool._wrap(super(SubstituteLogger, self).isDelegateNull())

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).trace(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).info(arg0, arg1)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(_SubstituteLogger, self).info(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).warn(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.equals(java.lang.Object)"""
        return bool._wrap(super(_SubstituteLogger, self).equals(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isWarnEnabled()"""
        return bool._wrap(super(SubstituteLogger, self).isWarnEnabled())

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).error(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.SubstituteLogger.getName()"""
        return str._wrap(super(SubstituteLogger, self).getName())

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).debug(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).debug(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String)"""
        super(_SubstituteLogger, self).trace(arg0)

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String)"""
        super(_SubstituteLogger, self).warn(arg0)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).info(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_SubstituteLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_SubstituteLogger, self).error(arg0, arg1)

    @overload
    def isDelegateEventAware(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDelegateEventAware()"""
        return bool._wrap(super(SubstituteLogger, self).isDelegateEventAware())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def info(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String)"""
        super(_SubstituteLogger, self).info(arg0)

    @overload
    def setDelegate(self, arg0: 'Logger'):
        """public void org.slf4j.helpers.SubstituteLogger.setDelegate(org.slf4j.Logger)"""
        super(_SubstituteLogger, self).setDelegate(arg0)

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isWarnEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_SubstituteLogger, self).isWarnEnabled(arg0))

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isTraceEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_SubstituteLogger, self).isTraceEnabled(arg0))

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isInfoEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_SubstituteLogger, self).isInfoEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_SubstituteLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atWarn()"""
        return 'spi.LoggingEventBuilder'._wrap(super(SubstituteLogger, self).atWarn())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_SubstituteLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(_SubstituteLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(_SubstituteLogger, self).error(arg0, arg1)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool._wrap(super(_SubstituteLogger, self).isEnabledForLevel(arg0))

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDebugEnabled()"""
        return bool._wrap(super(SubstituteLogger, self).isDebugEnabled()) 
 
 
# CLASS: org.slf4j.helpers.SubstituteServiceProvider
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.slf4j.helpers.SubstituteServiceProvider as _SubstituteServiceProvider
_SubstituteServiceProvider = _SubstituteServiceProvider
from pyquantum_helper import override
import org.slf4j.helpers.SubstituteLoggerFactory as _SubstituteLoggerFactory
_SubstituteLoggerFactory = _SubstituteLoggerFactory
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.slf4j.ILoggerFactory as _ILoggerFactory
_ILoggerFactory = _ILoggerFactory
import org.slf4j.spi.MDCAdapter as _MDCAdapter
_MDCAdapter = _MDCAdapter
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import org.slf4j.IMarkerFactory as _IMarkerFactory
_IMarkerFactory = _IMarkerFactory
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SubstituteServiceProvider():
    """org.slf4j.helpers.SubstituteServiceProvider"""
 
    @staticmethod
    def _wrap(java_value: _SubstituteServiceProvider) -> 'SubstituteServiceProvider':
        return SubstituteServiceProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SubstituteServiceProvider):
        """
        Dynamic initializer for SubstituteServiceProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SubstituteServiceProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SubstituteServiceProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLoggerFactory(self) -> 'slf4py.ILoggerFactory':
        """public org.slf4j.ILoggerFactory org.slf4j.helpers.SubstituteServiceProvider.getLoggerFactory()"""
        return 'slf4py.ILoggerFactory'._wrap(super(SubstituteServiceProvider, self).getLoggerFactory())

    @override
    @overload
    def getMDCAdapter(self) -> 'spi.MDCAdapter':
        """public org.slf4j.spi.MDCAdapter org.slf4j.helpers.SubstituteServiceProvider.getMDCAdapter()"""
        return 'spi.MDCAdapter'._wrap(super(SubstituteServiceProvider, self).getMDCAdapter())

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
    def getMarkerFactory(self) -> 'slf4py.IMarkerFactory':
        """public org.slf4j.IMarkerFactory org.slf4j.helpers.SubstituteServiceProvider.getMarkerFactory()"""
        return 'slf4py.IMarkerFactory'._wrap(super(SubstituteServiceProvider, self).getMarkerFactory())

    @overload
    def getSubstituteLoggerFactory(self) -> 'SubstituteLoggerFactory':
        """public org.slf4j.helpers.SubstituteLoggerFactory org.slf4j.helpers.SubstituteServiceProvider.getSubstituteLoggerFactory()"""
        return 'SubstituteLoggerFactory'._wrap(super(SubstituteServiceProvider, self).getSubstituteLoggerFactory())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def initialize(self):
        """public void org.slf4j.helpers.SubstituteServiceProvider.initialize()"""
        super(SubstituteServiceProvider, self).initialize()

    @overload
    def __init__(self):
        """public org.slf4j.helpers.SubstituteServiceProvider()"""
        val = _SubstituteServiceProvider()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getRequestedApiVersion(self) -> str:
        """public java.lang.String org.slf4j.helpers.SubstituteServiceProvider.getRequestedApiVersion()"""
        return str._wrap(super(SubstituteServiceProvider, self).getRequestedApiVersion())

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
    def __init__(self, ):
        """public org.slf4j.helpers.SubstituteServiceProvider()"""
        val = _SubstituteServiceProvider()
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
 
 
# CLASS: org.slf4j.helpers.MessageFormatter
import org.slf4j.helpers.FormattingTuple as _FormattingTuple
_FormattingTuple = _FormattingTuple
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
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import org.slf4j.helpers.MessageFormatter as _MessageFormatter
_MessageFormatter = _MessageFormatter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessageFormatter():
    """org.slf4j.helpers.MessageFormatter"""
 
    @staticmethod
    def _wrap(java_value: _MessageFormatter) -> 'MessageFormatter':
        return MessageFormatter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageFormatter):
        """
        Dynamic initializer for MessageFormatter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageFormatter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageFormatter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def arrayFormat(arg0: str, arg1: 'Object') -> 'FormattingTuple':
        """public static final org.slf4j.helpers.FormattingTuple org.slf4j.helpers.MessageFormatter.arrayFormat(java.lang.String,java.lang.Object[])"""
        return FormattingTuple._wrap(_MessageFormatter.arrayFormat(arg0, arg1))

    @staticmethod
    @overload
    def format(arg0: str, arg1: object) -> 'FormattingTuple':
        """public static final org.slf4j.helpers.FormattingTuple org.slf4j.helpers.MessageFormatter.format(java.lang.String,java.lang.Object)"""
        return FormattingTuple._wrap(_MessageFormatter.format(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.slf4j.helpers.MessageFormatter()"""
        val = _MessageFormatter()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def basicArrayFormat(arg0: 'NormalizedParameters') -> str:
        """public static java.lang.String org.slf4j.helpers.MessageFormatter.basicArrayFormat(org.slf4j.helpers.NormalizedParameters)"""
        return str._wrap(_MessageFormatter.basicArrayFormat(arg0))

    @staticmethod
    @overload
    def basicArrayFormat(arg0: str, arg1: 'Object') -> str:
        """public static final java.lang.String org.slf4j.helpers.MessageFormatter.basicArrayFormat(java.lang.String,java.lang.Object[])"""
        return str._wrap(_MessageFormatter.basicArrayFormat(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def arrayFormat(arg0: str, arg1: 'Object', arg2: 'Throwable') -> 'FormattingTuple':
        """public static final org.slf4j.helpers.FormattingTuple org.slf4j.helpers.MessageFormatter.arrayFormat(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        return FormattingTuple._wrap(_MessageFormatter.arrayFormat(arg0, arg1, arg2))

    @staticmethod
    @overload
    def format(arg0: str, arg1: object, arg2: object) -> 'FormattingTuple':
        """public static final org.slf4j.helpers.FormattingTuple org.slf4j.helpers.MessageFormatter.format(java.lang.String,java.lang.Object,java.lang.Object)"""
        return FormattingTuple._wrap(_MessageFormatter.format(arg0, arg1, arg2))

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
    def getThrowableCandidate(arg0: 'Object') -> 'Throwable':
        """public static java.lang.Throwable org.slf4j.helpers.MessageFormatter.getThrowableCandidate(java.lang.Object[])"""
        return Throwable._wrap(_MessageFormatter.getThrowableCandidate(arg0))

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
    def __init__(self, ):
        """public org.slf4j.helpers.MessageFormatter()"""
        val = _MessageFormatter()
        self.__wrapper = val

    @staticmethod
    @overload
    def trimmedCopy(arg0: 'Object') -> List[object]:
        """public static java.lang.Object[] org.slf4j.helpers.MessageFormatter.trimmedCopy(java.lang.Object[])"""
        return List[object]._wrap(_MessageFormatter.trimmedCopy(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.helpers.AbstractLogger
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.slf4j.helpers.AbstractLogger as _AbstractLogger
_AbstractLogger = _AbstractLogger
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import java.lang.String as _String
_String = _String
from builtins import object
import org.slf4j.Logger as _Logger
_Logger = _Logger
from abc import abstractmethod, ABC
import java.lang.String as _string
import org.slf4j.spi.LoggingEventBuilder as _LoggingEventBuilder
_LoggingEventBuilder = _LoggingEventBuilder
import java.lang.Integer as _int
try:
    from slf4py import event
except ImportError:
    event = _import_once("slf4py.event")

import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractLogger():
    """org.slf4j.helpers.AbstractLogger"""
 
    @staticmethod
    def _wrap(java_value: _AbstractLogger) -> 'AbstractLogger':
        return AbstractLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractLogger):
        """
        Dynamic initializer for AbstractLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2)

    @abstractmethod
    def isTraceEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String)"""
        super(_AbstractLogger, self).info(arg0)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2)

    @abstractmethod
    def isInfoEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.slf4j.helpers.AbstractLogger()"""
        val = _AbstractLogger()
        self.__wrapper = val

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(arg0, arg1)

    @abstractmethod
    def isDebugEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2, arg3)

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
    def warn(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String)"""
        super(_AbstractLogger, self).warn(arg0)

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.AbstractLogger.getName()"""
        return str._wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atTrace())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atWarn())

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2)

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled()"""
        pass

    @abstractmethod
    def isWarnEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def error(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String)"""
        super(_AbstractLogger, self).error(arg0)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool._wrap(super(_slf4py.Logger, self).isEnabledForLevel(arg0))

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String)"""
        super(_AbstractLogger, self).debug(arg0)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2, arg3)

    @abstractmethod
    def isErrorEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String)"""
        super(_AbstractLogger, self).trace(arg0)

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).atLevel(arg0))

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(arg0, arg1)

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atInfo())

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.AbstractLogger()"""
        val = _AbstractLogger()
        self.__wrapper = val

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(arg0, arg1)

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2) 
 
 
# CLASS: org.slf4j.helpers.CheckReturnValue
import org.slf4j.helpers.CheckReturnValue as _CheckReturnValue
_CheckReturnValue = _CheckReturnValue
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class CheckReturnValue():
    """org.slf4j.helpers.CheckReturnValue"""
 
    @staticmethod
    def _wrap(java_value: _CheckReturnValue) -> 'CheckReturnValue':
        return CheckReturnValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CheckReturnValue):
        """
        Dynamic initializer for CheckReturnValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CheckReturnValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CheckReturnValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: org.slf4j.helpers.NOP_FallbackServiceProvider
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.slf4j.helpers.NOP_FallbackServiceProvider as _NOP_FallbackServiceProvider
_NOP_FallbackServiceProvider = _NOP_FallbackServiceProvider
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.slf4j.ILoggerFactory as _ILoggerFactory
_ILoggerFactory = _ILoggerFactory
import org.slf4j.spi.MDCAdapter as _MDCAdapter
_MDCAdapter = _MDCAdapter
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import org.slf4j.IMarkerFactory as _IMarkerFactory
_IMarkerFactory = _IMarkerFactory
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NOP_FallbackServiceProvider():
    """org.slf4j.helpers.NOP_FallbackServiceProvider"""
 
    @staticmethod
    def _wrap(java_value: _NOP_FallbackServiceProvider) -> 'NOP_FallbackServiceProvider':
        return NOP_FallbackServiceProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NOP_FallbackServiceProvider):
        """
        Dynamic initializer for NOP_FallbackServiceProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NOP_FallbackServiceProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NOP_FallbackServiceProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getMDCAdapter(self) -> 'spi.MDCAdapter':
        """public org.slf4j.spi.MDCAdapter org.slf4j.helpers.NOP_FallbackServiceProvider.getMDCAdapter()"""
        return 'spi.MDCAdapter'._wrap(super(NOP_FallbackServiceProvider, self).getMDCAdapter())

    @override
    @overload
    def getLoggerFactory(self) -> 'slf4py.ILoggerFactory':
        """public org.slf4j.ILoggerFactory org.slf4j.helpers.NOP_FallbackServiceProvider.getLoggerFactory()"""
        return 'slf4py.ILoggerFactory'._wrap(super(NOP_FallbackServiceProvider, self).getLoggerFactory())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.NOP_FallbackServiceProvider()"""
        val = _NOP_FallbackServiceProvider()
        self.__wrapper = val

    @override
    @overload
    def getMarkerFactory(self) -> 'slf4py.IMarkerFactory':
        """public org.slf4j.IMarkerFactory org.slf4j.helpers.NOP_FallbackServiceProvider.getMarkerFactory()"""
        return 'slf4py.IMarkerFactory'._wrap(super(NOP_FallbackServiceProvider, self).getMarkerFactory())

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
    def getRequestedApiVersion(self) -> str:
        """public java.lang.String org.slf4j.helpers.NOP_FallbackServiceProvider.getRequestedApiVersion()"""
        return str._wrap(super(NOP_FallbackServiceProvider, self).getRequestedApiVersion())

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
    def initialize(self):
        """public void org.slf4j.helpers.NOP_FallbackServiceProvider.initialize()"""
        super(NOP_FallbackServiceProvider, self).initialize()

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

    @overload
    def __init__(self):
        """public org.slf4j.helpers.NOP_FallbackServiceProvider()"""
        val = _NOP_FallbackServiceProvider()
        self.__wrapper = val 
 
 
# CLASS: org.slf4j.helpers.BasicMDCAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Deque as Deque
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.util.Deque as _Deque
_Deque = _Deque
import java.lang.Integer as _int
import org.slf4j.helpers.BasicMDCAdapter as _BasicMDCAdapter
_BasicMDCAdapter = _BasicMDCAdapter
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BasicMDCAdapter():
    """org.slf4j.helpers.BasicMDCAdapter"""
 
    @staticmethod
    def _wrap(java_value: _BasicMDCAdapter) -> 'BasicMDCAdapter':
        return BasicMDCAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BasicMDCAdapter):
        """
        Dynamic initializer for BasicMDCAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BasicMDCAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BasicMDCAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clearDequeByKey(self, arg0: str):
        """public void org.slf4j.helpers.BasicMDCAdapter.clearDequeByKey(java.lang.String)"""
        super(_BasicMDCAdapter, self).clearDequeByKey(arg0)

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
    def popByKey(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.BasicMDCAdapter.popByKey(java.lang.String)"""
        return str._wrap(super(_BasicMDCAdapter, self).popByKey(arg0))

    @overload
    def getKeys(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.slf4j.helpers.BasicMDCAdapter.getKeys()"""
        return 'Set'._wrap(super(BasicMDCAdapter, self).getKeys())

    @overload
    def getCopyOfDequeByKey(self, arg0: str) -> 'Deque':
        """public java.util.Deque<java.lang.String> org.slf4j.helpers.BasicMDCAdapter.getCopyOfDequeByKey(java.lang.String)"""
        return 'Deque'._wrap(super(_BasicMDCAdapter, self).getCopyOfDequeByKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.slf4j.helpers.BasicMDCAdapter()"""
        val = _BasicMDCAdapter()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.BasicMDCAdapter()"""
        val = _BasicMDCAdapter()
        self.__wrapper = val

    @override
    @overload
    def pushByKey(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.BasicMDCAdapter.pushByKey(java.lang.String,java.lang.String)"""
        super(_BasicMDCAdapter, self).pushByKey(arg0, arg1)

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
    def put(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.BasicMDCAdapter.put(java.lang.String,java.lang.String)"""
        super(_BasicMDCAdapter, self).put(arg0, arg1)

    @overload
    def get(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.BasicMDCAdapter.get(java.lang.String)"""
        return str._wrap(super(_BasicMDCAdapter, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clear(self):
        """public void org.slf4j.helpers.BasicMDCAdapter.clear()"""
        super(BasicMDCAdapter, self).clear()

    @override
    @overload
    def getCopyOfContextMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.slf4j.helpers.BasicMDCAdapter.getCopyOfContextMap()"""
        return 'Map'._wrap(super(BasicMDCAdapter, self).getCopyOfContextMap())

    @override
    @overload
    def setContextMap(self, arg0: 'Map'):
        """public void org.slf4j.helpers.BasicMDCAdapter.setContextMap(java.util.Map<java.lang.String, java.lang.String>)"""
        super(_BasicMDCAdapter, self).setContextMap(arg0)

    @override
    @overload
    def remove(self, arg0: str):
        """public void org.slf4j.helpers.BasicMDCAdapter.remove(java.lang.String)"""
        super(_BasicMDCAdapter, self).remove(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.helpers.LegacyAbstractLogger
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.slf4j.helpers.AbstractLogger as _AbstractLogger
_AbstractLogger = _AbstractLogger
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import org.slf4j.helpers.LegacyAbstractLogger as _LegacyAbstractLogger
_LegacyAbstractLogger = _LegacyAbstractLogger
import java.lang.String as _String
_String = _String
from builtins import object
import org.slf4j.Logger as _Logger
_Logger = _Logger
from abc import abstractmethod, ABC
import java.lang.String as _string
import org.slf4j.spi.LoggingEventBuilder as _LoggingEventBuilder
_LoggingEventBuilder = _LoggingEventBuilder
import java.lang.Integer as _int
try:
    from slf4py import event
except ImportError:
    event = _import_once("slf4py.event")

import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LegacyAbstractLogger():
    """org.slf4j.helpers.LegacyAbstractLogger"""
 
    @staticmethod
    def _wrap(java_value: _LegacyAbstractLogger) -> 'LegacyAbstractLogger':
        return LegacyAbstractLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LegacyAbstractLogger):
        """
        Dynamic initializer for LegacyAbstractLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LegacyAbstractLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LegacyAbstractLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isTraceEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_LegacyAbstractLogger, self).isTraceEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String)"""
        super(_AbstractLogger, self).info(arg0)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2, arg3)

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
    def warn(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String)"""
        super(_AbstractLogger, self).warn(arg0)

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.AbstractLogger.getName()"""
        return str._wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).warn(arg0, arg1)

    @overload
    def __init__(self):
        """public org.slf4j.helpers.LegacyAbstractLogger()"""
        val = _LegacyAbstractLogger()
        self.__wrapper = val

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atTrace())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atWarn())

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isErrorEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_LegacyAbstractLogger, self).isErrorEnabled(arg0))

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2)

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled()"""
        pass

    @override
    @overload
    def error(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String)"""
        super(_AbstractLogger, self).error(arg0)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool._wrap(super(_slf4py.Logger, self).isEnabledForLevel(arg0))

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isDebugEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_LegacyAbstractLogger, self).isDebugEnabled(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String)"""
        super(_AbstractLogger, self).debug(arg0)

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.LegacyAbstractLogger()"""
        val = _LegacyAbstractLogger()
        self.__wrapper = val

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String)"""
        super(_AbstractLogger, self).trace(arg0)

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).atLevel(arg0))

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).debug(arg0, arg1)

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isInfoEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_LegacyAbstractLogger, self).isInfoEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(arg0, arg1)

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atInfo())

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(arg0, arg1)

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(arg0, arg1, arg2)

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isWarnEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_LegacyAbstractLogger, self).isWarnEnabled(arg0)) 
 
 
# CLASS: org.slf4j.helpers.FormattingTuple
import org.slf4j.helpers.FormattingTuple as _FormattingTuple
_FormattingTuple = _FormattingTuple
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FormattingTuple():
    """org.slf4j.helpers.FormattingTuple"""
 
    @staticmethod
    def _wrap(java_value: _FormattingTuple) -> 'FormattingTuple':
        return FormattingTuple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormattingTuple):
        """
        Dynamic initializer for FormattingTuple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormattingTuple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormattingTuple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.helpers.FormattingTuple.getMessage()"""
        return str._wrap(super(FormattingTuple, self).getMessage())

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.helpers.FormattingTuple.getThrowable()"""
        return 'Throwable'._wrap(super(FormattingTuple, self).getThrowable())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str):
        """public org.slf4j.helpers.FormattingTuple(java.lang.String)"""
        val = _FormattingTuple(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getArgArray(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.helpers.FormattingTuple.getArgArray()"""
        return List[object]._wrap(super(FormattingTuple, self).getArgArray())

    @overload
    def __init__(self, arg0: str, arg1: 'Object', arg2: 'Throwable'):
        """public org.slf4j.helpers.FormattingTuple(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = _FormattingTuple(arg0, arg1, arg2)
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