from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.util.Shutdownable as _Shutdownable
_Shutdownable = _Shutdownable
from abc import abstractmethod, ABC
 
class Shutdownable():
    """dev.ultreon.quantum.util.Shutdownable"""
 
    @staticmethod
    def _wrap(java_value: _Shutdownable) -> 'Shutdownable':
        return Shutdownable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Shutdownable):
        """
        Dynamic initializer for Shutdownable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Shutdownable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Shutdownable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def shutdown(self, ):
        """public abstract void dev.ultreon.quantum.util.Shutdownable.shutdown() throws java.lang.InterruptedException"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.util.Shutdownable
import dev.ultreon.quantum.util.Shutdownable as _Shutdownable
_Shutdownable = _Shutdownable
from abc import abstractmethod, ABC
 
class Shutdownable():
    """dev.ultreon.quantum.util.Shutdownable"""
 
    @staticmethod
    def _wrap(java_value: _Shutdownable) -> 'Shutdownable':
        return Shutdownable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Shutdownable):
        """
        Dynamic initializer for Shutdownable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Shutdownable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Shutdownable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import dev.ultreon.quantum.util.DataSizes as _DataSizes_Unit
_Unit = _DataSizes_Unit.Unit
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Unit():
    """dev.ultreon.quantum.util.DataSizes.Unit"""
 
    @staticmethod
    def _wrap(java_value: _Unit) -> 'Unit':
        return Unit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Unit):
        """
        Dynamic initializer for Unit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Unit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Unit__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Unit':
        """public static dev.ultreon.quantum.util.DataSizes$Unit dev.ultreon.quantum.util.DataSizes$Unit.valueOf(java.lang.String)"""
        return Unit._wrap(_Unit.valueOf(arg0))

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
    def values() -> List['Unit']:
        """public static dev.ultreon.quantum.util.DataSizes$Unit[] dev.ultreon.quantum.util.DataSizes$Unit.values()"""
        return List[Unit]._wrap(_Unit.values())

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


Unit.MiB = Unit._wrap(_MiB.MiB)

Unit.KiB = Unit._wrap(_KiB.KiB)

Unit.PiB = Unit._wrap(_PiB.PiB)

Unit.GiB = Unit._wrap(_GiB.GiB)

Unit.B = Unit._wrap(_B.B)

Unit.TiB = Unit._wrap(_TiB.TiB)

