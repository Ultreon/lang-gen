from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Calendar as Calendar
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.time.CalendarUtils as _CalendarUtils
_CalendarUtils = _CalendarUtils
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CalendarUtils():
    """org.apache.commons.lang3.time.CalendarUtils"""
 
    @staticmethod
    def _wrap(java_value: _CalendarUtils) -> 'CalendarUtils':
        return CalendarUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CalendarUtils):
        """
        Dynamic initializer for CalendarUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CalendarUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CalendarUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDayOfMonth(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getDayOfMonth()"""
        return int._wrap(super(CalendarUtils, self).getDayOfMonth())

    @overload
    def getMonth(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getMonth()"""
        return int._wrap(super(CalendarUtils, self).getMonth())

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
    def __init__(self, arg0: 'Calendar'):
        """public org.apache.commons.lang3.time.CalendarUtils(java.util.Calendar)"""
        val = _CalendarUtils(arg0)
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

    @overload
    def getDayOfYear(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getDayOfYear()"""
        return int._wrap(super(CalendarUtils, self).getDayOfYear())

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
    def getYear(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getYear()"""
        return int._wrap(super(CalendarUtils, self).getYear())

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

 
 
 
# CLASS: org.apache.commons.lang3.time.CalendarUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Calendar as Calendar
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.time.CalendarUtils as _CalendarUtils
_CalendarUtils = _CalendarUtils
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CalendarUtils():
    """org.apache.commons.lang3.time.CalendarUtils"""
 
    @staticmethod
    def _wrap(java_value: _CalendarUtils) -> 'CalendarUtils':
        return CalendarUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CalendarUtils):
        """
        Dynamic initializer for CalendarUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CalendarUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CalendarUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDayOfMonth(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getDayOfMonth()"""
        return int._wrap(super(CalendarUtils, self).getDayOfMonth())

    @overload
    def getMonth(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getMonth()"""
        return int._wrap(super(CalendarUtils, self).getMonth())

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
    def __init__(self, arg0: 'Calendar'):
        """public org.apache.commons.lang3.time.CalendarUtils(java.util.Calendar)"""
        val = _CalendarUtils(arg0)
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

    @overload
    def getDayOfYear(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getDayOfYear()"""
        return int._wrap(super(CalendarUtils, self).getDayOfYear())

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
    def getYear(self) -> int:
        """public int org.apache.commons.lang3.time.CalendarUtils.getYear()"""
        return int._wrap(super(CalendarUtils, self).getYear())

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

 
 
 
# CLASS: org.apache.commons.lang3.time.CalendarUtils 
 
 
# CLASS: org.apache.commons.lang3.time.DatePrinter
import java.text.FieldPosition as FieldPosition
import java.lang.StringBuffer as StringBuffer
import java.util.Calendar as Calendar
from abc import abstractmethod, ABC
import org.apache.commons.lang3.time.DatePrinter as _DatePrinter
_DatePrinter = _DatePrinter
import java.lang.Appendable as Appendable
import java.util.Date as Date
 
class DatePrinter():
    """org.apache.commons.lang3.time.DatePrinter"""
 
    @staticmethod
    def _wrap(java_value: _DatePrinter) -> 'DatePrinter':
        return DatePrinter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DatePrinter):
        """
        Dynamic initializer for DatePrinter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DatePrinter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DatePrinter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: org.apache.commons.lang3.time.StopWatch
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.time.StopWatch as _StopWatch
_StopWatch = _StopWatch
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StopWatch():
    """org.apache.commons.lang3.time.StopWatch"""
 
    @staticmethod
    def _wrap(java_value: _StopWatch) -> 'StopWatch':
        return StopWatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StopWatch):
        """
        Dynamic initializer for StopWatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StopWatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StopWatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isStarted(self) -> bool:
        """public boolean org.apache.commons.lang3.time.StopWatch.isStarted()"""
        return bool._wrap(super(StopWatch, self).isStarted())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.StopWatch()"""
        val = _StopWatch()
        self.__wrapper = val

    @staticmethod
    @overload
    def create() -> 'StopWatch':
        """public static org.apache.commons.lang3.time.StopWatch org.apache.commons.lang3.time.StopWatch.create()"""
        return StopWatch._wrap(_StopWatch.create())

    @overload
    def getSplitNanoTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getSplitNanoTime()"""
        return int._wrap(super(StopWatch, self).getSplitNanoTime())

    @overload
    def toSplitString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.toSplitString()"""
        return str._wrap(super(StopWatch, self).toSplitString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def formatTime(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.formatTime()"""
        return str._wrap(super(StopWatch, self).formatTime())

    @overload
    def resume(self):
        """public void org.apache.commons.lang3.time.StopWatch.resume()"""
        super(StopWatch, self).resume()

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.time.StopWatch(java.lang.String)"""
        val = _StopWatch(arg0)
        self.__wrapper = val

    @overload
    def reset(self):
        """public void org.apache.commons.lang3.time.StopWatch.reset()"""
        super(StopWatch, self).reset()

    @overload
    def suspend(self):
        """public void org.apache.commons.lang3.time.StopWatch.suspend()"""
        super(StopWatch, self).suspend()

    @overload
    def getStartTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getStartTime()"""
        return int._wrap(super(StopWatch, self).getStartTime())

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
    def split(self):
        """public void org.apache.commons.lang3.time.StopWatch.split()"""
        super(StopWatch, self).split()

    @overload
    def getSplitTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getSplitTime()"""
        return int._wrap(super(StopWatch, self).getSplitTime())

    @overload
    def stop(self):
        """public void org.apache.commons.lang3.time.StopWatch.stop()"""
        super(StopWatch, self).stop()

    @overload
    def getTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getTime()"""
        return int._wrap(super(StopWatch, self).getTime())

    @overload
    def formatSplitTime(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.formatSplitTime()"""
        return str._wrap(super(StopWatch, self).formatSplitTime())

    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.getMessage()"""
        return str._wrap(super(StopWatch, self).getMessage())

    @overload
    def start(self):
        """public void org.apache.commons.lang3.time.StopWatch.start()"""
        super(StopWatch, self).start()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.StopWatch()"""
        val = _StopWatch()
        self.__wrapper = val

    @overload
    def unsplit(self):
        """public void org.apache.commons.lang3.time.StopWatch.unsplit()"""
        super(StopWatch, self).unsplit()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def createStarted() -> 'StopWatch':
        """public static org.apache.commons.lang3.time.StopWatch org.apache.commons.lang3.time.StopWatch.createStarted()"""
        return StopWatch._wrap(_StopWatch.createStarted())

    @overload
    def isSuspended(self) -> bool:
        """public boolean org.apache.commons.lang3.time.StopWatch.isSuspended()"""
        return bool._wrap(super(StopWatch, self).isSuspended())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.StopWatch.toString()"""
        return str._wrap(super(StopWatch, self).toString())

    @overload
    def getTime(self, arg0: 'TimeUnit') -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getTime(java.util.concurrent.TimeUnit)"""
        return int._wrap(super(_StopWatch, self).getTime(arg0))

    @overload
    def getStopTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getStopTime()"""
        return int._wrap(super(StopWatch, self).getStopTime())

    @overload
    def isStopped(self) -> bool:
        """public boolean org.apache.commons.lang3.time.StopWatch.isStopped()"""
        return bool._wrap(super(StopWatch, self).isStopped())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getNanoTime(self) -> int:
        """public long org.apache.commons.lang3.time.StopWatch.getNanoTime()"""
        return int._wrap(super(StopWatch, self).getNanoTime())

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
 
 
# CLASS: org.apache.commons.lang3.time.DurationFormatUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.TimeZone as TimeZone
from builtins import bool
import org.apache.commons.lang3.time.DurationFormatUtils as _DurationFormatUtils
_DurationFormatUtils = _DurationFormatUtils
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DurationFormatUtils():
    """org.apache.commons.lang3.time.DurationFormatUtils"""
 
    @staticmethod
    def _wrap(java_value: _DurationFormatUtils) -> 'DurationFormatUtils':
        return DurationFormatUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DurationFormatUtils):
        """
        Dynamic initializer for DurationFormatUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DurationFormatUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DurationFormatUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.DurationFormatUtils()"""
        val = _DurationFormatUtils()
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def formatDuration(arg0: int, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDuration(long,java.lang.String)"""
        return str._wrap(_DurationFormatUtils.formatDuration(_long.valueOf(arg0), arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def formatDuration(arg0: int, arg1: str, arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDuration(long,java.lang.String,boolean)"""
        return str._wrap(_DurationFormatUtils.formatDuration(_long.valueOf(arg0), arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def formatPeriodISO(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatPeriodISO(long,long)"""
        return str._wrap(_DurationFormatUtils.formatPeriodISO(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def formatDurationWords(arg0: int, arg1: bool, arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDurationWords(long,boolean,boolean)"""
        return str._wrap(_DurationFormatUtils.formatDurationWords(_long.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def formatPeriod(arg0: int, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatPeriod(long,long,java.lang.String)"""
        return str._wrap(_DurationFormatUtils.formatPeriod(_long.valueOf(arg0), _long.valueOf(arg1), arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.DurationFormatUtils()"""
        val = _DurationFormatUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def formatDurationHMS(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDurationHMS(long)"""
        return str._wrap(_DurationFormatUtils.formatDurationHMS(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def formatDurationISO(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatDurationISO(long)"""
        return str._wrap(_DurationFormatUtils.formatDurationISO(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def formatPeriod(arg0: int, arg1: int, arg2: str, arg3: bool, arg4: 'TimeZone') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DurationFormatUtils.formatPeriod(long,long,java.lang.String,boolean,java.util.TimeZone)"""
        return str._wrap(_DurationFormatUtils.formatPeriod(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _boolean.valueOf(arg3), arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.time.DateUtils
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.time.DateUtils as _DateUtils
_DateUtils = _DateUtils
import java.util.Calendar as Calendar
import java.lang.String as _String
_String = _String
import java.util.Date as Date
import java.util.Iterator as Iterator
import java.util.Calendar as _Calendar
_Calendar = _Calendar
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.util.TimeZone as TimeZone
import java.util.Date as _Date
_Date = _Date
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DateUtils():
    """org.apache.commons.lang3.time.DateUtils"""
 
    @staticmethod
    def _wrap(java_value: _DateUtils) -> 'DateUtils':
        return DateUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DateUtils):
        """
        Dynamic initializer for DateUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DateUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DateUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getFragmentInSeconds(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInSeconds(java.util.Date,int)"""
        return int._wrap(_DateUtils.getFragmentInSeconds(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInHours(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInHours(java.util.Calendar,int)"""
        return int._wrap(_DateUtils.getFragmentInHours(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def setSeconds(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setSeconds(java.util.Date,int)"""
        return Date._wrap(_DateUtils.setSeconds(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.DateUtils()"""
        val = _DateUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def truncate(arg0: object, arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.truncate(java.lang.Object,int)"""
        return Date._wrap(_DateUtils.truncate(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameDay(arg0: 'Calendar', arg1: 'Calendar') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameDay(java.util.Calendar,java.util.Calendar)"""
        return bool._wrap(_DateUtils.isSameDay(arg0, arg1))

    @staticmethod
    @overload
    def truncatedEquals(arg0: 'Date', arg1: 'Date', arg2: int) -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.truncatedEquals(java.util.Date,java.util.Date,int)"""
        return bool._wrap(_DateUtils.truncatedEquals(arg0, arg1, _int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getFragmentInMinutes(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInMinutes(java.util.Calendar,int)"""
        return int._wrap(_DateUtils.getFragmentInMinutes(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def addHours(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addHours(java.util.Date,int)"""
        return Date._wrap(_DateUtils.addHours(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def parseDateStrictly(arg0: str, *arg1: str) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.parseDateStrictly(java.lang.String,java.lang.String...) throws java.text.ParseException"""
        return Date._wrap(_DateUtils.parseDateStrictly(arg0, arg1))

    @staticmethod
    @overload
    def setMilliseconds(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setMilliseconds(java.util.Date,int)"""
        return Date._wrap(_DateUtils.setMilliseconds(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInDays(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInDays(java.util.Date,int)"""
        return int._wrap(_DateUtils.getFragmentInDays(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def truncate(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.truncate(java.util.Date,int)"""
        return Date._wrap(_DateUtils.truncate(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def addMinutes(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addMinutes(java.util.Date,int)"""
        return Date._wrap(_DateUtils.addMinutes(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def round(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.round(java.util.Date,int)"""
        return Date._wrap(_DateUtils.round(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def setMonths(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setMonths(java.util.Date,int)"""
        return Date._wrap(_DateUtils.setMonths(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInMilliseconds(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInMilliseconds(java.util.Date,int)"""
        return int._wrap(_DateUtils.getFragmentInMilliseconds(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def parseDate(arg0: str, arg1: 'Locale', *arg2: str) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.parseDate(java.lang.String,java.util.Locale,java.lang.String...) throws java.text.ParseException"""
        return Date._wrap(_DateUtils.parseDate(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def parseDate(arg0: str, *arg1: str) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.parseDate(java.lang.String,java.lang.String...) throws java.text.ParseException"""
        return Date._wrap(_DateUtils.parseDate(arg0, arg1))

    @staticmethod
    @overload
    def truncatedCompareTo(arg0: 'Date', arg1: 'Date', arg2: int) -> int:
        """public static int org.apache.commons.lang3.time.DateUtils.truncatedCompareTo(java.util.Date,java.util.Date,int)"""
        return int._wrap(_DateUtils.truncatedCompareTo(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def truncate(arg0: 'Calendar', arg1: int) -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.truncate(java.util.Calendar,int)"""
        return Calendar._wrap(_DateUtils.truncate(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getFragmentInMinutes(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInMinutes(java.util.Date,int)"""
        return int._wrap(_DateUtils.getFragmentInMinutes(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.DateUtils()"""
        val = _DateUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def ceiling(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.ceiling(java.util.Date,int)"""
        return Date._wrap(_DateUtils.ceiling(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def round(arg0: 'Calendar', arg1: int) -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.round(java.util.Calendar,int)"""
        return Calendar._wrap(_DateUtils.round(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def iterator(arg0: object, arg1: int) -> 'Iterator':
        """public static java.util.Iterator<?> org.apache.commons.lang3.time.DateUtils.iterator(java.lang.Object,int)"""
        return Iterator._wrap(_DateUtils.iterator(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def addYears(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addYears(java.util.Date,int)"""
        return Date._wrap(_DateUtils.addYears(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def truncatedEquals(arg0: 'Calendar', arg1: 'Calendar', arg2: int) -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.truncatedEquals(java.util.Calendar,java.util.Calendar,int)"""
        return bool._wrap(_DateUtils.truncatedEquals(arg0, arg1, _int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def setDays(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setDays(java.util.Date,int)"""
        return Date._wrap(_DateUtils.setDays(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def addWeeks(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addWeeks(java.util.Date,int)"""
        return Date._wrap(_DateUtils.addWeeks(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def parseDateStrictly(arg0: str, arg1: 'Locale', *arg2: str) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.parseDateStrictly(java.lang.String,java.util.Locale,java.lang.String...) throws java.text.ParseException"""
        return Date._wrap(_DateUtils.parseDateStrictly(arg0, arg1, arg2))

    @staticmethod
    @overload
    def setHours(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setHours(java.util.Date,int)"""
        return Date._wrap(_DateUtils.setHours(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameInstant(arg0: 'Calendar', arg1: 'Calendar') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameInstant(java.util.Calendar,java.util.Calendar)"""
        return bool._wrap(_DateUtils.isSameInstant(arg0, arg1))

    @staticmethod
    @overload
    def addMilliseconds(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addMilliseconds(java.util.Date,int)"""
        return Date._wrap(_DateUtils.addMilliseconds(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameLocalTime(arg0: 'Calendar', arg1: 'Calendar') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameLocalTime(java.util.Calendar,java.util.Calendar)"""
        return bool._wrap(_DateUtils.isSameLocalTime(arg0, arg1))

    @staticmethod
    @overload
    def isSameInstant(arg0: 'Date', arg1: 'Date') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameInstant(java.util.Date,java.util.Date)"""
        return bool._wrap(_DateUtils.isSameInstant(arg0, arg1))

    @staticmethod
    @overload
    def setMinutes(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setMinutes(java.util.Date,int)"""
        return Date._wrap(_DateUtils.setMinutes(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def truncatedCompareTo(arg0: 'Calendar', arg1: 'Calendar', arg2: int) -> int:
        """public static int org.apache.commons.lang3.time.DateUtils.truncatedCompareTo(java.util.Calendar,java.util.Calendar,int)"""
        return int._wrap(_DateUtils.truncatedCompareTo(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def toCalendar(arg0: 'Date', arg1: 'TimeZone') -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.toCalendar(java.util.Date,java.util.TimeZone)"""
        return Calendar._wrap(_DateUtils.toCalendar(arg0, arg1))

    @staticmethod
    @overload
    def getFragmentInMilliseconds(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInMilliseconds(java.util.Calendar,int)"""
        return int._wrap(_DateUtils.getFragmentInMilliseconds(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def iterator(arg0: 'Date', arg1: int) -> 'Iterator':
        """public static java.util.Iterator<java.util.Calendar> org.apache.commons.lang3.time.DateUtils.iterator(java.util.Date,int)"""
        return Iterator._wrap(_DateUtils.iterator(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getFragmentInDays(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInDays(java.util.Calendar,int)"""
        return int._wrap(_DateUtils.getFragmentInDays(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def toCalendar(arg0: 'Date') -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.toCalendar(java.util.Date)"""
        return Calendar._wrap(_DateUtils.toCalendar(arg0))

    @staticmethod
    @overload
    def getFragmentInHours(arg0: 'Date', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInHours(java.util.Date,int)"""
        return int._wrap(_DateUtils.getFragmentInHours(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ceiling(arg0: object, arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.ceiling(java.lang.Object,int)"""
        return Date._wrap(_DateUtils.ceiling(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def addMonths(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addMonths(java.util.Date,int)"""
        return Date._wrap(_DateUtils.addMonths(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def addSeconds(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addSeconds(java.util.Date,int)"""
        return Date._wrap(_DateUtils.addSeconds(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def getFragmentInSeconds(arg0: 'Calendar', arg1: int) -> int:
        """public static long org.apache.commons.lang3.time.DateUtils.getFragmentInSeconds(java.util.Calendar,int)"""
        return int._wrap(_DateUtils.getFragmentInSeconds(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def addDays(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.addDays(java.util.Date,int)"""
        return Date._wrap(_DateUtils.addDays(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameDay(arg0: 'Date', arg1: 'Date') -> bool:
        """public static boolean org.apache.commons.lang3.time.DateUtils.isSameDay(java.util.Date,java.util.Date)"""
        return bool._wrap(_DateUtils.isSameDay(arg0, arg1))

    @staticmethod
    @overload
    def round(arg0: object, arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.round(java.lang.Object,int)"""
        return Date._wrap(_DateUtils.round(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def iterator(arg0: 'Calendar', arg1: int) -> 'Iterator':
        """public static java.util.Iterator<java.util.Calendar> org.apache.commons.lang3.time.DateUtils.iterator(java.util.Calendar,int)"""
        return Iterator._wrap(_DateUtils.iterator(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ceiling(arg0: 'Calendar', arg1: int) -> 'Calendar':
        """public static java.util.Calendar org.apache.commons.lang3.time.DateUtils.ceiling(java.util.Calendar,int)"""
        return Calendar._wrap(_DateUtils.ceiling(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def setYears(arg0: 'Date', arg1: int) -> 'Date':
        """public static java.util.Date org.apache.commons.lang3.time.DateUtils.setYears(java.util.Date,int)"""
        return Date._wrap(_DateUtils.setYears(arg0, _int.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.lang3.time.DateFormatUtils
import java.util.Locale as Locale
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Calendar as Calendar
import java.lang.String as _String
_String = _String
import java.util.Date as Date
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.lang3.time.DateFormatUtils as _DateFormatUtils
_DateFormatUtils = _DateFormatUtils
import java.util.TimeZone as TimeZone
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DateFormatUtils():
    """org.apache.commons.lang3.time.DateFormatUtils"""
 
    @staticmethod
    def _wrap(java_value: _DateFormatUtils) -> 'DateFormatUtils':
        return DateFormatUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DateFormatUtils):
        """
        Dynamic initializer for DateFormatUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DateFormatUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DateFormatUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Date,java.lang.String,java.util.Locale)"""
        return str._wrap(_DateFormatUtils.format(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def formatUTC(arg0: 'Date', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.formatUTC(java.util.Date,java.lang.String)"""
        return str._wrap(_DateFormatUtils.formatUTC(arg0, arg1))

    @staticmethod
    @overload
    def formatUTC(arg0: 'Date', arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.formatUTC(java.util.Date,java.lang.String,java.util.Locale)"""
        return str._wrap(_DateFormatUtils.formatUTC(arg0, arg1, arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.DateFormatUtils()"""
        val = _DateFormatUtils()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Date,java.lang.String)"""
        return str._wrap(_DateFormatUtils.format(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: str, arg2: 'TimeZone') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Date,java.lang.String,java.util.TimeZone)"""
        return str._wrap(_DateFormatUtils.format(arg0, arg1, arg2))

    @staticmethod
    @overload
    def format(arg0: 'Calendar', arg1: str, arg2: 'TimeZone', arg3: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Calendar,java.lang.String,java.util.TimeZone,java.util.Locale)"""
        return str._wrap(_DateFormatUtils.format(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def format(arg0: int, arg1: str, arg2: 'TimeZone') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(long,java.lang.String,java.util.TimeZone)"""
        return str._wrap(_DateFormatUtils.format(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def format(arg0: int, arg1: str, arg2: 'TimeZone', arg3: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(long,java.lang.String,java.util.TimeZone,java.util.Locale)"""
        return str._wrap(_DateFormatUtils.format(_long.valueOf(arg0), arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def format(arg0: 'Calendar', arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Calendar,java.lang.String,java.util.Locale)"""
        return str._wrap(_DateFormatUtils.format(arg0, arg1, arg2))

    @staticmethod
    @overload
    def formatUTC(arg0: int, arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.formatUTC(long,java.lang.String,java.util.Locale)"""
        return str._wrap(_DateFormatUtils.formatUTC(_long.valueOf(arg0), arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def format(arg0: 'Date', arg1: str, arg2: 'TimeZone', arg3: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Date,java.lang.String,java.util.TimeZone,java.util.Locale)"""
        return str._wrap(_DateFormatUtils.format(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def format(arg0: 'Calendar', arg1: str, arg2: 'TimeZone') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Calendar,java.lang.String,java.util.TimeZone)"""
        return str._wrap(_DateFormatUtils.format(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.time.DateFormatUtils()"""
        val = _DateFormatUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def formatUTC(arg0: int, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.formatUTC(long,java.lang.String)"""
        return str._wrap(_DateFormatUtils.formatUTC(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def format(arg0: 'Calendar', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(java.util.Calendar,java.lang.String)"""
        return str._wrap(_DateFormatUtils.format(arg0, arg1))

    @staticmethod
    @overload
    def format(arg0: int, arg1: str, arg2: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(long,java.lang.String,java.util.Locale)"""
        return str._wrap(_DateFormatUtils.format(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def format(arg0: int, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.time.DateFormatUtils.format(long,java.lang.String)"""
        return str._wrap(_DateFormatUtils.format(_long.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.time.DateParser
import org.apache.commons.lang3.time.DateParser as _DateParser
_DateParser = _DateParser
import java.text.ParsePosition as ParsePosition
import java.util.Calendar as Calendar
from abc import abstractmethod, ABC
 
class DateParser():
    """org.apache.commons.lang3.time.DateParser"""
 
    @staticmethod
    def _wrap(java_value: _DateParser) -> 'DateParser':
        return DateParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DateParser):
        """
        Dynamic initializer for DateParser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DateParser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DateParser__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: org.apache.commons.lang3.time.FastDatePrinter
import java.text.FieldPosition as FieldPosition
from builtins import str
import java.util.Locale as Locale
import java.lang.StringBuffer as _StringBuffer
_StringBuffer = _StringBuffer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.lang.Appendable as _Appendable
_Appendable = _Appendable
import java.util.Calendar as Calendar
import java.lang.String as _String
_String = _String
import java.util.Date as Date
import java.lang.Appendable as Appendable
import java.lang.Integer as _int
import java.util.TimeZone as _TimeZone
_TimeZone = _TimeZone
import org.apache.commons.lang3.time.FastDatePrinter as _FastDatePrinter
_FastDatePrinter = _FastDatePrinter
from builtins import bool
import java.util.TimeZone as TimeZone
import java.lang.Long as _long
from builtins import int
import java.util.Locale as _Locale
_Locale = _Locale
import java.lang.Class as _Class
_Class = _Class
 
class FastDatePrinter():
    """org.apache.commons.lang3.time.FastDatePrinter"""
 
    @staticmethod
    def _wrap(java_value: _FastDatePrinter) -> 'FastDatePrinter':
        return FastDatePrinter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FastDatePrinter):
        """
        Dynamic initializer for FastDatePrinter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FastDatePrinter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FastDatePrinter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def format(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(long)"""
        return str._wrap(super(_FastDatePrinter, self).format(_long.valueOf(arg0)))

    @overload
    def format(self, arg0: 'Calendar') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar)"""
        return str._wrap(super(_FastDatePrinter, self).format(arg0))

    @overload
    def format(self, arg0: 'Calendar', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar,B)"""
        return 'Appendable'._wrap(super(_FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: 'Calendar', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Calendar,java.lang.StringBuffer)"""
        return 'StringBuffer'._wrap(super(_FastDatePrinter, self).format(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale org.apache.commons.lang3.time.FastDatePrinter.getLocale()"""
        return 'Locale'._wrap(super(FastDatePrinter, self).getLocale())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.getPattern()"""
        return str._wrap(super(FastDatePrinter, self).getPattern())

    @overload
    def format(self, arg0: 'Date', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date,java.lang.StringBuffer)"""
        return 'StringBuffer'._wrap(super(_FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: int, arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(long,B)"""
        return 'Appendable'._wrap(super(_FastDatePrinter, self).format(_long.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: 'Date') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date)"""
        return str._wrap(super(_FastDatePrinter, self).format(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDatePrinter.toString()"""
        return str._wrap(super(FastDatePrinter, self).toString())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.time.FastDatePrinter.hashCode()"""
        return int._wrap(super(FastDatePrinter, self).hashCode())

    @override
    @overload
    def getTimeZone(self) -> 'TimeZone':
        """public java.util.TimeZone org.apache.commons.lang3.time.FastDatePrinter.getTimeZone()"""
        return 'TimeZone'._wrap(super(FastDatePrinter, self).getTimeZone())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.time.FastDatePrinter.equals(java.lang.Object)"""
        return bool._wrap(super(_FastDatePrinter, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def format(self, arg0: int, arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(long,java.lang.StringBuffer)"""
        return 'StringBuffer'._wrap(super(_FastDatePrinter, self).format(_long.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: 'Date', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDatePrinter.format(java.util.Date,B)"""
        return 'Appendable'._wrap(super(_FastDatePrinter, self).format(arg0, arg1))

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDatePrinter.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'._wrap(super(_FastDatePrinter, self).format(arg0, arg1, arg2))

    @overload
    def getMaxLengthEstimate(self) -> int:
        """public int org.apache.commons.lang3.time.FastDatePrinter.getMaxLengthEstimate()"""
        return int._wrap(super(FastDatePrinter, self).getMaxLengthEstimate()) 
 
 
# CLASS: org.apache.commons.lang3.time.TimeZones
from builtins import str
import org.apache.commons.lang3.time.TimeZones as _TimeZones
_TimeZones = _TimeZones
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.TimeZone as _TimeZone
_TimeZone = _TimeZone
import java.util.TimeZone as TimeZone
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TimeZones():
    """org.apache.commons.lang3.time.TimeZones"""
 
    @staticmethod
    def _wrap(java_value: _TimeZones) -> 'TimeZones':
        return TimeZones(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimeZones):
        """
        Dynamic initializer for TimeZones.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimeZones__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimeZones__wrapper":
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
    def toTimeZone(arg0: 'TimeZone') -> 'TimeZone':
        """public static java.util.TimeZone org.apache.commons.lang3.time.TimeZones.toTimeZone(java.util.TimeZone)"""
        return TimeZone._wrap(_TimeZones.toTimeZone(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.time.FastDateParser
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.text.ParsePosition as ParsePosition
import org.apache.commons.lang3.time.FastDateParser as _FastDateParser
_FastDateParser = _FastDateParser
import java.util.Calendar as Calendar
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Date as Date
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.TimeZone as _TimeZone
_TimeZone = _TimeZone
from builtins import bool
import java.util.TimeZone as TimeZone
import java.util.Date as _Date
_Date = _Date
import java.lang.Long as _long
from builtins import int
import java.util.Locale as _Locale
_Locale = _Locale
import java.lang.Class as _Class
_Class = _Class
 
class FastDateParser():
    """org.apache.commons.lang3.time.FastDateParser"""
 
    @staticmethod
    def _wrap(java_value: _FastDateParser) -> 'FastDateParser':
        return FastDateParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FastDateParser):
        """
        Dynamic initializer for FastDateParser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FastDateParser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FastDateParser__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition', arg2: 'Calendar') -> bool:
        """public boolean org.apache.commons.lang3.time.FastDateParser.parse(java.lang.String,java.text.ParsePosition,java.util.Calendar)"""
        return bool._wrap(super(_FastDateParser, self).parse(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.time.FastDateParser.hashCode()"""
        return int._wrap(super(FastDateParser, self).hashCode())

    @overload
    def toStringAll(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateParser.toStringAll()"""
        return str._wrap(super(FastDateParser, self).toStringAll())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.time.FastDateParser.equals(java.lang.Object)"""
        return bool._wrap(super(_FastDateParser, self).equals(arg0))

    @override
    @overload
    def getPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateParser.getPattern()"""
        return str._wrap(super(FastDateParser, self).getPattern())

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
        """public java.lang.String org.apache.commons.lang3.time.FastDateParser.toString()"""
        return str._wrap(super(FastDateParser, self).toString())

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
    def getTimeZone(self) -> 'TimeZone':
        """public java.util.TimeZone org.apache.commons.lang3.time.FastDateParser.getTimeZone()"""
        return 'TimeZone'._wrap(super(FastDateParser, self).getTimeZone())

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale org.apache.commons.lang3.time.FastDateParser.getLocale()"""
        return 'Locale'._wrap(super(FastDateParser, self).getLocale())

    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition') -> 'Date':
        """public java.util.Date org.apache.commons.lang3.time.FastDateParser.parse(java.lang.String,java.text.ParsePosition)"""
        return 'Date'._wrap(super(_FastDateParser, self).parse(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def parseObject(self, arg0: str, arg1: 'ParsePosition') -> object:
        """public java.lang.Object org.apache.commons.lang3.time.FastDateParser.parseObject(java.lang.String,java.text.ParsePosition)"""
        return object._wrap(super(_FastDateParser, self).parseObject(arg0, arg1))

    @overload
    def parse(self, arg0: str) -> 'Date':
        """public java.util.Date org.apache.commons.lang3.time.FastDateParser.parse(java.lang.String) throws java.text.ParseException"""
        return 'Date'._wrap(super(_FastDateParser, self).parse(arg0))

    @overload
    def parseObject(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.time.FastDateParser.parseObject(java.lang.String) throws java.text.ParseException"""
        return object._wrap(super(_FastDateParser, self).parseObject(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.time.FastTimeZone
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.time.FastTimeZone as _FastTimeZone
_FastTimeZone = _FastTimeZone
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.TimeZone as _TimeZone
_TimeZone = _TimeZone
import java.util.TimeZone as TimeZone
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FastTimeZone():
    """org.apache.commons.lang3.time.FastTimeZone"""
 
    @staticmethod
    def _wrap(java_value: _FastTimeZone) -> 'FastTimeZone':
        return FastTimeZone(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FastTimeZone):
        """
        Dynamic initializer for FastTimeZone.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FastTimeZone__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FastTimeZone__wrapper":
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
    def getGmtTimeZone(arg0: str) -> 'TimeZone':
        """public static java.util.TimeZone org.apache.commons.lang3.time.FastTimeZone.getGmtTimeZone(java.lang.String)"""
        return TimeZone._wrap(_FastTimeZone.getGmtTimeZone(arg0))

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
    def getGmtTimeZone() -> 'TimeZone':
        """public static java.util.TimeZone org.apache.commons.lang3.time.FastTimeZone.getGmtTimeZone()"""
        return TimeZone._wrap(_FastTimeZone.getGmtTimeZone())

    @staticmethod
    @overload
    def getTimeZone(arg0: str) -> 'TimeZone':
        """public static java.util.TimeZone org.apache.commons.lang3.time.FastTimeZone.getTimeZone(java.lang.String)"""
        return TimeZone._wrap(_FastTimeZone.getTimeZone(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.time.FastDateFormat
import org.apache.commons.lang3.time.FastDateFormat as _FastDateFormat
_FastDateFormat = _FastDateFormat
import java.text.FieldPosition as FieldPosition
import java.util.Locale as Locale
import java.lang.StringBuffer as _StringBuffer
_StringBuffer = _StringBuffer
import java.lang.Object as _Object
_Object = _Object
import java.text.AttributedCharacterIterator as AttributedCharacterIterator
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.text.ParsePosition as ParsePosition
import java.text.AttributedCharacterIterator as _AttributedCharacterIterator
_AttributedCharacterIterator = _AttributedCharacterIterator
import java.lang.String as _string
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.text.Format as _Format
_Format = _Format
import java.lang.Object as _object
import java.lang.Appendable as _Appendable
_Appendable = _Appendable
import java.util.Calendar as Calendar
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Date as Date
import java.lang.Appendable as Appendable
import java.lang.Integer as _int
import java.util.TimeZone as _TimeZone
_TimeZone = _TimeZone
import java.util.TimeZone as TimeZone
import java.lang.Long as _long
import java.util.Date as _Date
_Date = _Date
from builtins import int
import java.util.Locale as _Locale
_Locale = _Locale
import java.lang.Class as _Class
_Class = _Class
 
class FastDateFormat():
    """org.apache.commons.lang3.time.FastDateFormat"""
 
    @staticmethod
    def _wrap(java_value: _FastDateFormat) -> 'FastDateFormat':
        return FastDateFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FastDateFormat):
        """
        Dynamic initializer for FastDateFormat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FastDateFormat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FastDateFormat__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.time.FastDateFormat.hashCode()"""
        return int._wrap(super(FastDateFormat, self).hashCode())

    @staticmethod
    @overload
    def getDateTimeInstance(arg0: int, arg1: int) -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateTimeInstance(int,int)"""
        return FastDateFormat._wrap(_FastDateFormat.getDateTimeInstance(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def parseObject(self, arg0: str) -> object:
        """public java.lang.Object java.text.Format.parseObject(java.lang.String) throws java.text.ParseException"""
        return object._wrap(super(_Format, self).parseObject(arg0))

    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition', arg2: 'Calendar') -> bool:
        """public boolean org.apache.commons.lang3.time.FastDateFormat.parse(java.lang.String,java.text.ParsePosition,java.util.Calendar)"""
        return bool._wrap(super(_FastDateFormat, self).parse(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getTimeInstance(arg0: int, arg1: 'TimeZone', arg2: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getTimeInstance(int,java.util.TimeZone,java.util.Locale)"""
        return FastDateFormat._wrap(_FastDateFormat.getTimeInstance(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def getDateInstance(arg0: int, arg1: 'TimeZone') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateInstance(int,java.util.TimeZone)"""
        return FastDateFormat._wrap(_FastDateFormat.getDateInstance(_int.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: int, arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDateFormat.format(long,B)"""
        return 'Appendable'._wrap(super(_FastDateFormat, self).format(_long.valueOf(arg0), arg1))

    @overload
    def parseObject(self, arg0: str, arg1: 'ParsePosition') -> object:
        """public java.lang.Object org.apache.commons.lang3.time.FastDateFormat.parseObject(java.lang.String,java.text.ParsePosition)"""
        return object._wrap(super(_FastDateFormat, self).parseObject(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def format(self, arg0: 'Date') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.format(java.util.Date)"""
        return str._wrap(super(_FastDateFormat, self).format(arg0))

    @staticmethod
    @overload
    def getInstance(arg0: str) -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance(java.lang.String)"""
        return FastDateFormat._wrap(_FastDateFormat.getInstance(arg0))

    @overload
    def format(self, arg0: 'Calendar') -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.format(java.util.Calendar)"""
        return str._wrap(super(_FastDateFormat, self).format(arg0))

    @staticmethod
    @overload
    def getDateTimeInstance(arg0: int, arg1: int, arg2: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateTimeInstance(int,int,java.util.Locale)"""
        return FastDateFormat._wrap(_FastDateFormat.getDateTimeInstance(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def parse(self, arg0: str, arg1: 'ParsePosition') -> 'Date':
        """public java.util.Date org.apache.commons.lang3.time.FastDateFormat.parse(java.lang.String,java.text.ParsePosition)"""
        return 'Date'._wrap(super(_FastDateFormat, self).parse(arg0, arg1))

    @overload
    def format(self, arg0: int) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.format(long)"""
        return str._wrap(super(_FastDateFormat, self).format(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def getTimeInstance(arg0: int) -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getTimeInstance(int)"""
        return FastDateFormat._wrap(_FastDateFormat.getTimeInstance(_int.valueOf(arg0)))

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale org.apache.commons.lang3.time.FastDateFormat.getLocale()"""
        return 'Locale'._wrap(super(FastDateFormat, self).getLocale())

    @staticmethod
    @overload
    def getDateInstance(arg0: int, arg1: 'TimeZone', arg2: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateInstance(int,java.util.TimeZone,java.util.Locale)"""
        return FastDateFormat._wrap(_FastDateFormat.getDateInstance(_int.valueOf(arg0), arg1, arg2))

    @overload
    def formatToCharacterIterator(self, arg0: object) -> 'AttributedCharacterIterator':
        """public java.text.AttributedCharacterIterator java.text.Format.formatToCharacterIterator(java.lang.Object)"""
        return 'AttributedCharacterIterator'._wrap(super(_Format, self).formatToCharacterIterator(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getInstance() -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance()"""
        return FastDateFormat._wrap(_FastDateFormat.getInstance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def format(self, arg0: 'Calendar', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDateFormat.format(java.util.Calendar,B)"""
        return 'Appendable'._wrap(super(_FastDateFormat, self).format(arg0, arg1))

    @staticmethod
    @overload
    def getTimeInstance(arg0: int, arg1: 'TimeZone') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getTimeInstance(int,java.util.TimeZone)"""
        return FastDateFormat._wrap(_FastDateFormat.getTimeInstance(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def getDateInstance(arg0: int) -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateInstance(int)"""
        return FastDateFormat._wrap(_FastDateFormat.getDateInstance(_int.valueOf(arg0)))

    @override
    @overload
    def getPattern(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.getPattern()"""
        return str._wrap(super(FastDateFormat, self).getPattern())

    @overload
    def format(self, arg0: object, arg1: 'StringBuffer', arg2: 'FieldPosition') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDateFormat.format(java.lang.Object,java.lang.StringBuffer,java.text.FieldPosition)"""
        return 'StringBuffer'._wrap(super(_FastDateFormat, self).format(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getDateInstance(arg0: int, arg1: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateInstance(int,java.util.Locale)"""
        return FastDateFormat._wrap(_FastDateFormat.getDateInstance(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def getInstance(arg0: str, arg1: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance(java.lang.String,java.util.Locale)"""
        return FastDateFormat._wrap(_FastDateFormat.getInstance(arg0, arg1))

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.text.Format.clone()"""
        return object._wrap(super(Format, self).clone())

    @overload
    def format(self, arg0: 'Date', arg1: 'Appendable') -> 'Appendable':
        """public <B extends java.lang.Appendable> B org.apache.commons.lang3.time.FastDateFormat.format(java.util.Date,B)"""
        return 'Appendable'._wrap(super(_FastDateFormat, self).format(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getInstance(arg0: str, arg1: 'TimeZone', arg2: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance(java.lang.String,java.util.TimeZone,java.util.Locale)"""
        return FastDateFormat._wrap(_FastDateFormat.getInstance(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getTimeInstance(arg0: int, arg1: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getTimeInstance(int,java.util.Locale)"""
        return FastDateFormat._wrap(_FastDateFormat.getTimeInstance(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.time.FastDateFormat.toString()"""
        return str._wrap(super(FastDateFormat, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.time.FastDateFormat.equals(java.lang.Object)"""
        return bool._wrap(super(_FastDateFormat, self).equals(arg0))

    @staticmethod
    @overload
    def getDateTimeInstance(arg0: int, arg1: int, arg2: 'TimeZone', arg3: 'Locale') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateTimeInstance(int,int,java.util.TimeZone,java.util.Locale)"""
        return FastDateFormat._wrap(_FastDateFormat.getDateTimeInstance(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @overload
    def format(self, arg0: int, arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDateFormat.format(long,java.lang.StringBuffer)"""
        return 'StringBuffer'._wrap(super(_FastDateFormat, self).format(_long.valueOf(arg0), arg1))

    @overload
    def format(self, arg0: object) -> str:
        """public final java.lang.String java.text.Format.format(java.lang.Object)"""
        return str._wrap(super(_Format, self).format(arg0))

    @overload
    def format(self, arg0: 'Date', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDateFormat.format(java.util.Date,java.lang.StringBuffer)"""
        return 'StringBuffer'._wrap(super(_FastDateFormat, self).format(arg0, arg1))

    @staticmethod
    @overload
    def getDateTimeInstance(arg0: int, arg1: int, arg2: 'TimeZone') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getDateTimeInstance(int,int,java.util.TimeZone)"""
        return FastDateFormat._wrap(_FastDateFormat.getDateTimeInstance(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def getTimeZone(self) -> 'TimeZone':
        """public java.util.TimeZone org.apache.commons.lang3.time.FastDateFormat.getTimeZone()"""
        return 'TimeZone'._wrap(super(FastDateFormat, self).getTimeZone())

    @overload
    def format(self, arg0: 'Calendar', arg1: 'StringBuffer') -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.time.FastDateFormat.format(java.util.Calendar,java.lang.StringBuffer)"""
        return 'StringBuffer'._wrap(super(_FastDateFormat, self).format(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getMaxLengthEstimate(self) -> int:
        """public int org.apache.commons.lang3.time.FastDateFormat.getMaxLengthEstimate()"""
        return int._wrap(super(FastDateFormat, self).getMaxLengthEstimate())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getInstance(arg0: str, arg1: 'TimeZone') -> 'FastDateFormat':
        """public static org.apache.commons.lang3.time.FastDateFormat org.apache.commons.lang3.time.FastDateFormat.getInstance(java.lang.String,java.util.TimeZone)"""
        return FastDateFormat._wrap(_FastDateFormat.getInstance(arg0, arg1))

    @overload
    def parse(self, arg0: str) -> 'Date':
        """public java.util.Date org.apache.commons.lang3.time.FastDateFormat.parse(java.lang.String) throws java.text.ParseException"""
        return 'Date'._wrap(super(_FastDateFormat, self).parse(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.time.DurationUtils
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.time.temporal.Temporal as Temporal
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import java.time.Duration as _Duration
_Duration = _Duration
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

import org.apache.commons.lang3.time.DurationUtils as _DurationUtils
_DurationUtils = _DurationUtils
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DurationUtils():
    """org.apache.commons.lang3.time.DurationUtils"""
 
    @staticmethod
    def _wrap(java_value: _DurationUtils) -> 'DurationUtils':
        return DurationUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DurationUtils):
        """
        Dynamic initializer for DurationUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DurationUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DurationUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.commons.lang3.time.DurationUtils()"""
        val = _DurationUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getNanosOfMiili(arg0: 'Duration') -> int:
        """public static int org.apache.commons.lang3.time.DurationUtils.getNanosOfMiili(java.time.Duration)"""
        return int._wrap(_DurationUtils.getNanosOfMiili(arg0))

    @staticmethod
    @overload
    def toDuration(arg0: int, arg1: 'TimeUnit') -> 'Duration':
        """public static java.time.Duration org.apache.commons.lang3.time.DurationUtils.toDuration(long,java.util.concurrent.TimeUnit)"""
        return Duration._wrap(_DurationUtils.toDuration(_long.valueOf(arg0), arg1))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.time.DurationUtils()"""
        val = _DurationUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getNanosOfMilli(arg0: 'Duration') -> int:
        """public static int org.apache.commons.lang3.time.DurationUtils.getNanosOfMilli(java.time.Duration)"""
        return int._wrap(_DurationUtils.getNanosOfMilli(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def accept(arg0: 'FailableBiConsumer', arg1: 'Duration'):
        """public static <T extends java.lang.Throwable> void org.apache.commons.lang3.time.DurationUtils.accept(org.apache.commons.lang3.function.FailableBiConsumer<java.lang.Long, java.lang.Integer, T>,java.time.Duration) throws T"""
        _DurationUtils.accept(arg0, arg1)

    @staticmethod
    @overload
    def toMillisInt(arg0: 'Duration') -> int:
        """public static int org.apache.commons.lang3.time.DurationUtils.toMillisInt(java.time.Duration)"""
        return int._wrap(_DurationUtils.toMillisInt(arg0))

    @staticmethod
    @overload
    def of(arg0: 'FailableConsumer') -> 'Duration':
        """public static <E extends java.lang.Throwable> java.time.Duration org.apache.commons.lang3.time.DurationUtils.of(org.apache.commons.lang3.function.FailableConsumer<java.time.Instant, E>) throws E"""
        return Duration._wrap(_DurationUtils.of(arg0))

    @staticmethod
    @overload
    def since(arg0: 'Temporal') -> 'Duration':
        """public static java.time.Duration org.apache.commons.lang3.time.DurationUtils.since(java.time.temporal.Temporal)"""
        return Duration._wrap(_DurationUtils.since(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: 'FailableRunnable') -> 'Duration':
        """public static <E extends java.lang.Throwable> java.time.Duration org.apache.commons.lang3.time.DurationUtils.of(org.apache.commons.lang3.function.FailableRunnable<E>) throws E"""
        return Duration._wrap(_DurationUtils.of(arg0))

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
    def isPositive(arg0: 'Duration') -> bool:
        """public static boolean org.apache.commons.lang3.time.DurationUtils.isPositive(java.time.Duration)"""
        return bool._wrap(_DurationUtils.isPositive(arg0))

    @staticmethod
    @overload
    def zeroIfNull(arg0: 'Duration') -> 'Duration':
        """public static java.time.Duration org.apache.commons.lang3.time.DurationUtils.zeroIfNull(java.time.Duration)"""
        return Duration._wrap(_DurationUtils.zeroIfNull(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())