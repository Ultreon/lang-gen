from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

from builtins import object
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.config.entries.StringEntry as __StringEntry
__StringEntry = __StringEntry
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from builtins import int
 
class StringEntry(config.__ConfigEntry, gui.ConfigEntry):
    """dev.ultreon.quantum.client.config.entries.StringEntry"""
 
    @staticmethod
    def __wrap(java_value: __StringEntry) -> 'StringEntry':
        return StringEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringEntry):
        """
        Dynamic initializer for StringEntry.
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
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str.__wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object.__wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(__gui.ConfigEntry, self).set(arg0)

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.StringEntry(java.lang.String,java.lang.String,dev.ultreon.quantum.client.config.Configuration)"""
        val = __StringEntry(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str.__wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'.__wrap(super(__gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(__gui.ConfigEntry, self).readAndSet(arg0)

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
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str.__wrap(super(gui.ConfigEntry, self).getDescription())

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

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str.__wrap(super(gui.ConfigEntry, self).write())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.StringEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

from builtins import object
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.config.entries.StringEntry as __StringEntry
__StringEntry = __StringEntry
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from builtins import int
 
class StringEntry(config.__ConfigEntry, gui.ConfigEntry):
    """dev.ultreon.quantum.client.config.entries.StringEntry"""
 
    @staticmethod
    def __wrap(java_value: __StringEntry) -> 'StringEntry':
        return StringEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringEntry):
        """
        Dynamic initializer for StringEntry.
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
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str.__wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object.__wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(__gui.ConfigEntry, self).set(arg0)

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.StringEntry(java.lang.String,java.lang.String,dev.ultreon.quantum.client.config.Configuration)"""
        val = __StringEntry(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str.__wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'.__wrap(super(__gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(__gui.ConfigEntry, self).readAndSet(arg0)

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
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str.__wrap(super(gui.ConfigEntry, self).getDescription())

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

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str.__wrap(super(gui.ConfigEntry, self).write())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.StringEntry 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.DoubleEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

from builtins import float
from builtins import object
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import dev.ultreon.quantum.client.config.entries.DoubleEntry as __DoubleEntry
__DoubleEntry = __DoubleEntry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from builtins import int
 
class DoubleEntry(config.__ConfigEntry, gui.ConfigEntry):
    """dev.ultreon.quantum.client.config.entries.DoubleEntry"""
 
    @staticmethod
    def __wrap(java_value: __DoubleEntry) -> 'DoubleEntry':
        return DoubleEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleEntry):
        """
        Dynamic initializer for DoubleEntry.
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
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str.__wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object.__wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(__gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getMax(self) -> float:
        """public double dev.ultreon.quantum.client.config.entries.DoubleEntry.getMax()"""
        return float.__wrap(super(DoubleEntry, self).getMax())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str.__wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'.__wrap(super(__gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(__gui.ConfigEntry, self).readAndSet(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.DoubleEntry(java.lang.String,double,double,double,dev.ultreon.quantum.client.config.Configuration)"""
        val = __DoubleEntry(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), arg4)
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
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str.__wrap(super(gui.ConfigEntry, self).getDescription())

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
    def getMin(self) -> float:
        """public double dev.ultreon.quantum.client.config.entries.DoubleEntry.getMin()"""
        return float.__wrap(super(DoubleEntry, self).getMin())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str.__wrap(super(gui.ConfigEntry, self).write())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.FloatEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

from builtins import float
from builtins import object
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import dev.ultreon.quantum.client.config.entries.FloatEntry as __FloatEntry
__FloatEntry = __FloatEntry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from builtins import int
 
class FloatEntry(config.__ConfigEntry, gui.ConfigEntry):
    """dev.ultreon.quantum.client.config.entries.FloatEntry"""
 
    @staticmethod
    def __wrap(java_value: __FloatEntry) -> 'FloatEntry':
        return FloatEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatEntry):
        """
        Dynamic initializer for FloatEntry.
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
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str.__wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object.__wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(__gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str.__wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'.__wrap(super(__gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(__gui.ConfigEntry, self).readAndSet(arg0)

    @overload
    def __init__(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.FloatEntry(java.lang.String,float,float,float,dev.ultreon.quantum.client.config.Configuration)"""
        val = __FloatEntry(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getMax(self) -> float:
        """public float dev.ultreon.quantum.client.config.entries.FloatEntry.getMax()"""
        return float.__wrap(super(FloatEntry, self).getMax())

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
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str.__wrap(super(gui.ConfigEntry, self).getDescription())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getMin(self) -> float:
        """public float dev.ultreon.quantum.client.config.entries.FloatEntry.getMin()"""
        return float.__wrap(super(FloatEntry, self).getMin())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str.__wrap(super(gui.ConfigEntry, self).write())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.UUIDEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

from builtins import object
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.client.config.entries.UUIDEntry as __UUIDEntry
__UUIDEntry = __UUIDEntry
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from builtins import int
 
class UUIDEntry(config.__ConfigEntry, gui.ConfigEntry):
    """dev.ultreon.quantum.client.config.entries.UUIDEntry"""
 
    @staticmethod
    def __wrap(java_value: __UUIDEntry) -> 'UUIDEntry':
        return UUIDEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UUIDEntry):
        """
        Dynamic initializer for UUIDEntry.
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
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str.__wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object.__wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(__gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str.__wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'.__wrap(super(__gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(__gui.ConfigEntry, self).readAndSet(arg0)

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

    @overload
    def __init__(self, arg0: str, arg1: 'UUID', arg2: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.UUIDEntry(java.lang.String,java.util.UUID,dev.ultreon.quantum.client.config.Configuration)"""
        val = __UUIDEntry(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str.__wrap(super(gui.ConfigEntry, self).getDescription())

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

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str.__wrap(super(gui.ConfigEntry, self).write())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.IntEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

from builtins import object
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import java.lang.Long as __long
import dev.ultreon.quantum.client.config.entries.IntEntry as __IntEntry
__IntEntry = __IntEntry
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
 
class IntEntry(config.__ConfigEntry, gui.ConfigEntry):
    """dev.ultreon.quantum.client.config.entries.IntEntry"""
 
    @staticmethod
    def __wrap(java_value: __IntEntry) -> 'IntEntry':
        return IntEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntEntry):
        """
        Dynamic initializer for IntEntry.
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
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str.__wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object.__wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(__gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str.__wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'.__wrap(super(__gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(__gui.ConfigEntry, self).readAndSet(arg0)

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
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str.__wrap(super(gui.ConfigEntry, self).getDescription())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getMin(self) -> int:
        """public int dev.ultreon.quantum.client.config.entries.IntEntry.getMin()"""
        return int.__wrap(super(IntEntry, self).getMin())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMax(self) -> int:
        """public int dev.ultreon.quantum.client.config.entries.IntEntry.getMax()"""
        return int.__wrap(super(IntEntry, self).getMax())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str.__wrap(super(gui.ConfigEntry, self).write())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.IntEntry(java.lang.String,int,int,int,dev.ultreon.quantum.client.config.Configuration)"""
        val = __IntEntry(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.BooleanEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

from builtins import object
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.config.entries.BooleanEntry as __BooleanEntry
__BooleanEntry = __BooleanEntry
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
from builtins import int
 
class BooleanEntry(config.__ConfigEntry, gui.ConfigEntry):
    """dev.ultreon.quantum.client.config.entries.BooleanEntry"""
 
    @staticmethod
    def __wrap(java_value: __BooleanEntry) -> 'BooleanEntry':
        return BooleanEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanEntry):
        """
        Dynamic initializer for BooleanEntry.
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
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str.__wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object.__wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(__gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str.__wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'.__wrap(super(__gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(__gui.ConfigEntry, self).readAndSet(arg0)

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
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str.__wrap(super(gui.ConfigEntry, self).getDescription())

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
    def __init__(self, arg0: str, arg1: bool, arg2: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.BooleanEntry(java.lang.String,boolean,dev.ultreon.quantum.client.config.Configuration)"""
        val = __BooleanEntry(arg0, __boolean.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str.__wrap(super(gui.ConfigEntry, self).write())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.LongEntry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = __import_once__("pyquantum.client.config.gui")

from builtins import object
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.config.entries.LongEntry as __LongEntry
__LongEntry = __LongEntry
from builtins import bool
from builtins import int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as __ConfigEntry
__ConfigEntry = __ConfigEntry
 
class LongEntry(config.__ConfigEntry, gui.ConfigEntry):
    """dev.ultreon.quantum.client.config.entries.LongEntry"""
 
    @staticmethod
    def __wrap(java_value: __LongEntry) -> 'LongEntry':
        return LongEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongEntry):
        """
        Dynamic initializer for LongEntry.
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
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str.__wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object.__wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(__gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str.__wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'.__wrap(super(__gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(__gui.ConfigEntry, self).readAndSet(arg0)

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

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.LongEntry(java.lang.String,long,long,long,dev.ultreon.quantum.client.config.Configuration)"""
        val = __LongEntry(arg0, __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str.__wrap(super(gui.ConfigEntry, self).getDescription())

    @overload
    def getMax(self) -> int:
        """public long dev.ultreon.quantum.client.config.entries.LongEntry.getMax()"""
        return int.__wrap(super(LongEntry, self).getMax())

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
    def getMin(self) -> int:
        """public long dev.ultreon.quantum.client.config.entries.LongEntry.getMin()"""
        return int.__wrap(super(LongEntry, self).getMin())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str.__wrap(super(gui.ConfigEntry, self).write())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))