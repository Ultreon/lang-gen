from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.util.InvalidValueException as __InvalidValueException
__InvalidValueException = __InvalidValueException
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidValueException():
    """dev.ultreon.quantum.client.util.InvalidValueException"""
 
    @staticmethod
    def __wrap(java_value: __InvalidValueException) -> 'InvalidValueException':
        return InvalidValueException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidValueException):
        """
        Dynamic initializer for InvalidValueException.
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
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.Throwable)"""
        val = __InvalidValueException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.InvalidValueException()"""
        val = __InvalidValueException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.String,java.lang.Throwable)"""
        val = __InvalidValueException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.InvalidValueException()"""
        val = __InvalidValueException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.String)"""
        val = __InvalidValueException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

 
 
 
# CLASS: dev.ultreon.quantum.client.util.InvalidValueException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.util.InvalidValueException as __InvalidValueException
__InvalidValueException = __InvalidValueException
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidValueException():
    """dev.ultreon.quantum.client.util.InvalidValueException"""
 
    @staticmethod
    def __wrap(java_value: __InvalidValueException) -> 'InvalidValueException':
        return InvalidValueException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidValueException):
        """
        Dynamic initializer for InvalidValueException.
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
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.Throwable)"""
        val = __InvalidValueException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.InvalidValueException()"""
        val = __InvalidValueException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.String,java.lang.Throwable)"""
        val = __InvalidValueException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.InvalidValueException()"""
        val = __InvalidValueException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.util.InvalidValueException(java.lang.String)"""
        val = __InvalidValueException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

 
 
 
