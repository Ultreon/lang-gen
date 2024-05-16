from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.client.util.InvalidValueException as _InvalidValueException
_InvalidValueException = _InvalidValueException
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidValueException():
    """dev.ultreon.quantum.client.util.InvalidValueException"""
 
    @staticmethod
    def _wrap(java_value: _InvalidValueException) -> 'InvalidValueException':
        return InvalidValueException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidValueException):
        """
        Dynamic initializer for InvalidValueException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidValueException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidValueException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.Throwable)"""
        val = _InvalidValueException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.String)"""
        val = _InvalidValueException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.util.InvalidValueException()"""
        val = _InvalidValueException()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.InvalidValueException()"""
        val = _InvalidValueException()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.String,java.lang.Throwable)"""
        val = _InvalidValueException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

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

 
 
 
# CLASS: dev.ultreon.quantum.client.util.InvalidValueException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.client.util.InvalidValueException as _InvalidValueException
_InvalidValueException = _InvalidValueException
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidValueException():
    """dev.ultreon.quantum.client.util.InvalidValueException"""
 
    @staticmethod
    def _wrap(java_value: _InvalidValueException) -> 'InvalidValueException':
        return InvalidValueException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidValueException):
        """
        Dynamic initializer for InvalidValueException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidValueException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidValueException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.Throwable)"""
        val = _InvalidValueException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.String)"""
        val = _InvalidValueException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.util.InvalidValueException()"""
        val = _InvalidValueException()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.InvalidValueException()"""
        val = _InvalidValueException()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.String,java.lang.Throwable)"""
        val = _InvalidValueException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

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

 
 
 
# CLASS: dev.ultreon.quantum.client.util.InvalidValueException 
 
 
# CLASS: dev.ultreon.quantum.client.util.GG
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.util.GG as _GG
_GG = _GG
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GG():
    """dev.ultreon.quantum.client.util.GG"""
 
    @staticmethod
    def _wrap(java_value: _GG) -> 'GG':
        return GG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GG):
        """
        Dynamic initializer for GG.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GG__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GG__wrapper":
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

    @overload
    def say(self):
        """public void dev.ultreon.quantum.client.util.GG.say()"""
        super(GG, self).say()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.GG()"""
        val = _GG()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.GG()"""
        val = _GG()
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
 
 
# CLASS: dev.ultreon.quantum.client.util.RenderableArray
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.utils.Array as _Array_ArrayIterator
_ArrayIterator = _Array_ArrayIterator.ArrayIterator
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.util.RenderableArray as _RenderableArray
_RenderableArray = _RenderableArray
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderableArray():
    """dev.ultreon.quantum.client.util.RenderableArray"""
 
    @staticmethod
    def _wrap(java_value: _RenderableArray) -> 'RenderableArray':
        return RenderableArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderableArray):
        """
        Dynamic initializer for RenderableArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderableArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderableArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def pop(self) -> object:
        """public T com.badlogic.gdx.utils.Array.pop()"""
        return object._wrap(super(utils.Array, self).pop())

    @overload
    def add(self, arg0: 'Renderable', arg1: 'Renderable', arg2: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.add(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_RenderableArray, self).add(arg0, arg1, arg2)

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equalsIdentity(java.lang.Object)"""
        return bool._wrap(super(_utils.Array, self).equalsIdentity(arg0))

    @override
    @overload
    def shrink(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.shrink()"""
        return List[object]._wrap(super(utils.Array, self).shrink())

    @overload
    def setSize(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.setSize(int)"""
        return List[object]._wrap(super(_utils.Array, self).setSize(_int.valueOf(arg0)))

    @overload
    def add(self, arg0: 'Renderable', arg1: 'Renderable', arg2: 'Renderable', arg3: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.add(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_RenderableArray, self).add(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.set(int,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_RenderableArray, self).set(_int.valueOf(arg0), arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.Array.shuffle()"""
        super(utils.Array, self).shuffle()

    @override
    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.notEmpty()"""
        return bool._wrap(super(utils.Array, self).notEmpty())

    @override
    @overload
    def addAll(self, arg0: 'Array'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.addAll(com.badlogic.gdx.utils.Array<? extends com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_RenderableArray, self).addAll(arg0)

    @overload
    def add(self, arg0: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.add(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_RenderableArray, self).add(arg0)

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.quantum.client.util.RenderableArray.clear()"""
        super(RenderableArray, self).clear()

    @overload
    def removeAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.removeAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool._wrap(super(_utils.Array, self).removeAll(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'utils.Array$ArrayIterator':
        """public com.badlogic.gdx.utils.Array$ArrayIterator<T> com.badlogic.gdx.utils.Array.iterator()"""
        return 'utils.Array$ArrayIterator'._wrap(super(utils.Array, self).iterator())

    @override
    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.Array.sort()"""
        super(utils.Array, self).sort()

    @staticmethod
    @overload
    def with(*arg0: object) -> 'utils.Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.with(T...)"""
        return utils.Array._wrap(_Array.with(arg0))

    @overload
    def selectRankedIndex(self, arg0: 'Comparator', arg1: int) -> int:
        """public int com.badlogic.gdx.utils.Array.selectRankedIndex(java.util.Comparator<T>,int)"""
        return int._wrap(super(_utils.Array, self).selectRankedIndex(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.Array.reverse()"""
        super(utils.Array, self).reverse()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equals(java.lang.Object)"""
        return bool._wrap(super(_utils.Array, self).equals(arg0))

    @overload
    def contains(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.contains(T,boolean)"""
        return bool._wrap(super(_utils.Array, self).contains(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void com.badlogic.gdx.utils.Array.sort(java.util.Comparator<? super T>)"""
        super(_utils.Array, self).sort(arg0)

    @staticmethod
    @overload
    def getGlobalSize() -> int:
        """public static int dev.ultreon.quantum.client.util.RenderableArray.getGlobalSize()"""
        return int._wrap(_RenderableArray.getGlobalSize())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.isEmpty()"""
        return bool._wrap(super(utils.Array, self).isEmpty())

    @override
    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.insertRange(int,int)"""
        super(_utils.Array, self).insertRange(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.utils.Array.first()"""
        return object._wrap(super(utils.Array, self).first())

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public <V> V[] com.badlogic.gdx.utils.Array.toArray(java.lang.Class<V>)"""
        return List[object]._wrap(super(_utils.Array, self).toArray(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: 'Renderable', arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.util.RenderableArray(boolean,com.badlogic.gdx.graphics.g3d.Renderable[],int,int)"""
        val = _RenderableArray(_boolean.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def addAll(self, arg0: 'Array', arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.util.RenderableArray.addAll(com.badlogic.gdx.utils.Array<? extends com.badlogic.gdx.graphics.g3d.Renderable>,int,int)"""
        super(_RenderableArray, self).addAll(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.indexOf(T,boolean)"""
        return int._wrap(super(_utils.Array, self).indexOf(arg0, _boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Class'):
        """public dev.ultreon.quantum.client.util.RenderableArray(java.lang.Class)"""
        val = _RenderableArray(arg0)
        self.__wrapper = val

    @overload
    def transform(self, arg0: 'Consumer'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.transform(java.util.function.Consumer<com.badlogic.gdx.math.Matrix4>)"""
        super(_RenderableArray, self).transform(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setTranslation(self, arg0: 'Vector3'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.setTranslation(com.badlogic.gdx.math.Vector3)"""
        super(_RenderableArray, self).setTranslation(arg0)

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'Class'):
        """public dev.ultreon.quantum.client.util.RenderableArray(boolean,int,java.lang.Class)"""
        val = _RenderableArray(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def containsAny(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAny(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool._wrap(super(_utils.Array, self).containsAny(arg0, _boolean.valueOf(arg1)))

    @overload
    def add(self, arg0: 'Renderable', arg1: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.add(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_RenderableArray, self).add(arg0, arg1)

    @overload
    def addAll(self, arg0: 'Renderable', arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.util.RenderableArray.addAll(com.badlogic.gdx.graphics.g3d.Renderable[],int,int)"""
        super(_RenderableArray, self).addAll(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'Array'):
        """public dev.ultreon.quantum.client.util.RenderableArray(com.badlogic.gdx.utils.Array<? extends com.badlogic.gdx.graphics.g3d.Renderable>)"""
        val = _RenderableArray(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.RenderableArray()"""
        val = _RenderableArray()
        self.__wrapper = val

    @override
    @overload
    def peek(self) -> object:
        """public T com.badlogic.gdx.utils.Array.peek()"""
        return object._wrap(super(utils.Array, self).peek())

    @override
    @overload
    def random(self) -> object:
        """public T com.badlogic.gdx.utils.Array.random()"""
        return object._wrap(super(utils.Array, self).random())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.util.RenderableArray(int)"""
        val = _RenderableArray(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def select(self, arg0: 'Predicate') -> 'Iterable':
        """public java.lang.Iterable<T> com.badlogic.gdx.utils.Array.select(com.badlogic.gdx.utils.Predicate<T>)"""
        return 'Iterable'._wrap(super(_utils.Array, self).select(arg0))

    @override
    @overload
    def insert(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.Array.insert(int,T)"""
        super(_utils.Array, self).insert(_int.valueOf(arg0), arg1)

    @overload
    def removeValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.removeValue(T,boolean)"""
        return bool._wrap(super(_utils.Array, self).removeValue(arg0, _boolean.valueOf(arg1)))

    @overload
    def addAll(self, *arg0: 'g3d.Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.addAll(com.badlogic.gdx.graphics.g3d.Renderable...)"""
        super(_RenderableArray, self).addAll(arg0)

    @overload
    def lastIndexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.lastIndexOf(T,boolean)"""
        return int._wrap(super(_utils.Array, self).lastIndexOf(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.toArray()"""
        return List[object]._wrap(super(utils.Array, self).toArray())

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.util.RenderableArray(com.badlogic.gdx.graphics.g3d.Renderable[])"""
        val = _RenderableArray(arg0)
        self.__wrapper = val

    @overload
    def containsAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool._wrap(super(_utils.Array, self).containsAll(arg0, _boolean.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.RenderableArray()"""
        val = _RenderableArray()
        self.__wrapper = val

    @override
    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.removeRange(int,int)"""
        super(_utils.Array, self).removeRange(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.Array.hashCode()"""
        return int._wrap(super(utils.Array, self).hashCode())

    @override
    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.swap(int,int)"""
        super(_utils.Array, self).swap(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString()"""
        return str._wrap(super(utils.Array, self).toString())

    @staticmethod
    @overload
    def of(arg0: 'Class') -> 'utils.Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(java.lang.Class<T>)"""
        return utils.Array._wrap(_Array.of(arg0))

    @overload
    def ensureCapacity(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.ensureCapacity(int)"""
        return List[object]._wrap(super(_utils.Array, self).ensureCapacity(_int.valueOf(arg0)))

    @overload
    def removeIndex(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Array.removeIndex(int)"""
        return object._wrap(super(_utils.Array, self).removeIndex(_int.valueOf(arg0)))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString(java.lang.String)"""
        return str._wrap(super(_utils.Array, self).toString(arg0))

    @staticmethod
    @overload
    def of(arg0: bool, arg1: int, arg2: 'Class') -> 'utils.Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(boolean,int,java.lang.Class<T>)"""
        return utils.Array._wrap(_Array.of(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public dev.ultreon.quantum.client.util.RenderableArray(boolean,int)"""
        val = _RenderableArray(_boolean.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.Array.truncate(int)"""
        super(_utils.Array, self).truncate(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def selectRanked(self, arg0: 'Comparator', arg1: int) -> object:
        """public T com.badlogic.gdx.utils.Array.selectRanked(java.util.Comparator<T>,int)"""
        return object._wrap(super(_utils.Array, self).selectRanked(arg0, _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Array.get(int)"""
        return object._wrap(super(_utils.Array, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.util.DeferredDisposable
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import dev.ultreon.quantum.client.util.DeferredDisposable as _DeferredDisposable
_DeferredDisposable = _DeferredDisposable
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class DeferredDisposable():
    """dev.ultreon.quantum.client.util.DeferredDisposable"""
 
    @staticmethod
    def _wrap(java_value: _DeferredDisposable) -> 'DeferredDisposable':
        return DeferredDisposable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeferredDisposable):
        """
        Dynamic initializer for DeferredDisposable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeferredDisposable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeferredDisposable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def deferDispose(self, arg0: 'Disposable'):
        """public abstract <T extends com.badlogic.gdx.utils.Disposable> T dev.ultreon.quantum.client.util.DeferredDisposable.deferDispose(T)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.util.UtilityClass
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.util.UtilityClass as _UtilityClass
_UtilityClass = _UtilityClass
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UtilityClass():
    """dev.ultreon.quantum.client.util.UtilityClass"""
 
    @staticmethod
    def _wrap(java_value: _UtilityClass) -> 'UtilityClass':
        return UtilityClass(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UtilityClass):
        """
        Dynamic initializer for UtilityClass.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UtilityClass__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UtilityClass__wrapper":
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
 
 
# CLASS: dev.ultreon.quantum.client.util.InvalidThreadError
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.util.InvalidThreadError as _InvalidThreadError
_InvalidThreadError = _InvalidThreadError
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidThreadError():
    """dev.ultreon.quantum.client.util.InvalidThreadError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidThreadError) -> 'InvalidThreadError':
        return InvalidThreadError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidThreadError):
        """
        Dynamic initializer for InvalidThreadError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidThreadError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidThreadError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.util.InvalidThreadError(java.lang.String)"""
        val = _InvalidThreadError(arg0)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.util.Utils
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.util.Utils as _Utils
_Utils = _Utils
import java.lang.Runnable as Runnable
from builtins import object
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.lang.Runnable as _Runnable
_Runnable = _Runnable
import java.lang.Byte as _byte
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import java.lang.Class as _Class
_Class = _Class
 
class Utils():
    """dev.ultreon.quantum.client.util.Utils"""
 
    @staticmethod
    def _wrap(java_value: _Utils) -> 'Utils':
        return Utils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Utils):
        """
        Dynamic initializer for Utils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Utils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Utils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def with(arg0: object, arg1: 'BiConsumer') -> 'Consumer':
        """public static <R,T> java.util.function.Consumer<R> dev.ultreon.quantum.client.util.Utils.with(T,java.util.function.BiConsumer<R, T>)"""
        return Consumer._wrap(_Utils.with(arg0, arg1))

    @staticmethod
    @overload
    def make(arg0: 'Supplier') -> object:
        """public static <T> T dev.ultreon.quantum.client.util.Utils.make(java.util.function.Supplier<T>)"""
        return object._wrap(_Utils.make(arg0))

    @staticmethod
    @overload
    def normalizeToInt(arg0: int) -> int:
        """public static int dev.ultreon.quantum.client.util.Utils.normalizeToInt(byte)"""
        return int._wrap(_Utils.normalizeToInt(_byte.valueOf(arg0)))

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

    @staticmethod
    @overload
    def with(arg0: object, arg1: 'Consumer') -> 'Runnable':
        """public static <T> java.lang.Runnable dev.ultreon.quantum.client.util.Utils.with(T,java.util.function.Consumer<T>)"""
        return Runnable._wrap(_Utils.with(arg0, arg1))

    @staticmethod
    @overload
    def make(arg0: object, arg1: 'Consumer') -> object:
        """public static <T> T dev.ultreon.quantum.client.util.Utils.make(T,java.util.function.Consumer<T>)"""
        return object._wrap(_Utils.make(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.Utils()"""
        val = _Utils()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def toCoreLibs(arg0: 'Vector3') -> 'vector.Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.client.util.Utils.toCoreLibs(com.badlogic.gdx.math.Vector3)"""
        return vector.Vec3d._wrap(_Utils.toCoreLibs(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.Utils()"""
        val = _Utils()
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
 
 
# CLASS: dev.ultreon.quantum.client.util.DuplicateException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import dev.ultreon.quantum.client.util.DuplicateException as _DuplicateException
_DuplicateException = _DuplicateException
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DuplicateException():
    """dev.ultreon.quantum.client.util.DuplicateException"""
 
    @staticmethod
    def _wrap(java_value: _DuplicateException) -> 'DuplicateException':
        return DuplicateException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DuplicateException):
        """
        Dynamic initializer for DuplicateException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DuplicateException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DuplicateException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.client.util.DuplicateException(java.lang.Throwable)"""
        val = _DuplicateException(arg0)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.client.util.DuplicateException()"""
        val = _DuplicateException()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.util.DuplicateException(java.lang.String)"""
        val = _DuplicateException(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.client.util.DuplicateException(java.lang.String,java.lang.Throwable)"""
        val = _DuplicateException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.DuplicateException()"""
        val = _DuplicateException()
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.client.util.Drawable
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.util.Drawable as _Drawable
_Drawable = _Drawable
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class Drawable():
    """dev.ultreon.quantum.client.util.Drawable"""
 
    @staticmethod
    def _wrap(java_value: _Drawable) -> 'Drawable':
        return Drawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Drawable):
        """
        Dynamic initializer for Drawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Drawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Drawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public abstract void dev.ultreon.quantum.client.util.Drawable.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.util.Resizer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.util.Resizer as _Resizer
_Resizer = _Resizer
from builtins import float
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import dev.ultreon.quantum.client.util.Resizer as _Resizer_Orientation
_Orientation = _Resizer_Orientation.Orientation
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Resizer():
    """dev.ultreon.quantum.client.util.Resizer"""
 
    @staticmethod
    def _wrap(java_value: _Resizer) -> 'Resizer':
        return Resizer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Resizer):
        """
        Dynamic initializer for Resizer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Resizer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Resizer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thumbnail(self, arg0: float, arg1: float) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.client.util.Resizer.thumbnail(float,float)"""
        return 'vector.Vec2f'._wrap(super(_Resizer, self).thumbnail(_float.valueOf(arg0), _float.valueOf(arg1)))

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
    def getSourceWidth(self) -> float:
        """public float dev.ultreon.quantum.client.util.Resizer.getSourceWidth()"""
        return float._wrap(super(Resizer, self).getSourceWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getSourceHeight(self) -> float:
        """public float dev.ultreon.quantum.client.util.Resizer.getSourceHeight()"""
        return float._wrap(super(Resizer, self).getSourceHeight())

    @overload
    def getRatio(self) -> float:
        """public float dev.ultreon.quantum.client.util.Resizer.getRatio()"""
        return float._wrap(super(Resizer, self).getRatio())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.client.util.Resizer(float,float)"""
        val = _Resizer(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

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
    def getOrientation(self) -> 'Orientation':
        """public dev.ultreon.quantum.client.util.Resizer$Orientation dev.ultreon.quantum.client.util.Resizer.getOrientation()"""
        return 'Orientation'._wrap(super(Resizer, self).getOrientation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRelativeRatio(self) -> float:
        """public float dev.ultreon.quantum.client.util.Resizer.getRelativeRatio()"""
        return float._wrap(super(Resizer, self).getRelativeRatio())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.util.Named
import dev.ultreon.quantum.client.util.Named as _Named
_Named = _Named
from abc import abstractmethod, ABC
 
class Named():
    """dev.ultreon.quantum.client.util.Named"""
 
    @staticmethod
    def _wrap(java_value: _Named) -> 'Named':
        return Named(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Named):
        """
        Dynamic initializer for Named.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Named__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Named__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.client.util.Named.getName()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.util.ExtKt
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.util.Rot as _Rot
_Rot = _Rot
import dev.ultreon.quantum.client.util.ExtKt as _ExtKt
_ExtKt = _ExtKt
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExtKt():
    """dev.ultreon.quantum.client.util.ExtKt"""
 
    @staticmethod
    def _wrap(java_value: _ExtKt) -> 'ExtKt':
        return ExtKt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExtKt):
        """
        Dynamic initializer for ExtKt.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExtKt__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExtKt__wrapper":
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

    @staticmethod
    @overload
    def deg(arg0: 'Number') -> 'Rot':
        """public static final dev.ultreon.quantum.client.util.Rot dev.ultreon.quantum.client.util.ExtKt.deg(java.lang.Number)"""
        return Rot._wrap(_ExtKt.deg(arg0))

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
    def rad(arg0: 'Number') -> 'Rot':
        """public static final dev.ultreon.quantum.client.util.Rot dev.ultreon.quantum.client.util.ExtKt.rad(java.lang.Number)"""
        return Rot._wrap(_ExtKt.rad(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.client.util.TextureOffset
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.util.TextureOffset as _TextureOffset
_TextureOffset = _TextureOffset
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureOffset():
    """dev.ultreon.quantum.client.util.TextureOffset"""
 
    @staticmethod
    def _wrap(java_value: _TextureOffset) -> 'TextureOffset':
        return TextureOffset(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureOffset):
        """
        Dynamic initializer for TextureOffset.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureOffset__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureOffset__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.util.TextureOffset(int,int,int,int)"""
        val = _TextureOffset(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def bake(self, arg0: 'Texture') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.util.TextureOffset.bake(com.badlogic.gdx.graphics.Texture)"""
        return 'g2d.TextureRegion'._wrap(super(_TextureOffset, self).bake(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public dev.ultreon.quantum.client.util.TextureOffset(int,int,int,int,int,int)"""
        val = _TextureOffset(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.util.TextureOffset.equals(java.lang.Object)"""
        return bool._wrap(super(_TextureOffset, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def uWidth(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.uWidth()"""
        return int._wrap(super(TextureOffset, self).uWidth())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.util.TextureOffset.toString()"""
        return str._wrap(super(TextureOffset, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.hashCode()"""
        return int._wrap(super(TextureOffset, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.v()"""
        return int._wrap(super(TextureOffset, self).v())

    @overload
    def vHeight(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.vHeight()"""
        return int._wrap(super(TextureOffset, self).vHeight())

    @staticmethod
    @overload
    def blockUV(arg0: int, arg1: int) -> 'TextureOffset':
        """public static dev.ultreon.quantum.client.util.TextureOffset dev.ultreon.quantum.client.util.TextureOffset.blockUV(int,int)"""
        return TextureOffset._wrap(_TextureOffset.blockUV(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.util.TextureOffset(int,int)"""
        val = _TextureOffset(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def textureWidth(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.textureWidth()"""
        return int._wrap(super(TextureOffset, self).textureWidth())

    @overload
    def textureHeight(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.textureHeight()"""
        return int._wrap(super(TextureOffset, self).textureHeight())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.u()"""
        return int._wrap(super(TextureOffset, self).u()) 
 
 
# CLASS: dev.ultreon.quantum.client.util.AxisAlignedBB
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.client.util.AxisAlignedBB as _AxisAlignedBB
_AxisAlignedBB = _AxisAlignedBB
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AxisAlignedBB():
    """dev.ultreon.quantum.client.util.AxisAlignedBB"""
 
    @staticmethod
    def _wrap(java_value: _AxisAlignedBB) -> 'AxisAlignedBB':
        return AxisAlignedBB(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AxisAlignedBB):
        """
        Dynamic initializer for AxisAlignedBB.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AxisAlignedBB__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AxisAlignedBB__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def offset(self, arg0: float, arg1: float, arg2: float) -> 'AxisAlignedBB':
        """public dev.ultreon.quantum.client.util.AxisAlignedBB dev.ultreon.quantum.client.util.AxisAlignedBB.offset(float,float,float)"""
        return 'AxisAlignedBB'._wrap(super(_AxisAlignedBB, self).offset(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def intersects(self, arg0: 'AxisAlignedBB') -> bool:
        """public boolean dev.ultreon.quantum.client.util.AxisAlignedBB.intersects(dev.ultreon.quantum.client.util.AxisAlignedBB)"""
        return bool._wrap(super(_AxisAlignedBB, self).intersects(arg0))

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

    @overload
    def calculateIntersect(self, arg0: 'AxisAlignedBB', arg1: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.util.AxisAlignedBB.calculateIntersect(dev.ultreon.quantum.client.util.AxisAlignedBB,com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_AxisAlignedBB, self).calculateIntersect(arg0, arg1))

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
    def calculateIntersect(self, arg0: 'AxisAlignedBB', arg1: 'Vector3', arg2: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.util.AxisAlignedBB.calculateIntersect(dev.ultreon.quantum.client.util.AxisAlignedBB,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_AxisAlignedBB, self).calculateIntersect(arg0, arg1, arg2))

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
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public dev.ultreon.quantum.client.util.AxisAlignedBB(float,float,float,float,float,float)"""
        val = _AxisAlignedBB(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))
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
 
 
# CLASS: dev.ultreon.quantum.client.util.Resizer$Orientation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import dev.ultreon.quantum.client.util.Resizer as _Resizer_Orientation
_Orientation = _Resizer_Orientation.Orientation
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Orientation():
    """dev.ultreon.quantum.client.util.Resizer.Orientation"""
 
    @staticmethod
    def _wrap(java_value: _Orientation) -> 'Orientation':
        return Orientation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Orientation):
        """
        Dynamic initializer for Orientation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Orientation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Orientation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Orientation':
        """public static dev.ultreon.quantum.client.util.Resizer$Orientation dev.ultreon.quantum.client.util.Resizer$Orientation.valueOf(java.lang.String)"""
        return Orientation._wrap(_Orientation.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['Orientation']:
        """public static dev.ultreon.quantum.client.util.Resizer$Orientation[] dev.ultreon.quantum.client.util.Resizer$Orientation.values()"""
        return List[Orientation]._wrap(_Orientation.values())


Orientation.PORTRAIT = Orientation._wrap(_PORTRAIT.PORTRAIT)

Orientation.LANDSCAPE = Orientation._wrap(_LANDSCAPE.LANDSCAPE)

Orientation.SQUARE = Orientation._wrap(_SQUARE.SQUARE) 
 
 
# CLASS: dev.ultreon.quantum.client.util.Rot
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.client.util.Rot as _Rot
_Rot = _Rot
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Rot():
    """dev.ultreon.quantum.client.util.Rot"""
 
    @staticmethod
    def _wrap(java_value: _Rot) -> 'Rot':
        return Rot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rot):
        """
        Dynamic initializer for Rot.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rot__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rot__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.util.Rot.toString()"""
        return str._wrap(super(Rot, self).toString())

    @overload
    def copy(self, arg0: float) -> 'Rot':
        """public final dev.ultreon.quantum.client.util.Rot dev.ultreon.quantum.client.util.Rot.copy(float)"""
        return 'Rot'._wrap(super(_Rot, self).copy(_float.valueOf(arg0)))

    @overload
    def getRadians(self) -> float:
        """public final float dev.ultreon.quantum.client.util.Rot.getRadians()"""
        return float._wrap(super(Rot, self).getRadians())

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
    def __init__(self, arg0: float):
        """public dev.ultreon.quantum.client.util.Rot(float)"""
        val = _Rot(_float.valueOf(arg0))
        self.__wrapper = val

    @overload
    def component1(self) -> float:
        """public final float dev.ultreon.quantum.client.util.Rot.component1()"""
        return float._wrap(super(Rot, self).component1())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getDegrees(self) -> float:
        """public final float dev.ultreon.quantum.client.util.Rot.getDegrees()"""
        return float._wrap(super(Rot, self).getDegrees())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.util.Rot.hashCode()"""
        return int._wrap(super(Rot, self).hashCode())

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
        """public boolean dev.ultreon.quantum.client.util.Rot.equals(java.lang.Object)"""
        return bool._wrap(super(_Rot, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.util.PlayerView
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.util.PlayerView as _PlayerView
_PlayerView = _PlayerView
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerView():
    """dev.ultreon.quantum.client.util.PlayerView"""
 
    @staticmethod
    def _wrap(java_value: _PlayerView) -> 'PlayerView':
        return PlayerView(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerView):
        """
        Dynamic initializer for PlayerView.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerView__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerView__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'PlayerView':
        """public static dev.ultreon.quantum.client.util.PlayerView dev.ultreon.quantum.client.util.PlayerView.valueOf(java.lang.String)"""
        return PlayerView._wrap(_PlayerView.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['PlayerView']:
        """public static dev.ultreon.quantum.client.util.PlayerView[] dev.ultreon.quantum.client.util.PlayerView.values()"""
        return List[PlayerView]._wrap(_PlayerView.values())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


PlayerView.THIRD_PERSON_FRONT = PlayerView._wrap(_THIRD_PERSON_FRONT.THIRD_PERSON_FRONT)

PlayerView.FIRST_PERSON = PlayerView._wrap(_FIRST_PERSON.FIRST_PERSON)

PlayerView.THIRD_PERSON = PlayerView._wrap(_THIRD_PERSON.THIRD_PERSON) 
 
 
# CLASS: dev.ultreon.quantum.client.util.GameRenderable
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.client.util.GameRenderable as _GameRenderable
_GameRenderable = _GameRenderable
from abc import abstractmethod, ABC
 
class GameRenderable():
    """dev.ultreon.quantum.client.util.GameRenderable"""
 
    @staticmethod
    def _wrap(java_value: _GameRenderable) -> 'GameRenderable':
        return GameRenderable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameRenderable):
        """
        Dynamic initializer for GameRenderable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameRenderable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameRenderable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: float):
        """public abstract void dev.ultreon.quantum.client.util.GameRenderable.render(dev.ultreon.quantum.client.gui.Renderer,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.util.Renderable
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.util.Renderable as _Renderable
_Renderable = _Renderable
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class Renderable():
    """dev.ultreon.quantum.client.util.Renderable"""
 
    @staticmethod
    def _wrap(java_value: _Renderable) -> 'Renderable':
        return Renderable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Renderable):
        """
        Dynamic initializer for Renderable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Renderable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Renderable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public abstract void dev.ultreon.quantum.client.util.Renderable.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        pass