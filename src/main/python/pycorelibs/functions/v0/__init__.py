from __future__ import annotations
from overload import overload


 
from pyquantum_helper import transform as __transform
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
import dev.ultreon.libs.functions.v0.BiByte2ByteFunction as __BiByte2ByteFunction
__BiByte2ByteFunction = __BiByte2ByteFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.lang.Byte as Byte
import java.util.function.BiFunction as BiFunction
 
class BiByte2ByteFunction(ABC, __BiFunction, BiFunction):
    """dev.ultreon.libs.functions.v0.BiByte2ByteFunction"""
 
    @staticmethod
    def __wrap(java_value: __BiByte2ByteFunction) -> 'BiByte2ByteFunction':
        return BiByte2ByteFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiByte2ByteFunction):
        """
        Dynamic initializer for BiByte2ByteFunction.
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
    def and() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.and()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.and())

    @staticmethod
    @overload
    def or() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.or()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.or())

    @staticmethod
    @overload
    def sub() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.sub()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.sub())

    @staticmethod
    @overload
    def mul() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.mul()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.mul())

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract byte dev.ultreon.libs.functions.v0.BiByte2ByteFunction.apply(byte,byte)"""
        pass

    @staticmethod
    @overload
    def add() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.add()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.add())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'.__wrap(super(__BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def scalb() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.scalb()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.scalb())

    @overload
    def apply(self, arg0: 'Byte', arg1: 'Byte') -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.functions.v0.BiByte2ByteFunction.apply(java.lang.Byte,java.lang.Byte)"""
        return __transform(super(__BiByte2ByteFunction, self).apply(arg0, arg1)).'Byte'Value()

    @staticmethod
    @overload
    def mod() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.mod()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.mod())

    @staticmethod
    @overload
    def atan2() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.atan2()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.atan2())

    @staticmethod
    @overload
    def pow() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.pow()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.pow())

    @staticmethod
    @overload
    def div() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.div()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.div())

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiByte2ByteFunction
from pyquantum_helper import transform as __transform
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
import dev.ultreon.libs.functions.v0.BiByte2ByteFunction as __BiByte2ByteFunction
__BiByte2ByteFunction = __BiByte2ByteFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.lang.Byte as Byte
import java.util.function.BiFunction as BiFunction
 
class BiByte2ByteFunction(ABC, __BiFunction, BiFunction):
    """dev.ultreon.libs.functions.v0.BiByte2ByteFunction"""
 
    @staticmethod
    def __wrap(java_value: __BiByte2ByteFunction) -> 'BiByte2ByteFunction':
        return BiByte2ByteFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiByte2ByteFunction):
        """
        Dynamic initializer for BiByte2ByteFunction.
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
    def and() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.and()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.and())

    @staticmethod
    @overload
    def or() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.or()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.or())

    @staticmethod
    @overload
    def sub() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.sub()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.sub())

    @staticmethod
    @overload
    def mul() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.mul()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.mul())

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract byte dev.ultreon.libs.functions.v0.BiByte2ByteFunction.apply(byte,byte)"""
        pass

    @staticmethod
    @overload
    def add() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.add()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.add())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'.__wrap(super(__BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def scalb() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.scalb()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.scalb())

    @overload
    def apply(self, arg0: 'Byte', arg1: 'Byte') -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.functions.v0.BiByte2ByteFunction.apply(java.lang.Byte,java.lang.Byte)"""
        return __transform(super(__BiByte2ByteFunction, self).apply(arg0, arg1)).'Byte'Value()

    @staticmethod
    @overload
    def mod() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.mod()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.mod())

    @staticmethod
    @overload
    def atan2() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.atan2()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.atan2())

    @staticmethod
    @overload
    def pow() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.pow()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.pow())

    @staticmethod
    @overload
    def div() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.div()"""
        return BiByte2ByteFunction.__wrap(__BiByte2ByteFunction.div())

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiByte2ByteFunction 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiLong2LongFunction
from pyquantum_helper import transform as __transform
import java.lang.Long as Long
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import dev.ultreon.libs.functions.v0.BiLong2LongFunction as __BiLong2LongFunction
__BiLong2LongFunction = __BiLong2LongFunction
import java.util.function.BiFunction as BiFunction
 
class BiLong2LongFunction(ABC, __BiFunction, BiFunction):
    """dev.ultreon.libs.functions.v0.BiLong2LongFunction"""
 
    @staticmethod
    def __wrap(java_value: __BiLong2LongFunction) -> 'BiLong2LongFunction':
        return BiLong2LongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiLong2LongFunction):
        """
        Dynamic initializer for BiLong2LongFunction.
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
    def and() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.and()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.and())

    @staticmethod
    @overload
    def atan2() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.atan2()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.atan2())

    @staticmethod
    @overload
    def sub() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.sub()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.sub())

    @staticmethod
    @overload
    def mul() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.mul()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.mul())

    @overload
    def apply(self, arg0: 'Long', arg1: 'Long') -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.functions.v0.BiLong2LongFunction.apply(java.lang.Long,java.lang.Long)"""
        return __transform(super(__BiLong2LongFunction, self).apply(arg0, arg1)).'Long'Value()

    @staticmethod
    @overload
    def add() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.add()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.add())

    @staticmethod
    @overload
    def or() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.or()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.or())

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract long dev.ultreon.libs.functions.v0.BiLong2LongFunction.apply(long,long)"""
        pass

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'.__wrap(super(__BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def mod() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.mod()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.mod())

    @staticmethod
    @overload
    def pow() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.pow()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.pow())

    @staticmethod
    @overload
    def scalb() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.scalb()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.scalb())

    @staticmethod
    @overload
    def div() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.div()"""
        return BiLong2LongFunction.__wrap(__BiLong2LongFunction.div()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Int2IntFunction
from pyquantum_helper import transform as __transform
import java.lang.Integer as Integer
import java.util.function.Function as __Function
__Function = __Function
import dev.ultreon.libs.functions.v0.Int2IntFunction as __Int2IntFunction
__Int2IntFunction = __Int2IntFunction
import java.lang.Integer as __int
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class Int2IntFunction(ABC, __Function, Function):
    """dev.ultreon.libs.functions.v0.Int2IntFunction"""
 
    @staticmethod
    def __wrap(java_value: __Int2IntFunction) -> 'Int2IntFunction':
        return Int2IntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Int2IntFunction):
        """
        Dynamic initializer for Int2IntFunction.
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
    def mod(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.mod(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.mod(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def log1p() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.log1p()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.log1p())

    @staticmethod
    @overload
    def tanh() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.tanh()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.tanh())

    @staticmethod
    @overload
    def floor() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.floor()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.floor())

    @staticmethod
    @overload
    def sinh() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.sinh()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.sinh())

    @staticmethod
    @overload
    def log10() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.log10()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.log10())

    @staticmethod
    @overload
    def cos() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.cos()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.cos())

    @staticmethod
    @overload
    def signum() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.signum()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.signum())

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.scalb(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.scalb(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def atan() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.atan()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.atan())

    @staticmethod
    @overload
    def sub(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.sub(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.sub(__int.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Integer') -> 'Integer':
        """public default java.lang.Integer dev.ultreon.libs.functions.v0.Int2IntFunction.apply(java.lang.Integer)"""
        return __transform(super(__Int2IntFunction, self).apply(arg0)).'Integer'Value()

    @staticmethod
    @overload
    def ceil() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.ceil()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.ceil())

    @staticmethod
    @overload
    def atan2(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.atan2(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.atan2(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def or(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.or(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.or(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def div(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.div(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.div(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def cosh() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.cosh()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.cosh())

    @staticmethod
    @overload
    def pow(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.pow(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.pow(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def sin() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.sin()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.sin())

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract int dev.ultreon.libs.functions.v0.Int2IntFunction.apply(int)"""
        pass

    @staticmethod
    @overload
    def mul(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.mul(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.mul(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def acos() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.acos()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.acos())

    @staticmethod
    @overload
    def asin() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.asin()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.asin())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @staticmethod
    @overload
    def tan() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.tan()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.tan())

    @staticmethod
    @overload
    def plus() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.plus()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.plus())

    @staticmethod
    @overload
    def log() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.log()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.log())

    @staticmethod
    @overload
    def round() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.round()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.round())

    @staticmethod
    @overload
    def minus() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.minus()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.minus())

    @staticmethod
    @overload
    def sqrt() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.sqrt()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.sqrt())

    @staticmethod
    @overload
    def ulp() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.ulp()"""
        return Int2IntFunction.__wrap(__Int2IntFunction.ulp())

    @staticmethod
    @overload
    def and(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.and(int)"""
        return Int2IntFunction.__wrap(__Int2IntFunction.and(__int.valueOf(arg0)))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0)) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Long2LongFunction
import dev.ultreon.libs.functions.v0.Long2LongFunction as __Long2LongFunction
__Long2LongFunction = __Long2LongFunction
import java.lang.Long as __long
from pyquantum_helper import transform as __transform
import java.lang.Long as Long
import java.util.function.Function as __Function
__Function = __Function
from abc import abstractmethod, ABC
import java.lang.Integer as __int
import java.util.function.Function as Function
 
class Long2LongFunction(ABC, __Function, Function):
    """dev.ultreon.libs.functions.v0.Long2LongFunction"""
 
    @staticmethod
    def __wrap(java_value: __Long2LongFunction) -> 'Long2LongFunction':
        return Long2LongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Long2LongFunction):
        """
        Dynamic initializer for Long2LongFunction.
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
    def atan() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.atan()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.atan())

    @staticmethod
    @overload
    def tanh() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.tanh()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.tanh())

    @staticmethod
    @overload
    def sqrt() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.sqrt()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.sqrt())

    @staticmethod
    @overload
    def log1p() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.log1p()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.log1p())

    @staticmethod
    @overload
    def signum() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.signum()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.signum())

    @staticmethod
    @overload
    def tan() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.tan()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.tan())

    @staticmethod
    @overload
    def ceil() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.ceil()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.ceil())

    @staticmethod
    @overload
    def sinh() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.sinh()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.sinh())

    @staticmethod
    @overload
    def round() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.round()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.round())

    @staticmethod
    @overload
    def asin() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.asin()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.asin())

    @staticmethod
    @overload
    def cos() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.cos()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.cos())

    @staticmethod
    @overload
    def cosh() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.cosh()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.cosh())

    @staticmethod
    @overload
    def ulp() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.ulp()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.ulp())

    @staticmethod
    @overload
    def mul(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.mul(long)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.mul(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.scalb(int)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.scalb(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def minus() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.minus()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.minus())

    @staticmethod
    @overload
    def log() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.log()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.log())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @staticmethod
    @overload
    def pow(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.pow(long)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.pow(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.sub(long)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.sub(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def acos() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.acos()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.acos())

    @staticmethod
    @overload
    def or(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.or(long)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.or(__long.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Long') -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.functions.v0.Long2LongFunction.apply(java.lang.Long)"""
        return __transform(super(__Long2LongFunction, self).apply(arg0)).'Long'Value()

    @staticmethod
    @overload
    def sin() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.sin()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.sin())

    @staticmethod
    @overload
    def atan2(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.atan2(long)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.atan2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def log10() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.log10()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.log10())

    @staticmethod
    @overload
    def and(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.and(long)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.and(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mod(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.mod(long)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.mod(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def div(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.div(long)"""
        return Long2LongFunction.__wrap(__Long2LongFunction.div(__long.valueOf(arg0)))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract long dev.ultreon.libs.functions.v0.Long2LongFunction.apply(long)"""
        pass

    @staticmethod
    @overload
    def floor() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.floor()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.floor())

    @staticmethod
    @overload
    def plus() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.plus()"""
        return Long2LongFunction.__wrap(__Long2LongFunction.plus()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Float2FloatFunction
from pyquantum_helper import import_once as __import_once__
from pyquantum_helper import transform as __transform
import dev.ultreon.libs.functions.v0.Float2FloatFunction as __Float2FloatFunction
__Float2FloatFunction = __Float2FloatFunction
import java.lang.Float as __float
try:
    from pycorelibs.functions.v0 import supplier
except ImportError:
    supplier = __import_once__("pycorelibs.functions.v0.supplier")

import java.lang.Float as Float
import java.util.function.Function as __Function
__Function = __Function
from abc import abstractmethod, ABC
import java.lang.Integer as __int
import java.util.function.Function as Function
 
class Float2FloatFunction(ABC, __Function, Function):
    """dev.ultreon.libs.functions.v0.Float2FloatFunction"""
 
    @staticmethod
    def __wrap(java_value: __Float2FloatFunction) -> 'Float2FloatFunction':
        return Float2FloatFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Float2FloatFunction):
        """
        Dynamic initializer for Float2FloatFunction.
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
    def sub(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sub(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.sub(arg0))

    @staticmethod
    @overload
    def acos() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.acos()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.acos())

    @staticmethod
    @overload
    def sub(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sub(float)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.sub(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def pow(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.pow(float)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.pow(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def round() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.round()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.round())

    @staticmethod
    @overload
    def minus() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.minus()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.minus())

    @staticmethod
    @overload
    def atan2(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.atan2(float)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.atan2(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def log1p() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.log1p()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.log1p())

    @staticmethod
    @overload
    def pow(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.pow(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.pow(arg0))

    @abstractmethod
    def apply(self, arg0: float):
        """public abstract float dev.ultreon.libs.functions.v0.Float2FloatFunction.apply(float)"""
        pass

    @staticmethod
    @overload
    def mod(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.mod(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.mod(arg0))

    @staticmethod
    @overload
    def cosh() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.cosh()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.cosh())

    @staticmethod
    @overload
    def tan() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.tan()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.tan())

    @staticmethod
    @overload
    def ceil() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.ceil()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.ceil())

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.scalb(int)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.scalb(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def asin() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.asin()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.asin())

    @staticmethod
    @overload
    def div(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.div(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.div(arg0))

    @staticmethod
    @overload
    def mul(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.mul(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.mul(arg0))

    @staticmethod
    @overload
    def log() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.log()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.log())

    @staticmethod
    @overload
    def atan() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.atan()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.atan())

    @staticmethod
    @overload
    def tanh() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.tanh()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.tanh())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @staticmethod
    @overload
    def ulp() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.ulp()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.ulp())

    @staticmethod
    @overload
    def sqrt() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sqrt()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.sqrt())

    @staticmethod
    @overload
    def plus() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.plus()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.plus())

    @staticmethod
    @overload
    def add(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.add(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.add(arg0))

    @staticmethod
    @overload
    def div(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.div(float)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.div(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def mod(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.mod(float)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.mod(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def add(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.add(float)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.add(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def log10() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.log10()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.log10())

    @staticmethod
    @overload
    def sinh() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sinh()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.sinh())

    @staticmethod
    @overload
    def mul(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.mul(float)"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.mul(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def cos() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.cos()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.cos())

    @overload
    def apply(self, arg0: 'Float') -> 'Float':
        """public default java.lang.Float dev.ultreon.libs.functions.v0.Float2FloatFunction.apply(java.lang.Float)"""
        return __transform(super(__Float2FloatFunction, self).apply(arg0)).'Float'Value()

    @staticmethod
    @overload
    def signum() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.signum()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.signum())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

    @staticmethod
    @overload
    def sin() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sin()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.sin())

    @staticmethod
    @overload
    def floor() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.floor()"""
        return Float2FloatFunction.__wrap(__Float2FloatFunction.floor()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Double2DoubleFunction
from pyquantum_helper import transform as __transform
import java.util.function.Function as __Function
__Function = __Function
import java.lang.Double as __double
from abc import abstractmethod, ABC
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.lang.Double as Double
import dev.ultreon.libs.functions.v0.Double2DoubleFunction as __Double2DoubleFunction
__Double2DoubleFunction = __Double2DoubleFunction
 
class Double2DoubleFunction(ABC, __Function, Function):
    """dev.ultreon.libs.functions.v0.Double2DoubleFunction"""
 
    @staticmethod
    def __wrap(java_value: __Double2DoubleFunction) -> 'Double2DoubleFunction':
        return Double2DoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Double2DoubleFunction):
        """
        Dynamic initializer for Double2DoubleFunction.
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
    def log10() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log10()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.log10())

    @staticmethod
    @overload
    def div(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.div(double)"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.div(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sub(double)"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.sub(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def acos() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.acos()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.acos())

    @staticmethod
    @overload
    def minus() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.minus()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.minus())

    @overload
    def apply(self, arg0: 'Double') -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.functions.v0.Double2DoubleFunction.apply(java.lang.Double)"""
        return __transform(super(__Double2DoubleFunction, self).apply(arg0)).'Double'Value()

    @staticmethod
    @overload
    def ceil() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.ceil()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.ceil())

    @staticmethod
    @overload
    def asin() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.asin()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.asin())

    @staticmethod
    @overload
    def mul(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.mul(double)"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.mul(__double.valueOf(arg0)))

    @abstractmethod
    def apply(self, arg0: float):
        """public abstract double dev.ultreon.libs.functions.v0.Double2DoubleFunction.apply(double)"""
        pass

    @staticmethod
    @overload
    def atan2(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.atan2(double)"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.atan2(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def log() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.log())

    @staticmethod
    @overload
    def log1p() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log1p()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.log1p())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @staticmethod
    @overload
    def mod(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.mod(double)"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.mod(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def signum() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.signum()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.signum())

    @staticmethod
    @overload
    def atan() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.atan()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.atan())

    @staticmethod
    @overload
    def plus() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.plus()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.plus())

    @staticmethod
    @overload
    def pow(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.pow(double)"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.pow(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def round() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.round()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.round())

    @staticmethod
    @overload
    def sinh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sinh()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.sinh())

    @staticmethod
    @overload
    def ulp() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.ulp()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.ulp())

    @staticmethod
    @overload
    def floor() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.floor()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.floor())

    @staticmethod
    @overload
    def add(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.add(double)"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.add(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def sqrt() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sqrt()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.sqrt())

    @staticmethod
    @overload
    def sin() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sin()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.sin())

    @staticmethod
    @overload
    def tan() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.tan()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.tan())

    @staticmethod
    @overload
    def tanh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.tanh()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.tanh())

    @staticmethod
    @overload
    def cosh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.cosh()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.cosh())

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.scalb(int)"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.scalb(__int.valueOf(arg0)))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

    @staticmethod
    @overload
    def cos() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.cos()"""
        return Double2DoubleFunction.__wrap(__Double2DoubleFunction.cos()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Byte2ByteFunction
import dev.ultreon.libs.functions.v0.Byte2ByteFunction as __Byte2ByteFunction
__Byte2ByteFunction = __Byte2ByteFunction
from pyquantum_helper import transform as __transform
import java.lang.Byte as __byte
import java.util.function.Function as __Function
__Function = __Function
from abc import abstractmethod, ABC
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.lang.Byte as Byte
 
class Byte2ByteFunction(ABC, __Function, Function):
    """dev.ultreon.libs.functions.v0.Byte2ByteFunction"""
 
    @staticmethod
    def __wrap(java_value: __Byte2ByteFunction) -> 'Byte2ByteFunction':
        return Byte2ByteFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Byte2ByteFunction):
        """
        Dynamic initializer for Byte2ByteFunction.
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
    def atan2(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.atan2(byte)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.atan2(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def pow(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.pow(byte)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.pow(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.sub(byte)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.sub(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def sin() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.sin()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.sin())

    @staticmethod
    @overload
    def cos() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.cos()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.cos())

    @staticmethod
    @overload
    def acos() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.acos()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.acos())

    @staticmethod
    @overload
    def signum() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.signum()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.signum())

    @staticmethod
    @overload
    def floor() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.floor()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.floor())

    @staticmethod
    @overload
    def and(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.and(byte)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.and(__byte.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Byte') -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.functions.v0.Byte2ByteFunction.apply(java.lang.Byte)"""
        return __transform(super(__Byte2ByteFunction, self).apply(arg0)).'Byte'Value()

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract byte dev.ultreon.libs.functions.v0.Byte2ByteFunction.apply(byte)"""
        pass

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.scalb(int)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.scalb(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def div(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.div(byte)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.div(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def mod(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.mod(byte)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.mod(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def plus() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.plus()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.plus())

    @staticmethod
    @overload
    def tan() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.tan()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.tan())

    @staticmethod
    @overload
    def tanh() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.tanh()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.tanh())

    @staticmethod
    @overload
    def atan() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.atan()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.atan())

    @staticmethod
    @overload
    def mul(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.mul(byte)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.mul(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def round() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.round()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.round())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @staticmethod
    @overload
    def sqrt() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.sqrt()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.sqrt())

    @staticmethod
    @overload
    def ulp() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.ulp()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.ulp())

    @staticmethod
    @overload
    def ceil() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.ceil()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.ceil())

    @staticmethod
    @overload
    def log() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.log()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.log())

    @staticmethod
    @overload
    def log1p() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.log1p()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.log1p())

    @staticmethod
    @overload
    def asin() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.asin()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.asin())

    @staticmethod
    @overload
    def minus() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.minus()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.minus())

    @staticmethod
    @overload
    def sinh() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.sinh()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.sinh())

    @staticmethod
    @overload
    def cosh() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.cosh()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.cosh())

    @staticmethod
    @overload
    def or(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.or(byte)"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.or(__byte.valueOf(arg0)))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

    @staticmethod
    @overload
    def log10() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.log10()"""
        return Byte2ByteFunction.__wrap(__Byte2ByteFunction.log10()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction
from pyquantum_helper import transform as __transform
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction as __BiDouble2DoubleFunction
__BiDouble2DoubleFunction = __BiDouble2DoubleFunction
import java.util.function.BiFunction as BiFunction
import java.lang.Double as Double
 
class BiDouble2DoubleFunction(ABC, __BiFunction, BiFunction):
    """dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction"""
 
    @staticmethod
    def __wrap(java_value: __BiDouble2DoubleFunction) -> 'BiDouble2DoubleFunction':
        return BiDouble2DoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiDouble2DoubleFunction):
        """
        Dynamic initializer for BiDouble2DoubleFunction.
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
    def sub() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.sub()"""
        return BiDouble2DoubleFunction.__wrap(__BiDouble2DoubleFunction.sub())

    @staticmethod
    @overload
    def mod() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.mod()"""
        return BiDouble2DoubleFunction.__wrap(__BiDouble2DoubleFunction.mod())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'.__wrap(super(__BiFunction, self).andThen(arg0))

    @overload
    def apply(self, arg0: 'Double', arg1: 'Double') -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.apply(java.lang.Double,java.lang.Double)"""
        return __transform(super(__BiDouble2DoubleFunction, self).apply(arg0, arg1)).'Double'Value()

    @staticmethod
    @overload
    def mul() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.mul()"""
        return BiDouble2DoubleFunction.__wrap(__BiDouble2DoubleFunction.mul())

    @staticmethod
    @overload
    def scalb() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.scalb()"""
        return BiDouble2DoubleFunction.__wrap(__BiDouble2DoubleFunction.scalb())

    @staticmethod
    @overload
    def add() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.add()"""
        return BiDouble2DoubleFunction.__wrap(__BiDouble2DoubleFunction.add())

    @abstractmethod
    def apply(self, arg0: float, arg1: float):
        """public abstract double dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.apply(double,double)"""
        pass

    @staticmethod
    @overload
    def atan2() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.atan2()"""
        return BiDouble2DoubleFunction.__wrap(__BiDouble2DoubleFunction.atan2())

    @staticmethod
    @overload
    def pow() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.pow()"""
        return BiDouble2DoubleFunction.__wrap(__BiDouble2DoubleFunction.pow())

    @staticmethod
    @overload
    def div() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.div()"""
        return BiDouble2DoubleFunction.__wrap(__BiDouble2DoubleFunction.div()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiShort2ShortFunction
from pyquantum_helper import transform as __transform
import java.lang.Short as Short
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import dev.ultreon.libs.functions.v0.BiShort2ShortFunction as __BiShort2ShortFunction
__BiShort2ShortFunction = __BiShort2ShortFunction
import java.util.function.BiFunction as BiFunction
 
class BiShort2ShortFunction(ABC, __BiFunction, BiFunction):
    """dev.ultreon.libs.functions.v0.BiShort2ShortFunction"""
 
    @staticmethod
    def __wrap(java_value: __BiShort2ShortFunction) -> 'BiShort2ShortFunction':
        return BiShort2ShortFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiShort2ShortFunction):
        """
        Dynamic initializer for BiShort2ShortFunction.
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
    def mul() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.mul()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.mul())

    @overload
    def apply(self, arg0: 'Short', arg1: 'Short') -> 'Short':
        """public default java.lang.Short dev.ultreon.libs.functions.v0.BiShort2ShortFunction.apply(java.lang.Short,java.lang.Short)"""
        return __transform(super(__BiShort2ShortFunction, self).apply(arg0, arg1)).'Short'Value()

    @staticmethod
    @overload
    def sub() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.sub()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.sub())

    @staticmethod
    @overload
    def and() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.and()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.and())

    @staticmethod
    @overload
    def or() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.or()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.or())

    @staticmethod
    @overload
    def div() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.div()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.div())

    @staticmethod
    @overload
    def mod() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.mod()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.mod())

    @staticmethod
    @overload
    def pow() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.pow()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.pow())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'.__wrap(super(__BiFunction, self).andThen(arg0))

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract short dev.ultreon.libs.functions.v0.BiShort2ShortFunction.apply(short,short)"""
        pass

    @staticmethod
    @overload
    def atan2() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.atan2()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.atan2())

    @staticmethod
    @overload
    def add() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.add()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.add())

    @staticmethod
    @overload
    def scalb() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.scalb()"""
        return BiShort2ShortFunction.__wrap(__BiShort2ShortFunction.scalb()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiInt2IntFunction
import dev.ultreon.libs.functions.v0.BiInt2IntFunction as __BiInt2IntFunction
__BiInt2IntFunction = __BiInt2IntFunction
from pyquantum_helper import transform as __transform
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
import java.lang.Integer as Integer
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.util.function.BiFunction as BiFunction
 
class BiInt2IntFunction(ABC, __BiFunction, BiFunction):
    """dev.ultreon.libs.functions.v0.BiInt2IntFunction"""
 
    @staticmethod
    def __wrap(java_value: __BiInt2IntFunction) -> 'BiInt2IntFunction':
        return BiInt2IntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiInt2IntFunction):
        """
        Dynamic initializer for BiInt2IntFunction.
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
    def or() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.or()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.or())

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract int dev.ultreon.libs.functions.v0.BiInt2IntFunction.apply(int,int)"""
        pass

    @staticmethod
    @overload
    def scalb() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.scalb()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.scalb())

    @staticmethod
    @overload
    def div() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.div()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.div())

    @staticmethod
    @overload
    def mul() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.mul()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.mul())

    @staticmethod
    @overload
    def add() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.add()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.add())

    @overload
    def apply(self, arg0: 'Integer', arg1: 'Integer') -> 'Integer':
        """public default java.lang.Integer dev.ultreon.libs.functions.v0.BiInt2IntFunction.apply(java.lang.Integer,java.lang.Integer)"""
        return __transform(super(__BiInt2IntFunction, self).apply(arg0, arg1)).'Integer'Value()

    @staticmethod
    @overload
    def sub() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.sub()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.sub())

    @staticmethod
    @overload
    def mod() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.mod()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.mod())

    @staticmethod
    @overload
    def and() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.and()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.and())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'.__wrap(super(__BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def pow() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.pow()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.pow())

    @staticmethod
    @overload
    def atan2() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.atan2()"""
        return BiInt2IntFunction.__wrap(__BiInt2IntFunction.atan2()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.TriFunction
import dev.ultreon.libs.functions.v0.TriFunction as __TriFunction
__TriFunction = __TriFunction
from abc import abstractmethod, ABC
 
class TriFunction(ABC):
    """dev.ultreon.libs.functions.v0.TriFunction"""
 
    @staticmethod
    def __wrap(java_value: __TriFunction) -> 'TriFunction':
        return TriFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriFunction):
        """
        Dynamic initializer for TriFunction.
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
    def apply(self, arg0: object, arg1: object, arg2: object):
        """public abstract R dev.ultreon.libs.functions.v0.TriFunction.apply(A,B,C)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiFloat2FloatFunction
from pyquantum_helper import transform as __transform
import java.util.function.BiFunction as __BiFunction
__BiFunction = __BiFunction
import java.lang.Float as Float
import dev.ultreon.libs.functions.v0.BiFloat2FloatFunction as __BiFloat2FloatFunction
__BiFloat2FloatFunction = __BiFloat2FloatFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.util.function.BiFunction as BiFunction
 
class BiFloat2FloatFunction(ABC, __BiFunction, BiFunction):
    """dev.ultreon.libs.functions.v0.BiFloat2FloatFunction"""
 
    @staticmethod
    def __wrap(java_value: __BiFloat2FloatFunction) -> 'BiFloat2FloatFunction':
        return BiFloat2FloatFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiFloat2FloatFunction):
        """
        Dynamic initializer for BiFloat2FloatFunction.
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
    def pow() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.pow()"""
        return BiFloat2FloatFunction.__wrap(__BiFloat2FloatFunction.pow())

    @staticmethod
    @overload
    def add() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.add()"""
        return BiFloat2FloatFunction.__wrap(__BiFloat2FloatFunction.add())

    @staticmethod
    @overload
    def scalb() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.scalb()"""
        return BiFloat2FloatFunction.__wrap(__BiFloat2FloatFunction.scalb())

    @overload
    def apply(self, arg0: 'Float', arg1: 'Float') -> 'Float':
        """public default java.lang.Float dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.apply(java.lang.Float,java.lang.Float)"""
        return __transform(super(__BiFloat2FloatFunction, self).apply(arg0, arg1)).'Float'Value()

    @staticmethod
    @overload
    def mul() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.mul()"""
        return BiFloat2FloatFunction.__wrap(__BiFloat2FloatFunction.mul())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'.__wrap(super(__BiFunction, self).andThen(arg0))

    @abstractmethod
    def apply(self, arg0: float, arg1: float):
        """public abstract float dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.apply(float,float)"""
        pass

    @staticmethod
    @overload
    def atan2() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.atan2()"""
        return BiFloat2FloatFunction.__wrap(__BiFloat2FloatFunction.atan2())

    @staticmethod
    @overload
    def sub() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.sub()"""
        return BiFloat2FloatFunction.__wrap(__BiFloat2FloatFunction.sub())

    @staticmethod
    @overload
    def mod() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.mod()"""
        return BiFloat2FloatFunction.__wrap(__BiFloat2FloatFunction.mod())

    @staticmethod
    @overload
    def div() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.div()"""
        return BiFloat2FloatFunction.__wrap(__BiFloat2FloatFunction.div()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Short2ShortFunction
from pyquantum_helper import transform as __transform
import java.lang.Short as Short
import java.lang.Short as __short
import java.util.function.Function as __Function
__Function = __Function
import dev.ultreon.libs.functions.v0.Short2ShortFunction as __Short2ShortFunction
__Short2ShortFunction = __Short2ShortFunction
from abc import abstractmethod, ABC
import java.lang.Integer as __int
import java.util.function.Function as Function
 
class Short2ShortFunction(ABC, __Function, Function):
    """dev.ultreon.libs.functions.v0.Short2ShortFunction"""
 
    @staticmethod
    def __wrap(java_value: __Short2ShortFunction) -> 'Short2ShortFunction':
        return Short2ShortFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Short2ShortFunction):
        """
        Dynamic initializer for Short2ShortFunction.
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
    def apply(self, arg0: int):
        """public abstract short dev.ultreon.libs.functions.v0.Short2ShortFunction.apply(short)"""
        pass

    @staticmethod
    @overload
    def round() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.round()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.round())

    @staticmethod
    @overload
    def minus() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.minus()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.minus())

    @staticmethod
    @overload
    def cosh() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.cosh()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.cosh())

    @staticmethod
    @overload
    def div(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.div(short)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.div(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def atan2(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.atan2(short)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.atan2(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def and(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.and(short)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.and(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def mod(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.mod(short)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.mod(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def cos() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.cos()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.cos())

    @staticmethod
    @overload
    def acos() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.acos()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.acos())

    @staticmethod
    @overload
    def sin() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.sin()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.sin())

    @staticmethod
    @overload
    def log1p() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.log1p()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.log1p())

    @staticmethod
    @overload
    def or(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.or(short)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.or(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def ceil() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.ceil()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.ceil())

    @staticmethod
    @overload
    def ulp() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.ulp()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.ulp())

    @staticmethod
    @overload
    def signum() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.signum()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.signum())

    @staticmethod
    @overload
    def tan() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.tan()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.tan())

    @staticmethod
    @overload
    def plus() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.plus()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.plus())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @staticmethod
    @overload
    def asin() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.asin()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.asin())

    @staticmethod
    @overload
    def atan() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.atan()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.atan())

    @staticmethod
    @overload
    def tanh() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.tanh()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.tanh())

    @staticmethod
    @overload
    def sqrt() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.sqrt()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.sqrt())

    @staticmethod
    @overload
    def log() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.log()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.log())

    @staticmethod
    @overload
    def floor() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.floor()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.floor())

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.scalb(int)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.scalb(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def log10() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.log10()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.log10())

    @overload
    def apply(self, arg0: 'Short') -> 'Short':
        """public default java.lang.Short dev.ultreon.libs.functions.v0.Short2ShortFunction.apply(java.lang.Short)"""
        return __transform(super(__Short2ShortFunction, self).apply(arg0)).'Short'Value()

    @staticmethod
    @overload
    def pow(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.pow(short)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.pow(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.sub(short)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.sub(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def mul(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.mul(short)"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.mul(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def sinh() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.sinh()"""
        return Short2ShortFunction.__wrap(__Short2ShortFunction.sinh())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))