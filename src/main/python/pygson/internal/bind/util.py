from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.internal.bind.util.ISO8601Utils as _ISO8601Utils
_ISO8601Utils = _ISO8601Utils
import java.lang.Object as _object
from builtins import type
import java.text.ParsePosition as ParsePosition
import java.lang.String as _String
_String = _String
import java.util.Date as Date
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.TimeZone as TimeZone
from builtins import bool
import java.util.Date as _Date
_Date = _Date
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ISO8601Utils():
    """com.google.gson.internal.bind.util.ISO8601Utils"""
 
    @staticmethod
    def _wrap(java_value: _ISO8601Utils) -> 'ISO8601Utils':
        return ISO8601Utils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ISO8601Utils):
        """
        Dynamic initializer for ISO8601Utils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ISO8601Utils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ISO8601Utils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def format(arg0: 'Date') -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date)"""
        return str._wrap(_ISO8601Utils.format(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: bool, arg2: 'TimeZone') -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date,boolean,java.util.TimeZone)"""
        return str._wrap(_ISO8601Utils.format(arg0, _boolean.valueOf(arg1), arg2))

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
    def __init__(self, ):
        """public com.google.gson.internal.bind.util.ISO8601Utils()"""
        val = _ISO8601Utils()
        self.__wrapper = val

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: bool) -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date,boolean)"""
        return str._wrap(_ISO8601Utils.format(arg0, _boolean.valueOf(arg1)))

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
    def __init__(self):
        """public com.google.gson.internal.bind.util.ISO8601Utils()"""
        val = _ISO8601Utils()
        self.__wrapper = val

    @staticmethod
    @overload
    def parse(arg0: str, arg1: 'ParsePosition') -> 'Date':
        """public static java.util.Date com.google.gson.internal.bind.util.ISO8601Utils.parse(java.lang.String,java.text.ParsePosition) throws java.text.ParseException"""
        return Date._wrap(_ISO8601Utils.parse(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.gson.internal.bind.util.ISO8601Utils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.gson.internal.bind.util.ISO8601Utils as _ISO8601Utils
_ISO8601Utils = _ISO8601Utils
import java.lang.Object as _object
from builtins import type
import java.text.ParsePosition as ParsePosition
import java.lang.String as _String
_String = _String
import java.util.Date as Date
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.TimeZone as TimeZone
from builtins import bool
import java.util.Date as _Date
_Date = _Date
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ISO8601Utils():
    """com.google.gson.internal.bind.util.ISO8601Utils"""
 
    @staticmethod
    def _wrap(java_value: _ISO8601Utils) -> 'ISO8601Utils':
        return ISO8601Utils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ISO8601Utils):
        """
        Dynamic initializer for ISO8601Utils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ISO8601Utils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ISO8601Utils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def format(arg0: 'Date') -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date)"""
        return str._wrap(_ISO8601Utils.format(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: bool, arg2: 'TimeZone') -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date,boolean,java.util.TimeZone)"""
        return str._wrap(_ISO8601Utils.format(arg0, _boolean.valueOf(arg1), arg2))

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
    def __init__(self, ):
        """public com.google.gson.internal.bind.util.ISO8601Utils()"""
        val = _ISO8601Utils()
        self.__wrapper = val

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: bool) -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date,boolean)"""
        return str._wrap(_ISO8601Utils.format(arg0, _boolean.valueOf(arg1)))

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
    def __init__(self):
        """public com.google.gson.internal.bind.util.ISO8601Utils()"""
        val = _ISO8601Utils()
        self.__wrapper = val

    @staticmethod
    @overload
    def parse(arg0: str, arg1: 'ParsePosition') -> 'Date':
        """public static java.util.Date com.google.gson.internal.bind.util.ISO8601Utils.parse(java.lang.String,java.text.ParsePosition) throws java.text.ParseException"""
        return Date._wrap(_ISO8601Utils.parse(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.gson.internal.bind.util.ISO8601Utils