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
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger as _Slf4jLogger
_Slf4jLogger = _Slf4jLogger
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
 
class Slf4jLogger():
    """dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger"""
 
    @staticmethod
    def _wrap(java_value: _Slf4jLogger) -> 'Slf4jLogger':
        return Slf4jLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Slf4jLogger):
        """
        Dynamic initializer for Slf4jLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Slf4jLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Slf4jLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_Slf4jLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_Slf4jLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_Slf4jLogger, self).debug(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_Slf4jLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String)"""
        super(_Slf4jLogger, self).debug(arg0)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object)"""
        super(_Slf4jLogger, self).warn(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object)"""
        super(_Slf4jLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String)"""
        super(_Slf4jLogger, self).error(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_Slf4jLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_Slf4jLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object)"""
        super(_Slf4jLogger, self).info(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_Slf4jLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_Slf4jLogger, self).debug(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_Slf4jLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String)"""
        super(_Slf4jLogger, self).info(arg0)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_Slf4jLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_Slf4jLogger, self).warn(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def warn(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String)"""
        super(_Slf4jLogger, self).warn(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Logger'):
        """public dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger(org.slf4j.Logger)"""
        val = _Slf4jLogger(arg0)
        self.__wrapper = val

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_Slf4jLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object)"""
        super(_Slf4jLogger, self).debug(arg0, arg1)

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

 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger as _Slf4jLogger
_Slf4jLogger = _Slf4jLogger
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
 
class Slf4jLogger():
    """dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger"""
 
    @staticmethod
    def _wrap(java_value: _Slf4jLogger) -> 'Slf4jLogger':
        return Slf4jLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Slf4jLogger):
        """
        Dynamic initializer for Slf4jLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Slf4jLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Slf4jLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_Slf4jLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_Slf4jLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_Slf4jLogger, self).debug(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_Slf4jLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String)"""
        super(_Slf4jLogger, self).debug(arg0)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object)"""
        super(_Slf4jLogger, self).warn(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object)"""
        super(_Slf4jLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String)"""
        super(_Slf4jLogger, self).error(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_Slf4jLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_Slf4jLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object)"""
        super(_Slf4jLogger, self).info(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_Slf4jLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_Slf4jLogger, self).debug(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_Slf4jLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String)"""
        super(_Slf4jLogger, self).info(arg0)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(_Slf4jLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_Slf4jLogger, self).warn(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def warn(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String)"""
        super(_Slf4jLogger, self).warn(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Logger'):
        """public dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger(org.slf4j.Logger)"""
        val = _Slf4jLogger(arg0)
        self.__wrapper = val

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_Slf4jLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object)"""
        super(_Slf4jLogger, self).debug(arg0, arg1)

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

 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger