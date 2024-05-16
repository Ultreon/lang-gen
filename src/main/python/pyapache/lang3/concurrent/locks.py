from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_StampedLockVisitor
__StampedLockVisitor = __LockingVisitors_StampedLockVisitor.StampedLockVisitor
from builtins import object
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_LockVisitor
__LockVisitor = __LockingVisitors_LockVisitor.LockVisitor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StampedLockVisitor():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors.StampedLockVisitor"""
 
    @staticmethod
    def __wrap(java_value: __StampedLockVisitor) -> 'StampedLockVisitor':
        return StampedLockVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StampedLockVisitor):
        """
        Dynamic initializer for StampedLockVisitor.
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
    def applyReadLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyReadLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object.__wrap(super(__LockVisitor, self).applyReadLocked(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def acceptWriteLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptWriteLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(__LockVisitor, self).acceptWriteLocked(arg0)

    @override
    @overload
    def getLock(self) -> object:
        """public L org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getLock()"""
        return object.__wrap(super(LockVisitor, self).getLock())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getObject(self) -> object:
        """public O org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getObject()"""
        return object.__wrap(super(LockVisitor, self).getObject())

    @override
    @overload
    def acceptReadLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptReadLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(__LockVisitor, self).acceptReadLocked(arg0)

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
    def applyWriteLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyWriteLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object.__wrap(super(__LockVisitor, self).applyWriteLocked(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors$StampedLockVisitor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_StampedLockVisitor
__StampedLockVisitor = __LockingVisitors_StampedLockVisitor.StampedLockVisitor
from builtins import object
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_LockVisitor
__LockVisitor = __LockingVisitors_LockVisitor.LockVisitor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StampedLockVisitor():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors.StampedLockVisitor"""
 
    @staticmethod
    def __wrap(java_value: __StampedLockVisitor) -> 'StampedLockVisitor':
        return StampedLockVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StampedLockVisitor):
        """
        Dynamic initializer for StampedLockVisitor.
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
    def applyReadLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyReadLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object.__wrap(super(__LockVisitor, self).applyReadLocked(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def acceptWriteLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptWriteLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(__LockVisitor, self).acceptWriteLocked(arg0)

    @override
    @overload
    def getLock(self) -> object:
        """public L org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getLock()"""
        return object.__wrap(super(LockVisitor, self).getLock())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getObject(self) -> object:
        """public O org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getObject()"""
        return object.__wrap(super(LockVisitor, self).getObject())

    @override
    @overload
    def acceptReadLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptReadLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(__LockVisitor, self).acceptReadLocked(arg0)

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
    def applyWriteLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyWriteLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object.__wrap(super(__LockVisitor, self).applyWriteLocked(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors$StampedLockVisitor 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors$ReadWriteLockVisitor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_LockVisitor
__LockVisitor = __LockingVisitors_LockVisitor.LockVisitor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_ReadWriteLockVisitor
__ReadWriteLockVisitor = __LockingVisitors_ReadWriteLockVisitor.ReadWriteLockVisitor
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ReadWriteLockVisitor():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors.ReadWriteLockVisitor"""
 
    @staticmethod
    def __wrap(java_value: __ReadWriteLockVisitor) -> 'ReadWriteLockVisitor':
        return ReadWriteLockVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReadWriteLockVisitor):
        """
        Dynamic initializer for ReadWriteLockVisitor.
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
    def applyReadLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyReadLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object.__wrap(super(__LockVisitor, self).applyReadLocked(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def acceptWriteLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptWriteLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(__LockVisitor, self).acceptWriteLocked(arg0)

    @override
    @overload
    def getLock(self) -> object:
        """public L org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getLock()"""
        return object.__wrap(super(LockVisitor, self).getLock())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getObject(self) -> object:
        """public O org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getObject()"""
        return object.__wrap(super(LockVisitor, self).getObject())

    @override
    @overload
    def acceptReadLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptReadLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(__LockVisitor, self).acceptReadLocked(arg0)

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
    def applyWriteLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyWriteLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object.__wrap(super(__LockVisitor, self).applyWriteLocked(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.concurrent.locks.ReadWriteLock as ReadWriteLock
from builtins import type
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_StampedLockVisitor
__StampedLockVisitor = __LockingVisitors_StampedLockVisitor.StampedLockVisitor
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors
__LockingVisitors = __LockingVisitors
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_ReadWriteLockVisitor
__ReadWriteLockVisitor = __LockingVisitors_ReadWriteLockVisitor.ReadWriteLockVisitor
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LockingVisitors():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors"""
 
    @staticmethod
    def __wrap(java_value: __LockingVisitors) -> 'LockingVisitors':
        return LockingVisitors(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LockingVisitors):
        """
        Dynamic initializer for LockingVisitors.
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
    def create(arg0: object, arg1: 'ReadWriteLock') -> 'ReadWriteLockVisitor':
        """public static <O> org.apache.commons.lang3.concurrent.locks.LockingVisitors$ReadWriteLockVisitor<O> org.apache.commons.lang3.concurrent.locks.LockingVisitors.create(O,java.util.concurrent.locks.ReadWriteLock)"""
        return ReadWriteLockVisitor.__wrap(__LockingVisitors.create(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.locks.LockingVisitors()"""
        val = __LockingVisitors()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def reentrantReadWriteLockVisitor(arg0: object) -> 'ReadWriteLockVisitor':
        """public static <O> org.apache.commons.lang3.concurrent.locks.LockingVisitors$ReadWriteLockVisitor<O> org.apache.commons.lang3.concurrent.locks.LockingVisitors.reentrantReadWriteLockVisitor(O)"""
        return ReadWriteLockVisitor.__wrap(__LockingVisitors.reentrantReadWriteLockVisitor(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stampedLockVisitor(arg0: object) -> 'StampedLockVisitor':
        """public static <O> org.apache.commons.lang3.concurrent.locks.LockingVisitors$StampedLockVisitor<O> org.apache.commons.lang3.concurrent.locks.LockingVisitors.stampedLockVisitor(O)"""
        return StampedLockVisitor.__wrap(__LockingVisitors.stampedLockVisitor(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.locks.LockingVisitors()"""
        val = __LockingVisitors()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.locks.LockingVisitors as __LockingVisitors_LockVisitor
__LockVisitor = __LockingVisitors_LockVisitor.LockVisitor
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyapache.lang3 import function
except ImportError:
    function = __import_once__("pyapache.lang3.function")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LockVisitor():
    """org.apache.commons.lang3.concurrent.locks.LockingVisitors.LockVisitor"""
 
    @staticmethod
    def __wrap(java_value: __LockVisitor) -> 'LockVisitor':
        return LockVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LockVisitor):
        """
        Dynamic initializer for LockVisitor.
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
    def applyReadLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyReadLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object.__wrap(super(__LockVisitor, self).applyReadLocked(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def acceptWriteLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptWriteLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(__LockVisitor, self).acceptWriteLocked(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getLock(self) -> object:
        """public L org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getLock()"""
        return object.__wrap(super(LockVisitor, self).getLock())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getObject(self) -> object:
        """public O org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.getObject()"""
        return object.__wrap(super(LockVisitor, self).getObject())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def acceptReadLocked(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.acceptReadLocked(org.apache.commons.lang3.function.FailableConsumer<O, ?>)"""
        super(__LockVisitor, self).acceptReadLocked(arg0)

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
    def applyWriteLocked(self, arg0: 'FailableFunction') -> object:
        """public <T> T org.apache.commons.lang3.concurrent.locks.LockingVisitors$LockVisitor.applyWriteLocked(org.apache.commons.lang3.function.FailableFunction<O, T, ?>)"""
        return object.__wrap(super(__LockVisitor, self).applyWriteLocked(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))