from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import dev.ultreon.quantum.client.config.entries.StringEntry as _StringEntry
_StringEntry = _StringEntry
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringEntry():
    """dev.ultreon.quantum.client.config.entries.StringEntry"""
 
    @staticmethod
    def _wrap(java_value: _StringEntry) -> 'StringEntry':
        return StringEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringEntry):
        """
        Dynamic initializer for StringEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object._wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str._wrap(super(gui.ConfigEntry, self).getDescription())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(_gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str._wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.StringEntry(java.lang.String,java.lang.String,dev.ultreon.quantum.client.config.Configuration)"""
        val = _StringEntry(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'._wrap(super(_gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(_gui.ConfigEntry, self).readAndSet(arg0)

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
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str._wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str._wrap(super(gui.ConfigEntry, self).write())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.StringEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import dev.ultreon.quantum.client.config.entries.StringEntry as _StringEntry
_StringEntry = _StringEntry
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringEntry():
    """dev.ultreon.quantum.client.config.entries.StringEntry"""
 
    @staticmethod
    def _wrap(java_value: _StringEntry) -> 'StringEntry':
        return StringEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringEntry):
        """
        Dynamic initializer for StringEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object._wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str._wrap(super(gui.ConfigEntry, self).getDescription())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(_gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str._wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.StringEntry(java.lang.String,java.lang.String,dev.ultreon.quantum.client.config.Configuration)"""
        val = _StringEntry(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'._wrap(super(_gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(_gui.ConfigEntry, self).readAndSet(arg0)

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
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str._wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str._wrap(super(gui.ConfigEntry, self).write())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.StringEntry 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.DoubleEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
import dev.ultreon.quantum.client.config.entries.DoubleEntry as _DoubleEntry
_DoubleEntry = _DoubleEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DoubleEntry():
    """dev.ultreon.quantum.client.config.entries.DoubleEntry"""
 
    @staticmethod
    def _wrap(java_value: _DoubleEntry) -> 'DoubleEntry':
        return DoubleEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleEntry):
        """
        Dynamic initializer for DoubleEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object._wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str._wrap(super(gui.ConfigEntry, self).getDescription())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(_gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str._wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMax(self) -> float:
        """public double dev.ultreon.quantum.client.config.entries.DoubleEntry.getMax()"""
        return float._wrap(super(DoubleEntry, self).getMax())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'._wrap(super(_gui.ConfigEntry, self).comment(arg0))

    @overload
    def getMin(self) -> float:
        """public double dev.ultreon.quantum.client.config.entries.DoubleEntry.getMin()"""
        return float._wrap(super(DoubleEntry, self).getMin())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(_gui.ConfigEntry, self).readAndSet(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.DoubleEntry(java.lang.String,double,double,double,dev.ultreon.quantum.client.config.Configuration)"""
        val = _DoubleEntry(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), arg4)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str._wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str._wrap(super(gui.ConfigEntry, self).write())

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
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.FloatEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.config.entries.FloatEntry as _FloatEntry
_FloatEntry = _FloatEntry
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatEntry():
    """dev.ultreon.quantum.client.config.entries.FloatEntry"""
 
    @staticmethod
    def _wrap(java_value: _FloatEntry) -> 'FloatEntry':
        return FloatEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatEntry):
        """
        Dynamic initializer for FloatEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object._wrap(super(gui.ConfigEntry, self).get())

    @overload
    def __init__(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.FloatEntry(java.lang.String,float,float,float,dev.ultreon.quantum.client.config.Configuration)"""
        val = _FloatEntry(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)
        self.__wrapper = val

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str._wrap(super(gui.ConfigEntry, self).getDescription())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(_gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str._wrap(super(gui.ConfigEntry, self).getComment())

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
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'._wrap(super(_gui.ConfigEntry, self).comment(arg0))

    @overload
    def getMax(self) -> float:
        """public float dev.ultreon.quantum.client.config.entries.FloatEntry.getMax()"""
        return float._wrap(super(FloatEntry, self).getMax())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(_gui.ConfigEntry, self).readAndSet(arg0)

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
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str._wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str._wrap(super(gui.ConfigEntry, self).write())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMin(self) -> float:
        """public float dev.ultreon.quantum.client.config.entries.FloatEntry.getMin()"""
        return float._wrap(super(FloatEntry, self).getMin())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.UUIDEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

import dev.ultreon.quantum.client.config.entries.UUIDEntry as _UUIDEntry
_UUIDEntry = _UUIDEntry
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UUIDEntry():
    """dev.ultreon.quantum.client.config.entries.UUIDEntry"""
 
    @staticmethod
    def _wrap(java_value: _UUIDEntry) -> 'UUIDEntry':
        return UUIDEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UUIDEntry):
        """
        Dynamic initializer for UUIDEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UUIDEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UUIDEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object._wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str._wrap(super(gui.ConfigEntry, self).getDescription())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(_gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str._wrap(super(gui.ConfigEntry, self).getComment())

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
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'._wrap(super(_gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(_gui.ConfigEntry, self).readAndSet(arg0)

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
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str._wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str._wrap(super(gui.ConfigEntry, self).write())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'UUID', arg2: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.UUIDEntry(java.lang.String,java.util.UUID,dev.ultreon.quantum.client.config.Configuration)"""
        val = _UUIDEntry(arg0, arg1, arg2)
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
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.IntEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import dev.ultreon.quantum.client.config.entries.IntEntry as _IntEntry
_IntEntry = _IntEntry
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntEntry():
    """dev.ultreon.quantum.client.config.entries.IntEntry"""
 
    @staticmethod
    def _wrap(java_value: _IntEntry) -> 'IntEntry':
        return IntEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntEntry):
        """
        Dynamic initializer for IntEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object._wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str._wrap(super(gui.ConfigEntry, self).getDescription())

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.IntEntry(java.lang.String,int,int,int,dev.ultreon.quantum.client.config.Configuration)"""
        val = _IntEntry(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @overload
    def getMax(self) -> int:
        """public int dev.ultreon.quantum.client.config.entries.IntEntry.getMax()"""
        return int._wrap(super(IntEntry, self).getMax())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(_gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str._wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMin(self) -> int:
        """public int dev.ultreon.quantum.client.config.entries.IntEntry.getMin()"""
        return int._wrap(super(IntEntry, self).getMin())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'._wrap(super(_gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(_gui.ConfigEntry, self).readAndSet(arg0)

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
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str._wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str._wrap(super(gui.ConfigEntry, self).write())

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
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.BooleanEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import dev.ultreon.quantum.client.config.entries.BooleanEntry as _BooleanEntry
_BooleanEntry = _BooleanEntry
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BooleanEntry():
    """dev.ultreon.quantum.client.config.entries.BooleanEntry"""
 
    @staticmethod
    def _wrap(java_value: _BooleanEntry) -> 'BooleanEntry':
        return BooleanEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BooleanEntry):
        """
        Dynamic initializer for BooleanEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BooleanEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BooleanEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object._wrap(super(gui.ConfigEntry, self).get())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str._wrap(super(gui.ConfigEntry, self).getDescription())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(_gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str._wrap(super(gui.ConfigEntry, self).getComment())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: bool, arg2: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.BooleanEntry(java.lang.String,boolean,dev.ultreon.quantum.client.config.Configuration)"""
        val = _BooleanEntry(arg0, _boolean.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'._wrap(super(_gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(_gui.ConfigEntry, self).readAndSet(arg0)

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
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str._wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str._wrap(super(gui.ConfigEntry, self).write())

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
 
 
# CLASS: dev.ultreon.quantum.client.config.entries.LongEntry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.config import gui
except ImportError:
    gui = _import_once("pyquantum.client.config.gui")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import java.lang.String as _string
import dev.ultreon.quantum.client.config.entries.LongEntry as _LongEntry
_LongEntry = _LongEntry
import java.lang.Integer as _int
import dev.ultreon.quantum.client.config.gui.ConfigEntry as _ConfigEntry
_ConfigEntry = _ConfigEntry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongEntry():
    """dev.ultreon.quantum.client.config.entries.LongEntry"""
 
    @staticmethod
    def _wrap(java_value: _LongEntry) -> 'LongEntry':
        return LongEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongEntry):
        """
        Dynamic initializer for LongEntry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongEntry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongEntry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.client.config.gui.ConfigEntry.get()"""
        return object._wrap(super(gui.ConfigEntry, self).get())

    @overload
    def getMax(self) -> int:
        """public long dev.ultreon.quantum.client.config.entries.LongEntry.getMax()"""
        return int._wrap(super(LongEntry, self).getMax())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getDescription()"""
        return str._wrap(super(gui.ConfigEntry, self).getDescription())

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: 'Configuration'):
        """public dev.ultreon.quantum.client.config.entries.LongEntry(java.lang.String,long,long,long,dev.ultreon.quantum.client.config.Configuration)"""
        val = _LongEntry(arg0, _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.set(T)"""
        super(_gui.ConfigEntry, self).set(arg0)

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getComment()"""
        return str._wrap(super(gui.ConfigEntry, self).getComment())

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
    def comment(self, arg0: str) -> 'gui.ConfigEntry':
        """public dev.ultreon.quantum.client.config.gui.ConfigEntry<T> dev.ultreon.quantum.client.config.gui.ConfigEntry.comment(java.lang.String)"""
        return 'gui.ConfigEntry'._wrap(super(_gui.ConfigEntry, self).comment(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def readAndSet(self, arg0: str):
        """public void dev.ultreon.quantum.client.config.gui.ConfigEntry.readAndSet(java.lang.String)"""
        super(_gui.ConfigEntry, self).readAndSet(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getMin(self) -> int:
        """public long dev.ultreon.quantum.client.config.entries.LongEntry.getMin()"""
        return int._wrap(super(LongEntry, self).getMin())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getKey(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.getKey()"""
        return str._wrap(super(gui.ConfigEntry, self).getKey())

    @override
    @overload
    def write(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.config.gui.ConfigEntry.write()"""
        return str._wrap(super(gui.ConfigEntry, self).write())

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