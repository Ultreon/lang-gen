from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.text.ParsePosition as ParsePosition
import java.util.Date as Date
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.gson.internal.bind.util.ISO8601Utils as __ISO8601Utils
__ISO8601Utils = __ISO8601Utils
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.util.Date as __Date
__Date = __Date
import java.lang.Integer as __int
import java.util.TimeZone as TimeZone
from builtins import bool
from builtins import int
 
class ISO8601Utils():
    """com.google.gson.internal.bind.util.ISO8601Utils"""
 
    @staticmethod
    def __wrap(java_value: __ISO8601Utils) -> 'ISO8601Utils':
        return ISO8601Utils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ISO8601Utils):
        """
        Dynamic initializer for ISO8601Utils.
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
    def format(arg0: 'Date', arg1: bool) -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date,boolean)"""
        return str.__wrap(__ISO8601Utils.format(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def format(arg0: 'Date') -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date)"""
        return str.__wrap(__ISO8601Utils.format(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.util.ISO8601Utils()"""
        val = __ISO8601Utils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parse(arg0: str, arg1: 'ParsePosition') -> 'Date':
        """public static java.util.Date com.google.gson.internal.bind.util.ISO8601Utils.parse(java.lang.String,java.text.ParsePosition) throws java.text.ParseException"""
        return Date.__wrap(__ISO8601Utils.parse(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: bool, arg2: 'TimeZone') -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date,boolean,java.util.TimeZone)"""
        return str.__wrap(__ISO8601Utils.format(arg0, __boolean.valueOf(arg1), arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.util.ISO8601Utils()"""
        val = __ISO8601Utils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

 
 
 
# CLASS: com.google.gson.internal.bind.util.ISO8601Utils
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.text.ParsePosition as ParsePosition
import java.util.Date as Date
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.gson.internal.bind.util.ISO8601Utils as __ISO8601Utils
__ISO8601Utils = __ISO8601Utils
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.util.Date as __Date
__Date = __Date
import java.lang.Integer as __int
import java.util.TimeZone as TimeZone
from builtins import bool
from builtins import int
 
class ISO8601Utils():
    """com.google.gson.internal.bind.util.ISO8601Utils"""
 
    @staticmethod
    def __wrap(java_value: __ISO8601Utils) -> 'ISO8601Utils':
        return ISO8601Utils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ISO8601Utils):
        """
        Dynamic initializer for ISO8601Utils.
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
    def format(arg0: 'Date', arg1: bool) -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date,boolean)"""
        return str.__wrap(__ISO8601Utils.format(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def format(arg0: 'Date') -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date)"""
        return str.__wrap(__ISO8601Utils.format(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.google.gson.internal.bind.util.ISO8601Utils()"""
        val = __ISO8601Utils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parse(arg0: str, arg1: 'ParsePosition') -> 'Date':
        """public static java.util.Date com.google.gson.internal.bind.util.ISO8601Utils.parse(java.lang.String,java.text.ParsePosition) throws java.text.ParseException"""
        return Date.__wrap(__ISO8601Utils.parse(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: bool, arg2: 'TimeZone') -> str:
        """public static java.lang.String com.google.gson.internal.bind.util.ISO8601Utils.format(java.util.Date,boolean,java.util.TimeZone)"""
        return str.__wrap(__ISO8601Utils.format(arg0, __boolean.valueOf(arg1), arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.google.gson.internal.bind.util.ISO8601Utils()"""
        val = __ISO8601Utils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

 
 
 
# CLASS: com.google.gson.internal.bind.util.ISO8601Utils