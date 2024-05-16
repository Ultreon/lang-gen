from __future__ import annotations
from overload import overload


 
import java.text.FieldPosition as FieldPosition
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Appendable as __Appendable
__Appendable = __Appendable
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Calendar as Calendar
import org.apache.commons.lang3.time.FastDatePrinter as __FastDatePrinter
__FastDatePrinter = __FastDatePrinter
import java.util.Date as Date
import java.lang.Appendable as Appendable
import java.util.TimeZone as __TimeZone
__TimeZone = __TimeZone
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
import java.lang.Integer as __int
from builtins import bool
import java.util.TimeZone as TimeZone
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import int
 
class FastDatePrinter(__DatePrinter, DatePrinter, __Serializable, Serializable):
    """org.apache.commons.lang3.time.FastDatePrinter"""
 
    @staticmethod
    def __wrap(java_value: __FastDatePrinter) -> 'FastDatePrinter':
        return FastDatePrinter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FastDatePrinter):
        """
        Dynamic initializer for FastDatePrinter.
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
    def format(self, arg0: 'Date', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: 'Date') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date)"""
        return str.__wrap(super(__FastDatePrinter, self).format(arg0))

    @override
    @overload
    def getTimeZone(self) -> 'TimeZone':
        """public java.util.TimeZone org.apache.commons.lang3.time.FastDatePrinter.getTimeZone()"""
        return 'TimeZone'.__wrap(super(FastDatePrinter, self).getTimeZone())

    @overload
    def getMaxLengthEstimate(self) -> int:
        """public int org.apache.commons.lang3.time.FastDatePrinter.getMaxLengthEstimate()"""
        return int.__wrap(super(FastDatePrinter, self).getMaxLengthEstimate())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale org.apache.commons.lang3.time.FastDatePrinter.getLocale()"""
        return 'Locale'.__wrap(super(FastDatePrinter, self).getLocale())

    @overload
    def format(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(long)"""
        return str.__wrap(super(__FastDatePrinter, self).format(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.toString()"""
        return str.__wrap(super(FastDatePrinter, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.time.FastDatePrinter.equals(java.lang.Object)"""
        return bool.__wrap(super(__FastDatePrinter, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.getPattern()"""
        return str.__wrap(super(FastDatePrinter, self).getPattern())

    @overload
    def format(self, arg0: 'Date', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date,B)"""
        return 'Appendable'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: 'Calendar') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar)"""
        return str.__wrap(super(__FastDatePrinter, self).format(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.time.FastDatePrinter.hashCode()"""
        return int.__wrap(super(FastDatePrinter, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def format(self, arg0: int, arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(long,B)"""
        return 'Appendable'.__wrap(super(__FastDatePrinter, self).format(__long.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: 'Calendar', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar,B)"""
        return 'Appendable'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: int, arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(long,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDatePrinter, self).format(__long.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: 'Calendar', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1, arg2))

 
 
 
# CLASS: org.apache.commons.lang3.time.FastDatePrinter
import java.text.FieldPosition as FieldPosition
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Appendable as __Appendable
__Appendable = __Appendable
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Calendar as Calendar
import org.apache.commons.lang3.time.FastDatePrinter as __FastDatePrinter
__FastDatePrinter = __FastDatePrinter
import java.util.Date as Date
import java.lang.Appendable as Appendable
import java.util.TimeZone as __TimeZone
__TimeZone = __TimeZone
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
import java.lang.Integer as __int
from builtins import bool
import java.util.TimeZone as TimeZone
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import int
 
class FastDatePrinter(__DatePrinter, DatePrinter, __Serializable, Serializable):
    """org.apache.commons.lang3.time.FastDatePrinter"""
 
    @staticmethod
    def __wrap(java_value: __FastDatePrinter) -> 'FastDatePrinter':
        return FastDatePrinter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FastDatePrinter):
        """
        Dynamic initializer for FastDatePrinter.
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
    def format(self, arg0: 'Date', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: 'Date') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date)"""
        return str.__wrap(super(__FastDatePrinter, self).format(arg0))

    @override
    @overload
    def getTimeZone(self) -> 'TimeZone':
        """public java.util.TimeZone org.apache.commons.lang3.time.FastDatePrinter.getTimeZone()"""
        return 'TimeZone'.__wrap(super(FastDatePrinter, self).getTimeZone())

    @overload
    def getMaxLengthEstimate(self) -> int:
        """public int org.apache.commons.lang3.time.FastDatePrinter.getMaxLengthEstimate()"""
        return int.__wrap(super(FastDatePrinter, self).getMaxLengthEstimate())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale org.apache.commons.lang3.time.FastDatePrinter.getLocale()"""
        return 'Locale'.__wrap(super(FastDatePrinter, self).getLocale())

    @overload
    def format(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(long)"""
        return str.__wrap(super(__FastDatePrinter, self).format(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.toString()"""
        return str.__wrap(super(FastDatePrinter, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.time.FastDatePrinter.equals(java.lang.Object)"""
        return bool.__wrap(super(__FastDatePrinter, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.getPattern()"""
        return str.__wrap(super(FastDatePrinter, self).getPattern())

    @overload
    def format(self, arg0: 'Date', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date,B)"""
        return 'Appendable'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: 'Calendar') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar)"""
        return str.__wrap(super(__FastDatePrinter, self).format(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.time.FastDatePrinter.hashCode()"""
        return int.__wrap(super(FastDatePrinter, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def format(self, arg0: int, arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(long,B)"""
        return 'Appendable'.__wrap(super(__FastDatePrinter, self).format(__long.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: 'Calendar', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar,B)"""
        return 'Appendable'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: int, arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(long,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDatePrinter, self).format(__long.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: 'Calendar', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'.__wrap(super(__FastDatePrinter, self).format(arg0, arg1, arg2))

 
 
 
# CLASS: org.apache.commons.lang3.time.FastDatePrinter 
 
 
# CLASS: org.apache.commons.lang3.time.TimeZones
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.time.TimeZones as __TimeZones
__TimeZones = __TimeZones
import java.lang.Object as __object
from builtins import type
import java.util.TimeZone as __TimeZone
__TimeZone = __TimeZone
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.TimeZone as TimeZone
from builtins import bool
from builtins import int
 
class TimeZones():
    """org.apache.commons.lang3.time.TimeZones"""
 
    @staticmethod
    def __wrap(java_value: __TimeZones) -> 'TimeZones':
        return TimeZones(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimeZones):
        """
        Dynamic initializer for TimeZones.
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

    @staticmethod
    @overload
    def toTimeZone(arg0: 'TimeZone') -> 'TimeZone':
        """public static java.util.TimeZone org.apache.commons.lang3.time.TimeZones.toTimeZone(java.util.TimeZone)"""
        return TimeZone.__wrap(__TimeZones.toTimeZone(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
 
 
# CLASS: org.apache.commons.lang3.time.DurationFormatUtils
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.time.DurationFormatUtils as __DurationFormatUtils
__DurationFormatUtils = __DurationFormatUtils
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.TimeZone as TimeZone
from builtins import bool
from builtins import int
 
class DurationFormatUtils():
    """org.apache.commons.lang3.time.DurationFormatUtils"""
 
    @staticmethod
    def __wrap(java_value: __DurationFormatUtils) -> 'DurationFormatUtils':
        return DurationFormatUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DurationFormatUtils):
        """
        Dynamic initializer for DurationFormatUtils.
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

    @staticmethod
    @overload
    def formatDurationISO(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDurationISO(long)"""
        return str.__wrap(__DurationFormatUtils.formatDurationISO(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def formatPeriodISO(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatPeriodISO(long,long)"""
        return str.__wrap(__DurationFormatUtils.formatPeriodISO(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def formatPeriod(arg0: int, arg1: int, arg2: str, arg3: bool, arg4: 'TimeZone') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatPeriod(long,long,java.lang.String,boolean,java.util.TimeZone)"""
        return str.__wrap(__DurationFormatUtils.formatPeriod(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __boolean.valueOf(arg3), arg4))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.DurationFormatUtils()"""
        val = __DurationFormatUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def formatDurationHMS(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDurationHMS(long)"""
        return str.__wrap(__DurationFormatUtils.formatDurationHMS(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def formatPeriod(arg0: int, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatPeriod(long,long,java.lang.String)"""
        return str.__wrap(__DurationFormatUtils.formatPeriod(__long.valueOf(arg0), __long.valueOf(arg1), arg2))

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
    def formatDuration(arg0: int, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDuration(long,java.lang.String)"""
        return str.__wrap(__DurationFormatUtils.formatDuration(__long.valueOf(arg0), arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def formatDurationWords(arg0: int, arg1: bool, arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDurationWords(long,boolean,boolean)"""
        return str.__wrap(__DurationFormatUtils.formatDurationWords(__long.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def formatDuration(arg0: int, arg1: str, arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDuration(long,java.lang.String,boolean)"""
        return str.__wrap(__DurationFormatUtils.formatDuration(__long.valueOf(arg0), arg1, __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.DurationFormatUtils()"""
        val = __DurationFormatUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.time.StopWatch
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.time.StopWatch as __StopWatch
__StopWatch = __StopWatch
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StopWatch():
    """org.apache.commons.lang3.time.StopWatch"""
 
    @staticmethod
    def __wrap(java_value: __StopWatch) -> 'StopWatch':
        return StopWatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StopWatch):
        """
        Dynamic initializer for StopWatch.
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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.toString()"""
        return str.__wrap(super(StopWatch, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isStarted(self) -> bool:
        """public boolean org.apache.commons.lang3.time.StopWatch.isStarted()"""
        return bool.__wrap(super(StopWatch, self).isStarted())

    @overload
    def getSplitTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getSplitTime()"""
        return int.__wrap(super(StopWatch, self).getSplitTime())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.StopWatch()"""
        val = __StopWatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def resume(self):
        """public void org.apache.commons.lang3.time.StopWatch.resume()"""
        super(StopWatch, self).resume()

    @overload
    def reset(self):
        """public void org.apache.commons.lang3.time.StopWatch.reset()"""
        super(StopWatch, self).reset()

    @overload
    def suspend(self):
        """public void org.apache.commons.lang3.time.StopWatch.suspend()"""
        super(StopWatch, self).suspend()

    @overload
    def formatTime(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.formatTime()"""
        return str.__wrap(super(StopWatch, self).formatTime())

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.time.StopWatch(java.lang.String)"""
        val = __StopWatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def split(self):
        """public void org.apache.commons.lang3.time.StopWatch.split()"""
        super(StopWatch, self).split()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def stop(self):
        """public void org.apache.commons.lang3.time.StopWatch.stop()"""
        super(StopWatch, self).stop()

    @overload
    def start(self):
        """public void org.apache.commons.lang3.time.StopWatch.start()"""
        super(StopWatch, self).start()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getTime()"""
        return int.__wrap(super(StopWatch, self).getTime())

    @overload
    def getSplitNanoTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getSplitNanoTime()"""
        return int.__wrap(super(StopWatch, self).getSplitNanoTime())

    @overload
    def getStartTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getStartTime()"""
        return int.__wrap(super(StopWatch, self).getStartTime())

    @overload
    def toSplitString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.toSplitString()"""
        return str.__wrap(super(StopWatch, self).toSplitString())

    @staticmethod
    @overload
    def createStarted() -> 'StopWatch':
        """public static org.apache.commons.lang3.time.StopWatch org.apache.commons.lang3.time.StopWatch.createStarted()"""
        return StopWatch.__wrap(__StopWatch.createStarted())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.StopWatch()"""
        val = __StopWatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def unsplit(self):
        """public void org.apache.commons.lang3.time.StopWatch.unsplit()"""
        super(StopWatch, self).unsplit()

    @overload
    def getTime(self, arg0: 'TimeUnit') -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getTime(java.util.concurrent.TimeUnit)"""
        return int.__wrap(super(__StopWatch, self).getTime(arg0))

    @overload
    def isStopped(self) -> bool:
        """public boolean org.apache.commons.lang3.time.StopWatch.isStopped()"""
        return bool.__wrap(super(StopWatch, self).isStopped())

    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.getMessage()"""
        return str.__wrap(super(StopWatch, self).getMessage())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getNanoTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getNanoTime()"""
        return int.__wrap(super(StopWatch, self).getNanoTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def formatSplitTime(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.formatSplitTime()"""
        return str.__wrap(super(StopWatch, self).formatSplitTime())

    @overload
    def isSuspended(self) -> bool:
        """public boolean org.apache.commons.lang3.time.StopWatch.isSuspended()"""
        return bool.__wrap(super(StopWatch, self).isSuspended())

    @staticmethod
    @overload
    def create() -> 'StopWatch':
        """public static org.apache.commons.lang3.time.StopWatch org.apache.commons.lang3.time.StopWatch.create()"""
        return StopWatch.__wrap(__StopWatch.create())

    @overload
    def getStopTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getStopTime()"""
        return int.__wrap(super(StopWatch, self).getStopTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.time.FastTimeZone
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.time.FastTimeZone as __FastTimeZone
__FastTimeZone = __FastTimeZone
import java.util.TimeZone as __TimeZone
__TimeZone = __TimeZone
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.TimeZone as TimeZone
from builtins import bool
from builtins import int
 
class FastTimeZone():
    """org.apache.commons.lang3.time.FastTimeZone"""
 
    @staticmethod
    def __wrap(java_value: __FastTimeZone) -> 'FastTimeZone':
        return FastTimeZone(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FastTimeZone):
        """
        Dynamic initializer for FastTimeZone.
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getGmtTimeZone(arg0: str) -> 'TimeZone':
        """public static java.util.TimeZone org.apache.commons.lang3.time.FastTimeZone.getGmtTimeZone(java.lang.String)"""
        return TimeZone.__wrap(__FastTimeZone.getGmtTimeZone(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getGmtTimeZone() -> 'TimeZone':
        """public static java.util.TimeZone org.apache.commons.lang3.time.FastTimeZone.getGmtTimeZone()"""
        return TimeZone.__wrap(__FastTimeZone.getGmtTimeZone())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTimeZone(arg0: str) -> 'TimeZone':
        """public static java.util.TimeZone org.apache.commons.lang3.time.FastTimeZone.getTimeZone(java.lang.String)"""
        return TimeZone.__wrap(__FastTimeZone.getTimeZone(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.time.DateParser
import java.text.ParsePosition as ParsePosition
import java.util.Calendar as Calendar
from abc import abstractmethod, ABC
import org.apache.commons.lang3.time.DateParser as __DateParser
__DateParser = __DateParser
 
class DateParser(ABC):
    """org.apache.commons.lang3.time.DateParser"""
 
    @staticmethod
    def __wrap(java_value: __DateParser) -> 'DateParser':
        return DateParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DateParser):
        """
        Dynamic initializer for DateParser.
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
 
    @abstractmethod
    def parseObject(self, arg0: str):
        """public abstract java.lang.Object org.apache.commons.lang3.time.DateParser.parseObject(java.lang.String) throws java.text.ParseException"""
        pass

    @abstractmethod
    def parse(self, arg0: str):
        """public abstract java.util.Date org.apache.commons.lang3.time.DateParser.parse(java.lang.String) throws java.text.ParseException"""
        pass

    @abstractmethod
    def parseObject(self, arg0: str, arg1: 'ParsePosition'):
        """public abstract java.lang.Object org.apache.commons.lang3.time.DateParser.parseObject(java.lang.String,java.text.ParsePosition)"""
        pass

    @abstractmethod
    def parse(self, arg0: str, arg1: 'ParsePosition', arg2: 'Calendar'):
        """public abstract boolean org.apache.commons.lang3.time.DateParser.parse(java.lang.String,java.text.ParsePosition,java.util.Calendar)"""
        pass

    @abstractmethod
    def parse(self, arg0: str, arg1: 'ParsePosition'):
        """public abstract java.util.Date org.apache.commons.lang3.time.DateParser.parse(java.lang.String,java.text.ParsePosition)"""
        pass

    @abstractmethod
    def getLocale(self, ):
        """public abstract java.util.Locale org.apache.commons.lang3.time.DateParser.getLocale()"""
        pass

    @abstractmethod
    def getTimeZone(self, ):
        """public abstract java.util.TimeZone org.apache.commons.lang3.time.DateParser.getTimeZone()"""
        pass

    @abstractmethod
    def getPattern(self, ):
        """public abstract java.lang.String org.apache.commons.lang3.time.DateParser.getPattern()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.time.FastDateFormat
import java.text.FieldPosition as FieldPosition
import java.util.Locale as Locale
import java.text.AttributedCharacterIterator as AttributedCharacterIterator
import java.lang.Appendable as __Appendable
__Appendable = __Appendable
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.text.ParsePosition as ParsePosition
import java.text.Format as __Format
__Format = __Format
import java.text.AttributedCharacterIterator as __AttributedCharacterIterator
__AttributedCharacterIterator = __AttributedCharacterIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.StringBuffer as __StringBuffer
__StringBuffer = __StringBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Calendar as Calendar
import org.apache.commons.lang3.time.FastDateFormat as __FastDateFormat
__FastDateFormat = __FastDateFormat
from builtins import object
import java.util.Date as Date
import java.lang.Appendable as Appendable
import java.util.TimeZone as __TimeZone
__TimeZone = __TimeZone
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.Date as __Date
__Date = __Date
import java.lang.Integer as __int
import java.util.TimeZone as TimeZone
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import int
 
class FastDateFormat(__Format, Format, __DateParser, DateParser, __DatePrinter, DatePrinter):
    """org.apache.commons.lang3.time.FastDateFormat"""
 
    @staticmethod
    def __wrap(java_value: __FastDateFormat) -> 'FastDateFormat':
        return FastDateFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FastDateFormat):
        """
        Dynamic initializer for FastDateFormat.
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
    def parse(self, arg0: str) -> 'Date':
        """public java.util.Date org.apache.commons.lang3.time.FastDateFormat.parse(java.lang.String) throws java.text.ParseException"""
        return 'Date'.__wrap(super(__FastDateFormat, self).parse(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.time.FastDateFormat.equals(java.lang.Object)"""
        return bool.__wrap(super(__FastDateFormat, self).equals(arg0))

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDateFormat.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'.__wrap(super(__FastDateFormat, self).format(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getInstance(arg0: str, arg1: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance(java.lang.String,java.util.Locale)"""
        return FastDateFormat.__wrap(__FastDateFormat.getInstance(arg0, arg1))

    @staticmethod
    @overload
    def getInstance(arg0: str, arg1: 'TimeZone') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance(java.lang.String,java.util.TimeZone)"""
        return FastDateFormat.__wrap(__FastDateFormat.getInstance(arg0, arg1))

    @staticmethod
    @overload
    def getTimeInstance(arg0: int) -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getTimeInstance(int)"""
        return FastDateFormat.__wrap(__FastDateFormat.getTimeInstance(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getDateTimeInstance(arg0: int, arg1: int, arg2: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateTimeInstance(int,int,java.util.Locale)"""
        return FastDateFormat.__wrap(__FastDateFormat.getDateTimeInstance(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def getTimeInstance(arg0: int, arg1: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getTimeInstance(int,java.util.Locale)"""
        return FastDateFormat.__wrap(__FastDateFormat.getTimeInstance(__int.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: 'Calendar') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.format(java.util.Calendar)"""
        return str.__wrap(super(__FastDateFormat, self).format(arg0))

    @overload
    def formatToCharacterIterator(self, arg0: object) -> 'AttributedCharacterIterator':
        """public java.text.AttributedCharacterIterator java.text.Format.formatToCharacterIterator(java.lang.Object)"""
        return 'AttributedCharacterIterator'.__wrap(super(__Format, self).formatToCharacterIterator(arg0))

    @staticmethod
    @overload
    def getDateInstance(arg0: int, arg1: 'TimeZone') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateInstance(int,java.util.TimeZone)"""
        return FastDateFormat.__wrap(__FastDateFormat.getDateInstance(__int.valueOf(arg0), arg1))

    @overload
    def getMaxLengthEstimate(self) -> int:
        """public int org.apache.commons.lang3.time.FastDateFormat.getMaxLengthEstimate()"""
        return int.__wrap(super(FastDateFormat, self).getMaxLengthEstimate())

    @staticmethod
    @overload
    def getDateTimeInstance(arg0: int, arg1: int, arg2: 'TimeZone', arg3: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateTimeInstance(int,int,java.util.TimeZone,java.util.Locale)"""
        return FastDateFormat.__wrap(__FastDateFormat.getDateTimeInstance(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @overload
    def format(self, arg0: object) -> str:
        """public final java.lang.String java.text.Format.format(java.lang.Object)"""
        return str.__wrap(super(__Format, self).format(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.time.FastDateFormat.hashCode()"""
        return int.__wrap(super(FastDateFormat, self).hashCode())

    @staticmethod
    @overload
    def getTimeInstance(arg0: int, arg1: 'TimeZone', arg2: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getTimeInstance(int,java.util.TimeZone,java.util.Locale)"""
        return FastDateFormat.__wrap(__FastDateFormat.getTimeInstance(__int.valueOf(arg0), arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getInstance(arg0: str) -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance(java.lang.String)"""
        return FastDateFormat.__wrap(__FastDateFormat.getInstance(arg0))

    @override
    @overload
    def getTimeZone(self) -> 'TimeZone':
        """public java.util.TimeZone org.apache.commons.lang3.time.FastDateFormat.getTimeZone()"""
        return 'TimeZone'.__wrap(super(FastDateFormat, self).getTimeZone())

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale org.apache.commons.lang3.time.FastDateFormat.getLocale()"""
        return 'Locale'.__wrap(super(FastDateFormat, self).getLocale())

    @staticmethod
    @overload
    def getDateInstance(arg0: int, arg1: 'TimeZone', arg2: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateInstance(int,java.util.TimeZone,java.util.Locale)"""
        return FastDateFormat.__wrap(__FastDateFormat.getDateInstance(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def getDateInstance(arg0: int) -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateInstance(int)"""
        return FastDateFormat.__wrap(__FastDateFormat.getDateInstance(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.toString()"""
        return str.__wrap(super(FastDateFormat, self).toString())

    @overload
    def format(self, arg0: 'Date', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDateFormat.format(java.util.Date,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDateFormat, self).format(arg0, arg1))

    @overload
    def parseObject(self, arg0: str, arg1: 'ParsePosition') -> object:
        """public java.lang.Object org.apache.commons.lang3.time.FastDateFormat.parseObject(java.lang.String,java.text.ParsePosition)"""
        return object.__wrap(super(__FastDateFormat, self).parseObject(arg0, arg1))

    @staticmethod
    @overload
    def getDateTimeInstance(arg0: int, arg1: int) -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateTimeInstance(int,int)"""
        return FastDateFormat.__wrap(__FastDateFormat.getDateTimeInstance(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def format(self, arg0: int, arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDateFormat.format(long,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDateFormat, self).format(__long.valueOf(arg0), arg1))

    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition', arg2: 'Calendar') -> bool:
        """public boolean org.apache.commons.lang3.time.FastDateFormat.parse(java.lang.String,java.text.ParsePosition,java.util.Calendar)"""
        return bool.__wrap(super(__FastDateFormat, self).parse(arg0, arg1, arg2))

    @overload
    def format(self, arg0: int, arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDateFormat.format(long,B)"""
        return 'Appendable'.__wrap(super(__FastDateFormat, self).format(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def getInstance() -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance()"""
        return FastDateFormat.__wrap(__FastDateFormat.getInstance())

    @staticmethod
    @overload
    def getDateInstance(arg0: int, arg1: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateInstance(int,java.util.Locale)"""
        return FastDateFormat.__wrap(__FastDateFormat.getDateInstance(__int.valueOf(arg0), arg1))

    @overload
    def parseObject(self, arg0: str) -> object:
        """public java.lang.Object java.text.Format.parseObject(java.lang.String) throws java.text.ParseException"""
        return object.__wrap(super(__Format, self).parseObject(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def format(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.format(long)"""
        return str.__wrap(super(__FastDateFormat, self).format(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def format(self, arg0: 'Date', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDateFormat.format(java.util.Date,B)"""
        return 'Appendable'.__wrap(super(__FastDateFormat, self).format(arg0, arg1))

    @staticmethod
    @overload
    def getDateTimeInstance(arg0: int, arg1: int, arg2: 'TimeZone') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateTimeInstance(int,int,java.util.TimeZone)"""
        return FastDateFormat.__wrap(__FastDateFormat.getDateTimeInstance(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def format(self, arg0: 'Date') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.format(java.util.Date)"""
        return str.__wrap(super(__FastDateFormat, self).format(arg0))

    @overload
    def format(self, arg0: 'Calendar', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDateFormat.format(java.util.Calendar,java.lang.StringBuffer)"""
        return 'StringBuffer'.__wrap(super(__FastDateFormat, self).format(arg0, arg1))

    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition') -> 'Date':
        """public java.util.Date org.apache.commons.lang3.time.FastDateFormat.parse(java.lang.String,java.text.ParsePosition)"""
        return 'Date'.__wrap(super(__FastDateFormat, self).parse(arg0, arg1))

    @staticmethod
    @overload
    def getTimeInstance(arg0: int, arg1: 'TimeZone') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getTimeInstance(int,java.util.TimeZone)"""
        return FastDateFormat.__wrap(__FastDateFormat.getTimeInstance(__int.valueOf(arg0), arg1))

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.text.Format.clone()"""
        return object.__wrap(super(Format, self).clone())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def format(self, arg0: 'Calendar', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDateFormat.format(java.util.Calendar,B)"""
        return 'Appendable'.__wrap(super(__FastDateFormat, self).format(arg0, arg1))

    @staticmethod
    @overload
    def getInstance(arg0: str, arg1: 'TimeZone', arg2: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance(java.lang.String,java.util.TimeZone,java.util.Locale)"""
        return FastDateFormat.__wrap(__FastDateFormat.getInstance(arg0, arg1, arg2))

    @override
    @overload
    def getPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.getPattern()"""
        return str.__wrap(super(FastDateFormat, self).getPattern()) 
 
 
# CLASS: org.apache.commons.lang3.time.FastDateParser
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.text.ParsePosition as ParsePosition
import java.util.Calendar as Calendar
from builtins import object
import java.util.Date as Date
import java.util.TimeZone as __TimeZone
__TimeZone = __TimeZone
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import org.apache.commons.lang3.time.FastDateParser as __FastDateParser
__FastDateParser = __FastDateParser
import java.lang.Object as __Object
__Object = __Object
import java.util.Date as __Date
__Date = __Date
import java.lang.Integer as __int
from builtins import bool
import java.util.TimeZone as TimeZone
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import int
 
class FastDateParser(__DateParser, DateParser, __Serializable, Serializable):
    """org.apache.commons.lang3.time.FastDateParser"""
 
    @staticmethod
    def __wrap(java_value: __FastDateParser) -> 'FastDateParser':
        return FastDateParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FastDateParser):
        """
        Dynamic initializer for FastDateParser.
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
    def parse(self, arg0: str, arg1: 'ParsePosition', arg2: 'Calendar') -> bool:
        """public boolean org.apache.commons.lang3.time.FastDateParser.parse(java.lang.String,java.text.ParsePosition,java.util.Calendar)"""
        return bool.__wrap(super(__FastDateParser, self).parse(arg0, arg1, arg2))

    @overload
    def toStringAll(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateParser.toStringAll()"""
        return str.__wrap(super(FastDateParser, self).toStringAll())

    @overload
    def parseObject(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.time.FastDateParser.parseObject(java.lang.String) throws java.text.ParseException"""
        return object.__wrap(super(__FastDateParser, self).parseObject(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateParser.toString()"""
        return str.__wrap(super(FastDateParser, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.time.FastDateParser.equals(java.lang.Object)"""
        return bool.__wrap(super(__FastDateParser, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getTimeZone(self) -> 'TimeZone':
        """public java.util.TimeZone org.apache.commons.lang3.time.FastDateParser.getTimeZone()"""
        return 'TimeZone'.__wrap(super(FastDateParser, self).getTimeZone())

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
        """public int org.apache.commons.lang3.time.FastDateParser.hashCode()"""
        return int.__wrap(super(FastDateParser, self).hashCode())

    @overload
    def parse(self, arg0: str) -> 'Date':
        """public java.util.Date org.apache.commons.lang3.time.FastDateParser.parse(java.lang.String) throws java.text.ParseException"""
        return 'Date'.__wrap(super(__FastDateParser, self).parse(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateParser.getPattern()"""
        return str.__wrap(super(FastDateParser, self).getPattern())

    @overload
    def parseObject(self, arg0: str, arg1: 'ParsePosition') -> object:
        """public java.lang.Object org.apache.commons.lang3.time.FastDateParser.parseObject(java.lang.String,java.text.ParsePosition)"""
        return object.__wrap(super(__FastDateParser, self).parseObject(arg0, arg1))

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale org.apache.commons.lang3.time.FastDateParser.getLocale()"""
        return 'Locale'.__wrap(super(FastDateParser, self).getLocale())

    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition') -> 'Date':
        """public java.util.Date org.apache.commons.lang3.time.FastDateParser.parse(java.lang.String,java.text.ParsePosition)"""
        return 'Date'.__wrap(super(__FastDateParser, self).parse(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.time.DatePrinter
import java.text.FieldPosition as FieldPosition
import java.lang.StringBuffer as StringBuffer
import java.util.Calendar as Calendar
import org.apache.commons.lang3.time.DatePrinter as __DatePrinter
__DatePrinter = __DatePrinter
from abc import abstractmethod, ABC
import java.lang.Appendable as Appendable
import java.util.Date as Date
 
class DatePrinter(ABC):
    """org.apache.commons.lang3.time.DatePrinter"""
 
    @staticmethod
    def __wrap(java_value: __DatePrinter) -> 'DatePrinter':
        return DatePrinter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DatePrinter):
        """
        Dynamic initializer for DatePrinter.
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
 
    @abstractmethod
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition'):
        """public abstract java.lang.StringBuffer org.apache.commons.lang3.time.DatePrinter.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        pass

    @abstractmethod
    def format(self, arg0: 'Date'):
        """public abstract java.lang.String org.apache.commons.lang3.time.DatePrinter.format(java.util.Date)"""
        pass

    @abstractmethod
    def format(self, arg0: 'Calendar', arg1: 'StringBuffer'):
        """public abstract java.lang.StringBuffer org.apache.commons.lang3.time.DatePrinter.format(java.util.Calendar,java.lang.StringBuffer)"""
        pass

    @abstractmethod
    def format(self, arg0: int, arg1: 'Appendable'):
        """public abstract <B extends java.lang.Appendable> B org.apache.commons.lang3.time.DatePrinter.format(long,B)"""
        pass

    @abstractmethod
    def getLocale(self, ):
        """public abstract java.util.Locale org.apache.commons.lang3.time.DatePrinter.getLocale()"""
        pass

    @abstractmethod
    def format(self, arg0: 'Calendar'):
        """public abstract java.lang.String org.apache.commons.lang3.time.DatePrinter.format(java.util.Calendar)"""
        pass

    @abstractmethod
    def format(self, arg0: int):
        """public abstract java.lang.String org.apache.commons.lang3.time.DatePrinter.format(long)"""
        pass

    @abstractmethod
    def format(self, arg0: 'Date', arg1: 'Appendable'):
        """public abstract <B extends java.lang.Appendable> B org.apache.commons.lang3.time.DatePrinter.format(java.util.Date,B)"""
        pass

    @abstractmethod
    def format(self, arg0: int, arg1: 'StringBuffer'):
        """public abstract java.lang.StringBuffer org.apache.commons.lang3.time.DatePrinter.format(long,java.lang.StringBuffer)"""
        pass

    @abstractmethod
    def format(self, arg0: 'Calendar', arg1: 'Appendable'):
        """public abstract <B extends java.lang.Appendable> B org.apache.commons.lang3.time.DatePrinter.format(java.util.Calendar,B)"""
        pass

    @abstractmethod
    def getTimeZone(self, ):
        """public abstract java.util.TimeZone org.apache.commons.lang3.time.DatePrinter.getTimeZone()"""
        pass

    @abstractmethod
    def format(self, arg0: 'Date', arg1: 'StringBuffer'):
        """public abstract java.lang.StringBuffer org.apache.commons.lang3.time.DatePrinter.format(java.util.Date,java.lang.StringBuffer)"""
        pass

    @abstractmethod
    def getPattern(self, ):
        """public abstract java.lang.String org.apache.commons.lang3.time.DatePrinter.getPattern()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.time.DateFormatUtils
import java.util.Locale as Locale
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Calendar as Calendar
import java.util.Date as Date
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.time.DateFormatUtils as __DateFormatUtils
__DateFormatUtils = __DateFormatUtils
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.TimeZone as TimeZone
from builtins import bool
from builtins import int
 
class DateFormatUtils():
    """org.apache.commons.lang3.time.DateFormatUtils"""
 
    @staticmethod
    def __wrap(java_value: __DateFormatUtils) -> 'DateFormatUtils':
        return DateFormatUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DateFormatUtils):
        """
        Dynamic initializer for DateFormatUtils.
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
    def format(arg0: 'Calendar', arg1: str, arg2: 'TimeZone') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Calendar,java.lang.String,java.util.TimeZone)"""
        return str.__wrap(__DateFormatUtils.format(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def format(arg0: int, arg1: str, arg2: 'TimeZone') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(long,java.lang.String,java.util.TimeZone)"""
        return str.__wrap(__DateFormatUtils.format(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: str, arg2: 'TimeZone', arg3: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Date,java.lang.String,java.util.TimeZone,java.util.Locale)"""
        return str.__wrap(__DateFormatUtils.format(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Date,java.lang.String)"""
        return str.__wrap(__DateFormatUtils.format(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.DateFormatUtils()"""
        val = __DateFormatUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def format(arg0: 'Calendar', arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Calendar,java.lang.String,java.util.Locale)"""
        return str.__wrap(__DateFormatUtils.format(arg0, arg1, arg2))

    @staticmethod
    @overload
    def format(arg0: 'Calendar', arg1: str, arg2: 'TimeZone', arg3: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Calendar,java.lang.String,java.util.TimeZone,java.util.Locale)"""
        return str.__wrap(__DateFormatUtils.format(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def formatUTC(arg0: 'Date', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.formatUTC(java.util.Date,java.lang.String)"""
        return str.__wrap(__DateFormatUtils.formatUTC(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def formatUTC(arg0: int, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.formatUTC(long,java.lang.String)"""
        return str.__wrap(__DateFormatUtils.formatUTC(__long.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def format(arg0: int, arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(long,java.lang.String,java.util.Locale)"""
        return str.__wrap(__DateFormatUtils.format(__long.valueOf(arg0), arg1, arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.DateFormatUtils()"""
        val = __DateFormatUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def format(arg0: int, arg1: str, arg2: 'TimeZone', arg3: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(long,java.lang.String,java.util.TimeZone,java.util.Locale)"""
        return str.__wrap(__DateFormatUtils.format(__long.valueOf(arg0), arg1, arg2, arg3))

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: str, arg2: 'TimeZone') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Date,java.lang.String,java.util.TimeZone)"""
        return str.__wrap(__DateFormatUtils.format(arg0, arg1, arg2))

    @staticmethod
    @overload
    def formatUTC(arg0: 'Date', arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.formatUTC(java.util.Date,java.lang.String,java.util.Locale)"""
        return str.__wrap(__DateFormatUtils.formatUTC(arg0, arg1, arg2))

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
    def format(arg0: int, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(long,java.lang.String)"""
        return str.__wrap(__DateFormatUtils.format(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Date,java.lang.String,java.util.Locale)"""
        return str.__wrap(__DateFormatUtils.format(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def formatUTC(arg0: int, arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.formatUTC(long,java.lang.String,java.util.Locale)"""
        return str.__wrap(__DateFormatUtils.formatUTC(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def format(arg0: 'Calendar', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Calendar,java.lang.String)"""
        return str.__wrap(__DateFormatUtils.format(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.time.DurationUtils
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.time.temporal.Temporal as Temporal
import java.lang.Object as __object
from builtins import type
import java.time.Duration as Duration
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.time.DurationUtils as __DurationUtils
__DurationUtils = __DurationUtils
import java.time.Duration as __Duration
__Duration = __Duration
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DurationUtils():
    """org.apache.commons.lang3.time.DurationUtils"""
 
    @staticmethod
    def __wrap(java_value: __DurationUtils) -> 'DurationUtils':
        return DurationUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DurationUtils):
        """
        Dynamic initializer for DurationUtils.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.DurationUtils()"""
        val = __DurationUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def since(arg0: 'Temporal') -> 'Duration':
        """public static java.time.Duration org.apache.commons.lang3.time.DurationUtils.since(java.time.temporal.Temporal)"""
        return Duration.__wrap(__DurationUtils.since(arg0))

    @staticmethod
    @overload
    def accept(arg0: 'FailableBiConsumer', arg1: 'Duration'):
        """public static <T extends java.lang.Throwable> void org.apache.commons.lang3.time.DurationUtils.accept(org.apache.commons.lang3.function.FailableBiConsumer<java.lang.Long, java.lang.Integer, T>,java.time.Duration) throws T"""
        __DurationUtils.accept(arg0, arg1)

    @staticmethod
    @overload
    def isPositive(arg0: 'Duration') -> bool:
        """public static boolean org.apache.commons.lang3.time.DurationUtils.isPositive(java.time.Duration)"""
        return bool.__wrap(__DurationUtils.isPositive(arg0))

    @staticmethod
    @overload
    def of(arg0: 'FailableConsumer') -> 'Duration':
        """public static <E extends java.lang.Throwable> java.time.Duration org.apache.commons.lang3.time.DurationUtils.of(org.apache.commons.lang3.function.FailableConsumer<java.time.Instant, E>) throws E"""
        return Duration.__wrap(__DurationUtils.of(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toMillisInt(arg0: 'Duration') -> int:
        """public static int org.apache.commons.lang3.time.DurationUtils.toMillisInt(java.time.Duration)"""
        return int.__wrap(__DurationUtils.toMillisInt(arg0))

    @staticmethod
    @overload
    def of(arg0: 'FailableRunnable') -> 'Duration':
        """public static <E extends java.lang.Throwable> java.time.Duration org.apache.commons.lang3.time.DurationUtils.of(org.apache.commons.lang3.function.FailableRunnable<E>) throws E"""
        return Duration.__wrap(__DurationUtils.of(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.time.DurationUtils()"""
        val = __DurationUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def zeroIfNull(arg0: 'Duration') -> 'Duration':
        """public static java.time.Duration org.apache.commons.lang3.time.DurationUtils.zeroIfNull(java.time.Duration)"""
        return Duration.__wrap(__DurationUtils.zeroIfNull(arg0))

    @staticmethod
    @overload
    def getNanosOfMilli(arg0: 'Duration') -> int:
        """public static int org.apache.commons.lang3.time.DurationUtils.getNanosOfMilli(java.time.Duration)"""
        return int.__wrap(__DurationUtils.getNanosOfMilli(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toDuration(arg0: int, arg1: 'TimeUnit') -> 'Duration':
        """public static java.time.Duration org.apache.commons.lang3.time.DurationUtils.toDuration(long,java.util.concurrent.TimeUnit)"""
        return Duration.__wrap(__DurationUtils.toDuration(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def getNanosOfMiili(arg0: 'Duration') -> int:
        """public static int org.apache.commons.lang3.time.DurationUtils.getNanosOfMiili(java.time.Duration)"""
        return int.__wrap(__DurationUtils.getNanosOfMiili(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.time.DateUtils
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Calendar as __Calendar
__Calendar = __Calendar
import java.util.Calendar as Calendar
import java.util.Date as Date
import java.util.Iterator as Iterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.time.DateUtils as __DateUtils
__DateUtils = __DateUtils
import java.lang.Integer as __int
import java.util.Date as __Date
__Date = __Date
from builtins import bool
import java.util.TimeZone as TimeZone
from builtins import int
 
class DateUtils():
    """org.apache.commons.lang3.time.DateUtils"""
 
    @staticmethod
    def __wrap(java_value: __DateUtils) -> 'DateUtils':
        return DateUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DateUtils):
        """
        Dynamic initializer for DateUtils.
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
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.DateUtils()"""
        val = __DateUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def round(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.round(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.round(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def addYears(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addYears(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.addYears(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ceiling(arg0: 'Calendar', arg1: int) -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.ceiling(java.util.Calendar,int)"""
        return Calendar.__wrap(__DateUtils.ceiling(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameDay(arg0: 'Calendar', arg1: 'Calendar') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameDay(java.util.Calendar,java.util.Calendar)"""
        return bool.__wrap(__DateUtils.isSameDay(arg0, arg1))

    @staticmethod
    @overload
    def getFragmentInSeconds(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInSeconds(java.util.Calendar,int)"""
        return int.__wrap(__DateUtils.getFragmentInSeconds(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def setHours(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setHours(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.setHours(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def truncatedCompareTo(arg0: 'Calendar', arg1: 'Calendar', arg2: int) -> int:
        """public static int org.apache.commons.lang3.time.DateUtils.truncatedCompareTo(java.util.Calendar,java.util.Calendar,int)"""
        return int.__wrap(__DateUtils.truncatedCompareTo(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def setYears(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setYears(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.setYears(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def iterator(arg0: 'Calendar', arg1: int) -> 'Iterator':
        """public static java.util.Iterator<java.util.Calendar> org.apache.commons.lang3.time.DateUtils.iterator(java.util.Calendar,int)"""
        return Iterator.__wrap(__DateUtils.iterator(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isSameInstant(arg0: 'Calendar', arg1: 'Calendar') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameInstant(java.util.Calendar,java.util.Calendar)"""
        return bool.__wrap(__DateUtils.isSameInstant(arg0, arg1))

    @staticmethod
    @overload
    def truncate(arg0: object, arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.truncate(java.lang.Object,int)"""
        return Date.__wrap(__DateUtils.truncate(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def addMinutes(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addMinutes(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.addMinutes(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def toCalendar(arg0: 'Date') -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.toCalendar(java.util.Date)"""
        return Calendar.__wrap(__DateUtils.toCalendar(arg0))

    @staticmethod
    @overload
    def isSameInstant(arg0: 'Date', arg1: 'Date') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameInstant(java.util.Date,java.util.Date)"""
        return bool.__wrap(__DateUtils.isSameInstant(arg0, arg1))

    @staticmethod
    @overload
    def getFragmentInSeconds(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInSeconds(java.util.Date,int)"""
        return int.__wrap(__DateUtils.getFragmentInSeconds(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def round(arg0: object, arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.round(java.lang.Object,int)"""
        return Date.__wrap(__DateUtils.round(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def parseDateStrictly(arg0: str, *arg1: str) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.parseDateStrictly(java.lang.String,java.lang.String...) throws java.text.ParseException"""
        return Date.__wrap(__DateUtils.parseDateStrictly(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def addHours(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addHours(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.addHours(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def iterator(arg0: 'Date', arg1: int) -> 'Iterator':
        """public static java.util.Iterator<java.util.Calendar> org.apache.commons.lang3.time.DateUtils.iterator(java.util.Date,int)"""
        return Iterator.__wrap(__DateUtils.iterator(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def addMonths(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addMonths(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.addMonths(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInMilliseconds(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInMilliseconds(java.util.Calendar,int)"""
        return int.__wrap(__DateUtils.getFragmentInMilliseconds(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInMilliseconds(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInMilliseconds(java.util.Date,int)"""
        return int.__wrap(__DateUtils.getFragmentInMilliseconds(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInHours(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInHours(java.util.Calendar,int)"""
        return int.__wrap(__DateUtils.getFragmentInHours(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def iterator(arg0: object, arg1: int) -> 'Iterator':
        """public static java.util.Iterator<?> org.apache.commons.lang3.time.DateUtils.iterator(java.lang.Object,int)"""
        return Iterator.__wrap(__DateUtils.iterator(arg0, __int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.DateUtils()"""
        val = __DateUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def truncate(arg0: 'Calendar', arg1: int) -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.truncate(java.util.Calendar,int)"""
        return Calendar.__wrap(__DateUtils.truncate(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def setDays(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setDays(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.setDays(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInHours(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInHours(java.util.Date,int)"""
        return int.__wrap(__DateUtils.getFragmentInHours(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getFragmentInDays(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInDays(java.util.Date,int)"""
        return int.__wrap(__DateUtils.getFragmentInDays(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def setMonths(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setMonths(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.setMonths(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def setSeconds(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setSeconds(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.setSeconds(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def parseDateStrictly(arg0: str, arg1: 'Locale', *arg2: str) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.parseDateStrictly(java.lang.String,java.util.Locale,java.lang.String...) throws java.text.ParseException"""
        return Date.__wrap(__DateUtils.parseDateStrictly(arg0, arg1, arg2))

    @staticmethod
    @overload
    def addMilliseconds(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addMilliseconds(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.addMilliseconds(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def truncatedEquals(arg0: 'Date', arg1: 'Date', arg2: int) -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.truncatedEquals(java.util.Date,java.util.Date,int)"""
        return bool.__wrap(__DateUtils.truncatedEquals(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def truncatedCompareTo(arg0: 'Date', arg1: 'Date', arg2: int) -> int:
        """public static int org.apache.commons.lang3.time.DateUtils.truncatedCompareTo(java.util.Date,java.util.Date,int)"""
        return int.__wrap(__DateUtils.truncatedCompareTo(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def addWeeks(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addWeeks(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.addWeeks(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ceiling(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.ceiling(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.ceiling(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInMinutes(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInMinutes(java.util.Date,int)"""
        return int.__wrap(__DateUtils.getFragmentInMinutes(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def addDays(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addDays(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.addDays(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def setMinutes(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setMinutes(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.setMinutes(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def parseDate(arg0: str, arg1: 'Locale', *arg2: str) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.parseDate(java.lang.String,java.util.Locale,java.lang.String...) throws java.text.ParseException"""
        return Date.__wrap(__DateUtils.parseDate(arg0, arg1, arg2))

    @staticmethod
    @overload
    def toCalendar(arg0: 'Date', arg1: 'TimeZone') -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.toCalendar(java.util.Date,java.util.TimeZone)"""
        return Calendar.__wrap(__DateUtils.toCalendar(arg0, arg1))

    @staticmethod
    @overload
    def isSameDay(arg0: 'Date', arg1: 'Date') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameDay(java.util.Date,java.util.Date)"""
        return bool.__wrap(__DateUtils.isSameDay(arg0, arg1))

    @staticmethod
    @overload
    def isSameLocalTime(arg0: 'Calendar', arg1: 'Calendar') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameLocalTime(java.util.Calendar,java.util.Calendar)"""
        return bool.__wrap(__DateUtils.isSameLocalTime(arg0, arg1))

    @staticmethod
    @overload
    def getFragmentInMinutes(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInMinutes(java.util.Calendar,int)"""
        return int.__wrap(__DateUtils.getFragmentInMinutes(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def parseDate(arg0: str, *arg1: str) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.parseDate(java.lang.String,java.lang.String...) throws java.text.ParseException"""
        return Date.__wrap(__DateUtils.parseDate(arg0, arg1))

    @staticmethod
    @overload
    def setMilliseconds(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setMilliseconds(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.setMilliseconds(arg0, __int.valueOf(arg1)))

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
    def round(arg0: 'Calendar', arg1: int) -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.round(java.util.Calendar,int)"""
        return Calendar.__wrap(__DateUtils.round(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def addSeconds(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addSeconds(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.addSeconds(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def truncate(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.truncate(java.util.Date,int)"""
        return Date.__wrap(__DateUtils.truncate(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInDays(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInDays(java.util.Calendar,int)"""
        return int.__wrap(__DateUtils.getFragmentInDays(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def truncatedEquals(arg0: 'Calendar', arg1: 'Calendar', arg2: int) -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.truncatedEquals(java.util.Calendar,java.util.Calendar,int)"""
        return bool.__wrap(__DateUtils.truncatedEquals(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def ceiling(arg0: object, arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.ceiling(java.lang.Object,int)"""
        return Date.__wrap(__DateUtils.ceiling(arg0, __int.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.lang3.time.CalendarUtils
from builtins import str
import org.apache.commons.lang3.time.CalendarUtils as __CalendarUtils
__CalendarUtils = __CalendarUtils
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Calendar as Calendar
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CalendarUtils():
    """org.apache.commons.lang3.time.CalendarUtils"""
 
    @staticmethod
    def __wrap(java_value: __CalendarUtils) -> 'CalendarUtils':
        return CalendarUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CalendarUtils):
        """
        Dynamic initializer for CalendarUtils.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getDayOfYear(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getDayOfYear()"""
        return int.__wrap(super(CalendarUtils, self).getDayOfYear())

    @overload
    def getDayOfMonth(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getDayOfMonth()"""
        return int.__wrap(super(CalendarUtils, self).getDayOfMonth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Calendar'):
        """public org.apache.commons.lang3.time.CalendarUtils(java.util.Calendar)"""
        val = __CalendarUtils(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def getMonth(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getMonth()"""
        return int.__wrap(super(CalendarUtils, self).getMonth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getYear(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getYear()"""
        return int.__wrap(super(CalendarUtils, self).getYear())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))