# CLASS: dev.ultreon.quantum.client.util.InvalidValueException 
 
 
# CLASS: dev.ultreon.quantum.client.util.GG
import dev.ultreon.quantum.client.util.GG as __GG
__GG = __GG
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GG():
    """dev.ultreon.quantum.client.util.GG"""
 
    @staticmethod
    def __wrap(java_value: __GG) -> 'GG':
        return GG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GG):
        """
        Dynamic initializer for GG.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.GG()"""
        val = __GG()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.GG()"""
        val = __GG()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def say(self):
        """public void dev.ultreon.quantum.client.util.GG.say()"""
        super(GG, self).say()

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
 
 
# CLASS: dev.ultreon.quantum.client.util.RenderableArray
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.utils.Array as __Array_ArrayIterator
__ArrayIterator = __Array_ArrayIterator.ArrayIterator
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.util.RenderableArray as __RenderableArray
__RenderableArray = __RenderableArray
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import java.lang.Iterable as Iterable
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class RenderableArray():
    """dev.ultreon.quantum.client.util.RenderableArray"""
 
    @staticmethod
    def __wrap(java_value: __RenderableArray) -> 'RenderableArray':
        return RenderableArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderableArray):
        """
        Dynamic initializer for RenderableArray.
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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.utils.Array.hashCode()"""
        return int.__wrap(super(utils.Array, self).hashCode())

    @override
    @overload
    def peek(self) -> object:
        """public T com.badlogic.gdx.utils.Array.peek()"""
        return object.__wrap(super(utils.Array, self).peek())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addAll(self, arg0: 'Renderable', arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.util.RenderableArray.addAll(com.badlogic.gdx.graphics.g3d.Renderable[],int,int)"""
        super(__RenderableArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public dev.ultreon.quantum.client.util.RenderableArray(boolean,int)"""
        val = __RenderableArray(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.isEmpty()"""
        return bool.__wrap(super(utils.Array, self).isEmpty())

    @staticmethod
    @overload
    def with(*arg0: object) -> 'utils.Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.with(T...)"""
        return utils.Array.__wrap(__Array.with(arg0))

    @override
    @overload
    def random(self) -> object:
        """public T com.badlogic.gdx.utils.Array.random()"""
        return object.__wrap(super(utils.Array, self).random())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Array.get(int)"""
        return object.__wrap(super(__utils.Array, self).get(__int.valueOf(arg0)))

    @overload
    def transform(self, arg0: 'Consumer'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.transform(java.util.function.Consumer<com.badlogic.gdx.math.Matrix4>)"""
        super(__RenderableArray, self).transform(arg0)

    @override
    @overload
    def shuffle(self):
        """public void com.badlogic.gdx.utils.Array.shuffle()"""
        super(utils.Array, self).shuffle()

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.quantum.client.util.RenderableArray.clear()"""
        super(RenderableArray, self).clear()

    @overload
    def set(self, arg0: int, arg1: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.set(int,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__RenderableArray, self).set(__int.valueOf(arg0), arg1)

    @overload
    def selectRankedIndex(self, arg0: 'Comparator', arg1: int) -> int:
        """public int com.badlogic.gdx.utils.Array.selectRankedIndex(java.util.Comparator<T>,int)"""
        return int.__wrap(super(__utils.Array, self).selectRankedIndex(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def shrink(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.shrink()"""
        return List[object].__wrap(super(utils.Array, self).shrink())

    @override
    @overload
    def iterator(self) -> 'utils.Array$ArrayIterator':
        """public com.badlogic.gdx.utils.Array$ArrayIterator<T> com.badlogic.gdx.utils.Array.iterator()"""
        return 'utils.Array$ArrayIterator'.__wrap(super(utils.Array, self).iterator())

    @override
    @overload
    def sort(self):
        """public void com.badlogic.gdx.utils.Array.sort()"""
        super(utils.Array, self).sort()

    @override
    @overload
    def addAll(self, arg0: 'Array', arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.util.RenderableArray.addAll(com.badlogic.gdx.utils.Array<? extends com.badlogic.gdx.graphics.g3d.Renderable>,int,int)"""
        super(__RenderableArray, self).addAll(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def reverse(self):
        """public void com.badlogic.gdx.utils.Array.reverse()"""
        super(utils.Array, self).reverse()

    @override
    @overload
    def pop(self) -> object:
        """public T com.badlogic.gdx.utils.Array.pop()"""
        return object.__wrap(super(utils.Array, self).pop())

    @overload
    def select(self, arg0: 'Predicate') -> 'Iterable':
        """public java.lang.Iterable<T> com.badlogic.gdx.utils.Array.select(com.badlogic.gdx.utils.Predicate<T>)"""
        return 'Iterable'.__wrap(super(__utils.Array, self).select(arg0))

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString(java.lang.String)"""
        return str.__wrap(super(__utils.Array, self).toString(arg0))

    @overload
    def ensureCapacity(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.ensureCapacity(int)"""
        return List[object].__wrap(super(__utils.Array, self).ensureCapacity(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Array'):
        """public dev.ultreon.quantum.client.util.RenderableArray(com.badlogic.gdx.utils.Array<? extends com.badlogic.gdx.graphics.g3d.Renderable>)"""
        val = __RenderableArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setSize(self, arg0: int) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.setSize(int)"""
        return List[object].__wrap(super(__utils.Array, self).setSize(__int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.indexOf(T,boolean)"""
        return int.__wrap(super(__utils.Array, self).indexOf(arg0, __boolean.valueOf(arg1)))

    @overload
    def removeValue(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.removeValue(T,boolean)"""
        return bool.__wrap(super(__utils.Array, self).removeValue(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def of(arg0: 'Class') -> 'utils.Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(java.lang.Class<T>)"""
        return utils.Array.__wrap(__Array.of(arg0))

    @overload
    def lastIndexOf(self, arg0: object, arg1: bool) -> int:
        """public int com.badlogic.gdx.utils.Array.lastIndexOf(T,boolean)"""
        return int.__wrap(super(__utils.Array, self).lastIndexOf(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def removeRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.removeRange(int,int)"""
        super(__utils.Array, self).removeRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.RenderableArray()"""
        val = __RenderableArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.notEmpty()"""
        return bool.__wrap(super(utils.Array, self).notEmpty())

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public dev.ultreon.quantum.client.util.RenderableArray(com.badlogic.gdx.graphics.g3d.Renderable[])"""
        val = __RenderableArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool, arg1: 'Renderable', arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.util.RenderableArray(boolean,com.badlogic.gdx.graphics.g3d.Renderable[],int,int)"""
        val = __RenderableArray(__boolean.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def of(arg0: bool, arg1: int, arg2: 'Class') -> 'utils.Array':
        """public static <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.utils.Array.of(boolean,int,java.lang.Class<T>)"""
        return utils.Array.__wrap(__Array.of(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def __init__(self, arg0: 'Class'):
        """public dev.ultreon.quantum.client.util.RenderableArray(java.lang.Class)"""
        val = __RenderableArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAll(self, *arg0: 'g3d.Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.addAll(com.badlogic.gdx.graphics.g3d.Renderable...)"""
        super(__RenderableArray, self).addAll(arg0)

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void com.badlogic.gdx.utils.Array.sort(java.util.Comparator<? super T>)"""
        super(__utils.Array, self).sort(arg0)

    @overload
    def containsAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__utils.Array, self).containsAll(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @staticmethod
    @overload
    def getGlobalSize() -> int:
        """public static int dev.ultreon.quantum.client.util.RenderableArray.getGlobalSize()"""
        return int.__wrap(__RenderableArray.getGlobalSize())

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public <V> V[] com.badlogic.gdx.utils.Array.toArray(java.lang.Class<V>)"""
        return List[object].__wrap(super(__utils.Array, self).toArray(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equalsIdentity(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equalsIdentity(java.lang.Object)"""
        return bool.__wrap(super(__utils.Array, self).equalsIdentity(arg0))

    @overload
    def containsAny(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.containsAny(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__utils.Array, self).containsAny(arg0, __boolean.valueOf(arg1)))

    @overload
    def contains(self, arg0: object, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.contains(T,boolean)"""
        return bool.__wrap(super(__utils.Array, self).contains(arg0, __boolean.valueOf(arg1)))

    @overload
    def setTranslation(self, arg0: 'Vector3'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.setTranslation(com.badlogic.gdx.math.Vector3)"""
        super(__RenderableArray, self).setTranslation(arg0)

    @override
    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.swap(int,int)"""
        super(__utils.Array, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Renderable', arg1: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.add(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__RenderableArray, self).add(arg0, arg1)

    @overload
    def selectRanked(self, arg0: 'Comparator', arg1: int) -> object:
        """public T com.badlogic.gdx.utils.Array.selectRanked(java.util.Comparator<T>,int)"""
        return object.__wrap(super(__utils.Array, self).selectRanked(arg0, __int.valueOf(arg1)))

    @overload
    def removeAll(self, arg0: 'Array', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.removeAll(com.badlogic.gdx.utils.Array<? extends T>,boolean)"""
        return bool.__wrap(super(__utils.Array, self).removeAll(arg0, __boolean.valueOf(arg1)))

    @overload
    def removeIndex(self, arg0: int) -> object:
        """public T com.badlogic.gdx.utils.Array.removeIndex(int)"""
        return object.__wrap(super(__utils.Array, self).removeIndex(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.Array.toString()"""
        return str.__wrap(super(utils.Array, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.utils.Array.equals(java.lang.Object)"""
        return bool.__wrap(super(__utils.Array, self).equals(arg0))

    @overload
    def add(self, arg0: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.add(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__RenderableArray, self).add(arg0)

    @override
    @overload
    def truncate(self, arg0: int):
        """public void com.badlogic.gdx.utils.Array.truncate(int)"""
        super(__utils.Array, self).truncate(__int.valueOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'Class'):
        """public dev.ultreon.quantum.client.util.RenderableArray(boolean,int,java.lang.Class)"""
        val = __RenderableArray(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def addAll(self, arg0: 'Array'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.addAll(com.badlogic.gdx.utils.Array<? extends com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__RenderableArray, self).addAll(arg0)

    @override
    @overload
    def insertRange(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.Array.insertRange(int,int)"""
        super(__utils.Array, self).insertRange(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.utils.Array.first()"""
        return object.__wrap(super(utils.Array, self).first())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.util.RenderableArray(int)"""
        val = __RenderableArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def insert(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.utils.Array.insert(int,T)"""
        super(__utils.Array, self).insert(__int.valueOf(arg0), arg1)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public T[] com.badlogic.gdx.utils.Array.toArray()"""
        return List[object].__wrap(super(utils.Array, self).toArray())

    @overload
    def add(self, arg0: 'Renderable', arg1: 'Renderable', arg2: 'Renderable', arg3: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.add(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__RenderableArray, self).add(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: 'Renderable', arg1: 'Renderable', arg2: 'Renderable'):
        """public void dev.ultreon.quantum.client.util.RenderableArray.add(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__RenderableArray, self).add(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.RenderableArray()"""
        val = __RenderableArray()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.util.DeferredDisposable
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import dev.ultreon.quantum.client.util.DeferredDisposable as __DeferredDisposable
__DeferredDisposable = __DeferredDisposable
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
 
class DeferredDisposable(ABC):
    """dev.ultreon.quantum.client.util.DeferredDisposable"""
 
    @staticmethod
    def __wrap(java_value: __DeferredDisposable) -> 'DeferredDisposable':
        return DeferredDisposable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeferredDisposable):
        """
        Dynamic initializer for DeferredDisposable.
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
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def deferDispose(self, arg0: 'Disposable'):
        """public abstract <T extends com.badlogic.gdx.utils.Disposable> T dev.ultreon.quantum.client.util.DeferredDisposable.deferDispose(T)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.util.UtilityClass
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.util.UtilityClass as __UtilityClass
__UtilityClass = __UtilityClass
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UtilityClass():
    """dev.ultreon.quantum.client.util.UtilityClass"""
 
    @staticmethod
    def __wrap(java_value: __UtilityClass) -> 'UtilityClass':
        return UtilityClass(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UtilityClass):
        """
        Dynamic initializer for UtilityClass.
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
 
 
# CLASS: dev.ultreon.quantum.client.util.InvalidThreadError
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.client.util.InvalidThreadError as __InvalidThreadError
__InvalidThreadError = __InvalidThreadError
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidThreadError():
    """dev.ultreon.quantum.client.util.InvalidThreadError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidThreadError) -> 'InvalidThreadError':
        return InvalidThreadError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidThreadError):
        """
        Dynamic initializer for InvalidThreadError.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.util.InvalidThreadError(java.lang.String)"""
        val = __InvalidThreadError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.client.util.Utils
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.util.function.Consumer as __Consumer
__Consumer = __Consumer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import java.lang.Runnable as Runnable
from builtins import object
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Runnable as __Runnable
__Runnable = __Runnable
import dev.ultreon.quantum.client.util.Utils as __Utils
__Utils = __Utils
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Utils():
    """dev.ultreon.quantum.client.util.Utils"""
 
    @staticmethod
    def __wrap(java_value: __Utils) -> 'Utils':
        return Utils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Utils):
        """
        Dynamic initializer for Utils.
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
    def normalizeToInt(arg0: int) -> int:
        """public static int dev.ultreon.quantum.client.util.Utils.normalizeToInt(byte)"""
        return int.__wrap(__Utils.normalizeToInt(__byte.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def with(arg0: object, arg1: 'BiConsumer') -> 'Consumer':
        """public static <R,T> java.util.function.Consumer<R> dev.ultreon.quantum.client.util.Utils.with(T,java.util.function.BiConsumer<R, T>)"""
        return Consumer.__wrap(__Utils.with(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.Utils()"""
        val = __Utils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.Utils()"""
        val = __Utils()
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

    @staticmethod
    @overload
    def with(arg0: object, arg1: 'Consumer') -> 'Runnable':
        """public static <T> java.lang.Runnable dev.ultreon.quantum.client.util.Utils.with(T,java.util.function.Consumer<T>)"""
        return Runnable.__wrap(__Utils.with(arg0, arg1))

    @staticmethod
    @overload
    def toCoreLibs(arg0: 'Vector3') -> 'vector.Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.client.util.Utils.toCoreLibs(com.badlogic.gdx.math.Vector3)"""
        return vector.Vec3d.__wrap(__Utils.toCoreLibs(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def make(arg0: 'Supplier') -> object:
        """public static <T> T dev.ultreon.quantum.client.util.Utils.make(java.util.function.Supplier<T>)"""
        return object.__wrap(__Utils.make(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def make(arg0: object, arg1: 'Consumer') -> object:
        """public static <T> T dev.ultreon.quantum.client.util.Utils.make(T,java.util.function.Consumer<T>)"""
        return object.__wrap(__Utils.make(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.util.DuplicateException
import dev.ultreon.quantum.client.util.DuplicateException as __DuplicateException
__DuplicateException = __DuplicateException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DuplicateException():
    """dev.ultreon.quantum.client.util.DuplicateException"""
 
    @staticmethod
    def __wrap(java_value: __DuplicateException) -> 'DuplicateException':
        return DuplicateException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DuplicateException):
        """
        Dynamic initializer for DuplicateException.
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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.util.DuplicateException(java.lang.String)"""
        val = __DuplicateException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.util.DuplicateException()"""
        val = __DuplicateException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.util.DuplicateException()"""
        val = __DuplicateException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.client.util.DuplicateException(java.lang.String,java.lang.Throwable)"""
        val = __DuplicateException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.client.util.DuplicateException(java.lang.Throwable)"""
        val = __DuplicateException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.client.util.Drawable
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.util.Drawable as __Drawable
__Drawable = __Drawable
 
class Drawable(ABC):
    """dev.ultreon.quantum.client.util.Drawable"""
 
    @staticmethod
    def __wrap(java_value: __Drawable) -> 'Drawable':
        return Drawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Drawable):
        """
        Dynamic initializer for Drawable.
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
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public abstract void dev.ultreon.quantum.client.util.Drawable.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.util.Resizer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
import dev.ultreon.quantum.client.util.Resizer as __Resizer
__Resizer = __Resizer
from builtins import float
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.util.Resizer as __Resizer_Orientation
__Orientation = __Resizer_Orientation.Orientation
from builtins import int
 
class Resizer():
    """dev.ultreon.quantum.client.util.Resizer"""
 
    @staticmethod
    def __wrap(java_value: __Resizer) -> 'Resizer':
        return Resizer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Resizer):
        """
        Dynamic initializer for Resizer.
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
    def getSourceWidth(self) -> float:
        """public float dev.ultreon.quantum.client.util.Resizer.getSourceWidth()"""
        return float.__wrap(super(Resizer, self).getSourceWidth())

    @overload
    def getSourceHeight(self) -> float:
        """public float dev.ultreon.quantum.client.util.Resizer.getSourceHeight()"""
        return float.__wrap(super(Resizer, self).getSourceHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.client.util.Resizer(float,float)"""
        val = __Resizer(__float.valueOf(arg0), __float.valueOf(arg1))
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

    @overload
    def thumbnail(self, arg0: float, arg1: float) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.client.util.Resizer.thumbnail(float,float)"""
        return 'vector.Vec2f'.__wrap(super(__Resizer, self).thumbnail(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getOrientation(self) -> 'Orientation':
        """public dev.ultreon.quantum.client.util.Resizer$Orientation dev.ultreon.quantum.client.util.Resizer.getOrientation()"""
        return 'Orientation'.__wrap(super(Resizer, self).getOrientation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRelativeRatio(self) -> float:
        """public float dev.ultreon.quantum.client.util.Resizer.getRelativeRatio()"""
        return float.__wrap(super(Resizer, self).getRelativeRatio())

    @overload
    def getRatio(self) -> float:
        """public float dev.ultreon.quantum.client.util.Resizer.getRatio()"""
        return float.__wrap(super(Resizer, self).getRatio())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.util.Named
import dev.ultreon.quantum.client.util.Named as __Named
__Named = __Named
from abc import abstractmethod, ABC
 
class Named(ABC):
    """dev.ultreon.quantum.client.util.Named"""
 
    @staticmethod
    def __wrap(java_value: __Named) -> 'Named':
        return Named(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Named):
        """
        Dynamic initializer for Named.
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
    def getName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.client.util.Named.getName()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.util.ExtKt
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.util.ExtKt as __ExtKt
__ExtKt = __ExtKt
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.util.Rot as __Rot
__Rot = __Rot
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ExtKt():
    """dev.ultreon.quantum.client.util.ExtKt"""
 
    @staticmethod
    def __wrap(java_value: __ExtKt) -> 'ExtKt':
        return ExtKt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExtKt):
        """
        Dynamic initializer for ExtKt.
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
    def deg(arg0: 'Number') -> 'Rot':
        """public static final dev.ultreon.quantum.client.util.Rot dev.ultreon.quantum.client.util.ExtKt.deg(java.lang.Number)"""
        return Rot.__wrap(__ExtKt.deg(arg0))

    @staticmethod
    @overload
    def rad(arg0: 'Number') -> 'Rot':
        """public static final dev.ultreon.quantum.client.util.Rot dev.ultreon.quantum.client.util.ExtKt.rad(java.lang.Number)"""
        return Rot.__wrap(__ExtKt.rad(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.util.TextureOffset
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import dev.ultreon.quantum.client.util.TextureOffset as __TextureOffset
__TextureOffset = __TextureOffset
from builtins import type
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class TextureOffset():
    """dev.ultreon.quantum.client.util.TextureOffset"""
 
    @staticmethod
    def __wrap(java_value: __TextureOffset) -> 'TextureOffset':
        return TextureOffset(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureOffset):
        """
        Dynamic initializer for TextureOffset.
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
    def textureHeight(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.textureHeight()"""
        return int.__wrap(super(TextureOffset, self).textureHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def textureWidth(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.textureWidth()"""
        return int.__wrap(super(TextureOffset, self).textureWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.util.TextureOffset.toString()"""
        return str.__wrap(super(TextureOffset, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def bake(self, arg0: 'Texture') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.util.TextureOffset.bake(com.badlogic.gdx.graphics.Texture)"""
        return 'g2d.TextureRegion'.__wrap(super(__TextureOffset, self).bake(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.util.TextureOffset.equals(java.lang.Object)"""
        return bool.__wrap(super(__TextureOffset, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.hashCode()"""
        return int.__wrap(super(TextureOffset, self).hashCode())

    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.v()"""
        return int.__wrap(super(TextureOffset, self).v())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public dev.ultreon.quantum.client.util.TextureOffset(int,int,int,int,int,int)"""
        val = __TextureOffset(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.util.TextureOffset(int,int,int,int)"""
        val = __TextureOffset(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.client.util.TextureOffset(int,int)"""
        val = __TextureOffset(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def blockUV(arg0: int, arg1: int) -> 'TextureOffset':
        """public static dev.ultreon.quantum.client.util.TextureOffset dev.ultreon.quantum.client.util.TextureOffset.blockUV(int,int)"""
        return TextureOffset.__wrap(__TextureOffset.blockUV(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.u()"""
        return int.__wrap(super(TextureOffset, self).u())

    @overload
    def uWidth(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.uWidth()"""
        return int.__wrap(super(TextureOffset, self).uWidth())

    @overload
    def vHeight(self) -> int:
        """public int dev.ultreon.quantum.client.util.TextureOffset.vHeight()"""
        return int.__wrap(super(TextureOffset, self).vHeight()) 
 
 
# CLASS: dev.ultreon.quantum.client.util.AxisAlignedBB
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import dev.ultreon.quantum.client.util.AxisAlignedBB as __AxisAlignedBB
__AxisAlignedBB = __AxisAlignedBB
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AxisAlignedBB():
    """dev.ultreon.quantum.client.util.AxisAlignedBB"""
 
    @staticmethod
    def __wrap(java_value: __AxisAlignedBB) -> 'AxisAlignedBB':
        return AxisAlignedBB(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AxisAlignedBB):
        """
        Dynamic initializer for AxisAlignedBB.
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
    def calculateIntersect(self, arg0: 'AxisAlignedBB', arg1: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.util.AxisAlignedBB.calculateIntersect(dev.ultreon.quantum.client.util.AxisAlignedBB,com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__AxisAlignedBB, self).calculateIntersect(arg0, arg1))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public dev.ultreon.quantum.client.util.AxisAlignedBB(float,float,float,float,float,float)"""
        val = __AxisAlignedBB(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def offset(self, arg0: float, arg1: float, arg2: float) -> 'AxisAlignedBB':
        """public dev.ultreon.quantum.client.util.AxisAlignedBB dev.ultreon.quantum.client.util.AxisAlignedBB.offset(float,float,float)"""
        return 'AxisAlignedBB'.__wrap(super(__AxisAlignedBB, self).offset(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

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
    def intersects(self, arg0: 'AxisAlignedBB') -> bool:
        """public boolean dev.ultreon.quantum.client.util.AxisAlignedBB.intersects(dev.ultreon.quantum.client.util.AxisAlignedBB)"""
        return bool.__wrap(super(__AxisAlignedBB, self).intersects(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def calculateIntersect(self, arg0: 'AxisAlignedBB', arg1: 'Vector3', arg2: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.util.AxisAlignedBB.calculateIntersect(dev.ultreon.quantum.client.util.AxisAlignedBB,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__AxisAlignedBB, self).calculateIntersect(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.util.Resizer$Orientation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
import dev.ultreon.quantum.client.util.Resizer as __Resizer_Orientation
__Orientation = __Resizer_Orientation.Orientation
from builtins import int
 
class Orientation():
    """dev.ultreon.quantum.client.util.Resizer.Orientation"""
 
    @staticmethod
    def __wrap(java_value: __Orientation) -> 'Orientation':
        return Orientation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Orientation):
        """
        Dynamic initializer for Orientation.
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
 
    # public static final dev.ultreon.quantum.client.util.Resizer$Orientation dev.ultreon.quantum.client.util.Resizer$Orientation.PORTRAIT
    PORTRAIT: 'Orientation' = __wrap(__Orientation.PORTRAIT)

    # public static final dev.ultreon.quantum.client.util.Resizer$Orientation dev.ultreon.quantum.client.util.Resizer$Orientation.LANDSCAPE
    LANDSCAPE: 'Orientation' = __wrap(__Orientation.LANDSCAPE)

    # public static final dev.ultreon.quantum.client.util.Resizer$Orientation dev.ultreon.quantum.client.util.Resizer$Orientation.SQUARE
    SQUARE: 'Orientation' = __wrap(__Orientation.SQUARE)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['Orientation']:
        """public static dev.ultreon.quantum.client.util.Resizer$Orientation[] dev.ultreon.quantum.client.util.Resizer$Orientation.values()"""
        return List[Orientation].__wrap(__Orientation.values())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Orientation':
        """public static dev.ultreon.quantum.client.util.Resizer$Orientation dev.ultreon.quantum.client.util.Resizer$Orientation.valueOf(java.lang.String)"""
        return Orientation.__wrap(__Orientation.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.client.util.Rot
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.util.Rot as __Rot
__Rot = __Rot
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Rot():
    """dev.ultreon.quantum.client.util.Rot"""
 
    @staticmethod
    def __wrap(java_value: __Rot) -> 'Rot':
        return Rot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rot):
        """
        Dynamic initializer for Rot.
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
    def getRadians(self) -> float:
        """public final float dev.ultreon.quantum.client.util.Rot.getRadians()"""
        return float.__wrap(super(Rot, self).getRadians())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def copy(self, arg0: float) -> 'Rot':
        """public final dev.ultreon.quantum.client.util.Rot dev.ultreon.quantum.client.util.Rot.copy(float)"""
        return 'Rot'.__wrap(super(__Rot, self).copy(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.util.Rot.equals(java.lang.Object)"""
        return bool.__wrap(super(__Rot, self).equals(arg0))

    @overload
    def component1(self) -> float:
        """public final float dev.ultreon.quantum.client.util.Rot.component1()"""
        return float.__wrap(super(Rot, self).component1())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.util.Rot.toString()"""
        return str.__wrap(super(Rot, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.util.Rot.hashCode()"""
        return int.__wrap(super(Rot, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getDegrees(self) -> float:
        """public final float dev.ultreon.quantum.client.util.Rot.getDegrees()"""
        return float.__wrap(super(Rot, self).getDegrees())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.quantum.client.util.Rot(float)"""
        val = __Rot(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.util.PlayerView
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.util.PlayerView as __PlayerView
__PlayerView = __PlayerView
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class PlayerView():
    """dev.ultreon.quantum.client.util.PlayerView"""
 
    @staticmethod
    def __wrap(java_value: __PlayerView) -> 'PlayerView':
        return PlayerView(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerView):
        """
        Dynamic initializer for PlayerView.
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
 
    # public static final dev.ultreon.quantum.client.util.PlayerView dev.ultreon.quantum.client.util.PlayerView.FIRST_PERSON
    FIRST_PERSON: 'PlayerView' = __wrap(__PlayerView.FIRST_PERSON)

    # public static final dev.ultreon.quantum.client.util.PlayerView dev.ultreon.quantum.client.util.PlayerView.THIRD_PERSON_FRONT
    THIRD_PERSON_FRONT: 'PlayerView' = __wrap(__PlayerView.THIRD_PERSON_FRONT)

    # public static final dev.ultreon.quantum.client.util.PlayerView dev.ultreon.quantum.client.util.PlayerView.THIRD_PERSON
    THIRD_PERSON: 'PlayerView' = __wrap(__PlayerView.THIRD_PERSON)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'PlayerView':
        """public static dev.ultreon.quantum.client.util.PlayerView dev.ultreon.quantum.client.util.PlayerView.valueOf(java.lang.String)"""
        return PlayerView.__wrap(__PlayerView.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['PlayerView']:
        """public static dev.ultreon.quantum.client.util.PlayerView[] dev.ultreon.quantum.client.util.PlayerView.values()"""
        return List[PlayerView].__wrap(__PlayerView.values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.client.util.GameRenderable
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.util.GameRenderable as __GameRenderable
__GameRenderable = __GameRenderable
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class GameRenderable(ABC):
    """dev.ultreon.quantum.client.util.GameRenderable"""
 
    @staticmethod
    def __wrap(java_value: __GameRenderable) -> 'GameRenderable':
        return GameRenderable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameRenderable):
        """
        Dynamic initializer for GameRenderable.
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
    def render(self, arg0: 'Renderer', arg1: float):
        """public abstract void dev.ultreon.quantum.client.util.GameRenderable.render(dev.ultreon.quantum.client.gui.Renderer,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.util.Renderable
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.util.Renderable as __Renderable
__Renderable = __Renderable
 
class Renderable(ABC):
    """dev.ultreon.quantum.client.util.Renderable"""
 
    @staticmethod
    def __wrap(java_value: __Renderable) -> 'Renderable':
        return Renderable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Renderable):
        """
        Dynamic initializer for Renderable.
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
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public abstract void dev.ultreon.quantum.client.util.Renderable.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        pass