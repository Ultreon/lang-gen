from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.util.Shutdownable as __Shutdownable
__Shutdownable = __Shutdownable
from abc import abstractmethod, ABC
 
class Shutdownable(ABC):
    """dev.ultreon.quantum.util.Shutdownable"""
 
    @staticmethod
    def __wrap(java_value: __Shutdownable) -> 'Shutdownable':
        return Shutdownable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Shutdownable):
        """
        Dynamic initializer for Shutdownable.
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
    def shutdown(self, ):
        """public abstract void dev.ultreon.quantum.util.Shutdownable.shutdown() throws java.lang.InterruptedException"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.util.Shutdownable
import dev.ultreon.quantum.util.Shutdownable as __Shutdownable
__Shutdownable = __Shutdownable
from abc import abstractmethod, ABC
 
class Shutdownable(ABC):
    """dev.ultreon.quantum.util.Shutdownable"""
 
    @staticmethod
    def __wrap(java_value: __Shutdownable) -> 'Shutdownable':
        return Shutdownable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Shutdownable):
        """
        Dynamic initializer for Shutdownable.
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
    def shutdown(self, ):
        """public abstract void dev.ultreon.quantum.util.Shutdownable.shutdown() throws java.lang.InterruptedException"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.util.Shutdownable 
 
 
