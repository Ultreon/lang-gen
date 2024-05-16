from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_ReadWriteLockVisitor
_ReadWriteLockVisitor = _LockingVisitors_ReadWriteLockVisitor.ReadWriteLockVisitor
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

from builtins import bool
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_LockVisitor
_LockVisitor = _LockingVisitors_LockVisitor.LockVisitor
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReadWriteLockVisitor():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors.ReadWriteLockVisitor"""
 
    @staticmethod
    def _wrap(java_value: _ReadWriteLockVisitor) -> 'ReadWriteLockVisitor':
        return ReadWriteLockVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReadWriteLockVisitor):
        """
        Dynamic initializer for ReadWriteLockVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReadWriteLockVisitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReadWriteLockVisitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLock(self) -> object:
        """public L org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getLock()"""
        return object._wrap(super(LockVisitor, self).getLock())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getObject(self) -> object:
        """public O org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getObject()"""
        return object._wrap(super(LockVisitor, self).getObject())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def acceptWriteLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptWriteLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(_LockVisitor, self).acceptWriteLocked(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def applyWriteLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyWriteLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object._wrap(super(_LockVisitor, self).applyWriteLocked(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def applyReadLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyReadLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object._wrap(super(_LockVisitor, self).applyReadLocked(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def acceptReadLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptReadLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(_LockVisitor, self).acceptReadLocked(arg0)

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

 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors$ReadWriteLockVisitor
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_ReadWriteLockVisitor
_ReadWriteLockVisitor = _LockingVisitors_ReadWriteLockVisitor.ReadWriteLockVisitor
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

from builtins import bool
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_LockVisitor
_LockVisitor = _LockingVisitors_LockVisitor.LockVisitor
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReadWriteLockVisitor():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors.ReadWriteLockVisitor"""
 
    @staticmethod
    def _wrap(java_value: _ReadWriteLockVisitor) -> 'ReadWriteLockVisitor':
        return ReadWriteLockVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReadWriteLockVisitor):
        """
        Dynamic initializer for ReadWriteLockVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReadWriteLockVisitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReadWriteLockVisitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLock(self) -> object:
        """public L org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getLock()"""
        return object._wrap(super(LockVisitor, self).getLock())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getObject(self) -> object:
        """public O org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getObject()"""
        return object._wrap(super(LockVisitor, self).getObject())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def acceptWriteLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptWriteLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(_LockVisitor, self).acceptWriteLocked(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def applyWriteLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyWriteLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object._wrap(super(_LockVisitor, self).applyWriteLocked(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def applyReadLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyReadLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object._wrap(super(_LockVisitor, self).applyReadLocked(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def acceptReadLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptReadLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(_LockVisitor, self).acceptReadLocked(arg0)

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

 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors$ReadWriteLockVisitor 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_ReadWriteLockVisitor
_ReadWriteLockVisitor = _LockingVisitors_ReadWriteLockVisitor.ReadWriteLockVisitor
import java.lang.Object as _Object
_Object = _Object
import java.util.concurrent.locks.ReadWriteLock as ReadWriteLock
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_StampedLockVisitor
_StampedLockVisitor = _LockingVisitors_StampedLockVisitor.StampedLockVisitor
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors
_LockingVisitors = _LockingVisitors
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LockingVisitors():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors"""
 
    @staticmethod
    def _wrap(java_value: _LockingVisitors) -> 'LockingVisitors':
        return LockingVisitors(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LockingVisitors):
        """
        Dynamic initializer for LockingVisitors.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LockingVisitors__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LockingVisitors__wrapper":
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
    def stampedLockVisitor(arg0: object) -> 'StampedLockVisitor':
        """public static <O> org.apache.commons.lang3.concurrent.locks.LockingVisitors$StampedLockVisitor<O> org.apache.commons.lang3.concurrent.locks.LockingVisitors.stampedLockVisitor(O)"""
        return StampedLockVisitor._wrap(_LockingVisitors.stampedLockVisitor(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: object, arg1: 'ReadWriteLock') -> 'ReadWriteLockVisitor':
        """public static <O> org.apache.commons.lang3.concurrent.locks.LockingVisitors$ReadWriteLockVisitor<O> org.apache.commons.lang3.concurrent.locks.LockingVisitors.create(O,java.util.concurrent.locks.ReadWriteLock)"""
        return ReadWriteLockVisitor._wrap(_LockingVisitors.create(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def reentrantReadWriteLockVisitor(arg0: object) -> 'ReadWriteLockVisitor':
        """public static <O> org.apache.commons.lang3.concurrent.locks.LockingVisitors$ReadWriteLockVisitor<O> org.apache.commons.lang3.concurrent.locks.LockingVisitors.reentrantReadWriteLockVisitor(O)"""
        return ReadWriteLockVisitor._wrap(_LockingVisitors.reentrantReadWriteLockVisitor(arg0))

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
        """public org.apache.commons.lang3.concurrent.locks.LockingVisitors()"""
        val = _LockingVisitors()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.locks.LockingVisitors()"""
        val = _LockingVisitors()
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
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

from builtins import bool
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_LockVisitor
_LockVisitor = _LockingVisitors_LockVisitor.LockVisitor
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LockVisitor():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors.LockVisitor"""
 
    @staticmethod
    def _wrap(java_value: _LockVisitor) -> 'LockVisitor':
        return LockVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LockVisitor):
        """
        Dynamic initializer for LockVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LockVisitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LockVisitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def acceptWriteLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptWriteLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(_LockVisitor, self).acceptWriteLocked(arg0)

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
    def applyWriteLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyWriteLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object._wrap(super(_LockVisitor, self).applyWriteLocked(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def acceptReadLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptReadLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(_LockVisitor, self).acceptReadLocked(arg0)

    @overload
    def applyReadLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyReadLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object._wrap(super(_LockVisitor, self).applyReadLocked(arg0))

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
    def getObject(self) -> object:
        """public O org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getObject()"""
        return object._wrap(super(LockVisitor, self).getObject())

    @overload
    def getLock(self) -> object:
        """public L org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getLock()"""
        return object._wrap(super(LockVisitor, self).getLock())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors$StampedLockVisitor
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_StampedLockVisitor
_StampedLockVisitor = _LockingVisitors_StampedLockVisitor.StampedLockVisitor
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

from builtins import bool
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as _LockingVisitors_LockVisitor
_LockVisitor = _LockingVisitors_LockVisitor.LockVisitor
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StampedLockVisitor():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors.StampedLockVisitor"""
 
    @staticmethod
    def _wrap(java_value: _StampedLockVisitor) -> 'StampedLockVisitor':
        return StampedLockVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StampedLockVisitor):
        """
        Dynamic initializer for StampedLockVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StampedLockVisitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StampedLockVisitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLock(self) -> object:
        """public L org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getLock()"""
        return object._wrap(super(LockVisitor, self).getLock())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getObject(self) -> object:
        """public O org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getObject()"""
        return object._wrap(super(LockVisitor, self).getObject())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def acceptWriteLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptWriteLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(_LockVisitor, self).acceptWriteLocked(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def applyWriteLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyWriteLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object._wrap(super(_LockVisitor, self).applyWriteLocked(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def applyReadLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyReadLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object._wrap(super(_LockVisitor, self).applyReadLocked(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def acceptReadLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptReadLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(_LockVisitor, self).acceptReadLocked(arg0)

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