Unit.EiB = Unit._wrap(_EiB.EiB) 
 
 
# CLASS: dev.ultreon.quantum.util.Color
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import dev.ultreon.quantum.util.Color as _Color
_Color = _Color
import java.lang.Integer as _int
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

 
class Color():
    """dev.ultreon.quantum.util.Color"""
 
    @staticmethod
    def _wrap(java_value: _Color) -> 'Color':
        return Color(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Color):
        """
        Dynamic initializer for Color.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Color__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Color__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def withBlue(self, arg0: int) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withBlue(int)"""
        return 'Color'._wrap(super(_Color, self).withBlue(_int.valueOf(arg0)))

    @overload
    def withGreen(self, arg0: int) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withGreen(int)"""
        return 'Color'._wrap(super(_Color, self).withGreen(_int.valueOf(arg0)))

    @overload
    def toHex(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.util.Color.toHex()"""
        return str._wrap(super(Color, self).toHex())

    @overload
    def darker(self) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.darker()"""
        return 'Color'._wrap(super(Color, self).darker())

    @overload
    def withRed(self, arg0: int) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withRed(int)"""
        return 'Color'._wrap(super(_Color, self).withRed(_int.valueOf(arg0)))

    @overload
    def toGdx(self) -> 'graphics.Color':
        """public default com.badlogic.gdx.graphics.Color dev.ultreon.quantum.util.Color.toGdx()"""
        return 'graphics.Color'._wrap(super(Color, self).toGdx())

    @overload
    def lighter(self) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.lighter()"""
        return 'Color'._wrap(super(Color, self).lighter())

    @overload
    def withAlpha(self, arg0: int) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withAlpha(int)"""
        return 'Color'._wrap(super(_Color, self).withAlpha(_int.valueOf(arg0)))

    @abstractmethod
    def getBlue(self, ):
        """public abstract int dev.ultreon.quantum.util.Color.getBlue()"""
        pass

    @staticmethod
    @overload
    def fromGdx(arg0: 'Color') -> 'Color':
        """public static dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.fromGdx(com.badlogic.gdx.graphics.Color)"""
        return Color._wrap(_Color.fromGdx(arg0))

    @abstractmethod
    def getGreen(self, ):
        """public abstract int dev.ultreon.quantum.util.Color.getGreen()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.util.Result
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Result():
    """dev.ultreon.quantum.util.Result"""
 
    @staticmethod
    def _wrap(java_value: _Result) -> 'Result':
        return Result(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Result):
        """
        Dynamic initializer for Result.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Result__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Result__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def unwrapOr(self, arg0: object) -> object:
        """public T dev.ultreon.quantum.util.Result.unwrapOr(T)"""
        return object._wrap(super(_Result, self).unwrapOr(arg0))

    @overload
    def expectFailure(self, arg0: str) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.expectFailure(java.lang.String)"""
        return 'Throwable'._wrap(super(_Result, self).expectFailure(arg0))

    @overload
    def isFailure(self) -> bool:
        """public boolean dev.ultreon.quantum.util.Result.isFailure()"""
        return bool._wrap(super(Result, self).isFailure())

    @overload
    def getValueOrNull(self) -> object:
        """public T dev.ultreon.quantum.util.Result.getValueOrNull()"""
        return object._wrap(super(Result, self).getValueOrNull())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def unwrapFailure(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.unwrapFailure()"""
        return 'Throwable'._wrap(super(Result, self).unwrapFailure())

    @overload
    def getValueOr(self, arg0: object) -> object:
        """public T dev.ultreon.quantum.util.Result.getValueOr(T)"""
        return object._wrap(super(_Result, self).getValueOr(arg0))

    @overload
    def unwrap(self) -> object:
        """public T dev.ultreon.quantum.util.Result.unwrap()"""
        return object._wrap(super(Result, self).unwrap())

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
    def getFailure(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.getFailure()"""
        return 'Throwable'._wrap(super(Result, self).getFailure())

    @overload
    def getValueOrGet(self, arg0: 'Supplier') -> object:
        """public T dev.ultreon.quantum.util.Result.getValueOrGet(java.util.function.Supplier<? extends T>)"""
        return object._wrap(super(_Result, self).getValueOrGet(arg0))

    @overload
    def getOk(self) -> object:
        """public T dev.ultreon.quantum.util.Result.getOk()"""
        return object._wrap(super(Result, self).getOk())

    @overload
    def ifAny(self, arg0: 'Consumer', arg1: 'Consumer'):
        """public void dev.ultreon.quantum.util.Result.ifAny(java.util.function.Consumer<T>,java.util.function.Consumer<java.lang.Throwable>)"""
        super(_Result, self).ifAny(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def expect(self, arg0: str) -> object:
        """public T dev.ultreon.quantum.util.Result.expect(java.lang.String)"""
        return object._wrap(super(_Result, self).expect(arg0))

    @overload
    def ifValue(self, arg0: 'Consumer'):
        """public void dev.ultreon.quantum.util.Result.ifValue(java.util.function.Consumer<T>)"""
        super(_Result, self).ifValue(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getFailureOrNull(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.getFailureOrNull()"""
        return 'Throwable'._wrap(super(Result, self).getFailureOrNull())

    @staticmethod
    @overload
    def ok(arg0: object) -> 'Result':
        """public static <T> dev.ultreon.quantum.util.Result<T> dev.ultreon.quantum.util.Result.ok(T)"""
        return Result._wrap(_Result.ok(arg0))

    @staticmethod
    @overload
    def ok() -> 'Result':
        """public static dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.util.Result.ok()"""
        return Result._wrap(_Result.ok())

    @overload
    def ifValueOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.quantum.util.Result.ifValueOrElse(java.util.function.Consumer<T>,java.lang.Runnable)"""
        super(_Result, self).ifValueOrElse(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isOk(self) -> bool:
        """public boolean dev.ultreon.quantum.util.Result.isOk()"""
        return bool._wrap(super(Result, self).isOk())

    @overload
    def getFailureOrGet(self, arg0: 'Supplier') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.getFailureOrGet(java.util.function.Supplier<? extends java.lang.Throwable>)"""
        return 'Throwable'._wrap(super(_Result, self).getFailureOrGet(arg0))

    @overload
    def unwrapOrGet(self, arg0: 'Supplier') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.unwrapOrGet(java.util.function.Supplier<? extends java.lang.Throwable>)"""
        return 'Throwable'._wrap(super(_Result, self).unwrapOrGet(arg0))

    @overload
    def ifFailure(self, arg0: 'Consumer'):
        """public void dev.ultreon.quantum.util.Result.ifFailure(java.util.function.Consumer<java.lang.Throwable>)"""
        super(_Result, self).ifFailure(arg0)

    @overload
    def ifFailureOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.quantum.util.Result.ifFailureOrElse(java.util.function.Consumer<java.lang.Throwable>,java.lang.Runnable)"""
        super(_Result, self).ifFailureOrElse(arg0, arg1)

    @overload
    def map(self, arg0: 'Function', arg1: 'Function') -> 'Result':
        """public <R> dev.ultreon.quantum.util.Result<R> dev.ultreon.quantum.util.Result.map(java.util.function.Function<T, R>,java.util.function.Function<java.lang.Throwable, java.lang.Throwable>)"""
        return 'Result'._wrap(super(_Result, self).map(arg0, arg1))

    @staticmethod
    @overload
    def failure(arg0: 'Throwable') -> 'Result':
        """public static <T> dev.ultreon.quantum.util.Result<T> dev.ultreon.quantum.util.Result.failure(java.lang.Throwable)"""
        return Result._wrap(_Result.failure(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getFailureOr(self, arg0: 'Throwable') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.util.Result.getFailureOr(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Result, self).getFailureOr(arg0))

    @overload
    def flatMap(self, arg0: 'Function', arg1: 'Function') -> object:
        """public <R> R dev.ultreon.quantum.util.Result.flatMap(java.util.function.Function<T, R>,java.util.function.Function<java.lang.Throwable, R>)"""
        return object._wrap(super(_Result, self).flatMap(arg0, arg1))

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
 
 
# CLASS: dev.ultreon.quantum.util.Task
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.util.Task as _Task
_Task = _Task
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Task():
    """dev.ultreon.quantum.util.Task"""
 
    @staticmethod
    def _wrap(java_value: _Task) -> 'Task':
        return Task(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Task):
        """
        Dynamic initializer for Task.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Task__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Task__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, arg0: 'Identifier', arg1: 'Runnable'):
        """public dev.ultreon.quantum.util.Task(dev.ultreon.quantum.util.Identifier,java.lang.Runnable)"""
        val = _Task(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.util.Task.get()"""
        return object._wrap(super(Task, self).get())

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
    def run(self):
        """public void dev.ultreon.quantum.util.Task.run()"""
        super(Task, self).run()

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Supplier'):
        """public dev.ultreon.quantum.util.Task(dev.ultreon.quantum.util.Identifier,java.util.function.Supplier<T>)"""
        val = _Task(arg0, arg1)
        self.__wrapper = val

    @overload
    def id(self) -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Task.id()"""
        return 'Identifier'._wrap(super(Task, self).id())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.util.Task(dev.ultreon.quantum.util.Identifier)"""
        val = _Task(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.util.BoundingBox
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.Integer as _int
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import java.lang.Long as _long
import java.util.List as List
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BoundingBox():
    """dev.ultreon.quantum.util.BoundingBox"""
 
    @staticmethod
    def _wrap(java_value: _BoundingBox) -> 'BoundingBox':
        return BoundingBox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BoundingBox):
        """
        Dynamic initializer for BoundingBox.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BoundingBox__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BoundingBox__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getCorner100(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner100(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCorner100(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'List') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.set(java.util.List<dev.ultreon.libs.commons.v0.vector.Vec3d>)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).set(arg0))

    @overload
    def getCorner101(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner101(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCorner101(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.BoundingBox.toString()"""
        return str._wrap(super(BoundingBox, self).toString())

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
    def isValid(self) -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.isValid()"""
        return bool._wrap(super(BoundingBox, self).isValid())

    @overload
    def getCenterX(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getCenterX()"""
        return float._wrap(super(BoundingBox, self).getCenterX())

    @overload
    def getCorner110(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner110(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCorner110(arg0))

    @overload
    def getCorner111(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner111(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCorner111(arg0))

    @overload
    def getCenterY(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getCenterY()"""
        return float._wrap(super(BoundingBox, self).getCenterY())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.BoundingBox()"""
        val = _BoundingBox()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getCorner010(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner010(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCorner010(arg0))

    @overload
    def ext(self, arg0: 'Vec3d', arg1: float) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.ext(dev.ultreon.libs.commons.v0.vector.Vec3d,double)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(arg0, _double.valueOf(arg1)))

    @overload
    def getMin(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getMin(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getMin(arg0))

    @overload
    def updateByDelta(self, arg0: float, arg1: float, arg2: float) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.updateByDelta(double,double,double)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).updateByDelta(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def getWidth(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getWidth()"""
        return float._wrap(super(BoundingBox, self).getWidth())

    @overload
    def intersects(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.intersects(dev.ultreon.quantum.util.BoundingBox)"""
        return bool._wrap(super(_BoundingBox, self).intersects(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public dev.ultreon.quantum.util.BoundingBox(double,double,double,double,double,double)"""
        val = _BoundingBox(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4), _double.valueOf(arg5))
        self.__wrapper = val

    @overload
    def set(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.set(dev.ultreon.quantum.util.BoundingBox)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).set(arg0))

    @overload
    def ext(self, arg0: float, arg1: float, arg2: float) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.ext(double,double,double)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def contains(self, arg0: 'Vec3d') -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.contains(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return bool._wrap(super(_BoundingBox, self).contains(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'BoundingBox'):
        """public dev.ultreon.quantum.util.BoundingBox(dev.ultreon.quantum.util.BoundingBox)"""
        val = _BoundingBox(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def ext(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.ext(dev.ultreon.quantum.util.BoundingBox)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(arg0))

    @overload
    def getCenter(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCenter(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCenter(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.BoundingBox()"""
        val = _BoundingBox()
        self.__wrapper = val

    @overload
    def getHeight(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getHeight()"""
        return float._wrap(super(BoundingBox, self).getHeight())

    @overload
    def getDimensions(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getDimensions(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getDimensions(arg0))

    @overload
    def intersectsExclusive(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.intersectsExclusive(dev.ultreon.quantum.util.BoundingBox)"""
        return bool._wrap(super(_BoundingBox, self).intersectsExclusive(arg0))

    @overload
    def inf(self) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.inf()"""
        return 'BoundingBox'._wrap(super(BoundingBox, self).inf())

    @overload
    def getMax(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getMax(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getMax(arg0))

    @overload
    def getCorner000(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner000(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCorner000(arg0))

    @overload
    def getCorner001(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner001(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCorner001(arg0))

    @overload
    def ext(self, arg0: 'Vec3d') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.ext(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(arg0))

    @overload
    def getCenterZ(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getCenterZ()"""
        return float._wrap(super(BoundingBox, self).getCenterZ())

    @overload
    def set(self, arg0: 'Vec3d') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.set(dev.ultreon.libs.commons.v0.vector.Vec3d[])"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Vec3d', arg1: 'Vec3d'):
        """public dev.ultreon.quantum.util.BoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _BoundingBox(arg0, arg1)
        self.__wrapper = val

    @overload
    def getDepth(self) -> float:
        """public double dev.ultreon.quantum.util.BoundingBox.getDepth()"""
        return float._wrap(super(BoundingBox, self).getDepth())

    @overload
    def set(self, arg0: 'Vec3d', arg1: 'Vec3d') -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.set(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).set(arg0, arg1))

    @overload
    def getCorner011(self, arg0: 'Vec3d') -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BoundingBox.getCorner011(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'vector.Vec3d'._wrap(super(_BoundingBox, self).getCorner011(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def clr(self) -> 'BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBox.clr()"""
        return 'BoundingBox'._wrap(super(BoundingBox, self).clr())

    @overload
    def update(self):
        """public void dev.ultreon.quantum.util.BoundingBox.update()"""
        super(BoundingBox, self).update()

    @overload
    def contains(self, arg0: 'BoundingBox') -> bool:
        """public boolean dev.ultreon.quantum.util.BoundingBox.contains(dev.ultreon.quantum.util.BoundingBox)"""
        return bool._wrap(super(_BoundingBox, self).contains(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.util.RandomValueSource
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.util.RandomValueSource as _RandomValueSource
_RandomValueSource = _RandomValueSource
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.Random as Random
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RandomValueSource():
    """dev.ultreon.quantum.util.RandomValueSource"""
 
    @staticmethod
    def _wrap(java_value: _RandomValueSource) -> 'RandomValueSource':
        return RandomValueSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RandomValueSource):
        """
        Dynamic initializer for RandomValueSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RandomValueSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RandomValueSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of(arg0: 'Random', arg1: float, arg2: float) -> 'RandomValueSource':
        """public static dev.ultreon.quantum.util.RandomValueSource dev.ultreon.quantum.util.RandomValueSource.of(java.util.Random,double,double)"""
        return RandomValueSource._wrap(_RandomValueSource.of(arg0, _double.valueOf(arg1), _double.valueOf(arg2)))

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
    def getValue(self) -> float:
        """public double dev.ultreon.quantum.util.RandomValueSource.getValue()"""
        return float._wrap(super(RandomValueSource, self).getValue())

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
 
 
# CLASS: dev.ultreon.quantum.util.IllegalThreadError
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
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.quantum.util.IllegalThreadError as _IllegalThreadError
_IllegalThreadError = _IllegalThreadError
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IllegalThreadError():
    """dev.ultreon.quantum.util.IllegalThreadError"""
 
    @staticmethod
    def _wrap(java_value: _IllegalThreadError) -> 'IllegalThreadError':
        return IllegalThreadError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IllegalThreadError):
        """
        Dynamic initializer for IllegalThreadError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IllegalThreadError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IllegalThreadError__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.quantum.util.IllegalThreadError()"""
        val = _IllegalThreadError()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.IllegalThreadError()"""
        val = _IllegalThreadError()
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.IllegalThreadError(java.lang.String)"""
        val = _IllegalThreadError(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.util.Env
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.util.Env as _Env
_Env = _Env
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
 
class Env():
    """dev.ultreon.quantum.util.Env"""
 
    @staticmethod
    def _wrap(java_value: _Env) -> 'Env':
        return Env(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Env):
        """
        Dynamic initializer for Env.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Env__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Env__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Env':
        """public static dev.ultreon.quantum.util.Env dev.ultreon.quantum.util.Env.valueOf(java.lang.String)"""
        return Env._wrap(_Env.valueOf(arg0))

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
    def values() -> List['Env']:
        """public static dev.ultreon.quantum.util.Env[] dev.ultreon.quantum.util.Env.values()"""
        return List[Env]._wrap(_Env.values())


Env.SERVER = Env._wrap(_SERVER.SERVER)

Env.CLIENT = Env._wrap(_CLIENT.CLIENT) 
 
 
# CLASS: dev.ultreon.quantum.util.PagedList
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.util.PagedList as _PagedList
_PagedList = _PagedList
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PagedList():
    """dev.ultreon.quantum.util.PagedList"""
 
    @staticmethod
    def _wrap(java_value: _PagedList) -> 'PagedList':
        return PagedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PagedList):
        """
        Dynamic initializer for PagedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PagedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PagedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: int, arg1: int) -> object:
        """public T dev.ultreon.quantum.util.PagedList.get(int,int)"""
        return object._wrap(super(_PagedList, self).get(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getFullPage(self, arg0: int) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.util.PagedList.getFullPage(int)"""
        return 'List'._wrap(super(_PagedList, self).getFullPage(_int.valueOf(arg0)))

    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(_ArrayList, self).addLast(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int._wrap(super(ArrayList, self).hashCode())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_ArrayList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object._wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'._wrap(super(ArrayList, self).listIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(_ArrayList, self).add(_int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).removeAll(arg0))

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
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool._wrap(super(_ArrayList, self).add(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool._wrap(super(ArrayList, self).isEmpty())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_ArrayList, self).removeIf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).indexOf(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.util.PagedList(int)"""
        val = _PagedList(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'Collection'):
        """public dev.ultreon.quantum.util.PagedList(int,java.util.Collection<? extends T>)"""
        val = _PagedList(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'._wrap(super(ArrayList, self).spliterator())

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(_ArrayList, self).ensureCapacity(_int.valueOf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(_ArrayList, self).forEach(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(_ArrayList, self).addFirst(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(_ArrayList, self).sort(arg0)

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object._wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object._wrap(super(ArrayList, self).clone())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object._wrap(super(_ArrayList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object]._wrap(super(_ArrayList, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(arg0))

    @overload
    def __init__(self, arg0: 'PagedList'):
        """public dev.ultreon.quantum.util.PagedList(dev.ultreon.quantum.util.PagedList<? extends T>)"""
        val = _PagedList(arg0)
        self.__wrapper = val

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object._wrap(super(_ArrayList, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object._wrap(super(ArrayList, self).getLast())

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).lastIndexOf(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'._wrap(super(_ArrayList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).contains(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object._wrap(super(_ArrayList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int._wrap(super(ArrayList, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object]._wrap(super(ArrayList, self).toArray())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object._wrap(super(ArrayList, self).removeLast())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.util.PagedList(int,int)"""
        val = _PagedList(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'._wrap(super(ArrayList, self).iterator()) 
 
 
# CLASS: dev.ultreon.quantum.util.Hashing
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.util.Hashing as _Hashing
_Hashing = _Hashing
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Hashing():
    """dev.ultreon.quantum.util.Hashing"""
 
    @staticmethod
    def _wrap(java_value: _Hashing) -> 'Hashing':
        return Hashing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Hashing):
        """
        Dynamic initializer for Hashing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Hashing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Hashing__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.quantum.util.Hashing()"""
        val = _Hashing()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.Hashing()"""
        val = _Hashing()
        self.__wrapper = val

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
    def hashMD5(arg0: bytes) -> List[int]:
        """public static byte[] dev.ultreon.quantum.util.Hashing.hashMD5(byte[])"""
        return List[int]._wrap(_Hashing.hashMD5(bytes))

    @staticmethod
    @overload
    def verifyMD5(arg0: bytes, arg1: bytes) -> bool:
        """public static boolean dev.ultreon.quantum.util.Hashing.verifyMD5(byte[],byte[])"""
        return bool._wrap(_Hashing.verifyMD5(bytes, bytes))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.WorldRayCaster
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.util.WorldRayCaster as _WorldRayCaster
_WorldRayCaster = _WorldRayCaster
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.util.BlockHitResult as _BlockHitResult
_BlockHitResult = _BlockHitResult
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldRayCaster():
    """dev.ultreon.quantum.util.WorldRayCaster"""
 
    @staticmethod
    def _wrap(java_value: _WorldRayCaster) -> 'WorldRayCaster':
        return WorldRayCaster(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldRayCaster):
        """
        Dynamic initializer for WorldRayCaster.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldRayCaster__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldRayCaster__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public dev.ultreon.quantum.util.WorldRayCaster()"""
        val = _WorldRayCaster()
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def rayCast(arg0: 'World') -> 'BlockHitResult':
        """public static dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.util.WorldRayCaster.rayCast(dev.ultreon.quantum.world.World)"""
        return BlockHitResult._wrap(_WorldRayCaster.rayCast(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def rayCast(arg0: 'BlockHitResult', arg1: 'World', arg2: 'BlockMetaPredicate') -> 'BlockHitResult':
        """public static dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.util.WorldRayCaster.rayCast(dev.ultreon.quantum.util.BlockHitResult,dev.ultreon.quantum.world.World,dev.ultreon.quantum.util.BlockMetaPredicate)"""
        return BlockHitResult._wrap(_WorldRayCaster.rayCast(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def rayCast(arg0: 'BlockHitResult', arg1: 'World') -> 'BlockHitResult':
        """public static dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.util.WorldRayCaster.rayCast(dev.ultreon.quantum.util.BlockHitResult,dev.ultreon.quantum.world.World)"""
        return BlockHitResult._wrap(_WorldRayCaster.rayCast(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.WorldRayCaster()"""
        val = _WorldRayCaster()
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
 
 
# CLASS: dev.ultreon.quantum.util.HexTable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import dev.ultreon.quantum.util.HexTable as _HexTable
_HexTable = _HexTable
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HexTable():
    """dev.ultreon.quantum.util.HexTable"""
 
    @staticmethod
    def _wrap(java_value: _HexTable) -> 'HexTable':
        return HexTable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HexTable):
        """
        Dynamic initializer for HexTable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HexTable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HexTable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.HexTable()"""
        val = _HexTable()
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

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def dumpHexTable(arg0: bytes):
        """public static void dev.ultreon.quantum.util.HexTable.dumpHexTable(byte[])"""
        _HexTable.dumpHexTable(bytes)

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
        """public dev.ultreon.quantum.util.HexTable()"""
        val = _HexTable()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.MathHelper
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import dev.ultreon.quantum.util.MathHelper as _MathHelper
_MathHelper = _MathHelper
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MathHelper():
    """dev.ultreon.quantum.util.MathHelper"""
 
    @staticmethod
    def _wrap(java_value: _MathHelper) -> 'MathHelper':
        return MathHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MathHelper):
        """
        Dynamic initializer for MathHelper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MathHelper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MathHelper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def rotateZ(arg0: 'float', arg1: float, arg2: 'Vector3'):
        """public static void dev.ultreon.quantum.util.MathHelper.rotateZ(float[],float,com.badlogic.gdx.math.Vector3)"""
        _MathHelper.rotateZ(arg0, _float.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float dev.ultreon.quantum.util.MathHelper.lerp(float,float,float)"""
        return float._wrap(_MathHelper.lerp(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

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
    def rotateX(arg0: 'float', arg1: float, arg2: 'Vector3'):
        """public static void dev.ultreon.quantum.util.MathHelper.rotateX(float[],float,com.badlogic.gdx.math.Vector3)"""
        _MathHelper.rotateX(arg0, _float.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def round(arg0: 'Vec2f') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.util.MathHelper.round(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return vector.Vec2i._wrap(_MathHelper.round(arg0))

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
    def round(arg0: 'Vec3f') -> 'vector.Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.MathHelper.round(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return vector.Vec3i._wrap(_MathHelper.round(arg0))

    @staticmethod
    @overload
    def round(arg0: 'Vec2d') -> 'vector.Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.util.MathHelper.round(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return vector.Vec2i._wrap(_MathHelper.round(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.MathHelper()"""
        val = _MathHelper()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.MathHelper()"""
        val = _MathHelper()
        self.__wrapper = val

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.quantum.util.MathHelper.lerp(double,double,double)"""
        return float._wrap(_MathHelper.lerp(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def rotateY(arg0: 'float', arg1: float, arg2: 'Vector3'):
        """public static void dev.ultreon.quantum.util.MathHelper.rotateY(float[],float,com.badlogic.gdx.math.Vector3)"""
        _MathHelper.rotateY(arg0, _float.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def rotate(arg0: 'float', arg1: 'Vector3', arg2: 'Axis') -> List[float]:
        """public static float[] dev.ultreon.quantum.util.MathHelper.rotate(float[],com.badlogic.gdx.math.Vector3,dev.ultreon.quantum.util.Axis)"""
        return List[float]._wrap(_MathHelper.rotate(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.Suppliers
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.util.Suppliers as _Suppliers
_Suppliers = _Suppliers
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Suppliers():
    """dev.ultreon.quantum.util.Suppliers"""
 
    @staticmethod
    def _wrap(java_value: _Suppliers) -> 'Suppliers':
        return Suppliers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Suppliers):
        """
        Dynamic initializer for Suppliers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Suppliers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Suppliers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def memoizeWithExpiration(arg0: 'Supplier', arg1: int, arg2: 'TimeUnit') -> 'Supplier':
        """public static <T> java.util.function.Supplier<T> dev.ultreon.quantum.util.Suppliers.memoizeWithExpiration(java.util.function.Supplier<T>,int,java.util.concurrent.TimeUnit)"""
        return Supplier._wrap(_Suppliers.memoizeWithExpiration(arg0, _int.valueOf(arg1), arg2))

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
    def memoize(arg0: 'Supplier') -> 'Supplier':
        """public static <T> java.util.function.Supplier<T> dev.ultreon.quantum.util.Suppliers.memoize(java.util.function.Supplier<T>)"""
        return Supplier._wrap(_Suppliers.memoize(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.util.Numbers
import java.lang.Boolean as Boolean
from builtins import str
import dev.ultreon.quantum.util.Numbers as _Numbers
_Numbers = _Numbers
import java.lang.Long as Long
from pyquantum_helper import override
import java.lang.Short as Short
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Float as Float
import java.lang.String as _String
_String = _String
import java.lang.Byte as Byte
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Integer as Integer
from builtins import bool
import java.lang.Double as Double
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Numbers():
    """dev.ultreon.quantum.util.Numbers"""
 
    @staticmethod
    def _wrap(java_value: _Numbers) -> 'Numbers':
        return Numbers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Numbers):
        """
        Dynamic initializer for Numbers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Numbers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Numbers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toFloatOrNull(toFloatOrNull) -> 'Float':
        """public static java.lang.Float dev.ultreon.quantum.util.Numbers.toFloatOrNull(java.lang.String)"""
        return _transform(_arg0.Numbers(arg0: str)).'Float'Value()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.Numbers()"""
        val = _Numbers()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.Numbers()"""
        val = _Numbers()
        self.__wrapper = val

    @staticmethod
    @overload
    def toByteOrNull(toByteOrNull) -> 'Byte':
        """public static java.lang.Byte dev.ultreon.quantum.util.Numbers.toByteOrNull(java.lang.String)"""
        return _transform(_arg0.Numbers(arg0: str)).'Byte'Value()

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

    @staticmethod
    @overload
    def toLongOrNull(toLongOrNull) -> 'Long':
        """public static java.lang.Long dev.ultreon.quantum.util.Numbers.toLongOrNull(java.lang.String)"""
        return _transform(_arg0.Numbers(arg0: str)).'Long'Value()

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
    def toBooleanOrNull(arg0: str) -> 'Boolean':
        """public static java.lang.Boolean dev.ultreon.quantum.util.Numbers.toBooleanOrNull(java.lang.String)"""
        return Boolean._wrap(_Numbers.toBooleanOrNull(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toIntOrNull(toIntOrNull) -> 'Integer':
        """public static java.lang.Integer dev.ultreon.quantum.util.Numbers.toIntOrNull(java.lang.String)"""
        return _transform(_arg0.Numbers(arg0: str)).'Integer'Value()

    @staticmethod
    @overload
    def toDoubleOrNull(toDoubleOrNull) -> 'Double':
        """public static java.lang.Double dev.ultreon.quantum.util.Numbers.toDoubleOrNull(java.lang.String)"""
        return _transform(_arg0.Numbers(arg0: str)).'Double'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toShortOrNull(toShortOrNull) -> 'Short':
        """public static java.lang.Short dev.ultreon.quantum.util.Numbers.toShortOrNull(java.lang.String)"""
        return _transform(_arg0.Numbers(arg0: str)).'Short'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.ArgParser
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import java.lang.Integer as _int
import dev.ultreon.quantum.util.ArgParser as _ArgParser
_ArgParser = _ArgParser
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArgParser():
    """dev.ultreon.quantum.util.ArgParser"""
 
    @staticmethod
    def _wrap(java_value: _ArgParser) -> 'ArgParser':
        return ArgParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArgParser):
        """
        Dynamic initializer for ArgParser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArgParser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArgParser__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getArgv(self) -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.util.ArgParser.getArgv()"""
        return 'List'._wrap(super(ArgParser, self).getArgv())

    @overload
    def __init__(self, *arg0: str):
        """public dev.ultreon.quantum.util.ArgParser(java.lang.String...)"""
        val = _ArgParser(arg0)
        self.__wrapper = val

    @overload
    def getFlags(self) -> 'Set':
        """public java.util.Set<java.lang.String> dev.ultreon.quantum.util.ArgParser.getFlags()"""
        return 'Set'._wrap(super(ArgParser, self).getFlags())

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getKeywordArgs(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> dev.ultreon.quantum.util.ArgParser.getKeywordArgs()"""
        return 'Map'._wrap(super(ArgParser, self).getKeywordArgs())

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
    def getArgs(self) -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.util.ArgParser.getArgs()"""
        return 'List'._wrap(super(ArgParser, self).getArgs())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.RgbColor
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import dev.ultreon.quantum.util.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RgbColor():
    """dev.ultreon.quantum.util.RgbColor"""
 
    @staticmethod
    def _wrap(java_value: _RgbColor) -> 'RgbColor':
        return RgbColor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RgbColor):
        """
        Dynamic initializer for RgbColor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RgbColor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RgbColor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.RgbColor.toString()"""
        return str._wrap(super(RgbColor, self).toString())

    @staticmethod
    @overload
    def abgr(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.abgr(int)"""
        return RgbColor._wrap(_RgbColor.abgr(_int.valueOf(arg0)))

    @override
    @overload
    def toGdx(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color dev.ultreon.quantum.util.RgbColor.toGdx()"""
        return 'graphics.Color'._wrap(super(RgbColor, self).toGdx())

    @override
    @overload
    def getBlue(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getBlue()"""
        return int._wrap(super(RgbColor, self).getBlue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def withGreen(self, arg0: int) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.withGreen(int)"""
        return 'RgbColor'._wrap(super(_RgbColor, self).withGreen(_int.valueOf(arg0)))

    @overload
    def brighter(self) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.brighter()"""
        return 'RgbColor'._wrap(super(RgbColor, self).brighter())

    @overload
    def withRed(self, arg0: int) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.withRed(int)"""
        return 'RgbColor'._wrap(super(_RgbColor, self).withRed(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def of(arg0: 'ColorCode') -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.of(dev.ultreon.quantum.text.ColorCode)"""
        return RgbColor._wrap(_RgbColor.of(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def rgb(arg0: int, arg1: int, arg2: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgb(int,int,int)"""
        return RgbColor._wrap(_RgbColor.rgb(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toHex(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.util.Color.toHex()"""
        return str._wrap(super(Color, self).toHex())

    @staticmethod
    @overload
    def rgba(arg0: float, arg1: float, arg2: float, arg3: float) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgba(float,float,float,float)"""
        return RgbColor._wrap(_RgbColor.rgba(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def argb(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.argb(int)"""
        return RgbColor._wrap(_RgbColor.argb(_int.valueOf(arg0)))

    @override
    @overload
    def darker(self) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.darker()"""
        return 'RgbColor'._wrap(super(RgbColor, self).darker())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.quantum.util.RgbColor(float,float,float,float)"""
        val = _RgbColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @staticmethod
    @overload
    def gdx(arg0: 'Color') -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.gdx(com.badlogic.gdx.graphics.Color)"""
        return RgbColor._wrap(_RgbColor.gdx(arg0))

    @overload
    def withAlpha(self, arg0: int) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.withAlpha(int)"""
        return 'RgbColor'._wrap(super(_RgbColor, self).withAlpha(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def withBlue(self, arg0: int) -> 'RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.withBlue(int)"""
        return 'RgbColor'._wrap(super(_RgbColor, self).withBlue(_int.valueOf(arg0)))

    @override
    @overload
    def lighter(self) -> 'Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.lighter()"""
        return 'Color'._wrap(super(Color, self).lighter())

    @staticmethod
    @overload
    def rgba(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgba(int)"""
        return RgbColor._wrap(_RgbColor.rgba(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def bgra(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.bgra(int)"""
        return RgbColor._wrap(_RgbColor.bgra(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def rgba(arg0: int, arg1: int, arg2: int, arg3: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgba(int,int,int,int)"""
        return RgbColor._wrap(_RgbColor.rgba(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def hex(arg0: str) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.hex(java.lang.String)"""
        return RgbColor._wrap(_RgbColor.hex(arg0))

    @staticmethod
    @overload
    def bgr(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.bgr(int)"""
        return RgbColor._wrap(_RgbColor.bgr(_int.valueOf(arg0)))

    @override
    @overload
    def getAlpha(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getAlpha()"""
        return int._wrap(super(RgbColor, self).getAlpha())

    @override
    @overload
    def getGreen(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getGreen()"""
        return int._wrap(super(RgbColor, self).getGreen())

    @overload
    def getTransparency(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getTransparency()"""
        return int._wrap(super(RgbColor, self).getTransparency())

    @override
    @overload
    def getRed(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getRed()"""
        return int._wrap(super(RgbColor, self).getRed())

    @staticmethod
    @overload
    def hsb(arg0: float, arg1: float, arg2: float) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.hsb(float,float,float)"""
        return RgbColor._wrap(_RgbColor.hsb(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def rgb(arg0: int) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgb(int)"""
        return RgbColor._wrap(_RgbColor.rgb(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getRgb(self) -> int:
        """public int dev.ultreon.quantum.util.RgbColor.getRgb()"""
        return int._wrap(super(RgbColor, self).getRgb())

    @staticmethod
    @overload
    def rgb(arg0: float, arg1: float, arg2: float) -> 'RgbColor':
        """public static dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.util.RgbColor.rgb(float,float,float)"""
        return RgbColor._wrap(_RgbColor.rgb(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

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


RgbColor.MINT = RgbColor._wrap(_MINT.MINT)

RgbColor.BLUE = RgbColor._wrap(_BLUE.BLUE)

RgbColor.WHITE = RgbColor._wrap(_WHITE.WHITE)

RgbColor.GOLD = RgbColor._wrap(_GOLD.GOLD)

RgbColor.RED = RgbColor._wrap(_RED.RED)

RgbColor.ROSE = RgbColor._wrap(_ROSE.ROSE)

RgbColor.ORANGE = RgbColor._wrap(_ORANGE.ORANGE)

RgbColor.YELLOW_GREEN = RgbColor._wrap(_YELLOW_GREEN.YELLOW_GREEN)

RgbColor.AZURE = RgbColor._wrap(_AZURE.AZURE)

RgbColor.BLACK = RgbColor._wrap(_BLACK.BLACK)

RgbColor.YELLOW = RgbColor._wrap(_YELLOW.YELLOW)

RgbColor.MAGENTA = RgbColor._wrap(_MAGENTA.MAGENTA)

RgbColor.GREEN = RgbColor._wrap(_GREEN.GREEN)

RgbColor.TRANSPARENT = RgbColor._wrap(_TRANSPARENT.TRANSPARENT)

RgbColor.DARK_GRAY = RgbColor._wrap(_DARK_GRAY.DARK_GRAY)

RgbColor.GRAY = RgbColor._wrap(_GRAY.GRAY)

RgbColor.LIGHT_GRAY = RgbColor._wrap(_LIGHT_GRAY.LIGHT_GRAY)

RgbColor.CYAN = RgbColor._wrap(_CYAN.CYAN)

RgbColor.PURPLE = RgbColor._wrap(_PURPLE.PURPLE) 
 
 
# CLASS: dev.ultreon.quantum.util.Intersector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Intersector as _Intersector
_Intersector = _Intersector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Intersector():
    """dev.ultreon.quantum.util.Intersector"""
 
    @staticmethod
    def _wrap(java_value: _Intersector) -> 'Intersector':
        return Intersector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Intersector):
        """
        Dynamic initializer for Intersector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Intersector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Intersector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.Intersector()"""
        val = _Intersector()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.Intersector()"""
        val = _Intersector()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def intersectRayBounds(arg0: 'Ray', arg1: 'BoundingBox', arg2: 'Vec3d') -> bool:
        """public static boolean dev.ultreon.quantum.util.Intersector.intersectRayBounds(dev.ultreon.quantum.util.Ray,dev.ultreon.quantum.util.BoundingBox,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return bool._wrap(_Intersector.intersectRayBounds(arg0, arg1, arg2))

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
 
 
# CLASS: dev.ultreon.quantum.util.Copyable
import dev.ultreon.quantum.util.Copyable as _Copyable
_Copyable = _Copyable
from abc import abstractmethod, ABC
 
class Copyable():
    """dev.ultreon.quantum.util.Copyable"""
 
    @staticmethod
    def _wrap(java_value: _Copyable) -> 'Copyable':
        return Copyable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Copyable):
        """
        Dynamic initializer for Copyable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Copyable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Copyable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def cpy(self, ):
        """public abstract T dev.ultreon.quantum.util.Copyable.cpy()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.util.BoundingBoxUtils
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.util.BoundingBoxUtils as _BoundingBoxUtils
_BoundingBoxUtils = _BoundingBoxUtils
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BoundingBoxUtils():
    """dev.ultreon.quantum.util.BoundingBoxUtils"""
 
    @staticmethod
    def _wrap(java_value: _BoundingBoxUtils) -> 'BoundingBoxUtils':
        return BoundingBoxUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BoundingBoxUtils):
        """
        Dynamic initializer for BoundingBoxUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BoundingBoxUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BoundingBoxUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def clipXCollide(arg0: 'BoundingBox', arg1: 'BoundingBox', arg2: float) -> float:
        """public static double dev.ultreon.quantum.util.BoundingBoxUtils.clipXCollide(dev.ultreon.quantum.util.BoundingBox,dev.ultreon.quantum.util.BoundingBox,double)"""
        return float._wrap(_BoundingBoxUtils.clipXCollide(arg0, arg1, _double.valueOf(arg2)))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def clipYCollide(arg0: 'BoundingBox', arg1: 'BoundingBox', arg2: float) -> float:
        """public static double dev.ultreon.quantum.util.BoundingBoxUtils.clipYCollide(dev.ultreon.quantum.util.BoundingBox,dev.ultreon.quantum.util.BoundingBox,double)"""
        return float._wrap(_BoundingBoxUtils.clipYCollide(arg0, arg1, _double.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.BoundingBoxUtils()"""
        val = _BoundingBoxUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def offset(arg0: 'BoundingBox', arg1: float, arg2: float, arg3: float) -> 'BoundingBox':
        """public static dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.util.BoundingBoxUtils.offset(dev.ultreon.quantum.util.BoundingBox,double,double,double)"""
        return BoundingBox._wrap(_BoundingBoxUtils.offset(arg0, _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @staticmethod
    @overload
    def clipZCollide(arg0: 'BoundingBox', arg1: 'BoundingBox', arg2: float) -> float:
        """public static double dev.ultreon.quantum.util.BoundingBoxUtils.clipZCollide(dev.ultreon.quantum.util.BoundingBox,dev.ultreon.quantum.util.BoundingBox,double)"""
        return float._wrap(_BoundingBoxUtils.clipZCollide(arg0, arg1, _double.valueOf(arg2)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.BoundingBoxUtils()"""
        val = _BoundingBoxUtils()
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
 
 
# CLASS: dev.ultreon.quantum.util.ExceptionMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.util.ExceptionMap as _ExceptionMap
_ExceptionMap = _ExceptionMap
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExceptionMap():
    """dev.ultreon.quantum.util.ExceptionMap"""
 
    @staticmethod
    def _wrap(java_value: _ExceptionMap) -> 'ExceptionMap':
        return ExceptionMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExceptionMap):
        """
        Dynamic initializer for ExceptionMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExceptionMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExceptionMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.ExceptionMap()"""
        val = _ExceptionMap()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.ExceptionMap()"""
        val = _ExceptionMap()
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

    @staticmethod
    @overload
    def sendFatal(arg0: 'CommandSender', arg1: 'Throwable', arg2: bool):
        """public static void dev.ultreon.quantum.util.ExceptionMap.sendFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Throwable,boolean)"""
        _ExceptionMap.sendFatal(arg0, arg1, _boolean.valueOf(arg2))

    @staticmethod
    @overload
    def getErrorCode(arg0: 'Throwable') -> str:
        """public static java.lang.String dev.ultreon.quantum.util.ExceptionMap.getErrorCode(java.lang.Throwable)"""
        return str._wrap(_ExceptionMap.getErrorCode(arg0))

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
    def sendFatal(arg0: 'CommandSender', arg1: 'Throwable'):
        """public static void dev.ultreon.quantum.util.ExceptionMap.sendFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Throwable)"""
        _ExceptionMap.sendFatal(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.MathHelper$FaceRotation
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
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import dev.ultreon.quantum.util.MathHelper as _MathHelper_FaceRotation
_FaceRotation = _MathHelper_FaceRotation.FaceRotation
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FaceRotation():
    """dev.ultreon.quantum.util.MathHelper.FaceRotation"""
 
    @staticmethod
    def _wrap(java_value: _FaceRotation) -> 'FaceRotation':
        return FaceRotation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FaceRotation):
        """
        Dynamic initializer for FaceRotation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FaceRotation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FaceRotation__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FaceRotation':
        """public static dev.ultreon.quantum.util.MathHelper$FaceRotation dev.ultreon.quantum.util.MathHelper$FaceRotation.valueOf(java.lang.String)"""
        return FaceRotation._wrap(_FaceRotation.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['FaceRotation']:
        """public static dev.ultreon.quantum.util.MathHelper$FaceRotation[] dev.ultreon.quantum.util.MathHelper$FaceRotation.values()"""
        return List[FaceRotation]._wrap(_FaceRotation.values())

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


FaceRotation.DEGREES_90 = FaceRotation._wrap(_DEGREES_90.DEGREES_90)

FaceRotation.DEGREES_180 = FaceRotation._wrap(_DEGREES_180.DEGREES_180)

FaceRotation.DEGREES_270 = FaceRotation._wrap(_DEGREES_270.DEGREES_270)

FaceRotation.UNCHANGED = FaceRotation._wrap(_UNCHANGED.UNCHANGED) 
 
 
# CLASS: dev.ultreon.quantum.util.ValidationError
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
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import dev.ultreon.quantum.util.ValidationError as _ValidationError
_ValidationError = _ValidationError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValidationError():
    """dev.ultreon.quantum.util.ValidationError"""
 
    @staticmethod
    def _wrap(java_value: _ValidationError) -> 'ValidationError':
        return ValidationError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValidationError):
        """
        Dynamic initializer for ValidationError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValidationError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValidationError__wrapper":
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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.ValidationError(java.lang.String)"""
        val = _ValidationError(arg0)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.PollingExecutorService
from pyquantum_helper import import_once as _import_once
import java.lang.Thread as Thread
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = _import_once("pyquantum.debug.profiler")

import java.util.concurrent.Callable as Callable
from builtins import bool
import dev.ultreon.quantum.debug.profiler.Profiler as _Profiler
_Profiler = _Profiler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
import java.util.concurrent.CompletableFuture as CompletableFuture
import dev.ultreon.quantum.util.PollingExecutorService as _PollingExecutorService
_PollingExecutorService = _PollingExecutorService
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PollingExecutorService():
    """dev.ultreon.quantum.util.PollingExecutorService"""
 
    @staticmethod
    def _wrap(java_value: _PollingExecutorService) -> 'PollingExecutorService':
        return PollingExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PollingExecutorService):
        """
        Dynamic initializer for PollingExecutorService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PollingExecutorService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PollingExecutorService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_PollingExecutorService, self).invokeAny(arg0, _long.valueOf(arg1), arg2))

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isTerminated()"""
        return bool._wrap(super(PollingExecutorService, self).isTerminated())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Thread', arg1: 'Profiler'):
        """public dev.ultreon.quantum.util.PollingExecutorService(java.lang.Thread,dev.ultreon.quantum.debug.profiler.Profiler)"""
        val = _PollingExecutorService(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Profiler'):
        """public dev.ultreon.quantum.util.PollingExecutorService(dev.ultreon.quantum.debug.profiler.Profiler)"""
        val = _PollingExecutorService(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'._wrap(super(_PollingExecutorService, self).invokeAll(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_PollingExecutorService, self).invokeAny(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @property
    def profiler(self) -> Profiler:
        return Profiler._wrap(super(_PollingExecutorService).profiler())

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'._wrap(super(_PollingExecutorService, self).submit(arg0, arg1))

    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(_PollingExecutorService, self).execute(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(PollingExecutorService, self).pollAll()

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'._wrap(super(_PollingExecutorService, self).invokeAll(arg0, _long.valueOf(arg1), arg2))

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'._wrap(super(PollingExecutorService, self).shutdownNow())

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool._wrap(super(PollingExecutorService, self).isShutdown())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'._wrap(super(_PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_PollingExecutorService, self).awaitTermination(_long.valueOf(arg0), arg1))

    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(PollingExecutorService, self).poll()

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'._wrap(super(_PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def shutdown(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.shutdown()"""
        super(PollingExecutorService, self).shutdown()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.HitResult
import dev.ultreon.quantum.util.HitResult as _HitResult
_HitResult = _HitResult
from abc import abstractmethod, ABC
 
class HitResult():
    """dev.ultreon.quantum.util.HitResult"""
 
    @staticmethod
    def _wrap(java_value: _HitResult) -> 'HitResult':
        return HitResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HitResult):
        """
        Dynamic initializer for HitResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HitResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HitResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import java.lang.String as _string
import dev.ultreon.quantum.util.SanityCheckException as _SanityCheckException
_SanityCheckException = _SanityCheckException
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
 
class SanityCheckException():
    """dev.ultreon.quantum.util.SanityCheckException"""
 
    @staticmethod
    def _wrap(java_value: _SanityCheckException) -> 'SanityCheckException':
        return SanityCheckException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SanityCheckException):
        """
        Dynamic initializer for SanityCheckException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SanityCheckException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SanityCheckException__wrapper":
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
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.util.SanityCheckException(java.lang.Throwable)"""
        val = _SanityCheckException(arg0)
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
        """public dev.ultreon.quantum.util.SanityCheckException(java.lang.String,java.lang.Throwable)"""
        val = _SanityCheckException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.SanityCheckException(java.lang.String)"""
        val = _SanityCheckException(arg0)
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.SanityCheckException()"""
        val = _SanityCheckException()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.SanityCheckException()"""
        val = _SanityCheckException()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.EntityHitResult
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.util.EntityHitResult as _EntityHitResult
_EntityHitResult = _EntityHitResult
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
from builtins import float
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.CubicDirection as _CubicDirection
_CubicDirection = _CubicDirection
import dev.ultreon.quantum.util.Ray as _Ray
_Ray = _Ray
import java.lang.Float as _float
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import java.lang.Class as _Class
_Class = _Class
 
class EntityHitResult():
    """dev.ultreon.quantum.util.EntityHitResult"""
 
    @staticmethod
    def _wrap(java_value: _EntityHitResult) -> 'EntityHitResult':
        return EntityHitResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityHitResult):
        """
        Dynamic initializer for EntityHitResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityHitResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityHitResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Ray'):
        """public dev.ultreon.quantum.util.EntityHitResult(dev.ultreon.quantum.util.Ray)"""
        val = _EntityHitResult(arg0)
        self.__wrapper = val

    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.EntityHitResult.getPosition()"""
        return 'vector.Vec3d'._wrap(super(EntityHitResult, self).getPosition())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.EntityHitResult()"""
        val = _EntityHitResult()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.EntityHitResult()"""
        val = _EntityHitResult()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.util.EntityHitResult.hashCode()"""
        return int._wrap(super(EntityHitResult, self).hashCode())

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
    def getPos(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.EntityHitResult.getPos()"""
        return 'vector.Vec3i'._wrap(super(EntityHitResult, self).getPos())

    @overload
    def getNormal(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.EntityHitResult.getNormal()"""
        return 'vector.Vec3d'._wrap(super(EntityHitResult, self).getNormal())

    @property
    def entity(self, value: 'entity.Entity'):
        super(_EntityHitResult).entity(value)

    @overload
    def getDirection(self) -> 'world.CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.util.EntityHitResult.getDirection()"""
        return 'world.CubicDirection'._wrap(super(EntityHitResult, self).getDirection())

    @overload
    def setDirection(self, arg0: 'CubicDirection'):
        """public void dev.ultreon.quantum.util.EntityHitResult.setDirection(dev.ultreon.quantum.world.CubicDirection)"""
        super(_EntityHitResult, self).setDirection(arg0)

    @override
    @overload
    def getRay(self) -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.EntityHitResult.getRay()"""
        return 'Ray'._wrap(super(EntityHitResult, self).getRay())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getDistanceMax(self) -> float:
        """public float dev.ultreon.quantum.util.EntityHitResult.getDistanceMax()"""
        return float._wrap(super(EntityHitResult, self).getDistanceMax())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.util.EntityHitResult.equals(java.lang.Object)"""
        return bool._wrap(super(_EntityHitResult, self).equals(arg0))

    @overload
    def setInput(self, arg0: 'Ray') -> 'EntityHitResult':
        """public dev.ultreon.quantum.util.EntityHitResult dev.ultreon.quantum.util.EntityHitResult.setInput(dev.ultreon.quantum.util.Ray)"""
        return 'EntityHitResult'._wrap(super(_EntityHitResult, self).setInput(arg0))

    @override
    @overload
    def getDistance(self) -> float:
        """public double dev.ultreon.quantum.util.EntityHitResult.getDistance()"""
        return float._wrap(super(EntityHitResult, self).getDistance())

    @override
    @overload
    def isCollide(self) -> bool:
        """public boolean dev.ultreon.quantum.util.EntityHitResult.isCollide()"""
        return bool._wrap(super(EntityHitResult, self).isCollide())

    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.util.EntityHitResult.getEntity()"""
        return 'entity.Entity'._wrap(super(EntityHitResult, self).getEntity())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Ray', arg1: float):
        """public dev.ultreon.quantum.util.EntityHitResult(dev.ultreon.quantum.util.Ray,float)"""
        val = _EntityHitResult(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.util.EntityHitResult.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_EntityHitResult, self).write(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @property
    def entity(self) -> Entity:
        return Entity._wrap(super(_EntityHitResult).entity())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.util.EntityHitResult(dev.ultreon.quantum.network.PacketIO)"""
        val = _EntityHitResult(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.util.DataSizes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import dev.ultreon.quantum.util.DataSizes as _DataSizes
_DataSizes = _DataSizes
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DataSizes():
    """dev.ultreon.quantum.util.DataSizes"""
 
    @staticmethod
    def _wrap(java_value: _DataSizes) -> 'DataSizes':
        return DataSizes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DataSizes):
        """
        Dynamic initializer for DataSizes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DataSizes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DataSizes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self):
        """public dev.ultreon.quantum.util.DataSizes()"""
        val = _DataSizes()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def format(arg0: int) -> str:
        """public static java.lang.String dev.ultreon.quantum.util.DataSizes.format(long)"""
        return str._wrap(_DataSizes.format(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.DataSizes()"""
        val = _DataSizes()
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

    @staticmethod
    @overload
    def convert(arg0: int, arg1: 'Unit', arg2: 'Unit') -> int:
        """public static long dev.ultreon.quantum.util.DataSizes.convert(long,dev.ultreon.quantum.util.DataSizes$Unit,dev.ultreon.quantum.util.DataSizes$Unit)"""
        return int._wrap(_DataSizes.convert(_long.valueOf(arg0), arg1, arg2))

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
 
 
# CLASS: dev.ultreon.quantum.util.ExitCodes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.util.ExitCodes as _ExitCodes
_ExitCodes = _ExitCodes
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExitCodes():
    """dev.ultreon.quantum.util.ExitCodes"""
 
    @staticmethod
    def _wrap(java_value: _ExitCodes) -> 'ExitCodes':
        return ExitCodes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExitCodes):
        """
        Dynamic initializer for ExitCodes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExitCodes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExitCodes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.ExitCodes()"""
        val = _ExitCodes()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.util.ExitCodes()"""
        val = _ExitCodes()
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
 
 
# CLASS: dev.ultreon.quantum.util.Unit
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.util.Unit as _Unit
_Unit = _Unit
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Unit():
    """dev.ultreon.quantum.util.Unit"""
 
    @staticmethod
    def _wrap(java_value: _Unit) -> 'Unit':
        return Unit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Unit):
        """
        Dynamic initializer for Unit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Unit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Unit__wrapper":
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


Unit.INSTANCE = Unit._wrap(_INSTANCE.INSTANCE) 
 
 
# CLASS: dev.ultreon.quantum.util.ValueSource
import dev.ultreon.quantum.util.ValueSource as _ValueSource
_ValueSource = _ValueSource
from abc import abstractmethod, ABC
 
class ValueSource():
    """dev.ultreon.quantum.util.ValueSource"""
 
    @staticmethod
    def _wrap(java_value: _ValueSource) -> 'ValueSource':
        return ValueSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueSource):
        """
        Dynamic initializer for ValueSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getValue(self, ):
        """public abstract double dev.ultreon.quantum.util.ValueSource.getValue()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.util.Ray
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.util.Ray as _Ray
_Ray = _Ray
import java.lang.Float as _float
import dev.ultreon.quantum.world.CubicDirection as _CubicDirection
_CubicDirection = _CubicDirection
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import java.lang.Class as _Class
_Class = _Class
 
class Ray():
    """dev.ultreon.quantum.util.Ray"""
 
    @staticmethod
    def _wrap(java_value: _Ray) -> 'Ray':
        return Ray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ray):
        """
        Dynamic initializer for Ray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'Ray') -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.Ray.set(dev.ultreon.quantum.util.Ray)"""
        return 'Ray'._wrap(super(_Ray, self).set(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.Ray()"""
        val = _Ray()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.util.Ray(dev.ultreon.quantum.network.PacketIO)"""
        val = _Ray(arg0)
        self.__wrapper = val

    @overload
    def getDirection(self) -> 'world.CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.util.Ray.getDirection()"""
        return 'world.CubicDirection'._wrap(super(Ray, self).getDirection())

    @overload
    def __init__(self, arg0: 'Vec3d', arg1: 'Vec3d'):
        """public dev.ultreon.quantum.util.Ray(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _Ray(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.util.Ray.hashCode()"""
        return int._wrap(super(Ray, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.util.Ray.equals(java.lang.Object)"""
        return bool._wrap(super(_Ray, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.Ray.toString()"""
        return str._wrap(super(Ray, self).toString())

    @overload
    def cpy(self) -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.Ray.cpy()"""
        return 'Ray'._wrap(super(Ray, self).cpy())

    @overload
    def set(self, arg0: 'Vec3d', arg1: 'Vec3d') -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.Ray.set(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Ray'._wrap(super(_Ray, self).set(arg0, arg1))

    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.util.Ray.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Ray, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.Ray()"""
        val = _Ray()
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
    def getEndPoint(self, arg0: 'Vec3d', arg1: float) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.Ray.getEndPoint(dev.ultreon.libs.commons.v0.vector.Vec3d,float)"""
        return 'vector.Vec3d'._wrap(super(_Ray, self).getEndPoint(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.Ray.set(float,float,float,float,float,float)"""
        return 'Ray'._wrap(super(_Ray, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))) 
 
 
# CLASS: dev.ultreon.quantum.util.LazyValue
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
import dev.ultreon.quantum.util.LazyValue as _LazyValue
_LazyValue = _LazyValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LazyValue():
    """dev.ultreon.quantum.util.LazyValue"""
 
    @staticmethod
    def _wrap(java_value: _LazyValue) -> 'LazyValue':
        return LazyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LazyValue):
        """
        Dynamic initializer for LazyValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LazyValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LazyValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.util.LazyValue.get()"""
        return object._wrap(super(LazyValue, self).get())

    @overload
    def set(self, arg0: object):
        """public void dev.ultreon.quantum.util.LazyValue.set(T)"""
        super(_LazyValue, self).set(arg0)

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
    def isInitialized(self) -> bool:
        """public boolean dev.ultreon.quantum.util.LazyValue.isInitialized()"""
        return bool._wrap(super(LazyValue, self).isInitialized())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.util.LazyValue()"""
        val = _LazyValue()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.LazyValue()"""
        val = _LazyValue()
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
 
 
# CLASS: dev.ultreon.quantum.util.BlockMetaPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.util.BlockMetaPredicate as _BlockMetaPredicate
_BlockMetaPredicate = _BlockMetaPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockMetaPredicate():
    """dev.ultreon.quantum.util.BlockMetaPredicate"""
 
    @staticmethod
    def _wrap(java_value: _BlockMetaPredicate) -> 'BlockMetaPredicate':
        return BlockMetaPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockMetaPredicate):
        """
        Dynamic initializer for BlockMetaPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockMetaPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockMetaPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).or(arg0))

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
    def test(self, arg0: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.util.BlockMetaPredicate.test(dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_BlockMetaPredicate, self).test(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def negate(self) -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.negate()"""
        return 'Predicate'._wrap(super(Predicate, self).negate())

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

    @overload
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).and(arg0))

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


BlockMetaPredicate.WG_HEIGHT_CHK = BlockMetaPredicate._wrap(_WG_HEIGHT_CHK.WG_HEIGHT_CHK)

BlockMetaPredicate.EVERYTHING = BlockMetaPredicate._wrap(_EVERYTHING.EVERYTHING)

BlockMetaPredicate.NON_FLUID = BlockMetaPredicate._wrap(_NON_FLUID.NON_FLUID)

BlockMetaPredicate.TRANSPARENT = BlockMetaPredicate._wrap(_TRANSPARENT.TRANSPARENT)

BlockMetaPredicate.BREAK_INSTANTLY = BlockMetaPredicate._wrap(_BREAK_INSTANTLY.BREAK_INSTANTLY)

BlockMetaPredicate.FLUID = BlockMetaPredicate._wrap(_FLUID.FLUID)

BlockMetaPredicate.SOLID = BlockMetaPredicate._wrap(_SOLID.SOLID)

BlockMetaPredicate.REPLACEABLE = BlockMetaPredicate._wrap(_REPLACEABLE.REPLACEABLE) 
 
 
# CLASS: dev.ultreon.quantum.util.InvalidThreadException
from builtins import str
import dev.ultreon.quantum.util.InvalidThreadException as _InvalidThreadException
_InvalidThreadException = _InvalidThreadException
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
 
class InvalidThreadException():
    """dev.ultreon.quantum.util.InvalidThreadException"""
 
    @staticmethod
    def _wrap(java_value: _InvalidThreadException) -> 'InvalidThreadException':
        return InvalidThreadException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidThreadException):
        """
        Dynamic initializer for InvalidThreadException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidThreadException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidThreadException__wrapper":
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.InvalidThreadException(java.lang.String)"""
        val = _InvalidThreadException(arg0)
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.IntSizedList
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import it.unimi.dsi.fastutil.objects.Reference2IntFunction as Reference2IntFunction
from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.collections.v0.util.Range as _Range
_Range = _Range
import dev.ultreon.quantum.util.IntSizedList as _IntSizedList
_IntSizedList = _IntSizedList
from typing import List
import java.lang.Integer as _int
try:
    from pycorelibs.collections.v0 import util
except ImportError:
    util = _import_once("pycorelibs.collections.v0.util")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntSizedList():
    """dev.ultreon.quantum.util.IntSizedList"""
 
    @staticmethod
    def _wrap(java_value: _IntSizedList) -> 'IntSizedList':
        return IntSizedList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntSizedList):
        """
        Dynamic initializer for IntSizedList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntSizedList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntSizedList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def clear(self):
        """public void dev.ultreon.quantum.util.IntSizedList.clear()"""
        super(IntSizedList, self).clear()

    @overload
    def rangeOf(self, arg0: object) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.quantum.util.IntSizedList.rangeOf(T)"""
        return 'util.Range'._wrap(super(_IntSizedList, self).rangeOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.IntSizedList()"""
        val = _IntSizedList()
        self.__wrapper = val

    @overload
    def editLengths(self, arg0: 'Reference2IntFunction'):
        """public void dev.ultreon.quantum.util.IntSizedList.editLengths(it.unimi.dsi.fastutil.objects.Reference2IntFunction<T>)"""
        super(_IntSizedList, self).editLengths(arg0)

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
    def subList(self, arg0: int, arg1: int) -> 'IntSizedList':
        """public dev.ultreon.quantum.util.IntSizedList<T> dev.ultreon.quantum.util.IntSizedList.subList(int,int)"""
        return 'IntSizedList'._wrap(super(_IntSizedList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def insert(self, arg0: int, arg1: int, arg2: object) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.insert(int,int,T)"""
        return int._wrap(super(_IntSizedList, self).insert(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def getValue(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.util.IntSizedList.getValue(int)"""
        return object._wrap(super(_IntSizedList, self).getValue(_int.valueOf(arg0)))

    @overload
    def getDirectValue(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.util.IntSizedList.getDirectValue(int)"""
        return object._wrap(super(_IntSizedList, self).getDirectValue(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.IntSizedList()"""
        val = _IntSizedList()
        self.__wrapper = val

    @overload
    def remove(self, arg0: int):
        """public void dev.ultreon.quantum.util.IntSizedList.remove(int)"""
        super(_IntSizedList, self).remove(_int.valueOf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.indexOf(T)"""
        return int._wrap(super(_IntSizedList, self).indexOf(arg0))

    @overload
    def add(self, arg0: int, arg1: object) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.add(int,T)"""
        return int._wrap(super(_IntSizedList, self).add(_int.valueOf(arg0), arg1))

    @overload
    def getRange(self, arg0: int) -> 'util.Range':
        """public dev.ultreon.libs.collections.v0.util.Range dev.ultreon.quantum.util.IntSizedList.getRange(int)"""
        return 'util.Range'._wrap(super(_IntSizedList, self).getRange(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getSize(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.getSize(int)"""
        return int._wrap(super(_IntSizedList, self).getSize(_int.valueOf(arg0)))

    @overload
    def addAll(self, arg0: 'IntSizedList'):
        """public void dev.ultreon.quantum.util.IntSizedList.addAll(dev.ultreon.quantum.util.IntSizedList<? extends T>)"""
        super(_IntSizedList, self).addAll(arg0)

    @overload
    def size(self) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.size()"""
        return int._wrap(super(IntSizedList, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTotalSize(self) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.getTotalSize()"""
        return int._wrap(super(IntSizedList, self).getTotalSize())

    @overload
    def edit(self, arg0: object, arg1: int) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.edit(T,int)"""
        return int._wrap(super(_IntSizedList, self).edit(arg0, _int.valueOf(arg1)))

    @overload
    def edit(self, arg0: object, arg1: int, arg2: object) -> int:
        """public int dev.ultreon.quantum.util.IntSizedList.edit(T,int,T)"""
        return int._wrap(super(_IntSizedList, self).edit(arg0, _int.valueOf(arg1), arg2))

    @overload
    def getRanges(self) -> List['util.Range']:
        """public dev.ultreon.libs.collections.v0.util.Range[] dev.ultreon.quantum.util.IntSizedList.getRanges()"""
        return List['util.Range']._wrap(super(IntSizedList, self).getRanges())

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.Difficulty
import dev.ultreon.quantum.util.Difficulty as _Difficulty
_Difficulty = _Difficulty
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
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Difficulty():
    """dev.ultreon.quantum.util.Difficulty"""
 
    @staticmethod
    def _wrap(java_value: _Difficulty) -> 'Difficulty':
        return Difficulty(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Difficulty):
        """
        Dynamic initializer for Difficulty.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Difficulty__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Difficulty__wrapper":
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
    def values() -> List['Difficulty']:
        """public static dev.ultreon.quantum.util.Difficulty[] dev.ultreon.quantum.util.Difficulty.values()"""
        return List[Difficulty]._wrap(_Difficulty.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Difficulty':
        """public static dev.ultreon.quantum.util.Difficulty dev.ultreon.quantum.util.Difficulty.valueOf(java.lang.String)"""
        return Difficulty._wrap(_Difficulty.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Difficulty.HARD = Difficulty._wrap(_HARD.HARD)

Difficulty.IMPOSSIBLE = Difficulty._wrap(_IMPOSSIBLE.IMPOSSIBLE)

Difficulty.NORMAL = Difficulty._wrap(_NORMAL.NORMAL)

Difficulty.APOCALYPSE = Difficulty._wrap(_APOCALYPSE.APOCALYPSE)

Difficulty.EASY = Difficulty._wrap(_EASY.EASY)

Difficulty.PEACEFUL = Difficulty._wrap(_PEACEFUL.PEACEFUL) 
 
 
# CLASS: dev.ultreon.quantum.util.BlockHitResult
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.util.Ray as _Ray
_Ray = _Ray
import dev.ultreon.quantum.util.BlockHitResult as _BlockHitResult
_BlockHitResult = _BlockHitResult
from builtins import bool
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.CubicDirection as _CubicDirection
_CubicDirection = _CubicDirection
import java.lang.Float as _float
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockHitResult():
    """dev.ultreon.quantum.util.BlockHitResult"""
 
    @staticmethod
    def _wrap(java_value: _BlockHitResult) -> 'BlockHitResult':
        return BlockHitResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockHitResult):
        """
        Dynamic initializer for BlockHitResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockHitResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockHitResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPosition(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BlockHitResult.getPosition()"""
        return 'vector.Vec3d'._wrap(super(BlockHitResult, self).getPosition())

    @override
    @overload
    def isCollide(self) -> bool:
        """public boolean dev.ultreon.quantum.util.BlockHitResult.isCollide()"""
        return bool._wrap(super(BlockHitResult, self).isCollide())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setInput(self, arg0: 'Ray') -> 'BlockHitResult':
        """public dev.ultreon.quantum.util.BlockHitResult dev.ultreon.quantum.util.BlockHitResult.setInput(dev.ultreon.quantum.util.Ray)"""
        return 'BlockHitResult'._wrap(super(_BlockHitResult, self).setInput(arg0))

    @overload
    def getBlock(self) -> 'block.Block':
        """public dev.ultreon.quantum.block.Block dev.ultreon.quantum.util.BlockHitResult.getBlock()"""
        return 'block.Block'._wrap(super(BlockHitResult, self).getBlock())

    @override
    @overload
    def getDistanceMax(self) -> float:
        """public float dev.ultreon.quantum.util.BlockHitResult.getDistanceMax()"""
        return float._wrap(super(BlockHitResult, self).getDistanceMax())

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
    def __init__(self, arg0: 'Ray', arg1: float):
        """public dev.ultreon.quantum.util.BlockHitResult(dev.ultreon.quantum.util.Ray,float)"""
        val = _BlockHitResult(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.util.BlockHitResult.equals(java.lang.Object)"""
        return bool._wrap(super(_BlockHitResult, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.BlockHitResult()"""
        val = _BlockHitResult()
        self.__wrapper = val

    @override
    @overload
    def getRay(self) -> 'Ray':
        """public dev.ultreon.quantum.util.Ray dev.ultreon.quantum.util.BlockHitResult.getRay()"""
        return 'Ray'._wrap(super(BlockHitResult, self).getRay())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.util.BlockHitResult(dev.ultreon.quantum.network.PacketIO)"""
        val = _BlockHitResult(arg0)
        self.__wrapper = val

    @overload
    def getBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.util.BlockHitResult.getBlockMeta()"""
        return 'state.BlockProperties'._wrap(super(BlockHitResult, self).getBlockMeta())

    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.util.BlockHitResult.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_BlockHitResult, self).write(arg0)

    @overload
    def setDirection(self, arg0: 'CubicDirection'):
        """public void dev.ultreon.quantum.util.BlockHitResult.setDirection(dev.ultreon.quantum.world.CubicDirection)"""
        super(_BlockHitResult, self).setDirection(arg0)

    @overload
    def getDirection(self) -> 'world.CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.util.BlockHitResult.getDirection()"""
        return 'world.CubicDirection'._wrap(super(BlockHitResult, self).getDirection())

    @overload
    def getNormal(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.util.BlockHitResult.getNormal()"""
        return 'vector.Vec3d'._wrap(super(BlockHitResult, self).getNormal())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getPos(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.BlockHitResult.getPos()"""
        return 'vector.Vec3i'._wrap(super(BlockHitResult, self).getPos())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.util.BlockHitResult.hashCode()"""
        return int._wrap(super(BlockHitResult, self).hashCode())

    @overload
    def getNext(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.util.BlockHitResult.getNext()"""
        return 'vector.Vec3i'._wrap(super(BlockHitResult, self).getNext())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.BlockHitResult()"""
        val = _BlockHitResult()
        self.__wrapper = val

    @override
    @overload
    def getDistance(self) -> float:
        """public double dev.ultreon.quantum.util.BlockHitResult.getDistance()"""
        return float._wrap(super(BlockHitResult, self).getDistance())

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
    def __init__(self, arg0: 'Ray'):
        """public dev.ultreon.quantum.util.BlockHitResult(dev.ultreon.quantum.util.Ray)"""
        val = _BlockHitResult(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.util.IllegalThreadInterruptionError
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
import java.lang.InterruptedException as InterruptedException
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.util.IllegalThreadInterruptionError as _IllegalThreadInterruptionError
_IllegalThreadInterruptionError = _IllegalThreadInterruptionError
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
 
class IllegalThreadInterruptionError():
    """dev.ultreon.quantum.util.IllegalThreadInterruptionError"""
 
    @staticmethod
    def _wrap(java_value: _IllegalThreadInterruptionError) -> 'IllegalThreadInterruptionError':
        return IllegalThreadInterruptionError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IllegalThreadInterruptionError):
        """
        Dynamic initializer for IllegalThreadInterruptionError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IllegalThreadInterruptionError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IllegalThreadInterruptionError__wrapper":
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.IllegalThreadInterruptionError(java.lang.String)"""
        val = _IllegalThreadInterruptionError(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'InterruptedException'):
        """public dev.ultreon.quantum.util.IllegalThreadInterruptionError(java.lang.String,java.lang.InterruptedException)"""
        val = _IllegalThreadInterruptionError(arg0, arg1)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.Axis
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.util.Axis as _Axis
_Axis = _Axis
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Axis():
    """dev.ultreon.quantum.util.Axis"""
 
    @staticmethod
    def _wrap(java_value: _Axis) -> 'Axis':
        return Axis(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Axis):
        """
        Dynamic initializer for Axis.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Axis__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Axis__wrapper":
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

    @overload
    def getVector(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.util.Axis.getVector()"""
        return 'math.Vector3'._wrap(super(Axis, self).getVector())

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
    def values() -> List['Axis']:
        """public static dev.ultreon.quantum.util.Axis[] dev.ultreon.quantum.util.Axis.values()"""
        return List[Axis]._wrap(_Axis.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Axis':
        """public static dev.ultreon.quantum.util.Axis dev.ultreon.quantum.util.Axis.valueOf(java.lang.String)"""
        return Axis._wrap(_Axis.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Axis.X = Axis._wrap(_X.X)

Axis.Z = Axis._wrap(_Z.Z)

Axis.Y = Axis._wrap(_Y.Y) 
 
 
# CLASS: dev.ultreon.quantum.util.ModLoadingContext
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.util.ModLoadingContext as _ModLoadingContext
_ModLoadingContext = _ModLoadingContext
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.Mod as _Mod
_Mod = _Mod
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModLoadingContext():
    """dev.ultreon.quantum.util.ModLoadingContext"""
 
    @staticmethod
    def _wrap(java_value: _ModLoadingContext) -> 'ModLoadingContext':
        return ModLoadingContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModLoadingContext):
        """
        Dynamic initializer for ModLoadingContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModLoadingContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModLoadingContext__wrapper":
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
    def withinContext(arg0: 'Mod', arg1: 'Runnable'):
        """public static void dev.ultreon.quantum.util.ModLoadingContext.withinContext(dev.ultreon.quantum.Mod,java.lang.Runnable)"""
        _ModLoadingContext.withinContext(arg0, arg1)

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
    def get() -> 'ModLoadingContext':
        """public static dev.ultreon.quantum.util.ModLoadingContext dev.ultreon.quantum.util.ModLoadingContext.get()"""
        return ModLoadingContext._wrap(_ModLoadingContext.get())

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
    def getMod(self) -> 'pyquantum.Mod':
        """public dev.ultreon.quantum.Mod dev.ultreon.quantum.util.ModLoadingContext.getMod()"""
        return 'pyquantum.Mod'._wrap(super(ModLoadingContext, self).getMod())

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
 
 
# CLASS: dev.ultreon.quantum.util.PosOutOfBoundsException
from builtins import str
import dev.ultreon.quantum.util.PosOutOfBoundsException as _PosOutOfBoundsException
_PosOutOfBoundsException = _PosOutOfBoundsException
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
 
class PosOutOfBoundsException():
    """dev.ultreon.quantum.util.PosOutOfBoundsException"""
 
    @staticmethod
    def _wrap(java_value: _PosOutOfBoundsException) -> 'PosOutOfBoundsException':
        return PosOutOfBoundsException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PosOutOfBoundsException):
        """
        Dynamic initializer for PosOutOfBoundsException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PosOutOfBoundsException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PosOutOfBoundsException__wrapper":
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.PosOutOfBoundsException(java.lang.String)"""
        val = _PosOutOfBoundsException(arg0)
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.util.PosOutOfBoundsException()"""
        val = _PosOutOfBoundsException()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.util.PosOutOfBoundsException()"""
        val = _PosOutOfBoundsException()
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.util.GameMode
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.entity.player.PlayerAbilities as _PlayerAbilities
_PlayerAbilities = _PlayerAbilities
import java.lang.String as _String
_String = _String
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
import dev.ultreon.quantum.util.GameMode as _GameMode
_GameMode = _GameMode
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameMode():
    """dev.ultreon.quantum.util.GameMode"""
 
    @staticmethod
    def _wrap(java_value: _GameMode) -> 'GameMode':
        return GameMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameMode):
        """
        Dynamic initializer for GameMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameMode__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['GameMode']:
        """public static dev.ultreon.quantum.util.GameMode[] dev.ultreon.quantum.util.GameMode.values()"""
        return List[GameMode]._wrap(_GameMode.values())

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

    @staticmethod
    @overload
    def byOrdinal(arg0: int) -> 'GameMode':
        """public static dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.byOrdinal(int)"""
        return GameMode._wrap(_GameMode.byOrdinal(_int.valueOf(arg0)))

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

    @overload
    def setAbilities(self, arg0: 'PlayerAbilities') -> 'player.PlayerAbilities':
        """public dev.ultreon.quantum.entity.player.PlayerAbilities dev.ultreon.quantum.util.GameMode.setAbilities(dev.ultreon.quantum.entity.player.PlayerAbilities)"""
        return 'player.PlayerAbilities'._wrap(super(_GameMode, self).setAbilities(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GameMode':
        """public static dev.ultreon.quantum.util.GameMode dev.ultreon.quantum.util.GameMode.valueOf(java.lang.String)"""
        return GameMode._wrap(_GameMode.valueOf(arg0))

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


GameMode.SPECTATOR = GameMode._wrap(_SPECTATOR.SPECTATOR)

GameMode.SURVIVAL = GameMode._wrap(_SURVIVAL.SURVIVAL)

GameMode.ADVENTUROUS = GameMode._wrap(_ADVENTUROUS.ADVENTUROUS)

GameMode.BUILDER = GameMode._wrap(_BUILDER.BUILDER)

GameMode.BUILDER_PLUS = GameMode._wrap(_BUILDER_PLUS.BUILDER_PLUS) 
 
 
# CLASS: dev.ultreon.quantum.util.BlockPredicate
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Predicate as _Predicate
_Predicate = _Predicate
import java.lang.Integer as _int
import dev.ultreon.quantum.util.BlockPredicate as _BlockPredicate
_BlockPredicate = _BlockPredicate
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockPredicate():
    """dev.ultreon.quantum.util.BlockPredicate"""
 
    @staticmethod
    def _wrap(java_value: _BlockPredicate) -> 'BlockPredicate':
        return BlockPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockPredicate):
        """
        Dynamic initializer for BlockPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).or(arg0))

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
    def negate(self) -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.negate()"""
        return 'Predicate'._wrap(super(Predicate, self).negate())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def test(self, arg0: 'Block') -> bool:
        """public boolean dev.ultreon.quantum.util.BlockPredicate.test(dev.ultreon.quantum.block.Block)"""
        return bool._wrap(super(_BlockPredicate, self).test(arg0))

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
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'._wrap(super(_Predicate, self).and(arg0))

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


BlockPredicate.EVERYTHING = BlockPredicate._wrap(_EVERYTHING.EVERYTHING)

BlockPredicate.SOLID = BlockPredicate._wrap(_SOLID.SOLID)

BlockPredicate.NON_FLUID = BlockPredicate._wrap(_NON_FLUID.NON_FLUID)

BlockPredicate.TRANSPARENT = BlockPredicate._wrap(_TRANSPARENT.TRANSPARENT)

BlockPredicate.FLUID = BlockPredicate._wrap(_FLUID.FLUID)

BlockPredicate.REPLACEABLE = BlockPredicate._wrap(_REPLACEABLE.REPLACEABLE)

BlockPredicate.BREAK_INSTANTLY = BlockPredicate._wrap(_BREAK_INSTANTLY.BREAK_INSTANTLY) 
 
 
# CLASS: dev.ultreon.quantum.util.OverwriteError
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
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import dev.ultreon.quantum.util.OverwriteError as _OverwriteError
_OverwriteError = _OverwriteError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OverwriteError():
    """dev.ultreon.quantum.util.OverwriteError"""
 
    @staticmethod
    def _wrap(java_value: _OverwriteError) -> 'OverwriteError':
        return OverwriteError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OverwriteError):
        """
        Dynamic initializer for OverwriteError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OverwriteError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OverwriteError__wrapper":
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.OverwriteError(java.lang.String)"""
        val = _OverwriteError(arg0)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.util.Identifier
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = _import_once("pycorelibs.commons.v0.tuple")

import java.util.Collection as Collection
import java.lang.String as _string
import java.util.ArrayList as ArrayList
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.libs.commons.v0.tuple.Pair as _Pair
_Pair = _Pair
import java.util.List as _List
_List = _List
import java.util.function.BiFunction as BiFunction
from typing import List
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Identifier():
    """dev.ultreon.quantum.util.Identifier"""
 
    @staticmethod
    def _wrap(java_value: _Identifier) -> 'Identifier':
        return Identifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Identifier):
        """
        Dynamic initializer for Identifier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Identifier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Identifier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parse(arg0: str) -> 'Identifier':
        """public static dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.parse(java.lang.String)"""
        return Identifier._wrap(_Identifier.parse(arg0))

    @overload
    def toArrayList(self) -> 'ArrayList':
        """public java.util.ArrayList<java.lang.String> dev.ultreon.quantum.util.Identifier.toArrayList()"""
        return 'ArrayList'._wrap(super(Identifier, self).toArrayList())

    @overload
    def toPair(self) -> 'tuple.Pair':
        """public dev.ultreon.libs.commons.v0.tuple.Pair<java.lang.String, java.lang.String> dev.ultreon.quantum.util.Identifier.toPair()"""
        return 'tuple.Pair'._wrap(super(Identifier, self).toPair())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def tryParse(arg0: str) -> 'Identifier':
        """public static dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.tryParse(java.lang.String)"""
        return Identifier._wrap(_Identifier.tryParse(arg0))

    @overload
    def toList(self) -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.util.Identifier.toList()"""
        return 'List'._wrap(super(Identifier, self).toList())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def mapPath(self, arg0: 'UnaryOperator') -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.mapPath(java.util.function.UnaryOperator<java.lang.String>)"""
        return 'Identifier'._wrap(super(_Identifier, self).mapPath(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def path(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.Identifier.path()"""
        return str._wrap(super(Identifier, self).path())

    @overload
    def reduce(self, arg0: 'BiFunction') -> object:
        """public <T> T dev.ultreon.quantum.util.Identifier.reduce(java.util.function.BiFunction<java.lang.String, java.lang.String, T>)"""
        return object._wrap(super(_Identifier, self).reduce(arg0))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.util.Identifier(java.lang.String,java.lang.String)"""
        val = _Identifier(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.util.Identifier(java.lang.String)"""
        val = _Identifier(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.Identifier.toString()"""
        return str._wrap(super(Identifier, self).toString())

    @overload
    def namespace(self) -> str:
        """public java.lang.String dev.ultreon.quantum.util.Identifier.namespace()"""
        return str._wrap(super(Identifier, self).namespace())

    @staticmethod
    @overload
    def testNamespace(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.util.Identifier.testNamespace(java.lang.String)"""
        return str._wrap(_Identifier.testNamespace(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.util.Identifier.hashCode()"""
        return int._wrap(super(Identifier, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def withPath(self, arg0: str) -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.withPath(java.lang.String)"""
        return 'Identifier'._wrap(super(_Identifier, self).withPath(arg0))

    @overload
    def map(self, arg0: 'UnaryOperator', arg1: 'UnaryOperator') -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.map(java.util.function.UnaryOperator<java.lang.String>,java.util.function.UnaryOperator<java.lang.String>)"""
        return 'Identifier'._wrap(super(_Identifier, self).map(arg0, arg1))

    @overload
    def mapLocation(self, arg0: 'UnaryOperator') -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.mapLocation(java.util.function.UnaryOperator<java.lang.String>)"""
        return 'Identifier'._wrap(super(_Identifier, self).mapLocation(arg0))

    @overload
    def toCollection(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.quantum.util.Identifier.toCollection()"""
        return 'Collection'._wrap(super(Identifier, self).toCollection())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def testPath(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.util.Identifier.testPath(java.lang.String)"""
        return str._wrap(_Identifier.testPath(arg0))

    @overload
    def withNamespace(self, arg0: str) -> 'Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.util.Identifier.withNamespace(java.lang.String)"""
        return 'Identifier'._wrap(super(_Identifier, self).withNamespace(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.util.Identifier.equals(java.lang.Object)"""
        return bool._wrap(super(_Identifier, self).equals(arg0))

    @overload
    def toArray(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.util.Identifier.toArray()"""
        return List[str]._wrap(super(Identifier, self).toArray())