# CLASS: dev.ultreon.quantum.util.DataSizes$Unit
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
import dev.ultreon.quantum.util.DataSizes as __DataSizes_Unit
__Unit = __DataSizes_Unit.Unit
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Unit(__Enum, Enum):
    """dev.ultreon.quantum.util.DataSizes.Unit"""
 
    @staticmethod
    def __wrap(java_value: __Unit) -> 'Unit':
        return Unit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Unit):
        """
        Dynamic initializer for Unit.
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
 
    # public static final dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.B
    B: 'Unit' = __wrap(__Unit.B)

    # public static final dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.GiB
    GiB: 'Unit' = __wrap(__Unit.GiB)

    # public static final dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.MiB
    MiB: 'Unit' = __wrap(__Unit.MiB)

    # public static final dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.KiB
    KiB: 'Unit' = __wrap(__Unit.KiB)

    # public static final dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.PiB
    PiB: 'Unit' = __wrap(__Unit.PiB)

    # public static final dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.TiB
    TiB: 'Unit' = __wrap(__Unit.TiB)

    # public static final dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.EiB
    EiB: 'Unit' = __wrap(__Unit.EiB)


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

    @staticmethod
    @overload
    def values() -> List['Unit']:
        """public static dev.ultreon.quantum.util.DataSizes$Unit[] dev.ultreon.quantum.util.DataSizes$Unit.values()"""
        return List[Unit].__wrap(__Unit.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Unit':
        """public static dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.valueOf(java.lang.String)"""
        return Unit.__wrap(__Unit.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.util.Color
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.util.Color as __Color
__Color = __Color
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
import java.lang.String as __String
__String = __String
from abc import abstractmethod, ABC
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

 
class Color(ABC):
    """dev.ultreon.quantum.util.Color"""
 
    @staticmethod
    def __wrap(java_value: __Color) -> 'Color':
        return Color(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Color):
        """
        Dynamic initializer for Color.
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
    def getRed(self, ):
        """public abstract int dev.ultreon.quantum.util.Color.getRed()"""
        pass

    @abstractmethod
    def getAlpha(self, ):
        """public abstract int dev.ultreon.quantum.util.Color.getAlpha()"""
        pass

    @overload
    def withRed(self, arg0: int) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withRed(int)"""
        return 'Color'.__wrap(super(__Color, self).withRed(__int.valueOf(arg0)))

    @overload
    def toGdx(self) -> 'graphics.Color':
        """public default com.badlogic.gdx.graphics.Color dev.ultreon.quantum.util.Color.toGdx()"""
        return 'graphics.Color'.__wrap(super(Color, self).toGdx())

    @overload
    def toHex(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.util.Color.toHex()"""
        return str.__wrap(super(Color, self).toHex())

    @overload
    def withBlue(self, arg0: int) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withBlue(int)"""
        return 'Color'.__wrap(super(__Color, self).withBlue(__int.valueOf(arg0)))

    @overload
    def withAlpha(self, arg0: int) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withAlpha(int)"""
        return 'Color'.__wrap(super(__Color, self).withAlpha(__int.valueOf(arg0)))

    @abstractmethod
    def getBlue(self, ):
        """public abstract int dev.ultreon.quantum.util.Color.getBlue()"""
        pass

    @overload
    def lighter(self) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.lighter()"""
        return 'Color'.__wrap(super(Color, self).lighter())

    @overload
    def darker(self) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.darker()"""
        return 'Color'.__wrap(super(Color, self).darker())

    @abstractmethod
    def getGreen(self, ):
        """public abstract int dev.ultreon.quantum.util.Color.getGreen()"""
        pass

    @overload
    def withGreen(self, arg0: int) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withGreen(int)"""
        return 'Color'.__wrap(super(__Color, self).withGreen(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def fromGdx(arg0: 'Color') -> 'Color':
        """public static dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.fromGdx(com.badlogic.gdx.graphics.Color)"""
        return Color.__wrap(__Color.fromGdx(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.Result
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.lang.Runnable as Runnable
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Result():
    """dev.ultreon.quantum.util.Result"""
 
    @staticmethod
    def __wrap(java_value: __Result) -> 'Result':
        return Result(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Result):
        """
        Dynamic initializer for Result.
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
    def flatMap(self, arg0: 'Function', arg1: 'Function') -> object:
        """public <R> R dev.ultreon.quantum.util.Result.flatMap(java.util.function.Function<T, R>,java.util.function.Function<java.lang.Throwable, R>)"""
        return object.__wrap(super(__Result, self).flatMap(arg0, arg1))

    @overload
    def getValueOrGet(self, arg0: 'Supplier') -> object:
        """public T dev.ultreon.quantum.util.Result.getValueOrGet(java.util.function.Supplier<? extends T>)"""
        return object.__wrap(super(__Result, self).getValueOrGet(arg0))

    @overload
    def unwrapFailure(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.unwrapFailure()"""
        return 'Throwable'.__wrap(super(Result, self).unwrapFailure())

    @overload
    def unwrap(self) -> object:
        """public T dev.ultreon.quantum.util.Result.unwrap()"""
        return object.__wrap(super(Result, self).unwrap())

    @overload
    def expect(self, arg0: str) -> object:
        """public T dev.ultreon.quantum.util.Result.expect(java.lang.String)"""
        return object.__wrap(super(__Result, self).expect(arg0))

    @overload
    def ifFailure(self, arg0: 'Consumer'):
        """public void dev.ultreon.quantum.util.Result.ifFailure(java.util.function.Consumer<java.lang.Throwable>)"""
        super(__Result, self).ifFailure(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def expectFailure(self, arg0: str) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.expectFailure(java.lang.String)"""
        return 'Throwable'.__wrap(super(__Result, self).expectFailure(arg0))

    @overload
    def getValueOrNull(self) -> object:
        """public T dev.ultreon.quantum.util.Result.getValueOrNull()"""
        return object.__wrap(super(Result, self).getValueOrNull())

    @overload
    def isOk(self) -> bool:
        """public boolean dev.ultreon.quantum.util.Result.isOk()"""
        return bool.__wrap(super(Result, self).isOk())

    @overload
    def unwrapOrGet(self, arg0: 'Supplier') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.unwrapOrGet(java.util.function.Supplier<? extends java.lang.Throwable>)"""
        return 'Throwable'.__wrap(super(__Result, self).unwrapOrGet(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ifValue(self, arg0: 'Consumer'):
        """public void dev.ultreon.quantum.util.Result.ifValue(java.util.function.Consumer<T>)"""
        super(__Result, self).ifValue(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def ok(arg0: object) -> 'Result':
        """public static <T> dev.ultreon.quantum.util.Result<T> dev.ultreon.quantum.util.Result.ok(T)"""
        return Result.__wrap(__Result.ok(arg0))

    @overload
    def getFailureOrNull(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.getFailureOrNull()"""
        return 'Throwable'.__wrap(super(Result, self).getFailureOrNull())

    @overload
    def getOk(self) -> object:
        """public T dev.ultreon.quantum.util.Result.getOk()"""
        return object.__wrap(super(Result, self).getOk())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getFailureOr(self, arg0: 'Throwable') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.getFailureOr(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Result, self).getFailureOr(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def failure(arg0: 'Throwable') -> 'Result':
        """public static <T> dev.ultreon.quantum.util.Result<T> dev.ultreon.quantum.util.Result.failure(java.lang.Throwable)"""
        return Result.__wrap(__Result.failure(arg0))

    @overload
    def map(self, arg0: 'Function', arg1: 'Function') -> 'Result':
        """public <R> dev.ultreon.quantum.util.Result<R> dev.ultreon.quantum.util.Result.map(java.util.function.Function<T, R>,java.util.function.Function<java.lang.Throwable, java.lang.Throwable>)"""
        return 'Result'.__wrap(super(__Result, self).map(arg0, arg1))

    @overload
    def getFailure(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.getFailure()"""
        return 'Throwable'.__wrap(super(Result, self).getFailure())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isFailure(self) -> bool:
        """public boolean dev.ultreon.quantum.util.Result.isFailure()"""
        return bool.__wrap(super(Result, self).isFailure())

    @overload
    def getFailureOrGet(self, arg0: 'Supplier') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.getFailureOrGet(java.util.function.Supplier<? extends java.lang.Throwable>)"""
        return 'Throwable'.__wrap(super(__Result, self).getFailureOrGet(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def unwrapOr(self, arg0: object) -> object:
        """public T dev.ultreon.quantum.util.Result.unwrapOr(T)"""
        return object.__wrap(super(__Result, self).unwrapOr(arg0))

    @overload
    def ifValueOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.quantum.util.Result.ifValueOrElse(java.util.function.Consumer<T>,java.lang.Runnable)"""
        super(__Result, self).ifValueOrElse(arg0, arg1)

    @overload
    def ifAny(self, arg0: 'Consumer', arg1: 'Consumer'):
        """public void dev.ultreon.quantum.util.Result.ifAny(java.util.function.Consumer<T>,java.util.function.Consumer<java.lang.Throwable>)"""
        super(__Result, self).ifAny(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ok() -> 'Result':
        """public static dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.util.Result.ok()"""
        return Result.__wrap(__Result.ok())

    @overload
    def ifFailureOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.quantum.util.Result.ifFailureOrElse(java.util.function.Consumer<java.lang.Throwable>,java.lang.Runnable)"""
        super(__Result, self).ifFailureOrElse(arg0, arg1)

    @overload
    def getValueOr(self, arg0: object) -> object:
        """public T dev.ultreon.quantum.util.Result.getValueOr(T)"""
        return object.__wrap(super(__Result, self).getValueOr(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.Task
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
from builtins import object
import dev.ultreon.quantum.util.Task as __Task
__Task = __Task
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Task(__Runnable, Runnable):
    """dev.ultreon.quantum.util.Task"""
 
    @staticmethod
    def __wrap(java_value: __Task) -> 'Task':
        return Task(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Task):
        """
        Dynamic initializer for Task.
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
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.util.Task(dev.ultreon.quantum.util.Identifier)"""
        val = __Task(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Runnable'):
        """public dev.ultreon.quantum.util.Task(dev.ultreon.quantum.util.Identifier,java.lang.Runnable)"""
        val = __Task(arg0, arg1)
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

    @overload
    def id(self) -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Task.id()"""
        return 'Identifier'.__wrap(super(Task, self).id())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def run(self):
        """public void dev.ultreon.quantum.util.Task.run()"""
        super(Task, self).run()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Supplier'):
        """public dev.ultreon.quantum.util.Task(dev.ultreon.quantum.util.Identifier,java.util.function.Supplier<T>)"""
        val = __Task(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.util.Task.get()"""
        return object.__wrap(super(Task, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.BoundingBox
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
from builtins import float
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import java.util.List as List
from builtins import int
 
class BoundingBox(__Serializable, Serializable):
    """dev.ultreon.quantum.util.BoundingBox"""
 
    @staticmethod
    def __wrap(java_value: __BoundingBox) -> 'BoundingBox':
        return BoundingBox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundingBox):
        """
        Dynamic initializer for BoundingBox.
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
    def set(self, arg0: 'List') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.set(java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d>)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def ext(self, arg0: 'Vec3d') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.ext(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def ext(self, arg0: float, arg1: float, arg2: float) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.ext(double,double,double)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Vec3d', arg1: 'Vec3d') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.set(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0, arg1))

    @overload
    def __init__(self, arg0: 'BoundingBox'):
        """public dev.ultreon.quantum.util.BoundingBox(dev.ultreon.quantum.util.BoundingBox)"""
        val = __BoundingBox(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getMax(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getMax(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getMax(arg0))

    @overload
    def getDepth(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getDepth()"""
        return float.__wrap(super(BoundingBox, self).getDepth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getDimensions(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getDimensions(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getDimensions(arg0))

    @overload
    def getCorner001(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner001(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCorner001(arg0))

    @overload
    def getCenterZ(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getCenterZ()"""
        return float.__wrap(super(BoundingBox, self).getCenterZ())

    @overload
    def getCorner000(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner000(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCorner000(arg0))

    @overload
    def getCorner101(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner101(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCorner101(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.BoundingBox()"""
        val = __BoundingBox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clr(self) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.clr()"""
        return 'BoundingBox'.__wrap(super(BoundingBox, self).clr())

    @overload
    def getCorner100(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner100(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCorner100(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def contains(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.contains(dev.ultreon.quantum.util.BoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).contains(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public dev.ultreon.quantum.util.BoundingBox(double,double,double,double,double,double)"""
        val = __BoundingBox(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4), __double.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getWidth(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getWidth()"""
        return float.__wrap(super(BoundingBox, self).getWidth())

    @overload
    def intersectsExclusive(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.intersectsExclusive(dev.ultreon.quantum.util.BoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).intersectsExclusive(arg0))

    @overload
    def inf(self) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.inf()"""
        return 'BoundingBox'.__wrap(super(BoundingBox, self).inf())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.BoundingBox()"""
        val = __BoundingBox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def intersects(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.intersects(dev.ultreon.quantum.util.BoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).intersects(arg0))

    @overload
    def __init__(self, arg0: 'Vec3d', arg1: 'Vec3d'):
        """public dev.ultreon.quantum.util.BoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = __BoundingBox(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCorner111(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner111(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCorner111(arg0))

    @overload
    def ext(self, arg0: 'Vec3d', arg1: float) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.ext(dev.ultreon.libs.commons.v0.vector.Vec3d,double)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0, __double.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getMin(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getMin(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getMin(arg0))

    @overload
    def getCorner011(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner011(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCorner011(arg0))

    @overload
    def ext(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.ext(dev.ultreon.quantum.util.BoundingBox)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0))

    @overload
    def getCenter(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCenter(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCenter(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.BoundingBox.toString()"""
        return str.__wrap(super(BoundingBox, self).toString())

    @overload
    def updateByDelta(self, arg0: float, arg1: float, arg2: float) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.updateByDelta(double,double,double)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).updateByDelta(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def getCorner010(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner010(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCorner010(arg0))

    @overload
    def getCenterY(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getCenterY()"""
        return float.__wrap(super(BoundingBox, self).getCenterY())

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
    def isValid(self) -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.isValid()"""
        return bool.__wrap(super(BoundingBox, self).isValid())

    @overload
    def getCorner110(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner110(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'.__wrap(super(__BoundingBox, self).getCorner110(arg0))

    @overload
    def update(self):
        """public void dev.ultreon.quantum.util.BoundingBox.update()"""
        super(BoundingBox, self).update()

    @overload
    def contains(self, arg0: 'Vec3d') -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.contains(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return bool.__wrap(super(__BoundingBox, self).contains(arg0))

    @overload
    def set(self, arg0: 'Vec3d') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.set(dev.ultreon.libs.commons.v0.vector.Vec3d[])"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def getCenterX(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getCenterX()"""
        return float.__wrap(super(BoundingBox, self).getCenterX())

    @overload
    def set(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.set(dev.ultreon.quantum.util.BoundingBox)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def getHeight(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getHeight()"""
        return float.__wrap(super(BoundingBox, self).getHeight()) 
 
 
# CLASS: dev.ultreon.quantum.util.RandomValueSource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.quantum.util.RandomValueSource as __RandomValueSource
__RandomValueSource = __RandomValueSource
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import java.util.Random as Random
from builtins import int
 
class RandomValueSource(__ValueSource, ValueSource):
    """dev.ultreon.quantum.util.RandomValueSource"""
 
    @staticmethod
    def __wrap(java_value: __RandomValueSource) -> 'RandomValueSource':
        return RandomValueSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RandomValueSource):
        """
        Dynamic initializer for RandomValueSource.
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
    def getValue(self) -> float:
        """public double dev.ultreon.quantum.util.RandomValueSource.getValue()"""
        return float.__wrap(super(RandomValueSource, self).getValue())

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

    @staticmethod
    @overload
    def of(arg0: 'Random', arg1: float, arg2: float) -> 'RandomValueSource':
        """public static dev.ultreon.quantum.util.RandomValueSource dev.ultreon.quantum.util.RandomValueSource.of(java.util.Random,double,double)"""
        return RandomValueSource.__wrap(__RandomValueSource.of(arg0, __double.valueOf(arg1), __double.valueOf(arg2)))

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
 
 
# CLASS: dev.ultreon.quantum.util.IllegalThreadError
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
import dev.ultreon.quantum.util.IllegalThreadError as __IllegalThreadError
__IllegalThreadError = __IllegalThreadError
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IllegalThreadError(__Error, Error):
    """dev.ultreon.quantum.util.IllegalThreadError"""
 
    @staticmethod
    def __wrap(java_value: __IllegalThreadError) -> 'IllegalThreadError':
        return IllegalThreadError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IllegalThreadError):
        """
        Dynamic initializer for IllegalThreadError.
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
    def __init__(self):
        """public dev.ultreon.quantum.util.IllegalThreadError()"""
        val = __IllegalThreadError()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.IllegalThreadError()"""
        val = __IllegalThreadError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.IllegalThreadError(java.lang.String)"""
        val = __IllegalThreadError(arg0)
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.util.Env
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.util.Env as __Env
__Env = __Env
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
 
class Env(__Enum, Enum):
    """dev.ultreon.quantum.util.Env"""
 
    @staticmethod
    def __wrap(java_value: __Env) -> 'Env':
        return Env(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Env):
        """
        Dynamic initializer for Env.
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
 
    # public static final dev.ultreon.quantum.util.Env dev.ultreon.quantum.util.Env.CLIENT
    CLIENT: 'Env' = __wrap(__Env.CLIENT)

    # public static final dev.ultreon.quantum.util.Env dev.ultreon.quantum.util.Env.SERVER
    SERVER: 'Env' = __wrap(__Env.SERVER)


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

    @staticmethod
    @overload
    def values() -> List['Env']:
        """public static dev.ultreon.quantum.util.Env[] dev.ultreon.quantum.util.Env.values()"""
        return List[Env].__wrap(__Env.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Env':
        """public static dev.ultreon.quantum.util.Env dev.ultreon.quantum.util.Env.valueOf(java.lang.String)"""
        return Env.__wrap(__Env.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.util.PagedList
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
from builtins import type
import dev.ultreon.quantum.util.PagedList as __PagedList
__PagedList = __PagedList
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class PagedList(__ArrayList, ArrayList):
    """dev.ultreon.quantum.util.PagedList"""
 
    @staticmethod
    def __wrap(java_value: __PagedList) -> 'PagedList':
        return PagedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PagedList):
        """
        Dynamic initializer for PagedList.
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
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object.__wrap(super(__ArrayList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool.__wrap(super(ArrayList, self).isEmpty())

    @overload
    def get(self, arg0: int, arg1: int) -> object:
        """public T dev.ultreon.quantum.util.PagedList.get(int,int)"""
        return object.__wrap(super(__PagedList, self).get(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'.__wrap(super(__ArrayList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'.__wrap(super(ArrayList, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ArrayList, self).retainAll(arg0))

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(__ArrayList, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool.__wrap(super(__ArrayList, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(__ArrayList, self).sort(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object].__wrap(super(__ArrayList, self).toArray(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object.__wrap(super(__ArrayList, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object.__wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object].__wrap(super(ArrayList, self).toArray())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__ArrayList, self).removeIf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'.__wrap(super(ArrayList, self).spliterator())

    @overload
    def __init__(self, arg0: int, arg1: 'Collection'):
        """public dev.ultreon.quantum.util.PagedList(int,java.util.Collection<? extends T>)"""
        val = __PagedList(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int.__wrap(super(ArrayList, self).size())

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(__ArrayList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object.__wrap(super(ArrayList, self).clone())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__ArrayList, self).indexOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'PagedList'):
        """public dev.ultreon.quantum.util.PagedList(dev.ultreon.quantum.util.PagedList<? extends T>)"""
        val = __PagedList(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__ArrayList, self).listIterator(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.util.PagedList(int)"""
        val = __PagedList(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object.__wrap(super(__ArrayList, self).get(__int.valueOf(arg0)))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ArrayList, self).removeAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ArrayList, self).addAll(arg0))

    @overload
    def getFullPage(self, arg0: int) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.util.PagedList.getFullPage(int)"""
        return 'List'.__wrap(super(__PagedList, self).getFullPage(__int.valueOf(arg0)))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(__ArrayList, self).addFirst(arg0)

    @override
    @overload
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object.__wrap(super(ArrayList, self).removeLast())

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object.__wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int.__wrap(super(ArrayList, self).hashCode())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).contains(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ArrayList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object.__wrap(super(ArrayList, self).getLast())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.util.PagedList(int,int)"""
        val = __PagedList(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).remove(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(__ArrayList, self).addLast(arg0)

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).equals(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__ArrayList, self).lastIndexOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(__ArrayList, self).forEach(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'.__wrap(super(ArrayList, self).listIterator()) 
 
 
# CLASS: dev.ultreon.quantum.util.Hashing
import dev.ultreon.quantum.util.Hashing as __Hashing
__Hashing = __Hashing
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from typing import List
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
 
class Hashing():
    """dev.ultreon.quantum.util.Hashing"""
 
    @staticmethod
    def __wrap(java_value: __Hashing) -> 'Hashing':
        return Hashing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Hashing):
        """
        Dynamic initializer for Hashing.
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

    @staticmethod
    @overload
    def hashMD5(arg0: bytes) -> List[int]:
        """public static byte[] dev.ultreon.quantum.util.Hashing.hashMD5(byte[])"""
        return List[int].__wrap(__Hashing.hashMD5(bytes))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.Hashing()"""
        val = __Hashing()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.Hashing()"""
        val = __Hashing()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def verifyMD5(arg0: bytes, arg1: bytes) -> bool:
        """public static boolean dev.ultreon.quantum.util.Hashing.verifyMD5(byte[],byte[])"""
        return bool.__wrap(__Hashing.verifyMD5(bytes, bytes))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.WorldRayCaster
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.util.WorldRayCaster as __WorldRayCaster
__WorldRayCaster = __WorldRayCaster
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.util.BlockHitResult as __BlockHitResult
__BlockHitResult = __BlockHitResult
import java.lang.Object as __object
from builtins import type
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
 
class WorldRayCaster():
    """dev.ultreon.quantum.util.WorldRayCaster"""
 
    @staticmethod
    def __wrap(java_value: __WorldRayCaster) -> 'WorldRayCaster':
        return WorldRayCaster(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldRayCaster):
        """
        Dynamic initializer for WorldRayCaster.
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
    def __init__(self):
        """public dev.ultreon.quantum.util.WorldRayCaster()"""
        val = __WorldRayCaster()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.WorldRayCaster()"""
        val = __WorldRayCaster()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def rayCast(arg0: 'BlockHitResult', arg1: 'World', arg2: 'BlockMetaPredicate') -> 'BlockHitResult':
        """public static dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.util.WorldRayCaster.rayCast(dev.ultreon.quantum.util.BlockHitResult,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return BlockHitResult.__wrap(__WorldRayCaster.rayCast(arg0, arg1, arg2))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def rayCast(arg0: 'World') -> 'BlockHitResult':
        """public static dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.util.WorldRayCaster.rayCast(dev.ultreon.quantum.world.World)"""
        return BlockHitResult.__wrap(__WorldRayCaster.rayCast(arg0))

    @staticmethod
    @overload
    def rayCast(arg0: 'BlockHitResult', arg1: 'World') -> 'BlockHitResult':
        """public static dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.util.WorldRayCaster.rayCast(dev.ultreon.quantum.util.BlockHitResult,dev.ultreon.quantum.world.World)"""
        return BlockHitResult.__wrap(__WorldRayCaster.rayCast(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.HexTable
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.util.HexTable as __HexTable
__HexTable = __HexTable
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HexTable():
    """dev.ultreon.quantum.util.HexTable"""
 
    @staticmethod
    def __wrap(java_value: __HexTable) -> 'HexTable':
        return HexTable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HexTable):
        """
        Dynamic initializer for HexTable.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.HexTable()"""
        val = __HexTable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def dumpHexTable(arg0: bytes):
        """public static void dev.ultreon.quantum.util.HexTable.dumpHexTable(byte[])"""
        __HexTable.dumpHexTable(bytes)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.HexTable()"""
        val = __HexTable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.MathHelper
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.util.MathHelper as __MathHelper
__MathHelper = __MathHelper
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

from typing import List
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

import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MathHelper():
    """dev.ultreon.quantum.util.MathHelper"""
 
    @staticmethod
    def __wrap(java_value: __MathHelper) -> 'MathHelper':
        return MathHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MathHelper):
        """
        Dynamic initializer for MathHelper.
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
    def rotateY(arg0: 'float', arg1: float, arg2: 'Vector3'):
        """public static void dev.ultreon.quantum.util.MathHelper.rotateY(float[],float,com.badlogic.gdx.math.Vector3)"""
        __MathHelper.rotateY(arg0, __float.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.quantum.util.MathHelper.lerp(double,double,double)"""
        return float.__wrap(__MathHelper.lerp(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.MathHelper()"""
        val = __MathHelper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def rotate(arg0: 'float', arg1: 'Vector3', arg2: 'Axis') -> List[float]:
        """public static float[] dev.ultreon.quantum.util.MathHelper.rotate(float[],com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.util.Axis)"""
        return List[float].__wrap(__MathHelper.rotate(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.MathHelper()"""
        val = __MathHelper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def round(arg0: 'Vec2f') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.util.MathHelper.round(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return vector.Vec2i.__wrap(__MathHelper.round(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float dev.ultreon.quantum.util.MathHelper.lerp(float,float,float)"""
        return float.__wrap(__MathHelper.lerp(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

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
    def rotateZ(arg0: 'float', arg1: float, arg2: 'Vector3'):
        """public static void dev.ultreon.quantum.util.MathHelper.rotateZ(float[],float,com.badlogic.gdx.math.Vector3)"""
        __MathHelper.rotateZ(arg0, __float.valueOf(arg1), arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def rotateX(arg0: 'float', arg1: float, arg2: 'Vector3'):
        """public static void dev.ultreon.quantum.util.MathHelper.rotateX(float[],float,com.badlogic.gdx.math.Vector3)"""
        __MathHelper.rotateX(arg0, __float.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def round(arg0: 'Vec3f') -> 'vector.Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.MathHelper.round(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return vector.Vec3i.__wrap(__MathHelper.round(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def round(arg0: 'Vec2d') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.util.MathHelper.round(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return vector.Vec2i.__wrap(__MathHelper.round(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.Suppliers
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.util.Suppliers as __Suppliers
__Suppliers = __Suppliers
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Supplier as __Supplier
__Supplier = __Supplier
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Suppliers():
    """dev.ultreon.quantum.util.Suppliers"""
 
    @staticmethod
    def __wrap(java_value: __Suppliers) -> 'Suppliers':
        return Suppliers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Suppliers):
        """
        Dynamic initializer for Suppliers.
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
    def memoizeWithExpiration(arg0: 'Supplier', arg1: int, arg2: 'TimeUnit') -> 'Supplier':
        """public static <T> java.util.function.Supplier<T> dev.ultreon.quantum.util.Suppliers.memoizeWithExpiration(java.util.function.Supplier<T>,int,java.util.concurrent.TimeUnit)"""
        return Supplier.__wrap(__Suppliers.memoizeWithExpiration(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def memoize(arg0: 'Supplier') -> 'Supplier':
        """public static <T> java.util.function.Supplier<T> dev.ultreon.quantum.util.Suppliers.memoize(java.util.function.Supplier<T>)"""
        return Supplier.__wrap(__Suppliers.memoize(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.Numbers
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Long as Long
from pyquantum_helper import override
import java.lang.Short as Short
import java.lang.Object as __object
from builtins import type
import java.lang.Float as Float
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import java.lang.Byte as Byte
import dev.ultreon.quantum.util.Numbers as __Numbers
__Numbers = __Numbers
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Double as Double
from builtins import int
 
class Numbers():
    """dev.ultreon.quantum.util.Numbers"""
 
    @staticmethod
    def __wrap(java_value: __Numbers) -> 'Numbers':
        return Numbers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Numbers):
        """
        Dynamic initializer for Numbers.
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
    def toBooleanOrNull(arg0: str) -> 'Boolean':
        """public static java.lang.Boolean dev.ultreon.quantum.util.Numbers.toBooleanOrNull(java.lang.String)"""
        return Boolean.__wrap(__Numbers.toBooleanOrNull(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toByteOrNull(toByteOrNull) -> 'Byte':
        """public static java.lang.Byte dev.ultreon.quantum.util.Numbers.toByteOrNull(java.lang.String)"""
        return __transform(__arg0.Numbers(arg0: str)).'Byte'Value()

    @staticmethod
    @overload
    def toFloatOrNull(toFloatOrNull) -> 'Float':
        """public static java.lang.Float dev.ultreon.quantum.util.Numbers.toFloatOrNull(java.lang.String)"""
        return __transform(__arg0.Numbers(arg0: str)).'Float'Value()

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toDoubleOrNull(toDoubleOrNull) -> 'Double':
        """public static java.lang.Double dev.ultreon.quantum.util.Numbers.toDoubleOrNull(java.lang.String)"""
        return __transform(__arg0.Numbers(arg0: str)).'Double'Value()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.Numbers()"""
        val = __Numbers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toIntOrNull(toIntOrNull) -> 'Integer':
        """public static java.lang.Integer dev.ultreon.quantum.util.Numbers.toIntOrNull(java.lang.String)"""
        return __transform(__arg0.Numbers(arg0: str)).'Integer'Value()

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

    @staticmethod
    @overload
    def toShortOrNull(toShortOrNull) -> 'Short':
        """public static java.lang.Short dev.ultreon.quantum.util.Numbers.toShortOrNull(java.lang.String)"""
        return __transform(__arg0.Numbers(arg0: str)).'Short'Value()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.Numbers()"""
        val = __Numbers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def toLongOrNull(toLongOrNull) -> 'Long':
        """public static java.lang.Long dev.ultreon.quantum.util.Numbers.toLongOrNull(java.lang.String)"""
        return __transform(__arg0.Numbers(arg0: str)).'Long'Value() 
 
 
# CLASS: dev.ultreon.quantum.util.ArgParser
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.util.ArgParser as __ArgParser
__ArgParser = __ArgParser
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
import java.util.List as List
from builtins import int
 
class ArgParser():
    """dev.ultreon.quantum.util.ArgParser"""
 
    @staticmethod
    def __wrap(java_value: __ArgParser) -> 'ArgParser':
        return ArgParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArgParser):
        """
        Dynamic initializer for ArgParser.
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
    def __init__(self, *arg0: str):
        """public dev.ultreon.quantum.util.ArgParser(java.lang.String...)"""
        val = __ArgParser(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getKeywordArgs(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> dev.ultreon.quantum.util.ArgParser.getKeywordArgs()"""
        return 'Map'.__wrap(super(ArgParser, self).getKeywordArgs())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getFlags(self) -> 'Set':
        """public java.util.Set<java.lang.String> dev.ultreon.quantum.util.ArgParser.getFlags()"""
        return 'Set'.__wrap(super(ArgParser, self).getFlags())

    @overload
    def getArgv(self) -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.util.ArgParser.getArgv()"""
        return 'List'.__wrap(super(ArgParser, self).getArgv())

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
    def getArgs(self) -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.util.ArgParser.getArgs()"""
        return 'List'.__wrap(super(ArgParser, self).getArgs())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.RgbColor
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.util.Color as __Color
__Color = __Color
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class RgbColor(__Color, Color):
    """dev.ultreon.quantum.util.RgbColor"""
 
    @staticmethod
    def __wrap(java_value: __RgbColor) -> 'RgbColor':
        return RgbColor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RgbColor):
        """
        Dynamic initializer for RgbColor.
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
 
    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.PURPLE
    PURPLE: 'RgbColor' = __wrap(__RgbColor.PURPLE)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.BLACK
    BLACK: 'RgbColor' = __wrap(__RgbColor.BLACK)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.WHITE
    WHITE: 'RgbColor' = __wrap(__RgbColor.WHITE)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.GOLD
    GOLD: 'RgbColor' = __wrap(__RgbColor.GOLD)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.BLUE
    BLUE: 'RgbColor' = __wrap(__RgbColor.BLUE)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.DARK_GRAY
    DARK_GRAY: 'RgbColor' = __wrap(__RgbColor.DARK_GRAY)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.RED
    RED: 'RgbColor' = __wrap(__RgbColor.RED)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.YELLOW
    YELLOW: 'RgbColor' = __wrap(__RgbColor.YELLOW)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.AZURE
    AZURE: 'RgbColor' = __wrap(__RgbColor.AZURE)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.ROSE
    ROSE: 'RgbColor' = __wrap(__RgbColor.ROSE)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.LIGHT_GRAY
    LIGHT_GRAY: 'RgbColor' = __wrap(__RgbColor.LIGHT_GRAY)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.ORANGE
    ORANGE: 'RgbColor' = __wrap(__RgbColor.ORANGE)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.MAGENTA
    MAGENTA: 'RgbColor' = __wrap(__RgbColor.MAGENTA)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.GRAY
    GRAY: 'RgbColor' = __wrap(__RgbColor.GRAY)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.GREEN
    GREEN: 'RgbColor' = __wrap(__RgbColor.GREEN)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.MINT
    MINT: 'RgbColor' = __wrap(__RgbColor.MINT)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.CYAN
    CYAN: 'RgbColor' = __wrap(__RgbColor.CYAN)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.TRANSPARENT
    TRANSPARENT: 'RgbColor' = __wrap(__RgbColor.TRANSPARENT)

    # public static final dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.YELLOW_GREEN
    YELLOW_GREEN: 'RgbColor' = __wrap(__RgbColor.YELLOW_GREEN)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getGreen(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getGreen()"""
        return int.__wrap(super(RgbColor, self).getGreen())

    @staticmethod
    @overload
    def of(arg0: 'ColorCode') -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.of(dev.ultreon.quantum.text.ColorCode)"""
        return RgbColor.__wrap(__RgbColor.of(arg0))

    @overload
    def getRgb(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getRgb()"""
        return int.__wrap(super(RgbColor, self).getRgb())

    @staticmethod
    @overload
    def rgb(arg0: float, arg1: float, arg2: float) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgb(float,float,float)"""
        return RgbColor.__wrap(__RgbColor.rgb(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRed(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getRed()"""
        return int.__wrap(super(RgbColor, self).getRed())

    @overload
    def withGreen(self, arg0: int) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.withGreen(int)"""
        return 'RgbColor'.__wrap(super(__RgbColor, self).withGreen(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def bgra(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.bgra(int)"""
        return RgbColor.__wrap(__RgbColor.bgra(__int.valueOf(arg0)))

    @override
    @overload
    def toHex(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.util.Color.toHex()"""
        return str.__wrap(super(Color, self).toHex())

    @staticmethod
    @overload
    def rgb(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgb(int)"""
        return RgbColor.__wrap(__RgbColor.rgb(__int.valueOf(arg0)))

    @overload
    def getTransparency(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getTransparency()"""
        return int.__wrap(super(RgbColor, self).getTransparency())

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
    def abgr(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.abgr(int)"""
        return RgbColor.__wrap(__RgbColor.abgr(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def rgba(arg0: float, arg1: float, arg2: float, arg3: float) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgba(float,float,float,float)"""
        return RgbColor.__wrap(__RgbColor.rgba(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def hsb(arg0: float, arg1: float, arg2: float) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.hsb(float,float,float)"""
        return RgbColor.__wrap(__RgbColor.hsb(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def argb(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.argb(int)"""
        return RgbColor.__wrap(__RgbColor.argb(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def rgba(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgba(int)"""
        return RgbColor.__wrap(__RgbColor.rgba(__int.valueOf(arg0)))

    @overload
    def withBlue(self, arg0: int) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.withBlue(int)"""
        return 'RgbColor'.__wrap(super(__RgbColor, self).withBlue(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def rgb(arg0: int, arg1: int, arg2: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgb(int,int,int)"""
        return RgbColor.__wrap(__RgbColor.rgb(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def darker(self) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.darker()"""
        return 'RgbColor'.__wrap(super(RgbColor, self).darker())

    @override
    @overload
    def getAlpha(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getAlpha()"""
        return int.__wrap(super(RgbColor, self).getAlpha())

    @override
    @overload
    def lighter(self) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.lighter()"""
        return 'Color'.__wrap(super(Color, self).lighter())

    @override
    @overload
    def toGdx(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color dev.ultreon.quantum.util.RgbColor.toGdx()"""
        return 'graphics.Color'.__wrap(super(RgbColor, self).toGdx())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.quantum.util.RgbColor(float,float,float,float)"""
        val = __RgbColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def brighter(self) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.brighter()"""
        return 'RgbColor'.__wrap(super(RgbColor, self).brighter())

    @override
    @overload
    def getBlue(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getBlue()"""
        return int.__wrap(super(RgbColor, self).getBlue())

    @overload
    def withRed(self, arg0: int) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.withRed(int)"""
        return 'RgbColor'.__wrap(super(__RgbColor, self).withRed(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def bgr(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.bgr(int)"""
        return RgbColor.__wrap(__RgbColor.bgr(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def gdx(arg0: 'Color') -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.gdx(com.badlogic.gdx.graphics.Color)"""
        return RgbColor.__wrap(__RgbColor.gdx(arg0))

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
    def withAlpha(self, arg0: int) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.withAlpha(int)"""
        return 'RgbColor'.__wrap(super(__RgbColor, self).withAlpha(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def rgba(arg0: int, arg1: int, arg2: int, arg3: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgba(int,int,int,int)"""
        return RgbColor.__wrap(__RgbColor.rgba(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def hex(arg0: str) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.hex(java.lang.String)"""
        return RgbColor.__wrap(__RgbColor.hex(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.RgbColor.toString()"""
        return str.__wrap(super(RgbColor, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.util.Intersector
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Intersector as __Intersector
__Intersector = __Intersector
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Intersector():
    """dev.ultreon.quantum.util.Intersector"""
 
    @staticmethod
    def __wrap(java_value: __Intersector) -> 'Intersector':
        return Intersector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Intersector):
        """
        Dynamic initializer for Intersector.
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

    @staticmethod
    @overload
    def intersectRayBounds(arg0: 'Ray', arg1: 'BoundingBox', arg2: 'Vec3d') -> bool:
        """public static boolean dev.ultreon.quantum.util.Intersector.intersectRayBounds(dev.ultreon.quantum.util.Ray,dev.ultreon.quantum.util.BoundingBox,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return bool.__wrap(__Intersector.intersectRayBounds(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.Intersector()"""
        val = __Intersector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public dev.ultreon.quantum.util.Intersector()"""
        val = __Intersector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.Copyable
import dev.ultreon.quantum.util.Copyable as __Copyable
__Copyable = __Copyable
from abc import abstractmethod, ABC
 
class Copyable(ABC):
    """dev.ultreon.quantum.util.Copyable"""
 
    @staticmethod
    def __wrap(java_value: __Copyable) -> 'Copyable':
        return Copyable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Copyable):
        """
        Dynamic initializer for Copyable.
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
    def cpy(self, ):
        """public abstract T dev.ultreon.quantum.util.Copyable.cpy()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.util.BoundingBoxUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.quantum.util.BoundingBoxUtils as __BoundingBoxUtils
__BoundingBoxUtils = __BoundingBoxUtils
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
from builtins import int
 
class BoundingBoxUtils():
    """dev.ultreon.quantum.util.BoundingBoxUtils"""
 
    @staticmethod
    def __wrap(java_value: __BoundingBoxUtils) -> 'BoundingBoxUtils':
        return BoundingBoxUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundingBoxUtils):
        """
        Dynamic initializer for BoundingBoxUtils.
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
    def clipXCollide(arg0: 'BoundingBox', arg1: 'BoundingBox', arg2: float) -> float:
        """public static double dev.ultreon.quantum.util.BoundingBoxUtils.clipXCollide(dev.ultreon.quantum.util.BoundingBox,dev.ultreon.quantum.util.BoundingBox,double)"""
        return float.__wrap(__BoundingBoxUtils.clipXCollide(arg0, arg1, __double.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def clipYCollide(arg0: 'BoundingBox', arg1: 'BoundingBox', arg2: float) -> float:
        """public static double dev.ultreon.quantum.util.BoundingBoxUtils.clipYCollide(dev.ultreon.quantum.util.BoundingBox,dev.ultreon.quantum.util.BoundingBox,double)"""
        return float.__wrap(__BoundingBoxUtils.clipYCollide(arg0, arg1, __double.valueOf(arg2)))

    @staticmethod
    @overload
    def clipZCollide(arg0: 'BoundingBox', arg1: 'BoundingBox', arg2: float) -> float:
        """public static double dev.ultreon.quantum.util.BoundingBoxUtils.clipZCollide(dev.ultreon.quantum.util.BoundingBox,dev.ultreon.quantum.util.BoundingBox,double)"""
        return float.__wrap(__BoundingBoxUtils.clipZCollide(arg0, arg1, __double.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def offset(arg0: 'BoundingBox', arg1: float, arg2: float, arg3: float) -> 'BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBoxUtils.offset(dev.ultreon.quantum.util.BoundingBox,double,double,double)"""
        return BoundingBox.__wrap(__BoundingBoxUtils.offset(arg0, __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.BoundingBoxUtils()"""
        val = __BoundingBoxUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.BoundingBoxUtils()"""
        val = __BoundingBoxUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.util.ExceptionMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import dev.ultreon.quantum.util.ExceptionMap as __ExceptionMap
__ExceptionMap = __ExceptionMap
from builtins import bool
from builtins import int
 
class ExceptionMap():
    """dev.ultreon.quantum.util.ExceptionMap"""
 
    @staticmethod
    def __wrap(java_value: __ExceptionMap) -> 'ExceptionMap':
        return ExceptionMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExceptionMap):
        """
        Dynamic initializer for ExceptionMap.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sendFatal(arg0: 'CommandSender', arg1: 'Throwable', arg2: bool):
        """public static void dev.ultreon.quantum.util.ExceptionMap.sendFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Throwable,boolean)"""
        __ExceptionMap.sendFatal(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def sendFatal(arg0: 'CommandSender', arg1: 'Throwable'):
        """public static void dev.ultreon.quantum.util.ExceptionMap.sendFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Throwable)"""
        __ExceptionMap.sendFatal(arg0, arg1)

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

    @staticmethod
    @overload
    def getErrorCode(arg0: 'Throwable') -> str:
        """public static java.lang.String dev.ultreon.quantum.util.ExceptionMap.getErrorCode(java.lang.Throwable)"""
        return str.__wrap(__ExceptionMap.getErrorCode(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.ExceptionMap()"""
        val = __ExceptionMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.ExceptionMap()"""
        val = __ExceptionMap()
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
 
 
# CLASS: dev.ultreon.quantum.util.MathHelper$FaceRotation
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.util.MathHelper as __MathHelper_FaceRotation
__FaceRotation = __MathHelper_FaceRotation.FaceRotation
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
from builtins import int
 
class FaceRotation(__Enum, Enum):
    """dev.ultreon.quantum.util.MathHelper.FaceRotation"""
 
    @staticmethod
    def __wrap(java_value: __FaceRotation) -> 'FaceRotation':
        return FaceRotation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FaceRotation):
        """
        Dynamic initializer for FaceRotation.
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
 
    # public static final dev.ultreon.quantum.util.MathHelper$FaceRotation dev.ultreon.quantum.util.MathHelper$FaceRotation.UNCHANGED
    UNCHANGED: 'FaceRotation' = __wrap(__FaceRotation.UNCHANGED)

    # public static final dev.ultreon.quantum.util.MathHelper$FaceRotation dev.ultreon.quantum.util.MathHelper$FaceRotation.DEGREES_90
    DEGREES_90: 'FaceRotation' = __wrap(__FaceRotation.DEGREES_90)

    # public static final dev.ultreon.quantum.util.MathHelper$FaceRotation dev.ultreon.quantum.util.MathHelper$FaceRotation.DEGREES_270
    DEGREES_270: 'FaceRotation' = __wrap(__FaceRotation.DEGREES_270)

    # public static final dev.ultreon.quantum.util.MathHelper$FaceRotation dev.ultreon.quantum.util.MathHelper$FaceRotation.DEGREES_180
    DEGREES_180: 'FaceRotation' = __wrap(__FaceRotation.DEGREES_180)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FaceRotation':
        """public static dev.ultreon.quantum.util.MathHelper$FaceRotation dev.ultreon.quantum.util.MathHelper$FaceRotation.valueOf(java.lang.String)"""
        return FaceRotation.__wrap(__FaceRotation.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['FaceRotation']:
        """public static dev.ultreon.quantum.util.MathHelper$FaceRotation[] dev.ultreon.quantum.util.MathHelper$FaceRotation.values()"""
        return List[FaceRotation].__wrap(__FaceRotation.values()) 
 
 
# CLASS: dev.ultreon.quantum.util.ValidationError
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
import dev.ultreon.quantum.util.ValidationError as __ValidationError
__ValidationError = __ValidationError
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
 
class ValidationError(__Error, Error):
    """dev.ultreon.quantum.util.ValidationError"""
 
    @staticmethod
    def __wrap(java_value: __ValidationError) -> 'ValidationError':
        return ValidationError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValidationError):
        """
        Dynamic initializer for ValidationError.
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.ValidationError(java.lang.String)"""
        val = __ValidationError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.PollingExecutorService
from pyquantum_helper import import_once as __import_once__
import java.lang.Thread as Thread
from builtins import type
import dev.ultreon.quantum.debug.profiler.Profiler as __Profiler
__Profiler = __Profiler
import dev.ultreon.quantum.util.PollingExecutorService as __PollingExecutorService
__PollingExecutorService = __PollingExecutorService
import java.util.Collection as Collection
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = __import_once__("pyquantum.debug.profiler")

import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
import java.lang.Runnable as Runnable
from builtins import object
import java.lang.Long as __long
import java.util.List as __List
__List = __List
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.concurrent.CompletableFuture as CompletableFuture
import java.util.List as List
from builtins import int
 
class PollingExecutorService(__ExecutorService, ExecutorService):
    """dev.ultreon.quantum.util.PollingExecutorService"""
 
    @staticmethod
    def __wrap(java_value: __PollingExecutorService) -> 'PollingExecutorService':
        return PollingExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PollingExecutorService):
        """
        Dynamic initializer for PollingExecutorService.
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
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'.__wrap(super(__PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'.__wrap(super(__PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'.__wrap(super(__PollingExecutorService, self).invokeAll(arg0))

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__PollingExecutorService, self).awaitTermination(__long.valueOf(arg0), arg1))

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'.__wrap(super(__PollingExecutorService, self).invokeAll(arg0, __long.valueOf(arg1), arg2))

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'.__wrap(super(PollingExecutorService, self).shutdownNow())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @property
    def profiler(self) -> Profiler:
        return Profiler.__wrap(super(__PollingExecutorService).profiler())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Profiler'):
        """public dev.ultreon.quantum.util.PollingExecutorService(dev.ultreon.quantum.debug.profiler.Profiler)"""
        val = __PollingExecutorService(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool.__wrap(super(PollingExecutorService, self).isShutdown())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(PollingExecutorService, self).pollAll()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'.__wrap(super(__PollingExecutorService, self).submit(arg0, arg1))

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__PollingExecutorService, self).invokeAny(arg0, __long.valueOf(arg1), arg2))

    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(__PollingExecutorService, self).execute(arg0)

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__PollingExecutorService, self).invokeAny(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isTerminated()"""
        return bool.__wrap(super(PollingExecutorService, self).isTerminated())

    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(PollingExecutorService, self).poll()

    @overload
    def __init__(self, arg0: 'Thread', arg1: 'Profiler'):
        """public dev.ultreon.quantum.util.PollingExecutorService(java.lang.Thread,dev.ultreon.quantum.debug.profiler.Profiler)"""
        val = __PollingExecutorService(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def shutdown(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.shutdown()"""
        super(PollingExecutorService, self).shutdown() 
 
 
# CLASS: dev.ultreon.quantum.util.HitResult
import dev.ultreon.quantum.util.HitResult as __HitResult
__HitResult = __HitResult
from abc import abstractmethod, ABC
 
class HitResult(ABC):
    """dev.ultreon.quantum.util.HitResult"""
 
    @staticmethod
    def __wrap(java_value: __HitResult) -> 'HitResult':
        return HitResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HitResult):
        """
        Dynamic initializer for HitResult.
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
    def getRay(self, ):
        """public abstract dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.HitResult.getRay()"""
        pass

    @abstractmethod
    def getDistance(self, ):
        """public abstract double dev.ultreon.quantum.util.HitResult.getDistance()"""
        pass

    @abstractmethod
    def getDistanceMax(self, ):
        """public abstract float dev.ultreon.quantum.util.HitResult.getDistanceMax()"""
        pass

    @abstractmethod
    def isCollide(self, ):
        """public abstract boolean dev.ultreon.quantum.util.HitResult.isCollide()"""
        pass

    @abstractmethod
    def getPos(self, ):
        """public abstract dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.HitResult.getPos()"""
        pass

    @abstractmethod
    def getPosition(self, ):
        """public abstract dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.HitResult.getPosition()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.util.SanityCheckException
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
import dev.ultreon.quantum.util.SanityCheckException as __SanityCheckException
__SanityCheckException = __SanityCheckException
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SanityCheckException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.util.SanityCheckException"""
 
    @staticmethod
    def __wrap(java_value: __SanityCheckException) -> 'SanityCheckException':
        return SanityCheckException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SanityCheckException):
        """
        Dynamic initializer for SanityCheckException.
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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.util.SanityCheckException(java.lang.Throwable)"""
        val = __SanityCheckException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.SanityCheckException()"""
        val = __SanityCheckException()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.SanityCheckException()"""
        val = __SanityCheckException()
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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.util.SanityCheckException(java.lang.String,java.lang.Throwable)"""
        val = __SanityCheckException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.SanityCheckException(java.lang.String)"""
        val = __SanityCheckException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.util.EntityHitResult
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.world.CubicDirection as __CubicDirection
__CubicDirection = __CubicDirection
import dev.ultreon.quantum.util.EntityHitResult as __EntityHitResult
__EntityHitResult = __EntityHitResult
from builtins import str
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import dev.ultreon.quantum.util.Ray as __Ray
__Ray = __Ray
 
class EntityHitResult(__HitResult, HitResult):
    """dev.ultreon.quantum.util.EntityHitResult"""
 
    @staticmethod
    def __wrap(java_value: __EntityHitResult) -> 'EntityHitResult':
        return EntityHitResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityHitResult):
        """
        Dynamic initializer for EntityHitResult.
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
    def setInput(self, arg0: 'Ray') -> 'EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.util.EntityHitResult.setInput(dev.ultreon.quantum.util.Ray)"""
        return 'EntityHitResult'.__wrap(super(__EntityHitResult, self).setInput(arg0))

    @overload
    def setDirection(self, arg0: 'CubicDirection'):
        """public void dev.ultreon.quantum.util.EntityHitResult.setDirection(dev.ultreon.quantum.world.CubicDirection)"""
        super(__EntityHitResult, self).setDirection(arg0)

    @override
    @overload
    def isCollide(self) -> bool:
        """public boolean dev.ultreon.quantum.util.EntityHitResult.isCollide()"""
        return bool.__wrap(super(EntityHitResult, self).isCollide())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.util.EntityHitResult.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__EntityHitResult, self).write(arg0)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.util.EntityHitResult(dev.ultreon.quantum.network.PacketIO)"""
        val = __EntityHitResult(arg0)
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
        """public int dev.ultreon.quantum.util.EntityHitResult.hashCode()"""
        return int.__wrap(super(EntityHitResult, self).hashCode())

    @override
    @overload
    def getRay(self) -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.EntityHitResult.getRay()"""
        return 'Ray'.__wrap(super(EntityHitResult, self).getRay())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.EntityHitResult()"""
        val = __EntityHitResult()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @property
    def entity(self, value: 'entity.Entity'):
        super(__EntityHitResult).entity(value)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.EntityHitResult()"""
        val = __EntityHitResult()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Ray', arg1: float):
        """public dev.ultreon.quantum.util.EntityHitResult(dev.ultreon.quantum.util.Ray,float)"""
        val = __EntityHitResult(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.util.EntityHitResult.equals(java.lang.Object)"""
        return bool.__wrap(super(__EntityHitResult, self).equals(arg0))

    @property
    def entity(self) -> Entity:
        return Entity.__wrap(super(__EntityHitResult).entity())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.util.EntityHitResult.getEntity()"""
        return 'entity.Entity'.__wrap(super(EntityHitResult, self).getEntity())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getDistance(self) -> float:
        """public double dev.ultreon.quantum.util.EntityHitResult.getDistance()"""
        return float.__wrap(super(EntityHitResult, self).getDistance())

    @override
    @overload
    def getDistanceMax(self) -> float:
        """public float dev.ultreon.quantum.util.EntityHitResult.getDistanceMax()"""
        return float.__wrap(super(EntityHitResult, self).getDistanceMax())

    @override
    @overload
    def getPos(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.EntityHitResult.getPos()"""
        return 'vector.Vec3i'.__wrap(super(EntityHitResult, self).getPos())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDirection(self) -> 'world.CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.util.EntityHitResult.getDirection()"""
        return 'world.CubicDirection'.__wrap(super(EntityHitResult, self).getDirection())

    @overload
    def __init__(self, arg0: 'Ray'):
        """public dev.ultreon.quantum.util.EntityHitResult(dev.ultreon.quantum.util.Ray)"""
        val = __EntityHitResult(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getNormal(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.EntityHitResult.getNormal()"""
        return 'vector.Vec3d'.__wrap(super(EntityHitResult, self).getNormal())

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.EntityHitResult.getPosition()"""
        return 'vector.Vec3d'.__wrap(super(EntityHitResult, self).getPosition()) 
 
 
# CLASS: dev.ultreon.quantum.util.DataSizes
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
import dev.ultreon.quantum.util.DataSizes as __DataSizes
__DataSizes = __DataSizes
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DataSizes():
    """dev.ultreon.quantum.util.DataSizes"""
 
    @staticmethod
    def __wrap(java_value: __DataSizes) -> 'DataSizes':
        return DataSizes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataSizes):
        """
        Dynamic initializer for DataSizes.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def convert(arg0: int, arg1: 'Unit', arg2: 'Unit') -> int:
        """public static long dev.ultreon.quantum.util.DataSizes.convert(long,dev.ultreon.quantum.util.DataSizes$Unit,dev.ultreon.quantum.util.DataSizes$Unit)"""
        return int.__wrap(__DataSizes.convert(__long.valueOf(arg0), arg1, arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.DataSizes()"""
        val = __DataSizes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def format(arg0: int) -> str:
        """public static java.lang.String dev.ultreon.quantum.util.DataSizes.format(long)"""
        return str.__wrap(__DataSizes.format(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.DataSizes()"""
        val = __DataSizes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.ExitCodes
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.util.ExitCodes as __ExitCodes
__ExitCodes = __ExitCodes
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ExitCodes():
    """dev.ultreon.quantum.util.ExitCodes"""
 
    @staticmethod
    def __wrap(java_value: __ExitCodes) -> 'ExitCodes':
        return ExitCodes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExitCodes):
        """
        Dynamic initializer for ExitCodes.
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.ExitCodes()"""
        val = __ExitCodes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.ExitCodes()"""
        val = __ExitCodes()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.util.Unit
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import dev.ultreon.quantum.util.Unit as __Unit
__Unit = __Unit
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Unit():
    """dev.ultreon.quantum.util.Unit"""
 
    @staticmethod
    def __wrap(java_value: __Unit) -> 'Unit':
        return Unit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Unit):
        """
        Dynamic initializer for Unit.
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
 
    # public static final dev.ultreon.quantum.util.Unit dev.ultreon.quantum.util.Unit.INSTANCE
    INSTANCE: 'Unit' = __wrap(__Unit.INSTANCE)


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
 
 
# CLASS: dev.ultreon.quantum.util.ValueSource
from abc import abstractmethod, ABC
import dev.ultreon.quantum.util.ValueSource as __ValueSource
__ValueSource = __ValueSource
 
class ValueSource(ABC):
    """dev.ultreon.quantum.util.ValueSource"""
 
    @staticmethod
    def __wrap(java_value: __ValueSource) -> 'ValueSource':
        return ValueSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueSource):
        """
        Dynamic initializer for ValueSource.
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
    def getValue(self, ):
        """public abstract double dev.ultreon.quantum.util.ValueSource.getValue()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.util.Ray
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.world.CubicDirection as __CubicDirection
__CubicDirection = __CubicDirection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Float as __float
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.util.Ray as __Ray
__Ray = __Ray
from builtins import int
 
class Ray(__Serializable, Serializable):
    """dev.ultreon.quantum.util.Ray"""
 
    @staticmethod
    def __wrap(java_value: __Ray) -> 'Ray':
        return Ray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ray):
        """
        Dynamic initializer for Ray.
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
    def __init__(self, arg0: 'Vec3d', arg1: 'Vec3d'):
        """public dev.ultreon.quantum.util.Ray(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = __Ray(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.Ray.toString()"""
        return str.__wrap(super(Ray, self).toString())

    @overload
    def cpy(self) -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.Ray.cpy()"""
        return 'Ray'.__wrap(super(Ray, self).cpy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Vec3d', arg1: 'Vec3d') -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.Ray.set(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Ray'.__wrap(super(__Ray, self).set(arg0, arg1))

    @overload
    def getDirection(self) -> 'world.CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.util.Ray.getDirection()"""
        return 'world.CubicDirection'.__wrap(super(Ray, self).getDirection())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.Ray.set(float,float,float,float,float,float)"""
        return 'Ray'.__wrap(super(__Ray, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def set(self, arg0: 'Ray') -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.Ray.set(dev.ultreon.quantum.util.Ray)"""
        return 'Ray'.__wrap(super(__Ray, self).set(arg0))

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.util.Ray(dev.ultreon.quantum.network.PacketIO)"""
        val = __Ray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getEndPoint(self, arg0: 'Vec3d', arg1: float) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.Ray.getEndPoint(dev.ultreon.libs.commons.v0.vector.Vec3d,float)"""
        return 'vector.Vec3d'.__wrap(super(__Ray, self).getEndPoint(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.util.Ray.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Ray, self).write(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.Ray()"""
        val = __Ray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.util.Ray.equals(java.lang.Object)"""
        return bool.__wrap(super(__Ray, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.util.Ray.hashCode()"""
        return int.__wrap(super(Ray, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.Ray()"""
        val = __Ray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.util.LazyValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.util.LazyValue as __LazyValue
__LazyValue = __LazyValue
from builtins import int
 
class LazyValue():
    """dev.ultreon.quantum.util.LazyValue"""
 
    @staticmethod
    def __wrap(java_value: __LazyValue) -> 'LazyValue':
        return LazyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LazyValue):
        """
        Dynamic initializer for LazyValue.
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
    def __init__(self):
        """public dev.ultreon.quantum.util.LazyValue()"""
        val = __LazyValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.LazyValue()"""
        val = __LazyValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.util.LazyValue.set(T)"""
        super(__LazyValue, self).set(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isInitialized(self) -> bool:
        """public boolean dev.ultreon.quantum.util.LazyValue.isInitialized()"""
        return bool.__wrap(super(LazyValue, self).isInitialized())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.util.LazyValue.get()"""
        return object.__wrap(super(LazyValue, self).get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.BlockMetaPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import dev.ultreon.quantum.util.BlockMetaPredicate as __BlockMetaPredicate
__BlockMetaPredicate = __BlockMetaPredicate
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlockMetaPredicate(__Predicate, Predicate):
    """dev.ultreon.quantum.util.BlockMetaPredicate"""
 
    @staticmethod
    def __wrap(java_value: __BlockMetaPredicate) -> 'BlockMetaPredicate':
        return BlockMetaPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockMetaPredicate):
        """
        Dynamic initializer for BlockMetaPredicate.
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
 
    # public static final dev.ultreon.quantum.util.BlockMetaPredicate dev.ultreon.quantum.util.BlockMetaPredicate.WG_HEIGHT_CHK
    WG_HEIGHT_CHK: 'BlockMetaPredicate' = __wrap(__BlockMetaPredicate.WG_HEIGHT_CHK)

    # public static final dev.ultreon.quantum.util.BlockMetaPredicate dev.ultreon.quantum.util.BlockMetaPredicate.REPLACEABLE
    REPLACEABLE: 'BlockMetaPredicate' = __wrap(__BlockMetaPredicate.REPLACEABLE)

    # public static final dev.ultreon.quantum.util.BlockMetaPredicate dev.ultreon.quantum.util.BlockMetaPredicate.BREAK_INSTANTLY
    BREAK_INSTANTLY: 'BlockMetaPredicate' = __wrap(__BlockMetaPredicate.BREAK_INSTANTLY)

    # public static final dev.ultreon.quantum.util.BlockMetaPredicate dev.ultreon.quantum.util.BlockMetaPredicate.NON_FLUID
    NON_FLUID: 'BlockMetaPredicate' = __wrap(__BlockMetaPredicate.NON_FLUID)

    # public static final dev.ultreon.quantum.util.BlockMetaPredicate dev.ultreon.quantum.util.BlockMetaPredicate.EVERYTHING
    EVERYTHING: 'BlockMetaPredicate' = __wrap(__BlockMetaPredicate.EVERYTHING)

    # public static final dev.ultreon.quantum.util.BlockMetaPredicate dev.ultreon.quantum.util.BlockMetaPredicate.FLUID
    FLUID: 'BlockMetaPredicate' = __wrap(__BlockMetaPredicate.FLUID)

    # public static final dev.ultreon.quantum.util.BlockMetaPredicate dev.ultreon.quantum.util.BlockMetaPredicate.SOLID
    SOLID: 'BlockMetaPredicate' = __wrap(__BlockMetaPredicate.SOLID)

    # public static final dev.ultreon.quantum.util.BlockMetaPredicate dev.ultreon.quantum.util.BlockMetaPredicate.TRANSPARENT
    TRANSPARENT: 'BlockMetaPredicate' = __wrap(__BlockMetaPredicate.TRANSPARENT)


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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def test(self, arg0: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.util.BlockMetaPredicate.test(dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__BlockMetaPredicate, self).test(arg0))

    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).or(arg0))

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
    def negate(self) -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.negate()"""
        return 'Predicate'.__wrap(super(Predicate, self).negate())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).and(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.InvalidThreadException
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.util.InvalidThreadException as __InvalidThreadException
__InvalidThreadException = __InvalidThreadException
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
 
class InvalidThreadException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.util.InvalidThreadException"""
 
    @staticmethod
    def __wrap(java_value: __InvalidThreadException) -> 'InvalidThreadException':
        return InvalidThreadException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidThreadException):
        """
        Dynamic initializer for InvalidThreadException.
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.InvalidThreadException(java.lang.String)"""
        val = __InvalidThreadException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.IntSizedList
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.libs.collections.v0.util.Range as __Range
__Range = __Range
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import it.unimi.dsi.fastutil.objects.Reference2IntFunction as Reference2IntFunction
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.collections.v0 import util
except ImportError:
    util = __import_once__("pycorelibs.collections.v0.util")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.util.IntSizedList as __IntSizedList
__IntSizedList = __IntSizedList
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntSizedList():
    """dev.ultreon.quantum.util.IntSizedList"""
 
    @staticmethod
    def __wrap(java_value: __IntSizedList) -> 'IntSizedList':
        return IntSizedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntSizedList):
        """
        Dynamic initializer for IntSizedList.
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
    def clear(self):
        """public void dev.ultreon.quantum.util.IntSizedList.clear()"""
        super(IntSizedList, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def rangeOf(self, arg0: object) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.quantum.util.IntSizedList.rangeOf(T)"""
        return 'util.Range'.__wrap(super(__IntSizedList, self).rangeOf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.indexOf(T)"""
        return int.__wrap(super(__IntSizedList, self).indexOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRanges(self) -> List['util.Range']:
        """public dev.ultreon.libs.collections.v0.util.Range[] dev.ultreon.quantum.util.IntSizedList.getRanges()"""
        return List['util.Range'].__wrap(super(IntSizedList, self).getRanges())

    @overload
    def size(self) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.size()"""
        return int.__wrap(super(IntSizedList, self).size())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.IntSizedList()"""
        val = __IntSizedList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getDirectValue(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.util.IntSizedList.getDirectValue(int)"""
        return object.__wrap(super(__IntSizedList, self).getDirectValue(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getValue(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.util.IntSizedList.getValue(int)"""
        return object.__wrap(super(__IntSizedList, self).getValue(__int.valueOf(arg0)))

    @overload
    def edit(self, arg0: object, arg1: int, arg2: object) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.edit(T,int,T)"""
        return int.__wrap(super(__IntSizedList, self).edit(arg0, __int.valueOf(arg1), arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getSize(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.getSize(int)"""
        return int.__wrap(super(__IntSizedList, self).getSize(__int.valueOf(arg0)))

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.quantum.util.IntSizedList.remove(int)"""
        super(__IntSizedList, self).remove(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, arg0: int, arg1: object) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.add(int,T)"""
        return int.__wrap(super(__IntSizedList, self).add(__int.valueOf(arg0), arg1))

    @overload
    def addAll(self, arg0: 'IntSizedList'):
        """public void dev.ultreon.quantum.util.IntSizedList.addAll(dev.ultreon.quantum.util.IntSizedList<? extends T>)"""
        super(__IntSizedList, self).addAll(arg0)

    @overload
    def editLengths(self, arg0: 'Reference2IntFunction'):
        """public void dev.ultreon.quantum.util.IntSizedList.editLengths(it.unimi.dsi.fastutil.objects.Reference2IntFunction<T>)"""
        super(__IntSizedList, self).editLengths(arg0)

    @overload
    def getTotalSize(self) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.getTotalSize()"""
        return int.__wrap(super(IntSizedList, self).getTotalSize())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.IntSizedList()"""
        val = __IntSizedList()
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

    @overload
    def subList(self, arg0: int, arg1: int) -> 'IntSizedList':
        """public dev.ultreon.quantum.util.IntSizedList<T> dev.ultreon.quantum.util.IntSizedList.subList(int,int)"""
        return 'IntSizedList'.__wrap(super(__IntSizedList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def edit(self, arg0: object, arg1: int) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.edit(T,int)"""
        return int.__wrap(super(__IntSizedList, self).edit(arg0, __int.valueOf(arg1)))

    @overload
    def insert(self, arg0: int, arg1: int, arg2: object) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.insert(int,int,T)"""
        return int.__wrap(super(__IntSizedList, self).insert(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRange(self, arg0: int) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.quantum.util.IntSizedList.getRange(int)"""
        return 'util.Range'.__wrap(super(__IntSizedList, self).getRange(__int.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.quantum.util.Difficulty
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.util.Difficulty as __Difficulty
__Difficulty = __Difficulty
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
 
class Difficulty(__Enum, Enum):
    """dev.ultreon.quantum.util.Difficulty"""
 
    @staticmethod
    def __wrap(java_value: __Difficulty) -> 'Difficulty':
        return Difficulty(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Difficulty):
        """
        Dynamic initializer for Difficulty.
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
 
    # public static final dev.ultreon.quantum.util.Difficulty dev.ultreon.quantum.util.Difficulty.PEACEFUL
    PEACEFUL: 'Difficulty' = __wrap(__Difficulty.PEACEFUL)

    # public static final dev.ultreon.quantum.util.Difficulty dev.ultreon.quantum.util.Difficulty.APOCALYPSE
    APOCALYPSE: 'Difficulty' = __wrap(__Difficulty.APOCALYPSE)

    # public static final dev.ultreon.quantum.util.Difficulty dev.ultreon.quantum.util.Difficulty.EASY
    EASY: 'Difficulty' = __wrap(__Difficulty.EASY)

    # public static final dev.ultreon.quantum.util.Difficulty dev.ultreon.quantum.util.Difficulty.HARD
    HARD: 'Difficulty' = __wrap(__Difficulty.HARD)

    # public static final dev.ultreon.quantum.util.Difficulty dev.ultreon.quantum.util.Difficulty.NORMAL
    NORMAL: 'Difficulty' = __wrap(__Difficulty.NORMAL)

    # public static final dev.ultreon.quantum.util.Difficulty dev.ultreon.quantum.util.Difficulty.IMPOSSIBLE
    IMPOSSIBLE: 'Difficulty' = __wrap(__Difficulty.IMPOSSIBLE)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Difficulty':
        """public static dev.ultreon.quantum.util.Difficulty dev.ultreon.quantum.util.Difficulty.valueOf(java.lang.String)"""
        return Difficulty.__wrap(__Difficulty.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def values() -> List['Difficulty']:
        """public static dev.ultreon.quantum.util.Difficulty[] dev.ultreon.quantum.util.Difficulty.values()"""
        return List[Difficulty].__wrap(__Difficulty.values())

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
 
 
# CLASS: dev.ultreon.quantum.util.BlockHitResult
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.world.CubicDirection as __CubicDirection
__CubicDirection = __CubicDirection
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.Ray as __Ray
__Ray = __Ray
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.util.BlockHitResult as __BlockHitResult
__BlockHitResult = __BlockHitResult
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Float as __float
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class BlockHitResult(__HitResult, HitResult):
    """dev.ultreon.quantum.util.BlockHitResult"""
 
    @staticmethod
    def __wrap(java_value: __BlockHitResult) -> 'BlockHitResult':
        return BlockHitResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockHitResult):
        """
        Dynamic initializer for BlockHitResult.
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
    def getDirection(self) -> 'world.CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.util.BlockHitResult.getDirection()"""
        return 'world.CubicDirection'.__wrap(super(BlockHitResult, self).getDirection())

    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.util.BlockHitResult.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__BlockHitResult, self).write(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.BlockHitResult()"""
        val = __BlockHitResult()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setInput(self, arg0: 'Ray') -> 'BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.util.BlockHitResult.setInput(dev.ultreon.quantum.util.Ray)"""
        return 'BlockHitResult'.__wrap(super(__BlockHitResult, self).setInput(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.util.BlockHitResult.hashCode()"""
        return int.__wrap(super(BlockHitResult, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRay(self) -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.BlockHitResult.getRay()"""
        return 'Ray'.__wrap(super(BlockHitResult, self).getRay())

    @overload
    def __init__(self, arg0: 'Ray', arg1: float):
        """public dev.ultreon.quantum.util.BlockHitResult(dev.ultreon.quantum.util.Ray,float)"""
        val = __BlockHitResult(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BlockHitResult.getPosition()"""
        return 'vector.Vec3d'.__wrap(super(BlockHitResult, self).getPosition())

    @override
    @overload
    def getDistanceMax(self) -> float:
        """public float dev.ultreon.quantum.util.BlockHitResult.getDistanceMax()"""
        return float.__wrap(super(BlockHitResult, self).getDistanceMax())

    @override
    @overload
    def isCollide(self) -> bool:
        """public boolean dev.ultreon.quantum.util.BlockHitResult.isCollide()"""
        return bool.__wrap(super(BlockHitResult, self).isCollide())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.util.BlockHitResult(dev.ultreon.quantum.network.PacketIO)"""
        val = __BlockHitResult(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.BlockHitResult()"""
        val = __BlockHitResult()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.util.BlockHitResult.getBlockMeta()"""
        return 'state.BlockProperties'.__wrap(super(BlockHitResult, self).getBlockMeta())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.util.BlockHitResult.equals(java.lang.Object)"""
        return bool.__wrap(super(__BlockHitResult, self).equals(arg0))

    @overload
    def getNext(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.BlockHitResult.getNext()"""
        return 'vector.Vec3i'.__wrap(super(BlockHitResult, self).getNext())

    @overload
    def setDirection(self, arg0: 'CubicDirection'):
        """public void dev.ultreon.quantum.util.BlockHitResult.setDirection(dev.ultreon.quantum.world.CubicDirection)"""
        super(__BlockHitResult, self).setDirection(arg0)

    @overload
    def getNormal(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BlockHitResult.getNormal()"""
        return 'vector.Vec3d'.__wrap(super(BlockHitResult, self).getNormal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getPos(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.BlockHitResult.getPos()"""
        return 'vector.Vec3i'.__wrap(super(BlockHitResult, self).getPos())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Ray'):
        """public dev.ultreon.quantum.util.BlockHitResult(dev.ultreon.quantum.util.Ray)"""
        val = __BlockHitResult(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.util.BlockHitResult.getBlock()"""
        return 'block.Block'.__wrap(super(BlockHitResult, self).getBlock())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getDistance(self) -> float:
        """public double dev.ultreon.quantum.util.BlockHitResult.getDistance()"""
        return float.__wrap(super(BlockHitResult, self).getDistance()) 
 
 
# CLASS: dev.ultreon.quantum.util.IllegalThreadInterruptionError
from builtins import str
import java.lang.InterruptedException as InterruptedException
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.util.IllegalThreadInterruptionError as __IllegalThreadInterruptionError
__IllegalThreadInterruptionError = __IllegalThreadInterruptionError
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
 
class IllegalThreadInterruptionError(__Error, Error):
    """dev.ultreon.quantum.util.IllegalThreadInterruptionError"""
 
    @staticmethod
    def __wrap(java_value: __IllegalThreadInterruptionError) -> 'IllegalThreadInterruptionError':
        return IllegalThreadInterruptionError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IllegalThreadInterruptionError):
        """
        Dynamic initializer for IllegalThreadInterruptionError.
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.IllegalThreadInterruptionError(java.lang.String)"""
        val = __IllegalThreadInterruptionError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: str, arg1: 'InterruptedException'):
        """public dev.ultreon.quantum.util.IllegalThreadInterruptionError(java.lang.String,java.lang.InterruptedException)"""
        val = __IllegalThreadInterruptionError(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.Axis
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.util.Axis as __Axis
__Axis = __Axis
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
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
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Axis(__Enum, Enum):
    """dev.ultreon.quantum.util.Axis"""
 
    @staticmethod
    def __wrap(java_value: __Axis) -> 'Axis':
        return Axis(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Axis):
        """
        Dynamic initializer for Axis.
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
 
    # public static final dev.ultreon.quantum.util.Axis dev.ultreon.quantum.util.Axis.Y
    Y: 'Axis' = __wrap(__Axis.Y)

    # public static final dev.ultreon.quantum.util.Axis dev.ultreon.quantum.util.Axis.Z
    Z: 'Axis' = __wrap(__Axis.Z)

    # public static final dev.ultreon.quantum.util.Axis dev.ultreon.quantum.util.Axis.X
    X: 'Axis' = __wrap(__Axis.X)


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

    @staticmethod
    @overload
    def values() -> List['Axis']:
        """public static dev.ultreon.quantum.util.Axis[] dev.ultreon.quantum.util.Axis.values()"""
        return List[Axis].__wrap(__Axis.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Axis':
        """public static dev.ultreon.quantum.util.Axis dev.ultreon.quantum.util.Axis.valueOf(java.lang.String)"""
        return Axis.__wrap(__Axis.valueOf(arg0))

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
    def getVector(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.util.Axis.getVector()"""
        return 'math.Vector3'.__wrap(super(Axis, self).getVector())

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
 
 
# CLASS: dev.ultreon.quantum.util.ModLoadingContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.util.ModLoadingContext as __ModLoadingContext
__ModLoadingContext = __ModLoadingContext
import java.lang.Runnable as Runnable
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.Mod as __Mod
__Mod = __Mod
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModLoadingContext():
    """dev.ultreon.quantum.util.ModLoadingContext"""
 
    @staticmethod
    def __wrap(java_value: __ModLoadingContext) -> 'ModLoadingContext':
        return ModLoadingContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModLoadingContext):
        """
        Dynamic initializer for ModLoadingContext.
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

    @staticmethod
    @overload
    def withinContext(arg0: 'Mod', arg1: 'Runnable'):
        """public static void dev.ultreon.quantum.util.ModLoadingContext.withinContext(dev.ultreon.quantum.Mod,java.lang.Runnable)"""
        __ModLoadingContext.withinContext(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get() -> 'ModLoadingContext':
        """public static dev.ultreon.quantum.util.ModLoadingContext dev.ultreon.quantum.util.ModLoadingContext.get()"""
        return ModLoadingContext.__wrap(__ModLoadingContext.get())

    @overload
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.util.ModLoadingContext.getMod()"""
        return 'pyquantum.Mod'.__wrap(super(ModLoadingContext, self).getMod())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.PosOutOfBoundsException
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
import dev.ultreon.quantum.util.PosOutOfBoundsException as __PosOutOfBoundsException
__PosOutOfBoundsException = __PosOutOfBoundsException
from builtins import int
 
class PosOutOfBoundsException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.util.PosOutOfBoundsException"""
 
    @staticmethod
    def __wrap(java_value: __PosOutOfBoundsException) -> 'PosOutOfBoundsException':
        return PosOutOfBoundsException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PosOutOfBoundsException):
        """
        Dynamic initializer for PosOutOfBoundsException.
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
    def __init__(self):
        """public dev.ultreon.quantum.util.PosOutOfBoundsException()"""
        val = __PosOutOfBoundsException()
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.PosOutOfBoundsException(java.lang.String)"""
        val = __PosOutOfBoundsException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.PosOutOfBoundsException()"""
        val = __PosOutOfBoundsException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.util.GameMode
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.util.GameMode as __GameMode
__GameMode = __GameMode
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.entity.player.PlayerAbilities as __PlayerAbilities
__PlayerAbilities = __PlayerAbilities
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
 
class GameMode(__Enum, Enum):
    """dev.ultreon.quantum.util.GameMode"""
 
    @staticmethod
    def __wrap(java_value: __GameMode) -> 'GameMode':
        return GameMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameMode):
        """
        Dynamic initializer for GameMode.
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
 
    # public static final dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.SPECTATOR
    SPECTATOR: 'GameMode' = __wrap(__GameMode.SPECTATOR)

    # public static final dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.ADVENTUROUS
    ADVENTUROUS: 'GameMode' = __wrap(__GameMode.ADVENTUROUS)

    # public static final dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.SURVIVAL
    SURVIVAL: 'GameMode' = __wrap(__GameMode.SURVIVAL)

    # public static final dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.BUILDER
    BUILDER: 'GameMode' = __wrap(__GameMode.BUILDER)

    # public static final dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.BUILDER_PLUS
    BUILDER_PLUS: 'GameMode' = __wrap(__GameMode.BUILDER_PLUS)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def byOrdinal(arg0: int) -> 'GameMode':
        """public static dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.byOrdinal(int)"""
        return GameMode.__wrap(__GameMode.byOrdinal(__int.valueOf(arg0)))

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
    def setAbilities(self, arg0: 'PlayerAbilities') -> 'player.PlayerAbilities':
        """public dev.ultreon.quantum.entity.player.PlayerAbilities dev.ultreon.quantum.util.GameMode.setAbilities(dev.ultreon.quantum.entity.player.PlayerAbilities)"""
        return 'player.PlayerAbilities'.__wrap(super(__GameMode, self).setAbilities(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

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
    def valueOf(arg0: str) -> 'GameMode':
        """public static dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.valueOf(java.lang.String)"""
        return GameMode.__wrap(__GameMode.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['GameMode']:
        """public static dev.ultreon.quantum.util.GameMode[] dev.ultreon.quantum.util.GameMode.values()"""
        return List[GameMode].__wrap(__GameMode.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.util.BlockPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import java.lang.Object as __object
from builtins import type
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import dev.ultreon.quantum.util.BlockPredicate as __BlockPredicate
__BlockPredicate = __BlockPredicate
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
 
class BlockPredicate(__Predicate, Predicate):
    """dev.ultreon.quantum.util.BlockPredicate"""
 
    @staticmethod
    def __wrap(java_value: __BlockPredicate) -> 'BlockPredicate':
        return BlockPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockPredicate):
        """
        Dynamic initializer for BlockPredicate.
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
 
    # public static final dev.ultreon.quantum.util.BlockPredicate dev.ultreon.quantum.util.BlockPredicate.BREAK_INSTANTLY
    BREAK_INSTANTLY: 'BlockPredicate' = __wrap(__BlockPredicate.BREAK_INSTANTLY)

    # public static final dev.ultreon.quantum.util.BlockPredicate dev.ultreon.quantum.util.BlockPredicate.TRANSPARENT
    TRANSPARENT: 'BlockPredicate' = __wrap(__BlockPredicate.TRANSPARENT)

    # public static final dev.ultreon.quantum.util.BlockPredicate dev.ultreon.quantum.util.BlockPredicate.FLUID
    FLUID: 'BlockPredicate' = __wrap(__BlockPredicate.FLUID)

    # public static final dev.ultreon.quantum.util.BlockPredicate dev.ultreon.quantum.util.BlockPredicate.NON_FLUID
    NON_FLUID: 'BlockPredicate' = __wrap(__BlockPredicate.NON_FLUID)

    # public static final dev.ultreon.quantum.util.BlockPredicate dev.ultreon.quantum.util.BlockPredicate.EVERYTHING
    EVERYTHING: 'BlockPredicate' = __wrap(__BlockPredicate.EVERYTHING)

    # public static final dev.ultreon.quantum.util.BlockPredicate dev.ultreon.quantum.util.BlockPredicate.SOLID
    SOLID: 'BlockPredicate' = __wrap(__BlockPredicate.SOLID)

    # public static final dev.ultreon.quantum.util.BlockPredicate dev.ultreon.quantum.util.BlockPredicate.REPLACEABLE
    REPLACEABLE: 'BlockPredicate' = __wrap(__BlockPredicate.REPLACEABLE)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def test(self, arg0: 'Block') -> bool:
        """public boolean dev.ultreon.quantum.util.BlockPredicate.test(dev.ultreon.quantum.block.Block)"""
        return bool.__wrap(super(__BlockPredicate, self).test(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).or(arg0))

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
    def negate(self) -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.negate()"""
        return 'Predicate'.__wrap(super(Predicate, self).negate())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).and(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.OverwriteError
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
import dev.ultreon.quantum.util.OverwriteError as __OverwriteError
__OverwriteError = __OverwriteError
from builtins import int
 
class OverwriteError(__Error, Error):
    """dev.ultreon.quantum.util.OverwriteError"""
 
    @staticmethod
    def __wrap(java_value: __OverwriteError) -> 'OverwriteError':
        return OverwriteError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OverwriteError):
        """
        Dynamic initializer for OverwriteError.
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.OverwriteError(java.lang.String)"""
        val = __OverwriteError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.Identifier
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = __import_once__("pycorelibs.commons.v0.tuple")

import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import object
import java.util.function.BiFunction as BiFunction
from typing import List
import java.util.List as __List
__List = __List
import dev.ultreon.libs.commons.v0.tuple.Pair as __Pair
__Pair = __Pair
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
 
class Identifier():
    """dev.ultreon.quantum.util.Identifier"""
 
    @staticmethod
    def __wrap(java_value: __Identifier) -> 'Identifier':
        return Identifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Identifier):
        """
        Dynamic initializer for Identifier.
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
        """public java.lang.String dev.ultreon.quantum.util.Identifier.toString()"""
        return str.__wrap(super(Identifier, self).toString())

    @overload
    def reduce(self, arg0: 'BiFunction') -> object:
        """public <T> T dev.ultreon.quantum.util.Identifier.reduce(java.util.function.BiFunction<java.lang.String, java.lang.String, T>)"""
        return object.__wrap(super(__Identifier, self).reduce(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArrayList(self) -> 'ArrayList':
        """public java.util.ArrayList<java.lang.String> dev.ultreon.quantum.util.Identifier.toArrayList()"""
        return 'ArrayList'.__wrap(super(Identifier, self).toArrayList())

    @overload
    def withPath(self, arg0: str) -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.withPath(java.lang.String)"""
        return 'Identifier'.__wrap(super(__Identifier, self).withPath(arg0))

    @overload
    def mapPath(self, arg0: 'UnaryOperator') -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.mapPath(java.util.function.UnaryOperator<java.lang.String>)"""
        return 'Identifier'.__wrap(super(__Identifier, self).mapPath(arg0))

    @overload
    def toPair(self) -> 'tuple.Pair':
        """public dev.ultreon.libs.commons.v0.tuple.Pair<java.lang.String, java.lang.String> dev.ultreon.quantum.util.Identifier.toPair()"""
        return 'tuple.Pair'.__wrap(super(Identifier, self).toPair())

    @overload
    def withNamespace(self, arg0: str) -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.withNamespace(java.lang.String)"""
        return 'Identifier'.__wrap(super(__Identifier, self).withNamespace(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.util.Identifier.hashCode()"""
        return int.__wrap(super(Identifier, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def path(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.Identifier.path()"""
        return str.__wrap(super(Identifier, self).path())

    @staticmethod
    @overload
    def tryParse(arg0: str) -> 'Identifier':
        """public static dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.tryParse(java.lang.String)"""
        return Identifier.__wrap(__Identifier.tryParse(arg0))

    @overload
    def mapLocation(self, arg0: 'UnaryOperator') -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.mapLocation(java.util.function.UnaryOperator<java.lang.String>)"""
        return 'Identifier'.__wrap(super(__Identifier, self).mapLocation(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.Identifier(java.lang.String)"""
        val = __Identifier(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toArray(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.util.Identifier.toArray()"""
        return List[str].__wrap(super(Identifier, self).toArray())

    @staticmethod
    @overload
    def parse(arg0: str) -> 'Identifier':
        """public static dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.parse(java.lang.String)"""
        return Identifier.__wrap(__Identifier.parse(arg0))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.util.Identifier(java.lang.String,java.lang.String)"""
        val = __Identifier(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toList(self) -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.util.Identifier.toList()"""
        return 'List'.__wrap(super(Identifier, self).toList())

    @overload
    def namespace(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.Identifier.namespace()"""
        return str.__wrap(super(Identifier, self).namespace())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.util.Identifier.equals(java.lang.Object)"""
        return bool.__wrap(super(__Identifier, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toCollection(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.quantum.util.Identifier.toCollection()"""
        return 'Collection'.__wrap(super(Identifier, self).toCollection())

    @staticmethod
    @overload
    def testPath(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.util.Identifier.testPath(java.lang.String)"""
        return str.__wrap(__Identifier.testPath(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def map(self, arg0: 'UnaryOperator', arg1: 'UnaryOperator') -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.map(java.util.function.UnaryOperator<java.lang.String>,java.util.function.UnaryOperator<java.lang.String>)"""
        return 'Identifier'.__wrap(super(__Identifier, self).map(arg0, arg1))

    @staticmethod
    @overload
    def testNamespace(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.util.Identifier.testNamespace(java.lang.String)"""
        return str.__wrap(__Identifier.testNamespace(arg0))