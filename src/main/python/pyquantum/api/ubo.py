from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.ubo.UboFormatter as _UboFormatter
_UboFormatter = _UboFormatter
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UboFormatter():
    """dev.ultreon.quantum.api.ubo.UboFormatter"""
 
    @staticmethod
    def _wrap(java_value: _UboFormatter) -> 'UboFormatter':
        return UboFormatter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UboFormatter):
        """
        Dynamic initializer for UboFormatter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UboFormatter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UboFormatter__wrapper":
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
    def format(arg0: 'DataType') -> 'text.TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.ubo.UboFormatter.format(dev.ultreon.ubo.types.DataType<?>)"""
        return text.TextObject._wrap(_UboFormatter.format(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.ubo.UboFormatter()"""
        val = _UboFormatter()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def format(arg0: 'DataType', arg1: int) -> 'text.TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.ubo.UboFormatter.format(dev.ultreon.ubo.types.DataType<?>,int)"""
        return text.TextObject._wrap(_UboFormatter.format(arg0, _int.valueOf(arg1)))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.ubo.UboFormatter()"""
        val = _UboFormatter()
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.api.ubo.UboFormatter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.ubo.UboFormatter as _UboFormatter
_UboFormatter = _UboFormatter
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UboFormatter():
    """dev.ultreon.quantum.api.ubo.UboFormatter"""
 
    @staticmethod
    def _wrap(java_value: _UboFormatter) -> 'UboFormatter':
        return UboFormatter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UboFormatter):
        """
        Dynamic initializer for UboFormatter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UboFormatter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UboFormatter__wrapper":
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
    def format(arg0: 'DataType') -> 'text.TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.ubo.UboFormatter.format(dev.ultreon.ubo.types.DataType<?>)"""
        return text.TextObject._wrap(_UboFormatter.format(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.ubo.UboFormatter()"""
        val = _UboFormatter()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def format(arg0: 'DataType', arg1: int) -> 'text.TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.ubo.UboFormatter.format(dev.ultreon.ubo.types.DataType<?>,int)"""
        return text.TextObject._wrap(_UboFormatter.format(arg0, _int.valueOf(arg1)))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.ubo.UboFormatter()"""
        val = _UboFormatter()
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.api.ubo.UboFormatter