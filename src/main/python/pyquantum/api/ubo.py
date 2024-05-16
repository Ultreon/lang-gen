from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.api.ubo.UboFormatter as __UboFormatter
__UboFormatter = __UboFormatter
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class UboFormatter():
    """dev.ultreon.quantum.api.ubo.UboFormatter"""
 
    @staticmethod
    def __wrap(java_value: __UboFormatter) -> 'UboFormatter':
        return UboFormatter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UboFormatter):
        """
        Dynamic initializer for UboFormatter.
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
    def __init__(self):
        """public dev.ultreon.quantum.api.ubo.UboFormatter()"""
        val = __UboFormatter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def format(arg0: 'DataType') -> 'text.TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.ubo.UboFormatter.format(dev.ultreon.ubo.types.DataType<?>)"""
        return text.TextObject.__wrap(__UboFormatter.format(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def format(arg0: 'DataType', arg1: int) -> 'text.TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.ubo.UboFormatter.format(dev.ultreon.ubo.types.DataType<?>,int)"""
        return text.TextObject.__wrap(__UboFormatter.format(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.ubo.UboFormatter()"""
        val = __UboFormatter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.api.ubo.UboFormatter
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.api.ubo.UboFormatter as __UboFormatter
__UboFormatter = __UboFormatter
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
 
class UboFormatter():
    """dev.ultreon.quantum.api.ubo.UboFormatter"""
 
    @staticmethod
    def __wrap(java_value: __UboFormatter) -> 'UboFormatter':
        return UboFormatter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UboFormatter):
        """
        Dynamic initializer for UboFormatter.
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
    def __init__(self):
        """public dev.ultreon.quantum.api.ubo.UboFormatter()"""
        val = __UboFormatter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def format(arg0: 'DataType') -> 'text.TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.ubo.UboFormatter.format(dev.ultreon.ubo.types.DataType<?>)"""
        return text.TextObject.__wrap(__UboFormatter.format(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def format(arg0: 'DataType', arg1: int) -> 'text.TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.ubo.UboFormatter.format(dev.ultreon.ubo.types.DataType<?>,int)"""
        return text.TextObject.__wrap(__UboFormatter.format(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.ubo.UboFormatter()"""
        val = __UboFormatter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.api.ubo.UboFormatter