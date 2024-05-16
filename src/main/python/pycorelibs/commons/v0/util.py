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
from typing import List
import java.lang.String as _string
import dev.ultreon.libs.commons.v0.util.ColorUtils as _ColorUtils
_ColorUtils = _ColorUtils
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import dev.ultreon.libs.commons.v0.Color as _Color
_Color = _Color
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ColorUtils():
    """dev.ultreon.libs.commons.v0.util.ColorUtils"""
 
    @staticmethod
    def _wrap(java_value: _ColorUtils) -> 'ColorUtils':
        return ColorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorUtils):
        """
        Dynamic initializer for ColorUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.ColorUtils()"""
        val = _ColorUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def parseHexList(arg0: str) -> List['v0.Color']:
        """public static dev.ultreon.libs.commons.v0.Color[] dev.ultreon.libs.commons.v0.util.ColorUtils.parseHexList(java.lang.String)"""
        return List[v0.Color]._wrap(_ColorUtils.parseHexList(arg0))

    @staticmethod
    @overload
    def extractMultiHex(*arg0: str) -> List['v0.Color']:
        """public static dev.ultreon.libs.commons.v0.Color[] dev.ultreon.libs.commons.v0.util.ColorUtils.extractMultiHex(java.lang.String...)"""
        return List[v0.Color]._wrap(_ColorUtils.extractMultiHex(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.ColorUtils()"""
        val = _ColorUtils()
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

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.ColorUtils
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import dev.ultreon.libs.commons.v0.util.ColorUtils as _ColorUtils
_ColorUtils = _ColorUtils
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import dev.ultreon.libs.commons.v0.Color as _Color
_Color = _Color
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ColorUtils():
    """dev.ultreon.libs.commons.v0.util.ColorUtils"""
 
    @staticmethod
    def _wrap(java_value: _ColorUtils) -> 'ColorUtils':
        return ColorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorUtils):
        """
        Dynamic initializer for ColorUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.ColorUtils()"""
        val = _ColorUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def parseHexList(arg0: str) -> List['v0.Color']:
        """public static dev.ultreon.libs.commons.v0.Color[] dev.ultreon.libs.commons.v0.util.ColorUtils.parseHexList(java.lang.String)"""
        return List[v0.Color]._wrap(_ColorUtils.parseHexList(arg0))

    @staticmethod
    @overload
    def extractMultiHex(*arg0: str) -> List['v0.Color']:
        """public static dev.ultreon.libs.commons.v0.Color[] dev.ultreon.libs.commons.v0.util.ColorUtils.extractMultiHex(java.lang.String...)"""
        return List[v0.Color]._wrap(_ColorUtils.extractMultiHex(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.ColorUtils()"""
        val = _ColorUtils()
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

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.ColorUtils 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.CollectionUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.Comparable as Comparable
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.util.CollectionUtils as _CollectionUtils
_CollectionUtils = _CollectionUtils
import java.lang.Comparable as _Comparable
_Comparable = _Comparable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CollectionUtils():
    """dev.ultreon.libs.commons.v0.util.CollectionUtils"""
 
    @staticmethod
    def _wrap(java_value: _CollectionUtils) -> 'CollectionUtils':
        return CollectionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollectionUtils):
        """
        Dynamic initializer for CollectionUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollectionUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollectionUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def max(arg0: 'Collection', arg1: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<T>> T dev.ultreon.libs.commons.v0.util.CollectionUtils.max(java.util.Collection<T>,T)"""
        return Comparable._wrap(_CollectionUtils.max(arg0, arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.CollectionUtils()"""
        val = _CollectionUtils()
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
        """public dev.ultreon.libs.commons.v0.util.CollectionUtils()"""
        val = _CollectionUtils()
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
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.EnumUtils
import dev.ultreon.libs.commons.v0.util.EnumUtils as _EnumUtils
_EnumUtils = _EnumUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EnumUtils():
    """dev.ultreon.libs.commons.v0.util.EnumUtils"""
 
    @staticmethod
    def _wrap(java_value: _EnumUtils) -> 'EnumUtils':
        return EnumUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EnumUtils):
        """
        Dynamic initializer for EnumUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EnumUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EnumUtils__wrapper":
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
    def byOrdinal(arg0: int, arg1: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E dev.ultreon.libs.commons.v0.util.EnumUtils.byOrdinal(int,E)"""
        return Enum._wrap(_EnumUtils.byOrdinal(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def byIndex(arg0: int, arg1: 'Enum', arg2: 'Function') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E dev.ultreon.libs.commons.v0.util.EnumUtils.byIndex(int,E,java.util.function.Function<E, java.lang.Integer>)"""
        return Enum._wrap(_EnumUtils.byIndex(_int.valueOf(arg0), arg1, arg2))

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
    def byName(arg0: str, arg1: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E dev.ultreon.libs.commons.v0.util.EnumUtils.byName(java.lang.String,E)"""
        return Enum._wrap(_EnumUtils.byName(arg0, arg1))

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
    def validate(arg0: object, arg1: 'Class') -> bool:
        """public static <E extends java.lang.Enum<E>> boolean dev.ultreon.libs.commons.v0.util.EnumUtils.validate(java.lang.Object,java.lang.Class<E>)"""
        return bool._wrap(_EnumUtils.validate(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.ExceptionUtils
import dev.ultreon.libs.commons.v0.util.ExceptionUtils as _ExceptionUtils
_ExceptionUtils = _ExceptionUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.RuntimeException as _RuntimeException
_RuntimeException = _RuntimeException
import java.lang.Integer as _int
import java.lang.RuntimeException as RuntimeException
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExceptionUtils():
    """dev.ultreon.libs.commons.v0.util.ExceptionUtils"""
 
    @staticmethod
    def _wrap(java_value: _ExceptionUtils) -> 'ExceptionUtils':
        return ExceptionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExceptionUtils):
        """
        Dynamic initializer for ExceptionUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExceptionUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExceptionUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.ExceptionUtils()"""
        val = _ExceptionUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getStackTrace(arg0: 'Throwable') -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.ExceptionUtils.getStackTrace(java.lang.Throwable)"""
        return str._wrap(_ExceptionUtils.getStackTrace(arg0))

    @staticmethod
    @overload
    def utilityClass() -> 'RuntimeException':
        """public static java.lang.RuntimeException dev.ultreon.libs.commons.v0.util.ExceptionUtils.utilityClass()"""
        return RuntimeException._wrap(_ExceptionUtils.utilityClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getStackTrace(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.ExceptionUtils.getStackTrace(java.lang.String)"""
        return str._wrap(_ExceptionUtils.getStackTrace(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.ExceptionUtils()"""
        val = _ExceptionUtils()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getStackTrace() -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.ExceptionUtils.getStackTrace()"""
        return str._wrap(_ExceptionUtils.getStackTrace())

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.StringUtils
from builtins import str
import java.lang.Character as _char
import java.text.AttributedString as _AttributedString
_AttributedString = _AttributedString
import dev.ultreon.libs.commons.v0.util.StringUtils as _StringUtils
_StringUtils = _StringUtils
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.awt.Font as Font
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.text.AttributedString as AttributedString
import java.lang.String as _string
import java.lang.Integer as _int
import java.awt.FontMetrics as FontMetrics
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringUtils():
    """dev.ultreon.libs.commons.v0.util.StringUtils"""
 
    @staticmethod
    def _wrap(java_value: _StringUtils) -> 'StringUtils':
        return StringUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringUtils):
        """
        Dynamic initializer for StringUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def count(arg0: str, arg1: str) -> int:
        """public static int dev.ultreon.libs.commons.v0.util.StringUtils.count(java.lang.String,char)"""
        return int._wrap(_StringUtils.count(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def createFallbackString(arg0: str, arg1: 'Font', arg2: 'Font') -> 'AttributedString':
        """public static java.text.AttributedString dev.ultreon.libs.commons.v0.util.StringUtils.createFallbackString(java.lang.String,java.awt.Font,java.awt.Font)"""
        return AttributedString._wrap(_StringUtils.createFallbackString(arg0, arg1, arg2))

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
    def splitIntoLines(arg0: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.libs.commons.v0.util.StringUtils.splitIntoLines(java.lang.String)"""
        return List._wrap(_StringUtils.splitIntoLines(arg0))

    @staticmethod
    @overload
    def join(arg0: 'List', arg1: str) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.StringUtils.join(java.util.List<java.lang.String>,java.lang.String)"""
        return str._wrap(_StringUtils.join(arg0, arg1))

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
    def findBreakAfter(arg0: str, arg1: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.util.StringUtils.findBreakAfter(java.lang.String,int)"""
        return int._wrap(_StringUtils.findBreakAfter(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def findBreakBefore(arg0: str, arg1: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.util.StringUtils.findBreakBefore(java.lang.String,int)"""
        return int._wrap(_StringUtils.findBreakBefore(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def wrapLineInto(arg0: str, arg1: 'List', arg2: 'FontMetrics', arg3: int):
        """public static void dev.ultreon.libs.commons.v0.util.StringUtils.wrapLineInto(java.lang.String,java.util.List<java.lang.String>,java.awt.FontMetrics,int)"""
        _StringUtils.wrapLineInto(arg0, arg1, arg2, _int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.StringUtils()"""
        val = _StringUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: 'FontMetrics', arg2: int) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.libs.commons.v0.util.StringUtils.wrap(java.lang.String,java.awt.FontMetrics,int)"""
        return List._wrap(_StringUtils.wrap(arg0, arg1, _int.valueOf(arg2)))

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
        """public dev.ultreon.libs.commons.v0.util.StringUtils()"""
        val = _StringUtils()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.IllegalCallerException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import dev.ultreon.libs.commons.v0.util.IllegalCallerException as _IllegalCallerException
_IllegalCallerException = _IllegalCallerException
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IllegalCallerException():
    """dev.ultreon.libs.commons.v0.util.IllegalCallerException"""
 
    @staticmethod
    def _wrap(java_value: _IllegalCallerException) -> 'IllegalCallerException':
        return IllegalCallerException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IllegalCallerException):
        """
        Dynamic initializer for IllegalCallerException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IllegalCallerException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IllegalCallerException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException()"""
        val = _IllegalCallerException()
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException(java.lang.Throwable)"""
        val = _IllegalCallerException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException(java.lang.String)"""
        val = _IllegalCallerException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException()"""
        val = _IllegalCallerException()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException(java.lang.String,java.lang.Throwable)"""
        val = _IllegalCallerException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.ClassUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
from builtins import type
import java.lang.Object as _object
import dev.ultreon.libs.commons.v0.util.ClassUtils as _ClassUtils
_ClassUtils = _ClassUtils
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ClassUtils():
    """dev.ultreon.libs.commons.v0.util.ClassUtils"""
 
    @staticmethod
    def _wrap(java_value: _ClassUtils) -> 'ClassUtils':
        return ClassUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClassUtils):
        """
        Dynamic initializer for ClassUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClassUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClassUtils__wrapper":
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
    def getCallerClass() -> 'type.Class':
        """public static java.lang.Class<?> dev.ultreon.libs.commons.v0.util.ClassUtils.getCallerClass()"""
        return type.Class._wrap(_ClassUtils.getCallerClass())

    @staticmethod
    @overload
    def checkCallerClassExtends(arg0: 'Class'):
        """public static void dev.ultreon.libs.commons.v0.util.ClassUtils.checkCallerClassExtends(java.lang.Class<?>)"""
        _ClassUtils.checkCallerClassExtends(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.ClassUtils()"""
        val = _ClassUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def checkCallerClassEquals(arg0: 'Class'):
        """public static void dev.ultreon.libs.commons.v0.util.ClassUtils.checkCallerClassEquals(java.lang.Class<?>)"""
        _ClassUtils.checkCallerClassEquals(arg0)

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
    def getCallerClassName() -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.ClassUtils.getCallerClassName()"""
        return str._wrap(_ClassUtils.getCallerClassName())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.ClassUtils()"""
        val = _ClassUtils()
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
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.TimeUtils
from builtins import str
import dev.ultreon.libs.commons.v0.util.TimeUtils as _TimeUtils
_TimeUtils = _TimeUtils
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TimeUtils():
    """dev.ultreon.libs.commons.v0.util.TimeUtils"""
 
    @staticmethod
    def _wrap(java_value: _TimeUtils) -> 'TimeUtils':
        return TimeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimeUtils):
        """
        Dynamic initializer for TimeUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimeUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimeUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.TimeUtils()"""
        val = _TimeUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def formatDuration(arg0: int) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.TimeUtils.formatDuration(long)"""
        return str._wrap(_TimeUtils.formatDuration(_long.valueOf(arg0)))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def formatDuration(arg0: int, arg1: int, arg2: float) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.TimeUtils.formatDuration(int,int,double)"""
        return str._wrap(_TimeUtils.formatDuration(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

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
        """public dev.ultreon.libs.commons.v0.util.TimeUtils()"""
        val = _TimeUtils()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.FileUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.io.PrintWriter as PrintWriter
import dev.ultreon.libs.commons.v0.util.FileUtils as _FileUtils
_FileUtils = _FileUtils
import java.io.PrintWriter as _PrintWriter
_PrintWriter = _PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileUtils():
    """dev.ultreon.libs.commons.v0.util.FileUtils"""
 
    @staticmethod
    def _wrap(java_value: _FileUtils) -> 'FileUtils':
        return FileUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileUtils):
        """
        Dynamic initializer for FileUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.FileUtils()"""
        val = _FileUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.FileUtils()"""
        val = _FileUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getExtension(arg0: 'File') -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.FileUtils.getExtension(java.io.File)"""
        return str._wrap(_FileUtils.getExtension(arg0))

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

    @staticmethod
    @overload
    def setCwd(arg0: 'File') -> bool:
        """public static boolean dev.ultreon.libs.commons.v0.util.FileUtils.setCwd(java.io.File)"""
        return bool._wrap(_FileUtils.setCwd(arg0))

    @staticmethod
    @overload
    def openOutputFile(arg0: str) -> 'PrintWriter':
        """public static java.io.PrintWriter dev.ultreon.libs.commons.v0.util.FileUtils.openOutputFile(java.lang.String)"""
        return PrintWriter._wrap(_FileUtils.openOutputFile(arg0))

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.IOUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.util.IOUtils as _IOUtils
_IOUtils = _IOUtils
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOUtils():
    """dev.ultreon.libs.commons.v0.util.IOUtils"""
 
    @staticmethod
    def _wrap(java_value: _IOUtils) -> 'IOUtils':
        return IOUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOUtils):
        """
        Dynamic initializer for IOUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def readAllBytes(arg0: 'InputStream') -> List[int]:
        """public static byte[] dev.ultreon.libs.commons.v0.util.IOUtils.readAllBytes(java.io.InputStream) throws java.io.IOException"""
        return List[int]._wrap(_IOUtils.readAllBytes(arg0))

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.IOUtils()"""
        val = _IOUtils()
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
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.IOUtils()"""
        val = _IOUtils()
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