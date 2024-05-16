from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger as __Slf4jLogger
__Slf4jLogger = __Slf4jLogger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Slf4jLogger():
    """dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger"""
 
    @staticmethod
    def __wrap(java_value: __Slf4jLogger) -> 'Slf4jLogger':
        return Slf4jLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Slf4jLogger):
        """
        Dynamic initializer for Slf4jLogger.
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
    def warn(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String)"""
        super(__Slf4jLogger, self).warn(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__Slf4jLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__Slf4jLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__Slf4jLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__Slf4jLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object)"""
        super(__Slf4jLogger, self).debug(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def info(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String)"""
        super(__Slf4jLogger, self).info(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__Slf4jLogger, self).info(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__Slf4jLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__Slf4jLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__Slf4jLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__Slf4jLogger, self).warn(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__Slf4jLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String)"""
        super(__Slf4jLogger, self).error(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__Slf4jLogger, self).error(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object)"""
        super(__Slf4jLogger, self).info(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object)"""
        super(__Slf4jLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__Slf4jLogger, self).debug(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'Logger'):
        """public dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger(org.slf4j.Logger)"""
        val = __Slf4jLogger(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object)"""
        super(__Slf4jLogger, self).error(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def debug(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String)"""
        super(__Slf4jLogger, self).debug(arg0)

 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger as __Slf4jLogger
__Slf4jLogger = __Slf4jLogger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Slf4jLogger():
    """dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger"""
 
    @staticmethod
    def __wrap(java_value: __Slf4jLogger) -> 'Slf4jLogger':
        return Slf4jLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Slf4jLogger):
        """
        Dynamic initializer for Slf4jLogger.
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
    def warn(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String)"""
        super(__Slf4jLogger, self).warn(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__Slf4jLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__Slf4jLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__Slf4jLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__Slf4jLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object)"""
        super(__Slf4jLogger, self).debug(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def info(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String)"""
        super(__Slf4jLogger, self).info(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__Slf4jLogger, self).info(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__Slf4jLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        super(__Slf4jLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__Slf4jLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__Slf4jLogger, self).warn(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__Slf4jLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String)"""
        super(__Slf4jLogger, self).error(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__Slf4jLogger, self).error(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.info(java.lang.String,java.lang.Object)"""
        super(__Slf4jLogger, self).info(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.warn(java.lang.String,java.lang.Object)"""
        super(__Slf4jLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__Slf4jLogger, self).debug(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'Logger'):
        """public dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger(org.slf4j.Logger)"""
        val = __Slf4jLogger(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.error(java.lang.String,java.lang.Object)"""
        super(__Slf4jLogger, self).error(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def debug(self, arg0: str):
        """public void dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger.debug(java.lang.String)"""
        super(__Slf4jLogger, self).debug(arg0)

 
 
 
# CLASS: dev.ultreon.quantum.desktop.DesktopLogger.Slf4jLogger